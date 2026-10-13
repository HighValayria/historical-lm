# 进度记录

## 2026-07-17

第一轮探索已经完成。核心产物包括文献矩阵、史料注册表、概念地图、候选题评分表、推荐方向、访问探针、OCR/元数据探针、benchmark 规范、12 条试点题目、本地工程探针、执行简报、最终报告和下一轮任务图。

## 能力使用审计

本轮使用了研究写作编排、文献综述、证据驱动写作、实验/评测规划和验证约束。所有完成声明均经过文件存在性、JSON/JSONL 解析或脚本复跑验证。

## 2026-10-13 Data Feasibility Pilot

- Stage: S3 experiments, beginning with source-access and evidence gates.
- Active packet: `plan/task-packets/DATA_FEASIBILITY_PILOT.md`.
- Objective: obtain and verify a small set of real primary-source pages before any model comparison.
- Current gate: DFP-A active; DFP-D blocked until page-grounded items exist.

### Completion update

- DFP-A complete: downloaded two explicitly public-domain source versions and excluded one rights-unclear municipal report.
- DFP-B complete for a purposive feasibility sample: 14 pages, 47,479 OCR characters and 12 short passages checked against page images; micro character divergence on the checked snippets was 1.35%, but a table value changed from 5,807 to 6,807 in OCR.
- DFP-C complete as a development artifact: 20 page-grounded trial items in 11 evidence-independence groups.
- DFP-D configured only: 60 B0/B1/B2 prompt packets and a human rubric were generated; no model outputs or scores exist because no controlled local/authorized interface was present.
- DFP-E complete: recommend a narrower, institution- and source-bounded benchmark/behavior study before Historical RAG or model adaptation.

## 2026-10-13 Research Validity & Baseline Pilot

- Stage: S3 experiment redesign plus S5 validity review.
- Active packet: `plan/task-packets/RESEARCH_VALIDITY_BASELINE_PILOT.md`.
- Inputs are frozen at the Data Feasibility Pilot state (`b06656f`); the original 20 items and B0/B1/B2 packets will not be overwritten.
- Current gates: item construct audit, factorial-prompt validity, adjudication design, then controlled-interface check. Model execution is conditional rather than assumed.

### Completion update

- Audited 20/20 items: 10 directly usable for source/epistemic research, 2 need revision, 7 are controls and 1 is unsuitable for the text-only main experiment.
- Only Q017 directly tests a historical time/knowledge-boundary distinction; no current item has enough independent chronology to label post-cutoff knowledge intrusion.
- Generated and verified 72 E0/E1/E2/E3 packets for 18 eligible items; Q007 and Q012 are excluded with explicit reasons.
- Prepared 12 blind passage tasks, 20 blind item tasks, a disagreement queue and eight-dimensional scoring ledger. Independent reviews completed: 0.
- Added a resumable OpenAI-compatible runner. No controlled local/authorized interface was detected; real model outputs remain 0.
- Direction decision: source fidelity and epistemic calibration is the evidence-supported primary path; chronology-backed anachronism is a small extension; joint modeling is conditional on observed failures.

### Capability-use audit

- Required and used: `using-research-writing` routed the task; `paper-orchestration` produced the task packet, progress record, spec/quality reviews and traceability updates; `experiment-results-planning` enforced construct-to-metric separation and the 2×2 design; `verification` required rerunnable structural checks before completion claims.
- Inputs actually used: frozen 20 items, 12 evidence records/verified passages, 14 page records, prior 60 B0/B1/B2 packets/rubric, prior report and state files.
- Intentionally unused: literature search, new archive downloads, document-generation and visualization skills; this task required internal validity auditing and no new evidence acquisition or plot was justified.
- Artifacts: audit/revision, 72 hashed packets, annotation/scoring guides, blind-review packets, chronology-gap registry, inference adapter, status and direction/final reports.
- Validation: Python compilation passed; 18 automated invariant checks passed; dry run selected four packets without network requests or output creation.
- Remaining risks: independent review is absent, strict temporal construct is underrepresented, source ecology remains narrow, and no real model behavior has been observed.

## 2026-10-13 Anachronism Repository Migration

- Stage: S0 scope reset plus repository/infrastructure migration.
- Active packet: `plan/task-packets/ANACHRONISM_REPOSITORY_MIGRATION.md`.
- Confirmed scope: computer-science master's thesis, direction A as the primary scientific problem, method innovation as the intended contribution, and late-Qing public health as a preserved legacy scenario rather than the project boundary.
- Preflight facts: local `main` starts at `1a3119a` and is 27 commits ahead of `origin/main`; GitHub repository is `HighValayria/historical-lm`, default branch `main`, and the authenticated account has admin/push permission; target GitHub name and target local directory are both currently absent.
- Safety gate: protect the pre-migration commit with a tag, preserve/ignore machine-local Obsidian state, push the pre-migration history, then make research-direction and infrastructure commits before attempting the final directory rename.

### Execution status

- Research direction commit: `b0dc3dc`.
- Migration safeguards commit: `6aa25c4`.
- GitHub: original repository renamed in place to `HighValayria/llm-historical-anachronism`; origin, description and topics updated; `main` pushed.
- Local path: rename attempted and rejected because the active Codex process holds the directory. No duplicate checkout was created. B-0006 and `scripts/complete_local_path_migration.ps1` record the exact post-close action.
- Persistent automation: found one paused cron automation named“每日自动化迭代”; it still targets the old saved project/path and must remain paused until the new local path is added and retargeted.

### Capability-use audit

- Required skills: using-research-writing, brainstorming-research, paper-orchestration, verification.
- Skills actually used: all four. The user's migration specification supplied and explicitly confirmed the thesis type, field, main topic, contribution goal and candidate methods, so brainstorming produced a recorded scope decision without reopening settled questions.
- Inputs consumed: Git status/history/remotes/worktree/config, authenticated GitHub repository metadata, README/charter/design/version files, automation protocols and binding, active state/backlog, both pilot reports/manifests and critical hashes.
- Inputs not used and why: no new web literature or historical sources were collected because this was an identity/structure migration; no model interface or training route was invoked because no method experiment was authorized by evidence.
- Artifacts produced: v002 design, active research structure, Legacy indexes, new backlog/graph/config, GitHub rename and metadata, protection tag, migration manifest/verifier, guarded local rename script, reviews, node/final reports.
- Verification run: both existing pilot verifiers pass; repository migration verifier passes in pre-rename mode; JSON/YAML parse and Python compilation pass; GitHub API and `ls-remote` verify the new repository independently of redirects.
- Remaining risk: B-0006 prevents the final local directory and Codex automation binding from satisfying acceptance criteria in the active session. M1/M2/M3 still have no experimental result.
