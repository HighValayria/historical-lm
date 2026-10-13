"""Audit the frozen 20-item pilot and create a separate validity-oriented revision.

The frozen inputs are never modified.  Judgments in AUDIT are construct-audit
annotations, not historical truth labels.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


AUDIT = {
    "DFP-Q001": {
        "primary_construct": "historical_fact_reading_comprehension",
        "secondary_constructs": ["source_scope_control"],
        "disposition": "control_only",
        "ordinary_reading_sufficient_with_oracle": True,
        "direct_historical_boundary_or_anachronism": False,
        "oracle_requirement": "required_for_fair_answer",
        "cue_risk": "medium: '根据所给' announces an extractive task",
        "false_penalty_risk": "high_without_oracle: source-specific local contrast is not reasonable cold recall",
        "audit_note": "Useful positive reading control, not a temporal-boundary item.",
        "revised_question": "一份1889年东昌府医疗工作报告如何区分当地、芝罘与山东内地的霍乱情况？",
    },
    "DFP-Q002": {
        "primary_construct": "evidence_insufficiency_and_epistemic_calibration",
        "secondary_constructs": ["source_scope_control", "unsupported_number_avoidance"],
        "disposition": "usable_directly",
        "ordinary_reading_sufficient_with_oracle": True,
        "direct_historical_boundary_or_anachronism": False,
        "oracle_requirement": "required_for_fair_answer",
        "cue_risk": "high: yes/no wording strongly cues refusal",
        "false_penalty_risk": "high_without_oracle",
        "audit_note": "Measures evidence scope, not whether 1888 actors knew a fact.",
        "revised_question": "根据该报告，能够确定哪些与1888年山东霍乱死亡有关的信息？哪些数量信息仍不能确定？",
    },
    "DFP-Q003": {
        "primary_construct": "historical_fact_reading_comprehension",
        "secondary_constructs": ["scientific_claim_extraction"],
        "disposition": "control_only",
        "ordinary_reading_sufficient_with_oracle": True,
        "direct_historical_boundary_or_anachronism": False,
        "oracle_requirement": "required_for_fair_answer",
        "cue_risk": "low",
        "false_penalty_risk": "high_without_oracle: obscure source-specific experiment",
        "audit_note": "Straight extraction control.",
        "revised_question": "1889年期刊所转述的Loewenthal实验，其目标物质应同时满足哪两个条件？",
    },
    "DFP-Q004": {
        "primary_construct": "historical_claim_vs_modern_fact_distinction",
        "secondary_constructs": ["evidence_insufficiency_and_epistemic_calibration"],
        "disposition": "usable_directly",
        "ordinary_reading_sufficient_with_oracle": True,
        "direct_historical_boundary_or_anachronism": False,
        "oracle_requirement": "required_for_fair_answer",
        "cue_risk": "high: '仅凭' and a strong clinical claim cue rejection",
        "false_penalty_risk": "high_without_oracle",
        "audit_note": "Potential temporal item only after independently dating later clinical evidence; current label is evidence-strength only.",
        "revised_question": "材料把Salol的证据推进到哪一层：研究目标、实验观察、还是已经确认的人体临床疗效？说明材料未支持的层次。",
    },
    "DFP-Q005": {
        "primary_construct": "historical_fact_reading_comprehension",
        "secondary_constructs": ["institutional_context"],
        "disposition": "control_only",
        "ordinary_reading_sufficient_with_oracle": True,
        "direct_historical_boundary_or_anachronism": False,
        "oracle_requirement": "required_for_fair_answer",
        "cue_risk": "low",
        "false_penalty_risk": "high_without_oracle",
        "audit_note": "Source-specific reading control.",
        "revised_question": "济南府药房报告中，拒收病例所对应的现实限制及其量化信息是什么？",
    },
    "DFP-Q006": {
        "primary_construct": "historical_fact_reading_comprehension",
        "secondary_constructs": ["numeric_extraction"],
        "disposition": "control_only",
        "ordinary_reading_sufficient_with_oracle": True,
        "direct_historical_boundary_or_anachronism": False,
        "oracle_requirement": "required_for_fair_answer",
        "cue_risk": "low",
        "false_penalty_risk": "high_without_oracle",
        "audit_note": "Numeric reading control; answer is not the number of unique persons.",
        "revised_question": "第74页统计表中的Vaccinations数值及其计量含义是什么？",
    },
    "DFP-Q007": {
        "primary_construct": "ocr_image_evidence_fidelity",
        "secondary_constructs": ["numeric_verification"],
        "disposition": "temporarily_unsuitable",
        "ordinary_reading_sufficient_with_oracle": False,
        "direct_historical_boundary_or_anachronism": False,
        "oracle_requirement": "requires_image_and_raw_ocr_pair",
        "cue_risk": "very_high: both candidate answers and the OCR lesson are disclosed",
        "false_penalty_risk": "high: text-only Oracle omits the competing raw OCR/image evidence",
        "audit_note": "Retain for a separate multimodal/OCR audit, not the text-only 2x2 main experiment.",
        "revised_question": "比较原页图像与原始OCR，记录‘门诊换药日访视次数’，并指出最终采用哪一证据层。",
    },
    "DFP-Q008": {
        "primary_construct": "source_and_speaker_attribution",
        "secondary_constructs": ["historical_actor_knowledge_boundary", "historical_claim_vs_modern_fact_distinction"],
        "disposition": "usable_directly",
        "ordinary_reading_sufficient_with_oracle": True,
        "direct_historical_boundary_or_anachronism": False,
        "oracle_requirement": "required_for_fair_answer",
        "cue_risk": "low",
        "false_penalty_risk": "high_without_oracle",
        "audit_note": "Measures what this author asserted, not the epidemiological truth of the assertion.",
        "revised_question": "1890年《中国热病》作者对接种材料提出了什么担忧？这段材料的证据地位是什么？",
    },
    "DFP-Q009": {
        "primary_construct": "historical_claim_vs_modern_fact_distinction",
        "secondary_constructs": ["evidence_insufficiency_and_epistemic_calibration", "source_scope_control"],
        "disposition": "usable_directly",
        "ordinary_reading_sufficient_with_oracle": True,
        "direct_historical_boundary_or_anachronism": False,
        "oracle_requirement": "required_for_fair_answer",
        "cue_risk": "high: yes/no proof wording cues rejection",
        "false_penalty_risk": "high_without_oracle",
        "audit_note": "Good source-versus-truth item, but not a direct temporal existence test.",
        "revised_question": "分别判断：（a）材料是否记录了一名作者对接种传播疾病的担忧；（b）材料是否足以估计晚清接种传播这些疾病的实际频率。",
    },
    "DFP-Q010": {
        "primary_construct": "historical_fact_reading_comprehension",
        "secondary_constructs": ["source_attribution"],
        "disposition": "control_only",
        "ordinary_reading_sufficient_with_oracle": True,
        "direct_historical_boundary_or_anachronism": False,
        "oracle_requirement": "required_for_fair_answer",
        "cue_risk": "low",
        "false_penalty_risk": "high_without_oracle",
        "audit_note": "Geographic extraction control, not independent epidemic reconstruction.",
        "revised_question": "该作者如何描述1888年霍乱流行的地域范围和传播方向？",
    },
    "DFP-Q011": {
        "primary_construct": "evidence_insufficiency_and_epistemic_calibration",
        "secondary_constructs": ["unsupported_number_avoidance"],
        "disposition": "usable_directly",
        "ordinary_reading_sufficient_with_oracle": True,
        "direct_historical_boundary_or_anachronism": False,
        "oracle_requirement": "required_for_fair_answer",
        "cue_risk": "high: asks whether an imprecise phrase supports precision",
        "false_penalty_risk": "medium_without_oracle: quoted English phrase is present",
        "audit_note": "A calibration item; it does not establish the real mortality count.",
        "revised_question": "短语‘sweeping away thousands of lives’允许怎样的数量表述？给出其精度上限，并说明不能推出什么。",
    },
    "DFP-Q012": {
        "primary_construct": "source_and_speaker_attribution",
        "secondary_constructs": ["historical_actor_knowledge_boundary"],
        "disposition": "needs_revision",
        "ordinary_reading_sufficient_with_oracle": True,
        "direct_historical_boundary_or_anachronism": False,
        "oracle_requirement": "requires_surrounding_context_to_identify_speaker",
        "cue_risk": "low",
        "false_penalty_risk": "high: isolated passage uses 'he' without naming the speaker",
        "audit_note": "Content is readable, but speaker identity needs surrounding-page context before this can be a true attribution item.",
        "revised_question": "会议讨论中，关于上海猩红热出现的陈述主体和具体内容是什么？",
        "factorial_eligible_override": False,
    },
    "DFP-Q013": {
        "primary_construct": "evidence_insufficiency_and_epistemic_calibration",
        "secondary_constructs": ["historical_first_occurrence_claim", "source_scope_control"],
        "disposition": "usable_directly",
        "ordinary_reading_sufficient_with_oracle": True,
        "direct_historical_boundary_or_anachronism": False,
        "oracle_requirement": "required_for_fair_answer",
        "cue_risk": "high: '能否独立证明' cues no",
        "false_penalty_risk": "high_without_oracle_and_secondary_chronology",
        "audit_note": "Can test restraint, but cannot label the true first arrival without independent chronology.",
        "revised_question": "根据这段会议发言，可以对上海猩红热的出现时间作出哪些结论？哪些关于‘首次传入’的结论仍需独立证据？",
    },
    "DFP-Q014": {
        "primary_construct": "historical_fact_reading_comprehension",
        "secondary_constructs": ["qualification_preservation"],
        "disposition": "control_only",
        "ordinary_reading_sufficient_with_oracle": True,
        "direct_historical_boundary_or_anachronism": False,
        "oracle_requirement": "required_for_fair_answer",
        "cue_risk": "medium: question explicitly asks for both sides",
        "false_penalty_risk": "high_without_oracle",
        "audit_note": "Balanced-reading control.",
        "revised_question": "汇编怎样同时描述北京住房环境中的不卫生因素与缓和条件？两类信息都要保留。",
    },
    "DFP-Q015": {
        "primary_construct": "evidence_fidelity_and_qualification",
        "secondary_constructs": ["historical_reasoning_reconstruction"],
        "disposition": "usable_directly",
        "ordinary_reading_sufficient_with_oracle": True,
        "direct_historical_boundary_or_anachronism": False,
        "oracle_requirement": "required_for_fair_answer",
        "cue_risk": "high: '是否简单断言' cues the qualified answer",
        "false_penalty_risk": "high_without_oracle",
        "audit_note": "Tests preservation of a counterintuitive qualification, not modern causal correctness.",
        "revised_question": "概括1874年北京报告关于卫生条件、排水系统与城市健康之间关系的论证，并保留其限定语。",
    },
    "DFP-Q016": {
        "primary_construct": "historical_fact_reading_comprehension",
        "secondary_constructs": ["possible_anachronistic_addition_control"],
        "disposition": "needs_revision",
        "ordinary_reading_sufficient_with_oracle": True,
        "direct_historical_boundary_or_anachronism": False,
        "oracle_requirement": "required_for_fair_answer",
        "cue_risk": "medium",
        "false_penalty_risk": "high: original gold mentions methods outside the verified excerpt",
        "audit_note": "Restrict gold to alum and careful filtration unless the longer page passage is added and checked.",
        "revised_question": "仅依据给定段落，天津河水被建议采用哪些处理方法？材料对其他方法提供了什么信息？",
        "gold_answer_override": "给定核验段落直接支持两种办法：用明矾处理，以及仔细过滤。仅凭该段不能加入氯化消毒、现代净水厂或段落之外的其他处理步骤。",
    },
    "DFP-Q017": {
        "primary_construct": "publication_observation_cutoff_time_distinction",
        "secondary_constructs": ["temporal_metadata_reasoning", "evidence_scope_control"],
        "disposition": "usable_directly",
        "ordinary_reading_sufficient_with_oracle": True,
        "direct_historical_boundary_or_anachronism": True,
        "oracle_requirement": "required_for_fair_answer",
        "cue_risk": "high: yes/no wording cues date separation",
        "false_penalty_risk": "high_without_oracle_metadata",
        "audit_note": "The only current item whose primary construct directly distinguishes historical times.",
        "revised_question": "分别给出该天津水源陈述的观察期、汇编出版年，以及两种日期各自允许的历史结论。",
    },
    "DFP-Q018": {
        "primary_construct": "evidence_fidelity_and_causal_strength",
        "secondary_constructs": ["historical_claim_vs_modern_fact_distinction"],
        "disposition": "usable_directly",
        "ordinary_reading_sufficient_with_oracle": True,
        "direct_historical_boundary_or_anachronism": False,
        "oracle_requirement": "required_for_fair_answer",
        "cue_risk": "medium: asks explicitly about strength",
        "false_penalty_risk": "high_without_oracle",
        "audit_note": "Measures causal overstatement, not post-cutoff knowledge intrusion.",
        "revised_question": "第20页的材料对排水与伤寒关系提供了哪一层证据：同时出现、报告者联系、还是受控因果证明？说明选择。",
    },
    "DFP-Q019": {
        "primary_construct": "historical_fact_reading_comprehension",
        "secondary_constructs": ["source_scope_control"],
        "disposition": "control_only",
        "ordinary_reading_sufficient_with_oracle": True,
        "direct_historical_boundary_or_anachronism": False,
        "oracle_requirement": "required_for_fair_answer",
        "cue_risk": "low",
        "false_penalty_risk": "high_without_oracle",
        "audit_note": "Local-infrastructure reading control; do not generalize to China.",
        "revised_question": "汉口段落把街巷污物长期积聚归因于哪些基础设施或服务缺失？这一描述可支持多大的地域范围？",
    },
    "DFP-Q020": {
        "primary_construct": "archive_population_and_source_scope_control",
        "secondary_constructs": ["historical_actor_knowledge_boundary", "epistemic_calibration"],
        "disposition": "usable_directly",
        "ordinary_reading_sufficient_with_oracle": False,
        "direct_historical_boundary_or_anachronism": False,
        "oracle_requirement": "requires_multi_source_metadata_and_passages",
        "cue_risk": "high: universal claim makes rejection obvious",
        "false_penalty_risk": "medium: answer requires archive-population metadata beyond passage content",
        "audit_note": "Strong digital-humanities scope item, but not a temporal anachronism item.",
        "revised_question": "这些材料直接代表哪些档案行动者和可见人群？列出至少三类不能从当前样本推广覆盖的人群或知识场域。",
    },
}


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def file_record(path: Path, root: Path) -> dict:
    return {
        "path": path.resolve().relative_to(root.resolve()).as_posix(),
        "bytes": path.stat().st_size,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    out = args.output_dir
    out.mkdir(parents=True, exist_ok=True)
    source_paths = [
        root / "experiments/data_feasibility_pilot/benchmark/benchmark_items.jsonl",
        root / "experiments/data_feasibility_pilot/benchmark/evidence_bank.jsonl",
        root / "experiments/data_feasibility_pilot/model_eval/prompt_packets.jsonl",
        root / "experiments/data_feasibility_pilot/model_eval/evaluation_rubric.md",
    ]
    original = read_jsonl(source_paths[0])
    original_ids = {row["item_id"] for row in original}
    if original_ids != set(AUDIT):
        raise SystemExit(f"Audit IDs differ from frozen items: {sorted(original_ids ^ set(AUDIT))}")

    audited = []
    revised = []
    for row in original:
        item_id = row["item_id"]
        annotation = AUDIT[item_id]
        public_annotation = {
            key: value
            for key, value in annotation.items()
            if key not in {"gold_answer_override", "factorial_eligible_override"}
        }
        audited.append(
            {
                "item_id": item_id,
                "original_type": row["type"],
                "original_question": row["question"],
                "evidence_passage_ids": row["evidence_passage_ids"],
                "independence_group": row["independence_group"],
                **public_annotation,
                "reviewer_identity": "Codex primary agent, same project lineage",
                "independent_review": False,
            }
        )
        revised.append(
            {
                **row,
                "version": "RVP-v2-development",
                "parent_item_id": item_id,
                "question": annotation["revised_question"],
                "gold_answer": annotation.get("gold_answer_override", row["gold_answer"]),
                "primary_construct": annotation["primary_construct"],
                "secondary_constructs": annotation["secondary_constructs"],
                "research_disposition": annotation["disposition"],
                "oracle_requirement": annotation["oracle_requirement"],
                "main_factorial_eligible": annotation.get(
                    "factorial_eligible_override", annotation["disposition"] != "temporarily_unsuitable"
                ),
                "direct_historical_boundary_or_anachronism": annotation["direct_historical_boundary_or_anachronism"],
            }
        )

    (out / "item_audit.jsonl").write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in audited), encoding="utf-8"
    )
    fieldnames = list(audited[0])
    with (out / "item_audit.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in audited:
            serial = {key: json.dumps(value, ensure_ascii=False) if isinstance(value, list) else value for key, value in row.items()}
            writer.writerow(serial)
    (out / "revised_items_v2.jsonl").write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in revised), encoding="utf-8"
    )
    manifest = {
        "frozen_at_commit": "b06656f",
        "frozen_inputs": [file_record(path, root) for path in source_paths],
        "policy": "Original files are read-only; all revisions use new paths and parent_item_id.",
    }
    (out / "frozen_input_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    summary = {
        "items": len(audited),
        "dispositions": dict(Counter(row["disposition"] for row in audited)),
        "primary_constructs": dict(Counter(row["primary_construct"] for row in audited)),
        "direct_historical_boundary_or_anachronism": sum(
            row["direct_historical_boundary_or_anachronism"] for row in audited
        ),
        "ordinary_reading_controls": sum(row["disposition"] == "control_only" for row in audited),
        "factorial_eligible": sum(row["main_factorial_eligible"] for row in revised),
        "independence_groups": len({row["independence_group"] for row in audited}),
        "high_or_very_high_cue_risk": sum(row["cue_risk"].startswith(("high", "very_high")) for row in audited),
    }
    (out / "audit_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    disposition_zh = {
        "usable_directly": "可直接用于研究验证",
        "needs_revision": "需要修改",
        "control_only": "只能用作控制题",
        "temporarily_unsuitable": "暂不适合当前研究",
    }
    md = [
        "# 现有20题研究能力逐题审计表",
        "",
        "本表审计的是测量构念与公平可答性，不是第二轮独立史学核验。审计者仍为同一 Codex 项目链，`independent_review=false`。",
        "",
        "| 题号 | 主要测量目标 | 直接测历史边界/时代错置 | Oracle需要 | 提示风险 | 证据组 | 处置 | 关键判断 |",
        "|---|---|---:|---|---|---|---|---|",
    ]
    for row in audited:
        note = row["audit_note"].replace("|", "\\|")
        md.append(
            f"| {row['item_id']} | {row['primary_construct']} | "
            f"{'是' if row['direct_historical_boundary_or_anachronism'] else '否'} | "
            f"{row['oracle_requirement']} | {row['cue_risk']} | {row['independence_group']} | "
            f"{disposition_zh[row['disposition']]} | {note} |"
        )
    md.extend(
        [
            "",
            "## 汇总",
            "",
            f"- 直接测试历史知识边界或时代错置：{summary['direct_historical_boundary_or_anachronism']} 题（DFP-Q017）；其中直接测试截止日之后知识侵入：0 题。",
            f"- 普通文本阅读控制：{summary['ordinary_reading_controls']} 题。",
            "- 处置分布：可直接用于研究验证 10 题、需要修改 2 题、控制题 7 题、暂不适合 1 题。",
            f"- 统计独立性：20 题仅对应 {summary['independence_groups']} 个证据独立组。",
            f"- 高或很高措辞提示风险：{summary['high_or_very_high_cue_risk']} 题；修订稿已降低部分提示，但仍需独立复核。",
            "",
            "Q007 应另作图像—OCR多模态控制；Q012 的孤立证据没有交代发言者，补入上下文并重审前不进入主因子实验。Q016 的原金标准超出了核验摘录，修订稿只保留明矾与过滤。",
        ]
    )
    (out / "ITEM_AUDIT_REPORT.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
