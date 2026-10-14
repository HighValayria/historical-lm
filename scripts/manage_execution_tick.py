#!/usr/bin/env python
"""Claim and finish one bounded five-hour research execution tick.

The tick clock is independent from the 1/3/7/14-day research-review clocks.
Automatic runs use a fixed Asia/Shanghai anchor and skip stale or duplicate
slots.  Manual runs acquire the same repository lock but never advance the
automatic slot state.
"""

from __future__ import annotations

import argparse
import json
import uuid
from datetime import datetime, timedelta
from pathlib import Path
from tempfile import NamedTemporaryFile
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STATE_PATH = ROOT / "state" / "execution_tick_state.json"
DEFAULT_LOCK_PATH = ROOT / ".git" / "research_execution.lock"
SHANGHAI = ZoneInfo("Asia/Shanghai")
DEFAULT_ANCHOR = datetime(2026, 10, 14, 9, 0, tzinfo=SHANGHAI)
DEFAULT_INTERVAL = timedelta(hours=5)
DEFAULT_LATE_TOLERANCE = timedelta(minutes=30)
DEFAULT_LOCK_LEASE = timedelta(minutes=120)


def parse_timestamp(value: str | None) -> datetime | None:
    if value is None:
        return None
    parsed = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=SHANGHAI)
    return parsed.astimezone(SHANGHAI)


def iso_timestamp(value: datetime) -> str:
    return value.astimezone(SHANGHAI).isoformat(timespec="seconds")


def slot_at_or_before(
    now: datetime,
    anchor: datetime = DEFAULT_ANCHOR,
    interval: timedelta = DEFAULT_INTERVAL,
) -> datetime | None:
    now_local = now.astimezone(SHANGHAI)
    anchor_local = anchor.astimezone(SHANGHAI)
    if now_local < anchor_local:
        return None
    elapsed = now_local - anchor_local
    slot_number = int(elapsed.total_seconds() // interval.total_seconds())
    return anchor_local + slot_number * interval


def slot_id(value: datetime) -> str:
    return value.astimezone(SHANGHAI).strftime("%Y%m%dT%H%M%S%z")


def default_state() -> dict:
    return {
        "version": 1,
        "timezone": "Asia/Shanghai",
        "anchor": iso_timestamp(DEFAULT_ANCHOR),
        "interval_hours": 5,
        "late_tolerance_minutes": 30,
        "missed_slot_policy": "SKIP_MISSED_SLOTS",
        "last_valid_execution_slot": None,
        "last_successful_research_task_at": None,
        "completed_slots": [],
        "current_task_checkpoint": None,
        "execution_lock": {
            "status": "unlocked",
            "run_id": None,
            "slot_id": None,
            "acquired_at": None,
            "heartbeat_at": None,
        },
    }


def load_state(path: Path) -> dict:
    if not path.exists():
        return default_state()
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def atomic_write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False, newline="\n") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        temporary = Path(handle.name)
    temporary.replace(path)


def _read_lock(path: Path) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def _lock_is_active(lock: dict | None, now: datetime, lease: timedelta) -> bool:
    if not lock:
        return False
    heartbeat = parse_timestamp(lock.get("heartbeat_at") or lock.get("acquired_at"))
    return heartbeat is not None and now.astimezone(SHANGHAI) - heartbeat <= lease


