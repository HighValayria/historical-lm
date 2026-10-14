# 年代证据卡模式 v0.1

## 用途与边界

一张卡描述一个可审核的历史命题及其在指定截止点、行动者和档案范围内的证据状态；它不是事件真相的自动裁决，也不是模型输出。卡可支撑题目、检索记录或人工复核，但只有 `review_status: verified` 且满足相应标签的证据门槛时，才可作为严格时代错置判定的依据。

每张卡必须分开记录四层状态：

| 字段 | 问题 | 禁止的推理 |
|---|---|---|
| `knowledge_existence` | 该知识 / 事件在世界某处是否已存在？ | 档案未收录，因此不存在。 |
| `actor_access` | 指定行动者在截止点前是否可合理接触？ | 世界上已存在，因此行动者一定知道。 |
| `archival_record` | 目标档案是否记载？ | 档案记载，因此行动者必然相信或使用。 |
| `model_use` | 模型输出是否把后出或不可达知识作为当时可用？ | 模型回答是历史证据。 |

`unknown`、`unverified` 和 `contested` 都是合法状态。它们要求保留不确定性或使用不可判定标签，而不是用缺失字段补成否定结论。

## 必填结构

`chronology_card.schema.json` 是机器可校验的 JSON Schema Draft 2020-12。顶层必填：

- `card_id`、`claim`、`cutoff`、`actor_scope`；
- 四层状态对象；
- 至少一条 `sources`；
- `allowed_labels`、`review_status` 与 `review`。

来源须标记 `source_type`、稳定标识符或 URL、直接支持还是推断、对应的层以及不确定性。日期应尽量使用 ISO-8601；无法精确到日时可使用年份或区间，并在 `temporal_precision` 与 `uncertainty` 中说明。

## 判定门槛

1. `explicit_future_fact`：输出片段 + 截止日后发生 / 发表 / 可得的独立年代证据；若只是来源缺失，标 `indeterminate`。
2. `post_cutoff_knowledge`：除时间证据外，还要界定该“知识”而非单一文献，且说明它与回答的关系。
3. `access_anachronism`：不能只用世界范围存在证明；须有行动者范围和正 / 反可达性证据，或将 `actor_access.status` 标为 `unknown` / `contested`。
4. `archival_silence`：只能说明指定档案的检索 / 保存范围，不能推出知识不存在。
5. `model_use`：必须独立保存模型运行标识、输出片段、评分者和所依赖证据卡；卡本身不应含模型生成内容。

## 复核规则

- `draft`：允许空缺和候选来源，不能生成严格标签。
- `under_review`：至少一位复核者检查过，仍可有争议。
- `verified`：两名独立复核者或等价的记录化裁决确认；卡的 `review.decision` 必须为 `accept` 或 `accept_with_limitations`，且每个拟用严格标签的门槛可追溯。
- `rejected`：保留原因和来源，不删除，以防重复劳动。

独立性以未共同撰写同一判断、未仅复述彼此结论为最低标准；同一模型复查不算独立复核。每张卡还必须声明档案留存、识字 / 阶层、地域、作者 / 出版者、OCR、现代编辑、数字化和训练污染等偏差中哪些适用。

## 最小示例（结构占位，不是历史事实）

```json
{
  "card_id": "CARD-DEMO-0001",
  "claim": {"text": "占位命题，不得当作历史事实。", "claim_type": "event"},
  "cutoff": {"value": "1900", "temporal_precision": "year", "basis": "evaluation cutoff"},
  "actor_scope": {"description": "待定义的行动者范围", "geography": ["unknown"], "languages": ["unknown"], "institutional_context": "unknown"},
  "knowledge_existence": {"status": "unverified", "evidence_ids": []},
  "actor_access": {"status": "unknown", "evidence_ids": []},
  "archival_record": {"status": "unknown", "archive_scope": "未检索", "evidence_ids": []},
  "model_use": {"status": "not_assessed", "evidence_ids": []},
  "sources": [{"source_id": "S1", "source_type": "catalogue", "citation": "占位目录", "stable_locator": "https://example.invalid/", "supports": "direct", "layers": ["archival_record"], "uncertainty": "仅演示结构。"}],
  "allowed_labels": ["indeterminate"],
  "review_status": "draft",
  "review": {"reviewers": [], "decision": "pending", "notes": "不可用于评测。"},
  "biases": ["archive_survival", "digitization"]
}
```
