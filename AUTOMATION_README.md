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

## Manual inspection

For future review, check these first:

```text
reports/half_month/
research_design/CURRENT_RESEARCH_DESIGN.md
research_design/DESIGN_CHANGELOG.md
```
