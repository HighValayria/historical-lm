param(
    [string]$Source = 'D:\Resources\historical_lm_exploration_starter',
    [string]$Target = 'D:\Resources\llm-historical-anachronism',
    [switch]$Execute
)

$ErrorActionPreference = 'Stop'

if (-not (Test-Path -LiteralPath $Source)) {
    throw "Source does not exist: $Source"
}
if (Test-Path -LiteralPath $Target) {
    throw "Target already exists: $Target"
}
$resolvedSource = (Resolve-Path -LiteralPath $Source).Path
if ($resolvedSource -ne $Source) {
    throw "Unexpected resolved source: $resolvedSource"
}
if (-not (Test-Path -LiteralPath (Join-Path $Source '.git'))) {
    throw "Source is not the expected Git repository: $Source"
}
$current = (Get-Location).Path
if ($current.StartsWith($Source, [System.StringComparison]::OrdinalIgnoreCase)) {
    throw 'Run this script from D:\Resources after closing Codex/Obsidian processes using the old directory.'
}

$status = git -C $Source status --porcelain
if ($LASTEXITCODE -ne 0) {
    throw 'Unable to read Git status.'
}
if ($status) {
    throw "Working tree is not clean:`n$status"
}
$localHead = git -C $Source rev-parse HEAD
$remoteHead = git -C $Source rev-parse origin/main
if ($localHead -ne $remoteHead) {
    throw "Local HEAD ($localHead) differs from origin/main ($remoteHead)."
}

if (-not $Execute) {
    [pscustomobject]@{
        ready = $true
        source = $Source
        target = $Target
        head = $localHead
        instruction = "Close the current Codex workspace, open PowerShell in D:\Resources, then rerun with -Execute."
    } | ConvertTo-Json
    exit 0
}

Rename-Item -LiteralPath $Source -NewName ([System.IO.Path]::GetFileName($Target))
if ((Test-Path -LiteralPath $Source) -or -not (Test-Path -LiteralPath $Target)) {
    throw 'Directory rename verification failed.'
}

$manifest = Join-Path $Target 'reports\migration\pre_migration_manifest.json'
$verification = Join-Path $Target 'reports\migration\post_rename_verification.json'
python (Join-Path $Target 'scripts\verify_repository_migration.py') `
    --root $Target `
    --manifest $manifest `
    --output $verification
if ($LASTEXITCODE -ne 0) {
    throw 'Post-rename repository verification failed.'
}

[pscustomobject]@{
    completed = $true
    source_exists = Test-Path -LiteralPath $Source
    target_exists = Test-Path -LiteralPath $Target
    head = git -C $Target rev-parse HEAD
    origin = git -C $Target remote get-url origin
    verification = $verification
    next_action = 'Re-add/open the new path in Codex and retarget the paused automation to the new project.'
} | ConvertTo-Json
