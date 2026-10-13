# LLM Historical Anachronism

本项目研究大语言模型在指定历史时间与信息条件下产生的历史时代错置（historical / temporal anachronism），以及可验证的缓解方法。它面向计算机相关专业硕士研究，目标不是只发布一个 Benchmark，而是以最小可信评测为测量工具，识别稳定缺陷并发展模型或系统方法。

## 核心科学问题

给定截止时间、历史行动者和可用信息，模型是否会引入当时尚未发生的事件、尚未形成的知识或制度，把在其他地区或社群已经存在的知识错误归给目标行动者，使用后世概念或后见解释，或在证据不足时仍过度确定？

项目严格区分四个命题：知识是否已存在、目标行动者是否可能接触、某份档案是否记录、模型是否实际使用了后世知识。单一档案没有记载，不能证明历史上不存在。

## 方法研究路线

- **M1 时间条件化参数适配：**比较时间 Prompt、LoRA/SFT，并在必要且算力允许时评估 DAPT/CPT。
- **M2 Temporal/Historical RAG：**区分文档时间、事件时间、知识有效时间和检索时点，过滤未来证据并保留来源链。
- **M3 时代错置验证 Agent：**识别可疑主张，生成年代查证问题，查询可信证据，执行时间有效性判断并修正或拒答。

三条路线目前是候选，不代表已经实现。路线选择必须由真实基线、最小原型和消融证据决定。

## 当前状态

已验证的基础设施包括历史来源与页级出处链、OCR/转录分层、证据与 Prompt 冻结、可恢复推理适配器、多维评分和实验结构校验。晚清公共卫生试点取得两种真实历史文献数字版本、14个页级样本、12个核验段落、20道开发题和11个证据组。

Research Validity Pilot 同时发现：20题中只有1题主要测量历史时间边界，严格可判未来知识侵入的题为0；现有数据更多支持来源忠实性和认识论校准。尚未进行真实模型实验，也没有 LoRA、DAPT、Temporal RAG 或 Agent 的效果结果。

## 数据与 Benchmark 的角色

Benchmark 是方法研究的测量基础，而不是最终目标。新数据建设从时代错置命题和年代证据链出发，再选择历史材料；不再以扩大某一时期史料页数作为默认进展指标。

主动研究入口位于 `research/`、`data/chronology/`、`experiments/anachronism_discovery/`、`experiments/baselines/` 和 `experiments/method_prototypes/`。

## 晚清研究资产

晚清公共卫生不再限定整个项目，但仍是已开发、可复用的历史场景。原始数据、处理结果、冻结 Prompt、报告与验证脚本保持原路径不变。入口见 [`legacy/late_qing/README.md`](legacy/late_qing/README.md)。

## 复现入口

```powershell
python scripts/data_feasibility_pilot/verify_pilot.py
python scripts/research_validity_pilot/verify_validity_pilot.py --root . --output reports/research_validity_pilot/VERIFICATION.json
python scripts/research_validity_pilot/run_openai_compatible.py --help
```

模型调用必须使用明确授权、可记录精确模型标识的接口。仓库不允许擅自调用付费 API、大规模训练、绕过访问控制或使用生成文本替代历史证据。

## 路线图

1. 明确时代错置定义、标签边界与反例。
2. 建立10—15个跨时期、跨领域的知识年代案例。
3. 构建最小可信评测并运行可控 Baseline。
4. 分别完成 M1/M2/M3 的最小原型和停止条件测试。
5. 根据错误覆盖、效果、成本和可复现性选择一条主方法路线。

当前正式设计见 [`research_design/RESEARCH_DESIGN.md`](research_design/RESEARCH_DESIGN.md)，历史结论与已冻结实验不得由新方向反向改写。
