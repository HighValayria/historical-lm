param(
    [string]$AccessResults = "probes/data_access/access_probe_results.json",
    [string]$OutDir = "probes/ocr"
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

$access = Get-Content -Raw -LiteralPath $AccessResults | ConvertFrom-Json
$sources = $access | Where-Object { $_.status -eq "reachable" }

$keywordPatterns = [ordered]@{
    pdf = "(?i)\bpdf\b"
    ocr = "(?i)\bocr\b"
    full_text = "(?i)full\s*text|全文"
    download = "(?i)download|下载"
    iiif = "(?i)iiif|manifest"
    rights = "(?i)rights|license|licence|copyright|public domain|terms|使用|版權|版权"
    date = "(?i)\b18[0-9]{2}\b|\b19[0-9]{2}\b|year|date|出版|年份"
    title = "(?i)<title|title|題名|题名"
}

function Resolve-Link {
    param([string]$BaseUrl, [string]$Href)
    try {
        return ([System.Uri]::new([System.Uri]$BaseUrl, $Href)).AbsoluteUri
    }
    catch {
        return $Href
    }
}

$results = foreach ($source in $sources) {
    $record = [ordered]@{
        id = $source.id
        url = $source.url
        probed_at = (Get-Date).ToString("o")
        status = "not_started"
        http_status = $null
        keyword_counts = [ordered]@{}
        candidate_links = @()
        metadata_score = 0
        text_signal_score = 0
        feasibility = "unknown"
        notes = @()
        error = $null
    }

    try {
        $response = Invoke-WebRequest -Uri $source.url -UseBasicParsing -TimeoutSec 30 -Headers @{
            "User-Agent" = "historical-lm-ocr-metadata-probe/0.1 (link-signals-only)"
        }
        $html = [string]$response.Content
        $record.http_status = [int]$response.StatusCode

        foreach ($name in $keywordPatterns.Keys) {
            $record.keyword_counts[$name] = ([regex]::Matches($html, $keywordPatterns[$name])).Count
        }

        $links = [regex]::Matches($html, "<a\s+[^>]*href\s*=\s*[""']([^""']+)[""'][^>]*>(.*?)</a>", "IgnoreCase,Singleline")
        $candidateLinks = foreach ($match in $links) {
            $href = $match.Groups[1].Value
            $text = (($match.Groups[2].Value -replace "<[^>]+>", " ") -replace "\s+", " ").Trim()
            $combined = "$href $text"
            if ($combined -match "(?i)pdf|download|full\s*text|ocr|iiif|manifest|view|read|content|file|全文|下载") {
                [pscustomobject]@{
                    href = Resolve-Link -BaseUrl $source.url -Href $href
                    text = $text
                }
            }
        }
        $record.candidate_links = @($candidateLinks | Select-Object -First 25)

        if ($record.keyword_counts.title -gt 0) { $record.metadata_score += 1 }
        if ($record.keyword_counts.date -gt 0) { $record.metadata_score += 1 }
        if ($record.keyword_counts.rights -gt 0) { $record.metadata_score += 1 }
        if ($record.keyword_counts.pdf -gt 0) { $record.text_signal_score += 1 }
        if ($record.keyword_counts.full_text -gt 0) { $record.text_signal_score += 1 }
        if ($record.keyword_counts.download -gt 0) { $record.text_signal_score += 1 }
        if ($record.keyword_counts.iiif -gt 0) { $record.text_signal_score += 1 }
        if ($record.keyword_counts.ocr -gt 0) { $record.text_signal_score += 1 }

        if ($record.text_signal_score -ge 3) {
            $record.feasibility = "high_for_followup"
        }
        elseif ($record.text_signal_score -ge 1) {
            $record.feasibility = "medium_for_followup"
        }
        else {
            $record.feasibility = "low_without_manual_navigation"
        }

        if ($record.keyword_counts.ocr -eq 0) {
            $record.notes += "No explicit OCR keyword signal found on page."
        }
        if ($record.keyword_counts.rights -gt 0) {
            $record.notes += "Rights/terms language detected; review before reuse."
        }
        if (@($record.candidate_links).Count -eq 0) {
            $record.notes += "No candidate full-text/download links detected by regex."
        }

        $record.status = "probed"
    }
    catch {
        $record.status = "failed"
        $record.error = $_.Exception.Message
    }

    [pscustomobject]$record
}

$outPath = Join-Path $OutDir "ocr_metadata_probe_results.json"
$results | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $outPath -Encoding UTF8
$results | Format-Table id, status, metadata_score, text_signal_score, feasibility -AutoSize
