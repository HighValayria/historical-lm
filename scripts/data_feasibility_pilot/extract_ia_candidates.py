"""Rank page-level public-health candidates in the CMMJ pilot volume.

This is a read-only extraction step: it does not normalize or silently repair OCR.
The output keeps the PDF page index, the Internet Archive leaf number, the detected
printed page number, and the verbatim text returned by the PDF text layer.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from pypdf import PdfReader


TERMS = {
    "cholera": 5,
    "small-pox": 5,
    "vaccin": 5,
    "sanitary": 4,
    "epidemic": 4,
    "sewage": 4,
    "drainage": 3,
    "water supply": 4,
    "quarantine": 5,
    "filth": 3,
    "latrine": 3,
    "hospital": 1,
    "dispensary": 1,
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=Path, required=True)
    parser.add_argument("--page-numbers", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--limit", type=int, default=80)
    args = parser.parse_args()

    mapping = json.loads(args.page_numbers.read_text(encoding="utf-8"))["pages"]
    by_leaf = {int(row["leafNum"]): row for row in mapping}
    reader = PdfReader(str(args.pdf))
    candidates = []

    for pdf_index, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        lowered = text.lower()
        hits = {term: len(re.findall(re.escape(term), lowered)) for term in TERMS}
        hits = {term: count for term, count in hits.items() if count}
        if not hits:
            continue
        score = sum(TERMS[term] * count for term, count in hits.items())
        map_row = by_leaf.get(pdf_index, {})
        candidates.append(
            {
                "pdf_page_1based": pdf_index + 1,
                "pdf_index_0based": pdf_index,
                "ia_leaf_num": pdf_index,
                "printed_page_detected": map_row.get("pageNumber", ""),
                "page_number_confidence": map_row.get("confidence"),
                "keyword_hits": hits,
                "score": score,
                "text": text,
            }
        )

    candidates.sort(key=lambda row: (-row["score"], row["pdf_page_1based"]))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(candidates[: args.limit], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "pdf_pages": len(reader.pages),
                "matched_pages": len(candidates),
                "written": min(args.limit, len(candidates)),
                "output": str(args.output),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
