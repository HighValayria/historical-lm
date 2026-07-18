import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "benchmarks" / "pilot" / "schema.json"
SOURCES_PATH = ROOT / "benchmarks" / "pilot" / "source_records.jsonl"
ITEMS_PATH = ROOT / "benchmarks" / "pilot" / "pilot_items.jsonl"
OUT_JSON = ROOT / "prototypes" / "min_engineering_probe" / "probe_results.json"
OUT_MD = ROOT / "prototypes" / "min_engineering_probe" / "probe_summary.md"


TOKEN_RE = re.compile(r"[A-Za-z0-9_]+")
PASSAGE_REQUIRED = {
    "source_grounded_factual",
    "lexical_anachronism",
    "causal_anachronism",
    "value_anachronism",
}


def load_jsonl(path):
    rows = []
    with path.open("r", encoding="utf-8-sig") as handle:
        for line_no, line in enumerate(handle, start=1):
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            row["_line_no"] = line_no
            rows.append(row)
    return rows


def tokens(text):
    return Counter(t.lower() for t in TOKEN_RE.findall(text or ""))


def source_text(source):
    parts = [
        source.get("source_id", ""),
        source.get("source_family", ""),
        source.get("record_type", ""),
        source.get("title", ""),
        source.get("date_signal", ""),
        source.get("use_in_pilot", ""),
        source.get("limitations", ""),
    ]
    return " ".join(parts)


def score_overlap(query_counts, source_counts):
    if not query_counts or not source_counts:
        return 0
    return sum(min(count, source_counts.get(tok, 0)) for tok, count in query_counts.items())


def main():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    sources = load_jsonl(SOURCES_PATH)
    items = load_jsonl(ITEMS_PATH)

    required = set(schema["required_fields"])
    allowed_families = set(schema["allowed_families"])
    allowed_evidence = set(schema["allowed_evidence_status"])
    allowed_policies = set(schema["allowed_answer_policies"])
    allowed_labels = set(schema["allowed_anachronism_labels"])

    errors = []
    source_ids = {s["source_id"] for s in sources}
    source_index = [(s, tokens(source_text(s))) for s in sources]
    item_results = []

    for item in items:
        item_id = item.get("item_id", f"line-{item.get('_line_no')}")
        missing = sorted(required - set(item.keys()))
        if missing:
            errors.append({"item_id": item_id, "error": "missing_fields", "fields": missing})
        if item.get("family") not in allowed_families:
            errors.append({"item_id": item_id, "error": "invalid_family", "value": item.get("family")})
        if item.get("evidence_status") not in allowed_evidence:
            errors.append({"item_id": item_id, "error": "invalid_evidence_status", "value": item.get("evidence_status")})
        if item.get("expected_answer_policy") not in allowed_policies:
            errors.append({"item_id": item_id, "error": "invalid_answer_policy", "value": item.get("expected_answer_policy")})
        for label in item.get("anachronism_labels", []):
            if label not in allowed_labels:
                errors.append({"item_id": item_id, "error": "invalid_label", "value": label})
        for sid in item.get("source_ids", []):
            if sid not in source_ids:
                errors.append({"item_id": item_id, "error": "unknown_source_id", "value": sid})

        query = " ".join([
            item.get("question", ""),
            item.get("source_population", ""),
            " ".join(item.get("source_ids", [])),
            " ".join(item.get("anachronism_labels", [])),
        ])
        q_counts = tokens(query)
        ranked = []
        for source, s_counts in source_index:
            overlap = score_overlap(q_counts, s_counts)
            if overlap > 0:
                ranked.append({
                    "source_id": source["source_id"],
                    "source_family": source["source_family"],
                    "overlap": overlap,
                })
        ranked.sort(key=lambda r: (-r["overlap"], r["source_id"]))

        evidence_status = item.get("evidence_status")
        family = item.get("family")
        requires_passage = family in PASSAGE_REQUIRED
        scoring_ready = evidence_status != "needs_source_excerpt" and (
            not requires_passage or evidence_status == "source_passage_verified"
        )
        readiness_reason = "ready_for_policy_or_metadata_scoring" if scoring_ready else "requires_verified_source_passage"

        item_results.append({
            "item_id": item_id,
            "family": family,
            "evidence_status": evidence_status,
            "expected_answer_policy": item.get("expected_answer_policy"),
            "scoring_ready": scoring_ready,
            "readiness_reason": readiness_reason,
            "top_retrieval_candidates": ranked[:3],
        })

    summary = {
        "schema": str(SCHEMA_PATH.relative_to(ROOT)),
        "source_count": len(sources),
        "item_count": len(items),
        "error_count": len(errors),
        "errors": errors,
        "scoring_ready_count": sum(1 for r in item_results if r["scoring_ready"]),
        "requires_passage_count": sum(1 for r in item_results if not r["scoring_ready"]),
        "items": item_results,
    }

    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# 最小工程探针摘要",
        "",
        f"- 来源记录：{summary['source_count']}",
        f"- 试点题目：{summary['item_count']}",
        f"- 校验错误：{summary['error_count']}",
        f"- 当前可评分题目：{summary['scoring_ready_count']}",
        f"- 需要真实史料段落的题目：{summary['requires_passage_count']}",
        "",
        "## 题目就绪情况",
        "",
        "| 题目 | 类型 | 证据状态 | 是否可评分 | 主要候选来源 |",
        "|---|---|---|---:|---|",
    ]
    for result in item_results:
        candidates = ", ".join(c["source_id"] for c in result["top_retrieval_candidates"]) or "none"
        lines.append(
            f"| {result['item_id']} | {result['family']} | {result['evidence_status']} | "
            f"{str(result['scoring_ready']).lower()} | {candidates} |"
        )
    if errors:
        lines.extend(["", "## 校验错误", ""])
        for error in errors:
            lines.append(f"- `{error}`")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "source_count": summary["source_count"],
        "item_count": summary["item_count"],
        "error_count": summary["error_count"],
        "scoring_ready_count": summary["scoring_ready_count"],
        "requires_passage_count": summary["requires_passage_count"],
        "output": str(OUT_JSON.relative_to(ROOT)),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
