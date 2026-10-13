"""Verify structural and leakage invariants for the Research Validity Pilot."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_hash(value: dict) -> str:
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    checks: list[dict] = []

    def check(name: str, passed: bool, detail: str) -> None:
        checks.append({"check": name, "passed": bool(passed), "detail": detail})

    base = root / "experiments/research_validity_pilot"
    manifest = json.loads((base / "audit/frozen_input_manifest.json").read_text(encoding="utf-8"))
    frozen_ok = True
    for item in manifest["frozen_inputs"]:
        source = root / item["path"]
        frozen_ok &= source.exists() and sha256(source) == item["sha256"]
    check("frozen_inputs_unchanged", frozen_ok, f"{len(manifest['frozen_inputs'])} files match recorded SHA-256")

    audit = read_jsonl(base / "audit/item_audit.jsonl")
    revised = read_jsonl(base / "audit/revised_items_v2.jsonl")
    summary = json.loads((base / "audit/audit_summary.json").read_text(encoding="utf-8"))
    check("audit_has_20_unique_items", len(audit) == 20 and len({r['item_id'] for r in audit}) == 20, str(len(audit)))
    check("audit_expected_dispositions", summary["dispositions"] == {"control_only": 7, "usable_directly": 10, "temporarily_unsuitable": 1, "needs_revision": 2}, str(summary["dispositions"]))
    check("strict_temporal_count", summary["direct_historical_boundary_or_anachronism"] == 1, str(summary["direct_historical_boundary_or_anachronism"]))
    check("revised_items_preserve_parents", len(revised) == 20 and {r['parent_item_id'] for r in revised} == {r['item_id'] for r in audit}, str(len(revised)))

    evidence = {r["passage_id"]: r for r in read_jsonl(root / "experiments/data_feasibility_pilot/benchmark/evidence_bank.jsonl")}
    packets = read_jsonl(base / "factorial/prompt_packets_v2.jsonl")
    counts = Counter(r["condition"] for r in packets)
    check("balanced_factorial", len(packets) == 72 and counts == {"E0": 18, "E1": 18, "E2": 18, "E3": 18}, str(dict(counts)))
    check("four_cells_per_item", all(Counter(r["condition"] for r in packets if r["item_id"] == item) == {"E0": 1, "E1": 1, "E2": 1, "E3": 1} for item in {r['item_id'] for r in packets}), "18 items")
    check("prompt_hashes", all(r["prompt_sha256"] == canonical_hash(r["prompt"]) for r in packets), "72 canonical hashes")
    check("time_clause_only_in_E1_E3", all(("知识可用性截止于" in r["prompt"]["system"]) == (r["condition"] in {"E1", "E3"}) for r in packets), "condition clause invariant")
    check("oracle_only_in_E2_E3", all(("以下为本题可使用的历史原始证据" in r["prompt"]["user"]) == (r["condition"] in {"E2", "E3"}) for r in packets), "condition Oracle invariant")
    check("oracle_reference_fields", all((bool(r["evidence_passage_ids"]) == (r["condition"] in {"E2", "E3"})) for r in packets), "evidence ids match cells")
    forbidden = []
    for packet in packets:
        if packet["condition"] not in {"E2", "E3"}:
            continue
        prompt_text = packet["prompt"]["user"]
        for passage_id in packet["evidence_passage_ids"]:
            row = evidence[passage_id]
            for field in ("normalized_text", "modern_interpretation", "caution", "gold_answer"):
                value = row.get(field)
                if isinstance(value, str) and value.strip() and value.strip() in prompt_text:
                    forbidden.append((packet["packet_id"], passage_id, field))
    check("no_oracle_annotation_leakage", not forbidden, str(forbidden[:3]))

    excluded = json.loads((base / "factorial/excluded_items.json").read_text(encoding="utf-8"))
    check("expected_exclusions", {r["item_id"] for r in excluded} == {"DFP-Q007", "DFP-Q012"}, str([r['item_id'] for r in excluded]))
    with (base / "model_runs/scoring_ledger.csv").open(encoding="utf-8-sig", newline="") as handle:
        score_rows = list(csv.DictReader(handle))
    check("scoring_ledger_rows", len(score_rows) == 72 and all(r["adjudication_status"] == "unscored_no_model_output" for r in score_rows), str(len(score_rows)))
    trans = read_jsonl(base / "adjudication/blind_transcription_tasks.jsonl")
    items = read_jsonl(base / "adjudication/blind_item_tasks.jsonl")
    adj_summary = json.loads((base / "adjudication/adjudication_summary.json").read_text(encoding="utf-8"))
    check("blind_review_packets", len(trans) == 12 and len(items) == 20 and adj_summary["independent_reviews_completed"] == 0, f"{len(trans)} passages, {len(items)} items, 0 complete")
    chronology = read_jsonl(base / "adjudication/chronology_gap_registry.jsonl")
    check("chronology_labels_withheld", len(chronology) == 4 and all(r["label_allowed"] is False for r in chronology), f"{len(chronology)} gaps")
    run_status = json.loads((base / "model_runs/run_status.json").read_text(encoding="utf-8"))
    check("no_fabricated_model_results", run_status["real_model_outputs"] == 0 and not (base / "model_runs/raw_responses.jsonl").exists(), "0 outputs; raw response file absent")
    check("dry_run_did_not_write", not (base / "model_runs/dry_run_should_not_exist.jsonl").exists(), "dry-run output absent")

    failed = [c for c in checks if not c["passed"]]
    result = {"status": "PASS" if not failed else "FAIL", "checks": len(checks), "failed": len(failed), "details": checks}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"status": result["status"], "checks": len(checks), "failed": len(failed)}, ensure_ascii=False))
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
