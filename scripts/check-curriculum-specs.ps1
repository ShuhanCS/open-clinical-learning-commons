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

$module04 = Test-ModuleContract `
    -Label 'Module 04' `
    -SpecPath (Join-Path $repo 'docs\curriculum\courses\DA-730\modules\04-distributions-summaries-spec.md') `
    -ModuleRoot (Join-Path $repo 'courses\data-visualization\modules\04-distributions-vs-summaries') `
    -RequiredFiles @(
        'README.md',
        'data-spec.md',
        'source-record.yml',
        'build_cms_ed_calibration.R',
        'generate_ed_los.R',
        'validate_ed_los.R',
        'lab.R',
        'critique_charts.R',
        'assessment.md',
        'instructor-notes.md',
        'release.json',
        'data\cms_ed_op18b_2026.csv',
        'data\ed_los_2026.csv'
    )
if (
    $module04.Release.module.version -ne '0.4.0' -or
    $module04.Release.data.row_count -ne 8392 -or
    $module04.Release.calibration.row_count -ne 4658
) {
    throw 'DA-730 Module 04 release metadata does not match the 0.4.0, 8,392-encounter, 4,658-calibration-row contract.'
}

$module05 = Test-ModuleContract `
    -Label 'Module 05' `
    -SpecPath (Join-Path $repo 'docs\curriculum\courses\DA-730\modules\05-rates-denominators-adjustment-spec.md') `
    -ModuleRoot (Join-Path $repo 'courses\data-visualization\modules\05-rates-denominators-adjustment') `
    -RequiredFiles @(
        'README.md',
        'data-spec.md',
        'source-record.yml',
        'build_county_rates.py',
        'validate_county_rates.py',
        'lab.R',
        'critique_charts.R',
        'assessment.md',
        'instructor-notes.md',
        'release.json',
        'data\places_diabetes_county_2024.csv',
        'data\acs_adult_population_county_2024.csv',
        'data\nc_county_boundaries_2024.csv',
        'data\nc_diabetes_rates_2024.csv'
    )
if (
    $module05.Release.module.version -ne '0.1.0' -or
    $module05.Release.data.row_count -ne 100 -or
    $module05.Release.sources.cdc_places.row_count -ne 6290 -or
    $module05.Release.sources.census_acs.row_count -ne 3222 -or
    $module05.Release.sources.census_tigerweb.county_features -ne 100
) {
    throw 'DA-730 Module 05 release metadata does not match the 0.1.0 public-source county contract.'
}

$module06 = Test-ModuleContract `
    -Label 'Module 06' `
    -SpecPath (Join-Path $repo 'docs\curriculum\courses\DA-730\modules\06-uncertainty-variation-small-numbers-spec.md') `
    -ModuleRoot (Join-Path $repo 'courses\data-visualization\modules\06-uncertainty-variation-small-numbers') `
    -RequiredFiles @(
        'README.md',
        'data-spec.md',
        'source-record.yml',
        'build_hf_uncertainty.py',
        'validate_hf_uncertainty.py',
        'lab.R',
        'critique_charts.R',
        'assessment.md',
        'instructor-notes.md',
        'release.json',
        'data\cms_hf_readmission_hospitals_2026.csv',
        'data\cms_unplanned_national_2026.csv',
        'data\cms_footnote_crosswalk_2026.csv',
        'data\ma_hf_readmission_uncertainty_2026.csv'
    )
if (
    $module06.Release.module.version -ne '0.1.0' -or
    $module06.Release.module.commons_release -ne '0.17.0' -or
    $module06.Release.data.row_count -ne 65 -or
    $module06.Release.sources.cms_hospital.row_count -ne 4790 -or
    $module06.Release.sources.cms_national.row_count -ne 14 -or
    $module06.Release.sources.cms_footnotes.row_count -ne 32
) {
    throw 'DA-730 Module 06 release metadata does not match the 0.1.0 public-source uncertainty contract.'
}

