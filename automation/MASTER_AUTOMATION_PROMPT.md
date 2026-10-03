# Master Automation Prompt

You are entering this repository as the daily Codex Automation worker.

Repository files are the authoritative long-term memory. Do not rely on prior chat context.

Before acting:

1. Read `AGENTS.md`.
2. Read `state/automation_state.json`.
3. Determine the run mode.

Supported modes:

- `AUTO`
- `DAILY`
- `FIVE_DAY`
- `HALF_MONTH`
- `FULL`

Default mode is `AUTO`.

`AUTO` uses `state/automation_state.json` and the actual date to decide which layers are due.

Manual modes ignore whether the selected layer is due:

- `DAILY` forces Daily only.
- `FIVE_DAY` forces Five-Day only.
- `HALF_MONTH` forces Half-Month only.
- `FULL` forces Daily, then Five-Day, then Half-Month.

4. Determine schedule-update behavior.

Supported value:

```text
UPDATE_SCHEDULE=true|false
```

Rules:

- In `AUTO`, always update the corresponding `last_*` dates and run counts after each successful due layer.
- In manual modes with `UPDATE_SCHEDULE=true`, treat the run as a formal cycle run and update the corresponding `last_*` dates and run counts after success.
- In manual modes with `UPDATE_SCHEDULE=false`, execute the work but do not change the automatic cycle dates or run counts.
- Default manual behavior is `UPDATE_SCHEDULE=false`.

5. Run:

```bash
python scripts/check_schedule.py
```

If `python` is not available on `PATH`, use the Python runtime bundled with Codex App to run the same script.
On this machine, `C:\Users\33967\AppData\Local\Programs\Python\Python312\python.exe` is a verified fallback.

For manual modes, run the checker with environment variables or equivalent CLI flags, for example:

```bash
FORCE_MODE=FIVE_DAY UPDATE_SCHEDULE=false python scripts/check_schedule.py
```

On Windows PowerShell:

```powershell
$env:FORCE_MODE = "FIVE_DAY"
$env:UPDATE_SCHEDULE = "false"
python scripts/check_schedule.py
```

6. Execute the selected layers in this fixed order:
   - Daily
   - Five-Day
   - Half-Month
7. For each selected layer, read and follow the matching protocol under `automation/`.
8. Update changed state files only after the corresponding work succeeds and only when the checker reports that the matching `update_*_state` value is `true`.
9. Commit the repository changes with a concise Git message.
10. If a remote exists and permissions are available, push the commit.
11. Do not wait for human confirmation.

Scheduling is rolling and state-based:

- Daily runs every automation entry.
- Five-Day runs when at least 5 actual days have passed since the last successful Five-Day run, or when no previous Five-Day run is recorded.
- Half-Month runs when at least 15 actual days have passed since the last successful Half-Month run, or when no previous Half-Month run is recorded.

Do not use calendar day-of-month rules.

Do not perform large-scale training, paid API calls, access-control bypass, unauthorized scraping, or bulk downloading. If a task is blocked, record it and continue with other due work.
