# Half-Month 协议

## 触发条件

仅当 `scripts/check_schedule.py` 返回 `run_half_month: true` 时运行。

## 目的

审计研究方向，并且只有在证据支持时才决定是否创建新的正式研究设计版本。

Half-Month 报告必须使用中文。论文标题、数据集名称、来源名称、标识符、文件路径和必要枚举值可以保留原文。

正式研究设计主文档是 `research_design/RESEARCH_DESIGN.md`。当前版本由 `research_design/CURRENT.md` 声明，版本历史由 `research_design/VERSION_LOG.md` 记录。

Half-Month 是唯一允许决定正式版本升级的自动化层级。

## 必须首先回答

Half-Month 必须首先回答：

> Does accumulated evidence justify a new formal research-design version?

如果答案是 **NO**：

- 不修改 `research_design/RESEARCH_DESIGN.md`；
- 不修改 `research_design/CURRENT.md`；
- 不修改 `research_design/VERSION_LOG.md`；
- 不创建空版本；
- 不修改 `research_design/archive/`；
- 只输出 Half-Month 审计报告。

如果答案是 **YES**，才允许执行正式版本升级流程。

## 输入

- 当前 `research_design/CURRENT.md`；
- 当前 `research_design/RESEARCH_DESIGN.md`；
- `research_design/VERSION_LOG.md`；
- 最近的 Daily 报告；
- 最近的 Five-Day 报告，尤其是 `PROPOSED DESIGN REVISION`；
- `evidence/literature_master.csv`；
- `evidence/dataset_registry.csv`；
- `evidence/source_registry.csv`；
- `state/blockers.json`；
- `state/queues.json`；
- 必要时读取辅助结构化文件：`research_design/contribution_map.md`、`research_design/experiment_matrix.csv`。

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
12. 是否已有足够证据创建新的正式研究设计版本？

## 若不创建新版本

当 Half-Month 判断不需要新版本时：

1. 用中文写入 Half-Month 报告：`reports/half_month/YYYY-MM-DD.md`。
2. 在报告中说明为什么不创建新版本。
3. 不修改当前正式研究设计或版本文件。
4. 成功运行后，仅在调度更新规则允许时，更新 `state/automation_state.json` 中的 `last_half_month`、`half_month_run_count` 和 `last_successful_run`。

## 若创建新版本

当 Half-Month 判断必须创建新版本时，固定执行：

```text
current RESEARCH_DESIGN.md = vXXX
        ↓
copy/freeze current content as
research_design/archive/RESEARCH_DESIGN_vXXX.md
        ↓
generate complete new
research_design/RESEARCH_DESIGN.md
        ↓
version becomes vXXX+1
        ↓
update research_design/CURRENT.md
        ↓
append research_design/VERSION_LOG.md
```

新版本必须是完整、独立、可人类阅读的研究设计文档，不得只是 diff 或补丁说明。

archive 中的历史版本视为只读冻结快照。自动任务不得修改 archive 中已经归档的版本。

若辅助结构化文件仍然保留且受到新正式版本影响，应在更新主文档后同步这些辅助文件；若未同步，必须在 Half-Month 报告中解释原因。

正式版本升级必须在 Half-Month 报告和 `research_design/VERSION_LOG.md` 中解释：

- 为什么已有证据足以支持新版本；
- 旧版本号；
- 新版本号；
- 归档文件路径；
- 主要变更章节；
- 证据来源；
- 信心等级。

不得无声改变研究方向。
