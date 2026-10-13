"""Extract verbatim ALTO token streams and rank Wellcome pilot pages."""

from __future__ import annotations

import argparse
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


TERMS = {
    "sanitary": 5,
    "drain": 4,
    "sewage": 5,
    "water": 3,
    "cholera": 5,
    "small-pox": 5,
    "vaccin": 5,
    "epidemic": 4,
    "latrine": 4,
    "filth": 4,
    "hospital": 1,
}


def alto_text(path: Path) -> str:
    root = ET.parse(path).getroot()
    words = []
    for element in root.iter():
        if element.tag.rsplit("}", 1)[-1] == "String":
            content = element.attrib.get("CONTENT")
            if content:
                words.append(content)
    return " ".join(words)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = []
    for path in sorted(args.input_dir.glob("*.xml")):
        text = alto_text(path)
        lowered = text.lower()
        hits = {term: len(re.findall(re.escape(term), lowered)) for term in TERMS}
        hits = {term: count for term, count in hits.items() if count}
        score = sum(TERMS[term] * count for term, count in hits.items())
        leaf_match = re.search(r"_(\d{4})\.jp2", path.name)
        rows.append(
            {
                "file": path.name,
                "leaf": int(leaf_match.group(1)) if leaf_match else None,
                "keyword_hits": hits,
                "score": score,
                "text": text,
            }
        )
    rows.sort(key=lambda row: (-row["score"], row["leaf"] or 0))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"files": len(rows), "output": str(args.output)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
