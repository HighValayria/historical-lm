"""Verify local identity, preserved assets and Git continuity after migration."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


def run_git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(root), *args], text=True, encoding="utf-8").strip()


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--expected-directory", default="llm-historical-anachronism")
    parser.add_argument("--expected-origin", default="https://github.com/HighValayria/llm-historical-anachronism.git")
    parser.add_argument("--allow-old-directory", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    checks: list[dict] = []

    def check(name: str, passed: bool, detail: str) -> None:
        checks.append({"check": name, "passed": bool(passed), "detail": detail})

    check("git_repository", (root / ".git").is_dir(), str(root / ".git"))
    expected_name = args.expected_directory
    directory_ok = root.name == expected_name or (args.allow_old_directory and root.name == "historical_lm_exploration_starter")
    check("directory_identity", directory_ok, root.name)
    check("readme_identity", (root / "README.md").exists() and "LLM Historical Anachronism" in (root / "README.md").read_text(encoding="utf-8"), "README title")
    check("design_v002", "Version: v002" in (root / "research_design/CURRENT.md").read_text(encoding="utf-8"), "CURRENT.md")
    check("legacy_index", (root / "legacy/late_qing/README.md").exists(), "legacy/late_qing/README.md")

    origin = run_git(root, "remote", "get-url", "origin")
    origin_ok = origin == args.expected_origin or (args.allow_old_directory and origin.endswith("/historical-lm.git"))
    check("origin_identity", origin_ok, origin)
    baseline = manifest["baseline_head"]
    ancestor = subprocess.run(["git", "-C", str(root), "merge-base", "--is-ancestor", baseline, "HEAD"]).returncode == 0
    check("history_continuity", ancestor, f"{baseline} is ancestor of HEAD")
    tags = run_git(root, "tag", "--list", manifest["protection_tag"]).splitlines()
    check("protection_tag", manifest["protection_tag"] in tags, manifest["protection_tag"])

    mismatches = []
    for record in manifest["critical_files"]:
        path = root / record["path"]
        if not path.exists() or path.stat().st_size != record["bytes"] or digest(path.read_bytes()) != record["sha256"]:
            mismatches.append(record["path"])
    check("critical_legacy_assets", not mismatches, f"{len(manifest['critical_files'])} checked; mismatches={mismatches}")

    tag_spec = manifest["original_design"]["tag_path"]
    original_bytes = subprocess.check_output(["git", "-C", str(root), "show", tag_spec])
    check("original_design_recoverable", digest(original_bytes) == manifest["original_design"]["sha256"], tag_spec)
    check("obsidian_preserved", (root / ".obsidian").is_dir(), ".obsidian local directory")

    result = {"status": "PASS" if all(c["passed"] for c in checks) else "FAIL", "root": str(root), "checks": checks}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"status": result["status"], "checks": len(checks), "failed": sum(not c["passed"] for c in checks)}, ensure_ascii=False))
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
