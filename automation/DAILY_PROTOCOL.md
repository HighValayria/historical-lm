# Daily 协议

## 目的

Daily Research Radar 是多通道研究环境检查，不是单纯论文搜索任务。

Daily 必须回答：

> 今天研究环境中出现了哪些真正新增、且与本项目相关的信息？

Daily 报告必须使用中文。论文标题、数据集名称、档案名称、标识符、`newly_discovered` 等枚举值和路径可以保留原文。

Daily 优先保证覆盖面，而不是深度。论文通道很丰富也不能替代对数据集、档案、方法、资源和项目影响的检查。

Daily 不得修改 `research_design/RESEARCH_DESIGN.md`。正式研究设计只能由 Five-Day 在有限证据更新范围内修改，或由 Half-Month 进行核心重构。Daily 只提供新证据、registry 更新和队列。

## 固定通道

Daily 有六个必查通道：

1. `PAPERS`
2. `DATASETS`
3. `ARCHIVES`
4. `METHODS`
5. `RESOURCES`
6. `PROJECT_IMPACT`

只有当每个通道都有以下状态之一时，Daily 才算完成：

- `checked_material_update`
- `checked_no_material_update`
- `blocked`

不得使用 `skipped` 或 `not_needed`。

如果某个通道因为网络、访问或环境问题无法检查，将其标记为 `blocked`，把 blocker 写入 `state/blockers.json`，然后继续检查其余通道。

## 广度优先策略

Daily 必须按以下第一轮顺序检查通道：

1. `PAPERS`
2. `DATASETS`
3. `ARCHIVES`
4. `METHODS`
5. `RESOURCES`
6. `PROJECT_IMPACT`

只有在六个通道全部检查后，Daily 才能回到某个高价值通道继续加深。

如果上下文、时间或额度紧张，应降低每个通道的深度。不得完整深入 `PAPERS` 后放弃其他通道。

软预算规则：`PAPERS` 默认不应超过 Daily 探索工作量的大约 35%。Daily 不追踪多跳引用图；这类工作应放入 Five-Day 队列。

### 轻量主线平衡（2026-10-12 起）

本项目的主要贡献仍是来源约束下的时代错置、历史性无知与可审计评测；OCR 是来源可用性和证据质量的支撑层，不是默认的中心研究方向。为防止发现池因“中文历史文档”检索词而系统性偏向 OCR：

- 在完成基础 OCR / 版面 / 转写可行性扫描后，PAPERS 与 METHODS 的加深优先顺序为：来源约束 RAG 与出处归因、时间边界 / 时代错置、拒答与不确定性、档案偏差 / 来源生态、评测与标注设计，随后才是 OCR。
- 纯 OCR、版面或识别论文只有在能直接改变候选来源的合法可用性、页级出处链、修订审计方案或小样本质量控制决策时，才可作为当日 `checked_material_update` 的实质发现；其他相关论文可以简要记录为已检查，不应挤占深读队列。
- 不设机械数量配额，也不因其属于 OCR 而排除：当 OCR 发现真正解除来源可行性 blocker 时，应优先登记并说明这种例外。

## 通道 1：`PAPERS`

检查：

- 近期新发表论文；
- 新发现的既有工作；
- seed paper 的新引用；
- 尚未登记的 seed paper references；
- 已知论文的新更新；
- 综述、benchmark 论文和方法论文。

关键主题：

- historical language model；
- temporal knowledge；
- temporal leakage；
- knowledge cutoff；
- ex-ante reasoning；
- anachronism；
- Historical RAG；
- provenance；
- source diversity；
- digital humanities plus LLM。

对论文而言，“new” 指：

```text
new_to_system = absent from state/seen_papers.json and evidence/literature_master.csv
```

这包括几个月或几年前发表、但今天第一次被本系统发现的论文。

论文发现分类为：

- `newly_published`：近期发表、新上线、新接收或新公开，且此前未进入本系统的工作。
- `newly_discovered`：较早发表但此前未进入本系统的工作。
- `existing_paper_update`：关于已知论文的实质性新信息。

去重优先级：

1. DOI；
2. arXiv ID；
3. Semantic Scholar、OpenAlex、ACL Anthology 或其他稳定 paper ID；
4. 规范化标题。

高相关论文发现进入 `state/queues.json -> deep_reading`。

## 通道 2：`DATASETS`

独立检查数据集。论文中提到某个数据集，并不等于完成 `DATASETS` 通道。

检查：