$module07 = Test-ModuleContract `
    -Label 'Module 07' `
    -SpecPath (Join-Path $repo 'docs\curriculum\courses\DA-730\modules\07-color-accessible-communication-spec.md') `
    -ModuleRoot (Join-Path $repo 'courses\data-visualization\modules\07-color-accessible-communication') `
    -RequiredFiles @(
        'README.md',
        'data-spec.md',
        'source-record.yml',
        'build_accessibility_case.py',
        'validate_accessibility_case.py',
        'lab.R',
        'critique_charts.R',
        'assessment.md',
        'instructor-notes.md',
        'release.json',
        'data\accessibility_hf_readmission_2026.csv'
    )
if (
    $module07.Release.module.version -ne '0.1.0' -or
    $module07.Release.module.commons_release -ne '0.18.0' -or
    $module07.Release.data.row_count -ne 65 -or
    $module07.Release.data.column_count -ne 27 -or
    $module07.Release.data.sha256 -ne 'b58168d9002a3e489213b0fafde1eca76f5b1a426c71ea3d61551671d76a49c2' -or
    $module07.Release.validation.measured_results.reported_rows -ne 53 -or
    $module07.Release.validation.measured_results.minimum_contrast_on_white -ne 5.54
) {
    throw 'DA-730 Module 07 release metadata does not match the 0.1.0, 65-row accessibility contract.'
}

$module08 = Test-ModuleContract `
    -Label 'Module 08' `
    -SpecPath (Join-Path $repo 'docs\curriculum\courses\DA-730\modules\08-time-process-variation-spec.md') `
    -ModuleRoot (Join-Path $repo 'courses\data-visualization\modules\08-time-process-variation') `
    -RequiredFiles @(
        'README.md',
        'data-spec.md',
        'source-record.yml',
        'build_nhsn_time_series.py',
        'validate_nhsn_time_series.py',
        'lab.R',
        'critique_charts.R',
        'assessment.md',
        'instructor-notes.md',
        'release.json',
        'data\nhsn_hospital_capacity_jurisdiction_2024_2026.csv',
        'data\ma_hospital_capacity_time_2024_2026.csv'
    )
if (
    $module08.Release.module.version -ne '0.1.0' -or
    $module08.Release.module.commons_release -ne '0.19.0' -or
    $module08.Release.data.all_jurisdictions.row_count -ne 6208 -or
    $module08.Release.data.all_jurisdictions.column_count -ne 14 -or
    $module08.Release.data.all_jurisdictions.sha256 -ne '8a492c3d2d3dae07c42e89ef35ed714d23acab32596f42037dcf8dd0284531d1' -or
    $module08.Release.data.massachusetts.row_count -ne 94 -or
    $module08.Release.data.massachusetts.column_count -ne 21 -or
    $module08.Release.data.massachusetts.sha256 -ne '394d9b02d2cc9b4fbf0d9f415db3da6b04393dd9430816973e81fef86fb0e616' -or
    $module08.Release.validation.measured_results.date_gaps -ne 0 -or
    $module08.Release.validation.measured_results.reporting_coverage_minimum_pct -ne 67.05
) {
    throw 'DA-730 Module 08 release metadata does not match the 0.1.0 public-source time-series contract.'
}

$module09 = Test-ModuleContract `
    -Label 'Module 09' `
    -SpecPath (Join-Path $repo 'docs\curriculum\courses\DA-730\modules\09-comparison-small-multiples-spec.md') `
    -ModuleRoot (Join-Path $repo 'courses\data-visualization\modules\09-comparison-small-multiples') `
    -RequiredFiles @(
        'README.md',
        'data-spec.md',
        'source-record.yml',
        'build_places_comparison.py',
        'validate_places_comparison.py',
        'lab.R',
        'critique_charts.R',
        'assessment.md',
        'instructor-notes.md',
        'release.json',
        'data\places_county_comparison_2024.csv',
        'data\nc_county_health_profiles_2024.csv'
    )
