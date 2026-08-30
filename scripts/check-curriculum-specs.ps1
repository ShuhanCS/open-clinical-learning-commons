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

$fnd1 = Join-Path $repo 'docs\curriculum\courses\FND-1\course-spec.md'
$fnd1Source = Join-Path $repo 'docs\source\fnd-1-healthcare-data-foundations-source-record.md'
$fnd1Package = Join-Path $repo 'courses\healthcare-data-foundations\README.md'
if (-not (Test-Path -LiteralPath $fnd1) -or -not (Test-Path -LiteralPath $fnd1Source) -or -not (Test-Path -LiteralPath $fnd1Package)) {
    throw 'FND-1 must include its course specification, source record, and course package README.'
}

$fnd1Content = Get-Content -Raw -LiteralPath $fnd1
$fnd1ModuleCount = [regex]::Matches($fnd1Content, '(?m)^## Module \d{2} brief:').Count
if ($fnd1ModuleCount -ne 7) {
    throw "FND-1 must define seven module briefs; found $fnd1ModuleCount."
}

$fnd1HourMatches = [regex]::Matches(
    $fnd1Content,
    '(?m)^\| \d{2} \| [^|]+ \| \d \| (?<hours>\d+(?:\.\d+)?) \|'
)
$fnd1Hours = ($fnd1HourMatches | ForEach-Object { [decimal]$_.Groups['hours'].Value } | Measure-Object -Sum).Sum
if ($fnd1HourMatches.Count -ne 7 -or $fnd1Hours -ne [decimal]112.5) {
    throw "FND-1 must define seven schedule rows totaling 112.5 hours; found $($fnd1HourMatches.Count) rows and $fnd1Hours hours."
}

$fnd1CheckpointCount = [regex]::Matches($fnd1Content, '(?m)^## (?:Checkpoint \d|Final checkpoint):').Count
if ($fnd1CheckpointCount -ne 3) {
    throw "FND-1 must define three cumulative checkpoints; found $fnd1CheckpointCount."
}

if (
    $fnd1Content -match '[—–]' -or
    $fnd1Content -notmatch '40%' -or
    $fnd1Content -notmatch '25%' -or
    $fnd1Content -notmatch '35%' -or
    $fnd1Content -notmatch '70a78f38824066770b724aca907211ce6df94b3232cbeb8dbfa8389a24556692' -or
    $fnd1Content -notmatch 'FND-1 and FND-2 are separate technical foundations'
) {
    throw 'FND-1 is missing its source fingerprint, assessment weights, ownership boundary, or plain-ASCII punctuation contract.'
}

$fnd1Module01Root = Join-Path $repo 'courses\healthcare-data-foundations\modules\01-reproducible-workspace'
$fnd1Module01Spec = Join-Path $repo 'docs\curriculum\courses\FND-1\modules\01-reproducible-workspace-spec.md'
$fnd1Module01Files = @(
    'README.md',
    'assessment.md',
    'build_workspace.py',
    'data-spec.md',
    'instructor-notes.md',
    'release.json',
    'source-record.yml',
    'validate_workspace.py',
    'template\.gitattributes',
    'template\.gitignore',
    'template\README.md',
    'template\VERSION',
    'template\requirements.txt',
    'template\ai-use.md',
    'template\environment-note.md',
    'template\reproducibility-check.md',
    'template\version-policy.md',
    'template\analysis\r-smoke-test.R',
    'template\data\workspace_smoke_test.csv',
    'template\notebooks\01-smoke-test.ipynb',
    'template\outputs\.gitkeep',
    'template\sql\00-smoke-test.sql',
    'template\src\smoke_test.py'
)
$fnd1Module01Missing = @($fnd1Module01Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $fnd1Module01Root $_))
})
if (-not (Test-Path -LiteralPath $fnd1Module01Spec) -or $fnd1Module01Missing.Count -gt 0) {
    throw "FND-1 Module 01 is missing its specification or package files: $($fnd1Module01Missing -join ', ')."
}

$fnd1Module01Content = Get-Content -Raw -LiteralPath $fnd1Module01Spec
$fnd1Module01Sections = [regex]::Matches($fnd1Module01Content, '(?m)^## \d+\.').Count
if ($fnd1Module01Sections -ne 21) {
    throw "FND-1 Module 01 must define 21 contract sections; found $fnd1Module01Sections."
}
if ($fnd1Module01Content -match '[—–]' -or $fnd1Module01Content -match '(?im)[A-Z]:\\Users\\') {
    throw 'FND-1 Module 01 contains a Unicode dash or learner-facing local absolute path.'
}

