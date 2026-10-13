"""Build the reproducible 14-page feasibility-pilot bundle.

The script preserves OCR verbatim.  It creates page-level metadata, individual OCR
files, and SHA-256 inventories; manual verification/transcription remains a separate
human-review artifact.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

from pypdf import PdfReader


CMMJ_PAGES = {
    35: (31, 1889, "A Year's Medical Work in Tungchowfu"),
    80: (68, 1889, "Salol as a Remedy for Asiatic Cholera"),
    81: (69, 1889, "Editorial continuation on cholera"),
    83: (71, 1889, "Hospital Reports"),
    86: (74, 1889, "Hospital Reports / Society Reports"),
    437: (165, 1890, "The Fevers of China"),
    439: (167, 1890, "The Fevers of China"),
    442: (170, 1890, "Society discussion on fevers"),
}

WELLCOME_PAGES = {
    26: (2, "Peking: population, houses, burial, drains and water supply"),
    27: (3, "Peking: moats, wells, water supply and diet"),
    31: (7, "Peking: sanitary conditions, drainage and mortality"),
    33: (9, "Tientsin: water supply, filtration, drainage and health"),
    44: (20, "Drainage, sewer proximity and disease observations"),
    49: (25, "Hankow: flooding, drainage, latrines and disease"),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def alto_text(path: Path) -> str:
    root = ET.parse(path).getroot()
    words = []
    for element in root.iter():
        if element.tag.rsplit("}", 1)[-1] == "String":
            content = element.attrib.get("CONTENT")
            if content:
                words.append(content)
    return " ".join(words)


def rel(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    root = args.root.resolve()
    raw = root / "data/raw/data_feasibility_pilot"
    processed = root / "data/processed/data_feasibility_pilot"
    experiment = root / "experiments/data_feasibility_pilot"
    cmmj_ocr_dir = processed / "ocr/ia_cmmj"
    wellcome_ocr_dir = processed / "ocr/wellcome_customs_1884"
    cmmj_ocr_dir.mkdir(parents=True, exist_ok=True)
    wellcome_ocr_dir.mkdir(parents=True, exist_ok=True)

    cmmj_pdf = raw / "ia_cmmj_1889_1890/3522418_1889_1890_text.pdf"
    reader = PdfReader(str(cmmj_pdf))
    pages = []
    for pdf_page, (printed_page, year, section) in CMMJ_PAGES.items():
        text = reader.pages[pdf_page - 1].extract_text() or ""
        ocr_path = cmmj_ocr_dir / f"pdf_page_{pdf_page:04d}.txt"
        ocr_path.write_text(text, encoding="utf-8")
        image_path = processed / f"pages/ia_cmmj/pdf_page_{pdf_page:04d}.png"
        pages.append(
            {
                "page_id": f"CMMJ-{year}-PDF-{pdf_page:04d}",
                "source_id": "IA-CMMJ-1889-1890",
                "source_version_id": "IA-3522418-TEXT-PDF",
                "document_title": "The China Medical Missionary Journal (Volumes III-IV)",
                "section_title": section,
                "publication_year": year,
                "observation_period": str(year),
                "pdf_page_1based": pdf_page,
                "printed_page": printed_page,
                "scan_leaf": pdf_page - 1,
                "original_file": rel(cmmj_pdf, root),
                "page_image": rel(image_path, root),
                "ocr_file": rel(ocr_path, root),
                "ocr_provenance": "Internet Archive text PDF; ABBYY FineReader 11 extended OCR",
                "rights": "Public Domain Mark 1.0",
                "source_url": "https://archive.org/details/3522418_1889_1890",
                "visual_check": "completed_by_research_agent",
            }
        )

    manifest_path = raw / "wellcome_customs_1884/b20416179_manifest.json"
    for leaf, (printed_page, section) in WELLCOME_PAGES.items():
        alto_path = raw / f"wellcome_customs_1884/alto_candidates/b20416179_{leaf:04d}.jp2.xml"
        text = alto_text(alto_path)
        ocr_path = wellcome_ocr_dir / f"leaf_{leaf:04d}.txt"
        ocr_path.write_text(text, encoding="utf-8")
        image_path = raw / f"wellcome_customs_1884/selected_images/b20416179_{leaf:04d}.jp2.jpg"
        pages.append(
            {
                "page_id": f"WC-CUSTOMS-1884-LEAF-{leaf:04d}",
                "source_id": "WELLCOME-B20416179-1884",
                "source_version_id": "WELLCOME-IIIF-B20416179",
                "document_title": "An epitome of the reports of the medical officers to the Chinese imperial maritime customs service, from 1871 to 1882",
                "section_title": section,
                "publication_year": 1884,
                "observation_period": "compiled from reports dated 1871-1882; exact dates vary within page",
                "iiif_canvas_leaf": leaf,
                "printed_page": printed_page,
                "original_file": rel(manifest_path, root),
                "page_image": rel(image_path, root),
                "ocr_file": rel(ocr_path, root),
                "ocr_provenance": "Wellcome Collection page-level ALTO OCR",
                "rights": "Public Domain Mark 1.0",
                "source_url": "https://wellcomecollection.org/works/za7rnxwq",
                "iiif_manifest": "https://iiif.wellcomecollection.org/presentation/v2/b20416179",
                "visual_check": "completed_by_research_agent",
            }
        )

    page_manifest = experiment / "manifests/selected_pages.jsonl"
    page_manifest.parent.mkdir(parents=True, exist_ok=True)
    page_manifest.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in pages),
        encoding="utf-8",
    )

    inventory = []
    for base_label, base in (("raw", raw), ("processed", processed)):
        for path in sorted(p for p in base.rglob("*") if p.is_file()):
            inventory.append(
                {
                    "scope": base_label,
                    "path": rel(path, root),
                    "bytes": path.stat().st_size,
                    "sha256": sha256(path),
                }
            )
    inventory_path = experiment / "manifests/file_inventory_sha256.json"
    inventory_path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2), encoding="utf-8")

    summary = {
        "selected_pages": len(pages),
        "cmmj_pages": len(CMMJ_PAGES),
        "wellcome_pages": len(WELLCOME_PAGES),
        "inventory_files": len(inventory),
        "inventory_bytes": sum(row["bytes"] for row in inventory),
        "page_manifest": rel(page_manifest, root),
        "inventory": rel(inventory_path, root),
    }
    (experiment / "manifests/build_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
