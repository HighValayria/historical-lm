# Task Journal

## T00 - Bootstrap workspace and protocols

- Date: 2026-07-17.
- Status: completed.
- Actions: read governing files, inspected the repository, initialized working directories and core tracking files.
- Artifacts: `plan/*`, `evidence/*`, `reports/nodes/T00.md`, `logs/task_journal.md`, `decisions/DECISIONS.md`, `assumptions/ASSUMPTIONS.md`, `blockers/BLOCKERS.md`, `failures/FAILURES.md`, `state/run_state.json`.
- Changed assumptions: none.
- Decisions: use English machine-readable repository artifacts to avoid encoding drift; final chat summaries can be Chinese.
- Blockers: none.
- Next ready nodes: T10, T11, T12.

## T10 - Research and method landscape

- Date: 2026-07-17.
- Status: completed.
- Actions: collected and normalized method/literature evidence on temporal NLP, historical language models, RAG, PEFT, and late-Qing public-health conceptual history.
- Artifacts: `evidence/literature_matrix.md`, `evidence/evidence_map.md`, `reports/nodes/T10.md`.
- Changed assumptions: source-grounded benchmark design should precede any substantial adaptation work.
- Decisions: treat post-1900 sources as contrastive foils unless explicitly marked otherwise.
- Blockers: no hard blocker; close reading is still needed for fine-grained historical claims.
- Next ready nodes: T11 and T12 remain running.

## T11 - Historical source and access landscape

- Date: 2026-07-17.
- Status: completed.
- Actions: mapped archive/database candidates, access modes, OCR/text signals, metadata quality, bulk-use feasibility, and source-population bias.
- Artifacts: `evidence/source_registry.md`, `evidence/evidence_map.md`, `reports/nodes/T11.md`.
- Changed assumptions: first pilot should be framed around accessible source ecologies, likely treaty-port/customs/missionary/municipal materials, not all late-Qing China.
- Decisions: subscription newspaper/periodical databases are not bulk sources unless explicit institutional authorization is obtained.
- Blockers: unauthorized bulk use of Shen Bao, late-Qing periodical databases, ProQuest-style products, and some commercial gazetteer platforms.
- Next ready nodes: T12 remains running.

## T12 - Digital-humanities concept map

- Date: 2026-07-17.
- Status: completed.
- Actions: defined project concepts, converted them into benchmark indicators, and drafted a label schema for historically bounded answers.
- Artifacts: `evidence/concept_map.md`, `evidence/evidence_map.md`, `reports/nodes/T12.md`.
- Changed assumptions: the benchmark must reward historically appropriate ignorance and provenance caveats.
- Decisions: anachronism will be treated as a multi-label taxonomy, not a single error class.
- Blockers: none.
- Next ready node: T20.

## T20 - Generate candidate research questions

- Date: 2026-07-17.
- Status: completed.
- Actions: generated seven candidate research questions from T10/T11/T12 evidence.
- Artifacts: `reports/candidate_research_questions.md`, `reports/nodes/T20.md`.
- Changed assumptions: strong candidates should combine source criticism, benchmark design, and lightweight technical evaluation.
- Decisions: defer model adaptation comparisons until after data and benchmark probes.
- Blockers: none.
- Next ready node: T21.

## T21 - Score and select candidate directions

- Date: 2026-07-17.
- Status: completed.
- Actions: scored seven candidates on the six configured dimensions and selected a primary direction.
- Artifacts: `reports/candidate_topic_scorecard.md`, `reports/recommended_direction.md`, `reports/nodes/T21.md`.
- Changed assumptions: first probes should support benchmark construction and lightweight historical RAG, not adaptation.
- Decisions: C1 is selected as the primary direction; C2/C5/C7 are support/alternative paths.
- Blockers: none.
- Next ready nodes: T30, T40, T50.

## T30 - Probe real data access

- Date: 2026-07-17.
- Status: completed.
- Actions: created and ran a metadata-only source access probe for four high-priority source candidates.
- Artifacts: `probes/data_access/probe_sources.ps1`, `probes/data_access/access_probe_results.json`, `probes/data_access/access_probe_summary.md`, `data/raw/access_probe/*_http_metadata.json`, `reports/nodes/T30.md`.
- Changed assumptions: there are enough reachable item-level source entry points for a small pilot.
- Decisions: continue with small item-level probes; do not infer bulk permissions from HTTP 200 pages.
- Blockers: OCR/text availability and reuse terms remain unresolved for T31.
- Next ready nodes: T31; T40 and T50 are also ready from T21.

## T31 - Probe OCR and metadata quality

- Date: 2026-07-17.
- Status: completed.
- Actions: created and ran a link/keyword probe for OCR, full-text, PDF, download, IIIF, rights, date, and title signals on T30-reachable pages.
- Artifacts: `probes/ocr/probe_text_signals.ps1`, `probes/ocr/ocr_metadata_probe_results.json`, `probes/ocr/ocr_metadata_probe_summary.md`, `reports/nodes/T31.md`.
- Changed assumptions: first benchmark should use curated excerpts and metadata, not a presumed clean OCR corpus.
- Decisions: prioritize Wellcome/CRL and possibly bnAsie for item-level text follow-up; treat Academia Sinica portal as discovery/manual-navigation source for now.
- Blockers: actual OCR accuracy remains unmeasured; no explicit OCR signal found on probed pages.
- Next ready nodes: T40 and T50; T41 can follow T40.

## T40 - Design anachronism benchmark

- Date: 2026-07-17.
- Status: completed.
- Actions: designed pilot benchmark scope, item families, evidence status values, answer policies, scoring dimensions, and exclusion rules.
- Artifacts: `benchmarks/pilot/benchmark_spec.md`, `benchmarks/pilot/schema.json`, `reports/nodes/T40.md`.
- Changed assumptions: pilot seed data can include metadata-only and post-cutoff control items if they are clearly labelled.
- Decisions: unverified source-grounded items must be marked `needs_source_excerpt` and excluded from scoring.
- Blockers: source-passage extraction still needed for full factual/lexical/causal/value evaluation.
- Next ready node: T41.

## T41 - Build a small pilot benchmark

- Date: 2026-07-17.
- Status: completed.
- Actions: created pilot source records, 12 seed benchmark items, and annotation guidelines.
- Artifacts: `benchmarks/pilot/source_records.jsonl`, `benchmarks/pilot/pilot_items.jsonl`, `benchmarks/pilot/annotation_guidelines.md`, `reports/nodes/T41.md`.
- Changed assumptions: current seed is ready for schema/prototype validation, not full historical scoring.
- Decisions: passage-dependent items are labelled `needs_source_excerpt` and excluded from scoring.
- Blockers: verified historical passages are still required for full factual/lexical/causal/value benchmark items.
- Next ready node: T50 or T51 after T50.

## T50 - Compare technical routes

- Date: 2026-07-17.
- Status: completed.
- Actions: compared prompting, source-provided prompting, local RAG, OCR-first corpus work, DAPT/TAPT, LoRA/QLoRA, and hybrid routes.
- Artifacts: `reports/technical_route_comparison.md`, `reports/nodes/T50.md`.
- Changed assumptions: first engineering probe should validate benchmark and retrieval readiness, not train a model.
- Decisions: T51 will implement a local no-training schema/retrieval/evaluation-readiness prototype.
- Blockers: none.
- Next ready node: T51.