$fnd1Module01Release = Get-Content -Raw -LiteralPath (Join-Path $fnd1Module01Root 'release.json') | ConvertFrom-Json
$fnd1Module01Data = Join-Path $fnd1Module01Root 'template\data\workspace_smoke_test.csv'
$fnd1Module01Notebook = Get-Content -Raw -LiteralPath (Join-Path $fnd1Module01Root 'template\notebooks\01-smoke-test.ipynb') | ConvertFrom-Json
if (
    $fnd1Module01Release.module.version -ne '0.1.0' -or
    $fnd1Module01Release.module.commons_release -ne '0.28.0' -or
    $fnd1Module01Release.module.hours -ne 15.5 -or
    $fnd1Module01Release.module.checkpoint_component_weight_percent -ne 15 -or
    $fnd1Module01Release.data.bytes -ne 134 -or
    $fnd1Module01Release.data.row_count -ne 3 -or
    $fnd1Module01Release.data.column_count -ne 3 -or
    $fnd1Module01Release.data.sha256 -ne '330da80c517c912fccd9bca3963aded84898dbb51e8b7271aa3bc53b0439c3ab' -or
    (Get-Item -LiteralPath $fnd1Module01Data).Length -ne 134 -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath $fnd1Module01Data).Hash.ToLowerInvariant() -ne '330da80c517c912fccd9bca3963aded84898dbb51e8b7271aa3bc53b0439c3ab' -or
    @($fnd1Module01Notebook.cells | Where-Object { $_.cell_type -eq 'code' }).Count -ne 3 -or
    @($fnd1Module01Notebook.cells | Where-Object { -not $_.id }).Count -ne 0 -or
    $fnd1Module01Release.package.starter_validation_checks -ne 15 -or
    $fnd1Module01Release.package.submission_validation_checks -ne 26 -or
    $fnd1Module01Release.validation.builder_self_check -ne 'pass' -or
    $fnd1Module01Release.validation.validator_self_check -ne 'pass' -or
    $fnd1Module01Release.validation.clean_target_build -ne 'pass' -or
    $fnd1Module01Release.validation.fresh_environment_install -ne 'pass' -or
    $fnd1Module01Release.validation.python_sqlite_execution -ne 'pass' -or
    $fnd1Module01Release.validation.notebook_execution -ne 'pass' -or
    $fnd1Module01Release.validation.r_execution -ne 'pass' -or
    $fnd1Module01Release.validation.nonempty_target_refusal -ne 'pass' -or
    $fnd1Module01Release.validation.incomplete_submission_rejection -ne 'pass'
) {
    throw 'FND-1 Module 01 release metadata, source, notebook, or validation facts do not match the 0.1.0 contract.'
}

& python (Join-Path $fnd1Module01Root 'build_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-1 Module 01 builder self-check failed.'
}
& python (Join-Path $fnd1Module01Root 'validate_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-1 Module 01 validator self-check failed.'
}

$fnd1Module02Root = Join-Path $repo 'courses\healthcare-data-foundations\modules\02-databases-retrieval'
$fnd1Module02Spec = Join-Path $repo 'docs\curriculum\courses\FND-1\modules\02-databases-retrieval-spec.md'
$fnd1Module02Files = @(
    'README.md', 'assessment.md', 'build_database.py', 'data-spec.md', 'instructor-notes.md',
    'reference-first-extracts.sql', 'release.json', 'run_queries.py', 'schema.sql',
    'source-manifest.csv', 'source-record.yml', 'validate_database.py',
    'template\.gitattributes', 'template\.gitignore', 'template\README.md', 'template\VERSION',
    'template\ai-use.md', 'template\data-model.mmd', 'template\fhir-json-reading.md',
    'template\schema-description.md', 'template\source-record.yml',
    'template\validation-notes.md', 'template\sql\01-first-extracts.sql'
)
$fnd1Module02Missing = @($fnd1Module02Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $fnd1Module02Root $_))
})
if (-not (Test-Path -LiteralPath $fnd1Module02Spec) -or $fnd1Module02Missing.Count -gt 0) {
    throw "FND-1 Module 02 is missing its specification or package files: $($fnd1Module02Missing -join ', ')."
}
$fnd1Module02Content = Get-Content -Raw -LiteralPath $fnd1Module02Spec
$fnd1Module02Sections = [regex]::Matches($fnd1Module02Content, '(?m)^## \d+\.').Count
if ($fnd1Module02Sections -ne 21 -or $fnd1Module02Content -match '[—–]' -or $fnd1Module02Content -match '(?im)[A-Z]:\\Users\\') {
    throw "FND-1 Module 02 must define 21 plain-ASCII contract sections without local absolute paths; found $fnd1Module02Sections sections."
}
$fnd1Module02Release = Get-Content -Raw -LiteralPath (Join-Path $fnd1Module02Root 'release.json') | ConvertFrom-Json
$fnd1Module02Manifest = Import-Csv -LiteralPath (Join-Path $fnd1Module02Root 'source-manifest.csv')
if (
    $fnd1Module02Release.module.version -ne '0.1.0' -or
    $fnd1Module02Release.module.commons_release -ne '0.29.0' -or
    $fnd1Module02Release.module.hours -ne 16 -or
    $fnd1Module02Release.source.bytes -ne 8982431 -or
    $fnd1Module02Release.source.sha256 -ne '4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a' -or
    $fnd1Module02Release.source.tables -ne 16 -or
    $fnd1Module02Release.source.rows -ne 471836 -or
    $fnd1Module02Release.database.data_dictionary_rows -ne 177 -or
    $fnd1Module02Release.database.foreign_key_failures -ne 0 -or
    $fnd1Module02Release.database.integrity_check -ne 'ok' -or
    $fnd1Module02Release.validation.database_checks -ne 96 -or
    $fnd1Module02Release.validation.complete_submission_checks -ne 126 -or
    $fnd1Module02Manifest.Count -ne 16 -or
    ($fnd1Module02Manifest | Measure-Object -Property source_rows -Sum).Sum -ne 471836 -or
    ($fnd1Module02Manifest | Measure-Object -Property source_columns -Sum).Sum -ne 168
) {
    throw 'FND-1 Module 02 release metadata or source manifest does not match the 0.1.0 contract.'
}
& python (Join-Path $fnd1Module02Root 'build_database.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 Module 02 builder self-check failed.' }
& python (Join-Path $fnd1Module02Root 'run_queries.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 Module 02 query-runner self-check failed.' }
& python (Join-Path $fnd1Module02Root 'validate_database.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 Module 02 validator self-check failed.' }

