# Five-Day 协议

## 触发条件

仅当 `scripts/check_schedule.py` 返回 `run_five_day: true` 时运行。

## 目的

消化过去五天的新增变化。Five-Day 不应继续做开放式搜索。

Five-Day 报告必须使用中文。论文标题、数据集名称、来源名称、标识符、文件路径和必要枚举值可以保留原文。

Five-Day 必须综合所有 Daily 通道，不得只总结论文。

Five-Day 必须回答：“这5天的新证据对当前研究设计产生了什么影响？”

Five-Day 的正式权限是：**synthesis + revision proposal only**。

正式研究设计主文档是 `research_design/RESEARCH_DESIGN.md`。Five-Day 可以读取它，但不得修改它。

## 输入

- 最近的 Daily 报告；
- `state/queues.json`；
- `deep_reading` 队列；
- `dataset_review` 队列；
- `archive_review` 队列；
- `method_review` 队列；
- `resource_review` 队列；
- `evidence/literature_master.csv`；
- `evidence/dataset_registry.csv`；
- `evidence/source_registry.csv`；
- `research_design/CURRENT.md`；
- `research_design/RESEARCH_DESIGN.md`；
- 必要时读取辅助结构化文件：`research_design/contribution_map.md`、`research_design/experiment_matrix.csv`。

## 可以执行的动作

1. 只深读或复核各类队列中真正高价值的条目。
2. 复核高价值的数据集、档案、方法和资源队列条目。
3. 更新 `evidence/literature_master.csv`。
4. 更新 `evidence/dataset_registry.csv`。
5. 更新 `evidence/source_registry.csv`。
6. 更新 `state/queues.json`。
7. 将新增工作和资源与当前研究设计进行比较。
8. 判断当前设计受到什么影响，以及当前贡献是否被新文献覆盖或威胁。
9. 识别可复用的数据、代码、benchmark、工具或档案接口。
10. 重新评估历史来源可行性。
11. 在证据支持时识别更合适的方法。
12. 识别当前设计中的新弱点。
13. 用中文写入 Five-Day 报告：`reports/five_day/YYYY-MM-DD.md`。
14. 如果认为研究设计需要变化，只在 Five-Day 报告中提出 `PROPOSED DESIGN REVISION`。
15. 成功运行后，仅在调度更新规则允许时，更新 `state/automation_state.json` 中的 `last_five_day`、`five_day_run_count` 和 `last_successful_run`。

## Five-Day 不得执行的动作

Five-Day 不得：

- 修改 `research_design/RESEARCH_DESIGN.md`；
- 修改 `research_design/CURRENT.md`；
- 修改 `research_design/VERSION_LOG.md`；
- 创建新研究设计版本；
- 修改 `research_design/archive/`；
- 修改 archive 中的历史版本；
- 将 proposal 写成正式设计结论。

## 跨类型问题

Five-Day 必须回答：

- 过去5天文献发生了什么变化？
- 数据生态发生了什么变化？
- 史料可行性发生了什么变化？
- 方法工具发生了什么变化？
- 研究资源是否降低了实际工作量？
- 哪些变化真正影响研究设计？

## 受保护的贡献候选

- historical ignorance；
- provenance / source ecology；
- multi-level anachronism；
- late-Qing Chinese public health；
- archive-dependent historical cognition。

## Revision Proposal 规则

如果 Five-Day 判断以下任何部分必须改变，只能提出 proposal，等待 Half-Month 决定是否创建新的正式版本：

- RQ；
- research story；
- primary contribution；
- benchmark framework；
- experimental paradigm；
- source strategy；
- Core Research Question；
- Research Questions；
- Current Research Story；
- Contribution Claims；
- Conceptual Framework；
- Benchmark Design；
- Experimental Design。

Five-Day 报告中的 proposal 使用固定标记：

```text
PROPOSED DESIGN REVISION
```

proposal 应说明：

- 建议修改什么；
- 为什么已有证据支持该建议；
- 涉及哪些 legacy / Daily / Five-Day 证据；
- 建议由 Half-Month 审查的优先级。

Five-Day 报告也可以包含以下中文小节：

```text
## 拟议研究设计修订
```
