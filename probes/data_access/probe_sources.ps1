param(
    [string]$OutDir = "probes/data_access",
    [string]$RawDir = "data/raw/access_probe"
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

New-Item -ItemType Directory -Force -Path $OutDir, $RawDir | Out-Null

$sources = @(
    @{
        id = "SRC-CUSTOMS-WELLCOME"
        url = "https://wellcomecollection.org/works/za7rnxwq"
        expected = "Wellcome item page for C. A. Gordon customs medical reports epitome"
    },
    @{
        id = "SRC-CMMJ-CRL"
        url = "https://digitalcollections.crl.edu/record/370733?ln=en&v=uv"
        expected = "CRL record for China Medical Missionary Journal"
    },
    @{
        id = "SRC-SMC-BNASIE"
        url = "https://www.bnasie.eu/BN/Periodicals?ID=60"
        expected = "bnAsie Shanghai Municipal Council annual report page"
    },
    @{
        id = "SRC-CUSTOMS-AS"
        url = "https://mhdb.mh.sinica.edu.tw/customs/web/"
        expected = "Academia Sinica Chinese Maritime Customs database landing page"
    }
)

function Get-Sha256Hex {
    param([byte[]]$Bytes)
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        return (($sha.ComputeHash($Bytes) | ForEach-Object { $_.ToString("x2") }) -join "")
    }
    finally {
        $sha.Dispose()
    }
}

$results = foreach ($source in $sources) {
    $record = [ordered]@{
        id = $source.id
        url = $source.url
        expected = $source.expected
        probed_at = (Get-Date).ToString("o")
        status = "not_started"
        http_status = $null
        content_type = $null
        content_length_header = $null
        observed_bytes = $null
        sha256 = $null
        title = $null
        raw_metadata_file = $null
        error = $null
    }

    try {
        $response = Invoke-WebRequest -Uri $source.url -UseBasicParsing -TimeoutSec 30 -Headers @{
            "User-Agent" = "historical-lm-access-probe/0.1 (metadata-only)"
        }
        $bytes = [System.Text.Encoding]::UTF8.GetBytes([string]$response.Content)
        $titleMatch = [regex]::Match([string]$response.Content, "<title[^>]*>(.*?)</title>", "IgnoreCase,Singleline")
        $title = if ($titleMatch.Success) {
            ($titleMatch.Groups[1].Value -replace "\s+", " ").Trim()
        } else {
            $null
        }

        $headers = [ordered]@{}
        foreach ($key in $response.Headers.Keys) {
            $headers[$key] = [string]$response.Headers[$key]
        }

        $rawMetadata = [ordered]@{
            id = $source.id
            url = $source.url
            probed_at = $record.probed_at
            status_code = [int]$response.StatusCode
            headers = $headers
            title = $title
            sha256 = Get-Sha256Hex -Bytes $bytes
            observed_bytes = $bytes.Length
            note = "Metadata-only access probe; response body was not persisted."
        }

        $rawPath = Join-Path $RawDir ($source.id + "_http_metadata.json")
        $rawMetadata | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $rawPath -Encoding UTF8

        $record.status = "reachable"
        $record.http_status = [int]$response.StatusCode
        $record.content_type = [string]$response.Headers["Content-Type"]
        $record.content_length_header = [string]$response.Headers["Content-Length"]
        $record.observed_bytes = $bytes.Length
        $record.sha256 = $rawMetadata.sha256
        $record.title = $title
        $record.raw_metadata_file = $rawPath
    }
    catch {
        $record.status = "failed"
        $record.error = $_.Exception.Message
    }

    [pscustomobject]$record
}

$results | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $OutDir "access_probe_results.json") -Encoding UTF8
$results | Format-Table id, status, http_status, content_type, observed_bytes, title -AutoSize