$fnd1Module03Root = Join-Path $repo 'courses\healthcare-data-foundations\modules\03-cohorts-analytic-tables'
$fnd1Module03Spec = Join-Path $repo 'docs\curriculum\courses\FND-1\modules\03-cohorts-analytic-tables-spec.md'
$fnd1Module03Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'ai-use.md', 'assessment.md', 'build_cohort.py',
    'cohort-spec.md', 'data-dictionary.csv', 'instructor-notes.md', 'release.json',
    'reproducibility-check.md', 'source-record.yml', 'table-spec.md', 'transformation-record.md',
    'validate_cohort.py', 'sql\01-eligible-events.sql', 'sql\02-index-cohort.sql',
    'sql\03-analytic-table.sql', 'sql\04-validation.sql', 'outputs\eligible-events.csv',
    'outputs\index-cohort.csv', 'outputs\analytic-table.csv', 'outputs\cohort-flow.csv',
    'outputs\query-checks.csv', 'learner-template\.gitattributes', 'learner-template\README.md',
    'learner-template\VERSION', 'learner-template\ai-use.md', 'learner-template\cohort-spec.md',
    'learner-template\data-dictionary.csv', 'learner-template\reproducibility-check.md',
    'learner-template\source-record.yml', 'learner-template\table-spec.md',
    'learner-template\transformation-record.md', 'learner-template\sql\01-eligible-events.sql',
    'learner-template\sql\02-index-cohort.sql', 'learner-template\sql\03-analytic-table.sql',
    'learner-template\sql\04-validation.sql'
)
$fnd1Module03Missing = @($fnd1Module03Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $fnd1Module03Root $_))
})
if (-not (Test-Path -LiteralPath $fnd1Module03Spec) -or $fnd1Module03Missing.Count -gt 0) {
    throw "FND-1 Module 03 is missing its specification or package files: $($fnd1Module03Missing -join ', ')."
}
$fnd1Module03Content = Get-Content -Raw -LiteralPath $fnd1Module03Spec
$fnd1Module03Sections = [regex]::Matches($fnd1Module03Content, '(?m)^## \d+\.').Count
if ($fnd1Module03Sections -ne 21 -or $fnd1Module03Content -match '[—–]' -or $fnd1Module03Content -match '(?im)[A-Z]:\\Users\\') {
    throw "FND-1 Module 03 must define 21 plain-ASCII contract sections without local absolute paths; found $fnd1Module03Sections sections."
}
$fnd1Module03Release = Get-Content -Raw -LiteralPath (Join-Path $fnd1Module03Root 'release.json') | ConvertFrom-Json
$fnd1Module03Dictionary = Import-Csv -LiteralPath (Join-Path $fnd1Module03Root 'data-dictionary.csv')
$fnd1Module03StarterDictionary = Import-Csv -LiteralPath (Join-Path $fnd1Module03Root 'learner-template\data-dictionary.csv')
$fnd1Module03Eligible = Import-Csv -LiteralPath (Join-Path $fnd1Module03Root 'outputs\eligible-events.csv')
$fnd1Module03Index = Import-Csv -LiteralPath (Join-Path $fnd1Module03Root 'outputs\index-cohort.csv')
$fnd1Module03Analytic = Import-Csv -LiteralPath (Join-Path $fnd1Module03Root 'outputs\analytic-table.csv')
$fnd1Module03Flow = Import-Csv -LiteralPath (Join-Path $fnd1Module03Root 'outputs\cohort-flow.csv')
$fnd1Module03Checks = Import-Csv -LiteralPath (Join-Path $fnd1Module03Root 'outputs\query-checks.csv')
$fnd1Module03AnalyticPath = Join-Path $fnd1Module03Root 'outputs\analytic-table.csv'
if (
    $fnd1Module03Release.module.version -ne '0.1.0' -or
    $fnd1Module03Release.module.commons_release -ne '0.30.0' -or
    $fnd1Module03Release.module.hours -ne 16.5 -or
    $fnd1Module03Release.module.checkpoint_component_weight_percent -ne 25 -or
    $fnd1Module03Release.upstream.database_bytes -ne 141234176 -or
    $fnd1Module03Release.upstream.database_sha256 -ne '1116dda22c4297fcfeab6bf2c99bb3dbfaf9f9b5e04041b96be90719c76e704a' -or
    $fnd1Module03Release.cohort.adult_eligible_events -ne 1048 -or
    $fnd1Module03Release.cohort.included_patients -ne 374 -or
    $fnd1Module03Release.analytic_table.fields -ne 29 -or
    $fnd1Module03Release.validation.complete_submission_checks -ne 614 -or
    $fnd1Module03Eligible.Count -ne 1048 -or
    $fnd1Module03Index.Count -ne 374 -or
    $fnd1Module03Analytic.Count -ne 374 -or
    $fnd1Module03Dictionary.Count -ne 29 -or
    $fnd1Module03StarterDictionary.Count -ne 29 -or
    $fnd1Module03Flow.Count -ne 4 -or
    $fnd1Module03Checks.Count -ne 16 -or
    @($fnd1Module03Checks | Where-Object { $_.status -ne 'pass' }).Count -ne 0 -or
    (Get-Item -LiteralPath $fnd1Module03AnalyticPath).Length -ne 121787 -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath $fnd1Module03AnalyticPath).Hash.ToLowerInvariant() -ne '3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a'
) {
    throw 'FND-1 Module 03 release metadata, cohort outputs, dictionary, or fingerprints do not match the 0.1.0 contract.'
}
& python (Join-Path $fnd1Module03Root 'build_cohort.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 Module 03 builder self-check failed.' }
& python (Join-Path $fnd1Module03Root 'validate_cohort.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 Module 03 validator self-check failed.' }

