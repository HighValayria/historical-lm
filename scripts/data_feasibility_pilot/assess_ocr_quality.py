"""Measure selected-passage OCR divergence from visually verified transcription."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def edit_distance(a: str, b: str) -> int:
    previous = list(range(len(b) + 1))
    for i, char_a in enumerate(a, 1):
        current = [i]
        for j, char_b in enumerate(b, 1):
            current.append(
                min(
                    current[-1] + 1,
                    previous[j] + 1,
                    previous[j - 1] + (char_a != char_b),
                )
            )
        previous = current
    return previous[-1]


def comparable(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--passages", type=Path, required=True)
    parser.add_argument("--page-manifest", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    passages = [json.loads(line) for line in args.passages.read_text(encoding="utf-8").splitlines() if line]
    pages = [json.loads(line) for line in args.page_manifest.read_text(encoding="utf-8").splitlines() if line]
    per_passage = []
    total_edits = 0
    total_verified_chars = 0
    for row in passages:
        raw = comparable(row["raw_ocr_excerpt"])
        verified = comparable(row["verified_transcription"])
        edits = edit_distance(raw, verified)
        total_edits += edits
        total_verified_chars += len(verified)
        per_passage.append(
            {
                "passage_id": row["passage_id"],
                "page_id": row["page_id"],
                "raw_chars": len(raw),
                "verified_chars": len(verified),
                "edit_distance": edits,
                "character_error_rate": edits / max(1, len(verified)),
            }
        )

    page_stats = []
    for page in pages:
        path = args.root / page["ocr_file"]
        text = path.read_text(encoding="utf-8")
        page_stats.append(
            {
                "page_id": page["page_id"],
                "source_id": page["source_id"],
                "ocr_chars": len(text),
                "ocr_words_whitespace": len(text.split()),
            }
        )

    result = {
        "method": "character-level Levenshtein distance after whitespace collapse; verified snippets only",
        "limitations": [
            "small purposive sample",
            "single visual verification pass",
            "punctuation and typographic normalization count as edits",
            "not a whole-page or whole-document OCR accuracy estimate",
        ],
        "passages": len(passages),
        "verified_characters": total_verified_chars,
        "micro_character_error_rate": total_edits / max(1, total_verified_chars),
        "per_passage": per_passage,
        "selected_page_ocr": {
            "pages": len(page_stats),
            "characters": sum(row["ocr_chars"] for row in page_stats),
            "whitespace_words": sum(row["ocr_words_whitespace"] for row in page_stats),
            "by_page": page_stats,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("passages", "verified_characters", "micro_character_error_rate")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
