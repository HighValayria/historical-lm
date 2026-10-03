#!/usr/bin/env python
"""Check rolling 1-day / 5-day / 15-day automation schedule."""

from __future__ import annotations

import argparse
import json
from datetime import date, datetime
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STATE_PATH = ROOT / "state" / "automation_state.json"


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

    with TemporaryDirectory() as tmpdir:
        state_path = Path(tmpdir) / "automation_state.json"
        state_path.write_text(json.dumps(base_state), encoding="utf-8")
        assert load_state(state_path)["version"] == 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, default=DEFAULT_STATE_PATH)
    parser.add_argument("--today", help="Override today's date as YYYY-MM-DD.")
    parser.add_argument("--self-test", action="store_true", help="Run built-in assert tests.")
    args = parser.parse_args()

    if args.self_test:
        run_self_tests()
        print("Self-test passed.")
        return 0

    today = parse_day(args.today) if args.today else date.today()
    assert today is not None
    schedule = compute_schedule(load_state(args.state), today)
    print(json.dumps(schedule, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
