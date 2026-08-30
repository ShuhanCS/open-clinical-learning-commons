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

$module10 = Test-ModuleContract `
    -Label 'Module 10' `
    -SpecPath (Join-Path $repo 'docs\curriculum\courses\DA-730\modules\10-maps-geography-place-spec.md') `
    -ModuleRoot (Join-Path $repo 'courses\data-visualization\modules\10-maps-geography-place') `
    -RequiredFiles @(
        'README.md',
        'data-spec.md',
        'source-record.yml',
        'build_place_access_case.py',
        'validate_place_access_case.py',
        'lab.R',
        'critique_charts.R',
        'assessment.md',
        'instructor-notes.md',
        'release.json',
        'data\hpsa_primary_care_nc_2026_08_29.csv',
        'data\nc_place_access_2026.csv',
        'data\nc_county_boundaries_2024.csv'
    )
if (
    $module10.Release.module.version -ne '0.1.0' -or
    $module10.Release.module.commons_release -ne '0.21.0' -or
    $module10.Release.data.hpsa_selected.row_count -ne 1546 -or
    $module10.Release.data.hpsa_selected.column_count -ne 28 -or
    $module10.Release.data.hpsa_selected.sha256 -ne '061fe5e18bc9cd58bd89256c686ddefbce6d77972c1139b1b339497f2eab5445' -or
    $module10.Release.data.teaching.row_count -ne 100 -or
    $module10.Release.data.teaching.column_count -ne 29 -or
    $module10.Release.data.teaching.sha256 -ne '90a575f03bc94cc0eb336d263e3f9d8afe09cf68ddb95476bf1836c0574f9a07' -or
    $module10.Release.data.boundaries.row_count -ne 7121 -or
    $module10.Release.data.boundaries.column_count -ne 6 -or
    $module10.Release.data.boundaries.sha256 -ne '6eb085f49b400d4ecf6f88646f51dd01fdd4154533262e66ade02b1d1d8f666f' -or
    $module10.Release.validation.measured_results.active_hpsa_rows -ne 740 -or
    $module10.Release.validation.measured_results.both_screen_conditions -ne 19 -or
    $module10.Release.validation.measured_results.reference_shortlist -ne 12
) {
    throw 'DA-730 Module 10 release metadata does not match the 0.1.0 public-source place contract.'
}

$module11 = Test-ModuleContract `
    -Label 'Module 11' `
    -SpecPath (Join-Path $repo 'docs\curriculum\courses\DA-730\modules\11-flow-networks-composition-hierarchy-spec.md') `
    -ModuleRoot (Join-Path $repo 'courses\data-visualization\modules\11-flow-networks-composition-hierarchy') `
    -RequiredFiles @(
        'README.md',
        'data-spec.md',
        'source-record.yml',
        'build_transition_case.py',
        'validate_transition_case.py',
        'lab.R',
        'critique_charts.R',
        'assessment.md',
        'instructor-notes.md',
        'release.json',
        'data\synthea_patients_transition_source_2020.csv',
        'data\synthea_encounters_transition_source_2020.csv',
        'data\synthea_acute_transition_cohort_2020.csv',
        'data\synthea_transition_edges_2020.csv'
    )
if (
    $module11.Release.module.version -ne '0.1.0' -or
    $module11.Release.module.commons_release -ne '0.22.0' -or
    $module11.Release.data.patients.row_count -ne 1171 -or
    $module11.Release.data.patients.column_count -ne 6 -or
    $module11.Release.data.patients.sha256 -ne 'a208fe4ff6fc9dc5cee4a201043a2f059943b8c058fdb191e19b0f9ffbb821bf' -or
    $module11.Release.data.encounters.row_count -ne 53346 -or
    $module11.Release.data.encounters.column_count -ne 9 -or
    $module11.Release.data.encounters.sha256 -ne '00298bf68f89dee9734cf133c516ad6b7efe95c8cd15a9458e7fb09c1dca56ce' -or
    $module11.Release.data.cohort.row_count -ne 374 -or
    $module11.Release.data.cohort.column_count -ne 25 -or
    $module11.Release.data.cohort.sha256 -ne 'b3f1cf69a54fd2f38dfe6debfd009ebb1c7d2b1ef7b42d7b35c989a9f068f3ca' -or
    $module11.Release.data.edges.row_count -ne 15 -or
    $module11.Release.data.edges.column_count -ne 9 -or
    $module11.Release.data.edges.sha256 -ne '13ee29b6fb6e16235cb3b9509d72f95a6b478024a7322d011bb04a4e8064fa8d' -or
    $module11.Release.validation.measured_results.cohort_patients -ne 374 -or
    $module11.Release.validation.measured_results.acute_return_90d -ne 36 -or
    $module11.Release.validation.measured_results.priority_path_patients -ne 38
) {
    throw 'DA-730 Module 11 release metadata does not match the 0.1.0 synthetic transition contract.'
}