def _create_lock(path: Path, lock: dict) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(lock, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
    except FileExistsError:
        return False
    return True


def _remove_lock(path: Path, run_id: str) -> None:
    lock = _read_lock(path)
    if lock and lock.get("run_id") != run_id:
        raise ValueError("Execution lock belongs to another run")
    try:
        path.unlink()
    except FileNotFoundError:
        pass


def claim_tick(
    state_path: Path,
    lock_path: Path,
    now: datetime,
    scheduled_at: datetime | None = None,
    run_id: str | None = None,
    manual: bool = False,
    lease: timedelta = DEFAULT_LOCK_LEASE,
) -> dict:
    now_local = now.astimezone(SHANGHAI)
    state = load_state(state_path)
    anchor = parse_timestamp(state.get("anchor")) or DEFAULT_ANCHOR
    interval = timedelta(hours=int(state.get("interval_hours", 5)))
    tolerance = timedelta(minutes=int(state.get("late_tolerance_minutes", 30)))

    if manual:
        chosen_slot = None
        chosen_slot_id = f"manual:{run_id or uuid.uuid4().hex}"
    else:
        chosen_slot = scheduled_at.astimezone(SHANGHAI) if scheduled_at else slot_at_or_before(now_local, anchor, interval)
        if chosen_slot is None:
            return {"decision": "skip", "reason": "before_anchor"}
        inferred = slot_at_or_before(chosen_slot, anchor, interval)
        if inferred != chosen_slot:
            return {"decision": "skip", "reason": "not_a_scheduled_slot", "scheduled_at": iso_timestamp(chosen_slot)}
        if now_local < chosen_slot:
            return {"decision": "skip", "reason": "scheduled_in_future", "scheduled_at": iso_timestamp(chosen_slot)}
        if now_local - chosen_slot > tolerance:
            return {
                "decision": "skip",
                "reason": "stale_slot",
                "scheduled_at": iso_timestamp(chosen_slot),
                "late_by_minutes": int((now_local - chosen_slot).total_seconds() // 60),
            }
        chosen_slot_id = slot_id(chosen_slot)
        if chosen_slot_id in state.get("completed_slots", []):
            return {"decision": "skip", "reason": "slot_already_completed", "slot_id": chosen_slot_id}

    existing = _read_lock(lock_path)
    if _lock_is_active(existing, now_local, lease):
        return {
            "decision": "skip",
            "reason": "active_execution_lock",
            "active_run_id": existing.get("run_id"),
            "active_slot_id": existing.get("slot_id"),
        }
    if existing:
        try:
            lock_path.unlink()
        except FileNotFoundError:
            pass

    actual_run_id = run_id or f"tick-{chosen_slot_id}-{uuid.uuid4().hex[:8]}"
    lock = {
        "run_id": actual_run_id,
        "slot_id": chosen_slot_id,
        "manual": manual,
        "acquired_at": iso_timestamp(now_local),
        "heartbeat_at": iso_timestamp(now_local),
        "lease_minutes": int(lease.total_seconds() // 60),
    }
    if not _create_lock(lock_path, lock):
        winner = _read_lock(lock_path) or {}
        return {
            "decision": "skip",
            "reason": "concurrent_lock_race",
            "active_run_id": winner.get("run_id"),
        }

    state["execution_lock"] = {"status": "locked", **lock}
    state["current_task_checkpoint"] = state.get("current_task_checkpoint")
    if not manual:
        state["last_valid_execution_slot"] = iso_timestamp(chosen_slot)
    atomic_write_json(state_path, state)
    return {
        "decision": "run",
        "run_id": actual_run_id,
        "slot_id": chosen_slot_id,
        "scheduled_at": iso_timestamp(chosen_slot) if chosen_slot else None,
        "manual": manual,
        "max_tasks": 3,
        "max_minutes": 90,
    }


def checkpoint_tick(
    state_path: Path,
    lock_path: Path,
    run_id: str,
    checkpoint: str,
    now: datetime,
) -> dict:
    state = load_state(state_path)
    lock = _read_lock(lock_path)
    if not lock or lock.get("run_id") != run_id:
        raise ValueError("No execution lock held by this run")
    timestamp = iso_timestamp(now)
    lock["heartbeat_at"] = timestamp
    lock_path.write_text(json.dumps(lock, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    state["current_task_checkpoint"] = {
        "run_id": run_id,
        "slot_id": lock.get("slot_id"),
        "updated_at": timestamp,
        "value": checkpoint,
    }
    state["execution_lock"] = {"status": "locked", **lock}
    atomic_write_json(state_path, state)
    return {"status": "checkpointed", "run_id": run_id, "checkpoint": checkpoint}


def finish_tick(
    state_path: Path,
    lock_path: Path,
    run_id: str,
    result: str,
    now: datetime,
    checkpoint: str = "",
    research_task_successful: bool = False,
) -> dict:
    state = load_state(state_path)
    lock = _read_lock(lock_path)
    if not lock or lock.get("run_id") != run_id:
        raise ValueError("No execution lock held by this run")
    timestamp = iso_timestamp(now)
    manual = bool(lock.get("manual"))
    completed = state.setdefault("completed_slots", [])
    if result == "success" and not manual and lock["slot_id"] not in completed:
        completed.append(lock["slot_id"])
        state["completed_slots"] = completed[-256:]
    if result == "success" and research_task_successful:
        state["last_successful_research_task_at"] = timestamp
    state["current_task_checkpoint"] = None if result == "success" else {
        "run_id": run_id,
        "slot_id": lock.get("slot_id"),
        "updated_at": timestamp,
        "value": checkpoint,
        "result": result,
    }
    state["execution_lock"] = {
        "status": "unlocked",
        "run_id": None,
        "slot_id": None,
        "acquired_at": None,
        "heartbeat_at": None,
        "last_released_at": timestamp,
        "last_result": result,
    }
    atomic_write_json(state_path, state)
    _remove_lock(lock_path, run_id)
    return {"status": "finished", "run_id": run_id, "result": result, "manual": manual}


def parse_bool(value: str) -> bool:
    normalized = value.lower()
    if normalized not in {"true", "false"}:
        raise argparse.ArgumentTypeError("expected true or false")
    return normalized == "true"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE_PATH)
    parser.add_argument("--lock", type=Path, default=DEFAULT_LOCK_PATH)
    subparsers = parser.add_subparsers(dest="action", required=True)

    claim = subparsers.add_parser("claim")
    claim.add_argument("--now")
    claim.add_argument("--scheduled-at")
    claim.add_argument("--run-id")
    claim.add_argument("--manual", action="store_true")

    checkpoint = subparsers.add_parser("checkpoint")
    checkpoint.add_argument("--run-id", required=True)
    checkpoint.add_argument("--value", required=True)
    checkpoint.add_argument("--at")

    finish = subparsers.add_parser("finish")
    finish.add_argument("--run-id", required=True)
    finish.add_argument("--result", choices=["success", "failed", "interrupted"], required=True)
    finish.add_argument("--at")
    finish.add_argument("--checkpoint", default="")
    finish.add_argument("--research-task-successful", type=parse_bool, default=False)

    args = parser.parse_args()
    if args.action == "claim":
        now = parse_timestamp(args.now) or datetime.now(SHANGHAI)
        scheduled_at = parse_timestamp(args.scheduled_at)
        result = claim_tick(args.state, args.lock, now, scheduled_at, args.run_id, args.manual)
    elif args.action == "checkpoint":
        now = parse_timestamp(args.at) or datetime.now(SHANGHAI)
        result = checkpoint_tick(args.state, args.lock, args.run_id, args.value, now)
    else:
        now = parse_timestamp(args.at) or datetime.now(SHANGHAI)
        result = finish_tick(
            args.state,
            args.lock,
            args.run_id,
            args.result,
            now,
            args.checkpoint,
            args.research_task_successful,
        )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
