# Cross-branch Synthesis

## Verified Findings

1. The repository now has a literature matrix covering temporal NLP, historical NLP, RAG, adaptation, and late-Qing public-health conceptual history.
2. The source registry identifies twelve source families and records access, OCR/text, metadata, bias, and probe status.
3. Four high-priority source entry points were reachable with HTTP 200 in the metadata-only T30 probe:
   - Wellcome customs medical reports epitome.
   - CRL China Medical Missionary Journal record.
   - bnAsie Shanghai Municipal Council annual report page.
   - Academia Sinica Chinese Maritime Customs portal.
4. T31 found strong PDF/download/IIIF link signals for Wellcome and CRL, medium PDF/full-text signals for bnAsie, and no simple direct text/download links on the Academia Sinica landing page.
5. The pilot benchmark schema and JSONL seed validate with 0 errors in the T51 engineering probe.
6. The pilot seed contains 12 items: 10 ready for policy/metadata/post-cutoff scoring and 2 correctly blocked until verified source passages are added.

## Interpretations

1. The project is feasible as an individual-scale exploratory digital-humanities project if the first contribution is framed as source-grounded benchmark and provenance-aware evaluation, not large-scale model training.
2. The first source ecology should be described narrowly: treaty-port, customs, missionary, municipal, and partly English-language materials.
3. The strongest scholarly contribution is likely the operationalization of historical knowledge boundaries: date, source population, accessibility, provenance, archival bias, and historically appropriate ignorance.
4. RAG is useful as a provenance/evaluation scaffold, but a full historical RAG system should wait until verified passages and OCR quality are available.
5. Lightweight adaptation remains a plausible later comparison, but it is premature before a source-grounded benchmark and stable corpus exist.

## Unresolved Questions

1. Can verified source passages be extracted lawfully and reproducibly from Wellcome, CRL, and bnAsie items?
2. What is the actual OCR quality of PDFs/images for late-Qing public-health passages?
3. Can Chinese-language source families be included without subscription or no-batch-download violations?
4. Can annotators consistently distinguish factual, lexical, causal, value, attribution, and provenance anachronism?
5. Does retrieval improve historically bounded answering compared with source-provided prompting?
6. How should target actor/source ecology be represented when sources are multilingual and institutionally biased?

## Recommended Direction

Proceed with the C1 direction: a source-grounded pilot benchmark for late-Qing public-health anachronism and historical ignorance. Pair it with a minimal local RAG/provenance prototype only after verified passages are added.

## Viable Alternatives

- C7: Compare customs/municipal governance records with missionary medical records as a source-ecology study.
- C2: Build a treaty-port public-health RAG prototype with provenance and caveat scoring.
- C5: Extend OCR and metadata feasibility into a standalone data paper or technical appendix.

## Deferred or Rejected Directions

- Large-scale model training: rejected for this stage.
- LoRA/DAPT comparison: deferred until benchmark and corpus are stable.
- Bulk use of Shen Bao, late-Qing periodicals, ProQuest-style newspaper databases, or commercial gazetteers: blocked unless authorized access and terms are available.
- Claims about all late-Qing people: rejected as incompatible with the current source ecology.

## Next Autonomous Tasks

1. Extract 4-8 verified passages from Wellcome and bnAsie sources, preserving page/source metadata and rights notes.
2. Add passage-grounded factual, lexical, causal, and value-anachronism items to the benchmark.
3. Add family-aware retrieval filters so post-cutoff controls do not retrieve historical source records.
4. Run a small prompt-only versus source-provided versus local retrieval comparison without paid APIs.
5. Explore authorized Chinese-language source access separately and document terms before use.

