# Minimum Viable Pilot Study

## Aim

Test whether a small, source-grounded benchmark can expose anachronistic, unsupported, or overconfident answers in late-Qing public-health LLM/RAG settings.

## Pilot Corpus

Start with 4-8 verified passages from open or permission-compatible sources:

- Wellcome customs medical reports epitome.
- CRL China Medical Missionary Journal item(s).
- bnAsie Shanghai Municipal Council report.

Each passage must include source title, date, source family, page/stable locator, transcription status, rights/access note, and source-population caveat.

## Pilot Benchmark

Expand `benchmarks/pilot/pilot_items.jsonl` from 12 seed items to 20-30 items:

- 4 post-cutoff controls.
- 4 metadata/provenance items.
- 4 source-grounded factual items.
- 3 lexical-anachronism items.
- 3 causal/value-anachronism items.
- 3 source-misattribution items.
- 3 historical-ignorance/abstention items.

## Evaluation Conditions

1. Prompt-only baseline.
2. Source-provided prompting with one passage and metadata.
3. Local retrieval over curated passages and metadata.

No paid model API calls and no large training are required for the pilot.

## Metrics

- Temporal consistency.
- Source support.
- Correct answer policy.
- Provenance caveat.
- Accessibility caveat.
- Correct anachronism label.
- Attribution correctness.
- Abstention quality.

## Success Criteria

The pilot is successful if it demonstrates that:

- the item schema can be applied consistently;
- source-population caveats materially change expected answers;
- at least one evaluation condition exposes distinct anachronism or attribution failures;
- the source limitations are explicit enough to prevent overclaiming.

## Negative-result Value

If models fail, the pilot still produces a useful error taxonomy and evidence about why historical boundary evaluation is hard. If source passage extraction fails, the pilot still documents access/OCR constraints and narrows the next source strategy.

