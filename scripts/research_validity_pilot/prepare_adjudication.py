"""Prepare blinded second-review tasks without claiming independent review occurred."""

from __future__ import annotations

import argparse
import json
import random
import re
from pathlib import Path


MEDICAL_TERMS = re.compile(
    r"cholera|small-pox|vaccin|syphilis|scrofula|tuberculosis|scarlet|typhoid|dysentery|salol",
    re.I,
)


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--passages", type=Path, required=True)
    parser.add_argument("--pages", type=Path, required=True)
    parser.add_argument("--items", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=20261013)
    args = parser.parse_args()
    passages = read_jsonl(args.passages)
    pages = {row["page_id"]: row for row in read_jsonl(args.pages)}
    items = read_jsonl(args.items)
    audit = {row["item_id"]: row for row in read_jsonl(args.audit)}
    evidence = {row["passage_id"]: row for row in passages}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    shuffled_passages = passages[:]
    rng.shuffle(shuffled_passages)
    transcription_tasks = []
    transcription_key = []
    disagreement = []
    for index, row in enumerate(shuffled_passages, 1):
        review_id = f"TR-{index:03d}"
        page = pages[row["page_id"]]
        reasons = []
        if re.search(r"\d", row["verified_transcription"]):
            reasons.append("digits_or_dates")
        if MEDICAL_TERMS.search(row["verified_transcription"]):
            reasons.append("medical_terms")
        if row["passage_id"] == "PASS-CMMJ-1889-0086-A":
            reasons.append("known_5807_vs_6807_ocr_conflict")
        if row["passage_id"] == "PASS-CMMJ-1890-0442-A":
            reasons.append("speaker_identity_missing_from_isolated_passage")
        transcription_tasks.append(
            {
                "review_id": review_id,
                "page_image": page["page_image"],
                "printed_page": page["printed_page"],
                "raw_ocr_excerpt": row["raw_ocr_excerpt"],
                "reviewer_transcription": "",
                "reviewer_uncertain_spans": [],
                "reviewer_id": "",
                "review_timestamp": "",
            }
        )
        transcription_key.append(
            {
                "review_id": review_id,
                "passage_id": row["passage_id"],
                "existing_verified_transcription": row["verified_transcription"],
                "existing_verifier": "Codex primary agent in Data Feasibility Pilot",
                "existing_verification_independent_of_current_agent": False,
            }
        )
        disagreement.append(
            {
                "review_id": review_id,
                "passage_id": row["passage_id"],
                "priority": "high" if reasons else "standard",
                "review_reasons": reasons or ["routine_second_pass"],
                "status": "awaiting_independent_reviewer",
            }
        )

    shuffled_items = items[:]
    rng.shuffle(shuffled_items)
    item_tasks = []
    item_key = []
    for index, row in enumerate(shuffled_items, 1):
        review_id = f"IT-{index:03d}"
        blocks = []
        for pid in row["evidence_passage_ids"]:
            e = evidence[pid]
            blocks.append(
                {
                    "evidence_id": pid,
                    "publication_year": e["publication_year"],
                    "printed_page": e["printed_page"],
                    "verified_transcription": e["verified_transcription"],
                }
            )
        item_tasks.append(
            {
                "review_id": review_id,
                "question": row["question"],
                "evidence": blocks,
                "reviewer_proposed_answer": "",
                "reviewer_evidence_sufficiency": "",
                "reviewer_primary_construct": "",
                "reviewer_acceptable_alternatives": [],
                "reviewer_id": "",
                "review_timestamp": "",
            }
        )
        item_key.append(
            {
                "review_id": review_id,
                "item_id": row["item_id"],
                "existing_gold_answer": row["gold_answer"],
                "existing_primary_construct": row["primary_construct"],
                "existing_disposition": row["research_disposition"],
                "audit_note": audit[row["item_id"]]["audit_note"],
                "existing_reviewer": "Codex primary agent, same project lineage",
                "independent_review_completed": False,
            }
        )

    write_jsonl(args.output_dir / "blind_transcription_tasks.jsonl", transcription_tasks)
    write_jsonl(args.output_dir / "blind_transcription_key.jsonl", transcription_key)
    write_jsonl(args.output_dir / "blind_item_tasks.jsonl", item_tasks)
    write_jsonl(args.output_dir / "blind_item_key.jsonl", item_key)
    write_jsonl(args.output_dir / "disagreement_queue.jsonl", disagreement)
    summary = {
        "transcription_tasks": len(transcription_tasks),
        "item_tasks": len(item_tasks),
        "high_priority_transcription_reviews": sum(row["priority"] == "high" for row in disagreement),
        "independent_reviews_completed": 0,
        "seed": args.seed,
    }
    (args.output_dir / "adjudication_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
