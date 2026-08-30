$ErrorActionPreference = 'Stop'

$repo = Split-Path -Parent $PSScriptRoot
$da730 = Join-Path $repo 'docs\curriculum\courses\DA-730\course-spec.md'
$content = Get-Content -Raw -LiteralPath $da730

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

function Test-ModuleContract {
    param(
        [Parameter(Mandatory)] [string] $Label,
        [Parameter(Mandatory)] [string] $SpecPath,
        [Parameter(Mandatory)] [string] $ModuleRoot,
        [Parameter(Mandatory)] [string[]] $RequiredFiles
    )

    $missingFiles = @($RequiredFiles | Where-Object {
        -not (Test-Path -LiteralPath (Join-Path $ModuleRoot $_))
    })
    if ($missingFiles.Count -gt 0) {
        throw "DA-730 $Label is missing: $($missingFiles -join ', ')."
    }

    $moduleContent = Get-Content -Raw -LiteralPath $SpecPath
    $moduleSections = [regex]::Matches($moduleContent, '(?m)^## \d+\.').Count
    if ($moduleSections -ne 21) {
        throw "DA-730 $Label must define 21 contract sections; found $moduleSections."
    }
    if ($moduleContent -match '[—–]') {
        throw "DA-730 $Label contains a Unicode em dash or en dash."
    }

    [pscustomobject]@{
        Label = $Label
        Sections = $moduleSections
        FileCount = $RequiredFiles.Count
        Release = Get-Content -Raw -LiteralPath (Join-Path $ModuleRoot 'release.json') | ConvertFrom-Json
    }
}

$module01 = Test-ModuleContract `
    -Label 'Module 01' `
    -SpecPath (Join-Path $repo 'docs\curriculum\courses\DA-730\modules\01-encoding-grammar-spec.md') `
    -ModuleRoot (Join-Path $repo 'courses\data-visualization\modules\01-encoding-grammar') `
    -RequiredFiles @(
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
if ($module01.Release.module.version -ne '0.1.0' -or $module01.Release.data.row_count -ne 65) {
    throw 'DA-730 Module 01 release metadata does not match the 0.1.0, 65-row contract.'
}

$module02 = Test-ModuleContract `
    -Label 'Module 02' `
    -SpecPath (Join-Path $repo 'docs\curriculum\courses\DA-730\modules\02-perception-accuracy-spec.md') `
    -ModuleRoot (Join-Path $repo 'courses\data-visualization\modules\02-perception-accuracy') `
    -RequiredFiles @(
        'README.md',
        'data-spec.md',
        'source-record.yml',
        'build_perception_tasks.R',
        'validate_perception_tasks.R',
        'lab.R',
        'score_perception_test.R',
        'critique_charts.R',
        'assessment.md',
        'instructor-notes.md',
        'release.json',
        'data\perception_tasks_2026.csv'
    )
if ($module02.Release.module.version -ne '0.1.0' -or $module02.Release.data.task_rows -ne 10) {
    throw 'DA-730 Module 02 release metadata does not match the 0.1.0, 10-task contract.'
}

$module03 = Test-ModuleContract `
    -Label 'Module 03' `
    -SpecPath (Join-Path $repo 'docs\curriculum\courses\DA-730\modules\03-chart-selection-spec.md') `
    -ModuleRoot (Join-Path $repo 'courses\data-visualization\modules\03-chart-selection') `
    -RequiredFiles @(
        'README.md',
        'data-spec.md',
        'source-record.yml',
        'build_selection_cases.R',
        'validate_selection_cases.R',
        'lab.R',
        'critique_charts.R',
        'assessment.md',
        'instructor-notes.md',
        'release.json',
        'data\selection_cases_2026.csv'
    )
if ($module03.Release.module.version -ne '0.1.0' -or $module03.Release.data.case_rows -ne 10) {
    throw 'DA-730 Module 03 release metadata does not match the 0.1.0, 10-case contract.'
}

Write-Output "DA-730 specification passed: $moduleCount modules, $hours hours, $checkpointCount checkpoints."
Write-Output "DA-730 $($module01.Label) passed: $($module01.Sections) contract sections and $($module01.FileCount) required files."
Write-Output "DA-730 $($module02.Label) passed: $($module02.Sections) contract sections and $($module02.FileCount) required files."
Write-Output "DA-730 $($module03.Label) passed: $($module03.Sections) contract sections and $($module03.FileCount) required files."