$fnd1Module04Root = Join-Path $repo 'courses\healthcare-data-foundations\modules\04-cleaning-profiling'
$fnd1Module04Spec = Join-Path $repo 'docs\curriculum\courses\FND-1\modules\04-cleaning-profiling-spec.md'
$fnd1Module04Files = @(
    '.gitattributes', '.gitignore', 'README.md', 'VERSION', 'ai-use.md', 'assessment.md',
    'build_defect_release.py', 'data-dictionary.csv', 'data-spec.md', 'instructor-notes.md',
    'profile_quality.py', 'release.json', 'reproducibility-check.md', 'stop-fix-proceed.md',
    'transformation-record.md', 'validate_defect_release.py', 'data\accepted-analytic-table.csv',
    'data\defective-analytic-table.csv', 'data\defect-manifest.csv', 'data\quality-rules.csv',
    'data\fnd1-quality-defects.sqlite', 'data\build-report.json', 'notebooks\04-data-quality.ipynb',
    'outputs\quality-profile.csv', 'outputs\missingness-profile.csv',
    'outputs\quality-rule-results.csv', 'outputs\quality-risk-log.csv',
    'outputs\resolution-log.csv', 'outputs\resolved-analytic-table.csv',
    'outputs\profile-report.json', 'learner-template\.gitattributes',
    'learner-template\README.md', 'learner-template\VERSION', 'learner-template\ai-use.md',
    'learner-template\data-dictionary.csv', 'learner-template\data-spec.md',
    'learner-template\reproducibility-check.md', 'learner-template\stop-fix-proceed.md',
    'learner-template\transformation-record.md', 'learner-template\notebooks\04-data-quality.ipynb'
)
$fnd1Module04Missing = @($fnd1Module04Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $fnd1Module04Root $_))
})
if (-not (Test-Path -LiteralPath $fnd1Module04Spec) -or $fnd1Module04Missing.Count -gt 0) {
    throw "FND-1 Module 04 is missing its specification or package files: $($fnd1Module04Missing -join ', ')."
}
$fnd1Module04Content = Get-Content -Raw -LiteralPath $fnd1Module04Spec
$fnd1Module04Sections = [regex]::Matches($fnd1Module04Content, '(?m)^## \d+\.').Count
$fnd1Module04Release = Get-Content -Raw -LiteralPath (Join-Path $fnd1Module04Root 'release.json') | ConvertFrom-Json
$fnd1Module04Rules = Import-Csv -LiteralPath (Join-Path $fnd1Module04Root 'outputs\quality-rule-results.csv')
$fnd1Module04Resolved = Join-Path $fnd1Module04Root 'outputs\resolved-analytic-table.csv'
$fnd1Module04Defective = Join-Path $fnd1Module04Root 'data\defective-analytic-table.csv'
$fnd1Module04Database = Join-Path $fnd1Module04Root 'data\fnd1-quality-defects.sqlite'
if (
    $fnd1Module04Sections -ne 21 -or
    $fnd1Module04Content -match '[—–]' -or
    $fnd1Module04Content -match '(?im)[A-Z]:\\Users\\' -or
    $fnd1Module04Release.module.version -ne '0.1.0' -or
    $fnd1Module04Release.module.commons_release -ne '0.32.0' -or
    $fnd1Module04Release.module.hours -ne 16.5 -or
    $fnd1Module04Release.defect_release.rows -ne 379 -or
    $fnd1Module04Release.defect_release.seeded_cases -ne 56 -or
    $fnd1Module04Release.defect_release.manifest_changes -ne 68 -or
    $fnd1Module04Release.defect_release.total_rules -ne 28 -or
    $fnd1Module04Release.package.release_validation_checks -ne 344 -or
    $fnd1Module04Release.package.complete_submission_checks -ne 340 -or
    $fnd1Module04Rules.Count -ne 28 -or
    @($fnd1Module04Rules | Where-Object { $_.detection_status -ne 'pass' }).Count -ne 0 -or
    (Get-Item -LiteralPath $fnd1Module04Defective).Length -ne 123211 -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath $fnd1Module04Defective).Hash.ToLowerInvariant() -ne '7800c1d24093b93ce40634afe652e574a1ed2775eba8a742c0bd00bf3596a02d' -or
    (Get-Item -LiteralPath $fnd1Module04Database).Length -ne 385024 -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath $fnd1Module04Database).Hash.ToLowerInvariant() -ne '3b9cbf4ba7920f85a8af524902f2e7d35b3e837e5dd6b94deb4f20a156644275' -or
    (Get-Item -LiteralPath $fnd1Module04Resolved).Length -ne 121787 -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath $fnd1Module04Resolved).Hash.ToLowerInvariant() -ne '3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a'
) {
    throw "FND-1 Module 04 release metadata, specification, rule evidence, or fingerprints do not match the 0.1.0 contract."
}
& python (Join-Path $fnd1Module04Root 'build_defect_release.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 Module 04 builder self-check failed.' }
& python (Join-Path $fnd1Module04Root 'profile_quality.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 Module 04 profiler self-check failed.' }
& python (Join-Path $fnd1Module04Root 'validate_defect_release.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 Module 04 validator self-check failed.' }

