# E0/E1/E2/E3 factorial protocol

## Research purpose

This 2×2 design separates two interventions:

| Condition | Explicit historical cutoff | Verified Oracle passage |
|---|---:|---:|
| E0 | no | no |
| E1 | yes | no |
| E2 | no | yes |
| E3 | yes | yes |

The design does not assume that every item is a temporal-knowledge item. It estimates prompt/evidence behavior separately within pre-declared construct families. The current set contains only one strict temporal item, so temporal conclusions must remain case-based until a dedicated chronology-backed suite exists.

## Controlled components

- Same revised question, model identifier/revision, decoding parameters and output limit in all four cells.
- Same base system instruction in every condition.
- E1 and E3 add exactly the same cutoff clause.
- E2 and E3 add exactly the same Oracle block.
- Oracle blocks contain only bibliographic/page metadata and visually checked transcription. They exclude gold answers, normalized paraphrases, caution fields and post-hoc explanations.
- Full prompts and canonical SHA-256 values are saved before inference.
- Packet order is shuffled deterministically with seed `20261013`.

## Construct caveat

All current questions are source-specific. E0/E1 therefore often measure parametric recall, uncertainty and hallucination under absent evidence—not fair recall of an expected fact. Accuracy comparisons must be conditioned on `oracle_requirement`; a model must not be penalized for explicitly saying that a source-specific detail cannot be known without the source.

## Planned comparisons

For every scoring dimension, preserve item-level paired transitions rather than making a single weighted score:

- Time-prompt effect without evidence: E1 versus E0.
- Time-prompt effect with evidence: E3 versus E2.
- Oracle effect without time prompt: E2 versus E0.
- Oracle effect with time prompt: E3 versus E1.
- Qualitative interaction: whether the E3−E2 transition differs from E1−E0.

With only 11 evidence-independence groups, report counts and paired case transitions by group. Do not treat 18 eligible questions as 18 independent observations or claim conventional statistical significance.

## Model and decoding controls

- One exact provider/model revision per run batch.
- Default development setting: temperature 0, one sample, maximum 500 output tokens, seed `20261013` when supported.
- If stochastic robustness is later required, pre-register three repetitions at a nonzero temperature as a separate run; do not mix them with the deterministic baseline.
- Record whether the endpoint honors seeds and exposes a model revision.

## Dedicated anachronism suite gate

A future item may receive an anachronism label only when an independent chronology record establishes:

1. the proposition/term/institution and its earliest defensible availability;
2. the target cutoff;
3. the relevant historical actor and a reasoned access path;
4. the source record's coverage;
5. the exact model output span alleged to introduce post-cutoff knowledge.

Absence from one document is never sufficient. “Knowledge existed,” “this actor could access it,” “this archive recorded it,” and “the model used it” are four separate fields.

## Analysis sets

- Primary validity set: eight items across distinct evidence groups where possible.
- Reading controls: four ordinary source-comprehension items.
- Strict temporal set: currently only Q017.
- Q007 is excluded from the text-only factorial and retained for a future page-image/OCR condition. Q012 is also excluded until surrounding context identifies the speaker.

## Stopping rules

- Stop model execution if the endpoint/model revision is not identifiable, billing/authorization is unclear, or raw output cannot be saved.
- Stop temporal-effect claims if no strict temporal item is available beyond Q017.
- Stop aggregate accuracy claims if independent adjudication has not occurred.
