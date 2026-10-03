# Half-Month Protocol

## Trigger

Run only when `scripts/check_schedule.py` reports `run_half_month: true`.

## Purpose

Audit the research direction and make formal design updates only when evidence supports them.

Half-Month is the only automation layer allowed to change:

- `research_design/CURRENT_RESEARCH_DESIGN.md`;
- `research_design/contribution_map.md`;
- `research_design/experiment_matrix.csv`.

## Inputs

- recent Daily reports;
- recent Five-Day reports;
- `evidence/literature_master.csv`;
- `evidence/dataset_registry.csv`;
- `evidence/source_registry.csv`;
- `state/blockers.json`;
- `state/queues.json`;
- `research_design/CURRENT_RESEARCH_DESIGN.md`;
- `research_design/DESIGN_CHANGELOG.md`;
- `research_design/contribution_map.md`;
- `research_design/experiment_matrix.csv`.

## Required Questions

1. Does the research question still hold?
2. Has the core innovation been covered by new work?
3. Which contributions are strengthening?
4. Which contributions are weakening?
5. Has data feasibility changed?
6. Is Historical RAG still an appropriate route?
7. Should benchmark categories change?
8. Is historical ignorance still worth treating as a main contribution?
9. Should provenance / source ecology be strengthened?
10. Is there enough evidence to start a real pilot experiment?
11. What should the next 15 days of automation focus on?
12. Is there enough evidence for a major topic restructure?

## Required Actions

1. Write the Half-Month report to `reports/half_month/YYYY-MM-DD.md`.
2. If formal design files are changed, append an entry to `research_design/DESIGN_CHANGELOG.md` with:

```text
Date:
Changed:
Previous:
New:
Reason:
Evidence:
Confidence:
```

3. After a successful Half-Month run, update `last_half_month`, increment `half_month_run_count`, and update `last_successful_run` in `state/automation_state.json`.

Never silently change the research direction.
