# Data Feasibility Pilot benchmark trial

This is a **20-item trial set**, not a validated benchmark. Items are grouped by underlying evidence; therefore the nominal item count overstates statistical independence.

## Types

- `C1_source_comprehension`: answerable factual reading of the supplied evidence;
- `C2_attribution`: preserves who asserted a claim and at what evidential level;
- `C3_temporal_boundary` / `C3_cross_source_boundary`: distinguishes observation date, publication date and archival population;
- `C4_evidence_fidelity`: tests qualifications, OCR/image disagreement and causal overstatement;
- `C5_insufficiency_abstention`: requires refusal to infer what the source cannot establish.

All items cite one or more stable `passage_id` values in `evidence_bank.jsonl`. Answers were constructed from visually checked passages, but no independent historian has adjudicated them. Do not report model accuracy from this set as a general estimate of historical reasoning ability.
