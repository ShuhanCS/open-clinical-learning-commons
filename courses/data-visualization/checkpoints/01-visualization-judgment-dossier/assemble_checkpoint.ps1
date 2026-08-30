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

$rscript = (Get-Command $RscriptPath -ErrorAction Stop).Source
$work = Join-Path ([System.IO.Path]::GetTempPath()) ("oclc-da730-cp1-" + [guid]::NewGuid().ToString('N'))
$figures = Join-Path $targetPath 'figures'
$analysis = Join-Path $targetPath 'analysis'
$records = Join-Path $targetPath 'source-records'

New-Item -ItemType Directory -Path $work, $figures, $analysis, $records | Out-Null

function Invoke-Lab {
    param([string[]] $Arguments)
    & $rscript @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "R lab failed with exit code $LASTEXITCODE."
    }
}

try {
    $m03 = Join-Path $repo 'courses\data-visualization\modules\03-chart-selection'
    $m04 = Join-Path $repo 'courses\data-visualization\modules\04-distributions-vs-summaries'
    $m05 = Join-Path $repo 'courses\data-visualization\modules\05-rates-denominators-adjustment'
    $m06 = Join-Path $repo 'courses\data-visualization\modules\06-uncertainty-variation-small-numbers'
    $m01Data = Join-Path $repo 'courses\data-visualization\modules\01-encoding-grammar\data\hcahps_ma_recommend_2026.csv'

    $out03 = Join-Path $work 'm03'
    $out04 = Join-Path $work 'm04'
    $out05 = Join-Path $work 'm05'
    $out06 = Join-Path $work 'm06'

    Invoke-Lab @(
        (Join-Path $m03 'lab.R'),
        (Join-Path $m03 'data\selection_cases_2026.csv'),
        $m01Data,
        $out03
    )
    Invoke-Lab @(
        (Join-Path $m04 'lab.R'),
        (Join-Path $m04 'data\ed_los_2026.csv'),
        $out04
    )
    Invoke-Lab @(
        (Join-Path $m05 'lab.R'),
        (Join-Path $m05 'data\nc_diabetes_rates_2024.csv'),
        $out05
    )
    Invoke-Lab @(
        (Join-Path $m06 'lab.R'),
        '--data',
        (Join-Path $m06 'data\ma_hf_readmission_uncertainty_2026.csv'),
        '--output',
        $out06
    )

    Copy-Item -LiteralPath (Join-Path $out03 '01-comparison-dot-plot.png') -Destination (Join-Path $figures 'comparison.png')
    Copy-Item -LiteralPath (Join-Path $out04 '03-density-by-disposition.png') -Destination (Join-Path $figures 'distribution.png')
    Copy-Item -LiteralPath (Join-Path $out05 '03-adjusted-with-denominator.png') -Destination (Join-Path $figures 'rate.png')
    Copy-Item -LiteralPath (Join-Path $out06 '02-interval-caterpillar.png') -Destination (Join-Path $figures 'uncertainty.png')

    Copy-Item -LiteralPath (Join-Path $m03 'lab.R') -Destination (Join-Path $analysis 'comparison.R')
    Copy-Item -LiteralPath (Join-Path $m04 'lab.R') -Destination (Join-Path $analysis 'distribution.R')
    Copy-Item -LiteralPath (Join-Path $m05 'lab.R') -Destination (Join-Path $analysis 'rate.R')
    Copy-Item -LiteralPath (Join-Path $m06 'lab.R') -Destination (Join-Path $analysis 'uncertainty.R')

    Copy-Item -Path (Join-Path $packageRoot 'template\*.md') -Destination $targetPath
    Copy-Item -Path (Join-Path $packageRoot 'template\source-records\*.yml') -Destination $records
} finally {
    if (Test-Path -LiteralPath $work) {
        Remove-Item -LiteralPath $work -Recurse -Force
    }
}

Write-Output "Assembled checkpoint starter: $targetPath"
Write-Output 'Complete the six Markdown templates, then run validate_checkpoint.py.'
