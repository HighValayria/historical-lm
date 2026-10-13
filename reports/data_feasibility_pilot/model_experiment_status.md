# Model experiment status

## Outcome

B0/B1/B2 were **not executed**. No controlled local model command (`ollama`, `llama-server`, `lmstudio` or `llamafile`) and no configured authorized model credential were detected. Running an unrecorded interactive answer through the current assistant would not provide a fixed model revision, reproducible parameters or clean raw-output provenance, so it was not substituted for an experiment.

## Prepared artifacts

- `experiment_config.json` fixes the three conditions, default generation parameters and required run metadata.
- `prompt_packets.jsonl` contains 60 immutable packets: 20 items × B0/B1/B2, each with SHA-256.
- `human_evaluation_template.csv` has one row per packet and fields for correctness, temporal discipline, evidence fidelity, calibration, provenance use and failure flags.
- `evaluation_rubric.md` defines 0–2 coding anchors and warns against treating dependent items as independent.
- `scripts/data_feasibility_pilot/prepare_model_eval.py` reproduces the packet and evaluation files offline.

## Gate judgment

The data gate is provisionally met for a small descriptive run: 20 trial items, 12 verified evidence units and 11 evidence groups. The execution gate is blocked by the absence of a controlled model interface. Even after that interface is supplied, scores must remain provisional until a second human/historical review of the item set is complete.

No model accuracy, anachronism rate, evidence-use improvement or failure case can therefore be reported from this pilot.
