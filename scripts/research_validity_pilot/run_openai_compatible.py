"""Run frozen RVP packets through an explicitly authorized OpenAI-compatible endpoint.

Dry-run is the default.  The script never discovers or rewrites credentials and
requires an explicit flag before contacting a non-loopback endpoint.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def is_loopback(url: str) -> bool:
    host = (urllib.parse.urlparse(url).hostname or "").lower()
    return host in {"127.0.0.1", "localhost", "::1"}


def append_record(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--packets", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--model", required=True, help="Exact model identifier reported to the endpoint")
    parser.add_argument("--base-url", default="http://127.0.0.1:11434/v1")
    parser.add_argument("--api-key-env", default="OPENAI_API_KEY")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--max-tokens", type=int, default=800)
    parser.add_argument("--timeout", type=float, default=120.0)
    parser.add_argument("--condition", action="append", choices=["E0", "E1", "E2", "E3"])
    parser.add_argument("--item-id", action="append")
    parser.add_argument("--max-packets", type=int)
    parser.add_argument("--execute", action="store_true", help="Actually send requests; omission is a dry run")
    parser.add_argument("--allow-remote", action="store_true", help="Acknowledge an explicitly authorized remote endpoint")
    args = parser.parse_args()

    base_url = args.base_url.rstrip("/")
    if args.execute and not is_loopback(base_url) and not args.allow_remote:
        raise SystemExit("Remote execution requires --allow-remote and explicit authorization.")

    packets = read_jsonl(args.packets)
    if args.condition:
        packets = [p for p in packets if p["condition"] in set(args.condition)]
    if args.item_id:
        packets = [p for p in packets if p["item_id"] in set(args.item_id)]
    if args.max_packets is not None:
        packets = packets[: args.max_packets]

    completed: set[str] = set()
    if args.output.exists():
        for row in read_jsonl(args.output):
            if row.get("status") == "completed":
                completed.add(row["packet_id"])
    pending = [p for p in packets if p["packet_id"] not in completed]
    print(json.dumps({"selected": len(packets), "already_completed": len(packets) - len(pending), "pending": len(pending), "execute": args.execute}, ensure_ascii=False))
    if not args.execute:
        return

    api_key = os.environ.get(args.api_key_env, "")
    if not is_loopback(base_url) and not api_key:
        raise SystemExit(f"Remote endpoint requires a key in environment variable {args.api_key_env}.")

    endpoint = base_url + "/chat/completions"
    for packet in pending:
        request_body = {
            "model": args.model,
            "messages": [
                {"role": "system", "content": packet["prompt"]["system"]},
                {"role": "user", "content": packet["prompt"]["user"]},
            ],
            "temperature": args.temperature,
            "max_tokens": args.max_tokens,
        }
        request_hash = hashlib.sha256(
            json.dumps(request_body, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ).hexdigest()
        headers = {"Content-Type": "application/json"}
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"
        started = time.monotonic()
        record = {
            "packet_id": packet["packet_id"],
            "item_id": packet["item_id"],
            "condition": packet["condition"],
            "prompt_sha256": packet["prompt_sha256"],
            "request_sha256": request_hash,
            "endpoint": base_url,
            "model_requested": args.model,
            "temperature": args.temperature,
            "max_tokens": args.max_tokens,
            "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        }
        try:
            req = urllib.request.Request(
                endpoint,
                data=json.dumps(request_body, ensure_ascii=False).encode("utf-8"),
                headers=headers,
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=args.timeout) as response:
                raw = response.read().decode("utf-8")
            payload = json.loads(raw)
            record.update(
                {
                    "status": "completed",
                    "model_reported": payload.get("model"),
                    "system_fingerprint": payload.get("system_fingerprint"),
                    "output_text": payload["choices"][0]["message"]["content"],
                    "finish_reason": payload["choices"][0].get("finish_reason"),
                    "usage": payload.get("usage"),
                    "raw_response": payload,
                }
            )
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, KeyError, ValueError) as exc:
            record.update({"status": "failed", "error_type": type(exc).__name__, "error": str(exc)})
        record["elapsed_seconds"] = round(time.monotonic() - started, 3)
        append_record(args.output, record)
        print(json.dumps({"packet_id": packet["packet_id"], "status": record["status"]}, ensure_ascii=False))
        if record["status"] != "completed":
            print("Stopped after failure; rerun resumes completed packets.", file=sys.stderr)
            break


if __name__ == "__main__":
    main()
