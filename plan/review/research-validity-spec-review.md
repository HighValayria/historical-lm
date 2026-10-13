# Research Validity Pilot — Specification Compliance Review

Date: 2026-10-13
Reviewer: Codex primary agent (self-review; not independent historical adjudication)

| Requirement | Status | Evidence |
|---|---|---|
| Audit all 20 questions by research capability | pass | `audit/item_audit.jsonl`, 20 unique IDs |
| Separate direct-use, revise, control and unsuitable | pass | 10 / 2 / 7 / 1 disposition counts |
| Identify ordinary reading vs genuine temporal items | pass | Q017 is the sole direct temporal item; 7 controls |
| Preserve original/frozen version | pass | frozen manifest has four input hashes; revisions are under RVP paths |
| Build E0/E1/E2/E3 without answer leakage | pass | 72 packets; structural/leakage checks pass |
| Record full prompts and hashes | pass | every packet has canonical SHA-256 |
| Separate scoring dimensions; no composite | pass | eight-dimension framework and empty ledger |
| Prepare second-round review and disputes | pass as preparation | 12 passage tasks, 20 item tasks, queue; independent completed = 0 |
| Provide controlled inference and real results if possible | partial by environment | adapter and dry run pass; no authorized interface, 0 outputs |
| Reassess A/B/C directions | pass | direction report and final report |
| Avoid new bulk collection/training | pass | no download, paid API, RAG build or training performed |
| Answer Q1–Q6 | pass | final report section 8 |

Overall: **PASS for the achievable scope; model-result requirement correctly remains unexecuted rather than fabricated.** The deliverable is an experiment-ready development pilot, not a validated benchmark or completed baseline study.
