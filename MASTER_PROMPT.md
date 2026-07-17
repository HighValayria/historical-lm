# First autonomous exploration run

Execute the first autonomous exploration run for this repository.

First read all governing files:

- `AGENTS.md`
- `PROJECT_CHARTER.md`
- `.agent/PLANS.md`
- `state/graph.yaml`
- `state/config.yaml`
- `state/run_state.json`

Then perform T00. Initialize any missing working directories and files, including appropriate locations for tasks, evidence, data probes, benchmarks, prototypes, node reports, logs, decisions, blockers, assumptions, and failures.

After initialization, execute all reachable nodes in topological order. Do not request confirmation between nodes.

Use independent subagents only for genuinely separable branches, especially T10, T11, and T12. The main agent must normalize their evidence and retain responsibility for synthesis.

The central decision is whether late-Qing public-health materials can support an individual-scale, evaluable digital-humanities project concerning historical knowledge boundaries, anachronism, historical RAG, and lightweight model adaptation.

Proceed from broad landscape to detail:

1. map related work and methodological precedents;
2. map archives, databases, licensing, access, OCR, metadata, and bulk-processing feasibility;
3. define concepts such as historical knowledge boundary, knowledge accessibility, archival bias, historical ignorance, factual anachronism, lexical anachronism, causal anachronism, value anachronism, and source misattribution;
4. generate multiple research questions;
5. score and select candidate directions;
6. conduct small real-world probes of data, evaluation design, and engineering feasibility;
7. synthesize findings;
8. produce a detailed report and the next autonomous task graph.

Do not begin large-scale model training. Do not use paid external model APIs. Codex-generated answers may be used only as labelled engineering probes, never as historical evidence.

For each completed node:

- create `reports/nodes/<NODE_ID>.md`;
- update the run state;
- append a compact task-journal record;
- update evidence tables;
- record decisions, assumptions, failures, and blockers;
- make a meaningful Git commit;
- immediately begin the next ready node.

If a branch is blocked, document it and continue elsewhere. If new evidence creates a high-value question, add a dynamic node with explicit dependencies, artifacts, completion criteria, and stopping criteria.

At the end, create:

- `reports/EXECUTIVE_BRIEF.md`;
- `reports/FINAL_REPORT.md`;
- a literature matrix;
- a historical source registry;
- a candidate-topic scorecard;
- a recommended direction and viable alternatives;
- a minimum viable pilot study;
- a pilot anachronism benchmark specification or dataset;
- a list of rejected or blocked directions;
- `state/NEXT_RUN_BACKLOG.yaml`.

The final chat response should be concise and point to the main repository artifacts. The full reasoning and evidence must remain in the repository.