$fnd1Module05Root = Join-Path $repo 'courses\healthcare-data-foundations\modules\05-descriptive-results'
$fnd1Module05Spec = Join-Path $repo 'docs\curriculum\courses\FND-1\modules\05-descriptive-results-spec.md'
$fnd1Module05Files = @(
    '.gitattributes', '.gitignore', 'README.md', 'VERSION', 'ai-use.md', 'assessment.md',
    'build_descriptive.py', 'data-spec.md', 'instructor-notes.md', 'interpretation-memo.md',
    'release.json', 'reproducibility-check.md', 'source-record.yml', 'transformation-record.md',
    'validate_descriptive.py', 'data\resolved-analytic-table.csv', 'data\quality-rule-results.csv',
    'notebooks\05-descriptive-results.ipynb', 'outputs\variable-profile.csv',
    'outputs\cross-tabs.csv', 'outputs\rates.csv', 'outputs\stratified-table.csv',
    'outputs\denominator-registry.csv', 'outputs\descriptive-checks.csv', 'outputs\build-report.json',
    'learner-template\.gitattributes', 'learner-template\README.md', 'learner-template\VERSION',
    'learner-template\ai-use.md', 'learner-template\data-spec.md',
    'learner-template\interpretation-memo.md', 'learner-template\reproducibility-check.md',
    'learner-template\source-record.yml', 'learner-template\transformation-record.md',
    'learner-template\notebooks\05-descriptive-results.ipynb'
)
$fnd1Module05Missing = @($fnd1Module05Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $fnd1Module05Root $_))
})
if (-not (Test-Path -LiteralPath $fnd1Module05Spec) -or $fnd1Module05Missing.Count -gt 0) {
    throw "FND-1 Module 05 is missing its specification or package files: $($fnd1Module05Missing -join ', ')."
}
$fnd1Module05Content = Get-Content -Raw -LiteralPath $fnd1Module05Spec
$fnd1Module05Sections = [regex]::Matches($fnd1Module05Content, '(?m)^## \d+\.').Count
$fnd1Module05Release = Get-Content -Raw -LiteralPath (Join-Path $fnd1Module05Root 'release.json') | ConvertFrom-Json
$fnd1Module05Profiles = Import-Csv -LiteralPath (Join-Path $fnd1Module05Root 'outputs\variable-profile.csv')
$fnd1Module05CrossTabs = Import-Csv -LiteralPath (Join-Path $fnd1Module05Root 'outputs\cross-tabs.csv')
$fnd1Module05Rates = Import-Csv -LiteralPath (Join-Path $fnd1Module05Root 'outputs\rates.csv')
$fnd1Module05Strata = Import-Csv -LiteralPath (Join-Path $fnd1Module05Root 'outputs\stratified-table.csv')
$fnd1Module05Registry = Import-Csv -LiteralPath (Join-Path $fnd1Module05Root 'outputs\denominator-registry.csv')
$fnd1Module05Checks = Import-Csv -LiteralPath (Join-Path $fnd1Module05Root 'outputs\descriptive-checks.csv')
if (
    $fnd1Module05Sections -ne 21 -or
    $fnd1Module05Content -match '[—–]' -or
    $fnd1Module05Content -match '(?im)[A-Z]:\\Users\\' -or
    $fnd1Module05Release.module.version -ne '0.1.0' -or
    $fnd1Module05Release.module.commons_release -ne '0.33.0' -or
    $fnd1Module05Release.module.hours -ne 16 -or
    $fnd1Module05Release.module.checkpoint_component_weight_percent -ne 25 -or
    $fnd1Module05Release.package.release_validation_checks -ne 1101 -or
    $fnd1Module05Release.package.complete_submission_checks -ne 1100 -or
    $fnd1Module05Profiles.Count -ne 17 -or
    $fnd1Module05CrossTabs.Count -ne 12 -or
    $fnd1Module05Rates.Count -ne 6 -or
    $fnd1Module05Strata.Count -ne 2 -or
    $fnd1Module05Registry.Count -ne 27 -or
    $fnd1Module05Checks.Count -ne 18 -or
    @($fnd1Module05Checks | Where-Object { $_.status -ne 'pass' }).Count -ne 0 -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $fnd1Module05Root 'outputs\variable-profile.csv')).Hash.ToLowerInvariant() -ne '9d9bd1f8db71ebfdf3b775de13eb4450e30db9d52f8c71b2be0bf66918341f73' -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $fnd1Module05Root 'outputs\denominator-registry.csv')).Hash.ToLowerInvariant() -ne 'e13bd0e1cf0716b912476fd81c7e4dd8bc827b2df468421aa2efc33f1f234be6' -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $fnd1Module05Root 'outputs\descriptive-checks.csv')).Hash.ToLowerInvariant() -ne '9fb7970cda77bf1be25639265a762eab97a227106824b9f913f208000d99a1fa'
) {
    throw 'FND-1 Module 05 release metadata, specification, output counts, or fingerprints do not match the 0.1.0 contract.'
}
& python (Join-Path $fnd1Module05Root 'build_descriptive.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 Module 05 builder self-check failed.' }
& python (Join-Path $fnd1Module05Root 'validate_descriptive.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 Module 05 validator self-check failed.' }

