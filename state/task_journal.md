# 任务日志

## 2026-10-10 — Daily Research Radar

- 调度：`AUTO`；`scripts/check_schedule.py` 仅选择 Daily，且允许更新 Daily 状态。
- 完成：按 PAPERS、DATASETS、ARCHIVES、METHODS、RESOURCES、PROJECT_IMPACT 顺序完成六通道广度检查。
- 新证据：登记 AncientDoc / `acl:2026.findings-acl.1438`；它支持 OCR 到理解的分层评测，但不是晚清公共卫生语料，也不改变无训练、无付费 API 的边界。
- 变更假设：无。继续要求原始页—转录—段落—题项的可审计链，并将 OCR 误差与历史知识边界误差分开。
- 阻塞：无新增 blocker；CMMJ 与海关报告的许可、逐页抽取和 OCR 小样本验证仍留在既有 backlog。

## 2026-10-11 — Daily Research Radar

- 调度：`AUTO`；`scripts/check_schedule.py` 仅选择 Daily，且允许更新 Daily 状态。
- 完成：按 PAPERS、DATASETS、ARCHIVES、METHODS、RESOURCES、PROJECT_IMPACT 顺序完成六通道广度检查。
- 新证据：登记 `SRC-DDB-CMCS-MEDICAL-1890-ISS38-39`。它是 Bayerische Staatsbibliothek 数字化、目标时段 1890 海关医学报告的稳定目录入口，但目录的“仅非商业使用”标记与正文 / 页图像再利用范围尚未核验。
- 变更假设：来源候选池增加一个目标时段海关条目；不改变“目录可见不等于可合法用作语料”的假设，也不改变先做许可与逐页出处核验的顺序。
- 阻塞：无新增系统 blocker。对该来源的全文、页图像、OCR 和使用条款核验作为 `N00` / `archive_review` 后续工作；不下载、不抓取、不纳入试点评测语料。

## 2026-10-12 — Daily Research Radar

- 调度：`AUTO`；`scripts/check_schedule.py` 仅选择 Daily，且允许更新 Daily 状态。
- 完成：按 PAPERS、DATASETS、ARCHIVES、METHODS、RESOURCES、PROJECT_IMPACT 顺序完成六通道广度检查。
- 新证据：登记 `acl:2026.nlp4dh-1.1`（OCR 修订的 span 级出处链）与 `acl:2026.nlp4dh-1.6`（历史语料评测的目标级去污染）；前者支持原始 OCR—修订—证据链审计，后者支持防止跨记录复现的目标级重叠检查。
- 变更假设：不改变来源可行性或正式研究设计。将“保留原始 OCR”细化为可审计的修订 lineage，并把 document-level 去重视为不足的最低防护，而非充分条件。
- 阻塞：无新增系统 blocker；可合法使用的晚清公共卫生页图、段落和 OCR 小样本仍为主要实务约束。

## 2026-10-12 — Daily 发现权重微调

- 决策：按用户指示小幅提高来源约束 RAG、时代边界 / 拒答、档案偏差和评测设计的发现优先级。
- 执行：在 `automation/DAILY_PROTOCOL.md` 增加轻量主线平衡规则；OCR 继续作为来源可用性和证据审计的支撑层，但纯 OCR 发现须直接影响来源、出处链、修订审计或小样本质量控制决策，才进入实质发现或深读队列。
- 边界：不设机械配额，也不否定 OCR；当 OCR 工作实际解除来源可行性 blocker 时，仍可优先处理。

## 2026-10-13 — Daily Research Radar

- 调度：`AUTO`；`scripts/check_schedule.py` 仅选择 Daily，且允许更新 Daily 状态。
- 完成：按 PAPERS、DATASETS、ARCHIVES、METHODS、RESOURCES、PROJECT_IMPACT 顺序完成六通道广度检查。
- 新证据：登记 `rag-eval-historical-newspapers`。该公开 MIT 仓库提供历史报纸 RAG 的情景 YAML、页级 LOC 标识符、稳定 URL 与 PDF/JP2/XML/TXT 文件引用，支持将原始页与派生评测元数据分离的工程结构。
- 变更假设：不改变目标语料可行性或正式设计；补充一项可供 N03/N05 参考的页级出处链模板。该资源只覆盖美国英语历史报纸，不能作为晚清公共卫生数据、性能证据或许可代理。
- 阻塞：无新增系统 blocker；可合法复用的 1880—1899 晚清公共卫生页图、段落及其明确使用条款仍是主要实务约束。

## 2026-10-13 — DFP-2026-10-13

- 状态：整体节点完成；Phase D 执行受阻但配置已保存。
- 数据：2 个纳入的公共领域作品版本，14 页，47,479 OCR 字符，12 个核验段落。
- 评测：20 道开发题、11 个独立证据组、60 个冻结 Prompt packet；无模型结果。
- 决策变化：从“史料获取可行性未知”更新为“开放英语机构档案的小规模获取可行；正式评测的主要风险是代表性与标签核验”。
- 失败/限制：bnAsie 正文未因目录可见而下载；模型实验未因当前助手可回答而伪执行。
- Blocker：B-0001—B-0004 已在 Markdown 与 JSON 中同步。

## 2026-10-13 — RVP-2026-10-13

