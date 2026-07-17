# Candidate Research Questions

## Candidate C1: Source-grounded Anachronism and Historical Ignorance Benchmark

**Question.** Can a small, source-grounded benchmark evaluate whether LLM/RAG systems answer late-Qing public-health questions without importing post-1900 facts, modern lexical meanings, or unsupported causal/value frames?

- Source ecology: open or small-sample customs medical reports, China Medical Missionary Journal, Chinese Recorder, Shanghai Municipal Council annual reports, and selected secondary history for annotation guidance.
- Target contribution: pilot benchmark and taxonomy for historically bounded answering.
- Evaluation object: answer-level factual, lexical, causal, value, source-attribution, and provenance errors; calibrated abstention.
- Feasibility risks: source population overrepresents treaty ports, missionaries, customs officers, and English-language administrative records.
- Negative-result value: even if models fail badly, the error analysis defines where presentist or source-unsupported answers occur.

## Candidate C2: Treaty-port Public-health RAG with Provenance and Caveat Scoring

**Question.** Does a lightweight historical RAG pipeline reduce anachronistic and source-unsupported answers compared with prompting alone when restricted to late-Qing treaty-port public-health sources?

- Source ecology: customs reports, missionary medical journals, municipal annual reports.
- Target contribution: retrieval/provenance workflow and evaluation rubric.
- Evaluation object: citation support, provenance caveats, temporal consistency, and answer abstention.
- Feasibility risks: OCR may be poor, and open sources may be mostly English.
- Negative-result value: if RAG does not improve answers, failure analysis can show whether retrieval, OCR, prompt framing, or source bias is the bottleneck.

## Candidate C3: Lexical and Conceptual Drift of `weisheng` and Public-health Terms

**Question.** How do late-Qing public-health terms such as `weisheng`, quarantine, vaccination, plague, sanitation, and hygiene shift across source families, and can models avoid flattening them into modern meanings?

- Source ecology: late-Qing periodicals and newspapers if authorized access exists; otherwise secondary scholarship plus small open samples from missionary/customs/municipal sources.
- Target contribution: lexical-anachronism taxonomy and term-attestation dataset.
- Evaluation object: translation choice, historical term sense, first-attestation/provenance, and cross-source variation.
- Feasibility risks: high dependence on Chinese full-text access; OCR and term segmentation are hard.
- Negative-result value: if data access is insufficient, the project can still define a term registry and access gap map.

## Candidate C4: Source-ecology Sensitivity in Historical RAG

**Question.** How much do answers about late-Qing disease, sanitation, quarantine, and vaccination change when retrieval is restricted to customs, missionary, municipal, newspaper, or gazetteer source families?

- Source ecology: same question set answered against separate source-family indexes.
- Target contribution: demonstration of archival/source-population bias in RAG outputs.
- Evaluation object: answer content, cited source family, uncertainty, missing groups, and contradiction across source ecologies.
- Feasibility risks: requires enough comparable sources from multiple families; Chinese newspaper/gazetteer access may block balanced comparison.
- Negative-result value: imbalance itself is a valuable DH finding about digitized-source availability.

## Candidate C5: OCR-aware Late-Qing Public-health Corpus Feasibility Study

**Question.** Which open or authorized late-Qing public-health sources can be transformed into reliable text for RAG or benchmark construction, and where do OCR/provenance failures dominate?

- Source ecology: item-level probes across customs, missionary, municipal, pictorial, newspaper, periodical, and gazetteer sources where lawful access exists.
- Target contribution: data feasibility and OCR-quality report with repeatable scripts.
- Evaluation object: text extraction success, character/word noise, metadata completeness, layout risks, and rights constraints.
- Feasibility risks: may not produce a publishable modeling result alone.
- Negative-result value: negative OCR/access findings directly shape the viable research design.

## Candidate C6: Lightweight Adaptation versus RAG for Historically Bounded Answers

**Question.** Under a small compute budget, do prompting, RAG, DAPT/TAPT, or LoRA-style adaptation best support historically bounded public-health answers?

- Source ecology: requires a pilot corpus and benchmark from C1/C2 first.
- Target contribution: method comparison for historical knowledge boundaries.
- Evaluation object: anachronism, attribution, abstention, and source-grounding metrics.
- Feasibility risks: adaptation is premature without stable data and benchmark; local compute constraints unknown.
- Negative-result value: if adaptation worsens anachronism or source fidelity, that is a publishable cautionary result.

## Candidate C7: Public-health Governance versus Medical Missionary Knowledge Boundaries

**Question.** How do customs/municipal governance records and missionary medical records differ in what they make knowable about disease, hygiene, vaccination, and quarantine before 1900?

- Source ecology: customs and municipal reports versus missionary medical journals.
- Target contribution: comparative digital-humanities source analysis feeding RAG/benchmark design.
- Evaluation object: topic coverage, actor vocabulary, disease categories, causal frames, and missing populations.
- Feasibility risks: English-language and elite institutional bias remains high.
- Negative-result value: a limited source-ecology comparison still clarifies what an individual-scale historical RAG system can and cannot claim.

