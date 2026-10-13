# Trial benchmark report

## Result

The pilot produced 12 page-grounded evidence units and 20 development items. The items form 11 evidence-independence groups, so 20 is the nominal question count rather than 20 independent historical observations.

| Item family in the implemented schema | Count | What it tests |
|---|---:|---|
| `C1_source_comprehension` | 8 | Accurate reading of a supplied historical statement or statistic |
| `C2_attribution` | 2 | Preservation of the speaker/author and claim status |
| `C3_temporal_boundary` / `C3_cross_source_boundary` | 2 | Observation versus publication date; archival-population boundary |
| `C4_evidence_fidelity` | 3 | Qualifications, image/OCR conflict and causal overstatement |
| `C5_insufficiency_abstention` | 5 | Refusal to infer precise numbers, first occurrence or validated causality from insufficient evidence |

The naming differs slightly from the migration brief's C1–C5 labels because the implemented schema separates the failure mode more explicitly. Every item records its concrete type, cutoff date, gold answer, evidence passage IDs, required attribution, forbidden inference, independence group and adjudication status.

## Evidence chain

`source_manifest.jsonl` → `selected_pages.jsonl` → `verified_passages.jsonl` / `evidence_bank.jsonl` → `benchmark_items.jsonl`.

All 20 items resolve to an existing passage; every passage resolves to one of 14 selected pages; every selected page resolves to a local OCR file, a local page image and a stable archive locator. Automated referential-integrity checks passed.

## Representative cases

1. A table OCR changes “5,807” dressing visits to “6,807.” The item requires the page image to win over OCR.
2. A 1874 Peking report calls sanitary conditions poor but explicitly rejects the simple inference that the city is therefore unhealthy. The item tests whether a model preserves this qualification rather than importing a modern conclusion.
3. An 1890 author asserts that impure vaccination material transmitted other diseases. Paired items distinguish faithful attribution of the historical assertion from treating it as validated epidemiology.
4. A conference speaker claims scarlet fever was introduced by a foreign child about eight years earlier. The abstention item rejects using a single statement as proof of the disease's true first arrival.
5. A source published in 1884 recounts 1872–1873 Tientsin water conditions. The temporal item requires the model not to relabel the observation as an 1884 condition.

## Failed or rejected item patterns

- Exact mortality questions based on phrases such as “thousands of lives”: rejected as answerable numeric questions and converted to insufficiency tests.
- “When did X first appear in China?” from a single non-attestation or conference recollection: rejected without independent historical scholarship.
- Whole-society claims from customs/missionary English sources: rejected and replaced by an archival-population boundary item.
- Items that differ only by paraphrasing the same sentence: retained only when they test meaningfully different behaviors, and grouped under the same independence label.

## Validity status

The set demonstrates that real pages can support evidence-constrained evaluation. It is not yet a formal benchmark because it lacks independent historical adjudication, bilingual/Chinese-source coverage, broad topic/region balance, contamination analysis and a held-out test split. Results from it should be descriptive case analysis, not a population-level model ranking.
