# 自主科研调度与任务管理迁移验证报告

日期：2026-10-13
范围：框架迁移、兼容和轻量本地测试；未执行真实研究、联网检索、模型调用、下载或训练。

## 结构变更

- 调度从滚动1/5/15日升级为Daily + 3-Day Tactical + 7-Day Synthesis + 14-Day Audit，固定顺序为Daily → Tactical → Synthesis → Audit。
- `state/automation_state.json`升级为v2，四阶段独立保存`last_successful`与`run_count`；统一使用带`+08:00`偏移的ISO 8601时间戳。
- 新增`research_execution_state.json`、`execution_history.json`、`human_decisions.json`和`research_backlog.json`，支持checkpoint、幂等事件、低频人工决策及A/B双轨任务。
- 新增成功门控记录器和Backlog管理器；旧手动入口保留为显式别名，新入口支持AUTO、DAILY、TACTICAL、SYNTHESIS、AUDIT、FULL。
- 新增Tactical、Synthesis、Audit和Research Brief目录，但未创建虚假周期报告。

## 状态迁移

旧状态原样嵌入`legacy_migration.old_1_5_15_state`：Daily 10次（最近2026-10-13）、Five-Day 2次（最近2026-10-09）、Half-Month 1次（最近2026-10-04）。Daily历史延续；新Tactical/Synthesis/Audit的成功次数均为0，分别从迁移锚点后3/7/14天首次到期。

旧报告、原晚清资料、20题开发集、构念审计、Benchmark与研究设计v002均未重命名为新成果或覆盖。严格时代错置验证题数仍为0，真实模型输出仍为0。

## 测试结果

- 新测试：14/14 PASS。
- 覆盖：首次初始化、3/7/14边界、跨月跨年、失败不推进、漏跑单次补做、同日周期去重、强制模式、`UPDATE_SCHEDULE`、旧状态迁移、旧入口别名、Backlog依赖/恢复/Track平衡、正式设计权限。
- 旧Data Feasibility验证：PASS（73文件哈希、20题、60 Prompt；无模型输出）。
- 旧Research Validity验证：18/18 PASS（72个factorial packet；无伪造模型结果）。

## App Automation

既有Codex App“每日自动化迭代”已原位更新，没有创建重复日程。核验结果：`status=ACTIVE`，每天09:00运行，模型与reasoning设置保持不变，project ID保持不变，`cwds`已从旧路径更新为`D:\Resources\llm-historical-anachronism`。不需要手动重设Automation。

## Git与遗留问题

提交与push结果在完成Git操作后写入本报告最终提交记录。当前遗留研究阻塞为B-0003（无授权、版本明确的模型接口）和B-0005（严格验证时代错置题数为0）；它们没有被框架迁移掩盖。