$fnd1Checkpoint01Root = Join-Path $repo 'courses\healthcare-data-foundations\checkpoints\01-validated-cohort-release'
$fnd1Checkpoint01Spec = Join-Path $repo 'docs\curriculum\courses\FND-1\checkpoints\01-validated-cohort-release-spec.md'
$fnd1Checkpoint01Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'assessment.md', 'assemble_checkpoint.py',
    'instructor-notes.md', 'release.json', 'validate_checkpoint.py', 'assets\schema-diagram.svg',
    'template\.gitattributes', 'template\README.md', 'template\ai-use.md',
    'template\component-score.csv', 'template\reproducibility-check.md',
    'template\review-disposition.md', 'template\source-system-comparison.md',
    'template\transformation-record.md', 'reference\README.md', 'reference\environment-note.md',
    'reference\version-policy.md', 'reference\data-model.mmd', 'reference\schema-description.md',
    'reference\source-system-comparison.md', 'reference\fhir-json-reading.md',
    'reference\transformation-record.md', 'reference\reproducibility-check.md',
    'reference\ai-use.md', 'reference\component-score.csv', 'reference\review-disposition.md',
    'reference\evidence\module-01-ai-use.md',
    'reference\evidence\module-01-reproducibility-check.md',
    'reference\evidence\module-02-ai-use.md',
    'reference\evidence\module-02-validation-notes.md',
    'reference\evidence\module-03-ai-use.md',
    'reference\evidence\module-03-reproducibility-check.md',
    'reference\first-extracts\encounter-class-counts.csv',
    'reference\first-extracts\numeric-observation-sample.csv',
    'reference\first-extracts\observation-linkage.csv',
    'reference\first-extracts\selected-patient-timeline.csv',
    'reference\first-extracts\table-inventory.csv'
)
$fnd1Checkpoint01Missing = @($fnd1Checkpoint01Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $fnd1Checkpoint01Root $_))
})
if (-not (Test-Path -LiteralPath $fnd1Checkpoint01Spec) -or $fnd1Checkpoint01Missing.Count -gt 0) {
    throw "FND-1 Checkpoint 1 is missing its specification or package files: $($fnd1Checkpoint01Missing -join ', ')."
}
$fnd1Checkpoint01Content = Get-Content -Raw -LiteralPath $fnd1Checkpoint01Spec
$fnd1Checkpoint01Sections = [regex]::Matches($fnd1Checkpoint01Content, '(?m)^## \d+\.').Count
if ($fnd1Checkpoint01Sections -ne 17 -or $fnd1Checkpoint01Content -match '[—–]' -or $fnd1Checkpoint01Content -match '(?im)[A-Z]:\\Users\\') {
    throw "FND-1 Checkpoint 1 must define 17 plain-ASCII contract sections without local absolute paths; found $fnd1Checkpoint01Sections sections."
}
$fnd1Checkpoint01Release = Get-Content -Raw -LiteralPath (Join-Path $fnd1Checkpoint01Root 'release.json') | ConvertFrom-Json
$fnd1Checkpoint01Scores = Import-Csv -LiteralPath (Join-Path $fnd1Checkpoint01Root 'reference\component-score.csv')
$fnd1Checkpoint01Extracts = @(
    @{ Name = 'encounter-class-counts.csv'; Rows = 6; Hash = '26106dd682622ddbc6d75857a93607d48a353ba707ef56fc51d231be8f201d65' },
    @{ Name = 'numeric-observation-sample.csv'; Rows = 25; Hash = 'f6854aeeeca3a7083147f53fa7e41fd7797e3ee94f459864c087190126c2d940' },
    @{ Name = 'observation-linkage.csv'; Rows = 3; Hash = '901e06e7c9b71b5e11daf021772837af9223338c921641aeff60cc1ca214dd12' },
    @{ Name = 'selected-patient-timeline.csv'; Rows = 25; Hash = '411a05229819cd5e7cfe9d678fc8920053db8e2be8cc93135c6fcb88d1b28a0c' },
    @{ Name = 'table-inventory.csv'; Rows = 16; Hash = '3f8fc12567ef57d1b74c21aa9fcfaedfac764c772e8d422ced002b7901358c07' }
)
if (
    $fnd1Checkpoint01Release.checkpoint.version -ne '0.1.0' -or
    $fnd1Checkpoint01Release.checkpoint.commons_release -ne '0.31.0' -or
    $fnd1Checkpoint01Release.checkpoint.course_weight_percent -ne 40 -or
    $fnd1Checkpoint01Release.checkpoint.cumulative_hours -ne 48 -or
    ($fnd1Checkpoint01Release.components | Measure-Object -Property course_points -Sum).Sum -ne 40 -or
    $fnd1Checkpoint01Release.package.assembled_files -ne 45 -or
    $fnd1Checkpoint01Release.package.immutable_manifest_rows -ne 35 -or
    $fnd1Checkpoint01Release.package.manifest_sha256 -ne '36cf454387db595e9237f461556676db7611b3b60b2762f8554e4d9d580c96a6' -or
    $fnd1Checkpoint01Release.validation.starter_checks -ne 295 -or
    $fnd1Checkpoint01Release.validation.complete_reference_checks -ne 341 -or
    ($fnd1Checkpoint01Scores | Measure-Object -Property course_points_available -Sum).Sum -ne 40 -or
    ($fnd1Checkpoint01Scores | Measure-Object -Property points_earned -Sum).Sum -ne 40
) {
    throw 'FND-1 Checkpoint 1 release metadata, component weights, manifest, or validation facts do not match the 0.1.0 contract.'
}
foreach ($extract in $fnd1Checkpoint01Extracts) {
    $path = Join-Path $fnd1Checkpoint01Root (Join-Path 'reference\first-extracts' $extract.Name)
    if (
        (Import-Csv -LiteralPath $path).Count -ne $extract.Rows -or
        (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash.ToLowerInvariant() -ne $extract.Hash
    ) {
        throw "FND-1 Checkpoint 1 first extract changed: $($extract.Name)."
    }
}
& python (Join-Path $fnd1Checkpoint01Root 'assemble_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 Checkpoint 1 assembler self-check failed.' }
& python (Join-Path $fnd1Checkpoint01Root 'validate_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 Checkpoint 1 validator self-check failed.' }

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

$module13 = Test-ModuleContract `
    -Label 'Module 13' `
    -SpecPath (Join-Path $repo 'docs\curriculum\courses\DA-730\modules\13-audience-annotation-narrative-capstone-spec.md') `
    -ModuleRoot (Join-Path $repo 'courses\data-visualization\modules\13-audience-annotation-narrative-capstone') `
    -RequiredFiles @(
        'README.md',
        'data-spec.md',
        'source-record.yml',
        'validate_decision_story_case.py',
        'lab.R',
        'critique_charts.R',
        'assessment.md',
        'instructor-notes.md',
        'release.json'
    )
if (
    $module13.Release.module.version -ne '0.1.0' -or
    $module13.Release.module.commons_release -ne '0.25.0' -or
    $module13.Release.module.hours -ne 16.5 -or
    $module13.Release.module.week -ne 7 -or
    $module13.Release.upstream.teaching.row_count -ne 186 -or
    $module13.Release.upstream.teaching.column_count -ne 31 -or
    $module13.Release.upstream.teaching.sha256 -ne 'fbfcfcaf10d87cd48236a702622781f559d86d52b8773ca578d72313a9b270fd' -or
    $module13.Release.upstream.measure_dictionary.row_count -ne 3 -or
    $module13.Release.upstream.measure_dictionary.column_count -ne 18 -or
    $module13.Release.upstream.measure_dictionary.sha256 -ne '2db834a350c0fee342efb30fc4b028053e325b3b357cc1031a11f7c9e9b29412' -or
    $module13.Release.upstream.source_selection.row_count -ne 186 -or
    $module13.Release.upstream.source_selection.column_count -ne 15 -or
    $module13.Release.upstream.source_selection.sha256 -ne 'f28f5d56e5e0e29001c7a275b01306762e673c9a21459dc7a68ff1aea782943b' -or
    $module13.Release.validation.measured_results.upstream_rows -ne 186 -or
    $module13.Release.validation.measured_results.selected_rows -ne 3 -or
    $module13.Release.validation.measured_results.audience_versions -ne 2 -or
    $module13.Release.validation.measured_results.selected_op22_pct -ne 23 -or
    $module13.Release.validation.measured_results.selected_op22_source_lag_days -ne 590 -or
    $module13.Release.validation.measured_results.stable_supported_action -ne 'definition and current-data review' -or
    $module13.Release.validation.data_checks -ne '66 of 66 pass'
) {
    throw 'DA-730 Module 13 release metadata does not match the 0.1.0 two-audience decision-story contract.'
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

$checkpoint02Root = Join-Path $repo 'courses\data-visualization\checkpoints\02-applied-visualization-portfolio'
$checkpoint02Spec = Join-Path $repo 'docs\curriculum\courses\DA-730\checkpoints\02-applied-visualization-portfolio-spec.md'
$checkpoint02Files = @(
    'README.md',
    'assemble_checkpoint.ps1',
    'validate_checkpoint.py',
    'render_portfolio_artifact.R',
    'instructor-notes.md',
    'release.json',
    'template\README.md',
    'template\portfolio-index.md',
    'template\view-purpose-audit.md',
    'template\critique-and-repair.md',
    'template\accessibility-report.md',
    'template\decision-brief.md',
    'template\capstone-proposal.md',
    'template\ai-use.md',
    'template\analysis\accessible-display.R',
    'template\analysis\time-display.R',
    'template\analysis\comparison-display.R',
    'template\analysis\place-display.R',
    'template\analysis\structure-display.R',
    'template\analysis\dashboard.R',
    'template\source-records\accessible-display-source.yml',
    'template\source-records\time-display-source.yml',
    'template\source-records\comparison-display-source.yml',
    'template\source-records\place-display-source.yml',
    'template\source-records\structure-display-source.yml',
    'template\source-records\dashboard-source.yml'
)
$checkpoint02Missing = @($checkpoint02Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $checkpoint02Root $_))
})
if (-not (Test-Path -LiteralPath $checkpoint02Spec) -or $checkpoint02Missing.Count -gt 0) {
    throw "DA-730 Checkpoint 2 is missing its specification or package files: $($checkpoint02Missing -join ', ')."
}
$checkpoint02Content = Get-Content -Raw -LiteralPath $checkpoint02Spec
if ([regex]::Matches($checkpoint02Content, '(?m)^## \d+\.').Count -ne 17) {
    throw 'DA-730 Checkpoint 2 must define 17 numbered contract sections.'
}
if ($checkpoint02Content -match '[—–]') {
    throw 'DA-730 Checkpoint 2 contains a Unicode em dash or en dash.'
}
$checkpoint02Release = Get-Content -Raw -LiteralPath (Join-Path $checkpoint02Root 'release.json') | ConvertFrom-Json
if (
    $checkpoint02Release.checkpoint.version -ne '0.1.0' -or
    $checkpoint02Release.checkpoint.commons_release -ne '0.24.0' -or
    $checkpoint02Release.checkpoint.included_modules.Count -ne 6 -or
    $checkpoint02Release.starter_outputs.figures -ne 6 -or
    $checkpoint02Release.starter_outputs.evidence_tables -ne 6 -or
    $checkpoint02Release.starter_outputs.accessible_alternatives -ne 6 -or
    $checkpoint02Release.starter_outputs.table_rows.accessible_display -ne 65 -or
    $checkpoint02Release.starter_outputs.table_rows.time_display -ne 94 -or
    $checkpoint02Release.starter_outputs.table_rows.comparison_display -ne 500 -or
    $checkpoint02Release.starter_outputs.table_rows.place_display -ne 100 -or
    $checkpoint02Release.starter_outputs.table_rows.structure_display -ne 7 -or
    $checkpoint02Release.starter_outputs.table_rows.dashboard -ne 3 -or
    $checkpoint02Release.validation.validator_self_check -ne 'pass' -or
    $checkpoint02Release.validation.assembler -ne 'pass' -or
    $checkpoint02Release.validation.nonempty_target_refusal -ne 'pass'
) {
    throw 'DA-730 Checkpoint 2 release metadata does not match the 0.1.0 Week 6 portfolio contract.'
}
& python (Join-Path $checkpoint02Root 'validate_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'DA-730 Checkpoint 2 validator self-check failed.'
}

