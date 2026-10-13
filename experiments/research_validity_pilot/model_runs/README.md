# Model-run status and execution guide

Status: **configured, not executed**.

On 2026-10-13 the environment check found no `ollama`, `llama-server`, `lmstudio` or `llamafile` command and no matching OpenAI/Azure/Anthropic/Ollama/LM Studio credential variable names. No paid or unknown-quota endpoint was called. Consequently this directory contains an empty scoring template, not model scores.

The runner defaults to a dry run and a loopback endpoint. A real run requires an exact authorized model identifier and `--execute`:

```powershell
python scripts/research_validity_pilot/run_openai_compatible.py `
  --packets experiments/research_validity_pilot/factorial/prompt_packets_v2.jsonl `
  --output experiments/research_validity_pilot/model_runs/raw_responses.jsonl `
  --model EXACT_MODEL_ID `
  --base-url http://127.0.0.1:11434/v1 `
  --temperature 0 --max-tokens 500 --execute
```

For a remote endpoint, authorization and quota must first be confirmed; add `--allow-remote` and name the environment variable holding the key with `--api-key-env`. The script reads but never changes that variable. Completed packets are skipped on rerun, each response is flushed to append-only JSONL, and execution stops after the first failure so the run can be safely resumed.

Dry-run validation selected four packets and performed zero requests. No `dry_run_should_not_exist.jsonl` file was created.
