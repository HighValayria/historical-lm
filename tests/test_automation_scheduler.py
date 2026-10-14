from __future__ import annotations

import json
import sys
import tempfile
import unittest
from argparse import Namespace
from datetime import datetime, timezone, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_schedule import compute_run_plan, compute_schedule, migrate_legacy_state  # noqa: E402
from manage_execution_tick import (  # noqa: E402
    claim_tick,
    default_state as tick_state,
    finish_tick,
    slot_at_or_before,
    slot_id,
)
from record_automation_result import record  # noqa: E402


TZ8 = timezone(timedelta(hours=8))


def dt(value: str) -> datetime:
    return datetime.fromisoformat(value)


def state(anchor: str = "2026-10-13T00:00:00+08:00") -> dict:
    return {
        "version": 2,
        "timezone": "Asia/Shanghai",
        "schedule_anchor": anchor,
        "stages": {
            "daily": {"interval_days": 1, "last_successful": anchor, "run_count": 10, "not_before": anchor},
            "tactical": {"interval_days": 3, "last_successful": None, "run_count": 0, "not_before": "2026-10-16T00:00:00+08:00"},
            "synthesis": {"interval_days": 7, "last_successful": None, "run_count": 0, "not_before": "2026-10-20T00:00:00+08:00"},
            "audit": {"interval_days": 14, "last_successful": None, "run_count": 0, "not_before": "2026-10-27T00:00:00+08:00"},
        },
    }


