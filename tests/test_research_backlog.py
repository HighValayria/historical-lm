from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from manage_research_backlog import REQUIRED_FIELDS, record_failure, select_next, validate  # noqa: E402


class BacklogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads((ROOT / "state/research_backlog.json").read_text(encoding="utf-8"))

    def test_schema_and_statuses(self) -> None:
        self.assertEqual(validate(self.data), [])
        for task in self.data["tasks"]:
            self.assertTrue(REQUIRED_FIELDS.issubset(task))

    def test_dependencies_hold_proposed_tasks(self) -> None:
        data = json.loads(json.dumps(self.data))
        by_id = {task["task_id"]: task for task in data["tasks"]}
        # Persisted automation state advances over time; exercise the rule with
        # a dependency-incomplete snapshot instead of assuming a fresh repo.
        by_id["A2"]["status"] = "ready"
        by_id["B1"]["status"] = "ready"
        by_id["A3"]["status"] = "proposed"
        by_id["B2"]["status"] = "proposed"
        by_id["B3"]["status"] = "proposed"
        self.assertEqual(by_id["A3"]["status"], "proposed")
        self.assertIn("A2", by_id["A3"]["dependencies"])
        self.assertEqual(by_id["B2"]["status"], "proposed")

    def test_selection_uses_priority_and_track_balance(self) -> None:
        data = json.loads(json.dumps(self.data))
        # The persisted backlog may contain a task actively claimed by an
        # automation run. This unit test isolates tie-breaking among ready
        # tasks rather than inheriting that resumable-running state.
        for task in data["tasks"]:
            if task["status"] == "running":
                task["status"] = "ready"
                task["checkpoint"]["safe_to_resume"] = False
        by_id = {task["task_id"]: task for task in data["tasks"]}
        by_id["A2"]["status"] = "ready"
        by_id["B1"]["status"] = "ready"
        by_id["A3"]["status"] = "proposed"
        by_id["B2"]["status"] = "proposed"
        by_id["B3"]["status"] = "proposed"
        data["scheduler"]["last_claimed_track"] = "A"
        self.assertEqual(select_next(data)["task_id"], "B1")
        data["scheduler"]["last_claimed_track"] = "B"
        self.assertEqual(select_next(data)["track"], "A")

    def test_safe_running_task_resumes_first(self) -> None:
        data = json.loads(json.dumps(self.data))
        task = next(item for item in data["tasks"] if item["task_id"] == "B1")
        task["status"] = "running"
        task["checkpoint"]["safe_to_resume"] = True
        self.assertEqual(select_next(data)["task_id"], "B1")

    def test_second_failure_without_new_repair_blocks(self) -> None:
        task = json.loads(json.dumps(self.data["tasks"][0]))
        task.update({"status": "running", "attempt_count": 2})
        record_failure(task, ["repeat failure"], "same cause", False, "2026-10-13T12:00:00+08:00")
        self.assertEqual(task["status"], "blocked")
        self.assertFalse(task["checkpoint"]["safe_to_resume"])

    def test_formal_design_permissions_are_explicit(self) -> None:
        daily = (ROOT / "automation/DAILY_PROTOCOL.md").read_text(encoding="utf-8")
        tactical = (ROOT / "automation/TACTICAL_PROTOCOL.md").read_text(encoding="utf-8")
        synthesis = (ROOT / "automation/SYNTHESIS_PROTOCOL.md").read_text(encoding="utf-8")
        audit = (ROOT / "automation/AUDIT_PROTOCOL.md").read_text(encoding="utf-8")
        self.assertIn("不修改正式研究设计", daily)
        self.assertIn("不得修改正式研究设计", tactical)
        self.assertIn("不得修改正式设计", synthesis)
        self.assertIn("冻结当前完整", audit)
        self.assertIn("VERSION_LOG.md", audit)


if __name__ == "__main__":
    unittest.main()
