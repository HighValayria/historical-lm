# Research Design Migration Validation

## 1. Executive Result

Overall status: **FAIL**

Migration completeness: **约 72%**

Semantic fidelity: **medium-high**

Version-system compliance: **fail**

Automation-rule compliance: **partial**

结论摘要：

- 研究内容层面：核心研究定位、时代错置分类、来源边界、主实验路线和多数限制条件已经进入 `research_design/RESEARCH_DESIGN.md`，整体语义大体忠实。
- 精确状态层面：benchmark 与工程 probe 的具体成熟度没有完整迁移，尤其是“12 条 pilot items、4 条 source records、10 条当前可评分、2 条需真实史料段落后再评分”的状态被概括弱化。
- 版本机制层面：要求审计的 `research_design/CURRENT.md`、`research_design/VERSION_LOG.md`、`research_design/archive/`、`research_design/MIGRATION_MAP.md` 均不存在，因此不能通过版本化体系审计。
- 自动化规则层面：Daily 禁止修改正式研究设计已经正确表达；但 Five-Day 仍被允许直接更新 `RESEARCH_DESIGN.md` 的证据 / 状态部分，不符合“Five-Day 只形成 revision proposal，Half-Month 才决定是否创建新版本”的目标规则。
- 本次审计没有联网、没有运行 Daily / Five-Day / Half-Month、没有修复研究设计或自动化协议。

## 2. What Was Checked

检查的 legacy research artifacts：

- `PROJECT_CHARTER.md`
- `reports/FINAL_REPORT.md`
- `reports/EXECUTIVE_BRIEF.md`
- `reports/recommended_direction.md`
- `reports/minimum_viable_pilot.md`
- `reports/rejected_and_blocked_directions.md`
- `reports/technical_route_comparison.md`
- `reports/nodes/T10.md`
- `reports/nodes/T11.md`
- `reports/nodes/T12.md`
- `reports/nodes/T30.md`
- `reports/nodes/T31.md`
- `reports/nodes/T40.md`
- `reports/nodes/T41.md`
- `reports/nodes/T50.md`
- `reports/nodes/T51.md`
- `evidence/literature_matrix.md`
- `evidence/source_registry.md`
- `evidence/concept_map.md`
- `benchmarks/pilot/benchmark_spec.md`
- `benchmarks/pilot/schema.json`
- `benchmarks/pilot/pilot_items.jsonl`
- `benchmarks/pilot/source_records.jsonl`
- `probes/data_access/access_probe_summary.md`
- `probes/ocr/ocr_metadata_probe_summary.md`
- `prototypes/min_engineering_probe/probe_summary.md`
- `research_design/CURRENT_RESEARCH_DESIGN.md`
- `research_design/contribution_map.md`
- `research_design/experiment_matrix.csv`

检查的 current design / automation system：

- `research_design/RESEARCH_DESIGN.md`
- `research_design/CURRENT.md`：不存在
- `research_design/VERSION_LOG.md`：不存在
- `research_design/archive/`：不存在
- `research_design/MIGRATION_MAP.md`：不存在
- `research_design/DESIGN_CHANGELOG.md`
- `automation/MASTER_AUTOMATION_PROMPT.md`
- `automation/DAILY_PROTOCOL.md`
- `automation/FIVE_DAY_PROTOCOL.md`
- `automation/HALF_MONTH_PROTOCOL.md`
- `AGENTS.md`
- `AUTOMATION_README.md`

## 3. Legacy-to-Current Coverage Matrix

