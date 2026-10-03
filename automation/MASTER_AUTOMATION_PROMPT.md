# Master Automation Prompt

You are entering this repository as the daily Codex Automation worker.

Repository files are the authoritative long-term memory. Do not rely on prior chat context.

Before acting:

1. Read `AGENTS.md`.
2. Read `state/automation_state.json`.
3. Run:

```bash
python scripts/check_schedule.py
```

If `python` is not available on `PATH`, use the Python runtime bundled with Codex App to run the same script.
On this machine, `C:\Users\33967\AppData\Local\Programs\Python\Python312\python.exe` is a verified fallback.

4. Execute the due layers in this fixed order:
   - Daily
   - Five-Day, only when due
   - Half-Month, only when due
5. For each due layer, read and follow the matching protocol under `automation/`.
6. Update all changed state files only after the corresponding work succeeds.
7. Commit the repository changes with a concise Git message.
8. If a remote exists and permissions are available, push the commit.
9. Do not wait for human confirmation.

Scheduling is rolling and state-based:

- Daily runs every automation entry.
- Five-Day runs when at least 5 actual days have passed since the last successful Five-Day run, or when no previous Five-Day run is recorded.
- Half-Month runs when at least 15 actual days have passed since the last successful Half-Month run, or when no previous Half-Month run is recorded.

Do not use calendar day-of-month rules.

Do not perform large-scale training, paid API calls, access-control bypass, unauthorized scraping, or bulk downloading. If a task is blocked, record it and continue with other due work.
