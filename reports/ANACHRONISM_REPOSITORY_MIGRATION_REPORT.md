# LLM Historical Anachronism 项目迁移报告

日期：2026-10-13

状态：**研究方向、仓库内容与GitHub原地迁移已完成；本地目录改名和Codex项目/自动化重绑定因当前进程占用而未完成。整体迁移不得标记为全部验收通过。**

## 1. 迁移前后状态

| 项目 | 迁移前 | 当前实际状态 |
|---|---|---|
| 项目名称 | 晚清历史认知模型 / Historical LM Exploration | LLM Historical Anachronism |
| 本地目录 | `D:\Resources\historical_lm_exploration_starter` | 仍为旧路径；目标路径尚未创建，见B-0006 |
| GitHub仓库 | `HighValayria/historical-lm` | `HighValayria/llm-historical-anachronism`，已原地重命名 |
| 默认分支 | `main` | `main` |
| 原始HEAD | `1a3119aeb75f858bcf82a29bb21606cc67d94886` | 由保护标签固定 |
| 研究方向提交 | 无 | `b0dc3dc` |
| 路径/迁移保护提交 | 无 | `6aa25c4` |
| 迁移状态提交 | 无 | `a93d6549170d0c66ac18764d2ffbc664e564e182` |
| 本地/远程分支 | 本地最初比远程多27提交 | 在最终报告提交前，本地HEAD与新仓库`origin/main`均为`a93d654` |

迁移前 GitHub `main` 为 `2fb8f42`。在修改项目身份前，先将本地完整历史推至原仓库，并创建/推送 `pre-anachronism-migration-20261013`。GitHub原仓库随后通过正常重命名接口迁移，没有创建与旧历史无关的空仓库。

## 2. 研究方向变化

旧设计以1880—1899年晚清公共卫生、来源约束评测和历史性无知为主要方向。Research Validity Pilot 发现已有20题中只有Q017主要测历史时间边界，严格可判未来知识侵入的题为0；现有11个证据组更支持来源忠实性和认识论校准。

新设计以跨时期、跨地域、跨语言和跨领域的 LLM historical/temporal anachronism 为科学问题。目标贡献顺序调整为：

1. 通过真实Baseline确认可判定的时代错置缺陷；
2. 以模型或系统方法缓解缺陷；
3. 用最小可信Benchmark测量方法，而不是以题量作为最终贡献；
4. 将来源忠实性、归因、校准和拒答作为必要控制维度。

v002正式设计并行保留三条候选路线：M1时间条件化LoRA/SFT及必要的DAPT/CPT；M2区分文档、事件与知识有效时间的Temporal/Historical RAG；M3执行主张抽取、年代查证、证据判断和修正/拒答的验证Agent。三条路线均未被声称已经实现或有效，最终只能依据共同Baseline、消融、成本和可复现性选择。

## 3. 文件与目录变更

### 新增或重建的主动入口

- `README.md`与`PROJECT_CHARTER.md`：新项目身份、科学问题与贡献优先级。
- `research_design/RESEARCH_DESIGN.md`：完整v002正式设计。
- `research/`：问题定义、taxonomy、hypotheses、文献和M1/M2/M3方法目录。
- `data/chronology/`与`data/benchmarks/`：年代证据卡和新评测入口。
- `experiments/anachronism_discovery/`、`experiments/baselines/`、`experiments/method_prototypes/`。
- `state/NEXT_RUN_BACKLOG.yaml`：A10—A40 Research & Method Feasibility拓扑。

### 归档与保留

- v001正式设计冻结为`research_design/archive/RESEARCH_DESIGN_v001.md`；精确原文可由保护标签恢复。
- 旧Backlog和队列登记到`legacy/late_qing/`，标记为superseded/on-demand，而不是删除研究历史。
- 原有`data_feasibility_pilot`、`research_validity_pilot`、`benchmarks/pilot`、raw/processed数据、Prompt、哈希、评分与报告均保持原路径。
- `reports/FINAL_REPORT.md`、`reports/最终总结报告.md`内容未被迁移方向反向改写。
- `.obsidian/`仍在本地，现加入`.gitignore`以避免提交机器/窗口状态；没有删除。

### 路径兼容

非历史性代码中没有发现失效的旧绝对路径。现存旧路径引用只有：

- 原Data Feasibility报告记录当时真实执行目录，按要求保留；
- `complete_local_path_migration.ps1`必须显式知道旧路径，属于一次性兼容脚本；
- 迁移清单和本报告作为历史记录。

## 4. Git和GitHub实际操作

实际执行：

1. 审计分支、HEAD、dirty状态、remote、worktree、子模块/LFS配置、最大文件、凭据和目标名称冲突。
2. 创建并推送保护标签`pre-anachronism-migration-20261013`。
3. 将原本只在本地的27个提交快进推送到旧GitHub仓库。
4. 创建提交`b0dc3dc`、`6aa25c4`和`a93d654`。
5. 使用具有admin权限的现有GitHub账户把原仓库原地重命名为`llm-historical-anachronism`。
6. 更新Description和8个Topics。
7. 把本地`origin`改为`https://github.com/HighValayria/llm-historical-anachronism.git`。
8. 将迁移提交推送到新规范URL并核验分支SHA。

