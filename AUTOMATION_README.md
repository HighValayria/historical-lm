# Automation README

## Initial setup

1. Open Codex App.
2. Open this repository.
3. Create one Automation that runs every day at 09:00.
4. Use this Automation prompt:

```text
读取 automation/MASTER_AUTOMATION_PROMPT.md，
按照其中定义的滚动1天—5天—15天周期，
继续本项目的无人研究任务。
以仓库状态为准，不等待人工确认。
```

## Runtime requirement

This repository is designed for Codex App Scheduled Automation. It does not require a separate OpenAI API automation pipeline.

The scheduled environment should expose a `python` command for `python scripts/check_schedule.py`. If `python` is not on `PATH`, use the Python runtime bundled with Codex App to run the same script.

On this machine, the migration was also verified with:

```text
C:\Users\33967\AppData\Local\Programs\Python\Python312\python.exe
```

## Recovery

If a scheduled run is missed, the next run uses `last_five_day` and `last_half_month` in `state/automation_state.json` to decide whether Five-Day or Half-Month work should be caught up.

## Daily Research Radar

Daily paper discovery tracks work that is new to this repository, not only papers published in the last day.

All generated Daily, Five-Day, and Half-Month research reports should be written in Chinese. Original paper titles, identifiers, and paths may remain unchanged.

The system distinguishes:

- `newly_published`: recent work that was not previously registered;
- `newly_discovered`: older relevant work first found by this system now;
- `existing_paper_update`: new information about a paper already in `state/seen_papers.json` or `evidence/literature_master.csv`.

This lets the early automation phase fill historical literature gaps before naturally shifting toward monitoring genuinely recent research.

## Manual runs

Manual runs are available through:

```text
automation/manual/RUN_DAILY.md
automation/manual/RUN_FIVE_DAY.md
automation/manual/RUN_HALF_MONTH.md
automation/manual/RUN_FULL.md
```

Each file gives a minimal instruction for forcing one layer, or all layers, without waiting for the normal rolling schedule.

Manual runs default to:

```text
UPDATE_SCHEDULE=false
```

That means the work is executed, but the automatic `last_*` cycle dates and run counts are not changed. Set `UPDATE_SCHEDULE=true` only when the manual run should count as the official cycle run.

## Manual inspection

For future review, check these first:

```text
reports/half_month/
research_design/CURRENT_RESEARCH_DESIGN.md
research_design/DESIGN_CHANGELOG.md
```
