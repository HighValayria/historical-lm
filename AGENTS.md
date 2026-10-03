# Repository instructions

## Purpose

This repository is an autonomous exploratory research workspace for investigating historically time-consistent language models from a digital-humanities perspective.

The initial focus is late-Qing public-health knowledge, historical knowledge boundaries, anachronism, archival bias, historical RAG, and lightweight parameter adaptation.

This stage is exploratory. Do not begin large-scale model training. Reduce uncertainty first.

## Autonomous operation

Read `PROJECT_CHARTER.md`, `.agent/PLANS.md`, `state/graph.yaml`, `state/config.yaml`, and `state/run_state.json` before substantial work.

Process tasks in topological order. Do not stop after each task to request confirmation.

When a task is complete:

1. save its artifacts;
2. write a node report;
3. update the run state;
4. append to the task journal;
5. record changed assumptions, decisions, failures, and blockers;
6. continue to the next ready task.

If a task is blocked, document the blocker and continue with another ready task.

You may create dynamic tasks when they have high expected information value and materially affect topic selection, data feasibility, evaluation design, or method selection.

## Research standards

Prefer primary papers, official project pages, original datasets, institutional libraries, archival catalogues, and official documentation.

For important claims, record source, date, source type, direct support versus inference, and uncertainty.

Never treat another model's answer as historical evidence.

Do not claim that a model represents all late-Qing people. Specify the archival population represented by the data.

Explicitly consider archival survival bias, literacy and class bias, regional bias, author and publisher bias, OCR bias, modern editorial intervention, and digitization bias.

Do not bypass paywalls, authentication, CAPTCHAs, access controls, licensing restrictions, robots policies, or bulk-download restrictions.

## Engineering rules

Use scripts for repeatable transformations and checks. Preserve raw inputs separately from processed outputs.

Do not conduct paid external model API calls unless explicitly authorized.

Do not start large model training. Small engineering probes are allowed when they directly reduce uncertainty.

Use Git commits at meaningful node boundaries. Do not rewrite Git history or delete user files.

## Completion

Continue until all reachable tasks are completed, blocked, skipped with documented justification, or the run budget is exhausted.

The final report must distinguish:

- verified findings;
- interpretations;
- unresolved questions;
- recommended directions;
- rejected directions;
- blocked directions;
- next autonomous tasks.

## Autonomous Research Automation

This repository contains a persistent 1-day / 5-day / 15-day research automation.

Before autonomous research work:

1. Read `state/automation_state.json`.
2. Run `scripts/check_schedule.py`.
3. Read the corresponding protocol under `automation/`.
4. Treat repository state as authoritative memory.

Do not repeat previously processed papers or datasets.

Do not modify `CURRENT_RESEARCH_DESIGN.md` except during a due Half-Month audit.

Do not perform large-scale training, paid API calls, access-control bypass, or unauthorized scraping.

If an individual task is blocked, record it and continue.