未执行：强制推送、历史重写、`reset --hard`、`clean`、删除原仓库、新建空仓库或第二个可独立变化的工作副本。

GitHub补充检查：仓库公开、未归档、Issues启用、默认分支未受保护；本地不存在GitHub Actions工作流和`${{ secrets.* }}`引用；没有`.gitmodules`、`.gitattributes`或LFS pointer文件。Git LFS程序本身已安装，但该仓库未配置LFS跟踪。

## 5. 完整性检查

| 检查 | 结果 |
|---|---|
| Data Feasibility验证 | PASS：3来源登记、2纳入来源、14页、12证据单元、20题、60 Prompt、73文件哈希 |
| Research Validity验证 | PASS：18项检查、72个E0—E3 packet结构保持 |
| 迁移前/改名前本地验证 | PASS：11项 |
| 关键冻结资产 | PASS：6个文件字节数与SHA-256一致 |
| 原v001设计 | PASS：保护标签中原文件SHA-256一致且可恢复 |
| JSON/YAML解析 | PASS：最终检查45个JSON与7个YAML |
| Python脚本编译 | PASS |
| PowerShell改名脚本干运行 | PASS：`ready=true`，本地/远程HEAD一致 |
| Git历史连续 | PASS：`1a3119a`是当前HEAD祖先，提交数从43增加到46（最终报告提交前） |
| GitHub规范名称 | PASS：通过新API地址直接返回新`name/full_name`，不是依赖旧URL重定向 |
| 本地目录名称 | FAIL/BLOCKED：当前Codex进程持有旧目录句柄 |

详细证据见`reports/migration/pre_migration_manifest.json`、`local_pre_rename_verification.json`、`final_pre_rename_verification.json`和`remote_verification_2026-10-13.json`。

## 6. 遗留问题

### B-0006：本地目录与Codex绑定

实际执行`Rename-Item`时，Windows返回“文件正由另一进程使用”。检查后源目录仍存在、目标目录不存在，因此没有发生半完成移动。

关闭当前Codex工作区和可能打开该库的Obsidian窗口后，在普通PowerShell中执行：

```powershell
cd D:\Resources
powershell -NoProfile -ExecutionPolicy Bypass -File .\historical_lm_exploration_starter\scripts\complete_local_path_migration.ps1 -Execute
```

脚本会拒绝dirty工作区、已存在目标目录、错误源目录或本地/远程HEAD不一致；成功后运行迁移验证并写入新目录下的`reports/migration/post_rename_verification.json`。

随后需要把`D:\Resources\llm-historical-anachronism`重新加入/打开为Codex项目。名为“每日自动化迭代”的cron目前是`PAUSED`，仍绑定旧project ID和cwd；在新项目出现前不能安全重绑定，也不应恢复运行。更新后再解除B-0006。

### 研究阻塞

- B-0003：没有可控、版本明确的模型接口，真实Baseline仍为0。
- B-0005：尚无10—15个独立核验的跨领域年代案例。
- M1/M2/M3没有任何真实效果，不得由迁移文档推断可行性。

## 7. 新项目下一步工作

依赖顺序为：

1. A10：时代错置定义、不可判定规则和标注反例；
2. A11：M1/M2/M3直接竞争工作、开源实现、资源和差异化矩阵；
3. A12：10—15个跨领域年代证据卡；
4. A20/A21：最小可信评测和真实Baseline；
5. A30/A31/A32：三条路线的最小原型与共同消融；
6. A40：选择一条主方法路线。

晚清公共卫生扩张不再是默认前置工作。它只有在提供严格年代证据、行动者传播证据、跨来源对照或入选方法的独特压力测试时才重新激活。

## 8. 验收清单

- [x] 新项目章程体现时代错置与方法创新目标。
- [x] 原晚清资产得到完整保留和索引。
- [ ] 本地目录迁移到新名称——受当前Codex进程占用阻塞，已提供受保护脚本。
- [x] GitHub原仓库实际迁移到新名称。
- [x] 本地origin更新为新仓库规范地址。
- [x] Git历史完整保留。
- [x] 迁移提交成功推送并验证。
- [x] 原有关键数据和实验产物未受损。
- [x] 主要脚本和关键哈希通过检查；最终新路径检查等待本地改名。
- [x] README、研究设计、Backlog与自动化研究优先级已更新。
- [x] 最终迁移报告已保存；其提交与远程HEAD在提交后再次验证。

结论：**GitHub、Git历史、项目身份、研究设计和仓库内容迁移已经真实完成；本地路径与Codex自动化绑定尚未完成，因此本轮是“远程/内容完成，本地路径一项受阻”的迁移，而不是全部验收通过。**
