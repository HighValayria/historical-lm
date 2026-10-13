# Task Packet: Data Feasibility Pilot

- Node ID: DFP-2026-10-13
- Stage: S3 experiments, with data-access and evidence gates before model evaluation
- Objective: turn a small number of openly accessible late-Qing public-health sources into locally preserved, page-traceable, manually checked evidence and determine whether they support a valid pilot benchmark.
- Dependencies: completed T00-T62 exploration; N00-N04 from `state/NEXT_RUN_BACKLOG.yaml`.
- Files to read: project charter, formal research design, source registries, current pilot benchmark, blocker records, and source access probe outputs.
- Files allowed to edit: `experiments/data_feasibility_pilot/`, `data/raw/data_feasibility_pilot/`, `data/processed/data_feasibility_pilot/`, `reports/data_feasibility_pilot/`, `scripts/data_feasibility_pilot/`, planning/review files, blocker state, and append-only project logs/state needed for this pilot.
- Required skills: experiment-results-planning, PDF inspection, verification.
- Evidence inputs: only public archive metadata, openly downloadable source files, scan pages, archive-supplied OCR, and manually checked transcriptions. Generated text is not historical evidence.
- Required artifacts: access/rights report; download manifest with hashes; source/work/version/page metadata; 10-20 page sample where feasible; OCR/transcription quality audit; passage evidence bank; trial items; phase/status report; final pilot report.
- Rejection checks: no paywall bypass; no bulk restricted download; no unstated license inference; no metadata presented as body text; no passage without page-level provenance; no synthetic historical evidence; no paid model calls.
- Phase D gate: run B0/B1/B2 only if Phase C yields enough page-grounded items for meaningful analysis. Otherwise stop at Phase C and record the blocker.
- Validation commands: JSON/JSONL parse checks; SHA-256 verification; PDF metadata/page-count checks; sampled page renders; provenance referential-integrity check; benchmark schema check; git diff review.
- Completion criteria: at least one genuinely local primary-source asset and a defensible feasibility conclusion; preferred target is two source ecologies, 10-20 sampled pages, at least four verified passages, and a small page-grounded item set.
- Stopping criteria: access or reuse terms prohibit the sample; source identity cannot be established; files cannot be linked to stable page metadata; or evidence remains insufficient for valid model comparison.
- Risks: English institutional-source concentration; OCR distortion; publication date versus report date ambiguity; incomplete page labels; archive-version duplication; overinterpreting non-attestation.

## Outcome (2026-10-13)

- Status: completed through DFP-C and DFP-E; DFP-D configured but not executed.
- Data: two admitted public-domain works, 14 selected pages, 47,479 OCR characters, 12 visually checked passages.
- Evaluation development: 20 trial items in 11 evidence-independence groups and 60 frozen B0/B1/B2 prompt packets.
- Verification: referential integrity, file existence, SHA-256 inventory and prompt hashes passed `scripts/data_feasibility_pilot/verify_pilot.py`.
- Blocking conditions: no controlled model interface, no independent historical adjudication, unclear bnAsie reuse terms, and English institutional-source concentration.

