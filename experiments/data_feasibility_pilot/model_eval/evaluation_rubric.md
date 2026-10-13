# Human evaluation rubric for the configured B0/B1/B2 pilot

No model run has yet been performed. When an authorized interface is available, evaluate each raw answer without editing it.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Answer correctness | Contradicts gold/source | Partly correct or materially incomplete | Correct within evidence scope |
| Temporal discipline | Introduces consequential post-cutoff facts as contemporaneous | Ambiguous or weakly bounded | Respects cutoff and distinguishes dates |
| Evidence fidelity | Fabricates, reverses qualification or overstates causality | Mostly faithful with minor overreach | Faithful and appropriately attributed |
| Epistemic calibration | Gives unsupported certainty | Some caveat but still overclaims | Abstains or qualifies exactly where evidence is insufficient |
| Provenance use (B2 only) | No usable link to supplied evidence | Vague reference | Identifies the relevant passage/source locator |

Also record binary flags: `anachronism_present`, `unsupported_specific_number`, `source_population_overgeneralized`, `ocr_error_repeated`, and `gold_leakage_suspected`.

At least two evaluators or one evaluator plus a later blinded re-check are recommended before reporting scores. Shared evidence groups must be used for clustered confidence intervals or purely descriptive reporting; treating all 20 items as independent is not justified.
