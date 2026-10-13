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
