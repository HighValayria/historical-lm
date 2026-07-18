# OCR 与元数据探针摘要

执行命令：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File probes/ocr/probe_text_signals.ps1
```

| 来源编号 | 元数据分数 | 文本信号分数 | 可跟进性 | 关键信号 |
|---|---:|---:|---|---|
| SRC-CUSTOMS-WELLCOME | 3 | 3 | 高 | PDF、下载、IIIF 信号；候选 PDF 为 `https://iiif.wellcomecollection.org/pdf/b20416179`；检测到 Public Domain Mark 链接 |
| SRC-CMMJ-CRL | 3 | 3 | 高 | 下载和 IIIF 信号；检测到文件/下载区域 |
| SRC-SMC-BNASIE | 3 | 2 | 中 | PDF 与全文信号；候选 PDF 为 `https://www.bnasie.eu/Asset/Source/bnPeriodical_ID-60_No-1.pdf` |
| SRC-CUSTOMS-AS | 3 | 0 | 低 | 有元数据和权利说明信号，但入口页没有被正则探针识别出直接 PDF、全文、下载或 IIIF 链接 |

## 解释

简单关键词探针没有在任何页面上发现明确 OCR 信号。Wellcome 与 CRL 最适合下一步条目级跟进；bnAsie 可尝试 PDF 文本抽取；中研院海关入口需要人工导航或接口说明。
