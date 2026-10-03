# Five-Day 协议

## 触发条件

仅当 `scripts/check_schedule.py` 返回 `run_five_day: true` 时运行。

## 目的

消化过去五天的新增变化。Five-Day 不应继续做开放式搜索。

Five-Day 报告必须使用中文。论文标题、数据集名称、来源名称、标识符、文件路径和必要枚举值可以保留原文。

Five-Day 必须综合所有 Daily 通道，不得只总结论文。

Five-Day 必须回答：“这5天的新证据对当前研究设计产生了什么影响？”

正式研究设计主文档是 `research_design/RESEARCH_DESIGN.md`。

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
- `research_design/RESEARCH_DESIGN.md`；
- `research_design/DESIGN_CHANGELOG.md`；
- 必要时读取辅助结构化文件：`research_design/contribution_map.md`、`research_design/experiment_matrix.csv`。

## 必须执行的动作

1. 只深读或复核各类队列中真正高价值的条目。
2. 复核高价值的数据集、档案、方法和资源队列条目。
3. 更新 `evidence/literature_master.csv`。
4. 更新 `evidence/dataset_registry.csv`。
5. 更新 `evidence/source_registry.csv`。
6. 将新增工作和资源与当前研究设计进行比较。
7. 判断当前贡献是否被新文献覆盖或威胁。
8. 识别可复用的数据、代码、benchmark、工具或档案接口。
9. 重新评估历史来源可行性。
10. 在证据支持时识别更合适的方法。
11. 识别当前设计中的新弱点。
12. 用中文写入 Five-Day 报告：`reports/five_day/YYYY-MM-DD.md`。
13. 仅在 Five-Day 允许范围内更新 `research_design/RESEARCH_DESIGN.md`。
14. 如果对 `research_design/RESEARCH_DESIGN.md` 做了实质更新，向 `research_design/DESIGN_CHANGELOG.md` 追加一条合并的 Five-Day 记录。
15. 成功运行后，仅在调度更新规则允许时，更新 `state/automation_state.json` 中的 `last_five_day`、`five_day_run_count` 和 `last_successful_run`。

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

## 研究设计变更规则

Five-Day 可以更新 `research_design/RESEARCH_DESIGN.md`，但只能涉及以下内容：

- 新证据；
- 支持 / 反对证据（Evidence For / Against）；
- 开放问题（Open Questions）；
- 阻塞项（Blockers）；
- 下一步研究优先级（Next Research Priorities）；
- 贡献主张（Contribution Claims）的证据强弱状态；
- 数据源状态；
- benchmark 成熟度；
- 候选方法状态。

Five-Day 不得轻易修改：

- Core Research Question；
- 研究问题组（Research Questions）；
- 当前研究叙事（Current Research Story）；
- 核心贡献定义；
- 整体实验范式。

如果 Five-Day 判断核心部分需要变化，不得直接写入 `research_design/RESEARCH_DESIGN.md`。必须在 Five-Day 报告中加入以下固定标记：

```text
PROPOSED MAJOR DESIGN CHANGE
```

并说明拟议变更，交由 Half-Month 审查。

任何 Five-Day 对 `research_design/RESEARCH_DESIGN.md` 的实质更新，都必须在 `research_design/DESIGN_CHANGELOG.md` 中追加以下格式：

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

Five-Day 报告也可以包含以下中文小节：

```text
## 拟议研究设计变更
```
