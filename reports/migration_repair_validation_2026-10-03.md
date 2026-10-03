# Migration Repair Validation

## Result

PASS

本报告只验证 `reports/migration_validation_2026-10-03.md` 中导致 FAIL 的关键项是否已修复；未重新执行完整迁移审计，未运行 Daily / Five-Day / Half-Month，未联网，未创建 v002。

## Original FAIL items

### 1. Versioning infrastructure

Status: PASS

验证结果：

- `research_design/CURRENT.md` 已存在；
- `CURRENT.md` 声明当前版本为 `v001`；
- `research_design/VERSION_LOG.md` 已存在；
- `VERSION_LOG.md` 包含 `v001 — 2026-10-03`；
- `research_design/archive/` 已通过 `.gitkeep` 建立；
- `research_design/MIGRATION_MAP.md` 已存在；
- `research_design/RESEARCH_DESIGN.md` 的 Snapshot 已声明当前版本为 `v001`。

说明：

- 本次未创建 `v002`；
- 当前 `RESEARCH_DESIGN.md` 被认定为 `v001`；
- archive 当前只作为未来历史版本归档目录存在，未移动当前主文档。

### 2. Benchmark/probe fidelity

Status: PASS

`research_design/RESEARCH_DESIGN.md` 已恢复以下已有事实状态：

- 12 条 pilot items；
- 4 条 source records；
- 10 条当前在结构上可评分的题目；
- 2 条需要获得已验证真实史料段落后才能进行实质评分的题目；
- 最新本地 engineering probe 中结构 / schema 错误为 0。

同时已明确这些结果只证明：

- benchmark 数据结构可以运行；
- schema / pipeline 具备工程可行性；
- 当前题目中已有一部分可用于元数据、截止日期和回答策略层面的结构性评分。

并明确这些结果不证明：

- benchmark 已经得到历史学验证；
- taxonomy 已经具有稳定标注一致性；
- 12 道题已经构成正式研究 benchmark；
- Historical RAG 已经有效；
- B0 / B1 / B2 / B3 已经完成正式比较。

### 3. Five-Day permission conflict

Status: PASS

`automation/FIVE_DAY_PROTOCOL.md` 已改为：

- Five-Day 权限是 `synthesis + revision proposal only`；
- Five-Day 可以读取 `research_design/RESEARCH_DESIGN.md`，但不得修改；
- Five-Day 不得修改 `research_design/CURRENT.md`；
- Five-Day 不得修改 `research_design/VERSION_LOG.md`；
- Five-Day 不得创建新研究设计版本；
- Five-Day 不得修改 `research_design/archive/`；
- Five-Day 如认为研究设计需要变化，只能在报告中提出 `PROPOSED DESIGN REVISION`。

`automation/MASTER_AUTOMATION_PROMPT.md`、`AGENTS.md`、`AUTOMATION_README.md` 已同步同一权限规则。

### 4. Half-Month version rule

Status: PASS

`automation/HALF_MONTH_PROTOCOL.md` 已明确：

- Half-Month 必须首先回答：`Does accumulated evidence justify a new formal research-design version?`
- 若答案为 NO，不修改当前版本、不创建空版本、不修改 archive，只输出 Half-Month 审计报告；
- 若答案为 YES，固定执行：

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

同时已明确：

- 新版本必须是完整独立文档，不是 diff；
- archive 中的历史版本是只读冻结快照；
- 自动任务不得修改 archive 中已经归档的版本。

## Remaining issues

本次定向修复只处理原审计报告中的关键 FAIL 项。以下内容仍可作为后续单独任务考虑，但不影响本次 repair validation：

- 是否进一步补充 T30 / T31 的 HTTP 200、IIIF、PDF、OCR 信号细节；
- 是否显式补写 B0/B1/B2/B3 的 pairwise comparison 解释；
- 是否恢复“当代主义”和“出处不确定性”为独立概念风险；
- 是否把完整 source registry 背景纳入主设计。

这些属于原审计 P1 / P2 或后续增强项，本次没有执行。

## Final assessment

原审计导致 FAIL 的关键项已经修复：

1. v001 正式建立；
2. `CURRENT.md` 存在；
3. `VERSION_LOG.md` 存在；
4. `archive/` 存在；
5. `MIGRATION_MAP.md` 存在；
6. benchmark / probe 具体状态已恢复；
7. Five-Day 不再直接修改研究设计；
8. Half-Month 拥有唯一正式版本升级权限；
9. archive 历史版本规则已声明为只读冻结；
10. 本次未创建 v002；
11. 本次未运行 Daily、Five-Day 或 Half-Month。

Repair validation: **PASS**.
