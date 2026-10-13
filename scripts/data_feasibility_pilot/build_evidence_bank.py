"""Join verified passages to page-level provenance and validate references."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pages", type=Path, required=True)
    parser.add_argument("--passages", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    pages = {row["page_id"]: row for row in read_jsonl(args.pages)}
    passages = read_jsonl(args.passages)
    evidence = []
    for passage in passages:
        page = pages.get(passage["page_id"])
        if page is None:
            raise SystemExit(f"Unknown page_id: {passage['page_id']}")
        evidence.append(
            {
                **passage,
                "source_id": page["source_id"],
                "source_version_id": page["source_version_id"],
                "document_title": page["document_title"],
                "section_title": page["section_title"],
                "page_image": page["page_image"],
                "ocr_file": page["ocr_file"],
                "source_url": page["source_url"],
                "rights": page["rights"],
            }
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in evidence),
        encoding="utf-8",
    )
    print(json.dumps({"evidence_units": len(evidence), "output": str(args.output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
