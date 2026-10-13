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