class ScheduleTests(unittest.TestCase):
    def test_first_initialization_does_not_run_new_stages(self) -> None:
        self.assertEqual(compute_run_plan(state(), dt("2026-10-13T12:00:00+08:00"))["ordered_stages"], [])

    def test_radar_runs_at_most_once_per_24_hours(self) -> None:
        current = state()
        current["stages"]["daily"]["last_successful"] = "2026-10-14T09:10:34+08:00"
        self.assertFalse(compute_schedule(current, dt("2026-10-15T09:10:33+08:00"))["daily"])
        self.assertTrue(compute_schedule(current, dt("2026-10-15T09:10:34+08:00"))["daily"])

    def test_five_hour_ticks_do_not_accelerate_research_cycles(self) -> None:
        current = state()
        current["stages"]["daily"]["last_successful"] = "2026-10-14T09:10:34+08:00"
        for tick in ("2026-10-14T14:00:00+08:00", "2026-10-14T19:00:00+08:00", "2026-10-15T00:00:00+08:00"):
            due = compute_schedule(current, dt(tick))
            self.assertFalse(due["daily"])
            self.assertFalse(due["tactical"])
            self.assertFalse(due["synthesis"])
            self.assertFalse(due["audit"])

    def test_3_7_14_day_due_boundaries(self) -> None:
        current = state()
        self.assertTrue(compute_schedule(current, dt("2026-10-16T00:00:00+08:00"))["tactical"])
        self.assertFalse(compute_schedule(current, dt("2026-10-19T23:59:59+08:00"))["synthesis"])
        self.assertTrue(compute_schedule(current, dt("2026-10-20T00:00:00+08:00"))["synthesis"])
        self.assertTrue(compute_schedule(current, dt("2026-10-27T00:00:00+08:00"))["audit"])

    def test_cross_month_and_year(self) -> None:
        current = state("2026-12-25T00:00:00+08:00")
        current["stages"]["tactical"]["not_before"] = "2026-12-28T00:00:00+08:00"
        current["stages"]["synthesis"]["not_before"] = "2027-01-01T00:00:00+08:00"
        current["stages"]["audit"]["not_before"] = "2027-01-08T00:00:00+08:00"
        self.assertTrue(compute_schedule(current, dt("2027-01-08T00:00:00+08:00"))["audit"])

    def test_missed_runs_are_selected_once_not_multiplied(self) -> None:
        plan = compute_run_plan(state(), dt("2026-11-20T12:00:00+08:00"))
        self.assertEqual(plan["ordered_stages"], ["daily", "tactical", "synthesis", "audit"])

    def test_same_day_success_prevents_repeating_periodic_stage(self) -> None:
        current = state()
        current["stages"]["tactical"]["last_successful"] = "2026-10-16T09:00:00+08:00"
        plan = compute_run_plan(current, dt("2026-10-16T18:00:00+08:00"))
        self.assertEqual(plan["ordered_stages"], ["daily"])

    def test_manual_modes_and_legacy_aliases(self) -> None:
        now = dt("2026-10-13T12:00:00+08:00")
        tactical = compute_run_plan(state(), now, "TACTICAL")
        self.assertEqual(tactical["ordered_stages"], ["tactical"])
        self.assertFalse(tactical["update_tactical_state"])
        full = compute_run_plan(state(), now, "FULL", True)
        self.assertEqual(full["ordered_stages"], ["daily", "tactical", "synthesis", "audit"])
        self.assertTrue(full["update_audit_state"])
        legacy = compute_run_plan(state(), now, "FIVE_DAY")
        self.assertEqual(legacy["force_mode"], "SYNTHESIS")
        self.assertEqual(legacy["legacy_mode_alias"], "FIVE_DAY")

    def test_legacy_state_migration_preserves_evidence_not_new_successes(self) -> None:
        legacy = {
            "version": 1, "last_daily": "2026-10-13", "last_five_day": "2026-10-09",
            "last_half_month": "2026-10-04", "daily_run_count": 10,
            "five_day_run_count": 2, "half_month_run_count": 1,
        }
        migrated = migrate_legacy_state(legacy, dt("2026-10-13T00:00:00+08:00"))
        self.assertEqual(migrated["stages"]["daily"]["run_count"], 10)
        self.assertIsNone(migrated["stages"]["synthesis"]["last_successful"])
        self.assertEqual(migrated["legacy_migration"]["old_1_5_15_state"]["five_day_run_count"], 2)

    def test_failure_does_not_update_schedule_and_success_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT / "tests") as directory:
            root = Path(directory)
            (root / "state").mkdir()
            (root / "reports").mkdir()
            (root / "state/automation_state.json").write_text(json.dumps(state()), encoding="utf-8")
            (root / "state/research_execution_state.json").write_text(json.dumps({"version": 1, "current_run_id": None, "stages": {key: {} for key in ("daily", "tactical", "synthesis", "audit")}}), encoding="utf-8")
            (root / "state/execution_history.json").write_text(json.dumps({"version": 1, "events": []}), encoding="utf-8")
            base = dict(root=root, stage="tactical", at="2026-10-16T09:00:00+08:00", checkpoint="x", artifact=[], error=[], acceptance_passed=False, update_schedule=True, automation_state="state/automation_state.json", execution_state="state/research_execution_state.json", history="state/execution_history.json", result="success")
            record(Namespace(action="start", run_id="failed-run", **base))
            failed_args = dict(base, result="failed", error=["test failure"])
            record(Namespace(action="finish", run_id="failed-run", **failed_args))
            after_failure = json.loads((root / "state/automation_state.json").read_text(encoding="utf-8"))
            self.assertIsNone(after_failure["stages"]["tactical"]["last_successful"])

            artifact = root / "reports/result.md"
            artifact.write_text("verified", encoding="utf-8")
            record(Namespace(action="start", run_id="success-run", **base))
            success_args = dict(base, artifact=["reports/result.md"], acceptance_passed=True)
            first = record(Namespace(action="finish", run_id="success-run", **success_args))
            second = record(Namespace(action="finish", run_id="success-run", **success_args))
            self.assertEqual(first["status"], "recorded")
            self.assertEqual(second["status"], "idempotent_noop")
            after_success = json.loads((root / "state/automation_state.json").read_text(encoding="utf-8"))
            self.assertEqual(after_success["stages"]["tactical"]["run_count"], 1)


