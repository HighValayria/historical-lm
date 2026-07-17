# Concept and Gap Map

## Working Concepts

| Concept | Working definition | Operational signal | Risk or ambiguity | Evidence status |
|---|---|---|---|---|
| Historical knowledge boundary | The project-specific limit of what a defined historical actor, source ecology, or model/RAG system may responsibly claim for a specified date. It combines chronology, source circulation, provenance, archival survival, and accessibility. | Every benchmark item should include `target_date`, `source_date`, `source_family`, `audience`, `place`, and `evidence_status`. Answers should be penalized for post-cutoff entities or for presenting inaccessible knowledge as generally available. | A fact can be true today but unavailable or unattested in the target source ecology. | synthesis from temporal NLP, source criticism, and historiography |
| Knowledge accessibility | Whether a claim could plausibly have been available to a defined community through language, publication channels, institutions, geography, literacy, and professional networks. | Tag the imagined knower: treaty-port physician, missionary, customs officer, Qing official, newspaper reader, merchant, rural patient, etc. Separate global discovery date from local attestation. | Easy-to-digitize foreign-language archives can be mistaken for the whole historical knowledge world. | conceptual inference |
| Archival bias | Non-random production, survival, cataloguing, digitization, OCR, and retrieval of sources. Archives are not neutral mirrors of the past. | For each item, record creator, institution, genre, digitization path, OCR status, missing groups, and likely overrepresented voices. Stratify evaluation by source family. | Absence from a corpus is not absence from the past. | supported by archival studies and DH source criticism |
| Historical ignorance | A historically appropriate state of "unknown", "unattested", "not yet discovered", "not locally accessible", or "not supported by this corpus". | Include answer labels: `known`, `uncertain`, `not_attested`, `post_cutoff`, `not_accessible_to_actor`, `insufficient_evidence`. Score calibrated abstention. | Standard QA metrics may wrongly punish historically careful refusal. | conceptual inference from benchmark and historiographic needs |
| Factual anachronism | Importing later events, discoveries, institutions, names, policies, or technologies into a pre-cutoff answer. | Temporal entity check; cutoff contradiction; post-1900 terms/institutions in actor-level answers. | Modern biomedical correctness can hide historical error. | direct from anachronism taxonomy |
| Lexical anachronism | Using a word, translation, or semantic field as if its modern meaning were already stable in the target period. | Time-sliced lexicon; first-attestation notes; source-backed translations; flag terms whose meanings changed. | Normalizing `weisheng` as modern "public health" can flatten conceptual change. | supported by late-Qing public-health scholarship |
| Causal anachronism | Explaining earlier actions by later theories, outcomes, or teleological narratives rather than period-plausible causal frames. | Flag causal chains relying on later biomedical discoveries or modernization endpoints; require source-backed actor explanations. | Some later analytic categories are legitimate if clearly marked as analyst framing. | supported by anti-Whig/presentism concerns |
| Value anachronism | Attributing present-day moral, scientific, bureaucratic, or policy categories to historical actors without contextual framing. | Separate analyst judgment from actor categories; annotate present-day labels as analytical, not actor-level. | Contextualization should not become moral evasion; benchmark prompts must distinguish analysis from actor voice. | supported by historiographic method |
| Source misattribution | Attaching an atomic claim to the wrong source, date, author, genre, passage, or source family, or citing a passage that does not support the claim. | Passage-level citation check; source-date consistency; atomic claim support labels. | Fluent citation language can create false confidence. | supported by attribution/NLG literature |
| Provenance uncertainty | Uncertainty about source origin, date, authorship, edition, custodial path, OCR, transcription, or modern editorial intervention. | Metadata confidence score; edition/date confidence; OCR confidence; provenance caveat required in answer. | Digitization date or library metadata can be mistaken for historical circulation date. | supported by source criticism |
| Presentism | A broader interpretive habit of reading the past through present categories, endpoints, and priorities. It may be unavoidable as an analytic starting point but must be declared. | Penalize actor-level attribution of present categories; allow explicit present-day meta-analysis when the prompt asks for it. | The research project itself is present-driven, so prompts must state whether they ask for actor-level reconstruction or present-day analysis. | supported by historiography |

## Benchmark Label Schema Draft

| Field | Values | Purpose |
|---|---|---|
| `claim_type` | factual, lexical, causal, value, attribution, provenance | Separates error modes that would otherwise collapse into generic wrongness. |
| `temporal_status` | pre_cutoff_supported, pre_cutoff_uncertain, post_cutoff, mixed, undated | Records relation to 1900-01-01. |
| `accessibility_status` | accessible_to_named_actor, accessible_to_source_ecology, globally_known_not_local, not_attested, inaccessible | Prevents global historical knowledge from being attributed to all actors. |
| `source_population` | customs, missionary, municipal, newspaper, periodical, gazetteer, central_archive, secondary | Makes archival population explicit. |
| `answer_policy` | answer_with_citation, answer_with_caveat, abstain, reject_anachronism | Converts concepts into scoring behavior. |

## Core Concept Sources

| Source ID | Source | Relevance | Verification status |
|---|---|---|---|
| CONCEPT-SKINNER | Quentin Skinner, "Meaning and Understanding in the History of Ideas", DOI: 10.2307/2504188 | Supports attention to historical meaning and context rather than projecting present concepts. | verified by DOI metadata pattern; close reading recommended |
| CONCEPT-BUTTERFIELD | Herbert Butterfield, *The Whig Interpretation of History* | Supports anti-teleological caution. | public online edition exists; use as historiographic reference |
| CONCEPT-SCHWARTZ-COOK | Joan M. Schwartz and Terry Cook, "Archives, Records, and Power", DOI: 10.1007/BF02435628 | Supports the claim that archives are shaped by power and are not neutral repositories. | verified by DOI metadata pattern |
| CONCEPT-HARRIS | Verne Harris, "The Archival Sliver", DOI: 10.1023/A:1020813214144 | Supports archival partiality and survival limitations. | verified by DOI metadata pattern |
| CONCEPT-PUTNAM | Lara Putnam, "The Transnational and the Text-Searchable", DOI: 10.1093/ahr/121.2.377 | Supports caution that digitized search changes historical practice and visibility. | verified by DOI metadata pattern |
| CONCEPT-GIBBS-OWENS | Fred Gibbs and Trevor Owens, "The Hermeneutics of Data and Historical Writing", DOI: 10.2307/j.ctv65sx57.18 | Supports interpreting data as constructed evidence rather than raw fact. | verified by DOI metadata pattern |
| CONCEPT-RASHKIN | Rashkin et al., "Measuring Attribution in Natural Language Generation Models", DOI: 10.1162/coli_a_00486 | Supports passage-level attribution as an evaluation concern. | verified by DOI metadata pattern |
| CONCEPT-GAO | Gao et al., "Enabling Large Language Models to Generate Text with Citations", DOI: 10.18653/v1/2023.emnlp-main.398 | Supports citation generation and attribution evaluation concerns. | verified by ACL DOI pattern |
