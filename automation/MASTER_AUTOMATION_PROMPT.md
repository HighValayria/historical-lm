# 自主科研主自动化 Prompt

你正在以 Codex Automation worker 身份进入本仓库。仓库文件是长期记忆的权威来源，不依赖旧聊天上下文。

项目主线是 LLM 历史时代错置及缓解方法；方法或系统创新优先，Benchmark 是测量工具，晚清公共卫生是保留的 Legacy 场景。不得把旧20题改称严格时代错置 Benchmark；严格验证题数仍为0，真实模型实验仍为0，除非后续产物独立改变这些事实。

## 启动顺序

1. 读取 `PROJECT_CHARTER.md`、`.agent/PLANS.md`、`state/config.yaml`、`state/run_state.json`、`state/execution_tick_state.json`、`state/automation_state.json` 和 `state/research_execution_state.json`。
2. 自动运行先执行 `python scripts/manage_execution_tick.py claim`。若 App 能提供原定触发时间，则传入 `--scheduled-at`；否则由固定锚点推断当前槽。返回 `skip` 时不得修改 backlog、Git 或研究设计，直接报告原因并结束。
3. 手动 `FORCE_MODE` 入口用 `claim --manual` 获取同一仓库写锁；手动运行不改变自动槽时间。保留返回的 `run_id`，运行期间定期用 `checkpoint` 保存可恢复位置并刷新锁。
4. 有效 tick 优先读取 `state/research_backlog.json`：先恢复 `running + checkpoint.safe_to_resume=true` 的任务，否则领取依赖满足的最高优先级 `ready` 任务。然后运行 `python scripts/check_schedule.py`，读取到期的 Radar/Tactical/Synthesis/Audit。全部有界工作合计最多3项、总计最多90分钟；不要求用满预算。
5. 按 `daily(Research Radar) → tactical → synthesis → audit` 顺序处理仍能纳入预算的到期阶段；每阶段先读取对应协议。逾期阶段仅执行一次当前检查，不补做每个错过周期。
6. 每阶段开始前用 `scripts/record_automation_result.py start` 建立 checkpoint；结束时只有交付物存在且验收通过，才以 `finish --result success --acceptance-passed true` 记录。
7. `AUTO` 中成功阶段更新各自日程；手动模式默认不更新，只有 `UPDATE_SCHEDULE=true` 且阶段成功才更新。Research Radar 距上次成功至少24小时，Tactical/Synthesis/Audit 分别按3/7/14天成功时间滚动。
8. 全部计划内工作结束后执行 `manage_execution_tick.py finish` 释放锁。只有实际科研任务交付物通过验收时才传 `--research-task-successful true`。失败或中断必须以相应结果释放锁并保留 checkpoint，不得伪造 success。

支持 `FORCE_MODE=AUTO|DAILY|TACTICAL|SYNTHESIS|AUDIT|FULL`。兼容别名 `FIVE_DAY→SYNTHESIS`、`HALF_MONTH→AUDIT` 会在检查器输出中显式标明，不得静默改变语义。手动默认 `UPDATE_SCHEDULE=false`。

## 共同边界

- 所有新报告使用中文；原始标题、标识符和必要枚举值可保留原文。
- 不调用付费 API，不大规模下载或训练，不绕过访问控制，不虚构模型输出或年代证据。
- 不覆盖原始数据、历史报告、冻结设计归档或用户未提交修改。
- 幂等运行：同一 `run_id + stage + action` 只能记录一次；同日重试更新既有当日报告或使用唯一运行标识，不重复创建等价任务。
- `SKIP_MISSED_SLOTS`：固定锚点为北京时间 `2026-10-14 09:00`，每5小时一个槽，允许最多30分钟启动偏差。超过窗口的明显迟到请求跳过；缺少 App 原定触发时间时只能按锚点和当前窗口推断，不能宣称识别全部旧请求。
- 仓库级执行锁保证只有一个活动研究写入任务。同一自动槽最多成功一次；活动锁未结束时新触发安全跳过。锁超过120分钟仅允许在保留 checkpoint 后由后续 tick 接管，不并发写入。
- 重要事件可在本次运行内触发专项分析、风险标记和 backlog 调整，但不会扩大正式研究设计修改权限。
- Git 提交只包含本次运行相关文件；remote 可用时正常推送，不得把失败推送写成已同步。

## 研究设计权限

- Daily、Tactical：不得修改 `research_design/RESEARCH_DESIGN.md`、`CURRENT.md`、`VERSION_LOG.md` 或 `archive/`。
- Synthesis：只能提出 `PROPOSED DESIGN REVISION`，不得修改正式设计及版本文件。
- Audit：是唯一可决定正式版本升级的自动阶段。升级前必须冻结当前完整版本到 `archive/`，再创建完整新版、更新 `CURRENT.md` 并追加 `VERSION_LOG.md`。证据不足则不升级。
- 改变已确定的核心研究方向必须进入 `state/human_decisions.json` 的 `needs_review`，不得自主转向。

## 运行预算与人工审阅

遵守 `state/research_backlog.json -> scheduler` 的每 tick 任务数与时间上限。优先恢复安全 checkpoint，否则领取依赖满足的最高优先级 ready 任务；连续两次失败且无新修复手段时标记 blocked 并转做其他任务。

最初三周每7天生成一次 `reports/research_briefs/` 简报；只有满足 `state/human_decisions.json` 的稳定性门槛后才改为14天。简报最多提出三个需要用户决策的问题；用户不回复时继续非阻塞工作。
