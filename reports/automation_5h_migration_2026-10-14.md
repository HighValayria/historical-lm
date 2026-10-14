# 五小时自动化调度迁移报告

日期：2026-10-14（Asia/Shanghai）

## App 配置

- 原位更新唯一 Automation `automation`（显示名“每日自动化迭代”），未创建第二个 Automation。
- 状态：`ACTIVE`。
- App 实际持久化规则：`FREQ=HOURLY;INTERVAL=5;BYMINUTE=0`。
- App 目标项目：`local-651ff4f7ea9e6ff847d9a130d1f7d5cf`。
- 工作目录：`D:\Resources\llm-historical-anachronism`。
- 主机时区核验：Windows `China Standard Time`，UTC+08:00。

当前 App 更新接口明确不接受显式 DTSTART/时区行，且只读接口未返回 `nextRunAt`。因此 App 规则使用整点约束，固定相位锚点 `2026-10-14T09:00:00+08:00` 由 `state/execution_tick_state.json` 持久化并用于仓库侧校验。按该规则与锚点，迁移后的前三个预计触发点为：

1. 2026-10-14 14:00（Asia/Shanghai，UTC+08:00）；
2. 2026-10-14 19:00（Asia/Shanghai，UTC+08:00）；
3. 2026-10-15 00:00（Asia/Shanghai，UTC+08:00）。

这是由已保存规则计算的预计时间；当前 API 不暴露 App 内部实际 `nextRunAt`，因此未将不可读取的 UI 值伪报为已验证。

## 仓库侧迁移

- 新增独立 `EXECUTION_TICK` 状态机：五小时槽、30分钟迟到窗口、`SKIP_MISSED_SLOTS`、已完成槽幂等记录、checkpoint 与仓库级写锁。
- 活动锁存在时新触发安全跳过；锁租约为120分钟，高于90分钟单次预算。中断/失败保留 checkpoint，不记录科研成功。
- 每次有效 tick 优先恢复安全 running 任务，否则选择最高优先级 ready 任务；全部有界工作合计最多3项、90分钟。
- 六通道 Research Radar 改为距上次成功至少24小时；Tactical/Synthesis/Audit 继续按3/7/14天成功时间滚动。
- 手动 FORCE_MODE 保留，使用同一写锁但默认不改变自动槽或周期成功时间。
- 迁移未运行正式科研任务，未增加任何阶段 run count；迁移前后 Daily/Radar=11、Tactical=0、Synthesis=0、Audit=0。

## 休眠与补跑边界

仓库不会唤醒电脑。App 未触发时槽直接错过；恢复后只计算当前最近槽，不为多个错过槽批量补跑。若 App 提供原定时间，可准确执行30分钟迟到判断；当前 Prompt/API 不保证提供该字段，因此无原定时间时只能用固定锚点、当前窗口、执行锁和已完成槽降低旧请求误执行风险，不能保证识别所有补发请求。

## 验证

- 调度定向测试：18/18 通过。
- 仓库全量单元测试：27/27 通过。
- Backlog 校验：6项任务，状态 `valid`。
- Python 编译检查与 `git diff --check`：通过。
- 2026-10-14 14:00 的周期计划：Radar/Tactical/Synthesis/Audit 均未到期，证明五小时入口不会重复日巡检。
