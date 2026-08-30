param(
    [Parameter(Mandatory)] [string] $Target,
    [string] $RscriptPath = 'Rscript'
)

$ErrorActionPreference = 'Stop'

$packageRoot = $PSScriptRoot
$repo = (Resolve-Path -LiteralPath (Join-Path $packageRoot '..\..\..\..')).Path
$targetPath = if ([System.IO.Path]::IsPathRooted($Target)) {
    [System.IO.Path]::GetFullPath($Target)
} else {
    [System.IO.Path]::GetFullPath((Join-Path (Get-Location) $Target))
}

if (Test-Path -LiteralPath $targetPath) {
    if ((Get-ChildItem -LiteralPath $targetPath -Force | Select-Object -First 1)) {
        throw "Target must be absent or empty: $targetPath"
    }
} else {
    New-Item -ItemType Directory -Path $targetPath | Out-Null
}

$analysis = Join-Path $targetPath 'analysis'
$data = Join-Path $targetPath 'data'
$defense = Join-Path $targetPath 'defense'
New-Item -ItemType Directory -Path $analysis, $data, $defense | Out-Null

Copy-Item -LiteralPath (Join-Path $packageRoot 'render_decision_story.R') -Destination (Join-Path $analysis 'analysis.R')
Copy-Item -Path (Join-Path $packageRoot 'template\*.md') -Destination $targetPath
Copy-Item -Path (Join-Path $packageRoot 'template\*.yml') -Destination $targetPath
Copy-Item -Path (Join-Path $packageRoot 'template\defense\*.md') -Destination $defense

$upstreamData = Join-Path $repo 'courses\data-visualization\modules\12-dashboards-multi-view-composition\data'
foreach ($name in @(
    'ma_ed_public_reporting_dashboard_2026.csv',
    'ed_dashboard_measure_dictionary_2026.csv',
    'cms_ma_ed_dashboard_source_2026.csv'
)) {
    Copy-Item -LiteralPath (Join-Path $upstreamData $name) -Destination (Join-Path $data $name)
}

$rscript = (Get-Command $RscriptPath -ErrorAction Stop).Source
& $rscript (Join-Path $analysis 'analysis.R') --output $targetPath
if ($LASTEXITCODE -ne 0) {
    throw "Final checkpoint analysis failed with exit code $LASTEXITCODE."
}

foreach ($relative in @('figure-primary.png', 'figure-supporting.png', 'accessible-table.csv')) {
    $path = Join-Path $targetPath $relative
    if (-not (Test-Path -LiteralPath $path) -or (Get-Item -LiteralPath $path).Length -eq 0) {
        throw "Assembler did not create $relative."
    }
}

Write-Output "Assembled DA-730 final checkpoint starter: $targetPath"
Write-Output 'Complete every learner record, export defense/slides.pdf, complete the defense, record the review disposition, then run validate_checkpoint.py.'
