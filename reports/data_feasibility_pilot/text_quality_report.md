# Text quality report

## Sample and method

The quality sample contains 14 purposively selected English pages: 8 from the 1889–1890 *China Medical Missionary Journal* (CMMJ) text PDF and 6 from the 1884 Wellcome digitization of C. A. Gordon's customs medical-report epitome. The selected OCR totals 47,479 characters and 7,956 whitespace-delimited words.

Twelve short passages (3,706 verified characters) were compared once against rendered scan pages. Character divergence was calculated with Levenshtein distance after collapsing whitespace. The micro rate was 1.35%. This is **not** a whole-document accuracy estimate: the sample is small and purposive, the verification is single-pass, and typographic normalization and punctuation changes count as edits.

## Observed quality

| Layer/source | Finding | Consequence |
|---|---|---|
| CMMJ text PDF | Running prose is generally readable; titles, names and dates are searchable | Suitable for candidate-page discovery and preliminary passage extraction |
| CMMJ table/list layout | Reading order and digits can fail; the page-74 OCR gives 6,807 where the scan gives 5,807 | Any quantitative item requires image-level verification |
| CMMJ typography | `6th` became `Gth`, `I` became `1`, soft line-break marks remain, and ligatures such as `œ` can be lost | Dates, initials and historical spelling cannot be trusted without checking the scan |
| Wellcome ALTO | The selected prose pages are highly readable and maintain page-level tokens | Useful for full-text discovery and evidence extraction |
| Wellcome ALTO | Errors include `arc/are`, `tho/the`, `bo/be`, `remaiu/remain`, and occasional marginal-label intrusion | Search recall is good, but quotations and named entities need verification |
| Both sources | Page headers, side labels, multi-column layouts and editorial summaries may enter the same token stream as body text | Chunking must use page/layout boundaries rather than blind fixed windows |

The largest checked snippet divergence was the CMMJ statistical list (8.70%), driven by layout/punctuation changes and the consequential 5,807/6,807 digit error. Most prose snippets had low divergence, but low aggregate error does not imply low factual risk: one incorrect date, place, drug name or number can invalidate an evaluation item.

## Layer separation

- Provider OCR is preserved in `data/processed/data_feasibility_pilot/ocr/`.
- Short, visually checked text is stored separately as `verified_transcription` in `data/processed/data_feasibility_pilot/transcription/verified_passages.jsonl`.
- Interpretive modern paraphrases are stored as `normalized_text` and are not treated as historical evidence.
- Each passage carries a `caution` field for source bias, evidentiary strength or temporal ambiguity.

## Metadata quality

The CMMJ source has stable Internet Archive identifier, explicit volume information, page-count metadata, printed-page mapping and an explicit Public Domain Mark. The volume transition is identifiable: Volume IV (1890) starts at PDF page 231. Wellcome provides a stable work page, b-number, IIIF manifest, 464 canvases, printed page labels, ALTO links and explicit Public Domain Mark terms.

The main metadata hazard is temporal: the Wellcome work was published in 1884 but compiles reports from 1871–1882. Each benchmark item must distinguish publication availability from the date of the observation it summarizes.

## Fitness judgment

The two OCR layers are fit for discovery, limited full-text retrieval and human-verified evidence extraction. They are not fit for unattended benchmark generation or for accepting numbers, dates and proper names without scan checks. A formal benchmark needs double review or adjudication and should preserve the original image alongside every evidence passage.