$checkpoint03Root = Join-Path $repo 'courses\data-visualization\checkpoints\03-decision-story-capstone'
$checkpoint03Spec = Join-Path $repo 'docs\curriculum\courses\DA-730\checkpoints\03-decision-story-capstone-spec.md'
$checkpoint03Files = @(
    'README.md',
    'assemble_checkpoint.ps1',
    'render_decision_story.R',
    'validate_checkpoint.py',
    'instructor-notes.md',
    'release.json',
    'template\README.md',
    'template\decision-brief.md',
    'template\alt-text.md',
    'template\transformation-record.md',
    'template\audience-adaptation-record.md',
    'template\reproducibility-check.md',
    'template\critique-response.md',
    'template\ai-use.md',
    'template\review-disposition.md',
    'template\source-record.yml',
    'template\defense\slides-outline.md',
    'template\defense\questions-and-responses.md'
)
$checkpoint03Missing = @($checkpoint03Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $checkpoint03Root $_))
})
if (-not (Test-Path -LiteralPath $checkpoint03Spec) -or $checkpoint03Missing.Count -gt 0) {
    throw "DA-730 Checkpoint 3 is missing its specification or package files: $($checkpoint03Missing -join ', ')."
}
$checkpoint03Content = Get-Content -Raw -LiteralPath $checkpoint03Spec
if ([regex]::Matches($checkpoint03Content, '(?m)^## \d+\.').Count -ne 17) {
    throw 'DA-730 Checkpoint 3 must define 17 numbered contract sections.'
}
if ($checkpoint03Content -match '[—–]') {
    throw 'DA-730 Checkpoint 3 contains a Unicode em dash or en dash.'
}
$checkpoint03Release = Get-Content -Raw -LiteralPath (Join-Path $checkpoint03Root 'release.json') | ConvertFrom-Json
if (
    $checkpoint03Release.checkpoint.version -ne '0.1.0' -or
    $checkpoint03Release.checkpoint.commons_release -ne '0.26.0' -or
    $checkpoint03Release.checkpoint.included_modules.Count -ne 13 -or
    $checkpoint03Release.calendar.observed_2026_2027_elapsed_days.Count -ne 6 -or
    ($checkpoint03Release.calendar.observed_2026_2027_elapsed_days | Measure-Object -Minimum).Minimum -ne 49 -or
    ($checkpoint03Release.calendar.observed_2026_2027_elapsed_days | Measure-Object -Maximum).Maximum -ne 52 -or
    $checkpoint03Release.packaged_data.teaching.row_count -ne 186 -or
    $checkpoint03Release.packaged_data.teaching.column_count -ne 31 -or
    $checkpoint03Release.packaged_data.teaching.sha256 -ne 'fbfcfcaf10d87cd48236a702622781f559d86d52b8773ca578d72313a9b270fd' -or
    $checkpoint03Release.packaged_data.measure_dictionary.row_count -ne 3 -or
    $checkpoint03Release.packaged_data.measure_dictionary.column_count -ne 18 -or
    $checkpoint03Release.packaged_data.measure_dictionary.sha256 -ne '2db834a350c0fee342efb30fc4b028053e325b3b357cc1031a11f7c9e9b29412' -or
    $checkpoint03Release.packaged_data.source_selection.row_count -ne 186 -or
    $checkpoint03Release.packaged_data.source_selection.column_count -ne 15 -or
    $checkpoint03Release.packaged_data.source_selection.sha256 -ne 'f28f5d56e5e0e29001c7a275b01306762e673c9a21459dc7a68ff1aea782943b' -or
    $checkpoint03Release.starter_outputs.figures -ne 2 -or
    $checkpoint03Release.starter_outputs.accessible_table_rows -ne 3 -or
    $checkpoint03Release.starter_outputs.accessible_table_columns -ne 20 -or
    $checkpoint03Release.reference_invariants.selected_op22_percent -ne 23 -or
    $checkpoint03Release.reference_invariants.selected_op22_lag_days -ne 590 -or
    $checkpoint03Release.reference_invariants.stable_supported_action -ne 'definition and current-data review' -or
    $checkpoint03Release.validation.validator_self_check -ne 'pass' -or
    $checkpoint03Release.validation.assembler -ne 'pass' -or
    $checkpoint03Release.validation.analysis_rerun -ne 'pass' -or
    $checkpoint03Release.validation.nonempty_target_refusal -ne 'pass' -or
    $checkpoint03Release.validation.incomplete_starter_rejection -ne 'pass'
) {
    throw 'DA-730 Checkpoint 3 release metadata does not match the 0.1.0 final decision-story contract.'
}
& python (Join-Path $checkpoint03Root 'validate_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'DA-730 Checkpoint 3 validator self-check failed.'
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
Write-Output "DA-730 $($module13.Label) passed: $($module13.Sections) contract sections and $($module13.FileCount) required files."
Write-Output "DA-730 Checkpoint 1 passed: 17 contract sections and $($checkpoint01Files.Count) package files."
Write-Output "DA-730 Checkpoint 2 passed: 17 contract sections and $($checkpoint02Files.Count) package files."
Write-Output "DA-730 Checkpoint 3 passed: 17 contract sections and $($checkpoint03Files.Count) package files."
Write-Output "FND-1 specification passed: $fnd1ModuleCount modules, $fnd1Hours hours, $fnd1CheckpointCount checkpoints."
Write-Output "FND-1 Module 01 passed: $fnd1Module01Sections contract sections and $($fnd1Module01Files.Count) required files."
Write-Output "FND-1 Module 02 passed: $fnd1Module02Sections contract sections and $($fnd1Module02Files.Count) required files."
Write-Output "FND-1 Module 03 passed: $fnd1Module03Sections contract sections and $($fnd1Module03Files.Count) required files."
Write-Output "FND-1 Module 04 passed: $fnd1Module04Sections contract sections and $($fnd1Module04Files.Count) required files."
Write-Output "FND-1 Module 05 passed: $fnd1Module05Sections contract sections and $($fnd1Module05Files.Count) required files."
Write-Output "FND-1 Checkpoint 1 passed: $fnd1Checkpoint01Sections contract sections and $($fnd1Checkpoint01Files.Count) required files."
