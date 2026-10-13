# 自主科研自动化说明

## Codex App 每日 Automation

仓库内部只需要一个每天运行的 Codex App Automation。建议保留既有时区与每日触发时间，Prompt 更新为：

```text
打开仓库后读取 automation/MASTER_AUTOMATION_PROMPT.md，按仓库状态执行
Daily Execution + 3-Day Tactical Review + 7-Day Research Synthesis +
14-Day Strategic Audit。以 state/ 为权威记忆，不等待逐项确认。
```

本次已通过 Codex App 原位更新既有“每日自动化迭代”，没有创建重复日程。它保持每天09:00、`Asia/Shanghai`项目环境，状态为`ACTIVE`，项目与工作目录均指向`D:\Resources\llm-historical-anachronism`。如未来重新导入仓库或删除Automation，再使用上文Prompt恢复。

## 调度模型

`python scripts/check_schedule.py` 只读 `state/automation_state.json` 并输出运行计划：

- Daily：每次入口都运行；
- Tactical：距离上次成功满3天；
- Synthesis：距离上次成功满7天；
- Audit：距离上次成功满14天。

到期顺序固定为 Daily → Tactical → Synthesis → Audit。迁移锚点为 `2026-10-13T00:00:00+08:00`；新阶段首次分别不早于10月16日、20日、27日。旧 Five-Day/Half-Month 的日期和报告完整保留，但不会冒充新阶段成功。漏跑后每阶段只运行一次当前到期工作，不逐日追赶。

只有交付物存在且验收成功时，`scripts/record_automation_result.py` 才能更新该阶段的 `last_successful`。失败、中断或手动 `UPDATE_SCHEDULE=false` 都不推进周期。相同 `run_id + stage + action` 的重试是幂等 no-op。

## Research Backlog

权威执行队列是 `state/research_backlog.json`。每个任务包含目标、Track、依赖、验收、产物、资源预算、状态、证据、blocker、attempt 和 checkpoint。`state/NEXT_RUN_BACKLOG.yaml` 继续保留 A10—A40 研究拓扑，不作为第二套运行状态。

常用只读命令：

```powershell
python scripts/manage_research_backlog.py validate
python scripts/manage_research_backlog.py next
```

Daily 优先恢复可安全续跑的 running 任务，否则领取依赖满足的最高优先级 ready 任务。每次最多3项、总计最多90分钟。任务产物存在且验收通过后才能 completed；`refresh`在依赖完成后提升proposed任务，失败任务只有记录新修复路径后才可`retry`，连续失败两次且没有新修复路径时转blocked。

## 手动入口

入口位于 `automation/manual/`，支持：

```text
FORCE_MODE=AUTO|DAILY|TACTICAL|SYNTHESIS|AUDIT|FULL
UPDATE_SCHEDULE=true|false
```

手动默认 `UPDATE_SCHEDULE=false`。`FIVE_DAY` 明确映射到新的 Synthesis，`HALF_MONTH` 明确映射到新的 Audit；它们不再表示5日或15日周期。

示例：

```powershell
python scripts/check_schedule.py --force-mode TACTICAL --update-schedule false
python scripts/check_schedule.py --force-mode FULL --update-schedule true
```

## 状态、报告与恢复

- `state/automation_state.json`：独立周期的成功时间与次数；
- `state/research_execution_state.json`：当前阶段 checkpoint、开始/结束、状态、产物和错误；
- `state/execution_history.json`：幂等运行事件；
- `state/research_backlog.json`：研究任务状态；
- `state/human_decisions.json`：低频人工决定及简报节奏；
- `reports/daily/`、`tactical/`、`synthesis/`、`audit/`：阶段报告；
- `reports/research_briefs/`：前3周每7天一次，达到明确稳定性门槛后每14天一次的人工简报。

中断后先读取 `research_execution_state.json` 和 backlog checkpoint。不要手工伪造成功时间；修复后用新 `run_id` 重跑失败阶段。运行状态表示已落盘进度，不保证 Codex App 在另一个独立 worktree 运行时实时显示文件。

## 权限边界

Daily、Tactical 不得修改正式研究设计；Synthesis 只能提出 `PROPOSED DESIGN REVISION`；Audit 才能依据既有冻结—新建—更新索引—追加日志规则决定正式升级。核心研究方向变化进入 `needs_review`。所有周期均禁止付费 API、大规模训练/下载、绕过访问控制和伪造模型结果。

## 本地验证

```powershell
python -m unittest discover -s tests -v
python scripts/check_schedule.py --now 2026-10-13T12:00:00+08:00
python scripts/manage_research_backlog.py validate
```
