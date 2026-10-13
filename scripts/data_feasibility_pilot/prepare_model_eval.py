"""Prepare B0/B1/B2 prompt packets without calling any model.

The script is intentionally offline.  It creates immutable prompt packets and an
empty evaluation sheet.  A separate, explicitly authorized runner must record the
model/provider/revision and raw responses.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--benchmark", type=Path, required=True)
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    items = read_jsonl(args.benchmark)
    evidence = {row["passage_id"]: row for row in read_jsonl(args.evidence)}
    args.output_dir.mkdir(parents=True, exist_ok=True)

    packets = []
    for item in items:
        cutoff = item["cutoff_date"]
        historical_instruction = (
            f"你的回答必须限制在{cutoff}或之前可获得的知识与所指史料范围内。"
            "区分作者声称、材料直接支持和你的推断；证据不足时明确说不能判断。"
            "不要把一份材料未记载某事当作整个社会不存在该知识。"
        )
        selected = [evidence[pid] for pid in item["evidence_passage_ids"]]
        evidence_block = "\n\n".join(
            f"[{row['passage_id']}; {row['document_title']}; published {row['publication_year']}; "
            f"printed page {row['printed_page']}]\n{row['verified_transcription']}"
            for row in selected
        )
        conditions = {
            "B0": {"system": "请准确回答问题。", "user": item["question"]},
            "B1": {"system": historical_instruction, "user": item["question"]},
            "B2": {
                "system": historical_instruction + "回答必须以所给证据为依据并标明证据编号。",
                "user": f"证据：\n{evidence_block}\n\n问题：{item['question']}",
            },
        }
        for condition, prompt in conditions.items():
            canonical = json.dumps(prompt, ensure_ascii=False, sort_keys=True).encode("utf-8")
            packets.append(
                {
                    "packet_id": f"{item['item_id']}-{condition}",
                    "item_id": item["item_id"],
                    "condition": condition,
                    "cutoff_date": cutoff,
                    "prompt": prompt,
                    "prompt_sha256": hashlib.sha256(canonical).hexdigest(),
                    "evidence_passage_ids": item["evidence_passage_ids"] if condition == "B2" else [],
                }
            )
    packet_path = args.output_dir / "prompt_packets.jsonl"
    packet_path.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in packets),
        encoding="utf-8",
    )
    with (args.output_dir / "human_evaluation_template.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "packet_id",
                "item_id",
                "condition",
                "correctness_0_2",
                "temporal_discipline_0_2",
                "evidence_fidelity_0_2",
                "epistemic_calibration_0_2",
                "provenance_use_0_2",
                "anachronism_present",
                "unsupported_specific_number",
                "source_population_overgeneralized",
                "ocr_error_repeated",
                "notes",
            ]
        )
        for row in packets:
            writer.writerow([row["packet_id"], row["item_id"], row["condition"]] + [""] * 10)
    print(json.dumps({"items": len(items), "prompt_packets": len(packets), "conditions": 3}, ensure_ascii=False))


if __name__ == "__main__":
    main()
