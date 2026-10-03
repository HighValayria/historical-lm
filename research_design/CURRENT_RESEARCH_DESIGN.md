# Current Research Design

## Current Research Direction

晚清公共卫生语境下大模型历史知识边界、时代错置与 Historical RAG 研究。

The current recommended direction is a source-constrained pilot benchmark for late-Qing public-health anachronism and historical ignorance, using legally accessible small samples from customs, missionary medical, and municipal / treaty-port sources.

## Core Question

现代 LLM 能否真正遵循一个历史时期的知识边界？

Operationally, can an LLM or RAG system answer late-Qing public-health questions without importing post-1900 facts, modern lexical meanings, unsupported causal or value frameworks, false provenance, or unreasonable certainty where the historical record does not support it?

## Current Contribution Candidates

1. multi-level anachronism benchmark;
2. historical ignorance;
3. provenance / source ecology;
4. late-Qing Chinese public-health context;
5. archive-dependent historical cognition.

## Current Experimental Direction

Future candidate baselines:

- B0: direct answer;
- B1: time / role prompt;
- B2: oracle historical evidence;
- B3: Historical RAG;
- later, only if necessary, LoRA / DAPT.

The project has not entered formal model experiments.

## Current Priority

真实历史材料
→ 小型真实 benchmark
→ 标注可行性
→ B0 / B1 / B2 / B3
→ 再决定是否训练。

## Current Scope Limits

- No large-scale model training at this stage.
- No paid external model API calls unless explicitly authorized.
- No access-control bypass, unauthorized scraping, or bulk downloading.
- Do not claim that any source set represents all late-Qing people.
