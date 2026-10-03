# 自动化说明

## 初始设置

1. 打开 Codex App。
2. 打开本仓库。
3. 创建一个每天 09:00 运行的 Automation。
4. 使用以下 Automation prompt：

```text
读取 automation/MASTER_AUTOMATION_PROMPT.md，
按照其中定义的滚动1天—5天—15天周期，
继续本项目的无人研究任务。
以仓库状态为准，不等待人工确认。
```

## 运行环境要求

本仓库面向 Codex App Scheduled Automation 设计，不需要单独的 OpenAI API 自动化管线。

调度环境应提供可运行 `python scripts/check_schedule.py` 的 `python` 命令。如果 `PATH` 中没有 `python`，使用 Codex App 捆绑的 Python 运行同一脚本。

本机迁移也已用以下 Python 路径验证：

```text
C:\Users\33967\AppData\Local\Programs\Python\Python312\python.exe
```

## 恢复机制

如果某次计划运行错过，下一次运行会使用 `state/automation_state.json` 中的 `last_five_day` 和 `last_half_month` 判断是否需要补跑 Five-Day 或 Half-Month。

## Daily Research Radar

Daily 的论文发现跟踪的是对本仓库而言的新发现，而不只是最近一天发表的论文。

所有生成的 Daily、Five-Day 和 Half-Month 研究报告都应使用中文。原始论文标题、标识符和路径可以保留原文。

Daily 是多通道研究雷达，不是单纯论文搜索。每次运行必须检查 `PAPERS`、`DATASETS`、`ARCHIVES`、`METHODS`、`RESOURCES` 和 `PROJECT_IMPACT`，并在报告中显示每个通道已检查或被阻塞。没有实质更新也仍然是一次完成的通道检查。

Daily 不得修改 `research_design/RESEARCH_DESIGN.md`。Daily 只记录新证据、更新 registry、写 Daily 报告并加入 Five-Day 队列。

系统区分：

- `newly_published`：近期出现且此前未登记的工作；
- `newly_discovered`：本系统今天第一次发现的较早相关工作；
- `existing_paper_update`：关于已存在于 `state/seen_papers.json` 或 `evidence/literature_master.csv` 中论文的新信息。

这允许自动化早期先补齐历史文献欠账，随后自然转向监测真正近期研究。

## 研究设计状态

当前正式研究设计主文档是：

```text
research_design/RESEARCH_DESIGN.md
```

该文件是当前研究方案的人类可读正式依据。Five-Day 和 Half-Month 必须把它作为最终研究设计汇总入口。

`research_design/DESIGN_CHANGELOG.md` 记录对正式研究设计的实质变更。

Five-Day 只能更新有限的证据 / 状态区域：

- 新证据；
- 支持 / 反对证据（Evidence For / Against）；
- 开放问题（Open Questions）；
- 阻塞项（Blockers）；
- 下一步研究优先级（Next Research Priorities）；
- 贡献证据强度状态；
- 数据源状态；
- benchmark 成熟度；
- 候选方法状态。

Five-Day 对核心研究问题、研究问题组、研究叙事、核心贡献定义或整体实验范式的重大变化，只能提出建议，不能直接实施。

Half-Month 是唯一允许正式重构核心设计的层级。Half-Month 更新 `research_design/RESEARCH_DESIGN.md` 后，如果保留辅助文件且它们仍然有用，应同步更新。

`research_design/contribution_map.md` 和 `research_design/experiment_matrix.csv` 等辅助文件可以服务自动化；若它们与 `research_design/RESEARCH_DESIGN.md` 冲突，以主文档为准。

## 手动运行

手动运行入口：

```text
automation/manual/RUN_DAILY.md
automation/manual/RUN_FIVE_DAY.md
automation/manual/RUN_HALF_MONTH.md
automation/manual/RUN_FULL.md
```

每个文件都提供一个最简指令，用于在不等待正常滚动调度的情况下强制运行一个层级或全部层级。

手动运行默认使用：

```text
UPDATE_SCHEDULE=false
```

这意味着任务会执行，但自动 `last_*` 周期日期和运行次数不会改变。只有当手动运行应计为正式周期运行时，才设置 `UPDATE_SCHEDULE=true`。

## 人工检查

未来检查时优先查看：

```text
reports/half_month/
research_design/RESEARCH_DESIGN.md
research_design/DESIGN_CHANGELOG.md
```