class ExecutionTickTests(unittest.TestCase):
    def make_paths(self, root: Path) -> tuple[Path, Path]:
        state_path = root / "state" / "execution_tick_state.json"
        state_path.parent.mkdir()
        state_path.write_text(json.dumps(tick_state()), encoding="utf-8")
        return state_path, root / "runtime" / "execution.lock"

    def test_five_hour_slot_calculation(self) -> None:
        anchor = dt("2026-10-14T09:00:00+08:00")
        self.assertEqual(slot_at_or_before(dt("2026-10-14T13:59:59+08:00")), anchor)
        self.assertEqual(slot_at_or_before(dt("2026-10-14T14:00:00+08:00")), dt("2026-10-14T14:00:00+08:00"))

    def test_cross_day_cycle_is_continuous(self) -> None:
        self.assertEqual(slot_at_or_before(dt("2026-10-15T00:10:00+08:00")), dt("2026-10-15T00:00:00+08:00"))
        self.assertEqual(slot_at_or_before(dt("2026-10-15T05:00:00+08:00")), dt("2026-10-15T05:00:00+08:00"))

    def test_missed_slots_do_not_batch_catch_up(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT / "tests") as directory:
            state_path, lock_path = self.make_paths(Path(directory))
            result = claim_tick(state_path, lock_path, dt("2026-10-15T00:10:00+08:00"), run_id="wake")
            self.assertEqual(result["decision"], "run")
            self.assertEqual(result["slot_id"], slot_id(dt("2026-10-15T00:00:00+08:00")))
            self.assertNotIn("missed_slots", result)

    def test_late_execution_is_skipped(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT / "tests") as directory:
            state_path, lock_path = self.make_paths(Path(directory))
            result = claim_tick(
                state_path,
                lock_path,
                dt("2026-10-14T14:31:00+08:00"),
                scheduled_at=dt("2026-10-14T14:00:00+08:00"),
            )
            self.assertEqual(result["reason"], "stale_slot")
            self.assertFalse(lock_path.exists())

    def test_same_slot_cannot_complete_twice(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT / "tests") as directory:
            state_path, lock_path = self.make_paths(Path(directory))
            now = dt("2026-10-14T14:05:00+08:00")
            first = claim_tick(state_path, lock_path, now, run_id="first")
            self.assertEqual(first["decision"], "run")
            finish_tick(state_path, lock_path, "first", "success", now)
            second = claim_tick(state_path, lock_path, now, run_id="second")
            self.assertEqual(second["reason"], "slot_already_completed")

    def test_active_previous_run_blocks_new_trigger(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT / "tests") as directory:
            state_path, lock_path = self.make_paths(Path(directory))
            first = claim_tick(state_path, lock_path, dt("2026-10-14T14:05:00+08:00"), run_id="first")
            self.assertEqual(first["decision"], "run")
            second = claim_tick(state_path, lock_path, dt("2026-10-14T14:10:00+08:00"), run_id="second")
            self.assertEqual(second["reason"], "active_execution_lock")

    def test_manual_run_does_not_advance_automatic_slot(self) -> None:
        with tempfile.TemporaryDirectory(dir=ROOT / "tests") as directory:
            state_path, lock_path = self.make_paths(Path(directory))
            now = dt("2026-10-14T12:00:00+08:00")
            claimed = claim_tick(state_path, lock_path, now, run_id="manual-one", manual=True)
            self.assertTrue(claimed["manual"])
            finish_tick(state_path, lock_path, "manual-one", "success", now, research_task_successful=True)
            saved = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertIsNone(saved["last_valid_execution_slot"])
            self.assertEqual(saved["completed_slots"], [])
            self.assertEqual(saved["last_successful_research_task_at"], "2026-10-14T12:00:00+08:00")

    def test_timezone_is_normalized_to_shanghai(self) -> None:
        utc_time = dt("2026-10-14T06:05:00+00:00")
        self.assertEqual(slot_at_or_before(utc_time), dt("2026-10-14T14:00:00+08:00"))


if __name__ == "__main__":
    unittest.main()
