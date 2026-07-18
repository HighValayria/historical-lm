# 文献矩阵

| 编号 | 文献或来源 | 年份 | 主题 | 可用结论 | 与本项目关系 | 风险 |
|---|---:|---:|---|---|---|---|
| LIT-TEMP-01 | Lazaridou 等，Time Waits for No One! | 2022 | 时间错位 | 时间错位会影响 NLP 表现。 | 支持时间一致性评测。 | 现代英文任务，不是晚清中文。 |
| LIT-TEMP-02 | Röttger 与 Pierrehumbert，Temporal Effects on Pre-trained Models | 2022 | 时间鲁棒性 | NLP 评测需要报告和控制时间。 | 支持显式时间标注。 | 多为现代数据。 |
| LIT-TEMP-03 | Dhingra 等，Time-Aware Language Models as Temporal Knowledge Bases | 2022 | 时间知识 | 时间戳条件可用于变化事实探针。 | 为知识边界探针提供方法参照。 | 现代 Wikidata/新闻风格。 |
| LIT-HISTNLP-01 | MacBERTh | 2021 | 历史语言模型 | 历史领域预训练可改善历史文本任务。 | 支持历史领域适配可能性。 | 英文历史文本。 |
| LIT-HISTNLP-02 | WYWEB | 2023 | 古汉语评测 | 现有模型在古汉语任务上仍有困难。 | 说明中文历史 NLP 评测存在但不覆盖本题。 | 非公共卫生主题。 |
| LIT-RAG-01 | Lewis 等，Retrieval-Augmented Generation | 2020 | RAG | 外部检索可支持知识密集生成。 | 作为历史 RAG 技术基线。 | 检索质量依赖语料。 |
| LIT-ADAPT-01 | Gururangan 等，Don't Stop Pretraining | 2020 | 领域适配 | 领域/任务继续预训练可提升任务表现。 | 后续适配比较参照。 | 不能自动避免时代错置。 |
| LIT-ADAPT-02 | LoRA | 2022 | 轻量适配 | 低秩适配可降低可训练参数量。 | 后续个人规模适配可能路线。 | 需稳定 benchmark。 |
| LIT-HIST-01 | Rogaski，Hygienic Modernity | 2004 | 晚清/近代卫生史 | `weisheng` 与卫生现代性有历史变化。 | 支撑词汇/价值错置问题。 | 二手研究，细节需精读。 |
| LIT-HIST-02 | Benedict，Bubonic Plague in Nineteenth-Century China | 1996 | 瘟疫史 | 鼠疫史与社会、商业和生态背景相关。 | 支撑事实/因果错置设计。 | 二手研究。 |

本表只作为第一轮证据地图，详细引文和 DOI/URL 保留在原始提交历史与相关节点报告中。