- 新数据集；
- 新 benchmark；
- 已知数据集新版本；
- 新开放下载；
- license 变化；
- 新数据字段；
- historical QA；
- temporal benchmark；
- anachronism benchmark；
- Chinese historical NLP dataset；
- OCR dataset；
- provenance / source attribution dataset。

对每个实质性数据集发现，判断它是否真实存在，并在可用时记录：

- 公开访问情况；
- license；
- 语言；
- 时间范围；
- 领域；
- 与当前项目的适配性。

高相关数据集发现进入 `state/queues.json -> dataset_review`。

## 通道 3：`ARCHIVES`

独立检查历史来源和数字档案。

重点关注：

- Wellcome Collection；
- China Medical Missionary Journal；
- Chinese Maritime Customs；
- Shanghai Municipal Council；
- bnAsie；
- 晚清期刊数据库；
- 《申报》；
- 地方志；
- 医学期刊；
- 医学教科书；
- 海关报告；
- 市政 / 租界卫生资料；
- 新数字化项目；
- 新 OCR access；
- 新 API；
- 新全文访问；
- metadata 或 license 变化。

本通道回答：

> 历史材料是否变得更容易访问或使用？

高相关档案发现进入 `state/queues.json -> archive_review`。

## 通道 4：`METHODS`

检查可能改变实现成本或实验设计的方法与工具。

这可以包括论文、模型、库、release 或开源实现。

重点关注：

- historical OCR；
- document layout parsing；
- handwritten / printed historical text recognition；
- embedding；
- retrieval；
- reranking；
- temporal retrieval；
- provenance-aware retrieval；
- source attribution；
- citation grounding；
- long context；
- structured extraction；
- evaluation；
- uncertainty / abstention。

如果某个方法已经在 `PAPERS` 中发现，仍需单独回答它是否对本项目有直接工程价值。

高相关方法发现进入 `state/queues.json -> method_review`。

## 通道 5：`RESOURCES`

检查非论文研究资源：

- GitHub repository；
- research toolkit；
- benchmark framework；
- annotation tool；
- OCR pipeline；
- digital humanities platform；
- corpus browser；
- archive search interface；
- citation / provenance tool；
- dataset processing scripts；
- research project pages。

本通道回答：

> 是否出现了能直接降低当前研究工作量的东西？

高相关资源发现进入 `state/queues.json -> resource_review`。

## 通道 6：`PROJECT_IMPACT`

这是基于本次运行所有发现的独立项目状态检查。

回答：

- 是否出现直接竞争工作？
- 是否有新资源可能解决当前 blocker？
- 数据可行性是否发生实质变化？
- 是否有内容需要进入 Five-Day 队列？
- 是否有当前贡献明显受到威胁？
- 是否出现新的研究机会？

如果没有项目层面影响，写：

```text
No project-level impact.
```

## 必须更新的状态

Daily 成功运行后，为每个已检查的非 impact 通道分别更新 `state/channel_state.json`：

```json
{
  "PAPERS": {
    "last_checked": "YYYY-MM-DD",
    "last_material_update": "YYYY-MM-DD or null"
  }
}
```

只有当该通道状态为 `checked_material_update` 时，才更新 `last_material_update`。

仅当调度规则允许时，才更新 `state/automation_state.json`。

## 报告格式

每份 Daily 报告必须使用以下中文结构，即使某个通道没有实质更新：

```markdown
# Daily Research Radar — YYYY-MM-DD

## 1. 论文

状态：

Newly published:
Newly discovered:
Existing updates:

实质发现：

## 2. 数据集 / Benchmark

状态：

实质发现：

## 3. 历史档案 / 来源

状态：

实质发现：

## 4. 方法 / 工具

状态：

实质发现：

## 5. 研究资源

状态：

实质发现：

## 6. 项目影响

影响：

已更新队列：

## 覆盖检查

- PAPERS: checked / blocked
- DATASETS: checked / blocked
- ARCHIVES: checked / blocked
- METHODS: checked / blocked
- RESOURCES: checked / blocked
- PROJECT_IMPACT: checked / blocked
```

如果某个通道没有新发现，写：

```text
Status: checked_no_material_update
No material update.
```

## 限制

Daily 不得：

- 重写研究设计；
- 修改 `research_design/RESEARCH_DESIGN.md`；
- 生成长篇文献综述；
- 深入分析大量论文；
- 让 `PAPERS` 占用整个运行；
- 跳过数据集、档案、方法、资源或项目影响；
- 在没有实质更新时编造更新。

Daily 负责发现、去重、判断相关性、分类和入队。Five-Day 负责更深入阅读和跨类型综合。
