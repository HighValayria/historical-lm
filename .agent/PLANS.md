# Execution-plan protocol

For every task node, maintain the following fields:

- Node ID
- Objective
- Dependencies
- Questions to resolve
- Inputs
- Planned actions
- Expected artifacts
- Completion criteria
- Stopping criteria
- Risks
- Actual outcome
- Changed assumptions
- Follow-up tasks

Plan from broad landscape to narrow probes:

1. map the research landscape;
2. map sources and access;
3. define concepts and evaluation targets;
4. generate candidate research questions;
5. score and select candidates;
6. conduct small data, benchmark, and engineering probes;
7. synthesize evidence;
8. generate the next task graph.

Do not over-plan implementation before data and evaluation feasibility are known.

Dynamic tasks may be created when:

- uncertainty is high;
- the answer materially affects a decision;
- evidence is obtainable;
- expected value exceeds cost;
- the task has clear completion and stopping criteria.

Suggested dynamic-task priority:

`priority = impact × uncertainty × evidence_availability / estimated_cost`

Use ordinal scores from 1 to 5. Limit speculative branching.
