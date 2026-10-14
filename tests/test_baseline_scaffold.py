from __future__ import annotations

import json
import unittest
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "experiments" / "baselines" / "config.schema.json"


def dry_run_config() -> dict:
    return {
        "experiment_id": "schema-test",
        "status": "configured_not_executed",
        "execution_mode": "dry_run",
        "model": {"identifier": "REPLACE_WITH_EXACT_MODEL_ID", "revision": "REPLACE_IF_AVAILABLE"},
        "endpoint": {"type": "openai_compatible_chat_completions", "scope": "loopback"},
        "generation": {"temperature": 0.0, "max_tokens": 500, "seed": 20261014},
        "conditions": ["P0", "P1", "O0", "O1", "R0", "R1"],
        "input_packets": {"path": "experiments/future/packets.jsonl", "sha256": "0" * 64},
        "retrieval": {"license_review": "pending", "ordinary_rag": "not_configured", "temporal_rag": "not_configured"},
        "artifacts": {"raw_responses_path": "experiments/baselines/raw/responses.jsonl", "scoring_path": "experiments/baselines/scoring/ledger.csv"},
    }


class BaselineScaffoldTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(cls.schema)

    def test_dry_run_configuration_is_valid(self) -> None:
        jsonschema.validate(dry_run_config(), self.schema)

    def test_authorized_execution_requires_authorization_id(self) -> None:
        config = dry_run_config()
        config["execution_mode"] = "authorized_execute"
        config["status"] = "authorized_ready"
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate(config, self.schema)
        config["endpoint"]["authorization_id"] = "USER-AUTH-REQUIRED"
        jsonschema.validate(config, self.schema)

    def test_raw_and_scoring_locations_are_separated(self) -> None:
        config = dry_run_config()
        config["artifacts"]["raw_responses_path"] = "experiments/baselines/scoring/pretend-raw.jsonl"
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate(config, self.schema)


if __name__ == "__main__":
    unittest.main()
