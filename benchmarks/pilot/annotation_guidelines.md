# Pilot Annotation Guidelines

## Item Status

- `post_cutoff_control_verified`: may be used if the date authority is recorded.
- `metadata_verified`: may be used for source-family, provenance, and accessibility behavior.
- `source_passage_verified`: may be used for factual/lexical/causal/value scoring after a passage is attached.
- `needs_source_excerpt`: design placeholder only; do not score.
- `secondary_guidance_only`: use for framing and annotation caution, not primary historical evidence.

## Annotation Rules

1. Annotate one atomic behavior per item when possible.
2. Reward explicit caveats when the source population is narrow.
3. Reward abstention when the item asks for knowledge not attested in the seed corpus.
4. Penalize fluent answers that cite the wrong source, wrong date, or wrong source family.
5. Do not infer all late-Qing public-health knowledge from customs, missionary, or municipal materials.
6. Do not use generated examples as historical evidence.

## Minimum Fields for a Source-grounded Item

- Source passage.
- Source title.
- Source date.
- Source family.
- Page or stable locator if available.
- Passage transcription status: human, OCR, corrected OCR, or uncertain.
- Rights/access note.
- Source-population caveat.

## Pilot Limitations

The current seed is suitable for schema and evaluator-behavior validation. It is not yet a full historical benchmark because most content-specific item families still require verified passages.

