# 自主科研自动化说明

## Codex App Automation

仓库只使用一个 Codex App Automation：`每日自动化迭代`。它绑定
`D:\Resources\llm-historical-anachronism`，App 中实际保存的规则为每5小时、整点尝试触发。
当前 App 更新接口不接受显式 `DTSTART`/时区行，因此北京时间 `2026-10-14 09:00`
作为固定相位锚点持久化在仓库状态中。App 侧调度负责发起，仓库侧 `EXECUTION_TICK`
负责按该锚点进行迟到、重复和并发保护。

Automation Prompt 只需要求 worker 读取 `automation/MASTER_AUTOMATION_PROMPT.md`。
该文档是完整执行协议；不得另建第二个日程。

## 两层调度模型

第一层是每5小时一次的执行机会：

- 锚点：`2026-10-14T09:00:00+08:00`；
- 间隔：5小时，跨日连续滚动，不在每天零点重置；
- 策略：`SKIP_MISSED_SLOTS`，迟到超过30分钟的明显旧请求跳过；
- 每个有效槽先恢复安全的 running/checkpoint，否则领取最高优先级 ready 任务；
- 所有有界工作合计最多3项、总计最多90分钟，不要求用满；
- 同一槽最多成功一次，同一仓库最多一个活动研究写入任务。

第二层是按“上次成功时间”滚动的研究管理周期：

- Research Radar（历史键名 `daily`）：至少24小时；
- Tactical：3天；
- Synthesis：7天；
- Audit：14天。

每次 tick 并不自动重复六通道 Radar。逾期阶段在下一次有效 tick 各执行一次，不按错过天数批量补做。`scripts/check_schedule.py` 只读第二层状态，`scripts/manage_execution_tick.py` 管理第一层槽与锁。

## 执行锁、幂等与恢复

自动入口首先运行：

```powershell
python scripts/manage_execution_tick.py claim
```

若 App 能提供原定触发时间，追加 `--scheduled-at <ISO-8601>`；否则检查器以固定锚点和当前时间推断最近槽。由于当前 Automation Prompt 不保证暴露原定触发时间，仓库保护能跳过明显迟到任务，但不能百分之百识别所有 App 补发请求。

锁文件位于 `.git/research_execution.lock`，不会进入版本控制。活动锁未结束时新触发返回 `active_execution_lock`。执行中使用：

```powershell
python scripts/manage_execution_tick.py checkpoint --run-id <RUN_ID> --value "<CHECKPOINT>"
```

完成、失败或中断均必须释放锁：

```powershell
python scripts/manage_execution_tick.py finish --run-id <RUN_ID> --result success --research-task-successful true
python scripts/manage_execution_tick.py finish --run-id <RUN_ID> --result failed --checkpoint "<RECOVERY_POINT>"
```

`success` 只在计划内工作真实完成后使用。Backlog 任务仍须由既有验收逻辑确认产物；Radar/Tactical/Synthesis/Audit 仍须由 `record_automation_result.py` 验证至少一个真实交付物后才能推进各自成功时间。失败与中断保留 checkpoint，不更新科研成功时间。

## 状态分离

- `state/execution_tick_state.json`：最近有效自动槽、最近科研任务成功时间、已完成槽、当前 checkpoint 与执行锁镜像；
- `state/automation_state.json`：Radar/Tactical/Synthesis/Audit 各自成功时间和历史 run count；
- `state/research_execution_state.json`：当前研究阶段 checkpoint、开始/结束、产物和错误；
- `state/execution_history.json`：阶段生命周期的幂等事件；
- `state/research_backlog.json`：Research Backlog 任务状态。

迁移不会把旧 Daily、Five-Day、Half-Month 或现有 1/3/7/14 结果重置或冒充新成功；不会因配置变更增加任何 run count。

## 手动入口

原有 `FORCE_MODE=AUTO|DAILY|TACTICAL|SYNTHESIS|AUDIT|FULL` 继续可用，兼容别名 `FIVE_DAY→SYNTHESIS`、`HALF_MONTH→AUDIT` 保留。手动运行用 `claim --manual` 获取同一个写锁，默认 `UPDATE_SCHEDULE=false`，因此不会改变自动执行槽或周期成功时间。

## 休眠与平台边界

本仓库不会主动唤醒电脑。Codex App 或本地执行环境不可用时，该槽直接错过；恢复后只考虑当前正常槽，不为每个错过槽创建补跑。是否在系统恢复后投递旧请求由 App 平台决定；仓库侧以30分钟窗口、固定锚点、已完成槽记录和执行锁降低补跑风险。

## 本地验证

以下命令只运行调度与状态机单元测试，不启动研究、模型调用、下载或训练：

```powershell
python -m unittest discover -s tests -p "test_automation_scheduler.py" -v
python scripts/check_schedule.py --now 2026-10-14T14:00:00+08:00
python scripts/manage_research_backlog.py validate
```

全部测试可用 `python -m unittest discover -s tests -v` 运行。
