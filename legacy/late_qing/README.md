# 晚清公共卫生研究资产索引

本目录是旧研究场景的入口，不复制、不移动也不改写冻结资产。晚清公共卫生从项目边界调整为可复用案例；下列文件继续保持原路径和 Git 历史。

## Legacy Research Assets

- 原始与处理后数据：`data/raw/data_feasibility_pilot/`、`data/processed/data_feasibility_pilot/`
- Data Feasibility Pilot：`experiments/data_feasibility_pilot/`
- Research Validity Pilot：`experiments/research_validity_pilot/`
- 早期 Benchmark：`benchmarks/pilot/`
- 来源与证据登记：`evidence/source_registry.*`、`evidence/concept_map.md`
- 主要报告：`reports/data_feasibility_pilot/`、`reports/research_validity_pilot/`
- 原始综合报告：`reports/FINAL_REPORT.md`、`reports/最终总结报告.md`

## Reusable Infrastructure

可复用内容包括 OCR与候选页提取、来源—页面—段落—题项出处链、原 OCR 与核验转录分层、Prompt生成与哈希、可恢复推理适配器、多维评分、盲核材料和自动验证。

## 已知边界

当前材料集中于1884、1889、1890年的英文机构档案。20道开发题中只有Q017主要测历史时间边界，没有严格可判后世知识侵入的题目，且独立人工核验与真实模型实验尚未完成。因此这些资产不能被重新命名为已经验证的时代错置 Benchmark。

旧的史料扩张任务归档于 `legacy/late_qing/NEXT_RUN_BACKLOG_exploration-002-proposed.yaml`。如未来任务直接支持年代证据卡或方法压力测试，可按新主线重新激活，而不是整批恢复。
