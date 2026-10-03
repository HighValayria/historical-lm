# Five-Day Protocol

## Trigger

Run only when `scripts/check_schedule.py` reports `run_five_day: true`.

## Purpose

Digest the last five days of changes. This layer should not continue open-ended searching.

Five-Day reports must be written in Chinese. Paper titles, dataset names, source names, identifiers, file paths, and required enum values may remain in their original form.

Five-Day must synthesize across all Daily channels, not only papers.

Five-Day must answer: "这5天的新证据对当前研究设计产生了什么影响？"

The authoritative research design is `research_design/RESEARCH_DESIGN.md`.

## Inputs

- recent Daily reports;
- `state/queues.json`;
- `deep_reading` queue;
- `dataset_review` queue;
- `archive_review` queue;
- `method_review` queue;
- `resource_review` queue;
- `evidence/literature_master.csv`;
- `evidence/dataset_registry.csv`;
- `evidence/source_registry.csv`;
- `research_design/RESEARCH_DESIGN.md`;
- `research_design/DESIGN_CHANGELOG.md`;
- auxiliary structured files when needed: `research_design/contribution_map.md`, `research_design/experiment_matrix.csv`.

## Required Actions

1. Deep-read or review only genuinely high-value queued entries across all queue types.
2. Review high-value dataset, archive, method, and resource queue entries.
3. Update `evidence/literature_master.csv`.
4. Update `evidence/dataset_registry.csv`.
5. Update `evidence/source_registry.csv`.
6. Compare new work and resources with the current research design.
7. Judge whether the current contribution is covered or threatened by new literature.
8. Identify reusable data, code, benchmarks, tools, or archive interfaces.
9. Reassess historical-source feasibility.
10. Identify better methods if evidence supports them.
11. Identify new weaknesses in the current design.
12. Write the Five-Day report in Chinese to `reports/five_day/YYYY-MM-DD.md`.
13. Update `research_design/RESEARCH_DESIGN.md` only within the allowed Five-Day scope below.
14. Append a grouped Five-Day entry to `research_design/DESIGN_CHANGELOG.md` for any substantive update to `research_design/RESEARCH_DESIGN.md`.
15. After a successful Five-Day run, update `last_five_day`, increment `five_day_run_count`, and update `last_successful_run` in `state/automation_state.json` only when schedule-update rules allow it.

## Cross-Type Questions

Five-Day must answer:

- 过去5天文献发生了什么变化？
- 数据生态发生了什么变化？
- 史料可行性发生了什么变化？
- 方法工具发生了什么变化？
- 研究资源是否降低了实际工作量？
- 哪些变化真正影响研究设计？

## Protected Contribution Candidates

- historical ignorance;
- provenance / source ecology;
- multi-level anachronism;
- late-Qing Chinese public health;
- archive-dependent historical cognition.

## Design Change Rule

Five-Day may update `research_design/RESEARCH_DESIGN.md`, but only for:

- new evidence;
- Evidence For / Against;
- Open Questions;
- Blockers;
- Next Research Priorities;
- Contribution Claims evidence-strength status;
- data-source status;
- benchmark maturity;
- candidate-method status.

Five-Day must not lightly change:

- Core Research Question;
- Research Questions;
- Current Research Story;
- core contribution definitions;
- the overall experimental paradigm.

If Five-Day judges that any core section should change, do not implement that change in `research_design/RESEARCH_DESIGN.md`. Instead, include this exact marker in the Five-Day report:

```text
PROPOSED MAJOR DESIGN CHANGE
```

and explain the proposed change for Half-Month review.

Any substantive Five-Day update to `research_design/RESEARCH_DESIGN.md` must append to `research_design/DESIGN_CHANGELOG.md` using:

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

The Five-Day report may also include this Chinese section:

```text
## 拟议研究设计变更
```
