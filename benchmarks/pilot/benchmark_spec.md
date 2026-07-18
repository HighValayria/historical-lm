# 试点评测集规范

## 名称

晚清公共卫生历史知识边界试点评测集。

## 目的

评估 LLM 或 RAG 系统在回答晚清公共卫生问题时，是否能避免引入后出事实、现代词义、无出处支撑的因果/价值框架和错误来源归属。

## 范围

- 目标期段：1880-01-01 至 1899-12-31。
- 临时截止日期：1900-01-01。
- 初始来源生态：T30/T31 中可跟进的海关、传教士医学和通商口岸市政材料。

## 题目类型

| 类型 | 目的 | 是否需要真实史料段落 | 期望回答策略 |
|---|---|---:|---|
| `post_cutoff_control` | 检验是否拒绝 1900 年后的机构、事件或术语 | 否，但需要稳定日期依据 | 识别并拒绝时代错置 |
| `metadata_provenance` | 检验来源类型、日期、标题、权利与出处意识 | 否，元数据即可 | 带限定回答 |
| `source_grounded_factual` | 检验由段落支撑的原子事实 | 是 | 带引用回答 |
| `lexical_anachronism` | 检验词义和翻译谨慎性 | 是 | 带限定回答 |
| `causal_anachronism` | 检验是否避免后见因果解释 | 是 | 带限定或拒绝错置 |
| `value_anachronism` | 检验是否区分当代分析与历史行动者分类 | 是 | 带限定回答 |
| `source_misattribution` | 检验来源归属是否正确 | 视题目而定 | 拒绝或纠正归因 |
| `historical_ignorance` | 检验在证据不足、后出或不可达时能否合理拒答 | 否或是 | 说明理由后拒答 |

## 必备字段

每题必须包含 `item_id`、`family`、`question`、`target_date`、`cutoff_date`、`source_ids`、`source_population`、`audience_or_actor`、`evidence_status`、`expected_answer_policy`、`gold_behavior`、`anachronism_labels`、`accessibility_status`、`provenance_requirements`、`scoring_notes` 和 `risk_notes`。

## 证据状态

`source_passage_verified` 表示已有真实史料段落；`metadata_verified` 表示只验证了元数据；`post_cutoff_control_verified` 表示用于稳定后出日期控制；`needs_source_excerpt` 表示暂不可评分；`secondary_guidance_only` 表示只能作二手参考。

## 排除规则

`needs_source_excerpt` 题目不得评分；生成性改写不得当作历史证据；数字化可见性不得等同于历史流通；当前来源不得被说成代表全部晚清人群；订阅或受限材料必须在条款允许时才能使用。

## 最小规模

第一版应包含 12—20 条种子题，随后扩展到 20—30 条，其中至少 8 条应由真实史料段落支撑。
