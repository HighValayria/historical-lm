# 访问探针摘要

执行命令：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File probes/data_access/probe_sources.ps1
```

第一次在沙箱内运行时出现远程连接错误；获得网络访问授权后，同一元数据级探针成功运行。

| 来源编号 | 状态 | HTTP | 内容类型 | 观察字节数 | 标题线索 | 原始元数据 |
|---|---|---:|---|---:|---|---|
| SRC-CUSTOMS-WELLCOME | 可访问 | 200 | text/html; charset=utf-8 | 533508 | Wellcome 海关医学报告汇编条目 | `data/raw/access_probe/SRC-CUSTOMS-WELLCOME_http_metadata.json` |
| SRC-CMMJ-CRL | 可访问 | 200 | text/html; charset=UTF-8 | 55786 | China Medical Missionary Journal，1894 | `data/raw/access_probe/SRC-CMMJ-CRL_http_metadata.json` |
| SRC-SMC-BNASIE | 可访问 | 200 | text/html; charset=utf-8 | 12306 | 1898 年报告与 1899 年预算 | `data/raw/access_probe/SRC-SMC-BNASIE_http_metadata.json` |
| SRC-CUSTOMS-AS | 可访问 | 200 | text/html; charset=UTF-8 | 20509 | 中研院海关资料入口 | `data/raw/access_probe/SRC-CUSTOMS-AS_http_metadata.json` |

## 解释

这些结果只证明入口页面可访问，不证明可以批量下载、OCR 复用或文本挖掘。下一步应做小规模、条款兼容的段落或 PDF/OCR 探针。