| Legacy source | Legacy claim | Current location | Status | Fidelity | Notes |
|---|---|---|---|---|---|
| `PROJECT_CHARTER.md`; `reports/FINAL_REPORT.md` | 项目研究对象是历史知识边界、时代错置、historical RAG、档案偏差和历史性无知，不是商业历史聊天机器人。 | `RESEARCH_DESIGN.md` sections 2, 5, 16 | fully_migrated | faithful | 当前设计明确排除泛化历史聊天机器人和大规模训练。 |
| `reports/FINAL_REPORT.md`; `reports/EXECUTIVE_BRIEF.md` | 晚清公共卫生是实验场景，核心是来源约束的历史知识边界与时代错置评测。 | `RESEARCH_DESIGN.md` sections 1, 3, 5, 9 | fully_migrated | faithful | 核心定位保留。 |
| `reports/FINAL_REPORT.md`; `reports/technical_route_comparison.md` | benchmark/source criticism 优先于大规模训练；LoRA/DAPT 后置。 | `RESEARCH_DESIGN.md` sections 10, 16 | fully_migrated | faithful | B4 被标为暂缓。 |
| `reports/FINAL_REPORT.md`; `reports/minimum_viable_pilot.md` | Historical RAG 是实验方法之一，不是默认创新点。 | `RESEARCH_DESIGN.md` sections 5, 10, 12 | fully_migrated | faithful | 当前设计把 Historical RAG 放在 B3 条件，并指出单纯做 Historical RAG 不足以构成贡献。 |
| `evidence/concept_map.md`; `benchmark_spec.md`; `schema.json` | 正式分类包括 factual、lexical、causal、value、source misattribution / provenance、historical ignorance。 | `RESEARCH_DESIGN.md` sections 7, 9 | fully_migrated | faithful | 分类完整保留。 |
| `evidence/concept_map.md` | 旧成果还包含“出处不确定性”和“当代主义”。 | `RESEARCH_DESIGN.md` sections 7, 12, 13 | partially_migrated | weakened | 出处不确定性被纳入 provenance / uncertainty，但“当代主义”没有作为显式独立分类保留。 |
| `evidence/source_registry.md`; `FINAL_REPORT.md` | 主要可跟进来源集中于海关、传教士医学、市政 / 租界与部分英文材料。 | `RESEARCH_DESIGN.md` section 8 | fully_migrated | faithful | 来源生态边界保留。 |
| `source_registry.md`; `rejected_and_blocked_directions.md` | 《申报》、晚清期刊全文库、商业报纸数据库和部分方志全文库受订阅、授权或批量下载限制。 | `RESEARCH_DESIGN.md` sections 8, 14, 16 | partially_migrated | weakened | 当前设计概括为中文报纸、期刊或全文数据库限制，但没有完整列出所有 legacy 高价值受限来源。 |
| `access_probe_summary.md`; `T30.md` | 4 个重点入口返回 HTTP 200，但 HTTP 200 不等于可批量使用、OCR 复用或文本挖掘。 | `RESEARCH_DESIGN.md` sections 8, 14 | partially_migrated | weakened | 限制被保留，但“4 个入口 HTTP 200”及其证据边界没有进入主设计。 |
| `ocr_metadata_probe_summary.md`; `T31.md` | Wellcome 和 CRL 高可跟进，bnAsie 中等；简单关键词探针没有明确 OCR 信号。 | `RESEARCH_DESIGN.md` sections 8, 14, 15 | partially_migrated | weakened | OCR 尚未充分验证被保留，但具体探针结果没有完整迁移。 |
| `benchmark_spec.md`; `schema.json` | 已有 benchmark specification 与 schema。 | `RESEARCH_DESIGN.md` section 9 | fully_migrated | faithful | 主设计正确表达已有规范与字段类型。 |
| `pilot_items.jsonl`; `source_records.jsonl`; `T41.md`; `probe_summary.md` | 已有 12 条 pilot items、4 条 source records。 | `RESEARCH_DESIGN.md` section 9 | partially_migrated | weakened | 主设计写“第一版试点：12-20 条种子题”，没有明确保留“已经存在 12 条”和“已有 4 条来源记录”。 |
| `probe_summary.md`; `FINAL_REPORT.md` | T51：12 条题目、0 个结构错误、10 条当前可评分、2 条需要真实史料段落后再评分。 | `RESEARCH_DESIGN.md` sections 9, 14 | partially_migrated | weakened | “needs_source_excerpt 不可评分”被保留，但具体数量和 probe 结果缺失。 |
| `technical_route_comparison.md`; `experiment_matrix.csv` | B0 Direct answer、B1 Time / role prompt、B2 Oracle historical evidence、B3 Historical RAG、B4 LoRA/DAPT deferred。 | `RESEARCH_DESIGN.md` section 10; `experiment_matrix.csv` | fully_migrated | faithful | 条件状态正确。 |
| `minimum_viable_pilot.md`; `technical_route_comparison.md` | B1 vs B0 检验 prompt 约束，B2 vs B1 检验正确历史证据作用，B3 vs B2 检验真实检索相对 oracle evidence 的损失或增益。 | `RESEARCH_DESIGN.md` section 10 | partially_migrated | weakened | 主设计列出 B0-B3，但没有显式写出这些 pairwise comparison 的解释逻辑。 |
| `FINAL_REPORT.md`; `minimum_viable_pilot.md` | 下一步顺序：真实史料获取与核验 → 真实 pilot benchmark → 标注一致性验证 → B0/B1/B2/B3 → 错误类型分析 → 再判断 LoRA/DAPT。 | `RESEARCH_DESIGN.md` sections 10, 15 | partially_migrated | weakened | 大体顺序保留，但“错误类型分析”没有作为独立步骤显式出现。 |
| `rejected_and_blocked_directions.md` | 大规模训练、商业历史聊天机器人、把生成文本当历史证据、代表全部晚清人群均被拒绝。 | `RESEARCH_DESIGN.md` section 16 | fully_migrated | faithful | 完整保留。 |
| `reports/five_day/2026-10-03.md` | 宽泛“历史 LM 避免时代错置”和“做 Historical RAG”已受相近工作威胁，需收紧为来源约束、历史性无知和晚清公共卫生 benchmark。 | `RESEARCH_DESIGN.md` sections 5, 12, 15 | fully_migrated | faithful | 近期 Five-Day 判断已整合。 |
| `research_design/DESIGN_CHANGELOG.md` | 迁移记录应说明旧状态分散，当前主文档成为正式入口。 | `DESIGN_CHANGELOG.md` | fully_migrated | faithful | 已记录迁移，但不是版本日志。 |

