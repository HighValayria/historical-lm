# 现有20题研究能力逐题审计表

本表审计的是测量构念与公平可答性，不是第二轮独立史学核验。审计者仍为同一 Codex 项目链，`independent_review=false`。

| 题号 | 主要测量目标 | 直接测历史边界/时代错置 | Oracle需要 | 提示风险 | 证据组 | 处置 | 关键判断 |
|---|---|---:|---|---|---|---|---|
| DFP-Q001 | historical_fact_reading_comprehension | 否 | required_for_fair_answer | medium: '根据所给' announces an extractive task | CMMJ1889-Tungchowfu | 只能用作控制题 | Useful positive reading control, not a temporal-boundary item. |
| DFP-Q002 | evidence_insufficiency_and_epistemic_calibration | 否 | required_for_fair_answer | high: yes/no wording strongly cues refusal | CMMJ1889-Tungchowfu | 可直接用于研究验证 | Measures evidence scope, not whether 1888 actors knew a fact. |
| DFP-Q003 | historical_fact_reading_comprehension | 否 | required_for_fair_answer | low | CMMJ1889-Salol | 只能用作控制题 | Straight extraction control. |
| DFP-Q004 | historical_claim_vs_modern_fact_distinction | 否 | required_for_fair_answer | high: '仅凭' and a strong clinical claim cue rejection | CMMJ1889-Salol | 可直接用于研究验证 | Potential temporal item only after independently dating later clinical evidence; current label is evidence-strength only. |
| DFP-Q005 | historical_fact_reading_comprehension | 否 | required_for_fair_answer | low | CMMJ1889-Chinanfu | 只能用作控制题 | Source-specific reading control. |
| DFP-Q006 | historical_fact_reading_comprehension | 否 | required_for_fair_answer | low | CMMJ1889-InstitutionalStats | 只能用作控制题 | Numeric reading control; answer is not the number of unique persons. |
| DFP-Q007 | ocr_image_evidence_fidelity | 否 | requires_image_and_raw_ocr_pair | very_high: both candidate answers and the OCR lesson are disclosed | CMMJ1889-InstitutionalStats | 暂不适合当前研究 | Retain for a separate multimodal/OCR audit, not the text-only 2x2 main experiment. |
| DFP-Q008 | source_and_speaker_attribution | 否 | required_for_fair_answer | low | CMMJ1890-Fevers | 可直接用于研究验证 | Measures what this author asserted, not the epidemiological truth of the assertion. |
| DFP-Q009 | historical_claim_vs_modern_fact_distinction | 否 | required_for_fair_answer | high: yes/no proof wording cues rejection | CMMJ1890-Fevers | 可直接用于研究验证 | Good source-versus-truth item, but not a direct temporal existence test. |
| DFP-Q010 | historical_fact_reading_comprehension | 否 | required_for_fair_answer | low | CMMJ1890-Fevers | 只能用作控制题 | Geographic extraction control, not independent epidemic reconstruction. |
| DFP-Q011 | evidence_insufficiency_and_epistemic_calibration | 否 | required_for_fair_answer | high: asks whether an imprecise phrase supports precision | CMMJ1890-Fevers | 可直接用于研究验证 | A calibration item; it does not establish the real mortality count. |
| DFP-Q012 | source_and_speaker_attribution | 否 | requires_surrounding_context_to_identify_speaker | low | CMMJ1890-SocietyDiscussion | 需要修改 | Content is readable, but speaker identity needs surrounding-page context before this can be a true attribution item. |
| DFP-Q013 | evidence_insufficiency_and_epistemic_calibration | 否 | required_for_fair_answer | high: '能否独立证明' cues no | CMMJ1890-SocietyDiscussion | 可直接用于研究验证 | Can test restraint, but cannot label the true first arrival without independent chronology. |
| DFP-Q014 | historical_fact_reading_comprehension | 否 | required_for_fair_answer | medium: question explicitly asks for both sides | WC1884-Peking | 只能用作控制题 | Balanced-reading control. |
| DFP-Q015 | evidence_fidelity_and_qualification | 否 | required_for_fair_answer | high: '是否简单断言' cues the qualified answer | WC1884-Peking | 可直接用于研究验证 | Tests preservation of a counterintuitive qualification, not modern causal correctness. |
| DFP-Q016 | historical_fact_reading_comprehension | 否 | required_for_fair_answer | medium | WC1884-Tientsin | 需要修改 | Restrict gold to alum and careful filtration unless the longer page passage is added and checked. |
| DFP-Q017 | publication_observation_cutoff_time_distinction | 是 | required_for_fair_answer | high: yes/no wording cues date separation | WC1884-Tientsin | 可直接用于研究验证 | The only current item whose primary construct directly distinguishes historical times. |
| DFP-Q018 | evidence_fidelity_and_causal_strength | 否 | required_for_fair_answer | medium: asks explicitly about strength | WC1884-Drainage | 可直接用于研究验证 | Measures causal overstatement, not post-cutoff knowledge intrusion. |
| DFP-Q019 | historical_fact_reading_comprehension | 否 | required_for_fair_answer | low | WC1884-Hankow | 只能用作控制题 | Local-infrastructure reading control; do not generalize to China. |
| DFP-Q020 | archive_population_and_source_scope_control | 否 | requires_multi_source_metadata_and_passages | high: universal claim makes rejection obvious | CrossSource-Representativeness | 可直接用于研究验证 | Strong digital-humanities scope item, but not a temporal anachronism item. |

## 汇总

- 直接测试历史知识边界或时代错置：1 题（DFP-Q017）；其中直接测试截止日之后知识侵入：0 题。
- 普通文本阅读控制：7 题。
- 处置分布：可直接用于研究验证 10 题、需要修改 2 题、控制题 7 题、暂不适合 1 题。
- 统计独立性：20 题仅对应 11 个证据独立组。
- 高或很高措辞提示风险：9 题；修订稿已降低部分提示，但仍需独立复核。

Q007 应另作图像—OCR多模态控制；Q012 的孤立证据没有交代发言者，补入上下文并重审前不进入主因子实验。Q016 的原金标准超出了核验摘录，修订稿只保留明矾与过滤。
