# Five-Day Protocol

## Trigger

Run only when `scripts/check_schedule.py` reports `run_five_day: true`.

## Purpose

Digest the last five days of changes. This layer should not continue open-ended searching.

Five-Day reports must be written in Chinese. Paper titles, dataset names, source names, identifiers, file paths, and required enum values may remain in their original form.

Five-Day must synthesize across all Daily channels, not only papers.

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
- `research_design/CURRENT_RESEARCH_DESIGN.md`.

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
13. After a successful Five-Day run, update `last_five_day`, increment `five_day_run_count`, and update `last_successful_run` in `state/automation_state.json`.

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

Five-Day may recommend changes but must not edit `research_design/CURRENT_RESEARCH_DESIGN.md`.

If design changes are needed, include this Chinese section:

```text
## 拟议研究设计变更
```
