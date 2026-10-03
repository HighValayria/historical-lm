# Daily Protocol

## Purpose

Answer only:

> What genuinely new and project-relevant information appeared in the most recent cycle?

## Watch Areas

### Papers

- historical language model
- historical LM
- period-specific language model
- historical NLP
- temporal knowledge
- temporal leakage
- knowledge cutoff
- ex-ante reasoning
- anachronism
- cultural anachronism
- temporal consistency
- Historical RAG
- historical retrieval augmented generation
- provenance-aware RAG
- source-aware RAG
- source diversity
- digital humanities LLM
- computational history LLM
- historical archives LLM

### Datasets / Benchmarks

- temporal knowledge benchmark
- historical QA
- temporal leakage benchmark
- anachronism benchmark
- historical text datasets
- Chinese historical NLP datasets
- OCR datasets
- provenance datasets

### Historical Sources

- Wellcome historical collections
- CRL historical Chinese materials
- China Medical Missionary Journal
- Chinese Maritime Customs medical reports
- Shanghai Municipal Council reports
- bnAsie
- 晚清期刊
- 《申报》
- 地方志
- 医学期刊
- 医学教科书
- 海关报告
- 租界/市政卫生资料

### Methods

- historical OCR
- document parsing
- historical embedding
- retrieval
- reranking
- provenance
- source attribution
- temporal retrieval

## Required Actions

1. Process only newly observed items.
2. Deduplicate against `state/seen_papers.json`, `state/seen_datasets.json`, and the registry files.
3. Assign relevance as `high`, `medium`, or `low`.
4. Record reading depth as `title_only`, `abstract_read`, or `full_text_read`.
5. Add high-relevance items to the appropriate queues in `state/queues.json`.
6. Update registry files only when there is concrete information to record.
7. Write the daily report to `reports/daily/YYYY-MM-DD.md`.
8. After a successful Daily run, update `last_daily`, increment `daily_run_count`, and update `last_successful_run` in `state/automation_state.json`.

## Limits

Daily must not:

- rewrite the research design;
- produce a long literature review;
- deeply analyze dozens of papers;
- rerun old papers or datasets;
- invent updates when nothing material appeared.

If there is no material update, the report may contain only:

```text
No material update.
```