if (
    $module09.Release.module.version -ne '0.1.0' -or
    $module09.Release.module.commons_release -ne '0.20.0' -or
    $module09.Release.data.national_selected.row_count -ne 31450 -or
    $module09.Release.data.national_selected.column_count -ne 16 -or
    $module09.Release.data.national_selected.sha256 -ne '2af5ce99fc7d66a18e95451084afc397e0f7392e9f1a2b5476377fd8811658d2' -or
    $module09.Release.data.north_carolina.row_count -ne 500 -or
    $module09.Release.data.north_carolina.column_count -ne 27 -or
    $module09.Release.data.north_carolina.sha256 -ne '33b7cfc1c2459f1bde29cee7c05141aa116da2e6f79faf82646961e5162a75a9' -or
    $module09.Release.validation.measured_results.counties_above_all_five_national_points -ne 54 -or
    $module09.Release.validation.measured_results.counties_at_or_below_all_five_national_points -ne 9
) {
    throw 'DA-730 Module 09 release metadata does not match the 0.1.0 public-source comparison contract.'
}

$checkpoint01Root = Join-Path $repo 'courses\data-visualization\checkpoints\01-visualization-judgment-dossier'
$checkpoint01Spec = Join-Path $repo 'docs\curriculum\courses\DA-730\checkpoints\01-visualization-judgment-dossier-spec.md'
$checkpoint01Files = @(
    'README.md',
    'assemble_checkpoint.ps1',
    'validate_checkpoint.py',
    'template\README.md',
    'template\selection-matrix.md',
    'template\critique-and-repair.md',
    'template\accessibility-check.md',
    'template\decision-brief.md',
    'template\ai-use.md',
    'template\source-records\comparison-source.yml',
    'template\source-records\distribution-source.yml',
    'template\source-records\rate-source.yml',
    'template\source-records\uncertainty-source.yml'
)
$checkpoint01Missing = @($checkpoint01Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $checkpoint01Root $_))
})
if (-not (Test-Path -LiteralPath $checkpoint01Spec) -or $checkpoint01Missing.Count -gt 0) {
    throw "DA-730 Checkpoint 1 is missing its specification or package files: $($checkpoint01Missing -join ', ')."
}
$checkpoint01Content = Get-Content -Raw -LiteralPath $checkpoint01Spec
if ([regex]::Matches($checkpoint01Content, '(?m)^## \d+\.').Count -ne 17) {
    throw 'DA-730 Checkpoint 1 must define 17 numbered contract sections.'
}
if ($checkpoint01Content -match '[—–]') {
    throw 'DA-730 Checkpoint 1 contains a Unicode em dash or en dash.'
}
& python (Join-Path $checkpoint01Root 'validate_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'DA-730 Checkpoint 1 validator self-check failed.'
}

Write-Output "DA-730 specification passed: $moduleCount modules, $hours hours, $checkpointCount checkpoints."
Write-Output "DA-730 $($module01.Label) passed: $($module01.Sections) contract sections and $($module01.FileCount) required files."
Write-Output "DA-730 $($module02.Label) passed: $($module02.Sections) contract sections and $($module02.FileCount) required files."
Write-Output "DA-730 $($module03.Label) passed: $($module03.Sections) contract sections and $($module03.FileCount) required files."
Write-Output "DA-730 $($module04.Label) passed: $($module04.Sections) contract sections and $($module04.FileCount) required files."
Write-Output "DA-730 $($module05.Label) passed: $($module05.Sections) contract sections and $($module05.FileCount) required files."
Write-Output "DA-730 $($module06.Label) passed: $($module06.Sections) contract sections and $($module06.FileCount) required files."
Write-Output "DA-730 $($module07.Label) passed: $($module07.Sections) contract sections and $($module07.FileCount) required files."
Write-Output "DA-730 $($module08.Label) passed: $($module08.Sections) contract sections and $($module08.FileCount) required files."
Write-Output "DA-730 $($module09.Label) passed: $($module09.Sections) contract sections and $($module09.FileCount) required files."
Write-Output "DA-730 Checkpoint 1 passed: 17 contract sections and $($checkpoint01Files.Count) package files."
