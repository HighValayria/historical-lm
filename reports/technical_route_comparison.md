# Technical Route Comparison

## Decision Context

The selected direction is a source-grounded benchmark for historical knowledge boundaries. The first engineering goal is therefore not "make a model smarter"; it is to test whether the benchmark schema, source metadata, retrieval, citation, and answer-policy evaluation can be operationalized.

## Route Matrix

| Route | What it tests | Data requirement | Compute requirement | Strength | Main risk | First-run decision |
|---|---|---|---|---|---|---|
| Prompting only | Baseline behavior without retrieved sources | Benchmark items only | very low | Cheap baseline for anachronism and abstention failures | Model may answer fluently from modern priors | Keep as baseline |
| Source-provided prompting | Whether explicit source metadata/passages improve answer policy | Curated snippets or metadata | very low | Separates prompt framing from retrieval | Still not scalable and may overfit prompt wording | Keep as baseline |
| Local lightweight RAG | Whether retrieval and source metadata can support provenance/caveats | Small source records and snippets | low | Aligns with C1/C2; no paid API or training required | Retrieval over metadata is not full historical evidence | Select for T51 |
| OCR-first corpus pipeline | Whether sources can become usable text | Open PDFs/images and OCR tooling | medium | Necessary for later passage items | T31 shows OCR is unproven; may dominate the run | Defer to next-run source-passage task |
| DAPT/TAPT | Whether domain continued pretraining helps historical text handling | Larger clean corpus | medium-high | Supported by NLP literature | Premature without clean corpus and benchmark | Defer |
| LoRA/QLoRA | Whether lightweight adaptation improves historical boundary behavior | Stable training/eval set | medium | Individual-scale compared with full finetuning | May amplify modern priors or overfit tiny data | Defer |
| Hybrid RAG + PEFT | Whether retrieval plus adaptation works best | Corpus, benchmark, training set | high | Long-term promising | Too many moving parts for uncertainty-reduction run | Defer |

## Selected Minimum Engineering Route

T51 should implement a local, no-training prototype that:

1. validates the benchmark schema and JSONL files;
2. builds a tiny lexical retriever over `source_records.jsonl` and item metadata;
3. produces retrieval candidates for each pilot item;
4. checks whether item evidence statuses allow scoring;
5. outputs a compact evaluation-readiness report.

## Why This Route

- It directly tests the benchmark mechanics selected in T21 and designed in T40/T41.
- It avoids paid APIs and large training.
- It remains useful even if OCR/full passages are not yet available.
- It can be expanded later to BM25/vector retrieval, passage OCR, model calls, and PEFT experiments.

## Deferred Technical Questions

- Does OCR from the Wellcome and bnAsie PDFs produce reliable historical text?
- Does RAG reduce anachronism compared with source-provided prompting?
- Does LoRA or DAPT improve term sense without harming historical ignorance?
- Can Chinese-language term drift be evaluated without authorized Chinese full-text database access?

