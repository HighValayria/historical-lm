# Daily Execution 协议

## 目标与验收

每次自动化入口均执行 Daily。它由“六通道轻量巡检 + 有界 backlog 执行”组成；每天可以没有新发现，但如存在可执行任务，必须实际推进至少一个微任务。

Daily 成功需同时满足：

1. `PAPERS`、`DATASETS`、`ARCHIVES`、`METHODS`、`RESOURCES`、`PROJECT_IMPACT` 均记录为 `checked_material_update`、`checked_no_material_update` 或 `blocked`；
2. 对新增关键结论保存可验证来源，或明确记录没有实质更新；
3. 用 `scripts/manage_research_backlog.py next` 选择任务；存在 eligible 任务时保存一个有界交付物或可恢复 checkpoint；
4. 写入或幂等更新 `reports/daily/YYYY-MM-DD.md`，追加 `state/task_journal.md`；
5. 报告、registry、backlog 与 checkpoint 一致。

## 执行规则

- 广度优先依次检查六通道；完成首轮后才可加深。`PAPERS` 默认不超过巡检工作量约35%。
- 优先直接时代错置评测、时间条件化/知识编辑、Temporal RAG、年代验证、选择性验证Agent与可校准拒答。Legacy/OCR 仅在解除年代证据或方法 blocker 时进入主动队列。
- 优先恢复 `running + checkpoint.safe_to_resume=true`；否则选择最高优先级、依赖满足的 `ready` 任务。单次最多3个任务、总计最多90分钟。
- 两条 Track 都需持续推进；同优先级时任务管理器偏向上次未领取的 Track。
- 任务只有预期产物存在、验收条件实际通过，才可标记 completed。失败后记录原因；第二次失败且没有新修复路径时标记 blocked。
- Daily 不修改正式研究设计或版本文件，不执行需要用户授权的决定。

## 各通道保留检查项

- `PAPERS`：同时检查近期发表、首次发现的旧工作、seed引用与已知论文更新；按`newly_published`、`newly_discovered`、`existing_paper_update`分类。依次用DOI、arXiv ID、稳定论文ID、规范化标题去重，高相关项进入deep-reading队列。
- `DATASETS`：独立核验Benchmark/数据集是否真实存在、公开状态、license、语言、年代、领域、字段与适配性；论文提及不等于数据集通道已完成。
- `ARCHIVES`：核验机构目录、馆藏范围、稳定标识符、访问与许可条件；目录可见不等于正文可用，单一档案缺失不证明知识不存在。
- `METHODS`：检查时间条件化、knowledge cutoff、Temporal/Historical RAG、知识编辑、claim verification、Agent与去污染工具；记录代码可得性、环境需求和能否改变方法选择。
- `RESOURCES`：检查官方项目页、代码库、数据卡、模型卡、工具链与合规资源；不得把资源存在误写成已在本项目验证。
- `PROJECT_IMPACT`：明确新信息对研究问题、评测、数据、方法、资源、风险和优先级是`material`、`limited`还是`none`。

## 必须维护的既有状态

仅在有实际变化时更新`state/seen_papers.json`、`state/seen_datasets.json`、`state/queues.json`、`state/channel_state.json`、`state/blockers.json`及`evidence/`下相应registry。所有登记保留来源链接/标识符、日期、来源类型、直接支持或推断和不确定性。不要重复处理已登记论文或数据集。

Daily报告至少包含六通道结果、覆盖检查、实际推进的backlog任务、产物/checkpoint、限制与项目影响。没有新内容时如实写`checked_no_material_update`，不得用冗长摘要填充空缺。

## 事件触发

如发现竞争方法覆盖核心贡献、金标准失效、严重泄漏、关键 Baseline 异常或研究条件重大变化，在当日报告中新增 `URGENT RESEARCH EVENT`，更新风险和 backlog；需要授权的事项进入 `state/human_decisions.json`，但继续独立安全工作。
