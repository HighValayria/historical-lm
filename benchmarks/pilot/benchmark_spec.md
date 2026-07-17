# Pilot Benchmark Specification

## Name

Late-Qing Public-health Historical Boundary Benchmark, pilot seed.

## Purpose

Evaluate whether an LLM or RAG system can answer public-health questions about late-Qing source ecologies without importing post-1900 facts, modern lexical meanings, unsupported causal/value frames, or false source attributions.

## Scope

- Target period: 1880-01-01 to 1899-12-31.
- Provisional cutoff: 1900-01-01.
- Initial source ecology: reachable item-level sources from T30/T31, especially customs, missionary, and Shanghai municipal/treaty-port materials.
- Intended first use: benchmark design and lightweight RAG/provenance prototype, not a definitive historical evaluation.

## Item Families

| Family | Purpose | Requires historical passage? | Example answer policy |
|---|---|---:|---|
| `post_cutoff_control` | Test rejection of post-1900 institutions, events, or terminology. | no, but needs a stable date authority | reject_anachronism |
| `metadata_provenance` | Test source-family, date, title, rights, and provenance awareness. | no, metadata is enough | answer_with_caveat |
| `source_grounded_factual` | Test atomic factual claims from a passage. | yes | answer_with_citation |
| `lexical_anachronism` | Test historical term sense and translation caution. | yes | answer_with_caveat |
| `causal_anachronism` | Test whether answers avoid later teleological explanations. | yes | answer_with_caveat or reject_anachronism |
| `value_anachronism` | Test separation of present-day analysis from actor categories. | yes | answer_with_caveat |
| `source_misattribution` | Test whether a claim is attached to the correct source. | yes or metadata-only for source-family checks | reject_or_correct_attribution |
| `historical_ignorance` | Test abstention when evidence is unavailable, post-cutoff, or outside source ecology. | no or yes | abstain_with_reason |

## Required Item Fields

- `item_id`
- `family`
- `question`
- `target_date`
- `cutoff_date`
- `source_ids`
- `source_population`
- `audience_or_actor`
- `evidence_status`
- `expected_answer_policy`
- `gold_behavior`
- `anachronism_labels`
- `accessibility_status`
- `provenance_requirements`
- `scoring_notes`
- `risk_notes`

## Evidence Status Values

- `source_passage_verified`: a passage from a historical source directly supports the item.
- `metadata_verified`: item tests source metadata/provenance only.
- `post_cutoff_control_verified`: item tests a stable post-cutoff entity/event/date.
- `needs_source_excerpt`: item is a placeholder and must not be used for scoring.
- `secondary_guidance_only`: item is informed by secondary scholarship but lacks a primary passage.

## Answer Policies

| Policy | Expected behavior |
|---|---|
| `answer_with_citation` | Answer the question and cite the supporting source/passage. |
| `answer_with_caveat` | Answer only with explicit provenance, source-population, or accessibility caveats. |
| `abstain_with_reason` | Refuse or defer because evidence is unavailable, outside source ecology, or historically inaccessible. |
| `reject_anachronism` | Identify the anachronistic element and avoid answering as if it were available before 1900. |
| `reject_or_correct_attribution` | Reject unsupported citation or correct the source-family/date/provenance. |

## Scoring Dimensions

Each item can be scored on a 0/1 basis for:

1. Temporal consistency.
2. Source support.
3. Correct answer policy.
4. Provenance caveat.
5. Accessibility caveat.
6. Correct anachronism label.
7. Attribution correctness.
8. Abstention quality, when applicable.

## Exclusion Rules

- Do not score `needs_source_excerpt` items.
- Do not treat generated paraphrases as historical evidence.
- Do not treat a digitized source's availability today as proof of historical circulation.
- Do not infer all late-Qing Chinese public-health knowledge from treaty-port, missionary, customs, or municipal sources.
- Do not use subscription or restricted materials unless access terms explicitly permit the intended use.

## Minimum Pilot Size

- 12-20 seed items for schema validation.
- At least 3 source metadata records.
- At least 4 post-cutoff controls.
- At least 4 source-grounded passage items after lawful excerpts are available.
- At least 2 historical-ignorance or abstention items.

## Reporting Requirements

The pilot report must distinguish:

- verified source-grounded items;
- metadata-only items;
- post-cutoff controls;
- placeholders needing close reading;
- source-population limitations;
- OCR/provenance limitations.

