# 仓库指令

## 目的

本仓库是 LLM Historical Anachronism 的自主研究工作区，研究模型在历史截止时间和信息条件下使用未来知识、后出事件、后世概念或后见解释的问题及其缓解方法。

主要贡献目标是可验证的模型或系统方法。M1时间条件化参数适配、M2时间感知检索和M3时代错置验证Agent是候选路线；Benchmark是测量工具。晚清公共卫生是保留的Legacy场景，不再限定项目时期、地域、语言或领域。

当前阶段是Research & Method Feasibility。先建立严格年代证据、真实Baseline和最小方法探针，不开始大规模训练。

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

不要声称任何模型、时期样本或档案代表全部历史人群。必须说明数据、行动者和档案人群的范围。

必须显式考虑知识传播与行动者可达性、档案留存偏差、识字与阶层偏差、地域偏差、作者和出版者偏差、OCR偏差、现代编辑介入、数字化偏差和模型训练污染。

时代错置判定必须区分知识存在、行动者可达、档案记载和模型使用；单一档案缺失不得作为知识不存在的证据。

不得绕过 paywall、认证、CAPTCHA、访问控制、许可限制、robots policy 或批量下载限制。

## 工程规则

使用脚本完成可重复转换和检查。原始输入应与处理后输出分开保存。

除非得到明确授权，不得进行付费外部模型 API 调用。

不要开始大规模模型训练。允许小型LoRA/SFT、检索或Agent probe，但前提是它直接降低方法选择或实验有效性的不确定性。

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

本仓库包含一个持久的 Daily Execution / 3-Day Tactical Review / 7-Day Research Synthesis / 14-Day Strategic Audit 研究自动化。

在进行自主研究工作前：

1. 读取 `state/automation_state.json`。
2. 运行 `scripts/check_schedule.py`。
3. 读取 `state/research_backlog.json` 和 `automation/` 下对应协议。
4. 将仓库状态视为权威记忆。

不要重复处理已处理过的论文或数据集。

`research_design/RESEARCH_DESIGN.md` 是当前正式研究设计主文档。当前版本由 `research_design/CURRENT.md` 声明，版本历史由 `research_design/VERSION_LOG.md` 记录，历史版本归档在 `research_design/archive/`。

Daily 不得修改 `research_design/RESEARCH_DESIGN.md`；Daily 只记录证据、更新 registry、写报告和推进有界 backlog 微任务。

Tactical 不得修改正式研究设计，只能审计任务验收、失败、阻塞、证据状态、资源和短期优先级。

Synthesis 不得修改正式研究设计、`CURRENT.md`、`VERSION_LOG.md` 或 `archive/`。Synthesis 只能进行综合并在报告中提出 `PROPOSED DESIGN REVISION`。

Audit 是唯一允许决定是否创建新正式研究设计版本的自动层级。若需要新版本，必须先冻结当前版本到 `research_design/archive/`，再生成完整新的 `research_design/RESEARCH_DESIGN.md`，更新 `CURRENT.md`，并追加 `VERSION_LOG.md`。

旧 `FIVE_DAY` 与 `HALF_MONTH` 手动入口分别是 `SYNTHESIS` 与 `AUDIT` 的显式兼容别名；不得将旧成功时间当作新周期已经成功。失败或中断不得更新对应 `last_successful`。

`research_design/contribution_map.md` 和 `research_design/experiment_matrix.csv` 等辅助文件可继续服务结构化自动化；若它们与 `research_design/RESEARCH_DESIGN.md` 冲突，以主文档为准。

不得执行大规模训练、付费 API 调用、绕过访问控制或未授权抓取。

如果单个任务被阻塞，记录后继续。
