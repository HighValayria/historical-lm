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
