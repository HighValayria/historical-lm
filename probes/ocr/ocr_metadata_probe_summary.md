# OCR and Metadata Probe Summary

Probe command:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File probes/ocr/probe_text_signals.ps1
```

| Source ID | Metadata score | Text signal score | Feasibility | Key signals |
|---|---:|---:|---|---|
| SRC-CUSTOMS-WELLCOME | 3 | 3 | high_for_followup | PDF/download/IIIF signals; candidate PDF `https://iiif.wellcomecollection.org/pdf/b20416179`; Public Domain Mark link detected |
| SRC-CMMJ-CRL | 3 | 3 | high_for_followup | Download and IIIF signals; candidate record file/download section detected |
| SRC-SMC-BNASIE | 3 | 2 | medium_for_followup | PDF and full-text signals; candidate PDF `https://www.bnasie.eu/Asset/Source/bnPeriodical_ID-60_No-1.pdf` |
| SRC-CUSTOMS-AS | 3 | 0 | low_without_manual_navigation | Metadata and rights signals, but no direct PDF/full-text/download/IIIF links detected on landing page |

## Interpretation

- OCR is not explicitly advertised on any probed page by the simple keyword test.
- Wellcome and CRL have the strongest signals for immediate item-level follow-up.
- bnAsie has a direct PDF candidate and is likely usable for manual or scripted text extraction if terms permit.
- Academia Sinica's landing page is useful for discovery, but needs manual navigation or documentation before extraction.

## Next-step Implications

- T41 should use small, manually curated source excerpts rather than assume full OCR corpus availability.
- T51 can prototype retrieval over curated snippets and metadata rather than downloaded large corpora.
- Any later OCR task should start with the Wellcome PDF and bnAsie PDF, then evaluate CRL item files.