## 4. Missing Research Content

1. **版本化体系文件缺失。**
   - `research_design/CURRENT.md` 不存在。
   - `research_design/VERSION_LOG.md` 不存在。
   - `research_design/archive/` 不存在。
   - `research_design/MIGRATION_MAP.md` 不存在。
   - 因此无法验证 v001、CURRENT 指针、冻结 archive 或版本日志一致性。

2. **benchmark 真实当前状态缺少精确迁移。**
   - Legacy 明确记录：12 条 pilot items、4 条 source records、0 个结构错误、10 条当前可评分、2 条需真实史料段落后再评分。
   - `RESEARCH_DESIGN.md` 只写“第一版试点：12-20 条种子题”“下一目标：20-30 条题目”，没有明确写明当前实际已有数量与可评分状态。

3. **数据访问与 OCR 探针的具体结果缺失。**
   - Legacy 记录 4 个入口 HTTP 200，并且强调 HTTP 200 只证明入口页面可访问。
   - Legacy 记录 Wellcome / CRL / bnAsie 的 PDF、IIIF、download 或全文信号，以及未发现明确 OCR 信号。
   - 当前主设计只保留了概括性限制，没有保留这些 probe 级发现。

4. **实验对照逻辑不够完整。**
   - 当前主设计列出 B0/B1/B2/B3，但没有明确保留：
     - B1 vs B0：prompt 约束效果；
     - B2 vs B1：正确历史证据本身的作用；
     - B3 vs B2：真实检索相对 oracle evidence 的损失或增益。

5. **source registry 的完整来源谱没有进入主设计。**
   - 当前主设计保留了 Wellcome、CMMJ、bnAsie 和更广义的海关 / 传教士 / 市政来源。
   - 但 `source_registry.md` 中的 `SRC-SHENBAO`、`SRC-LQPERIODICALS`、`SRC-DIANSHIZHAI`、`SRC-GAZETTEERS-NLC`、`SRC-FHAC`、`SRC-NCH` 等未完整作为来源生态背景或受限来源清单保留。

## 5. Partially Migrated Content

1. **concept map 中“当代主义”被弱化。**
   - 当前主设计有 value anachronism 和行动者 / 分析者区分，但没有显式保留“当代主义”作为单独风险。

2. **“出处不确定性”被合并到 provenance / uncertainty。**
   - 合并本身合理，但失去了来源起源、日期、作者、版本、转写和现代编辑介入不明这一独立风险的可见性。

3. **source ecology / archival bias 保留为核心贡献，但具体来源群体不足。**
   - 主设计说不能代表全部晚清人群，但对各 source family 的具体偏差说明比 `source_records.jsonl` 和 `source_registry.md` 更概括。

4. **minimum viable pilot 的规模表述发生概括。**
   - `reports/recommended_direction.md` 写 10-20 个短段落或元数据记录、30-60 条原子题目。
   - `minimum_viable_pilot.md` 写 4-8 条段落、20-30 条题。
   - 当前主设计采用 20-30 题、至少 8 条真实段落支撑。该选择可被 later legacy evidence 支持，但没有说明为何采用后者。

