# Daily Protocol

## Purpose

Answer only:

> What genuinely new and project-relevant information appeared in the most recent cycle?

Daily Research Radar is not only a publication-date news monitor. For papers, "new" means:

```text
new_to_system = the paper is absent from state/seen_papers.json and evidence/literature_master.csv
```

This includes papers that were published months or years ago but are first discovered by this research system today.

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

1. Search for both freshness and coverage signals.
2. Deduplicate against `state/seen_papers.json`, `evidence/literature_master.csv`, `state/seen_datasets.json`, and registry files.
3. Classify new-to-system papers as `newly_published` or `newly_discovered`.
4. Classify already-known papers with material new information as `existing_paper_update`.
5. Assign relevance as `high`, `medium`, or `low`.
6. Record reading depth as `title_only`, `abstract_read`, or `full_text_read`.
7. Add only high-priority or high-relevance paper discoveries to `state/queues.json -> deep_reading`.
8. Update registry files only when there is concrete information to record.
9. Write the daily report to `reports/daily/YYYY-MM-DD.md`.
10. After a successful Daily run, update `last_daily`, increment `daily_run_count`, and update `last_successful_run` in `state/automation_state.json` when schedule rules allow it.

## Paper Discovery Semantics

Daily must process two kinds of new-to-system papers:

- `newly_published`: recently published, newly posted, newly accepted, or newly public work that was not previously in this system.
- `newly_discovered`: older work that was not previously in this system and was found through search, citation trails, related work, dataset pages, author pages, project pages, or other research paths.

Do not describe an older paper as a "new paper" merely because it was found today. Use "newly discovered relevant work."

If a paper already exists in `state/seen_papers.json` or `evidence/literature_master.csv`, do not create a new record. If there is material new information, record it as `existing_paper_update`.

Allowed existing-paper updates include:

- new version;
- new formal publication information;
- new code;
- new dataset;
- new citation information;
- new reading status;
- changed relevance judgment.

## Paper Deduplication

Use this identifier priority:

1. DOI;
2. arXiv ID;
3. Semantic Scholar, OpenAlex, ACL Anthology, or another stable paper ID;
4. normalized title.

Title-only matching is the fallback, not the default.

## Search Strategy

### Freshness Search

Use this to discover genuinely recent work, especially:

- last 30 days;
- recent months;
- current-year papers.

Focus on historical LM, temporal knowledge, temporal leakage, anachronism, Historical RAG, provenance, digital humanities plus LLMs, historical QA / benchmarks, and late-Qing / Chinese historical NLP.

### Coverage Search

Use this to fill gaps in the research knowledge graph. Coverage search may discover older papers through:

- current keyword searches;
- seed-paper references;
- seed-paper citations;
- high-relevance papers' related work;
- benchmark references;
- dataset papers;
- repeated authors or methods in existing reports;
- important works surfaced by field surveys.

Coverage search should be incremental. Do not rescan the entire literature history every day.

## Paper Priority

Highest priority:

1. recent publication plus high relevance;
2. older work that directly challenges or covers the current contribution;
3. older work with a clear citation relationship to a core seed paper;
4. older work that fills an obvious gap in the current literature matrix.

Medium priority:

5. work strongly related to the research design but not a core competing work;
6. work that provides a reusable dataset, benchmark, method, or historical source.

Low priority:

7. keyword overlap only;
8. weak connection to the core question.

Daily performs discovery, deduplication, relevance judgment, initial classification, and queueing. Five-Day handles deeper reading, relation to existing research, contribution-risk analysis, and research-graph updates.

## Daily Report Format

When papers are present, use these sections:

```text
## Newly Published

## Newly Discovered Existing Work

## Existing Paper Updates
```

Empty sections may be omitted. Include counts when useful, for example:

```text
Newly Published: 2
Newly Discovered Existing Work: 4
Existing Paper Updates: 1
```

During the cold-start phase, `newly_discovered` may be much larger than `newly_published`. This is expected and should fade naturally as `seen_papers.json` and `literature_master.csv` become more complete.

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
