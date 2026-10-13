"""Create an empty, auditable scoring ledger for real model outputs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--packets", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    packets = read_jsonl(args.packets)
    audit = {row["item_id"]: row for row in read_jsonl(args.audit)}
    fields = [
        "packet_id",
        "item_id",
        "condition",
        "independence_group",
        "primary_construct",
        "model_identifier",
        "model_revision",
        "annotator_id",
        "review_level",
        "source_fact_accuracy",
        "temporal_boundary_status",
        "source_attribution",
        "evidence_fidelity",
        "unsupported_content",
        "epistemic_calibration",
        "claim_truth_separation",
        "abstention_behavior",
        "error_span",
        "evidence_reference",
        "chronology_record_id",
        "actor_access_assessment",
        "rationale",
        "adjudication_status",
    ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for packet in packets:
            item = audit[packet["item_id"]]
            writer.writerow(
                {
                    "packet_id": packet["packet_id"],
                    "item_id": packet["item_id"],
                    "condition": packet["condition"],
                    "independence_group": packet["independence_group"],
                    "primary_construct": packet["primary_construct"],
                    "temporal_boundary_status": (
                        "" if item["direct_historical_boundary_or_anachronism"] else "NA"
                    ),
                    "evidence_fidelity": "" if packet["oracle_evidence"] else "NA",
                    "adjudication_status": "unscored_no_model_output",
                }
            )
    print(json.dumps({"rows": len(packets), "output": str(args.output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