## 6. Semantic Drift / Overstatement

未发现严重把计划写成已验证成果的系统性问题，但存在以下语义风险：

1. **贡献证据强度“强”可能缺少版本内证据出处。**
   - `contribution_map.md` 也标为强，因此不是迁移错误。
   - 但 `RESEARCH_DESIGN.md` 没有说明“强”来自第一轮设计判断，而不是完成的正式实验结果。

2. **“第一版试点：12-20 条种子题”弱化了实际已有 12 条。**
   - 这不是夸大，而是过度概括，导致当前读者无法恢复 benchmark 真实状态。

3. **“至少 8 条最终由真实来源段落支撑”是目标，不是当前事实。**
   - 当前主设计使用“最终至少应有”，语义状态正确。

4. **Wellcome API 的状态没有被夸大。**
   - 当前主设计写“调查中”“可能降低发现与元数据获取成本”，没有把 API 写成已解决数据可行性。

## 7. Epistemic Status Errors

### 已验证

可由实际文件、probe 或运行结果支持：

- T30 访问探针：4 个重点入口返回 HTTP 200。
- T31 OCR / 元数据探针：Wellcome、CRL、bnAsie 有后续跟进信号；简单关键词探针没有明确 OCR 信号。
- T40 / T41：已有 benchmark spec、schema、12 条 pilot items、4 条 source records。
- T51：本地无训练工程探针通过，12 条题目、0 个结构错误、10 条当前可评分、2 条需真实史料段落。

当前 `RESEARCH_DESIGN.md` 对这些已验证项的迁移不完整，但没有明显把它们改写成相反含义。

### 已设计

仍处于设计或候选阶段：

- B0 / B1 / B2 / B3。
- annotation / scoring feasibility。
- Historical RAG experiment。
- 从 source records 扩展到真实段落。

当前主设计基本正确标注为候选或下一步，没有把这些写成正式实验结果。

### 假设

仍是假设或预期：

- 来源约束提示或检索可能减少事实与出处错误。
- prompt-only temporal control 预计仍有残余时代错置。
- 部分问题应要求限定性不确定或拒答。
- LoRA / DAPT 是否值得测试取决于后续 benchmark 与语料状态。

当前主设计在 section 11 明确写“工作假设仍是临时判断”，语义状态正确。

### 未解决

仍未解决：

- OCR 真实质量。
- 中文全文合法获取。
- 标注一致性。
- RAG 是否真正优于 direct evidence。
- source ecology 是否足够均衡。

当前主设计保留了这些未解决问题，但不够精确地连接到 T30 / T31 / T51 的实际证据。

### 高优先级 epistemic issue

未发现“planned 写成 validated”“hypothesis 写成 finding”“candidate source 写成 usable”“engineering probe 写成 formal experiment”“HTTP 200 写成 data available”的严重错误。主要问题是：已验证的 probe 细节被省略，导致当前设计状态不够可恢复。

## 8. Versioning Issues

Version-system compliance: **fail**

发现：

1. `research_design/CURRENT.md` 不存在。
2. `research_design/VERSION_LOG.md` 不存在。
3. `research_design/archive/` 不存在。
4. `research_design/MIGRATION_MAP.md` 不存在。
5. `RESEARCH_DESIGN.md` 没有 version id，例如 `v001`。
6. `DESIGN_CHANGELOG.md` 记录了迁移，但不能替代 VERSION_LOG。
7. `CURRENT_RESEARCH_DESIGN.md` 是 legacy pointer，但不是 CURRENT 指针文件。
8. 没有 frozen archive snapshot，因此无法证明旧版本被冻结。

因此当前不是完整 versioned design system，而是“单一 authoritative 主文档 + changelog + legacy pointer”。

## 9. Automation Protocol Issues

Automation-rule compliance: **partial**

符合项：

- Daily 明确禁止修改 `research_design/RESEARCH_DESIGN.md`。
- Half-Month 被声明为唯一可正式重构核心研究设计的层级。
- 协议要求报告和研究文档使用中文。

冲突项：

- Five-Day 仍被允许直接更新 `research_design/RESEARCH_DESIGN.md` 的证据、Open Questions、Blockers、Next Research Priorities、数据源状态、benchmark 成熟度和候选方法状态。
- 审计任务给出的目标规则要求 Five-Day 只做 synthesis + revision proposal，由 Half-Month 决定是否创建新 formal version。
- 当前协议没有规定新版本创建流程：
  - current design → archive frozen snapshot → generate complete new design → update CURRENT → update VERSION_LOG。
