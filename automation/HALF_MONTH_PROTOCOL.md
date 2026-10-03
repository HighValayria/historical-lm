# Half-Month 协议

## 触发条件

仅当 `scripts/check_schedule.py` 返回 `run_half_month: true` 时运行。

## 目的

审计研究方向，并且只有在证据支持时才进行正式研究设计更新。

Half-Month 报告必须使用中文。论文标题、数据集名称、来源名称、标识符、文件路径和必要枚举值可以保留原文。

正式研究设计主文档是 `research_design/RESEARCH_DESIGN.md`。

Half-Month 是唯一允许正式重构核心研究设计部分的自动化层级，包括：

- 核心研究问题（Core Research Question）；
- 研究问题组（Research Questions）；
- 当前研究叙事（Current Research Story）；
- 贡献主张（Contribution Claims）；
- 概念框架（Conceptual Framework）；
- Benchmark 设计（Benchmark Design）；
- 实验设计（Experimental Design）；
- 假设（Hypotheses）；
- 优先级（Priorities）；
- 拒绝 / 暂缓方向（Rejected / Deferred Directions）。

`research_design/contribution_map.md` 和 `research_design/experiment_matrix.csv` 等辅助结构化文件可以保留给自动化使用，但 `research_design/RESEARCH_DESIGN.md` 是正式主文档。若辅助文件与主文档冲突，以主文档为准。Half-Month 更新主文档后，若辅助文件仍然有用，应同步更新。

## 输入

- 最近的 Daily 报告；
- 最近的 Five-Day 报告；
- `evidence/literature_master.csv`；
- `evidence/dataset_registry.csv`；
- `evidence/source_registry.csv`；
- `state/blockers.json`；
- `state/queues.json`；
- `research_design/RESEARCH_DESIGN.md`；
- `research_design/DESIGN_CHANGELOG.md`；
- `research_design/contribution_map.md`；
- `research_design/experiment_matrix.csv`。

## 必须回答的问题

1. 当前研究问题是否仍然成立？
2. 核心创新是否已经被新工作覆盖？
3. 哪些贡献正在增强？
4. 哪些贡献正在减弱？
5. 数据可行性是否发生变化？
6. Historical RAG 是否仍是合适路线？
7. benchmark 分类是否需要调整？
8. historical ignorance 是否仍值得作为主要贡献？
9. provenance / source ecology 是否应进一步强化？
10. 是否已有足够证据启动真实试点实验？
11. 未来 15 天自动化应聚焦什么？
12. 是否已有足够证据进行重大选题重构？

## 必须执行的动作

1. 阅读当前 `research_design/RESEARCH_DESIGN.md`。
2. 阅读过去 15 天的 Daily 报告、Five-Day 报告、registry、queue 和 blocker。
3. 重新审计研究问题、创新性、数据、benchmark、实验和优先级。
4. 如果证据支持核心变化，更新 `research_design/RESEARCH_DESIGN.md`，使其能够独立反映当前完整研究方案。
5. 如果辅助结构化文件仍然保留且受影响，在更新主文档后同步这些辅助文件。
6. 用中文写入 Half-Month 报告：`reports/half_month/YYYY-MM-DD.md`；报告负责解释为什么改变或为什么不改变。
7. 如果 `research_design/RESEARCH_DESIGN.md` 被修改，向 `research_design/DESIGN_CHANGELOG.md` 追加以下格式的记录：

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

Half-Month 的核心设计变化必须逐项记录。

8. 成功运行后，仅在调度更新规则允许时，更新 `state/automation_state.json` 中的 `last_half_month`、`half_month_run_count` 和 `last_successful_run`。

不得无声改变研究方向。
