# Research Design

## 1. Snapshot

- Last updated: 2026-10-03
- Updated by cycle: State migration
- Current phase: exploratory design consolidation and source-constrained pilot preparation
- Core topic: late-Qing public-health historical knowledge boundaries, anachronism, historical ignorance, and provenance-constrained evaluation for LLM / RAG systems
- Current primary contribution: a source-constrained pilot benchmark for late-Qing public-health anachronism and historical ignorance
- Main blocker: stable, legally usable historical source passages and metadata, especially for Chinese-language late-Qing materials
- Next milestone: verify a small set of usable source passages and expand the pilot benchmark from seed items toward 20-30 scored items
- Overall confidence: medium

This file is the authoritative source for the current research design. Auxiliary structured files may help automation, but if they conflict with this document, this document prevails.

## 2. Research Background

The repository explores historically time-consistent language models from a digital-humanities perspective. The initial focus is late-Qing public-health knowledge, historical knowledge boundaries, anachronism, archival bias, Historical RAG, and lightweight parameter adaptation.

The project asks whether late-Qing public-health materials can support a feasible and evaluable research project about:

- temporal knowledge boundaries;
- factual, lexical, causal, and value-based anachronism;
- historical RAG;
- lightweight parameter adaptation;
- archival and source bias;
- historically appropriate uncertainty and ignorance.

The provisional historical cutoff is 1900-01-01. The preferred source period is approximately 1880-1899. The provisional thematic domain is disease, medicine, hygiene, quarantine, vaccination, water, sanitation, and public governance.

This stage remains exploratory. Large-scale model training, paid external model API calls, access-control bypass, unauthorized scraping, and bulk downloading are outside the current scope.

## 3. Core Research Question

Can modern LLM or RAG systems answer late-Qing public-health questions while respecting the historical knowledge boundary of the period?

Operationally, can such systems avoid importing post-1900 facts, modern lexical meanings, unsupported causal or value frameworks, false provenance, and unreasonable certainty when the historical record does not support an answer?

## 4. Research Questions

1. What has already been studied about historical language models, temporal leakage, ex-ante inference, anachronism, Historical RAG, and source-aware retrieval?
2. What remains underexplored for late-Qing Chinese public-health materials specifically?
3. Which historical sources are legally accessible, usable, and sufficiently documented for a small pilot benchmark?
4. How should historical knowledge boundaries and anachronism be operationalized across factual, lexical, causal, value, provenance, and uncertainty dimensions?
5. What can prompting, source-provided answering, lightweight local RAG, continued pretraining, LoRA, and hybrid methods each plausibly test?
6. Which direction best balances digital-humanities value, novelty, data feasibility, evaluability, compute feasibility, and robustness to negative results?
7. What is the minimum viable pilot study?

## 5. Current Research Story

The current recommended direction is to build a source-constrained pilot benchmark for late-Qing public-health anachronism and historical ignorance.

The research story is not to build a broad historical chatbot or to claim reconstruction of late-Qing public opinion. Instead, it treats historical question answering as a bounded evidentiary task: a model should know when a claim is temporally inadmissible, when a term carries modern meaning, when a causal or value frame is hindsight, when a source does not support the answer, and when the proper response is qualified uncertainty or refusal.

The first empirical step is small and auditable: use legally accessible samples from customs, missionary medical, municipal, treaty-port, or comparable historical-source channels; create atomic benchmark items; and compare baseline prompting, source-provided answering, and lightweight local retrieval before considering any adaptation or training route.

## 6. Current Contribution Claims

| Contribution | Current role | Evidence strength | Notes |
|---|---|---|---|
| Multi-level anachronism benchmark | Primary evaluation frame | Strong | Covers factual, lexical, causal, value, provenance, and uncertainty errors. |
| Historical ignorance | Primary conceptual contribution | Strong | Measures whether systems can acknowledge historically unavailable, inaccessible, or unsupported knowledge. |
| Provenance / source ecology | Primary digital-humanities contribution | Strong | Keeps source communities, institutional context, access, and archival bias visible. |
| Late-Qing Chinese public health | Domain anchor | Strong | Provides concrete historical stakes and source constraints. |
| Archive-dependent historical cognition | Interpretive contribution | Medium | Useful once source groups are balanced enough for comparison. |
| Lightweight adaptation | Deferred technical route | Weak for current stage | Revisit only after benchmark and source feasibility are stable. |

