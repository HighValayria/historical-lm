# 2026-10-13 手动 Daily 自主科研测试

## 运行身份与边界

- run_id：`manual-daily-20261013T224500+0800`
- 入口：手动 `FORCE_MODE=DAILY`
- 调度写入：`UPDATE_SCHEDULE=false`
- 声明：本报告不是 Scheduled Automation 自动触发记录。
- 预算：最多 1 项 backlog 任务；A1 使用 8 个一手来源；未调用付费模型 API、未下载数据、未训练或运行模型。

## 六通道巡检

| 通道 | 状态 | 实际检查与结果 |
|---|---|---|
| PAPERS | `checked_material_update` | 核验 8 项核心一手工作；新登记 Rewind Time、EvolveBench、Time Sensitive Knowledge Editing，复核 ExAnte、Recall-Based Prompting、Underwood et al.、TCFT、HistoRAG。 |
| DATASETS | `checked_material_update` | 核验 Rewind Time 作者仓库的 factual/semantic/counterfactual 子集及其质量清理记录；登记 EvolveBench 官方仓库。两者许可/条目级出处仍标为未核验。 |
| ARCHIVES | `checked_no_material_update` | 检查 Wellcome Collection 档案指南及 Library of Congress 公共记忆/公共卫生发现页；未发现足以改变当前项目数据判断的新来源，未下载材料。 |
| METHODS | `checked_material_update` | 比较 cutoff prompt、recall prompting、TCFT、历史时间窗口 RAG、时间敏感知识编辑；形成方法—失败机制—潜在缺口矩阵。 |
| RESOURCES | `checked_material_update` | 核验 Rewind Time 作者代码/数据页和 EvolveBench 官方项目入口；资源存在不等于已在本项目复现。 |
| PROJECT_IMPACT | `checked_material_update` | 普通 cutoff prompt 不足以作为唯一提示基线；M2 应突出 cutoff admissibility 与年代证据链；TCFT 是 M3 的近邻竞争工作。影响为 `material`，但不足以修改正式研究设计。 |

## Backlog 执行

- 领取任务：`A1`，Track A，priority 1，依赖为空。
- 交付物：
  - `research/literature/METHOD_LANDSCAPE.md`
  - `research/literature/method_matrix.csv`
- 实际完成：以 8 项一手来源核验核心竞争方法、数据、作者报告结果、适用边界及本项目差异化风险；明确区分作者报告与本项目推断。
- 验收：通过。关键结论均链接到论文官方页/arXiv/作者仓库；矩阵字段分别记录方法、数据、结果、局限、差异化风险和证据状态；未使用自动摘要作为金标准。
- 研究状态边界：没有真实模型实验；旧 20 题未改名；严格验证的时代错置题仍为 0；没有正式研究设计版本变更。

## 状态与异常

- `state/research_execution_state.json`：Daily 从 `running` 收束到 `completed`，并记录本报告及 A1 产物；执行历史的阶段结果为 `success`。
- `state/execution_history.json`：以手动 run_id 记录 start/finish，明确 `UPDATE_SCHEDULE=false`。
- `state/automation_state.json`：应保持 Daily `last_successful=2026-10-13T00:00:00+08:00`、`run_count=10`；Tactical/Synthesis/Audit 未运行。
- 阻塞：无新增系统 blocker。数据集 license、具体 revision 与条目级时间出处仍为后续核验项，不影响 A1 首轮竞争矩阵验收。

## 一手来源入口

- [ExAnte](https://aclanthology.org/2026.eacl-long.72/)
- [Can Prompts Rewind Time?](https://arxiv.org/abs/2510.02340) / [作者仓库](https://github.com/gxx27/time_unlearn)
- [EvolveBench](https://aclanthology.org/2025.acl-long.788/)
- [Recall-Based Prompting](https://arxiv.org/abs/2606.05804)
- [Past without Anachronism](https://arxiv.org/abs/2505.00030)
- [Temporal Critique](https://arxiv.org/abs/2605.14636)
- [HistoRAG](https://arxiv.org/abs/2606.18103)
- [Time Sensitive Knowledge Editing](https://aclanthology.org/2024.acl-short.53/)
