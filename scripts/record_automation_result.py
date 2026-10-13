#!/usr/bin/env python
"""Persist one automation-stage lifecycle event with success-gated scheduling."""

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from tempfile import NamedTemporaryFile

from check_schedule import STAGE_ORDER, iso_timestamp, load_state, parse_bool, parse_timestamp


ROOT = Path(__file__).resolve().parents[1]
AUTOMATION_STATE = ROOT / "state" / "automation_state.json"
EXECUTION_STATE = ROOT / "state" / "research_execution_state.json"
EXECUTION_HISTORY = ROOT / "state" / "execution_history.json"


def atomic_write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False, newline="\n") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        temporary = Path(handle.name)
    temporary.replace(path)


def load_or_default(path: Path, default: dict) -> dict:
    return load_state(path) if path.exists() else default


def resolve_artifacts(root: Path, artifacts: list[str]) -> list[str]:
    normalized = []
    for artifact in artifacts:
        candidate = (root / artifact).resolve() if not Path(artifact).is_absolute() else Path(artifact).resolve()
        try:
            relative = candidate.relative_to(root.resolve())
        except ValueError as exc:
            raise ValueError(f"Artifact is outside repository: {artifact}") from exc
        if not candidate.exists():
            raise ValueError(f"Artifact does not exist: {artifact}")
        normalized.append(relative.as_posix())
    return normalized


def record(args: argparse.Namespace) -> dict:
    now = parse_timestamp(args.at) if args.at else datetime.now().astimezone()
    assert now is not None
    timestamp = iso_timestamp(now)
    root = args.root.resolve()
    execution_path = root / args.execution_state
    history_path = root / args.history
    automation_path = root / args.automation_state
    execution = load_or_default(
        execution_path,
        {"version": 1, "current_run_id": None, "stages": {stage: {} for stage in STAGE_ORDER}},
    )
    history = load_or_default(history_path, {"version": 1, "events": []})
    event_key = f"{args.run_id}:{args.stage}:{args.action}"
    existing = next((event for event in history["events"] if event["event_key"] == event_key), None)
    if existing:
        return {"status": "idempotent_noop", "event": existing}

    stage_state = execution.setdefault("stages", {}).setdefault(args.stage, {})
    if args.action == "start":
        stage_state.update(
            {
                "run_id": args.run_id,
                "status": "running",
                "checkpoint": args.checkpoint,
                "started_at": timestamp,
                "finished_at": None,
                "artifacts": [],
                "errors": [],
            }
        )
        execution["current_run_id"] = args.run_id
        event = {
            "event_key": event_key,
            "run_id": args.run_id,
            "stage": args.stage,
            "action": "start",
            "timestamp": timestamp,
            "checkpoint": args.checkpoint,
        }
    else:
        if stage_state.get("run_id") != args.run_id or stage_state.get("status") != "running":
            raise ValueError(f"Stage {args.stage} is not running under run_id {args.run_id}")
        if args.result == "success" and not args.acceptance_passed:
            raise ValueError("A successful finish requires --acceptance-passed true")
        artifacts = resolve_artifacts(root, args.artifact)
        if args.result == "success" and not artifacts:
            raise ValueError("A successful finish requires at least one existing --artifact")
        stage_state.update(
            {
                "status": "completed" if args.result == "success" else args.result,
                "checkpoint": args.checkpoint,
                "finished_at": timestamp,
                "artifacts": artifacts,
                "errors": args.error,
            }
        )
        event = {
            "event_key": event_key,
            "run_id": args.run_id,
            "stage": args.stage,
            "action": "finish",
            "result": args.result,
            "timestamp": timestamp,
            "checkpoint": args.checkpoint,
            "artifacts": artifacts,
            "errors": args.error,
            "acceptance_passed": args.acceptance_passed,
            "schedule_updated": False,
        }
        if args.result == "success" and args.update_schedule:
            automation = load_state(automation_path)
            target = automation["stages"][args.stage]
            target["last_successful"] = timestamp
            target["run_count"] = int(target.get("run_count", 0)) + 1
            automation["last_successful_run"] = timestamp
            atomic_write_json(automation_path, automation)
            event["schedule_updated"] = True
        if all(item.get("status") != "running" for item in execution["stages"].values()):
            execution["current_run_id"] = None

    history["events"].append(event)
    atomic_write_json(execution_path, execution)
    atomic_write_json(history_path, history)
    return {"status": "recorded", "event": event}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["start", "finish"])
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--stage", required=True, choices=STAGE_ORDER)
    parser.add_argument("--result", choices=["success", "failed", "interrupted"], default="success")
    parser.add_argument("--at", help="ISO-8601 event time")
    parser.add_argument("--checkpoint", default="")
    parser.add_argument("--artifact", action="append", default=[])
    parser.add_argument("--error", action="append", default=[])
    parser.add_argument("--acceptance-passed", type=parse_bool, default=False)
    parser.add_argument("--update-schedule", type=parse_bool, default=False)
    parser.add_argument("--automation-state", default="state/automation_state.json")
    parser.add_argument("--execution-state", default="state/research_execution_state.json")
    parser.add_argument("--history", default="state/execution_history.json")
    args = parser.parse_args()
    if args.action == "start" and (args.artifact or args.error):
        parser.error("start does not accept --artifact or --error")
    result = record(args)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
