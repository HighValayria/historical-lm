# Access Probe Summary

Probe command:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File probes/data_access/probe_sources.ps1
```

The first sandboxed run failed with remote-connection errors. The same metadata-only probe succeeded when run with approved network access.

| Source ID | Status | HTTP | Content type | Observed bytes | Title signal | Raw metadata |
|---|---|---:|---|---:|---|---|
| SRC-CUSTOMS-WELLCOME | reachable | 200 | text/html; charset=utf-8 | 533508 | Wellcome item for C. A. Gordon customs medical reports epitome | `data/raw/access_probe/SRC-CUSTOMS-WELLCOME_http_metadata.json` |
| SRC-CMMJ-CRL | reachable | 200 | text/html; charset=UTF-8 | 55786 | The China medical missionary journal, 1894 | `data/raw/access_probe/SRC-CMMJ-CRL_http_metadata.json` |
| SRC-SMC-BNASIE | reachable | 200 | text/html; charset=utf-8 | 12306 | Report for the year 1898 and budget for the year 1899 | `data/raw/access_probe/SRC-SMC-BNASIE_http_metadata.json` |
| SRC-CUSTOMS-AS | reachable | 200 | text/html; charset=UTF-8 | 20509 | Academia Sinica customs portal | `data/raw/access_probe/SRC-CUSTOMS-AS_http_metadata.json` |

## Interpretation

- The selected source candidates have live web entry points suitable for item-level follow-up.
- The probe does not establish permission for bulk download, OCR reuse, or large-scale text mining.
- The strongest next probes are OCR/text availability for Wellcome, CRL, and bnAsie items, plus manual navigation of the Academia Sinica customs interface.

