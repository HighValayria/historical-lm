# 仓库指令

## 目的

本仓库是一个自主探索式研究工作区，用于从数字人文角度研究具有历史时间一致性的语言模型。

初始重点是晚清公共卫生知识、历史知识边界、时代错置、档案偏差、Historical RAG 和轻量参数适配。

当前阶段是探索阶段。不要开始大规模模型训练。先降低不确定性。

## 自主运行

在进行实质性工作前，读取 `PROJECT_CHARTER.md`、`.agent/PLANS.md`、`state/graph.yaml`、`state/config.yaml` 和 `state/run_state.json`。

按拓扑顺序处理任务。不要每完成一个任务就停下来请求确认。

任务完成时：

1. 保存产物；
2. 写 node report；
3. 更新运行状态；
4. 追加任务日志；
5. 记录改变的假设、决策、失败和 blocker；
6. 继续下一个 ready task。

如果某个任务被阻塞，记录 blocker，并继续处理另一个 ready task。

当动态任务具有较高信息价值，并且会实质影响选题、数据可行性、评测设计或方法选择时，可以创建动态任务。

## 研究标准

优先使用 primary papers、官方项目页、原始数据集、机构图书馆、档案目录和官方文档。

重要论断必须记录来源、日期、来源类型、直接支持还是推断，以及不确定性。

绝不能把另一个模型的回答当作历史证据。

不要声称任何模型代表全部晚清人群。必须说明数据代表的档案人群。

必须显式考虑档案留存偏差、识字与阶层偏差、地域偏差、作者和出版者偏差、OCR 偏差、现代编辑介入和数字化偏差。

不得绕过 paywall、认证、CAPTCHA、访问控制、许可限制、robots policy 或批量下载限制。

## 工程规则

使用脚本完成可重复转换和检查。原始输入应与处理后输出分开保存。

除非得到明确授权，不得进行付费外部模型 API 调用。

不要开始大规模模型训练。允许小型工程 probe，但前提是它能直接降低不确定性。

在有意义的 node 边界使用 Git commit。不要重写 Git 历史或删除用户文件。

## 完成标准

继续运行，直到所有可达任务被完成、阻塞、带理由跳过，或运行预算耗尽。

最终报告必须区分：

- 已验证发现；
- 解释；
- 未解决问题；
- 推荐方向；
- 被拒绝方向；
- 被阻塞方向；
- 下一步自主任务。

## 自主研究自动化

本仓库包含一个持久的 1 天 / 5 天 / 15 天研究自动化。

在进行自主研究工作前：

1. 读取 `state/automation_state.json`。
2. 运行 `scripts/check_schedule.py`。
3. 读取 `automation/` 下对应协议。
4. 将仓库状态视为权威记忆。

不要重复处理已处理过的论文或数据集。

`research_design/RESEARCH_DESIGN.md` 是当前正式研究设计主文档。

Daily 不得修改 `research_design/RESEARCH_DESIGN.md`；Daily 只记录证据、更新 registry、写报告和加入队列。

Five-Day 只能对 `research_design/RESEARCH_DESIGN.md` 做有限证据 / 状态更新；任何实质更新都必须记录到 `research_design/DESIGN_CHANGELOG.md`。

Half-Month 是唯一允许正式重构核心研究问题、研究问题组、研究叙事、贡献主张、概念框架、benchmark 设计、实验设计、假设、优先级和拒绝 / 暂缓方向的层级。

`research_design/contribution_map.md` 和 `research_design/experiment_matrix.csv` 等辅助文件可继续服务结构化自动化；若它们与 `research_design/RESEARCH_DESIGN.md` 冲突，以主文档为准。

不得执行大规模训练、付费 API 调用、绕过访问控制或未授权抓取。

如果单个任务被阻塞，记录后继续。
