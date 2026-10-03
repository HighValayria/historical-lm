# Daily Protocol

## Purpose

Daily Research Radar is a multi-channel research-environment check, not a paper-search task.

Daily must answer:

> What genuinely new and project-relevant information appeared across the research environment?

Daily reports must be written in Chinese. Paper titles, dataset names, archive names, identifiers, enum values such as `newly_discovered`, and paths may remain in their original form.

Daily prioritizes coverage over depth. A rich paper channel must not replace checks of datasets, archives, methods, resources, and project impact.

## Fixed Channels

Daily has six required channels:

1. `PAPERS`
2. `DATASETS`
3. `ARCHIVES`
4. `METHODS`
5. `RESOURCES`
6. `PROJECT_IMPACT`

Daily is complete only after every channel has one of these statuses:

- `checked_material_update`
- `checked_no_material_update`
- `blocked`

Do not use `skipped` or `not_needed`.

If a channel cannot be checked because of network, access, or environment problems, mark it `blocked`, write the blocker to `state/blockers.json`, and continue with the remaining channels.

## Breadth-First Strategy

Daily must check channels in this first-round order:

1. `PAPERS`
2. `DATASETS`
3. `ARCHIVES`
4. `METHODS`
5. `RESOURCES`
6. `PROJECT_IMPACT`

Only after all six channels have been checked may Daily return to a high-value channel for additional exploration.

If context, time, or quota is tight, reduce depth in every channel. Do not fully execute `PAPERS` and abandon the other channels.

Soft budget rule: `PAPERS` should not default to more than about 35% of Daily exploration effort. Do not follow multi-hop citation graphs during Daily; put those into Five-Day queues instead.

## Channel 1: PAPERS

Check for:

- newly published papers;
- newly discovered existing work;
- new citations of seed papers;
- seed-paper references not yet registered;
- existing paper updates;
- reviews, benchmark papers, and method papers.

Key themes:

- historical language model;
- temporal knowledge;
- temporal leakage;
- knowledge cutoff;
- ex-ante reasoning;
- anachronism;
- Historical RAG;
- provenance;
- source diversity;
- digital humanities plus LLM.

For papers, "new" means:

```text
new_to_system = absent from state/seen_papers.json and evidence/literature_master.csv
```

This includes papers published months or years ago but first discovered by this system today.

Classify paper findings as:

- `newly_published`: recently published, newly posted, newly accepted, or newly public work not previously in this system.
- `newly_discovered`: older work not previously in this system.
- `existing_paper_update`: material new information about a known paper.

Deduplicate using this priority:

1. DOI;
2. arXiv ID;
3. Semantic Scholar, OpenAlex, ACL Anthology, or another stable paper ID;
4. normalized title.

High-relevance paper findings go to `state/queues.json -> deep_reading`.

## Channel 2: DATASETS

Check datasets independently. A dataset mentioned in a paper does not complete the `DATASETS` channel.

Check for:

- new dataset;
- new benchmark;
- known dataset new version;
- new open download;
- license change;
- new data fields;
- historical QA;
- temporal benchmark;
- anachronism benchmark;
- Chinese historical NLP dataset;
- OCR dataset;
- provenance / source attribution dataset.

For each material dataset finding, judge whether it really exists and record, when available:

- public access;
- license;
- language;
- time range;
- domain;
- fit for the current project.

High-relevance dataset findings go to `state/queues.json -> dataset_review`.

## Channel 3: ARCHIVES

Check historical sources and digital archives independently.

Focus on:

- Wellcome Collection;
- China Medical Missionary Journal;
- Chinese Maritime Customs;
- Shanghai Municipal Council;
- bnAsie;
- 晚清期刊数据库;
- 《申报》;
- 地方志;
- 医学期刊;
- 医学教科书;
- 海关报告;
- 市政 / 租界卫生资料;
- new digitization projects;
- new OCR access;
- new APIs;
- new full-text access;
- metadata or license changes.

This channel asks:

> Have historical materials become easier to access or use?

High-relevance archive findings go to `state/queues.json -> archive_review`.

## Channel 4: METHODS

Check methods and tools that may change implementation cost or experiment design.

This can include papers, models, libraries, releases, or open-source implementations.

Focus on:

- historical OCR;
- document layout parsing;
- handwritten / printed historical text recognition;
- embedding;
- retrieval;
- reranking;
- temporal retrieval;
- provenance-aware retrieval;
- source attribution;
- citation grounding;
- long context;
- structured extraction;
- evaluation;
- uncertainty / abstention.

If a method is found in `PAPERS`, still answer separately whether it has direct engineering value for this project.

High-relevance method findings go to `state/queues.json -> method_review`.

## Channel 5: RESOURCES

Check non-paper research resources:

- GitHub repository;
- research toolkit;
- benchmark framework;
- annotation tool;
- OCR pipeline;
- digital humanities platform;
- corpus browser;
- archive search interface;
- citation / provenance tool;
- dataset processing scripts;
- research project pages.

This channel asks:

> Did anything appear that can directly reduce current research work?

High-relevance resource findings go to `state/queues.json -> resource_review`.

## Channel 6: PROJECT_IMPACT

This is an independent project-state check based on all findings from the run.

Answer:

- Is there direct competing work?
- Is there a new resource that could resolve a current blocker?
- Did data feasibility materially change?
- Does anything need to enter a Five-Day queue?
- Is any current contribution clearly threatened?
- Is there a new research opportunity?

If there is no project-level impact, write:

```text
No project-level impact.
```

## Required State Updates

After a successful Daily run, update `state/channel_state.json` separately for each checked non-impact channel:

```json
{
  "PAPERS": {
    "last_checked": "YYYY-MM-DD",
    "last_material_update": "YYYY-MM-DD or null"
  }
}
```

Update `last_material_update` only when that channel has `checked_material_update`.

Update `state/automation_state.json` only when schedule rules allow it.

## Report Format

Every Daily report must use this Chinese structure, even when a channel has no material update:

```markdown
# Daily Research Radar — YYYY-MM-DD

## 1. Papers

Status:

Newly published:
Newly discovered:
Existing updates:

Material findings:

## 2. Datasets / Benchmarks

Status:

Material findings:

## 3. Historical Archives / Sources

Status:

Material findings:

## 4. Methods / Tools

Status:

Material findings:

## 5. Research Resources

Status:

Material findings:

## 6. Project Impact

Impact:

Queues updated:

## Coverage Check

- PAPERS: checked / blocked
- DATASETS: checked / blocked
- ARCHIVES: checked / blocked
- METHODS: checked / blocked
- RESOURCES: checked / blocked
- PROJECT_IMPACT: checked / blocked
```

If a channel has no new finding, write:

```text
Status: checked_no_material_update
No material update.
```

## Limits

Daily must not:

- rewrite the research design;
- produce a long literature review;
- deeply analyze many papers;
- let `PAPERS` consume the whole run;
- skip datasets, archives, methods, resources, or project impact;
- invent updates when nothing material appeared.

Daily discovers, deduplicates, judges relevance, classifies, and queues. Five-Day performs deeper reading and cross-type synthesis.
