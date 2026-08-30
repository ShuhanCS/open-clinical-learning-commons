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
$figures = Join-Path $targetPath 'figures'
$analysis = Join-Path $targetPath 'analysis'
$tables = Join-Path $targetPath 'evidence-tables'
$records = Join-Path $targetPath 'source-records'
$alternatives = Join-Path $targetPath 'alt-text'

New-Item -ItemType Directory -Path $figures, $analysis, $tables, $records, $alternatives | Out-Null
Copy-Item -Path (Join-Path $packageRoot 'template\*.md') -Destination $targetPath
Copy-Item -Path (Join-Path $packageRoot 'template\analysis\*.R') -Destination $analysis
Copy-Item -Path (Join-Path $packageRoot 'template\source-records\*.yml') -Destination $records

$artifacts = @(
    'accessible-display',
    'time-display',
    'comparison-display',
    'place-display',
    'structure-display',
    'dashboard'
)

Push-Location $repo
try {
    foreach ($artifact in $artifacts) {
        & $rscript (Join-Path $analysis "$artifact.R") $targetPath
        if ($LASTEXITCODE -ne 0) {
            throw "Checkpoint analysis $artifact failed with exit code $LASTEXITCODE."
        }
    }
} finally {
    Pop-Location
}

foreach ($artifact in $artifacts) {
    foreach ($relative in @(
        "figures\$artifact.png",
        "evidence-tables\$artifact.csv",
        "alt-text\$artifact.md"
    )) {
        $path = Join-Path $targetPath $relative
        if (-not (Test-Path -LiteralPath $path) -or (Get-Item -LiteralPath $path).Length -eq 0) {
            throw "Assembler did not create $relative."
        }
    }
}

Write-Output "Assembled Checkpoint 2 starter: $targetPath"
Write-Output 'Complete the eight Markdown templates, revise linked evidence when needed, then run validate_checkpoint.py.'
