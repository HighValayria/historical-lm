# 核心竞争工作矩阵（A1 首轮核验）

## 范围与核验口径

本轮在 `FORCE_MODE=DAILY`、`UPDATE_SCHEDULE=false` 的手动 Daily 中完成，限定为 8 个一手来源。结论只来自论文官方页面、arXiv 页面或作者公开代码仓库；未把搜索摘要、二手解读或其他模型输出当作证据。`method_matrix.csv` 保存逐项结构化记录。

这里的“报告结果”指作者报告，而不是本项目复现实验。当前项目仍没有真实模型实验结果，严格验证的时代错置题仍为 0。

## 已核验竞争版图

| 工作 | 核心对象 | 方法或评测 | 作者报告的主要结果 | 对本项目的边界 |
|---|---|---|---|---|
| ExAnte (2026) | 截止时点后的信息泄漏 | 股票预测、问答、Wikipedia 事件生成、论文生成四任务；leakage rate + quality | 多任务中持续违反时间约束 | 直接覆盖 ex-ante 评测，不等同于有行动者可达性证据的历史命题评测 |
| Can Prompts Rewind Time? (2025) | 提示能否模拟更早知识截止 | factual、semantic、counterfactual 三类数据与两种 meta-prompt | 直接事实与语义变化较易约束，因果相关的反事实明显更难 | 强力覆盖“只加截止提示”基线；数据仓库曾删低质量样本，版本必须固定 |
| EvolveBench (2025) | 演化知识上的时间意识 | cognition、awareness、trustworthiness、understanding、reasoning 五维评测 | 15 个模型中 GPT-4o 平均 EM 79.36，Llama-3.1-70B 72.47；错位上下文仍困难 | 覆盖现代演化事实和外部知识冲突，不直接给出历史档案证据或知识传播判定 |
| Recall-Based Prompting (2026) | prompted knowledge cutoff 的间接泄漏 | Self-Recall、Question-Recall 及其组合；新增 MHEB 多截止基准 | 在三个既有基准与 MHEB 上，SR→QR 总体最优，反事实问题改善突出 | 是低成本必备对照；仍依赖模型自述/回忆，不能核验命题年代 |
| Underwood et al. (2025) | 历史文本模拟中的时代错置 | period-prose prompting、微调、自动与人工辨别 | 提示不能稳定产生时代一致文本；微调能骗过自动评审但人类仍可区分 | 直接警示风格相似不等于历史有效；对象是文本模拟而非截止问答 |
| Temporal Critique / TCFT (2026) | 回答相对截止时间的可接受性 | cutoff prompt 分析；训练模型识别、解释并判断 post-cutoff leakage | Qwen2.5-7B/14B 上平均 leakage 分别降低 41.89/37.79 个百分点 | 高度接近命题级验证路线；仍需检查其标签年代证据、跨领域泛化和生成器外迁移 |
| HistoRAG (2026) | 历史研究中的检索偏斜与证据解释 | 检索/生成分离、时间窗口、关键词+语义检索、可争议的 LLM relevance filter | 1950年代词汇错位可导致零召回；向量相似度与 LLM relevance 相关仅 ρ=0.275 | 覆盖历史检索方法论，但时间窗口是时期平衡，不是逐命题 cutoff admissibility |
| Time Sensitive Knowledge Editing (2024) | 过时事实更新与新事实注入 | temporal KE 数据；PEFT 与 locate-and-edit 比较；多跳 QA | 作者报告 PEFT 在 time-sensitive edits 上优于 locate-and-edit | 方向主要是更新到新知识；“回退到过去且抑制未来知识”并未由该结果证明 |

## 方法—失败机制—潜在缺口

| 失败机制 | 已有直接覆盖 | 仍需验证的研究空间 |
|---|---|---|
| 显式 post-cutoff 事实泄漏 | ExAnte、Rewind Time、Recall-Based Prompting、TCFT | 是否能用独立年代证据在跨时期历史命题上稳定判定，而非只依赖题库答案 |
| 隐性后见之明/因果后果泄漏 | Rewind Time 的 counterfactual；Recall-Based Prompting 的 MHEB | 需要把“未来事实被使用”与合理的当时预测错误、普通事实错误分开 |
| 时间错位外部上下文 | EvolveBench | 历史材料还需区分知识存在、行动者可达、档案记载与模型使用四层 |
| 风格时代错置 | Underwood et al. | 风格识别不能替代命题级事实和认识论有效性；自动评审尤其需要人工/证据校准 |
| 历史检索的词汇与时期偏斜 | HistoRAG | 检索结果需要按“截止前可用”过滤，并保留事件、发表、首次记载、传播时间 |
| 参数内知识更新 | Time Sensitive KE | 更新事实与历史回退不是同一目标；反向时间条件化、遗忘副作用和跨截止可控性待测 |
| 候选回答的时间可接受性 | TCFT | 验证器是否能利用可审计的命题年代卡、何时选择性调用，以及误拒绝成本待测 |

## 对候选路线的影响

1. **Prompt 基线必须更强。** 普通截止提示不足以代表提示路线；最小实验至少应含直接 cutoff prompt、Self-Recall、Question-Recall 及组合，并按直接事实/语义/因果后见分别报告。
2. **M2 时间感知检索需与 HistoRAG 区分。** HistoRAG 已覆盖时期平衡和检索方法互补。本项目若推进 M2，应把可验证的 `available_at <= cutoff`、来源传播/行动者可达性和命题级证据链作为关键变量。
3. **M3 已有强邻近工作。** TCFT 已把 cutoff-aware critique 作为训练目标。选择性验证 Agent 只有在“外部可审计年代证据、选择性调用/成本、跨生成器迁移或不确定性校准”上产生增量，才可能形成清晰差异。
4. **M1 不能从知识编辑文献直接推导。** 现有时间敏感知识编辑主要研究把模型更新到较新事实；历史回退要求同时保留截止前知识并抑制截止后知识，需要独立实验。

以上均是基于本轮八项工作范围的**竞争边界推断**，不是新颖性证明。后续仍需引用追踪、全文表格核验和真实复现实验。

## 一手来源

- [ExAnte — ACL Anthology](https://aclanthology.org/2026.eacl-long.72/)
- [Can Prompts Rewind Time? — arXiv](https://arxiv.org/abs/2510.02340)；[作者代码与数据](https://github.com/gxx27/time_unlearn)
- [EvolveBench — ACL Anthology](https://aclanthology.org/2025.acl-long.788/)
- [Can LLMs Be Constrained to the Past? — arXiv](https://arxiv.org/abs/2606.05804)
- [Can Language Models Represent the Past without Anachronism? — arXiv](https://arxiv.org/abs/2505.00030)
- [Teaching Large Language Models When Not to Know — arXiv](https://arxiv.org/abs/2605.14636)
- [HistoRAG — arXiv](https://arxiv.org/abs/2606.18103)
- [Time Sensitive Knowledge Editing through Efficient Finetuning — ACL Anthology](https://aclanthology.org/2024.acl-short.53/)
