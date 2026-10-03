#!/usr/bin/env python
"""Check rolling 1-day / 5-day / 15-day automation schedule."""

from __future__ import annotations

import argparse
import json
import os
from datetime import date, datetime
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STATE_PATH = ROOT / "state" / "automation_state.json"
FORCE_MODES = {"AUTO", "DAILY", "FIVE_DAY", "HALF_MONTH", "FULL"}


def parse_day(value: str | None) -> date | None:
    if value is None:
        return None
    return datetime.strptime(value, "%Y-%m-%d").date()


def days_since(value: str | None, today: date) -> int | None:
    previous = parse_day(value)
    if previous is None:
        return None
    return (today - previous).days


def compute_schedule(state: dict, today: date) -> dict:
    five_day_gap = days_since(state.get("last_five_day"), today)
    half_month_gap = days_since(state.get("last_half_month"), today)

    return {
        "run_daily": True,
        "run_five_day": five_day_gap is None or five_day_gap >= 5,
        "run_half_month": half_month_gap is None or half_month_gap >= 15,
    }


def parse_bool(value: str | None) -> bool | None:
    if value is None:
        return None
    normalized = value.strip().lower()
    if normalized == "true":
        return True
    if normalized == "false":
        return False
    raise ValueError(f"Expected true or false, got {value!r}")


def normalize_force_mode(value: str | None) -> str:
    mode = (value or "AUTO").strip().upper()
    if mode not in FORCE_MODES:
        raise ValueError(f"Unsupported FORCE_MODE {value!r}; expected one of {sorted(FORCE_MODES)}")
    return mode


def compute_run_plan(
    state: dict,
    today: date,
    force_mode: str = "AUTO",
    update_schedule: bool | None = None,
) -> dict:
    mode = normalize_force_mode(force_mode)
    auto_schedule = compute_schedule(state, today)

    if mode == "AUTO":
        run_daily = auto_schedule["run_daily"]
        run_five_day = auto_schedule["run_five_day"]
        run_half_month = auto_schedule["run_half_month"]
        update_due_state = True
    else:
        run_daily = mode in {"DAILY", "FULL"}
        run_five_day = mode in {"FIVE_DAY", "FULL"}
        run_half_month = mode in {"HALF_MONTH", "FULL"}
        update_due_state = bool(update_schedule) if update_schedule is not None else False

    return {
        "force_mode": mode,
        "update_schedule": update_due_state,
        "run_daily": run_daily,
        "run_five_day": run_five_day,
        "run_half_month": run_half_month,
        "update_daily_state": run_daily and update_due_state,
        "update_five_day_state": run_five_day and update_due_state,
        "update_half_month_state": run_half_month and update_due_state,
    }


