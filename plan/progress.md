# Progress Log

## 2026-07-17

### Stage

Autonomous exploration. Initial stage classification: S1 evidence and S3 experiment planning, because the run must build a literature/source evidence base and then specify small feasibility probes rather than draft a manuscript.

### T00 Bootstrap

- Status: completed.
- Files initialized for planning, evidence, logs, reports, decisions, blockers, assumptions, failures, probes, benchmark design, and prototypes.
- No historical or literature claims were made during T00.

### Capability-use Audit

- Required skills: paper-orchestration, literature-review, evidence-driven-writing, experiment-results-planning, verification.
- Skills actually used: read local skill instructions for paper-orchestration, literature-review, evidence-driven-writing, experiment-results-planning, verification, and using-research-writing.
- Inputs consumed: governing repository files, current run state, and local skill instructions.
- Inputs not used and why: no external evidence was used in T00 because this node only initializes the workspace.
- Artifacts produced: planning files, evidence templates, logs, T00 node report, and updated run state.
- Verification run: directory and file existence checks are scheduled after file creation.
- Remaining risk: some local skill files are displayed with mojibake, so only unambiguous operational requirements were adopted.

### T10/T11/T12 Branch Start

- Status: running.
- T10 delegated as a read-only research/method landscape branch.
- T11 delegated as a read-only historical source/access landscape branch.
- T12 delegated as a read-only digital-humanities concept-map branch.
- Main-agent responsibility: normalize evidence, verify important claims, write repository artifacts, update state, and commit node boundaries.

### T10 Completion

- Status: completed.
- Main output: `evidence/literature_matrix.md` and `reports/nodes/T10.md`.
- Finding: there is enough adjacent method work to justify a pilot, but the missing piece is a source-grounded late-Qing public-health anachronism benchmark and not another generic temporal-LM experiment.

### Capability-use audit

- Required skills: literature-review, evidence-driven-writing, verification.
- Skills actually used: literature-review, evidence-driven-writing, verification.
- Inputs consumed: T10 subagent report, web source pages, project charter, task graph, config.
- Inputs not used and why: full texts behind access barriers were not used; detailed historical claims were downgraded to partial verification where close reading is pending.
- Artifacts produced: `evidence/literature_matrix.md`, updated `evidence/evidence_map.md`, `reports/nodes/T10.md`, journal/state/decision/assumption updates.
- Verification run: `Select-String` over literature matrix, run-state readback, `git status --short`.
- Remaining risk: some source claims are abstract-level or publisher-metadata-level and need close reading before manuscript use.

### T11 Completion

- Status: completed.
- Main output: `evidence/source_registry.md` and `reports/nodes/T11.md`.
- Finding: open first-round probes should focus on customs, missionary, and municipal-report materials; Chinese newspaper/periodical databases remain important but access-constrained.

### Capability-use audit

- Required skills: literature-review, evidence-driven-writing, verification.
- Skills actually used: literature-review, evidence-driven-writing, verification.
- Inputs consumed: T11 subagent report, archive/library/catalogue pages, project access rules.
- Inputs not used and why: subscription full-text databases were not accessed or bypassed.
- Artifacts produced: `evidence/source_registry.md`, updated `evidence/evidence_map.md`, `reports/nodes/T11.md`, journal/state/decision/assumption/blocker updates.
- Verification run: pending targeted file checks after patch.
- Remaining risk: exact item-level OCR and reuse terms require T30/T31 probes.

### T12 Completion

- Status: completed.
- Main output: `evidence/concept_map.md` and `reports/nodes/T12.md`.
- Finding: the evaluation target should be "source-grounded, historically bounded answering" rather than generic factual QA.

### Capability-use audit

- Required skills: evidence-driven-writing, verification.
- Skills actually used: evidence-driven-writing, verification.
- Inputs consumed: T12 subagent report, T10/T11 outputs, historiography/archival/DH/NLG source metadata.
- Inputs not used and why: one unverified 2026 benchmark-aging source proposed by the subagent was not included in core evidence.
- Artifacts produced: `evidence/concept_map.md`, updated `evidence/evidence_map.md`, `reports/nodes/T12.md`, journal/state/decision/assumption updates.
- Verification run: pending targeted file checks after patch.
- Remaining risk: label definitions need pilot annotation before they can be considered stable.