Protected scope: the project should remain centered on historically bounded knowledge, source support, uncertainty, and source ecology. It should not drift into a generic historical chatbot or a broad model-training project.

## 7. Conceptual Framework

The current framework treats historical consistency as a multi-dimensional relationship between a question, a target date, available sources, source populations, and model answer behavior.

Core dimensions:

- temporal admissibility: whether the answer imports knowledge unavailable before the cutoff;
- factual anachronism: post-cutoff events, institutions, discoveries, or categories;
- lexical anachronism: modern meanings or translations projected backward;
- causal anachronism: hindsight causal explanations unsupported by period evidence;
- value anachronism: present-day normative categories substituted for historical actors' categories without qualification;
- provenance and source ecology: whether an answer attributes claims to the correct source type, community, date, and evidentiary basis;
- historical ignorance: whether the system can say that a question is not answerable from the available historical record.

Recent Five-Day evidence strengthens the need to distinguish the broad problem of historical anachronism from this project's narrower source-constrained late-Qing public-health evaluation.

## 8. Data and Historical Sources

Priority source channels already identified:

- Wellcome customs medical or public-health materials;
- China Medical Missionary Journal records;
- Shanghai Municipal Council or treaty-port municipal materials;
- customs, missionary medical, and municipal / treaty-port sources more generally.

Current source status:

| Source or channel | Current status | Use in design |
|---|---|---|
| Wellcome Collection Catalogue API | Investigating | Potentially reduces discovery and metadata friction; still needs late-Qing public-health query and usage-limit probe. |
| Customs medical reports / Wellcome-related materials | Candidate | Possible source passages for the pilot benchmark. |
| CRL China Medical Missionary Journal entries | Candidate | Possible missionary-medical source channel; access and extractability still need verification. |
| bnAsie Shanghai Municipal Council annual reports | Candidate | Possible municipal / treaty-port source channel; OCR and metadata quality need verification. |

Known source limits:

- current sources cannot represent all late-Qing people;
- source populations may skew toward treaty ports, customs, missionary, municipal, elite, English-language, digitized, or institutionally preserved material;
- OCR quality, modern editorial intervention, digitization bias, and access restrictions must be documented;
- subscription or access-controlled materials may only be used when authorization and terms allow.

## 9. Benchmark Design

Benchmark name: late-Qing public-health historical knowledge boundary pilot benchmark.

Purpose: evaluate whether LLM or RAG systems avoid post-cutoff facts, modern lexical meanings, unsupported causal or value frameworks, false provenance, and unwarranted certainty when answering late-Qing public-health questions.

Scope:

- target period: 1880-01-01 to 1899-12-31;
- provisional cutoff: 1900-01-01;
- initial source ecology: customs, missionary medical, and treaty-port municipal materials.

Allowed item families:

- `post_cutoff_control`;
- `metadata_provenance`;
- `source_grounded_factual`;
- `lexical_anachronism`;
- `causal_anachronism`;
- `value_anachronism`;
- `source_misattribution`;
- `historical_ignorance`.

Minimum viable scale:

- first pilot: 12-20 seed items;
- next target: 20-30 items;
- at least 8 items should eventually be supported by real verified source passages.

Items with `needs_source_excerpt` should not be treated as scoreable until their historical evidence is verified.

## 10. Experimental Design

Current candidate baselines:

| Condition | Name | Status | Current role |
|---|---|---|---|
| B0 | Direct answer | Candidate | Baseline for default model behavior without source constraints. |
| B1 | Time / role prompt | Candidate | Tests prompt-only temporal control and residual anachronism. |
| B2 | Oracle historical evidence | Candidate | Tests source-grounded answering without retrieval noise. |
| B3 | Historical RAG | Candidate | Tests realistic retrieval plus generation after corpus and benchmark stabilize. |
| B4 | LoRA / DAPT | Deferred | Consider only after B0-B3 and benchmark feasibility are established. |

Current priority order:

1. verify real historical materials;
2. build a small real benchmark;
3. test annotation and scoring feasibility;
4. run B0 / B1 / B2 / B3;
5. decide later whether any adaptation or training is justified.

The project has not entered formal model experiments.

## 11. Current Hypotheses

No separate `hypotheses.yaml` currently exists. The current working hypotheses are provisional and should not be treated as confirmed findings:

- Source-constrained prompts or retrieval should reduce some factual and provenance errors compared with direct answering.
- Prompt-only temporal role control is expected to leave residual anachronism.
- Some questions should require qualified uncertainty or refusal because available period sources do not support a confident answer.
- Lightweight adaptation should remain deferred until benchmark and source feasibility are stable.

## 12. Evidence For / Against

Evidence supporting the current design:

- The existing contribution map rates multi-level anachronism, historical ignorance, provenance / source ecology, and late-Qing Chinese public health as strong contribution candidates.
- The pilot benchmark specification already defines item families, required fields, evidence statuses, answer policies, and scoring dimensions.
- The recommended direction and minimum viable pilot both converge on a small, source-constrained benchmark rather than a broad training project.
- The Five-Day synthesis found that Wellcome API may reduce discovery and metadata friction.

Evidence creating pressure or risk:

- Recent work on historical anachronism, historical pretraining, ex-ante inference, and HistoRAG overlaps with broad formulations of the project.
- A generic claim such as "historical language models can avoid anachronism" is likely too broad.
- A generic "build Historical RAG" contribution is insufficient without source-constrained evaluation, historical ignorance, and late-Qing public-health specificity.
- TDBench is useful as a benchmark-construction reference but does not solve late-Qing historical-data availability.

## 13. Open Questions

- Which legally accessible source passages can support the first scoreable benchmark items?
- Can the Wellcome Catalogue API and IIIF metadata reliably identify late-Qing public-health materials relevant to customs, missionary medicine, quarantine, hygiene, or sanitation?
- Are Chinese-language late-Qing public-health sources available in a form compatible with the project without violating access restrictions?
- How should source populations be described so the benchmark does not overclaim representativeness?
- Can local lightweight RAG reduce anachronism and false provenance, or does it mainly expose retrieval and OCR limitations?
- Should historical ignorance be separated into model-capability ignorance and historical-source-ecology uncertainty?
- When, if ever, would LoRA / DAPT become worth testing?

## 14. Blockers

Current formal blocker file has no active blockers, but the design still depends on resolving practical constraints:

- stable legally usable historical passages;
- OCR and transcription quality for scanned or multilingual materials;
- metadata completeness and stable citations;
- subscription or platform restrictions for Chinese newspapers, periodicals, or full-text databases;
- balanced source ecology across customs, missionary, municipal, and Chinese-language materials;
- avoiding claims that digitized or institutionally preserved material represents all late-Qing actors.

## 15. Next Research Priorities

1. Run a small source probe for Wellcome API and one or two candidate public-health queries.
2. Verify whether candidate records provide usable metadata, IIIF/PDF/image access, dates, and stable identifiers.
3. Select a small set of source passages or metadata records for benchmark item expansion.
4. Expand pilot items toward 20-30 items while separating scoreable items from `needs_source_excerpt` items.
5. Test whether a minimal local retrieval prototype can preserve source citation and provenance constraints.
6. Continue Daily multi-channel monitoring for papers, datasets, archives, methods, resources, and project impact.
7. Let the next Five-Day update evidence strength, blockers, priorities, and registries; reserve major research-story restructuring for Half-Month.

## 16. Rejected / Deferred Directions

Rejected for the current stage:

- large-scale model training;
- claiming to represent all late-Qing people;
- building a commercial historical chatbot;
- using generated text as historical evidence;
- bypassing paywalls, authentication, CAPTCHAs, access controls, licensing restrictions, robots policies, or bulk-download restrictions.

Deferred:

- LoRA / DAPT / QLoRA comparison until real passages, a stable benchmark, and a small corpus exist;
- cross-source ecology RAG sensitivity until more balanced legal sources are available;
- `weisheng` and Chinese public-health lexical drift until authorized Chinese full text or open subsets are available;
- OCR-first corpus pipeline until small Wellcome and bnAsie OCR quality probes are complete.