def load_state(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def run_self_tests() -> None:
    base_state = {
        "version": 1,
        "last_daily": None,
        "last_five_day": None,
        "last_half_month": None,
        "daily_run_count": 0,
        "five_day_run_count": 0,
        "half_month_run_count": 0,
        "last_successful_run": None,
    }
    today = date(2026, 10, 15)

    assert compute_schedule(base_state, today) == {
        "run_daily": True,
        "run_five_day": True,
        "run_half_month": True,
    }

    state = dict(base_state, last_five_day="2026-10-14", last_half_month="2026-10-14")
    assert compute_schedule(state, today) == {
        "run_daily": True,
        "run_five_day": False,
        "run_half_month": False,
    }

    state = dict(base_state, last_five_day="2026-10-10", last_half_month="2026-10-14")
    assert compute_schedule(state, today) == {
        "run_daily": True,
        "run_five_day": True,
        "run_half_month": False,
    }

    state = dict(base_state, last_five_day="2026-10-10", last_half_month="2026-09-30")
    assert compute_schedule(state, today) == {
        "run_daily": True,
        "run_five_day": True,
        "run_half_month": True,
    }

    state = dict(base_state, last_five_day="2026-10-09", last_half_month="2026-10-14")
    assert compute_schedule(state, today) == {
        "run_daily": True,
        "run_five_day": True,
        "run_half_month": False,
    }

    state = dict(base_state, last_five_day="2026-10-14", last_half_month="2026-09-28")
    assert compute_schedule(state, today) == {
        "run_daily": True,
        "run_five_day": False,
        "run_half_month": True,
    }

    state = dict(base_state, last_five_day="2026-10-14", last_half_month="2026-09-29")
    assert compute_schedule(state, today) == {
        "run_daily": True,
        "run_five_day": False,
        "run_half_month": True,
    }

    current_state = dict(base_state, last_daily="2026-10-14", last_five_day="2026-10-14", last_half_month="2026-10-14")
    assert compute_run_plan(current_state, today, "AUTO") == {
        "force_mode": "AUTO",
        "update_schedule": True,
        "run_daily": True,
        "run_five_day": False,
        "run_half_month": False,
        "update_daily_state": True,
        "update_five_day_state": False,
        "update_half_month_state": False,
    }
    assert compute_run_plan(current_state, today, "DAILY") == {
        "force_mode": "DAILY",
        "update_schedule": False,
        "run_daily": True,
        "run_five_day": False,
        "run_half_month": False,
        "update_daily_state": False,
        "update_five_day_state": False,
        "update_half_month_state": False,
    }
    assert compute_run_plan(current_state, today, "FIVE_DAY") == {
        "force_mode": "FIVE_DAY",
        "update_schedule": False,
        "run_daily": False,
        "run_five_day": True,
        "run_half_month": False,
        "update_daily_state": False,
        "update_five_day_state": False,
        "update_half_month_state": False,
    }
    assert compute_run_plan(current_state, today, "HALF_MONTH") == {
        "force_mode": "HALF_MONTH",
        "update_schedule": False,
        "run_daily": False,
        "run_five_day": False,
        "run_half_month": True,
        "update_daily_state": False,
        "update_five_day_state": False,
        "update_half_month_state": False,
    }
    assert compute_run_plan(current_state, today, "FULL") == {
        "force_mode": "FULL",
        "update_schedule": False,
        "run_daily": True,
        "run_five_day": True,
        "run_half_month": True,
        "update_daily_state": False,
        "update_five_day_state": False,
        "update_half_month_state": False,
    }
    assert compute_run_plan(current_state, today, "FULL", update_schedule=True) == {
        "force_mode": "FULL",
        "update_schedule": True,
        "run_daily": True,
        "run_five_day": True,
        "run_half_month": True,
        "update_daily_state": True,
        "update_five_day_state": True,
        "update_half_month_state": True,
    }

    with TemporaryDirectory() as tmpdir:
        state_path = Path(tmpdir) / "automation_state.json"
        state_path.write_text(json.dumps(base_state), encoding="utf-8")
        assert load_state(state_path)["version"] == 1
        before = state_path.read_text(encoding="utf-8")
        assert compute_run_plan(load_state(state_path), today, "FIVE_DAY")["update_five_day_state"] is False
        after = state_path.read_text(encoding="utf-8")
        assert after == before


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE_PATH)
    parser.add_argument("--today", help="Override today's date as YYYY-MM-DD.")
    parser.add_argument("--force-mode", choices=sorted(FORCE_MODES), default=None)
    parser.add_argument("--update-schedule", choices=["true", "false"], default=None)
    parser.add_argument("--self-test", action="store_true", help="Run built-in assert tests.")
    args = parser.parse_args()

    if args.self_test:
        run_self_tests()
        print("Self-test passed.")
        return 0

    today = parse_day(args.today) if args.today else date.today()
    assert today is not None
    force_mode = args.force_mode or os.environ.get("FORCE_MODE") or "AUTO"
    update_schedule_value = args.update_schedule
    if update_schedule_value is None:
        update_schedule_value = os.environ.get("UPDATE_SCHEDULE")
    schedule = compute_run_plan(load_state(args.state), today, force_mode, parse_bool(update_schedule_value))
    print(json.dumps(schedule, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
