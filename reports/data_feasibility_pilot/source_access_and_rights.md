# Source access and rights report

## Decision summary

Two public-domain source versions were admitted to the data-feasibility pilot. A third, the 1898/1899 Shanghai Municipal Council annual report on bnAsie, was registered but excluded from content processing because the saved catalogue page provides a PDF link while the site footer states “All Rights Reserved” and no item-level reuse licence was found.

| Source | Period represented | Verified local state | Rights/access decision | Pilot use |
|---|---:|---|---|---|
| *China Medical Missionary Journal*, vols. III–IV | Published 1889–1890 | 606-page text PDF, full OCR derivatives, page map and metadata downloaded; 8 pages rendered and selected | Internet Archive metadata explicitly records Public Domain Mark 1.0 | Included |
| C. A. Gordon, *Epitome of the Reports… Chinese Imperial Maritime Customs Service* | Published 1884; compiles reports from 1871–1882 | 464-canvas IIIF manifest, 25 ALTO candidate pages and 6 selected page images downloaded | Wellcome manifest explicitly records Public Domain Mark 1.0 and free reuse | Included |
| Shanghai Municipal Council, *Report for the year 1898 and budget for the year 1899* | 1898 activity / 1899 publication | Catalogue HTML saved; catalogue says 432 pages, full text and 10.5 MB PDF | Item-level licence not found; site footer says All Rights Reserved | Excluded pending clarification |

## Version and integrity controls

- Stable source and source-version identifiers are in `experiments/data_feasibility_pilot/manifests/source_manifest.jsonl`.
- Every local raw and processed file is enumerated with byte size and SHA-256 in `experiments/data_feasibility_pilot/manifests/file_inventory_sha256.json`.
- Every selected page has a stable page identifier, provider page/leaf locator, printed page number, OCR path and image path in `experiments/data_feasibility_pilot/manifests/selected_pages.jsonl`.
- The CMMJ provider metadata identifies ABBYY FineReader 11 extended OCR and a 400 ppi scan. The Wellcome OCR is page-level ALTO linked from the IIIF manifest.

## Important temporal distinction

The Wellcome volume is an 1884 publication but it compiles observations dated 1871–1882. It can establish that a statement was available in the compiled publication by 1884, but a passage describing conditions “in 1872–3” is not evidence of conditions in 1884. The CMMJ selections are genuinely published in 1889 or 1890 and therefore fall within the project's central 1880–1899 window.

## Representativeness boundary

The admitted corpus is concentrated in English-language foreign medical, customs and missionary institutions. It provides evidence about what these archival actors wrote, circulated and recorded; it does not represent all late-Qing people, Chinese medical communities, rural populations, women, non-literate groups or regions not covered by treaty-port and mission networks.
