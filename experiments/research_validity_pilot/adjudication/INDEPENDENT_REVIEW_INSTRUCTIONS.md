# Independent review instructions

## Status

The files in this directory prepare a second review; **no independent review has yet occurred**. The existing transcription, gold answers and audit were all produced within the same Codex project lineage. Re-running Codex or asking the same model to agree with itself does not satisfy independence.

## Transcription review

Give the reviewer only `blind_transcription_tasks.jsonl` and access to the listed page images. The reviewer should transcribe the target excerpt directly from the page, mark uncertain spans, and record identity/time. Do not expose `blind_transcription_key.jsonl` until the independent pass is locked.

After locking, compare the independent transcription with the existing key. Escalate every disagreement involving:

- numbers and dates;
- personal or place names;
- medical terminology;
- negation or modal language;
- quotation boundaries;
- speaker/author identity;
- claims about publication versus observation time.

## Item/gold review

Give the reviewer only `blind_item_tasks.jsonl`. The reviewer should produce an answer from the evidence, judge evidence sufficiency, propose the primary construct, and list acceptable alternatives. Do not expose `blind_item_key.jsonl` until answers are frozen.

Disagreement resolution must record both versions, the evidence used, the final decision, adjudicator identity and whether the adjudicator has relevant historical expertise.

## Independence levels

- `L0`: same model/project self-check; useful only for mechanical consistency.
- `L1`: different model with no shared generated rationale; still not human historical review.
- `L2`: independent human reading with hidden prior labels.
- `L3`: independent reviewer with relevant historical/domain expertise.

Formal benchmark publication should require at least L2 for every item and L3 for chronology, first-occurrence, causal-history and contested medical claims.
