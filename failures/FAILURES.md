# Failures and Negative Findings

| Failure ID | Date | Node | Failure or negative finding | Evidence | Impact | Follow-up |
|---|---|---|---|---|---|
| F-0001 | 2026-07-17 | T30 | Initial sandboxed web access probe failed with remote-connection errors for all four source URLs. | `probes/data_access/access_probe_results.json` from first run was overwritten by successful approved run; failure recorded in `probes/data_access/access_probe_summary.md`. | Demonstrated that local sandbox network status can confound access probes. | Re-run required network probes with approved access and record exact command. |
| F-0002 | 2026-07-17 | T31 | No explicit OCR keyword signal was detected on any of the four probed pages. | `probes/ocr/ocr_metadata_probe_results.json`. | The first pilot should not assume ready OCR text. | Use curated excerpts first; later test PDF extraction/OCR on a small item. |
| F-0003 | 2026-07-17 | T51 | `python` was not available on PATH. | Failed command output before rerun. | Local scripts must use bundled Python path or document dependency setup. | Use `C:\Users\33967\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`. |
