$ErrorActionPreference = 'Stop'

$repo = Split-Path -Parent $PSScriptRoot
$da730 = Join-Path $repo 'docs\curriculum\courses\DA-730\course-spec.md'
$content = Get-Content -Raw -LiteralPath $da730
$module01Spec = Join-Path $repo 'docs\curriculum\courses\DA-730\modules\01-encoding-grammar-spec.md'
$module01Root = Join-Path $repo 'courses\data-visualization\modules\01-encoding-grammar'

$moduleCount = [regex]::Matches($content, '(?m)^## Module \d{2} brief:').Count
if ($moduleCount -ne 13) {
    throw "DA-730 must define 13 module briefs; found $moduleCount."
}

$hourMatches = [regex]::Matches(
    $content,
    '(?m)^\| \d{2} \| [^|]+ \| \d+ \| (?<hours>\d+(?:\.\d+)?) \|'
)
$hours = ($hourMatches | ForEach-Object { [decimal]$_.Groups['hours'].Value } | Measure-Object -Sum).Sum
if ($hours -ne [decimal]112.5) {
    throw "DA-730 module hours must total 112.5; found $hours."
}

$checkpointCount = [regex]::Matches($content, '(?m)^## (?:Checkpoint \d|Final checkpoint):').Count
if ($checkpointCount -ne 3) {
    throw "DA-730 must define three checkpoints; found $checkpointCount."
}

if ($content -match '[—–]') {
    throw 'DA-730 contains a Unicode em dash or en dash.'
}

$requiredModule01Files = @(
    'README.md',
    'data-spec.md',
    'source-record.yml',
    'build_hcahps.R',
    'validate_hcahps.R',
    'lab.R',
    'critique_charts.R',
    'assessment.md',
    'instructor-notes.md',
    'release.json',
    'data\hcahps_ma_recommend_2026.csv'
)
$missingModule01Files = @($requiredModule01Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $module01Root $_))
})
if ($missingModule01Files.Count -gt 0) {
    throw "DA-730 Module 01 is missing: $($missingModule01Files -join ', ')."
}

$module01Content = Get-Content -Raw -LiteralPath $module01Spec
$module01Sections = [regex]::Matches($module01Content, '(?m)^## \d+\.').Count
if ($module01Sections -ne 21) {
    throw "DA-730 Module 01 must define 21 contract sections; found $module01Sections."
}
if ($module01Content -match '[—–]') {
    throw 'DA-730 Module 01 contains a Unicode em dash or en dash.'
}

$module01Release = Get-Content -Raw -LiteralPath (Join-Path $module01Root 'release.json') | ConvertFrom-Json
if ($module01Release.module.version -ne '0.1.0' -or $module01Release.data.row_count -ne 65) {
    throw 'DA-730 Module 01 release metadata does not match the 0.1.0, 65-row contract.'
}

Write-Output "DA-730 specification passed: $moduleCount modules, $hours hours, $checkpointCount checkpoints."
Write-Output "DA-730 Module 01 passed: $module01Sections contract sections and $($requiredModule01Files.Count) required files."
