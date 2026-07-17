# 第一次使用

这是“晚清公共卫生历史语言模型探索”项目的最小启动包。

你只需要：

1. 将整个目录放到本地，例如：
   `D:\Projects\historical-lm-exploration`
2. 在该目录初始化 Git：
   `git init`
3. 使用 Codex 打开该目录。
4. 把下面这句话作为第一次任务发送给 Codex：

   `请完整读取 AGENTS.md、PROJECT_CHARTER.md、.agent/PLANS.md、state/graph.yaml、state/config.yaml、state/run_state.json 和 MASTER_PROMPT.md，然后按照 MASTER_PROMPT.md 开始第一轮自主探索。不要等待逐步确认。`

第一次运行时，Codex应自行创建其余目录、任务文件、证据表、日志和报告。

不要在最开始手工创建大量空文件。只有当Agent真正需要某项产物时，再由它创建并记录用途。