- 状态：研究有效性审计和实验准备完成；真实模型执行仍受 B-0003 阻塞。
- 审计：20题中10题可直接用于来源/认识论研究，2题需修改，7题为普通阅读控制，1题不适合纯文本主实验；严格时间边界题仅 Q017，直接时代错置题为0。
- 实验：18题形成72个 E0/E1/E2/E3 packet；时间提示和 Oracle 在提示层面正交，18项结构/泄漏验证全部通过。
- 核验：12段与20题盲核材料已准备，但独立核验完成数为0；同一 Codex 复查未计作独立证据。
- 模型：可恢复推理脚本已验证干运行；未检测到可控本地/授权接口，没有付费调用，没有真实输出。
- 决策变化：论文主线优先方向B（来源忠实性与认识论校准）；方向A缩为需年代证据的小型模块；方向C由真实失败触发。
- 新阻塞：B-0005，现有题目不足以支撑系统性时代错置结论。

## 2026-10-13 — ARM-2026-10-13

- 已完成：新项目README/章程、v002正式研究设计、M1/M2/M3路线、主动Backlog、Legacy索引、自动化优先级和迁移验证器。
- Git安全：原始HEAD `1a3119a` 已创建并推送保护标签；原本落后27提交的GitHub `main` 已先同步。
- GitHub：原仓库已原地重命名为 `HighValayria/llm-historical-anachronism`，默认分支保留为`main`，Description/Topics与origin已更新。
- 完整性：Data Feasibility与Research Validity验证均通过；关键冻结资产哈希保持一致。
- 阻塞：Windows因当前Codex工作区占用拒绝本地目录改名；没有创建副本或伪称完成。B-0006记录一次性改名脚本和自动化重绑定步骤。

## 2026-10-13 — ARS-2026-10-13

- 状态：自主科研调度与任务管理框架迁移完成；本次未运行研究巡检、论文检索、Baseline、模型调用或训练。
- 调度：从旧1/5/15迁移为Daily/3-Day Tactical/7-Day Synthesis/14-Day Audit；旧成功记录完整保存在`legacy_migration`，新阶段从迁移锚点起算，没有伪造成功报告。
- Backlog：建立`state/research_backlog.json`，包含A1—A3与B1—B3、依赖、验收、预算、attempt和checkpoint；当前ready为A1、A2、B1。
- 恢复：新增独立阶段运行状态、幂等事件历史和成功后才推进日程的记录脚本；失败或中断不更新`last_successful`。
- 兼容：旧`FIVE_DAY`和`HALF_MONTH`分别显式映射到`SYNTHESIS`和`AUDIT`；旧协议、报告和研究资产未删除。
- 验证：新自动化单元测试14项全部通过；原Data Feasibility验证PASS，原Research Validity验证18/18 PASS，仍确认无模型输出。
- Blocker：B-0003与B-0005保持active；B-0006因当前路径及既有完成提交得到解决。
- App日程：既有“每日自动化迭代”已原位更新并启用，保持每天09:00，project ID不变，`cwds`已核验为当前仓库；没有创建重复Automation。
- Git：主迁移提交`b7d083b`已成功快进推送到`origin/main`；无强制推送或历史重写。

## 2026-10-13 — Manual Daily Test / A1

- 运行：手动 `FORCE_MODE=DAILY`、`UPDATE_SCHEDULE=false`；不是 Scheduled Automation 触发，只执行 Daily。
- 六通道：PAPERS、DATASETS、METHODS、RESOURCES、PROJECT_IMPACT 有实质更新；ARCHIVES 已检查但无实质更新。
- 任务：领取并完成 A1；用 8 项一手来源建立 `METHOD_LANDSCAPE.md` 与 `method_matrix.csv`，区分作者报告、范围限制和本项目推断。
- 决策变化：后续 Prompt 基线需含 Recall-Based Prompting；M2 重点收窄到命题级 cutoff admissibility；M3 必须与 TCFT 明确区分。未修改正式研究设计。
- 限制：没有真实模型实验；数据集许可、revision 和条目级时间出处仍需采用前核验；严格验证时代错置题仍为 0。
- 调度：手动执行不更新 `state/automation_state.json`，未执行 Tactical、Synthesis 或 Audit。

## 2026-10-14 — Scheduled Daily / B1

- 调度：`AUTO`；`scripts/check_schedule.py` 仅选择 Daily，允许在验收成功后更新其日程。
- 六通道：PAPERS、METHODS、RESOURCES、PROJECT_IMPACT 有实质更新；DATASETS 与 ARCHIVES 检查后无实质更新。
- 论文：登记 `arxiv:2609.23178` Chronologic；仅完成作者摘要级核验，进入 deep-reading，不把它当作本项目年代证据或可用数据集。
- 任务：完成 B1、A2、B2（本轮 Daily 上限 3 项）。B1 审计并将基线 README 改为零调用兼容契约；A2 交付四层年代证据卡 schema；B2 交付可记录版本 / 参数 / 条件 / 哈希与路径分离的干运行配置 schema。旧 20 题、原始输出和审计保持不变。
- 假设 / 决策：未来新题必须以年代卡、独立命题、截止点和行动者范围接入；B1/B2 不解除 B-0003 或 B-0005，也不改变正式研究设计。A3 已就绪，作为下一 Daily 的优先任务。
- 验证与完成状态：dry-run 未产生响应；年代卡 schema 通过 Draft 2020-12 与示例验证；Baseline scaffold、backlog 和调度共 17 项测试通过；JSON 与 diff 检查待收尾复核。
