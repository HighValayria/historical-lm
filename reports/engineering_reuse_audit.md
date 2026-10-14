# B1 工程复用审计与最小兼容改造

日期：2026-10-14
任务：B1（Track B，第 1 次尝试）

## 结论

现有试点可复用的是“冻结输入—明确运行条件—原始输出—派生评分”这一执行骨架，不能复用为严格的时代错置 Benchmark 或真实模型基线。已在 `experiments/baselines/README.md` 实现一个不改动既有数据和脚本的兼容契约：将旧 B0/B1/B2、E0/E1/E2/E3 映射为后续 P0/P1/O0/O1/R0/R1 所需条件，并明确接入与授权边界。

本次未调用模型、未触发网络端点、未改写旧题目、原始输出或历史审计。

## 复用边界

| 组件 | 状态 | 依据与处理 |
|---|---|---|
| `scripts/research_validity_pilot/run_openai_compatible.py` | 可复用 | 默认 dry-run；非 loopback 需要 `--execute --allow-remote`；逐条 append-only 输出并在失败后停止，可作为受授权接口的执行适配器。 |
| 72 个 E0/E1/E2/E3 冻结 packet | 可复用为来源 / 认识论控制 | 其时间提示与 Oracle 因子正交，packet 有哈希；但仅一题直接涉及时间，0 题有足够独立年代证据，不能作为严格时代错置主集。 |
| 20 项 Data Feasibility 题、B0/B1/B2 packet 与 OCR/页图 | 仅保留、不可改写 | 原始输入和输出须保留；题组受单轮验证、OCR 和独立组不足限制，只能作为 Legacy 阅读与来源控制。 |
| 评分 ledger、盲核任务与分歧队列 | 需改造 | 八维评分和盲核结构可沿用；严格标签需新增年代卡、截止点、行动者可达性、独立命题组和证据竞争字段。 |
| 普通 RAG / 时间过滤 RAG | 暂不可执行 | 尚无合法冻结的目标语料、页级时间元数据和受控模型接口；先在配置层保留 R0/R1，不产生检索或生成结果。 |
| LoRA/SFT 与大规模训练资产 | 不可复用 / 不启动 | 当前阶段、算力和证据均不支持；不以工程完成度替代方法可行性。 |

## 已实现的低风险改造

扩展 `experiments/baselines/README.md` 为接口契约，明确：

1. 旧条件与未来条件的语义映射；
2. 新年代评测的最小接入字段，而不改变旧资产；
3. 未授权时只能干运行；
4. 原始响应和评分派生物必须分离；
5. R0/R1 必须分别冻结语料、许可和时间元数据。

此改造只新增文档约束，故可逆、不会触及冻结输入，也不会制造模型输出。后续 B2 才负责可验证的配置 schema 与自动测试。

## 本地验证

执行：

```powershell
python scripts/research_validity_pilot/run_openai_compatible.py --packets experiments/research_validity_pilot/factorial/prompt_packets_v2.jsonl --output experiments/research_validity_pilot/model_runs/dry_run_should_not_exist.jsonl --model DRY_RUN --condition E0 --max-packets 1
python tests/test_research_backlog.py
python tests/test_automation_scheduler.py
```

预期且已核验的约束：dry-run 选择 packet 但不创建输出文件；14 项单元测试通过且不调用模型。为使队列选择测试在自动化已领取任务时仍只测试 tie-break，测试显式隔离 persisted `running` 状态。该项验证仅检验框架和状态迁移，不能解释为模型表现。

## 失败、blocker 与后续

- B-0003（缺少可控、获授权模型接口）保持 active；本任务不试图绕过它。
- B-0005（严格年代证据题为 0）保持 active；B2 或后续 Baseline 不能绕过 A2/A3。
- B2 在 B1 完成后可推进，但其实际执行仍受上述 blocker 限制。

## 验收

- 可复用、需改造、不可复用组件均已逐项记录：通过。
- 改造具有本地、零模型调用验证：待随本轮命令输出复核；通过后方可完成 B1。
- 旧 20 题、原始输出与历史审计保持不变：通过（本次未修改这些路径）。
