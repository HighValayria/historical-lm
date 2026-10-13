"""Create the balanced E0/E1/E2/E3 prompt packets for the validity pilot."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from collections import Counter
from pathlib import Path


BASE_SYSTEM = (
    "请简洁回答研究问题。明确区分直接可支持的陈述、合理推断和无法判断的内容；"
    "不要编造材料、数字、出处或确定性。"
)

TIME_CLAUSE = (
    "知识可用性截止于{cutoff_date}。涉及当时可知内容时，不得把截止日期之后才形成的知识、"
    "术语、制度或解释框架当作当时已有知识；如果问题要求评价史料或现代事实，须把现代判断"
    "与截止日前特定行动者或文献所能支持的判断分开。"
)


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def canonical_hash(value: dict) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def oracle_block(item: dict, evidence: dict[str, dict], pages: dict[str, dict]) -> str:
    blocks = []
    for passage_id in item["evidence_passage_ids"]:
        row = evidence[passage_id]
        page = pages[row["page_id"]]
        locator = (
            f"evidence_id={passage_id}; source={row['document_title']}; "
            f"publication_year={row['publication_year']}; printed_page={row['printed_page']}; "
            f"observation_context={page.get('observation_period', 'unknown')}"
        )
        blocks.append(f"[{locator}]\n{row['verified_transcription']}")
    return "\n\n".join(blocks)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--items", type=Path, required=True)
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--pages", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=20261013)
    args = parser.parse_args()
    items = read_jsonl(args.items)
    evidence = {row["passage_id"]: row for row in read_jsonl(args.evidence)}
    pages = {row["page_id"]: row for row in read_jsonl(args.pages)}
    args.output_dir.mkdir(parents=True, exist_ok=True)

    packets = []
    excluded = []
    for item in items:
        if not item["main_factorial_eligible"]:
            reason = (
                "Requires page image plus raw OCR and is not comparable in the text-only factorial."
                if item["item_id"] == "DFP-Q007"
                else "The isolated passage does not identify the speaker; surrounding context must be added before attribution scoring."
            )
            excluded.append(
                {
                    "item_id": item["item_id"],
                    "reason": reason,
                    "recommended_track": (
                        "separate_multimodal_ocr_control"
                        if item["item_id"] == "DFP-Q007"
                        else "expand_source_context_then_reaudit"
                    ),
                }
            )
            continue
        evidence_text = oracle_block(item, evidence, pages)
        for condition, time_on, evidence_on in (
            ("E0", False, False),
            ("E1", True, False),
            ("E2", False, True),
            ("E3", True, True),
        ):
            system = BASE_SYSTEM
            if time_on:
                system += "\n\n" + TIME_CLAUSE.format(cutoff_date=item["cutoff_date"])
            user = item["question"]
            if evidence_on:
                user = f"以下为本题可使用的历史原始证据。\n\n{evidence_text}\n\n研究问题：{item['question']}"
            prompt = {"system": system, "user": user}
            packets.append(
                {
                    "packet_id": f"RVP-{item['item_id']}-{condition}",
                    "item_id": item["item_id"],
                    "condition": condition,
                    "time_constraint": time_on,
                    "oracle_evidence": evidence_on,
                    "cutoff_date": item["cutoff_date"],
                    "independence_group": item["independence_group"],
                    "primary_construct": item["primary_construct"],
                    "research_disposition": item["research_disposition"],
                    "evidence_passage_ids": item["evidence_passage_ids"] if evidence_on else [],
                    "prompt": prompt,
                    "prompt_sha256": canonical_hash(prompt),
                }
            )

    rng = random.Random(args.seed)
    order = [row["packet_id"] for row in packets]
    rng.shuffle(order)
    run_order = {packet_id: index + 1 for index, packet_id in enumerate(order)}
    for row in packets:
        row["randomized_run_order"] = run_order[row["packet_id"]]
    packets.sort(key=lambda row: row["randomized_run_order"])

    (args.output_dir / "prompt_packets_v2.jsonl").write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in packets), encoding="utf-8"
    )
    (args.output_dir / "excluded_items.json").write_text(
        json.dumps(excluded, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    sets = {
        "primary_validity_items": [
            "DFP-Q002",
            "DFP-Q004",
            "DFP-Q008",
            "DFP-Q013",
            "DFP-Q015",
            "DFP-Q017",
            "DFP-Q018",
            "DFP-Q020",
        ],
        "reading_controls": ["DFP-Q001", "DFP-Q003", "DFP-Q005", "DFP-Q019"],
        "strict_temporal_items": ["DFP-Q017"],
        "all_factorial_eligible": [row["item_id"] for row in items if row["main_factorial_eligible"]],
        "excluded_from_text_factorial": [row["item_id"] for row in items if not row["main_factorial_eligible"]],
        "selection_note": "Primary set uses one item per evidence group where possible and is descriptive, not a confirmatory benchmark.",
    }
    (args.output_dir / "analysis_sets.json").write_text(json.dumps(sets, ensure_ascii=False, indent=2), encoding="utf-8")
    summary = {
        "eligible_items": len({row["item_id"] for row in packets}),
        "excluded_items": len(excluded),
        "prompt_packets": len(packets),
        "condition_counts": dict(Counter(row["condition"] for row in packets)),
        "independence_groups": len({row["independence_group"] for row in packets}),
        "seed": args.seed,
    }
    (args.output_dir / "packet_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