- 当前协议仍围绕直接更新 `RESEARCH_DESIGN.md`，没有围绕 versioned documents。

搜索结果中未发现仍要求修改 `CURRENT_RESEARCH_DESIGN.md` 的有效协议；该文件只作为 legacy pointer 出现。

## 10. Conflicting Legacy Evidence

1. **pilot 规模存在 early / later 差异。**
   - `reports/recommended_direction.md`：10-20 个短段落或元数据记录、30-60 条原子题目。
   - `reports/minimum_viable_pilot.md`：4-8 条可核验短段落、20-30 条题。
   - `benchmark_spec.md`：第一版 12-20 条种子题，随后扩展到 20-30 条，至少 8 条真实段落支撑。
   - 判断：后续更具体的 benchmark spec / minimum viable pilot 可视为 later legacy evidence，当前主设计采用 20-30 条方向不是迁移错误，但应记录选择依据。

2. **Historical RAG 的角色有阶段变化。**
   - 早期 charter 把 Historical RAG 列为核心探索议题。
   - 后期 Five-Day 报告指出“做 Historical RAG”本身不足以构成新颖贡献。
   - 判断：后期证据收紧了定位，不是迁移错误。

3. **轻量适配从探索议题转为暂缓路线。**
   - charter 将 lightweight parameter adaptation 列入探索对象。
   - later technical route comparison 和 final report 将 LoRA / DAPT 后置。
   - 判断：后期证据支持暂缓，不是迁移错误。

## 11. Recommended Fixes

本节只记录建议，不执行修复。

### P0 — must fix

1. 建立真正的 versioned design system：
   - 创建 `research_design/CURRENT.md`；
   - 创建 `research_design/VERSION_LOG.md`；
   - 创建 `research_design/archive/`；
   - 将当前主设计初始化为 `v001` 或明确当前版本；
   - 归档冻结快照；
   - 记录迁移映射或 `MIGRATION_MAP.md`。

2. 修改自动化协议，使其符合版本化规则：
   - Daily → evidence only；
   - Five-Day → synthesis + revision proposal；
   - Half-Month → decide whether a new formal version is justified；
   - new version → archive frozen snapshot → generate complete new design → update CURRENT → update VERSION_LOG。

3. 将 benchmark 当前真实状态补入正式设计或版本注释：
   - 12 条 pilot items；
   - 4 条 source records；
   - 10 条当前可评分；
   - 2 条 `needs_source_excerpt`；
   - 工程 probe 是本地无训练结构探针，不是 formal experiment。

### P1 — should fix

1. 在研究设计中补充 T30/T31 的 probe 级边界：
   - 4 个入口 HTTP 200；
   - HTTP 200 不等于 data available；
   - Wellcome / CRL / bnAsie 后续信号；
   - 无明确 OCR 信号。

2. 明确 B0/B1/B2/B3 的 pairwise comparison 逻辑：
   - B1 vs B0；
   - B2 vs B1；
   - B3 vs B2。

3. 将 source registry 中未进入主设计的受限 / 候选来源作为来源生态背景保留：
   - 《申报》；
   - 晚清期刊全文库；
   - 点石斋画报；
   - 方志；
   - 一史馆；
   - North-China Herald。

### P2 — optional cleanup

1. 将“当代主义”和“出处不确定性”作为概念框架中的独立风险恢复。
2. 为“贡献证据强度：强 / 中 / 弱”增加依据说明，避免被误读为实验验证强度。
3. 在 `DESIGN_CHANGELOG.md` 与未来 `VERSION_LOG.md` 之间明确分工。

## 12. Final Assessment

当前迁移在“研究内容摘要”层面大体可用：核心定位、主要贡献、source ecology、anachronism taxonomy、实验路线和主要限制都已进入 `RESEARCH_DESIGN.md`，且没有发现严重 epistemic status 夸大。

但本次审计目标是验证“当前版本化研究设计体系”是否完整、准确、无失真地承接 legacy 成果。该目标未达成，原因是：

- 版本系统核心文件不存在；
- 自动化协议仍允许 Five-Day 直接更新正式主文档；
- benchmark / probe 的实际成熟度没有完整进入正式设计；
- 部分来源与概念细节被过度概括。

因此本次审计结果为：**FAIL**。
