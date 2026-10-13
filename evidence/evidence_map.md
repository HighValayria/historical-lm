# 证据地图

| 来源编号 | 来源 | 类型 | 访问日期 | 可用事实 | 支撑的判断 | 支撑类型 | 不确定性 | 说明 |
|---|---|---|---|---|---|---|---|---|
| GOV-AGENTS | `AGENTS.md` | 本地治理文件 | 2026-07-17 | 项目要求先降低不确定性，记录史料与偏差边界。 | 本轮应优先做可行性、证据和偏差记录，而非训练。 | 直接 | 低 | 本地项目规则。 |
| GOV-CHARTER | `PROJECT_CHARTER.md` | 本地项目章程 | 2026-07-17 | 项目聚焦晚清公共卫生与历史知识边界。 | 候选方向应限定在公共卫生、时代错置、历史 RAG 或轻量适配。 | 直接 | 低 | 本地项目章程。 |
| T10-LANDSCAPE | `evidence/literature_matrix.md` | 文献综合 | 2026-07-17 | 相关方法充足，但没有现成晚清公共卫生时代错置评测集。 | 最强缺口是有来源约束的 benchmark，而非直接训练。 | 综合推断 | 中 | 细节历史论断仍需精读。 |
| T11-SOURCES | `evidence/source_registry.md` | 史料图景 | 2026-07-17 | 开放小样本最适合海关、传教士和市政/通商口岸材料；中文报刊库多受订阅限制。 | 第一版 pilot 应使用合法小样本，并把订阅库作为后续授权扩展。 | 直接与推断 | 中 | 访问条款与 OCR 仍需探针。 |
| T12-CONCEPTS | `evidence/concept_map.md` | 概念综合 | 2026-07-17 | 历史知识边界包括时间、可达性、出处、档案偏差和历史性无知。 | benchmark 必须区分多类时代错置并奖励合理拒答。 | 综合推断 | 中 | 标签需通过试点标注修订。 |
| T31-OCR-METADATA | `probes/ocr/ocr_metadata_probe_results.json` | 探针结果 | 2026-07-17 | Wellcome、CRL、bnAsie 有不同程度文本跟进信号；海关入口需人工导航。 | 第一版不要假设已有干净 OCR 语料。 | 直接探针 | 中 | 还未测 OCR 准确率。 |
| T51-ENGINEERING | `prototypes/min_engineering_probe/probe_results.json` | 工程探针 | 2026-07-17 | 12 条试点题校验 0 错误，10 条可评分，2 条需真实段落。 | 当前 seed 足以支持下一轮工程扩展。 | 直接脚本输出 | 低 | 检索只是词项重叠原型。 |
| RES-HIST-CHINESE-OCR-BENCH | `https://github.com/wwei2024/historical-chinese-ocr-benchmark` | 公开代码仓库 | 2026-10-08 | README 指定繁体竖排历史印刷书 OCR 比较、CER 计分，并明确严肃评测需人工核验真值。 | 后续 OCR 小样本探针应固定阅读顺序、保存原始输出并使用人工核验参考文本；不能将模型输出作为真值。 | 直接 | 中 | 仓库未见明确许可证、来源元数据或晚清公共卫生样本；仅作方法参考。 |
| LIT-HISTORICRAG-2026 | `https://openproceedings.org/2026/conf/edbt/paper-321.pdf` | 同行会议演示论文 | 2026-10-09 | 系统以 OCR 历史报纸检索为基础，在回答旁展示原始扫描页、时间线和地理上下文；论文说明其使用 GPT-4.1 mini。 | 项目应保存回答到页面级证据的可审计链，但不采用其付费模型路线，也不能把瑞士报纸结果外推到晚清公共卫生。 | 直接与边界推断 | 中 | 演示论文而非晚清 benchmark；来源、语言和任务不匹配。 |
| LIT-ANCIENTDOC-2026 | `https://aclanthology.org/2026.findings-acl.1438/`；`https://github.com/bytedance/AncientDoc` | ACL 同行论文与官方资源库 | 2026-10-10 | AncientDoc 覆盖页级 OCR、白话翻译、推理/知识/语言变体 QA 五类任务；官方 README 声称数据集为 CC0，约含 100+ 书、约 3,000 页并跨至清代。 | 试点评测可借鉴“转录—理解”分层和确定性指标，但不得把宽泛的古籍覆盖、README 许可声明或模型评分结果等同于晚清公共卫生语料的来源可用性或历史知识边界证据。 | 直接与边界推断 | 中 | 尚未核验单条材料出处、1880—1899 公共卫生子集与页面级再利用链；不进入项目语料。 |
| SRC-DDB-CMCS-1890-ISS38-39 | `https://www.deutsche-digitale-bibliothek.de/item/PV6DNV4TK3RXA72YFFJ2PITTRN4KDDZ6` | 数字档案目录条目 | 2026-10-11 | Deutsche Digitale Bibliothek 的条目记录 1890 年海关医学报告 Issue 38-39、1894 年上海出版、Bayerische Staatsbibliothek 数字化归属与稳定 URN；目录还显示仅非商业使用。 | 新增一个处于优先时段的来源核验入口，但在原始数据伙伴条款、页图像 / 文本可得性与段落级再利用权利复核前，不能作为项目语料。 | 直接与边界推断 | 中 | 目录条目并不证明可下载、可 OCR、可摘录或适合公共卫生段落；仍需 N00 小范围核验。 |
| RES-RAG-EVAL-HISTORICAL-NEWSPAPERS | `https://github.com/rsonnen/rag-eval-historical-newspapers` | 公开代码与评测元数据仓库 | 2026-10-13 | README 声明仓库为 MIT 许可，并为每页保留 LOC 标识符、网页 URL 与 PDF/JP2/XML/TXT 文件引用；实际报纸页不随仓库分发，需按元数据从 Chronicling America 获取。 | 后续晚清来源试点可借鉴“情景—页清单—稳定标识符—文件变体”结构，明确把原始档案页与派生评测元数据分开。 | 直接与边界推断 | 中 | 仅美国英语报纸（1848-1933），并非晚清公共卫生材料；仓库的许可声明不替代任何候选中文来源的逐项条款审计。 |
