# Half-Month Protocol

## Trigger

Run only when `scripts/check_schedule.py` reports `run_half_month: true`.

## Purpose

Audit the research direction and make formal design updates only when evidence supports them.

Half-Month reports must be written in Chinese. Paper titles, dataset names, source names, identifiers, file paths, and required enum values may remain in their original form.

The authoritative research design is `research_design/RESEARCH_DESIGN.md`.

Half-Month is the only automation layer allowed to formally restructure core research-design sections, including:

- Core Research Question;
- Research Questions;
- Current Research Story;
- Contribution Claims;
- Conceptual Framework;
- Benchmark Design;
- Experimental Design;
- Hypotheses;
- Priorities;
- Rejected / Deferred Directions.

Auxiliary structured files such as `research_design/contribution_map.md` and `research_design/experiment_matrix.csv` may be retained for automation, but `research_design/RESEARCH_DESIGN.md` is authoritative. If auxiliary files conflict with it, the main design document prevails. After Half-Month updates the main document, retained auxiliary files should be synchronized when they still matter.

## Inputs

- recent Daily reports;
- recent Five-Day reports;
- `evidence/literature_master.csv`;
- `evidence/dataset_registry.csv`;
- `evidence/source_registry.csv`;
- `state/blockers.json`;
- `state/queues.json`;
- `research_design/RESEARCH_DESIGN.md`;
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

1. Read the current `research_design/RESEARCH_DESIGN.md`.
2. Read the last 15 days of Daily reports, Five-Day reports, registries, queues, and blockers.
3. Re-audit the research question, innovation, data, benchmark, experiment, and priorities.
4. If evidence supports core changes, update `research_design/RESEARCH_DESIGN.md` so it independently reflects the full current research plan.
5. If auxiliary structured files are still retained and affected, synchronize them after updating the main design document.
6. Write the Half-Month report in Chinese to `reports/half_month/YYYY-MM-DD.md`; the report explains why changes were or were not made.
7. If `research_design/RESEARCH_DESIGN.md` is changed, append entries to `research_design/DESIGN_CHANGELOG.md` with:

```text
Date:
Cycle:
Section:
Previous:
New:
Reason:
Evidence:
Confidence:
```

Half-Month core design changes must be recorded item by item.

8. After a successful Half-Month run, update `last_half_month`, increment `half_month_run_count`, and update `last_successful_run` in `state/automation_state.json` only when schedule-update rules allow it.

Never silently change the research direction.
