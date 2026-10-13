# Data Feasibility Pilot Table Schema

| Table | Purpose | Rows | Metrics/fields | Data source | Replacement owner |
|---|---|---|---|---|---|
| Source acquisition table | report actual access and local assets | one row per digital version | source/work/version IDs, date, rights signal, access result, files, bytes, hashes | download/source manifests | pilot controller |
| Page quality table | summarize sampled page quality | one row per page | page ID, printed/digital page, OCR layer, layout, defects, verification status | page manifest and quality records | pilot controller |
| Evidence passage table | show traceable historical evidence | one row per passage | passage ID, page ID, raw OCR, verified text, topic, provenance, uncertainty | passage JSONL | pilot controller |
| Trial item distribution | characterize pilot questions | grouped rows | type, source, date, language, answerability, evidence status | item JSONL | pilot controller |
| Baseline results | compare B0/B1/B2 if gate passes | condition x item family | coded outcomes and raw-output links; no fabricated cells | real model logs only | pilot controller |

All tables must be generated from real manifests or explicitly marked as pending. No mock numerical results are permitted in the final pilot report.

## Research Validity Pilot tables

| Table | Rows | Purpose | Source |
|---|---:|---|---|
| Item construct audit | 20 | primary/secondary construct, leakage, fairness, dependence and disposition | `audit/item_audit.csv` |
| Factorial packet inventory | 72 | E0/E1/E2/E3 prompt hashes and factor flags | `factorial/prompt_packets_v2.jsonl` |
| Blind transcription review | 12 | second-pass review without prior transcription labels | `adjudication/blind_transcription_tasks.jsonl` |
| Blind item review | 20 | answerability, construct and acceptable-answer review | `adjudication/blind_item_tasks.jsonl` |
| Scoring ledger | 72 empty rows | independent dimension scores; remains empty until real outputs | `model_runs/scoring_ledger.csv` |

No baseline-results table is authorized until raw model responses and annotator records exist.

