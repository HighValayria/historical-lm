# Final Exploratory Report

## 1. Run Scope

This first autonomous exploration run investigated whether late-Qing public-health materials can support a feasible, evaluable, individual-scale digital-humanities project about historical knowledge boundaries, anachronism, historical RAG, and lightweight model adaptation.

The provisional cutoff was 1900-01-01. The provisional source period was 1880-01-01 to 1899-12-31.

## 2. Verified Findings

### 2.1 Literature and Method Landscape

The literature landscape supports the importance of temporal evaluation, historical-domain language adaptation, RAG/provenance, and lightweight adaptation. Key method references include temporal mismatch and time-aware language models, historical-domain pretraining, RAG, DAPT/TAPT, LoRA/QLoRA, and diachronic semantic-change work.

No ready-made benchmark was identified for source-grounded pre-1900 Chinese public-health anachronism and historically appropriate ignorance. This is the central gap.

Primary artifacts:

- `evidence/literature_matrix.md`
- `reports/nodes/T10.md`

### 2.2 Historical Source Landscape

The source registry identified twelve relevant source families. Open or item-level probe candidates are strongest for:

- Wellcome customs medical reports epitome.
- CRL China Medical Missionary Journal record.
- bnAsie Shanghai Municipal Council annual report page.
- Academia Sinica Chinese Maritime Customs portal.

High-value Chinese newspaper and periodical resources exist, including Shen Bao and late-Qing periodical databases, but they are subscription-bound or terms-constrained for bulk use.

Primary artifacts:

- `evidence/source_registry.md`
- `reports/nodes/T11.md`

### 2.3 Concept Map

The concept map operationalizes historical knowledge boundary as more than a date cutoff. It includes chronology, source circulation, knowledge accessibility, archival survival, provenance, and historically appropriate ignorance.

The benchmark taxonomy separates:

- factual anachronism;
- lexical anachronism;
- causal anachronism;
- value anachronism;
- source misattribution;
- provenance uncertainty;
- historical ignorance.

Primary artifacts:

- `evidence/concept_map.md`
- `reports/nodes/T12.md`

### 2.4 Access, OCR, and Metadata Probes

T30 verified reachability for four source entry points with HTTP 200. T31 found:

- high follow-up feasibility for Wellcome and CRL pages;
- medium follow-up feasibility for bnAsie;
- low extraction feasibility from the Academia Sinica landing page without manual navigation.

No explicit OCR keyword signal was found on the four probed pages. This means the first benchmark should use curated excerpts and metadata rather than assume a clean OCR corpus.

Primary artifacts:

- `probes/data_access/access_probe_summary.md`
- `probes/ocr/ocr_metadata_probe_summary.md`
- `reports/nodes/T30.md`
- `reports/nodes/T31.md`

### 2.5 Benchmark and Engineering Probe

The run produced a benchmark specification, a schema, a 12-item pilot seed, and a local no-training engineering probe.

The engineering probe validated:

- source records: 4;
- pilot items: 12;
- validation errors: 0;
- scoring-ready items: 10;
- items requiring verified passages: 2.

Primary artifacts:

- `benchmarks/pilot/benchmark_spec.md`
- `benchmarks/pilot/schema.json`
- `benchmarks/pilot/pilot_items.jsonl`
- `benchmarks/pilot/source_records.jsonl`
- `prototypes/min_engineering_probe/probe_summary.md`

## 3. Interpretations

The project is feasible if framed as a benchmark-first, source-critical digital-humanities project. Its value lies in testing historically bounded answering, not in claiming to reconstruct late-Qing public opinion or in training a large model.

The first pilot should explicitly identify its source ecology as customs, missionary, municipal/treaty-port, and partly English-language. That limitation is not a defect if it is part of the research question.

RAG is a strong near-term technical route because it exposes provenance and source-population caveats. LoRA, DAPT, and hybrid adaptation are plausible later comparisons but premature now.

## 4. Recommended Direction

Build a source-grounded pilot benchmark for late-Qing public-health anachronism and historical ignorance.

Working question:

Can a small benchmark evaluate whether LLM/RAG systems answer late-Qing public-health questions without importing post-1900 facts, modern lexical meanings, unsupported causal/value frames, or unsupported source attributions?

## 5. Viable Alternatives

- Compare customs/municipal governance records with missionary medical records as different public-health knowledge ecologies.
- Build a treaty-port historical RAG prototype with provenance and caveat scoring.
- Extend OCR and metadata feasibility into a standalone data feasibility study.

## 6. Rejected or Deferred Directions

- Large-scale model training: rejected for this stage.
- LoRA/DAPT comparison: deferred until verified passages and stable benchmark data exist.
- Bulk scraping of subscription databases: blocked without explicit authorization.
- Claims about all late-Qing people: rejected because the source ecology cannot support them.

## 7. Unresolved Questions

1. Can 4-8 verified passages be extracted lawfully and reproducibly from the top source candidates?
2. What is the actual OCR quality of the Wellcome and bnAsie PDFs?
3. Can authorized Chinese-language sources be added without violating access terms?
4. Can annotators consistently apply the anachronism taxonomy?
5. Does retrieval reduce anachronism compared with source-provided prompting?

## 8. Minimum Viable Pilot

The minimum viable pilot is specified in `reports/minimum_viable_pilot.md`.

## 9. Next Autonomous Tasks

The next-run backlog is specified in `state/NEXT_RUN_BACKLOG.yaml`.

## 10. Evidence Boundary

This report does not treat model-generated text as historical evidence. It does not claim the source ecology represents all late-Qing people. It distinguishes verified probe outputs from interpretations and recommendations.