$module12 = Test-ModuleContract `
    -Label 'Module 12' `
    -SpecPath (Join-Path $repo 'docs\curriculum\courses\DA-730\modules\12-dashboards-multi-view-composition-spec.md') `
    -ModuleRoot (Join-Path $repo 'courses\data-visualization\modules\12-dashboards-multi-view-composition') `
    -RequiredFiles @(
        'README.md',
        'data-spec.md',
        'source-record.yml',
        'build_ed_dashboard_case.py',
        'validate_ed_dashboard_case.py',
        'lab.R',
        'critique_charts.R',
        'assessment.md',
        'instructor-notes.md',
        'release.json',
        'data\cms_ma_ed_dashboard_source_2026.csv',
        'data\ma_ed_public_reporting_dashboard_2026.csv',
        'data\ed_dashboard_measure_dictionary_2026.csv'
    )
if (
    $module12.Release.module.version -ne '0.1.0' -or
    $module12.Release.module.commons_release -ne '0.23.0' -or
    $module12.Release.source.full_rows -ne 138084 -or
    $module12.Release.source.full_columns -ne 16 -or
    $module12.Release.source.full_sha256 -ne '1e5a1ca803c2b09468fe3ae3fe60fef3e910f5f5300630a24791c88a1abff516' -or
    $module12.Release.data.source_selection.row_count -ne 186 -or
    $module12.Release.data.source_selection.column_count -ne 15 -or
    $module12.Release.data.source_selection.facility_count -ne 62 -or
    $module12.Release.data.source_selection.sha256 -ne 'f28f5d56e5e0e29001c7a275b01306762e673c9a21459dc7a68ff1aea782943b' -or
    $module12.Release.data.teaching.row_count -ne 186 -or
    $module12.Release.data.teaching.column_count -ne 31 -or
    $module12.Release.data.teaching.facility_count -ne 62 -or
    $module12.Release.data.teaching.sha256 -ne 'fbfcfcaf10d87cd48236a702622781f559d86d52b8773ca578d72313a9b270fd' -or
    $module12.Release.data.measure_dictionary.row_count -ne 3 -or
    $module12.Release.data.measure_dictionary.column_count -ne 18 -or
    $module12.Release.data.measure_dictionary.sha256 -ne '2db834a350c0fee342efb30fc4b028053e325b3b357cc1031a11f7c9e9b29412' -or
    $module12.Release.validation.measured_results.selected_op22_pct -ne 23 -or
    $module12.Release.validation.measured_results.selected_op18b_minutes -ne 188 -or
    $module12.Release.validation.measured_results.op22_source_lag_days_at_release -ne 590 -or
    $module12.Release.validation.measured_results.dashboard_views -ne 5 -or
    $module12.Release.validation.data_checks -ne '179 of 179 pass'
) {
    throw 'DA-730 Module 12 release metadata does not match the 0.1.0 public-reporting dashboard contract.'
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
Write-Output "DA-730 $($module10.Label) passed: $($module10.Sections) contract sections and $($module10.FileCount) required files."
Write-Output "DA-730 $($module11.Label) passed: $($module11.Sections) contract sections and $($module11.FileCount) required files."
Write-Output "DA-730 $($module12.Label) passed: $($module12.Sections) contract sections and $($module12.FileCount) required files."
Write-Output "DA-730 Checkpoint 1 passed: 17 contract sections and $($checkpoint01Files.Count) package files."
