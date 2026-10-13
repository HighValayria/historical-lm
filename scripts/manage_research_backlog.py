#!/usr/bin/env python
"""Validate, select, and transition persistent research-backlog tasks."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from tempfile import NamedTemporaryFile


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BACKLOG = ROOT / "state" / "research_backlog.json"
STATUSES = {"proposed", "ready", "running", "completed", "blocked", "failed", "needs_review"}
REQUIRED_FIELDS = {
    "task_id", "track", "objective", "priority", "dependencies", "acceptance_criteria",
    "expected_artifacts", "resource_budget", "status", "evidence_paths", "blockers",
    "attempt_count", "checkpoint",
}


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict) -> None:
    with NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False, newline="\n") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
        temporary = Path(handle.name)
    temporary.replace(path)


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    tasks = data.get("tasks")
    if not isinstance(tasks, list):
        return ["tasks must be a list"]
    ids = [task.get("task_id") for task in tasks]
    if len(ids) != len(set(ids)):
        errors.append("task_id values must be unique")
    known = set(ids)
    for task in tasks:
        task_id = task.get("task_id", "<missing>")
        missing = REQUIRED_FIELDS - set(task)
        if missing:
            errors.append(f"{task_id}: missing fields {sorted(missing)}")
        if task.get("track") not in {"A", "B"}:
            errors.append(f"{task_id}: track must be A or B")
        if task.get("status") not in STATUSES:
            errors.append(f"{task_id}: invalid status {task.get('status')!r}")
        unknown_dependencies = set(task.get("dependencies", [])) - known
        if unknown_dependencies:
            errors.append(f"{task_id}: unknown dependencies {sorted(unknown_dependencies)}")
        if not isinstance(task.get("priority"), int):
            errors.append(f"{task_id}: priority must be an integer (lower is earlier)")
        if not task.get("expected_artifacts") or not task.get("acceptance_criteria"):
            errors.append(f"{task_id}: executable tasks need artifacts and acceptance criteria")
    return errors


def dependencies_complete(task: dict, by_id: dict[str, dict]) -> bool:
    return all(by_id[item]["status"] == "completed" for item in task["dependencies"])


def select_next(data: dict) -> dict | None:
    tasks = data["tasks"]
    by_id = {task["task_id"]: task for task in tasks}
    resumable = [
        task for task in tasks
        if task["status"] == "running"
        and task.get("checkpoint", {}).get("safe_to_resume", False)
        and dependencies_complete(task, by_id)
    ]
    if resumable:
        return sorted(resumable, key=lambda task: (task["priority"], task["task_id"]))[0]
    eligible = [task for task in tasks if task["status"] == "ready" and dependencies_complete(task, by_id)]
    if not eligible:
        return None
    last_track = data.get("scheduler", {}).get("last_claimed_track")
    return sorted(eligible, key=lambda task: (task["priority"], task["track"] == last_track, task["task_id"]))[0]


def find_task(data: dict, task_id: str) -> dict:
    for task in data["tasks"]:
        if task["task_id"] == task_id:
            return task
    raise ValueError(f"Unknown task_id {task_id}")


def timestamp() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def record_failure(task: dict, blockers: list[str], checkpoint: str, repair_available: bool, now: str) -> None:
    if task["status"] != "running":
        raise ValueError("Failure recording requires a running task")
    task["blockers"] = list(dict.fromkeys([*task["blockers"], *blockers]))
    should_block = task["attempt_count"] >= 2 and not repair_available
    task["status"] = "blocked" if should_block else "failed"
    task["checkpoint"] = {
        "updated_at": now,
        "summary": checkpoint or "attempt failed",
        "safe_to_resume": False,
        "repair_available": repair_available,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["validate", "next", "refresh", "claim", "complete", "fail", "retry"])
    parser.add_argument("--backlog", type=Path, default=DEFAULT_BACKLOG)
    parser.add_argument("--task-id")
    parser.add_argument("--checkpoint", default="")
    parser.add_argument("--evidence-path", action="append", default=[])
    parser.add_argument("--blocker", action="append", default=[])
    parser.add_argument("--acceptance-passed", action="store_true")
    parser.add_argument("--repair-available", action="store_true")
    args = parser.parse_args()
    data = read_json(args.backlog)
    errors = validate(data)
    if errors:
        print(json.dumps({"status": "invalid", "errors": errors}, ensure_ascii=False, indent=2))
        return 1
    if args.command == "validate":
        print(json.dumps({"status": "valid", "tasks": len(data["tasks"])}, ensure_ascii=False))
        return 0
    if args.command == "next":
        print(json.dumps({"task": select_next(data)}, ensure_ascii=False, indent=2))
        return 0
    if args.command == "refresh":
        by_id = {task["task_id"]: task for task in data["tasks"]}
        promoted = []
        for task in data["tasks"]:
            if task["status"] == "proposed" and dependencies_complete(task, by_id):
                task["status"] = "ready"
                task["checkpoint"] = {"updated_at": timestamp(), "summary": "dependencies satisfied", "safe_to_resume": False}
                promoted.append(task["task_id"])
        data["updated_at"] = timestamp()
        write_json(args.backlog, data)
        print(json.dumps({"status": "updated", "promoted": promoted}, ensure_ascii=False, indent=2))
        return 0
    if not args.task_id:
        parser.error(f"{args.command} requires --task-id")
    task = find_task(data, args.task_id)
    now = timestamp()
    if args.command == "retry":
        if task["status"] != "failed" or not args.repair_available:
            raise ValueError("Retry requires a failed task and --repair-available")
        task["status"] = "ready"
        task["checkpoint"] = {"updated_at": now, "summary": args.checkpoint or "new repair path recorded", "safe_to_resume": False}
    elif args.command == "claim":
        selected = select_next(data)
        if selected is None or selected["task_id"] != task["task_id"]:
            raise ValueError(f"{task['task_id']} is not the next eligible task")
        if task["status"] != "running":
            task["status"] = "running"
            task["attempt_count"] += 1
        task["checkpoint"] = {"updated_at": now, "summary": args.checkpoint or "claimed", "safe_to_resume": True}
        data.setdefault("scheduler", {})["last_claimed_track"] = task["track"]
    elif args.command == "complete":
        if task["status"] != "running" or not args.acceptance_passed:
            raise ValueError("Completion requires a running task and --acceptance-passed")
        evidence = list(dict.fromkeys([*task["evidence_paths"], *task["expected_artifacts"], *args.evidence_path]))
        missing = [item for item in task["expected_artifacts"] if not (ROOT / item).exists()]
        if missing:
            raise ValueError(f"Expected artifacts do not exist: {missing}")
        task.update({"status": "completed", "evidence_paths": evidence, "checkpoint": {"updated_at": now, "summary": args.checkpoint or "acceptance passed", "safe_to_resume": False}})
    else:
        record_failure(task, args.blocker, args.checkpoint, args.repair_available, now)
    data["updated_at"] = now
    write_json(args.backlog, data)
    print(json.dumps({"status": "updated", "task": task}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
