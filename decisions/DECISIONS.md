# Decisions

| Decision ID | Date | Node | Decision | Rationale | Evidence | Revisit trigger |
|---|---|---|---|---|---|---|
| D-0001 | 2026-07-17 | T00 | Use English for structured repository artifacts in this run. | Several existing Chinese files display mojibake in the terminal, while ASCII/English files are safer for scripts and diffs. | Local file reads on 2026-07-17. | If repository encoding is normalized later. |
| D-0002 | 2026-07-17 | T10 | Prioritize source-grounded evaluation before adaptation. | The literature landscape has many adaptation methods but no ready late-Qing public-health anachronism benchmark. | `evidence/literature_matrix.md`. | If T30/T31 show source access is too weak for a benchmark. |
| D-0003 | 2026-07-17 | T11 | Treat subscription Chinese newspaper/periodical databases as authorized-access extensions, not first-run bulk corpora. | Access notes and library/provider terms indicate subscription access and batch-download limits. | `evidence/source_registry.md`. | If the user provides institutional access and explicit permission-compatible terms. |
| D-0004 | 2026-07-17 | T12 | Model evaluation should include historically appropriate abstention as a positive behavior. | The concept map distinguishes not-yet-known, not-attested, not-accessible, and post-cutoff states. | `evidence/concept_map.md`. | If pilot annotators cannot apply the labels consistently. |
