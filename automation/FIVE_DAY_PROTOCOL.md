# Five-Day Protocol

## Trigger

Run only when `scripts/check_schedule.py` reports `run_five_day: true`.

## Purpose

Digest the last five days of changes. This layer should not continue open-ended searching.

Five-Day reports must be written in Chinese. Paper titles, dataset names, source names, identifiers, file paths, and required enum values may remain in their original form.

## Inputs

- recent Daily reports;
- `state/queues.json`;
- new high-relevance papers;
- new datasets;
- new historical sources;
- `evidence/literature_master.csv`;
- `evidence/dataset_registry.csv`;
- `evidence/source_registry.csv`;
- `research_design/CURRENT_RESEARCH_DESIGN.md`.

## Required Actions

1. Deep-read only genuinely high-value queued papers or sources.
2. Update `evidence/literature_master.csv`.
3. Update `evidence/dataset_registry.csv`.
4. Update `evidence/source_registry.csv`.
5. Compare new work with the current research design.
6. Judge whether the current contribution is covered by new work.
7. Identify reusable data, code, or benchmarks.
8. Reassess historical-source feasibility.
9. Identify better methods if evidence supports them.
10. Identify new weaknesses in the current design.
11. Write the Five-Day report in Chinese to `reports/five_day/YYYY-MM-DD.md`.
12. After a successful Five-Day run, update `last_five_day`, increment `five_day_run_count`, and update `last_successful_run` in `state/automation_state.json`.

## Protected Contribution Candidates

- historical ignorance;
- provenance / source ecology;
- multi-level anachronism;
- late-Qing Chinese public health;
- archive-dependent historical cognition.

## Design Change Rule

Five-Day may recommend changes but must not edit `research_design/CURRENT_RESEARCH_DESIGN.md`.

If design changes are needed, include this Chinese section:

```text
## 拟议研究设计变更
```
