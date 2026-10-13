# Data Feasibility Pilot Experiment Protocol

## Dataset and sampling

- Unit hierarchy: archive record -> historical work -> digital version/volume -> page -> text layer -> passage -> evaluation item.
- Initial source target: at least two distinct source ecologies among missionary medicine, customs medicine, and treaty-port municipal administration.
- Initial page sample: 10-20 pages selected purposively for public-health relevance and text/layout diversity; this is a feasibility sample, not a representative corpus.
- No train/test split is planned before a sufficiently large item set exists. Trial items remain development-only.

## Phase gates

1. DFP-A: verify archive identity, access, reuse signal, stable identifiers, and downloadability.
2. DFP-B: preserve original files; extract archive OCR where supplied; render selected pages; create faithful manual checks; measure or categorize extraction errors.
3. DFP-C: create page-grounded evidence records and trial questions. Separate extraction, question writing, answer annotation, and evidence verification.
4. DFP-D: only if at least eight defensible page-grounded items exist, compare B0 direct answer, B1 time/role prompt, and B2 verified Oracle passage using the same model/configuration.
5. DFP-E: reassess period, theme, source ecology, and thesis direction from observed evidence.

## Baselines

- B0 Direct answer: measures default model behavior without source constraints.
- B1 Time/role prompt: isolates prompt-only temporal constraint.
- B2 Oracle evidence: isolates evidence-use behavior without retrieval error.
- B3 Historical RAG: excluded from this pilot unless a larger stable passage corpus emerges.

## Metrics and coding

- Data layer: acquisition success, file integrity, page traceability, OCR availability, sampled transcription error or documented qualitative defects.
- Item layer: evidence sufficiency, answerability, temporal consistency, factual accuracy, source attribution, unsupported addition, uncertainty/abstention quality, evidence fidelity.
- Open interpretations require manual review; LLM-as-judge cannot be the sole adjudicator.
- No aggregate accuracy claim is permitted from highly dependent questions derived from the same passage.

## Reproducibility

- Record URLs, access time, HTTP metadata when available, archive identifiers, filenames, byte sizes, SHA-256, commands, software versions, page mappings, and all manual edits.
- Preserve original OCR and manually checked transcription as separate immutable layers.

## Allowed claims

- Positive claims may concern technical access, traceability, observed extraction quality, and whether sampled pages can support specific item types.
- The pilot cannot claim population representativeness or historical nonexistence from corpus absence.

## Research Validity & Baseline Pilot addendum (2026-10-13)

- Preserve B0/B1/B2 as historical artifacts. The new primary design is E0/E1/E2/E3: time cutoff absent/present crossed with verified Oracle absent/present.
- E1/E3 receive the same cutoff clause; E2/E3 receive the same evidence block. Questions, model and decoding remain fixed.
- The main text factorial contains 18 items and 72 packets. Q007 is a separate image/OCR control; Q012 awaits speaker context.
- Report eight scoring dimensions separately. A temporal violation requires independent chronology and actor-access evidence; Oracle silence is not a temporal label.
- Analyze paired transitions by the 11 evidence-independence groups. Current results are descriptive; no model run exists.

