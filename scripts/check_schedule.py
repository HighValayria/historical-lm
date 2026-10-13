#!/usr/bin/env python
"""Plan rolling Daily / 3-day / 7-day / 14-day research automation.

This module is intentionally read-only. A stage result is persisted only by
``record_automation_result.py`` after the stage's acceptance checks pass.
"""

from __future__ import annotations

import argparse
import json
import os
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STATE_PATH = ROOT / "state" / "automation_state.json"
STAGE_ORDER = ("daily", "tactical", "synthesis", "audit")
INTERVAL_DAYS = {"daily": 1, "tactical": 3, "synthesis": 7, "audit": 14}
MODE_TO_STAGES = {
    "DAILY": ("daily",),
    "TACTICAL": ("tactical",),
    "SYNTHESIS": ("synthesis",),
    "AUDIT": ("audit",),
    "FULL": STAGE_ORDER,
}
LEGACY_MODE_ALIASES = {"FIVE_DAY": "SYNTHESIS", "HALF_MONTH": "AUDIT"}
FORCE_MODES = {"AUTO", *MODE_TO_STAGES, *LEGACY_MODE_ALIASES}


def parse_timestamp(value: str | None, default_tz: timezone = timezone.utc) -> datetime | None:
    if value is None:
        return None
    normalized = value.strip()
    if len(normalized) == 10:
        parsed = datetime.combine(date.fromisoformat(normalized), time.min, tzinfo=default_tz)
    else:
        parsed = datetime.fromisoformat(normalized.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=default_tz)
    return parsed


def iso_timestamp(value: datetime) -> str:
    return value.isoformat(timespec="seconds")


def parse_bool(value: str | None) -> bool | None:
    if value is None:
        return None
    normalized = value.strip().lower()
    if normalized == "true":
        return True
    if normalized == "false":
        return False
    raise ValueError(f"Expected true or false, got {value!r}")


def normalize_force_mode(value: str | None) -> tuple[str, str | None]:
    requested = (value or "AUTO").strip().upper()
    if requested not in FORCE_MODES:
        raise ValueError(f"Unsupported FORCE_MODE {value!r}; expected one of {sorted(FORCE_MODES)}")
    alias = LEGACY_MODE_ALIASES.get(requested)
    return alias or requested, requested if alias else None


def migrate_legacy_state(state: dict, anchor: datetime) -> dict:
    """Return a v2 view without mutating or writing the supplied state.

    Legacy Daily history is preserved. Five-Day and Half-Month history is
    retained as migration evidence, but it does not seed success timestamps for
    the materially different 7-day synthesis and 14-day audit stages.
    """
    if state.get("version") == 2 and "stages" in state:
        return json.loads(json.dumps(state))

    anchor_text = iso_timestamp(anchor)
    daily_last = state.get("last_daily")
    migrated = {
        "version": 2,
        "timezone": "Asia/Shanghai",
        "schedule_anchor": anchor_text,
        "stages": {},
        "legacy_migration": {
            "source_version": state.get("version", 1),
            "migrated_at": anchor_text,
            "old_1_5_15_state": state,
            "policy": (
                "Daily history is preserved. Five-Day and Half-Month history is evidence only; "
                "new Tactical/Synthesis/Audit clocks start at schedule_anchor."
            ),
        },
    }
    for stage in STAGE_ORDER:
        migrated["stages"][stage] = {
            "interval_days": INTERVAL_DAYS[stage],
            "last_successful": None,
            "run_count": 0,
            "not_before": iso_timestamp(anchor + timedelta(days=INTERVAL_DAYS[stage])) if stage != "daily" else anchor_text,
        }
    migrated["stages"]["daily"]["last_successful"] = (
        iso_timestamp(parse_timestamp(daily_last, anchor.tzinfo or timezone.utc)) if daily_last else None
    )
    migrated["stages"]["daily"]["run_count"] = int(state.get("daily_run_count", 0))
    return migrated


def stage_due(stage: str, stage_state: dict, anchor: datetime, now: datetime) -> bool:
    if stage == "daily":
        return True
    last_successful = parse_timestamp(stage_state.get("last_successful"), now.tzinfo or timezone.utc)
    not_before = parse_timestamp(stage_state.get("not_before"), now.tzinfo or timezone.utc)
    due_at = anchor + timedelta(days=INTERVAL_DAYS[stage])
    if not_before is not None:
        due_at = max(due_at, not_before)
    if last_successful is not None:
        due_at = max(due_at, last_successful + timedelta(days=INTERVAL_DAYS[stage]))
    return now >= due_at


def compute_schedule(state: dict, now: datetime) -> dict[str, bool]:
    normalized = migrate_legacy_state(state, now)
    anchor = parse_timestamp(normalized["schedule_anchor"], now.tzinfo or timezone.utc)
    assert anchor is not None
    return {
        stage: stage_due(stage, normalized["stages"][stage], anchor, now)
        for stage in STAGE_ORDER
    }


def compute_run_plan(
    state: dict,
    now: datetime,
    force_mode: str = "AUTO",
    update_schedule: bool | None = None,
) -> dict:
    mode, legacy_alias = normalize_force_mode(force_mode)
    normalized = migrate_legacy_state(state, now)
    automatic = compute_schedule(normalized, now)
    selected = tuple(stage for stage in STAGE_ORDER if automatic[stage]) if mode == "AUTO" else MODE_TO_STAGES[mode]
    should_update = True if mode == "AUTO" else bool(update_schedule) if update_schedule is not None else False
    plan = {
        "force_mode": mode,
        "legacy_mode_alias": legacy_alias,
        "update_schedule": should_update,
        "ordered_stages": list(selected),
        "schedule_anchor": normalized["schedule_anchor"],
        "due": automatic,
    }
    for stage in STAGE_ORDER:
        plan[f"run_{stage}"] = stage in selected
        plan[f"update_{stage}_state"] = stage in selected and should_update
    return plan


def load_state(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE_PATH)
    parser.add_argument("--now", help="Override current time with an ISO-8601 timestamp.")
    parser.add_argument("--today", help="Deprecated date-only alias for --now (YYYY-MM-DD).")
    parser.add_argument("--force-mode", choices=sorted(FORCE_MODES), default=None)
    parser.add_argument("--update-schedule", choices=["true", "false"], default=None)
    args = parser.parse_args()

    raw_now = args.now or args.today
    now = parse_timestamp(raw_now, timezone(timedelta(hours=8))) if raw_now else datetime.now().astimezone()
    assert now is not None
    force_mode = args.force_mode or os.environ.get("FORCE_MODE") or "AUTO"
    update_schedule_value = args.update_schedule
    if update_schedule_value is None:
        update_schedule_value = os.environ.get("UPDATE_SCHEDULE")
    plan = compute_run_plan(load_state(args.state), now, force_mode, parse_bool(update_schedule_value))
    print(json.dumps(plan, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
