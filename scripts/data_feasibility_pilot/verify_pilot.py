"""Fail-closed integrity and referential checks for the feasibility pilot."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def unique(rows: list[dict], key: str) -> None:
    values = [row[key] for row in rows]
    if len(values) != len(set(values)):
        raise AssertionError(f"Duplicate {key}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    exp = root / "experiments/data_feasibility_pilot"

    sources = read_jsonl(exp / "manifests/source_manifest.jsonl")
    pages = read_jsonl(exp / "manifests/selected_pages.jsonl")
    evidence = read_jsonl(exp / "benchmark/evidence_bank.jsonl")
    items = read_jsonl(exp / "benchmark/benchmark_items.jsonl")
    packets = read_jsonl(exp / "model_eval/prompt_packets.jsonl")
    inventory = json.loads((exp / "manifests/file_inventory_sha256.json").read_text(encoding="utf-8"))

    unique(sources, "source_id")
    unique(pages, "page_id")
    unique(evidence, "passage_id")
    unique(items, "item_id")
    unique(packets, "packet_id")
    source_ids = {row["source_id"] for row in sources}
    page_ids = {row["page_id"] for row in pages}
    passage_ids = {row["passage_id"] for row in evidence}
    item_ids = {row["item_id"] for row in items}

    assert len(sources) == 3
    assert len(pages) == 14
    assert len(evidence) == 12
    assert len(items) == 20
    assert len(packets) == 60
    assert all(row["source_id"] in source_ids for row in pages)
    assert all(row["page_id"] in page_ids for row in evidence)
    assert all(set(row["evidence_passage_ids"]) <= passage_ids for row in items)
    assert all(row["item_id"] in item_ids for row in packets)
    assert Counter(row["condition"] for row in packets) == {"B0": 20, "B1": 20, "B2": 20}
    assert all((root / row["ocr_file"]).is_file() for row in pages)
    assert all((root / row["page_image"]).is_file() for row in pages)

    bad_hashes = []
    for row in inventory:
        path = root / row["path"]
        if not path.is_file() or path.stat().st_size != row["bytes"] or digest(path) != row["sha256"]:
            bad_hashes.append(row["path"])
    assert not bad_hashes, f"Inventory mismatch: {bad_hashes}"

    for row in packets:
        canonical = json.dumps(row["prompt"], ensure_ascii=False, sort_keys=True).encode("utf-8")
        assert hashlib.sha256(canonical).hexdigest() == row["prompt_sha256"]

    report = {
        "status": "PASS",
        "sources_registered": len(sources),
        "sources_admitted": sum(bool(row["usable_for_pilot"]) for row in sources),
        "selected_pages": len(pages),
        "evidence_units": len(evidence),
        "benchmark_items": len(items),
        "independence_groups": len({row["independence_group"] for row in items}),
        "item_type_counts": dict(Counter(row["type"] for row in items)),
        "prompt_packets": len(packets),
        "inventory_files_verified": len(inventory),
        "model_outputs_present": (exp / "model_eval/raw_responses.jsonl").is_file(),
        "warnings": [
            "Verified transcriptions received one visual pass, not double-keying or historian adjudication.",
            "Twenty items share evidence and form fewer independent groups.",
            "No model outputs are expected at this stage.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
