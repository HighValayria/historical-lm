# Auditable multi-dimensional scoring framework

## Rule: no composite score

Each dimension is reported independently at item, evidence-group and condition level. No weighted sum or single “historical accuracy” score is authorized for this pilot.

## Dimensions

| Dimension | Values | What is judged | Minimum evidence needed |
|---|---|---|---|
| `source_fact_accuracy` | `2 correct`, `1 partial`, `0 incorrect`, `NA` | Whether the response correctly reports the source-level content asked by the item | Verified passage/page and accepted-answer record |
| `temporal_boundary_status` | `compliant`, `violation`, `unscorable`, `NA` | Whether an output span uses knowledge that is demonstrably after the cutoff as if contemporaneous | Independent chronology record, cutoff, actor/access scope and cited output span |
| `source_attribution` | `2 correct`, `1 ambiguous`, `0 misattributed`, `NA` | Whether claims remain attached to the correct author/speaker/institution and archive population | Source metadata, surrounding context and output span |
| `evidence_fidelity` | `2 faithful`, `1 minor_overreach`, `0 contradiction_or_reversal`, `NA` | Whether E2/E3 follows the supplied Oracle including qualifications | Exact Oracle text and output span |
| `unsupported_content` | `none`, `minor`, `major`, `NA` | Material additions not supported by evidence or properly marked background knowledge | Complete prompt/evidence and output; for time labels, chronology is additionally required |
| `epistemic_calibration` | `2 appropriate`, `1 imperfect`, `0 overconfident_or_evasive`, `NA` | Whether certainty/refusal matches the information available in that condition | Pre-adjudicated sufficiency expectation for the condition and output language |
| `claim_truth_separation` | `2 explicit`, `1 implicit`, `0 conflated`, `NA` | Whether a historical author's assertion is distinguished from modern factual truth | Historical assertion, independent truth-status evidence where available, and output span |
| `abstention_behavior` | `appropriate`, `under_abstention`, `over_abstention`, `NA` | Whether refusal is warranted without discarding answerable content | Condition-specific answerability label and evidence availability |

## Temporal violation gate

Annotators must not mark anachronism merely because a detail is absent from the Oracle. A `violation` requires all of:

1. exact output span;
2. dated proposition/term/institution;
3. reliable chronology showing it post-dates the cutoff;
4. assessment of whether the named actor could plausibly access it;
5. confidence and sources for the chronology.

If any element is missing, use `unscorable` or code the behavior under `unsupported_content`, not temporal violation.

## Condition-specific interpretation

- E0/E1: source-specific factual failure may reflect absent evidence or parametric-memory limits. Record accuracy, calibration and unsupported content separately.
- E2/E3: evidence fidelity becomes directly scorable because the verified passage is present.
- E1/E3: temporal behavior is scorable only for items with independent chronology. The current strict set contains Q017 alone.
- Correct refusal in E0/E1 is not automatically inferior to a lucky unsupported guess.

## Adjudication record

Every non-`NA` error requires an `error_span`, `evidence_reference`, short rationale, annotator identity and review level. Conflicts are not silently averaged; they enter the disagreement queue.
