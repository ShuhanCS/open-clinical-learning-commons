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

$fnd2 = Join-Path $repo 'docs\curriculum\courses\FND-2\course-spec.md'
$fnd2Source = Join-Path $repo 'docs\source\fnd-2-modeling-inference-reproducible-analytics-source-record.md'
$fnd2Package = Join-Path $repo 'courses\modeling-inference-reproducible-analytics\README.md'
if (-not (Test-Path -LiteralPath $fnd2) -or -not (Test-Path -LiteralPath $fnd2Source) -or -not (Test-Path -LiteralPath $fnd2Package)) {
    throw 'FND-2 must include its course specification, source record, and course package README.'
}
$fnd2Content = Get-Content -Raw -LiteralPath $fnd2
$fnd2SourceContent = Get-Content -Raw -LiteralPath $fnd2Source
$fnd2PackageContent = Get-Content -Raw -LiteralPath $fnd2Package
$fnd2ModuleCount = [regex]::Matches($fnd2Content, '(?m)^## Module \d{2} brief:').Count
$fnd2HourMatches = [regex]::Matches(
    $fnd2Content,
    '(?m)^\| \d{2} \| [^|]+ \| \d \| (?<hours>\d+(?:\.\d+)?) \|'
)
$fnd2Hours = ($fnd2HourMatches | ForEach-Object { [decimal]$_.Groups['hours'].Value } | Measure-Object -Sum).Sum
$fnd2CheckpointCount = [regex]::Matches($fnd2Content, '(?m)^## (?:Checkpoint \d|Final checkpoint):').Count
if (
    $fnd2ModuleCount -ne 7 -or
    $fnd2HourMatches.Count -ne 7 -or
    $fnd2Hours -ne [decimal]112.5 -or
    $fnd2CheckpointCount -ne 3
) {
    throw "FND-2 must define seven modules, seven schedule rows totaling 112.5 hours, and three checkpoints; found $fnd2ModuleCount modules, $($fnd2HourMatches.Count) rows, $fnd2Hours hours, and $fnd2CheckpointCount checkpoints."
}
if (
    $fnd2Content -match '[—–]' -or
    $fnd2SourceContent -match '[—–]' -or
    $fnd2PackageContent -match '[—–]' -or
    $fnd2Content -match '(?im)[A-Z]:\\Users\\' -or
    $fnd2SourceContent -match '(?im)[A-Z]:\\Users\\' -or
    $fnd2PackageContent -match '(?im)[A-Z]:\\Users\\' -or
    $fnd2Content -notmatch 'Commons release: 0\.38\.0' -or
    $fnd2PackageContent -notmatch 'Commons release: 0\.48\.0' -or
    $fnd2Content -notmatch 'eef6fbb36cb27917f8b48b61e705895a5cb5eaad64bd0f0d38bf153525528c03' -or
    $fnd2SourceContent -notmatch 'eef6fbb36cb27917f8b48b61e705895a5cb5eaad64bd0f0d38bf153525528c03' -or
    $fnd2SourceContent -notmatch '21,850' -or
    $fnd2SourceContent -notmatch 'Curriculum-30-Credits-2026-08-29\.zip' -or
    $fnd2SourceContent -notmatch 'OneDrive_2026-08-29 \(1\)\.zip' -or
    $fnd2Content -notmatch 'FND-1 and FND-2 are separate straight-through technical foundations' -or
    $fnd2Content -notmatch '3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a' -or
    $fnd2Content -notmatch '224, 75, and 75' -or
    $fnd2Content -notmatch '25, 7, and 4' -or
    $fnd2Content -notmatch '8a492c3d2d3dae07c42e89ef35ed714d23acab32596f42037dcf8dd0284531d1' -or
    $fnd2Content -notmatch '394d9b02d2cc9b4fbf0d9f415db3da6b04393dd9430816973e81fef86fb0e616' -or
    $fnd2Content -notmatch 'teaching use only' -or
    $fnd2Content -notmatch 'https://www\.mghihp\.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current\.pdf' -or
    $fnd2Content -notmatch '15%' -or
    ([regex]::Matches($fnd2Content, '25%')).Count -lt 2 -or
    $fnd2Content -notmatch '35%' -or
    (Get-Content -Raw -LiteralPath (Join-Path $repo 'VERSION')).Trim() -ne '0.73.0'
) {
    throw 'FND-2 is missing its source, version, ownership, workload, assessment, modeling, forecasting, decision, or plain-ASCII contract.'
}

$fnd2Module01Root = Join-Path $repo 'courses\modeling-inference-reproducible-analytics\modules\01-aims-reproducible-workspace'
$fnd2Module01Spec = Join-Path $repo 'docs\curriculum\courses\FND-2\modules\01-aims-reproducible-workspace-spec.md'
$fnd2Module01Files = @(
    'README.md',
    'VERSION',
    'requirements.txt',
    'build_modeling_workspace.py',
    'validate_modeling_workspace.py',
    'data-spec.md',
    'source-record.yml',
    'aim-classification-exercises.csv',
    'aim-and-method-plan.md',
    'estimand-target-registry.csv',
    'feature-role-contract.csv',
    'environment-note.md',
    'reproducibility-check.md',
    'ai-use.md',
    'progression-decision.md',
    'assessment.md',
    'instructor-notes.md',
    'release.json',
    'learner-template\.gitattributes',
    'learner-template\.gitignore',
    'learner-template\README.md',
    'learner-template\VERSION',
    'learner-template\aim-and-method-plan.md',
    'learner-template\estimand-target-registry.csv',
    'learner-template\feature-role-contract.csv',
    'learner-template\environment-note.md',
    'learner-template\reproducibility-check.md',
    'learner-template\ai-use.md',
    'learner-template\progression-decision.md',
    'outputs\modeling-cohort.csv',
    'outputs\split-registry.csv',
    'outputs\baseline-metrics.csv',
    'outputs\modeling-checks.csv',
    'outputs\build-report.json'
)
$fnd2Module01Missing = @($fnd2Module01Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $fnd2Module01Root $_))
})
if (-not (Test-Path -LiteralPath $fnd2Module01Spec) -or $fnd2Module01Missing.Count -gt 0) {
    throw "FND-2 Module 01 is missing its specification or package files: $($fnd2Module01Missing -join ', ')."
}
$fnd2Module01Content = Get-Content -Raw -LiteralPath $fnd2Module01Spec
$fnd2Module01Sections = [regex]::Matches($fnd2Module01Content, '(?m)^## \d+\.').Count
if (
    $fnd2Module01Sections -ne 21 -or
    $fnd2Module01Content -match '[—–]' -or
    $fnd2Module01Content -match '(?im)[A-Z]:\\Users\\' -or
    $fnd2Module01Content -notmatch 'Commons release: 0\.39\.0' -or
    $fnd2Module01Content -notmatch '15937 release checks' -or
    $fnd2Module01Content -notmatch '0\.111607142857' -or
    $fnd2Module01Content -notmatch '6556ed149e69589253ab58572b2f08535899ae12c3e84dc7bafc7da2ebe6f332'
) {
    throw 'FND-2 Module 01 must define 21 plain-ASCII sections with the exact release, validation, baseline, and modeling-cohort contract.'
}
$fnd2Module01Release = Get-Content -Raw -LiteralPath (Join-Path $fnd2Module01Root 'release.json') | ConvertFrom-Json
if (
    $fnd2Module01Release.module.id -ne 'oclc-fnd2-01' -or
    $fnd2Module01Release.module.version -ne '0.1.0' -or
    $fnd2Module01Release.module.commons_release -ne '0.39.0' -or
    $fnd2Module01Release.module.hours -ne 15.5 -or
    $fnd2Module01Release.source.rows -ne 374 -or
    $fnd2Module01Release.source.fields -ne 29 -or
    $fnd2Module01Release.source.sha256 -ne '3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a' -or
    $fnd2Module01Release.outputs.'modeling-cohort.csv'.rows -ne 374 -or
    $fnd2Module01Release.outputs.'modeling-cohort.csv'.fields -ne 34 -or
    $fnd2Module01Release.outputs.'modeling-cohort.csv'.sha256 -ne '6556ed149e69589253ab58572b2f08535899ae12c3e84dc7bafc7da2ebe6f332' -or
    $fnd2Module01Release.split.train.rows -ne 224 -or
    $fnd2Module01Release.split.validation.rows -ne 75 -or
    $fnd2Module01Release.split.test.rows -ne 75 -or
    $fnd2Module01Release.split.train.positives -ne 25 -or
    $fnd2Module01Release.split.validation.positives -ne 7 -or
    $fnd2Module01Release.split.test.positives -ne 4 -or
    $fnd2Module01Release.baseline.constant_probability -ne '0.111607142857' -or
    $fnd2Module01Release.validation.release_checks -ne 15937 -or
    $fnd2Module01Release.validation.starter_checks -ne 15907
) {
    throw 'FND-2 Module 01 release metadata does not match the 0.1.0 modeling-workspace contract.'
}
& python (Join-Path $fnd2Module01Root 'build_modeling_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-2 Module 01 builder self-check failed.'
}
& python (Join-Path $fnd2Module01Root 'validate_modeling_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-2 Module 01 validator self-check failed.'
}

$fnd2Module02Root = Join-Path $repo 'courses\modeling-inference-reproducible-analytics\modules\02-regression-interpretation'
$fnd2Module02Spec = Join-Path $repo 'docs\curriculum\courses\FND-2\modules\02-regression-interpretation-spec.md'
$fnd2Module02Files = @(
    'README.md', 'VERSION', 'requirements.txt', 'build_regression_evidence.py',
    'validate_regression_evidence.py', 'data-spec.md', 'source-record.yml',
    'formula-registry.csv', 'reference-levels.csv', 'interpretation-quantity-guide.csv',
    'paired-models.R', 'regression-interpretation.md', 'environment-note.md',
    'reproducibility-check.md', 'r-run-record.md', 'ai-use.md', 'progression-decision.md',
    'assessment.md', 'instructor-notes.md', 'release.json',
    'learner-template\.gitattributes', 'learner-template\.gitignore',
    'learner-template\README.md', 'learner-template\VERSION',
    'learner-template\formula-registry.csv', 'learner-template\reference-levels.csv',
    'learner-template\interpretation-quantity-guide.csv',
    'learner-template\regression-interpretation.md', 'learner-template\environment-note.md',
    'learner-template\reproducibility-check.md', 'learner-template\r-run-record.md',
    'learner-template\ai-use.md', 'learner-template\progression-decision.md',
    'outputs\linear-subset-registry.csv', 'outputs\linear-coefficients.csv',
    'outputs\linear-diagnostics.csv', 'outputs\linear-prediction-examples.csv',
    'outputs\logistic-coefficients.csv', 'outputs\logistic-diagnostics.csv',
    'outputs\logistic-prediction-examples.csv', 'outputs\model-matrix-fields.csv',
    'outputs\model-comparison.csv', 'outputs\sparse-cell-checks.csv',
    'outputs\assumption-register.csv', 'outputs\r-reading-fixture.csv',
    'outputs\regression-checks.csv', 'outputs\build-report.json'
)
$fnd2Module02Missing = @($fnd2Module02Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $fnd2Module02Root $_))
})
if (-not (Test-Path -LiteralPath $fnd2Module02Spec) -or $fnd2Module02Missing.Count -gt 0) {
    throw "FND-2 Module 02 is missing its specification or package files: $($fnd2Module02Missing -join ', ')."
}
$fnd2Module02Content = Get-Content -Raw -LiteralPath $fnd2Module02Spec
$fnd2Module02Sections = [regex]::Matches($fnd2Module02Content, '(?m)^## \d+\.').Count
if (
    $fnd2Module02Sections -ne 21 -or
    $fnd2Module02Content -match '[—–]' -or
    $fnd2Module02Content -match '(?im)[A-Z]:\\Users\\' -or
    $fnd2Module02Content -notmatch 'Commons release: 0\.40\.0' -or
    $fnd2Module02Content -notmatch '2025 release checks' -or
    $fnd2Module02Content -notmatch '2\.20423495' -or
    $fnd2Module02Content -notmatch '4af1eee015652d064bdc583f931b1191b494910e15c70166dbde5af76375b6f4'
) {
    throw 'FND-2 Module 02 must define 21 plain-ASCII sections with the exact release, regression, validation, and interpretation contract.'
}
$fnd2Module02Release = Get-Content -Raw -LiteralPath (Join-Path $fnd2Module02Root 'release.json') | ConvertFrom-Json
if (
    $fnd2Module02Release.module.id -ne 'oclc-fnd2-02' -or
    $fnd2Module02Release.module.version -ne '0.1.0' -or
    $fnd2Module02Release.module.commons_release -ne '0.40.0' -or
    $fnd2Module02Release.module.hours -ne 16.0 -or
    $fnd2Module02Release.upstream.modeling_cohort_sha256 -ne '6556ed149e69589253ab58572b2f08535899ae12c3e84dc7bafc7da2ebe6f332' -or
    $fnd2Module02Release.linear_case.all_available_rows -ne 111 -or
    $fnd2Module02Release.linear_case.training_fit_rows -ne 69 -or
    $fnd2Module02Release.linear_case.structural_blanks -ne 263 -or
    $fnd2Module02Release.logistic_case.training_rows -ne 224 -or
    $fnd2Module02Release.logistic_case.positive_outcomes -ne 25 -or
    $fnd2Module02Release.logistic_case.prior_acute_odds_ratio -ne '2.20423495' -or
    $fnd2Module02Release.logistic_case.validation_used -ne $false -or
    $fnd2Module02Release.logistic_case.test_used -ne $false -or
    $fnd2Module02Release.outputs.'linear-coefficients.csv'.sha256 -ne '74a1b688949921468149c2d90bbbbfb5c0279331681de7a019fd4a913fc0d1da' -or
    $fnd2Module02Release.outputs.'logistic-coefficients.csv'.sha256 -ne '4af1eee015652d064bdc583f931b1191b494910e15c70166dbde5af76375b6f4' -or
    $fnd2Module02Release.validation.release_checks -ne 2025 -or
    $fnd2Module02Release.validation.starter_checks -ne 1972
) {
    throw 'FND-2 Module 02 release metadata does not match the 0.1.0 regression-evidence contract.'
}
& python (Join-Path $fnd2Module02Root 'build_regression_evidence.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-2 Module 02 builder self-check failed.'
}
& python (Join-Path $fnd2Module02Root 'validate_regression_evidence.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-2 Module 02 validator self-check failed.'
}

$fnd2Module03Root = Join-Path $repo 'courses\modeling-inference-reproducible-analytics\modules\03-prediction-evaluation'
$fnd2Module03Spec = Join-Path $repo 'docs\curriculum\courses\FND-2\modules\03-prediction-evaluation-spec.md'
$fnd2Module03Files = @(
    '.gitattributes', '.gitignore', 'README.md', 'VERSION', 'requirements.txt',
    'build_prediction_evidence.py', 'validate_prediction_evidence.py', 'data-spec.md',
    'source-record.yml', 'model-contract.json', 'prediction-evaluation-report.md',
    'figure-accessibility.md', 'environment-note.md', 'reproducibility-check.md',
    'ai-use.md', 'progression-decision.md', 'assessment.md', 'instructor-notes.md',
    'release.json', 'learner-template\.gitattributes', 'learner-template\.gitignore',
    'learner-template\README.md', 'learner-template\VERSION',
    'learner-template\prediction-evaluation-report.md',
    'learner-template\figure-accessibility.md', 'learner-template\environment-note.md',
    'learner-template\reproducibility-check.md', 'learner-template\ai-use.md',
    'learner-template\progression-decision.md', 'outputs\resampling-results.csv',
    'outputs\validation-predictions.csv', 'outputs\validation-comparison.csv',
    'outputs\model-selection-record.csv', 'outputs\threshold-table.csv',
    'outputs\threshold-decision.csv', 'outputs\test-predictions.csv',
    'outputs\test-metrics.csv', 'outputs\confusion-table.csv',
    'outputs\calibration-table.csv', 'outputs\subgroup-metrics.csv',
    'outputs\transformed-feature-names.csv', 'outputs\leaked-model-failure.csv',
    'outputs\prediction-checks.csv', 'outputs\calibration.svg',
    'outputs\threshold.svg', 'outputs\build-report.json'
)
$fnd2Module03Missing = @($fnd2Module03Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $fnd2Module03Root $_))
})
if (-not (Test-Path -LiteralPath $fnd2Module03Spec) -or $fnd2Module03Missing.Count -gt 0) {
    throw "FND-2 Module 03 is missing its specification or package files: $($fnd2Module03Missing -join ', ')."
}
$fnd2Module03Content = Get-Content -Raw -LiteralPath $fnd2Module03Spec
$fnd2Module03Sections = [regex]::Matches($fnd2Module03Content, '(?m)^## \d+\.').Count
if (
    $fnd2Module03Sections -ne 21 -or
    $fnd2Module03Content -match '[—–]' -or
    $fnd2Module03Content -match '(?im)[A-Z]:\\Users\\' -or
    $fnd2Module03Content -notmatch 'Commons release: 0\.41\.0' -or
    $fnd2Module03Content -notmatch '4601 checks' -or
    $fnd2Module03Content -notmatch '0\.08513264' -or
    $fnd2Module03Content -notmatch '48 / 23 / 2 / 2' -or
    $fnd2Module03Content -notmatch '531c00d310292aeeaea476d1c94e128f5c81c34c2fc60e014d2c157e152b7438'
) {
    throw 'FND-2 Module 03 must define 21 plain-ASCII sections with the exact release, model-selection, threshold, test, and validation contract.'
}
$fnd2Module03Release = Get-Content -Raw -LiteralPath (Join-Path $fnd2Module03Root 'release.json') | ConvertFrom-Json
if (
    $fnd2Module03Release.module.id -ne 'oclc-fnd2-03' -or
    $fnd2Module03Release.module.version -ne '0.1.0' -or
    $fnd2Module03Release.module.commons_release -ne '0.41.0' -or
    $fnd2Module03Release.module.hours -ne 16.5 -or
    $fnd2Module03Release.upstream.modeling_cohort_sha256 -ne '6556ed149e69589253ab58572b2f08535899ae12c3e84dc7bafc7da2ebe6f332' -or
    $fnd2Module03Release.partitions.train -ne 224 -or
    $fnd2Module03Release.partitions.validation -ne 75 -or
    $fnd2Module03Release.partitions.test -ne 75 -or
    $fnd2Module03Release.partitions.training_outcomes -ne 25 -or
    $fnd2Module03Release.partitions.validation_outcomes -ne 7 -or
    $fnd2Module03Release.partitions.test_outcomes -ne 4 -or
    $fnd2Module03Release.selection.model_id -ne 'ML01' -or
    $fnd2Module03Release.selection.locked_threshold -ne '0.08513264' -or
    $fnd2Module03Release.test_confusion.true_negative -ne 48 -or
    $fnd2Module03Release.test_confusion.false_positive -ne 23 -or
    $fnd2Module03Release.test_confusion.false_negative -ne 2 -or
    $fnd2Module03Release.test_confusion.true_positive -ne 2 -or
    $fnd2Module03Release.outputs.'test-predictions.csv'.sha256 -ne '531c00d310292aeeaea476d1c94e128f5c81c34c2fc60e014d2c157e152b7438' -or
    $fnd2Module03Release.validation_record.release_checks -ne 4601 -or
    $fnd2Module03Release.validation_record.starter_checks -ne 4549
) {
    throw 'FND-2 Module 03 release metadata does not match the 0.1.0 prediction-evaluation contract.'
}
& python (Join-Path $fnd2Module03Root 'build_prediction_evidence.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-2 Module 03 builder self-check failed.'
}
& python (Join-Path $fnd2Module03Root 'validate_prediction_evidence.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-2 Module 03 validator self-check failed.'
}

$fnd2Module04Root = Join-Path $repo 'courses\modeling-inference-reproducible-analytics\modules\04-validity-adjustment-longitudinal'
$fnd2Module04Spec = Join-Path $repo 'docs\curriculum\courses\FND-2\modules\04-validity-adjustment-longitudinal-spec.md'
$fnd2Module04Files = @(
    '.gitattributes', '.gitignore', 'README.md', 'VERSION', 'requirements.txt',
    'build_validity_evidence.py', 'validate_validity_evidence.py', 'data-spec.md',
    'source-record.yml', 'assessment.md', 'instructor-notes.md', 'dag.mmd',
    'paired-longitudinal-survival.R', 'causal-claim-screen.md', 'dag-narrative.md',
    'validity-adjustment-longitudinal-memo.md', 'mixed-model-reading.md',
    'survival-censoring-reading.md', 'specialist-referrals.md',
    'reproducibility-check.md', 'accessibility-review.md', 'ai-use.md',
    'progression-decision.md', 'release.json', 'learner-template\.gitattributes',
    'learner-template\.gitignore', 'learner-template\README.md',
    'learner-template\VERSION', 'learner-template\causal-claim-screen.md',
    'learner-template\dag-narrative.md',
    'learner-template\validity-adjustment-longitudinal-memo.md',
    'learner-template\mixed-model-reading.md',
    'learner-template\survival-censoring-reading.md',
    'learner-template\specialist-referrals.md',
    'learner-template\reproducibility-check.md',
    'learner-template\accessibility-review.md', 'learner-template\ai-use.md',
    'learner-template\progression-decision.md', 'outputs\treatment-fixture.csv',
    'outputs\repeated-measures-fixture.csv', 'outputs\survival-fixture.csv',
    'outputs\analytic-aim-validity-map.csv', 'outputs\dag-nodes.csv',
    'outputs\dag-edges.csv', 'outputs\propensity-predictions.csv',
    'outputs\overlap-table.csv', 'outputs\balance-table.csv',
    'outputs\adjustment-estimates.csv', 'outputs\selection-profile.csv',
    'outputs\missingness-profile.csv', 'outputs\missingness-mechanisms.csv',
    'outputs\longitudinal-models.csv', 'outputs\mixed-variance.csv',
    'outputs\kaplan-meier-table.csv', 'outputs\cox-reading.csv',
    'outputs\validity-threat-register.csv', 'outputs\validity-checks.csv',
    'outputs\dag.svg', 'outputs\build-report.json'
)
$fnd2Module04Missing = @($fnd2Module04Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $fnd2Module04Root $_))
})
if (-not (Test-Path -LiteralPath $fnd2Module04Spec) -or $fnd2Module04Missing.Count -gt 0) {
    throw "FND-2 Module 04 is missing its specification or package files: $($fnd2Module04Missing -join ', ')."
}
$fnd2Module04Content = Get-Content -Raw -LiteralPath $fnd2Module04Spec
$fnd2Module04Sections = [regex]::Matches($fnd2Module04Content, '(?m)^## \d+\.').Count
if (
    $fnd2Module04Sections -ne 21 -or
    $fnd2Module04Content -match '[—–]' -or
    $fnd2Module04Content -match '(?im)[A-Z]:\\Users\\' -or
    $fnd2Module04Content -notmatch 'Commons release target: 0\.43\.0' -or
    $fnd2Module04Content -notmatch '36,575 release checks' -or
    $fnd2Module04Content -notmatch '36,512 starter checks' -or
    $fnd2Module04Content -notmatch '0\.83598751' -or
    $fnd2Module04Content -notmatch '0\.67945425' -or
    $fnd2Module04Content -notmatch 'ea82788315dafab0921fd797623741d4ea850e92c3a65b634db32941833dd1c7'
) {
    throw 'FND-2 Module 04 must define 21 plain-ASCII sections with the exact validity, adjustment, longitudinal, survival, and validation contract.'
}
$fnd2Module04Release = Get-Content -Raw -LiteralPath (Join-Path $fnd2Module04Root 'release.json') | ConvertFrom-Json
if (
    $fnd2Module04Release.module.id -ne 'oclc-fnd2-04' -or
    $fnd2Module04Release.module.version -ne '0.1.0' -or
    $fnd2Module04Release.module.commons_release -ne '0.43.0' -or
    $fnd2Module04Release.module.hours -ne 16.5 -or
    $fnd2Module04Release.cases.selection_rows -ne 374 -or
    $fnd2Module04Release.cases.selected_timing_rows -ne 111 -or
    $fnd2Module04Release.cases.structural_blanks -ne 263 -or
    $fnd2Module04Release.cases.treatment_rows -ne 600 -or
    $fnd2Module04Release.cases.missing_severity -ne 91 -or
    $fnd2Module04Release.cases.repeated_rows -ne 2400 -or
    $fnd2Module04Release.cases.repeated_people -ne 600 -or
    $fnd2Module04Release.cases.events -ne 449 -or
    $fnd2Module04Release.cases.censored -ne 151 -or
    $fnd2Module04Release.reference_results.known_ate -ne '-6.00000000' -or
    $fnd2Module04Release.reference_results.icc -ne '0.83598751' -or
    $fnd2Module04Release.reference_results.treatment_hazard_ratio -ne '0.67945425' -or
    $fnd2Module04Release.outputs.'treatment-fixture.csv'.sha256 -ne 'ea82788315dafab0921fd797623741d4ea850e92c3a65b634db32941833dd1c7' -or
    $fnd2Module04Release.outputs.'dag.svg'.sha256 -ne '47533b8d784ac8ef9cc2e2fa54ba587ef0af7a2e8e8feb4b701e027bb0f9bd74' -or
    $fnd2Module04Release.validation_record.release_checks -ne 36575 -or
    $fnd2Module04Release.validation_record.starter_checks -ne 36512
) {
    throw 'FND-2 Module 04 release metadata does not match the 0.1.0 validity-evidence contract.'
}
& python (Join-Path $fnd2Module04Root 'build_validity_evidence.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-2 Module 04 builder self-check failed.'
}
& python (Join-Path $fnd2Module04Root 'validate_validity_evidence.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-2 Module 04 validator self-check failed.'
}

$fnd2Module05Root = Join-Path $repo 'courses\modeling-inference-reproducible-analytics\modules\05-forecasting-temporal-validation'
$fnd2Module05Spec = Join-Path $repo 'docs\curriculum\courses\FND-2\modules\05-forecasting-temporal-validation-spec.md'
$fnd2Module05Files = @(
    '.gitattributes', '.gitignore', 'README.md', 'VERSION', 'requirements.txt',
    'build_forecast_evidence.py', 'validate_forecast_evidence.py', 'data-spec.md',
    'source-record.yml', 'forecast-contract.json', 'assessment.md',
    'instructor-notes.md', 'forecasting-temporal-validation-memo.md',
    'benchmark-defense.md', 'arima-reading.md', 'forecast-text-alternative.md',
    'failure-and-referral.md', 'reproducibility-check.md', 'accessibility-review.md',
    'ai-use.md', 'progression-decision.md', 'release.json',
    'learner-template\.gitattributes', 'learner-template\.gitignore',
    'learner-template\README.md', 'learner-template\VERSION',
    'learner-template\forecasting-temporal-validation-memo.md',
    'learner-template\benchmark-defense.md', 'learner-template\arima-reading.md',
    'learner-template\forecast-text-alternative.md',
    'learner-template\failure-and-referral.md',
    'learner-template\reproducibility-check.md',
    'learner-template\accessibility-review.md', 'learner-template\ai-use.md',
    'learner-template\progression-decision.md', 'outputs\forecast-target.csv',
    'outputs\temporal-folds.csv', 'outputs\benchmark-registry.csv',
    'outputs\forecast-predictions.csv', 'outputs\holt-parameters.csv',
    'outputs\forecast-interval-reading.csv', 'outputs\aggregate-metrics.csv',
    'outputs\fold-metrics.csv', 'outputs\horizon-metrics.csv',
    'outputs\failure-analysis.csv', 'outputs\reporting-coverage-context.csv',
    'outputs\decomposition-reading.csv', 'outputs\stationarity-reading.csv',
    'outputs\arima-parameters.csv', 'outputs\arima-forecast-reading.csv',
    'outputs\residual-diagnostics.csv', 'outputs\forecast-checks.csv',
    'outputs\forecast.svg', 'outputs\build-report.json'
)
$fnd2Module05Missing = @($fnd2Module05Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $fnd2Module05Root $_))
})
if (-not (Test-Path -LiteralPath $fnd2Module05Spec) -or $fnd2Module05Missing.Count -gt 0) {
    throw "FND-2 Module 05 is missing its specification or package files: $($fnd2Module05Missing -join ', ')."
}
$fnd2Module05Content = Get-Content -Raw -LiteralPath $fnd2Module05Spec
$fnd2Module05Sections = [regex]::Matches($fnd2Module05Content, '(?m)^## \d+\.').Count
if (
    $fnd2Module05Sections -ne 21 -or
    $fnd2Module05Content -match '[—–]' -or
    $fnd2Module05Content -match '(?im)[A-Z]:\\Users\\' -or
    $fnd2Module05Content -notmatch 'Commons release target: 0\.44\.0' -or
    $fnd2Module05Content -notmatch '2,666 release validator checks' -or
    $fnd2Module05Content -notmatch '2,604 starter validator checks' -or
    $fnd2Module05Content -notmatch '14\.99587157' -or
    $fnd2Module05Content -notmatch '93\.15000000' -or
    $fnd2Module05Content -notmatch 'dfc91a5e38e2255437dc17a5227cccdb14d4970eb79e14b0260ab203aec8de7a'
) {
    throw 'FND-2 Module 05 must define 21 plain-ASCII sections with the exact source, temporal-fold, forecast, failure, and validation contract.'
}
$fnd2Module05Release = Get-Content -Raw -LiteralPath (Join-Path $fnd2Module05Root 'release.json') | ConvertFrom-Json
if (
    $fnd2Module05Release.module.id -ne 'oclc-fnd2-05' -or
    $fnd2Module05Release.module.version -ne '0.1.0' -or
    $fnd2Module05Release.module.commons_release -ne '0.44.0' -or
    $fnd2Module05Release.module.hours -ne 16.0 -or
    $fnd2Module05Release.source.all_rows -ne 6208 -or
    $fnd2Module05Release.source.massachusetts_rows -ne 94 -or
    $fnd2Module05Release.source.all_sha256 -ne '8a492c3d2d3dae07c42e89ef35ed714d23acab32596f42037dcf8dd0284531d1' -or
    $fnd2Module05Release.source.massachusetts_sha256 -ne '394d9b02d2cc9b4fbf0d9f415db3da6b04393dd9430816973e81fef86fb0e616' -or
    $fnd2Module05Release.backtest.folds -ne 5 -or
    $fnd2Module05Release.backtest.horizon_weeks -ne 4 -or
    $fnd2Module05Release.backtest.targets_per_model -ne 20 -or
    $fnd2Module05Release.reference_results.candidate_mae -ne '14.99587157' -or
    $fnd2Module05Release.reference_results.last_mae -ne '28.20000000' -or
    $fnd2Module05Release.reference_results.seasonal_naive_mae -ne '93.15000000' -or
    $fnd2Module05Release.outputs.'forecast-predictions.csv'.sha256 -ne 'dfc91a5e38e2255437dc17a5227cccdb14d4970eb79e14b0260ab203aec8de7a' -or
    $fnd2Module05Release.outputs.'forecast.svg'.sha256 -ne '10fb417f4450099127afc1ab829c1b7aa6a577facaae2b48c0b1ca6aff2a5458' -or
    $fnd2Module05Release.validation_record.release_checks -ne 2666 -or
    $fnd2Module05Release.validation_record.starter_checks -ne 2604
) {
    throw 'FND-2 Module 05 release metadata does not match the 0.1.0 forecasting-evidence contract.'
}
& python (Join-Path $fnd2Module05Root 'build_forecast_evidence.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-2 Module 05 builder self-check failed.'
}
& python (Join-Path $fnd2Module05Root 'validate_forecast_evidence.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-2 Module 05 validator self-check failed.'
}

$fnd2Module06Root = Join-Path $repo 'courses\modeling-inference-reproducible-analytics\modules\06-agent-assisted-modeling-testing'
$fnd2Module06Spec = Join-Path $repo 'docs\curriculum\courses\FND-2\modules\06-agent-assisted-modeling-testing-spec.md'
$fnd2Module06Files = @(
    '.gitattributes', '.gitignore', 'README.md', 'VERSION', 'requirements.txt',
    'run_contract_tests.py', 'build_agent_test_evidence.py',
    'validate_agent_test_evidence.py', 'data-spec.md', 'source-record.yml',
    'test-contract.json', 'prompt-constraints.md', 'assessment.md',
    'instructor-notes.md', 'agent-task-plan.md', 'prompt-trace-log.csv',
    'agent-critique.md', 'claim-adjudication.csv', 'independent-verification.md',
    'human-sign-off.md', 'reproducibility-check.md', 'accessibility-review.md',
    'ai-use.md', 'progression-decision.md', 'release.json',
    'learner-template\.gitattributes', 'learner-template\.gitignore',
    'learner-template\README.md', 'learner-template\VERSION',
    'learner-template\agent-task-plan.md', 'learner-template\prompt-trace-log.csv',
    'learner-template\agent-critique.md', 'learner-template\claim-adjudication.csv',
    'learner-template\independent-verification.md',
    'learner-template\human-sign-off.md',
    'learner-template\reproducibility-check.md',
    'learner-template\accessibility-review.md', 'learner-template\ai-use.md',
    'learner-template\progression-decision.md',
    'outputs\accepted-artifact-manifest.csv',
    'outputs\accepted-contract-tests.csv', 'outputs\seeded-failure-results.csv',
    'outputs\independent-verification.csv', 'outputs\claim-adjudication.csv',
    'outputs\data-class-rules.csv', 'outputs\test-summary.csv',
    'outputs\failure-fixtures.json', 'outputs\test-summary.md',
    'outputs\build-report.json'
)
$fnd2Module06Missing = @($fnd2Module06Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $fnd2Module06Root $_))
})
if (-not (Test-Path -LiteralPath $fnd2Module06Spec) -or $fnd2Module06Missing.Count -gt 0) {
    throw "FND-2 Module 06 is missing its specification or package files: $($fnd2Module06Missing -join ', ')."
}
$fnd2Module06Content = Get-Content -Raw -LiteralPath $fnd2Module06Spec
$fnd2Module06Sections = [regex]::Matches($fnd2Module06Content, '(?m)^## \d+\.').Count
if (
    $fnd2Module06Sections -ne 21 -or
    $fnd2Module06Content -match '[—–]' -or
    $fnd2Module06Content -match '(?im)[A-Z]:\\Users\\' -or
    $fnd2Module06Content -notmatch 'Commons release target: 0\.45\.0' -or
    $fnd2Module06Content -notmatch '519 release validator checks' -or
    $fnd2Module06Content -notmatch '490 starter validator checks' -or
    $fnd2Module06Content -notmatch '18 accepted tests' -or
    $fnd2Module06Content -notmatch '177f8bab9a8153c884241cbcdf2562b4d8bb53f629068100fa5f48591fc14a2e'
) {
    throw 'FND-2 Module 06 must define 21 plain-ASCII sections with the exact accepted-test, seeded-failure, agent-audit, human-owner, and validation contract.'
}
$fnd2Module06Release = Get-Content -Raw -LiteralPath (Join-Path $fnd2Module06Root 'release.json') | ConvertFrom-Json
if (
    $fnd2Module06Release.module.id -ne 'oclc-fnd2-06' -or
    $fnd2Module06Release.module.version -ne '0.1.0' -or
    $fnd2Module06Release.module.commons_release -ne '0.45.0' -or
    $fnd2Module06Release.module.hours -ne 16.0 -or
    $fnd2Module06Release.tests.accepted_artifacts -ne 13 -or
    $fnd2Module06Release.tests.accepted_tests -ne 18 -or
    $fnd2Module06Release.tests.seeded_failures -ne 10 -or
    $fnd2Module06Release.tests.independent_verifications -ne 3 -or
    $fnd2Module06Release.tests.agent_claims -ne 4 -or
    $fnd2Module06Release.tests.summary_gates -ne 7 -or
    $fnd2Module06Release.fixed_evidence.test_confusion -ne '48/23/2/2' -or
    $fnd2Module06Release.fixed_evidence.candidate_mae -ne '14.99587157' -or
    $fnd2Module06Release.outputs.'seeded-failure-results.csv'.sha256 -ne '177f8bab9a8153c884241cbcdf2562b4d8bb53f629068100fa5f48591fc14a2e' -or
    $fnd2Module06Release.validation_record.release_checks -ne 519 -or
    $fnd2Module06Release.validation_record.starter_checks -ne 490
) {
    throw 'FND-2 Module 06 release metadata does not match the 0.1.0 agent-test contract.'
}
& python (Join-Path $fnd2Module06Root 'build_agent_test_evidence.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-2 Module 06 builder self-check failed.'
}
& python (Join-Path $fnd2Module06Root 'validate_agent_test_evidence.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-2 Module 06 validator self-check failed.'
}

$fnd2Module07Root = Join-Path $repo 'courses\modeling-inference-reproducible-analytics\modules\07-model-cards-governance-defense'
$fnd2Module07Spec = Join-Path $repo 'docs\curriculum\courses\FND-2\modules\07-model-cards-governance-defense-spec.md'
$fnd2Module07Files = @(
    '.gitattributes', '.gitignore', 'README.md', 'VERSION', 'governance-contract.json',
    'assessment.md', 'instructor-notes.md', 'assemble_candidate.py', 'validate_candidate.py',
    'release.json', 'template\README.md', 'template\CHANGELOG.md',
    'template\release-notes.md', 'template\environment-and-commands.md',
    'template\evidence-index.csv', 'template\model-card.md',
    'template\performance-appendix.csv', 'template\subgroup-equity-review.md',
    'template\monitoring-plan.csv', 'template\drift-retraining-versioning.md',
    'template\rollback-stop-retirement.md', 'template\model-use-recommendation.md',
    'template\reproducibility-audit.md', 'template\accessibility-review.md',
    'template\ai-use.md', 'template\human-sign-off.md', 'template\handoff-brief.md',
    'template\technical-defense.md', 'template\component-score.csv',
    'template\gate-results.csv', 'template\release-checklist.csv',
    'template\conditions-register.csv', 'template\reviewer-record.md',
    'template\progression-decision.md', 'reference\README.md', 'reference\CHANGELOG.md',
    'reference\release-notes.md', 'reference\environment-and-commands.md',
    'reference\evidence-index.csv', 'reference\model-card.md',
    'reference\performance-appendix.csv', 'reference\subgroup-equity-review.md',
    'reference\monitoring-plan.csv', 'reference\drift-retraining-versioning.md',
    'reference\rollback-stop-retirement.md', 'reference\model-use-recommendation.md',
    'reference\reproducibility-audit.md', 'reference\accessibility-review.md',
    'reference\ai-use.md', 'reference\human-sign-off.md', 'reference\handoff-brief.md',
    'reference\technical-defense.md', 'reference\component-score.csv',
    'reference\gate-results.csv', 'reference\release-checklist.csv',
    'reference\conditions-register.csv', 'reference\reviewer-record.md',
    'reference\progression-decision.md'
)
$fnd2Module07Missing = @($fnd2Module07Files | Where-Object { -not (Test-Path -LiteralPath (Join-Path $fnd2Module07Root $_)) })
if (-not (Test-Path -LiteralPath $fnd2Module07Spec) -or $fnd2Module07Missing.Count -gt 0) {
    throw "FND-2 Module 07 is missing its specification or package files: $($fnd2Module07Missing -join ', ')."
}
$fnd2Module07Content = Get-Content -Raw -LiteralPath $fnd2Module07Spec
$fnd2Module07Sections = [regex]::Matches($fnd2Module07Content, '(?m)^## \d+\.').Count
if (
    $fnd2Module07Sections -ne 21 -or $fnd2Module07Content -match '[—–]' -or
    $fnd2Module07Content -match '(?im)[A-Z]:\\Users\\' -or
    $fnd2Module07Content -notmatch '0\.47\.0' -or
    $fnd2Module07Content -notmatch '143 immutable manifest rows' -or
    $fnd2Module07Content -notmatch 'ab2537e278ea549b8152434df0a21438394d28caa6031b03e9a570a27db07c1b' -or
    $fnd2Module07Content -notmatch 'Complete reference checks: 880' -or
    $fnd2Module07Content -notmatch 'Learner starter checks: 831'
) { throw 'FND-2 Module 07 must define 21 plain-ASCII sections with the exact candidate, governance, monitoring, validation, and use-decision contract.' }
$fnd2Module07Release = Get-Content -Raw -LiteralPath (Join-Path $fnd2Module07Root 'release.json') | ConvertFrom-Json
if (
    $fnd2Module07Release.module.id -ne 'oclc-fnd2-07' -or
    $fnd2Module07Release.module.version -ne '0.1.0' -or
    $fnd2Module07Release.module.commons_release -ne '0.47.0' -or
    $fnd2Module07Release.module.hours -ne 16.0 -or
    $fnd2Module07Release.package.immutable_manifest_rows -ne 143 -or
    $fnd2Module07Release.package.assembled_files -ne 168 -or
    $fnd2Module07Release.package.manifest_sha256 -ne 'ab2537e278ea549b8152434df0a21438394d28caa6031b03e9a570a27db07c1b' -or
    $fnd2Module07Release.assessment.noncompensable_gates -ne 18 -or
    $fnd2Module07Release.assessment.defense_questions -ne 10 -or
    $fnd2Module07Release.assessment.monitoring_signals -ne 10 -or
    $fnd2Module07Release.validation.complete_reference_checks -ne 880 -or
    $fnd2Module07Release.validation.starter_checks -ne 831 -or
    $fnd2Module07Release.decision.reference_model_use -ne 'teaching use only'
) { throw 'FND-2 Module 07 release metadata does not match the 0.1.0 governed-candidate contract.' }
& python (Join-Path $fnd2Module07Root 'assemble_candidate.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-2 Module 07 assembler self-check failed.' }
& python (Join-Path $fnd2Module07Root 'validate_candidate.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-2 Module 07 validator self-check failed.' }

$fnd2Checkpoint01Root = Join-Path $repo 'courses\modeling-inference-reproducible-analytics\checkpoints\01-modeling-readiness-release'
$fnd2Checkpoint01Spec = Join-Path $repo 'docs\curriculum\courses\FND-2\checkpoints\01-modeling-readiness-release-spec.md'
$fnd2Checkpoint01Files = @(
    '.gitattributes', '.gitignore', 'README.md', 'VERSION', 'checkpoint-contract.json',
    'assessment.md', 'instructor-notes.md', 'assemble_checkpoint.py',
    'validate_checkpoint.py', 'release.json', 'template\README.md',
    'template\cumulative-interpretation.md', 'template\technical-defense.md',
    'template\component-score.csv', 'template\gate-results.csv',
    'template\reviewer-record.md', 'template\reproduction-record.md',
    'template\accessibility-review.md', 'template\ai-use.md',
    'template\progression-decision.md', 'reference\README.md',
    'reference\cumulative-interpretation.md', 'reference\technical-defense.md',
    'reference\component-score.csv', 'reference\gate-results.csv',
    'reference\reviewer-record.md', 'reference\reproduction-record.md',
    'reference\accessibility-review.md', 'reference\ai-use.md',
    'reference\progression-decision.md'
)
$fnd2Checkpoint01Missing = @($fnd2Checkpoint01Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $fnd2Checkpoint01Root $_))
})
if (-not (Test-Path -LiteralPath $fnd2Checkpoint01Spec) -or $fnd2Checkpoint01Missing.Count -gt 0) {
    throw "FND-2 Checkpoint 1 is missing its specification or package files: $($fnd2Checkpoint01Missing -join ', ')."
}
$fnd2Checkpoint01Content = Get-Content -Raw -LiteralPath $fnd2Checkpoint01Spec
$fnd2Checkpoint01Sections = [regex]::Matches($fnd2Checkpoint01Content, '(?m)^## \d+\.').Count
if (
    $fnd2Checkpoint01Sections -ne 17 -or
    $fnd2Checkpoint01Content -match '[—–]' -or
    $fnd2Checkpoint01Content -match '(?im)[A-Z]:\\Users\\' -or
    $fnd2Checkpoint01Content -notmatch 'Commons release target: 0\.42\.0' -or
    $fnd2Checkpoint01Content -notmatch '78-row immutable manifest' -or
    $fnd2Checkpoint01Content -notmatch 'b3760f43e5852ba90150000a4c807bc3aadfedcc688b40c4f16017dc253ca836' -or
    $fnd2Checkpoint01Content -notmatch '500 checks' -or
    $fnd2Checkpoint01Content -notmatch '465 checks' -or
    $fnd2Checkpoint01Content -notmatch '\| H01 \| Cumulative handoff, defense, reviewer evidence, and progression decision \| Checkpoint \| 2\.50 \|' -or
    $fnd2Content -notmatch '\| H01 \| Cumulative handoff, defense, reviewer evidence, and progression decision \| 2\.50 \|'
) {
    throw 'FND-2 Checkpoint 1 must define 17 plain-ASCII sections with the corrected 40-point, manifest, validation, and progression contract.'
}
$fnd2Checkpoint01Release = Get-Content -Raw -LiteralPath (Join-Path $fnd2Checkpoint01Root 'release.json') | ConvertFrom-Json
if (
    $fnd2Checkpoint01Release.checkpoint.id -ne 'oclc-fnd2-cp1' -or
    $fnd2Checkpoint01Release.checkpoint.version -ne '0.1.0' -or
    $fnd2Checkpoint01Release.checkpoint.commons_release -ne '0.42.0' -or
    $fnd2Checkpoint01Release.checkpoint.cumulative_hours -ne 48.0 -or
    $fnd2Checkpoint01Release.checkpoint.course_points -ne 40 -or
    $fnd2Checkpoint01Release.package.module_artifacts -ne 72 -or
    $fnd2Checkpoint01Release.package.immutable_manifest_rows -ne 78 -or
    $fnd2Checkpoint01Release.package.assembled_files -ne 89 -or
    $fnd2Checkpoint01Release.package.manifest_sha256 -ne 'b3760f43e5852ba90150000a4c807bc3aadfedcc688b40c4f16017dc253ca836' -or
    $fnd2Checkpoint01Release.fixed_evidence.selected_model -ne 'ML01' -or
    $fnd2Checkpoint01Release.fixed_evidence.locked_threshold -ne '0.08513264' -or
    $fnd2Checkpoint01Release.fixed_evidence.test_confusion.true_negative -ne 48 -or
    $fnd2Checkpoint01Release.fixed_evidence.test_confusion.false_positive -ne 23 -or
    $fnd2Checkpoint01Release.fixed_evidence.test_confusion.false_negative -ne 2 -or
    $fnd2Checkpoint01Release.fixed_evidence.test_confusion.true_positive -ne 2 -or
    $fnd2Checkpoint01Release.assessment.noncompensable_gates -ne 23 -or
    $fnd2Checkpoint01Release.assessment.defense_questions -ne 12 -or
    $fnd2Checkpoint01Release.validation.complete_reference_checks -ne 500 -or
    $fnd2Checkpoint01Release.validation.starter_checks -ne 465
) {
    throw 'FND-2 Checkpoint 1 release metadata does not match the 0.1.0 cumulative modeling-readiness contract.'
}
& python (Join-Path $fnd2Checkpoint01Root 'assemble_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-2 Checkpoint 1 assembler self-check failed.'
}
& python (Join-Path $fnd2Checkpoint01Root 'validate_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-2 Checkpoint 1 validator self-check failed.'
}

$fnd2Checkpoint02Root = Join-Path $repo 'courses\modeling-inference-reproducible-analytics\checkpoints\02-validity-forecast-testing-release'
$fnd2Checkpoint02Spec = Join-Path $repo 'docs\curriculum\courses\FND-2\checkpoints\02-validity-forecast-testing-release-spec.md'
$fnd2Checkpoint02Files = @(
    '.gitattributes', '.gitignore', 'README.md', 'VERSION', 'checkpoint-contract.json',
    'assessment.md', 'instructor-notes.md', 'assemble_checkpoint.py',
    'validate_checkpoint.py', 'release.json', 'template\README.md',
    'template\cumulative-interpretation.md', 'template\technical-defense.md',
    'template\component-score.csv', 'template\gate-results.csv',
    'template\conditions-register.csv', 'template\reviewer-record.md',
    'template\reproduction-record.md', 'template\accessibility-review.md',
    'template\ai-use.md', 'template\human-sign-off.md',
    'template\progression-decision.md', 'reference\README.md',
    'reference\cumulative-interpretation.md', 'reference\technical-defense.md',
    'reference\component-score.csv', 'reference\gate-results.csv',
    'reference\conditions-register.csv', 'reference\reviewer-record.md',
    'reference\reproduction-record.md', 'reference\accessibility-review.md',
    'reference\ai-use.md', 'reference\human-sign-off.md',
    'reference\progression-decision.md'
)
$fnd2Checkpoint02Missing = @($fnd2Checkpoint02Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $fnd2Checkpoint02Root $_))
})
if (-not (Test-Path -LiteralPath $fnd2Checkpoint02Spec) -or $fnd2Checkpoint02Missing.Count -gt 0) {
    throw "FND-2 Checkpoint 2 is missing its specification or package files: $($fnd2Checkpoint02Missing -join ', ')."
}
$fnd2Checkpoint02Content = Get-Content -Raw -LiteralPath $fnd2Checkpoint02Spec
$fnd2Checkpoint02Sections = [regex]::Matches($fnd2Checkpoint02Content, '(?m)^## \d+\.').Count
if (
    $fnd2Checkpoint02Sections -ne 17 -or
    $fnd2Checkpoint02Content -match '[—–]' -or
    $fnd2Checkpoint02Content -match '(?im)[A-Z]:\\Users\\' -or
    $fnd2Checkpoint02Content -notmatch '0\.46\.0' -or
    $fnd2Checkpoint02Content -notmatch '117 immutable manifest members' -or
    $fnd2Checkpoint02Content -notmatch '16733c55e8a9930f4903006c81e5fb1acb9e75386507f1aa46867daac89f6ccc' -or
    $fnd2Checkpoint02Content -notmatch 'Complete reference checks: 735' -or
    $fnd2Checkpoint02Content -notmatch 'Learner starter checks: 689' -or
    $fnd2Checkpoint02Content -notmatch 'Twenty-five-gate contract' -or
    $fnd2Checkpoint02Content -notmatch 'Human sign-off'
) {
    throw 'FND-2 Checkpoint 2 must define 17 plain-ASCII sections with the exact manifest, 25-point, 25-gate, sign-off, validation, and progression contract.'
}
$fnd2Checkpoint02Release = Get-Content -Raw -LiteralPath (Join-Path $fnd2Checkpoint02Root 'release.json') | ConvertFrom-Json
if (
    $fnd2Checkpoint02Release.checkpoint.id -ne 'oclc-fnd2-cp2' -or
    $fnd2Checkpoint02Release.checkpoint.version -ne '0.1.0' -or
    $fnd2Checkpoint02Release.checkpoint.commons_release -ne '0.46.0' -or
    $fnd2Checkpoint02Release.checkpoint.cumulative_hours -ne 96.5 -or
    $fnd2Checkpoint02Release.checkpoint.course_points -ne 25 -or
    $fnd2Checkpoint02Release.package.upstream_artifacts -ne 111 -or
    $fnd2Checkpoint02Release.package.immutable_manifest_rows -ne 117 -or
    $fnd2Checkpoint02Release.package.assembled_files -ne 130 -or
    $fnd2Checkpoint02Release.package.manifest_sha256 -ne '16733c55e8a9930f4903006c81e5fb1acb9e75386507f1aa46867daac89f6ccc' -or
    $fnd2Checkpoint02Release.fixed_evidence.test_confusion.true_negative -ne 48 -or
    $fnd2Checkpoint02Release.fixed_evidence.test_confusion.false_positive -ne 23 -or
    $fnd2Checkpoint02Release.fixed_evidence.test_confusion.false_negative -ne 2 -or
    $fnd2Checkpoint02Release.fixed_evidence.test_confusion.true_positive -ne 2 -or
    $fnd2Checkpoint02Release.fixed_evidence.cdc_all.rows -ne 6208 -or
    $fnd2Checkpoint02Release.fixed_evidence.massachusetts.rows -ne 94 -or
    $fnd2Checkpoint02Release.fixed_evidence.forecast.candidate_mae -ne '14.99587157' -or
    $fnd2Checkpoint02Release.fixed_evidence.tests.accepted_tests -ne 18 -or
    $fnd2Checkpoint02Release.fixed_evidence.tests.seeded_failures -ne 10 -or
    $fnd2Checkpoint02Release.assessment.noncompensable_gates -ne 25 -or
    $fnd2Checkpoint02Release.assessment.defense_questions -ne 12 -or
    $fnd2Checkpoint02Release.validation.complete_reference_checks -ne 735 -or
    $fnd2Checkpoint02Release.validation.starter_checks -ne 689
) {
    throw 'FND-2 Checkpoint 2 release metadata does not match the 0.1.0 cumulative Week 6 contract.'
}
& python (Join-Path $fnd2Checkpoint02Root 'assemble_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-2 Checkpoint 2 assembler self-check failed.'
}
& python (Join-Path $fnd2Checkpoint02Root 'validate_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-2 Checkpoint 2 validator self-check failed.'
}

$fnd2Checkpoint03Root = Join-Path $repo 'courses\modeling-inference-reproducible-analytics\checkpoints\03-governed-analytics-package'
$fnd2Checkpoint03Spec = Join-Path $repo 'docs\curriculum\courses\FND-2\checkpoints\03-governed-analytics-package-spec.md'
$fnd2Checkpoint03Files = @(
    'README.md', 'VERSION', 'final-contract.json', 'assessment.md',
    'instructor-guide.md', 'assemble_final.py', 'validate_final.py', 'release.json',
    'template\submission-record.md', 'template\final-score.csv',
    'template\gate-results.csv', 'template\final-defense.md',
    'template\reviewer-record.md', 'template\final-reproduction.md',
    'template\conditions-register.csv', 'template\final-audit.md',
    'template\final-decision.md', 'template\release-acceptance.md',
    'reference\submission-record.md', 'reference\final-score.csv',
    'reference\gate-results.csv', 'reference\final-defense.md',
    'reference\reviewer-record.md', 'reference\final-reproduction.md',
    'reference\conditions-register.csv', 'reference\final-audit.md',
    'reference\final-decision.md', 'reference\release-acceptance.md'
)
$fnd2Checkpoint03Missing = @($fnd2Checkpoint03Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $fnd2Checkpoint03Root $_))
})
if (-not (Test-Path -LiteralPath $fnd2Checkpoint03Spec) -or $fnd2Checkpoint03Missing.Count -gt 0) {
    throw "FND-2 final checkpoint is missing its specification or package files: $($fnd2Checkpoint03Missing -join ', ')."
}
$fnd2Checkpoint03Content = Get-Content -Raw -LiteralPath $fnd2Checkpoint03Spec
$fnd2Checkpoint03Sections = [regex]::Matches($fnd2Checkpoint03Content, '(?m)^## \d+\.').Count
if (
    $fnd2Checkpoint03Sections -ne 17 -or
    $fnd2Checkpoint03Content -match '[—–]' -or
    $fnd2Checkpoint03Content -match '(?im)[A-Z]:\\Users\\' -or
    $fnd2Checkpoint03Content -notmatch '0\.48\.0' -or
    $fnd2Checkpoint03Content -notmatch 'exactly 182 files' -or
    $fnd2Checkpoint03Content -notmatch '4fd5b52c94aa038a10faf07372847c5229a394fca0776f8e13f4fc42166dd641' -or
    $fnd2Checkpoint03Content -notmatch 'Complete reference validation passes 947 checks' -or
    $fnd2Checkpoint03Content -notmatch 'Learner-starter validation passes 901 checks' -or
    $fnd2Checkpoint03Content -notmatch 'Twenty-seven noncompensable gates' -or
    $fnd2Checkpoint03Content -notmatch 'teaching use only'
) {
    throw 'FND-2 final checkpoint must define 17 plain-ASCII sections with the exact freeze, 35-point, 27-gate, validation, tag, and separate use-decision contract.'
}
$fnd2Checkpoint03Release = Get-Content -Raw -LiteralPath (Join-Path $fnd2Checkpoint03Root 'release.json') | ConvertFrom-Json
if (
    $fnd2Checkpoint03Release.checkpoint.id -ne 'oclc-fnd2-cp3' -or
    $fnd2Checkpoint03Release.checkpoint.version -ne '0.1.0' -or
    $fnd2Checkpoint03Release.checkpoint.commons_release -ne '0.48.0' -or
    $fnd2Checkpoint03Release.checkpoint.cumulative_hours -ne 112.5 -or
    $fnd2Checkpoint03Release.checkpoint.course_points -ne 35 -or
    $fnd2Checkpoint03Release.accepted_input.candidate_files -ne 168 -or
    $fnd2Checkpoint03Release.accepted_input.module_manifest_rows -ne 143 -or
    $fnd2Checkpoint03Release.accepted_input.module_manifest_sha256 -ne 'ab2537e278ea549b8152434df0a21438394d28caa6031b03e9a570a27db07c1b' -or
    $fnd2Checkpoint03Release.package.candidate_manifest_rows -ne 168 -or
    $fnd2Checkpoint03Release.package.candidate_manifest_bytes -ne 27695 -or
    $fnd2Checkpoint03Release.package.candidate_manifest_sha256 -ne '4fd5b52c94aa038a10faf07372847c5229a394fca0776f8e13f4fc42166dd641' -or
    $fnd2Checkpoint03Release.package.assembled_files -ne 182 -or
    $fnd2Checkpoint03Release.assessment.noncompensable_gates -ne 27 -or
    $fnd2Checkpoint03Release.assessment.defense_questions -ne 15 -or
    $fnd2Checkpoint03Release.decision.reference_package -ne 'accept with conditions' -or
    $fnd2Checkpoint03Release.decision.reference_model_use -ne 'teaching use only' -or
    $fnd2Checkpoint03Release.decision.tag_status -ne 'proposed - not created' -or
    $fnd2Checkpoint03Release.validation.complete_reference_checks -ne 947 -or
    $fnd2Checkpoint03Release.validation.starter_checks -ne 901
) {
    throw 'FND-2 final checkpoint release metadata does not match the 0.1.0 governed final-package contract.'
}
& python (Join-Path $fnd2Checkpoint03Root 'assemble_final.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-2 final checkpoint assembler self-check failed.'
}
& python (Join-Path $fnd2Checkpoint03Root 'validate_final.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'FND-2 final checkpoint validator self-check failed.'
}

$app1 = Join-Path $repo 'docs\curriculum\courses\APP-1\course-spec.md'
$app1Source = Join-Path $repo 'docs\source\app-1-clinical-care-source-record.md'
$app1Package = Join-Path $repo 'courses\clinical-care\README.md'
if (-not (Test-Path -LiteralPath $app1) -or -not (Test-Path -LiteralPath $app1Source) -or -not (Test-Path -LiteralPath $app1Package)) {
    throw 'APP-1 must include its course specification, source record, and course package README.'
}
$app1Content = Get-Content -Raw -LiteralPath $app1
$app1SourceContent = Get-Content -Raw -LiteralPath $app1Source
$app1PackageContent = Get-Content -Raw -LiteralPath $app1Package
$app1Sections = [regex]::Matches($app1Content, '(?m)^## \d+\.').Count
$app1ModuleCount = [regex]::Matches($app1Content, '(?m)^## \d+\. Module \d{2} brief:').Count
$app1HourMatches = [regex]::Matches(
    $app1Content,
    '(?m)^\| \d{2} \| [^|]+ \| \d \| (?<hours>\d+(?:\.\d+)?) \|'
)
$app1Hours = ($app1HourMatches | ForEach-Object { [decimal]$_.Groups['hours'].Value } | Measure-Object -Sum).Sum
$app1CheckpointCount = [regex]::Matches($app1Content, '(?m)^### (?:Checkpoint \d|Final checkpoint):').Count
if (
    $app1Sections -ne 24 -or
    $app1ModuleCount -ne 7 -or
    $app1HourMatches.Count -ne 7 -or
    $app1Hours -ne [decimal]112.5 -or
    $app1CheckpointCount -ne 3
) {
    throw "APP-1 must define 24 course sections, seven modules, seven schedule rows totaling 112.5 hours, and three checkpoints; found $app1Sections sections, $app1ModuleCount modules, $($app1HourMatches.Count) rows, $app1Hours hours, and $app1CheckpointCount checkpoints."
}
if (
    $app1Content -match '[—–]' -or
    $app1SourceContent -match '[—–]' -or
    $app1PackageContent -match '[—–]' -or
    $app1Content -match '(?im)[A-Z]:\\Users\\' -or
    $app1SourceContent -match '(?im)[A-Z]:\\Users\\' -or
    $app1PackageContent -match '(?im)[A-Z]:\\Users\\' -or
    $app1Content -notmatch '00e1ecf99fe3ad365b21e934fca64c225b1a63a00067afcf451a06050a372d57' -or
    $app1SourceContent -notmatch '00e1ecf99fe3ad365b21e934fca64c225b1a63a00067afcf451a06050a372d57' -or
    $app1SourceContent -notmatch '25,134' -or
    $app1SourceContent -notmatch 'Curriculum-30-Credits-2026-08-29\.zip' -or
    $app1SourceContent -notmatch 'OneDrive_2026-08-29 \(1\)\.zip' -or
    $app1Content -notmatch '20 points' -or
    $app1Content -notmatch '45 points' -or
    $app1Content -notmatch '35 points' -or
    $app1Content -notmatch 'eight-hour machine-learning extension' -or
    $app1Content -notmatch 'Joe Joseph, MD' -or
    $app1PackageContent -notmatch 'Commons release: 0\.55\.0' -or
    $app1PackageContent -notmatch 'all seven modules and all three cumulative checkpoints are runnable release candidates'
) {
    throw 'APP-1 is missing its source, version, workload, checkpoint, machine-learning, leadership, or plain-ASCII contract.'
}

$app1Module01Root = Join-Path $repo 'courses\clinical-care\modules\01-care-pathway-decision'
$app1Module01Spec = Join-Path $repo 'docs\curriculum\courses\APP-1\modules\01-care-pathway-decision-spec.md'
$app1Module01Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'decision-contract.json', 'source-record.yml',
    'data-spec.md', 'assessment.md', 'instructor-notes.md', 'profile_source.py',
    'build_workspace.py', 'validate_workspace.py', 'release.json',
    'data\source-table-inventory.csv', 'data\source-feasibility.csv',
    'template\care-pathway-decision-charter.md', 'template\pathway-map.csv',
    'template\outcome-set.csv', 'template\evidence-standard.csv',
    'template\stakeholder-map.csv', 'template\improvement-options.csv',
    'template\source-feasibility-interpretation.md', 'template\ai-use.md',
    'template\progression-decision.md',
    'reference\care-pathway-decision-charter.md', 'reference\pathway-map.csv',
    'reference\outcome-set.csv', 'reference\evidence-standard.csv',
    'reference\stakeholder-map.csv', 'reference\improvement-options.csv',
    'reference\source-feasibility-interpretation.md', 'reference\ai-use.md',
    'reference\progression-decision.md'
)
$app1Module01Missing = @($app1Module01Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $app1Module01Root $_))
})
if (-not (Test-Path -LiteralPath $app1Module01Spec) -or $app1Module01Missing.Count -gt 0) {
    throw "APP-1 Module 01 is missing its specification or package files: $($app1Module01Missing -join ', ')."
}
$app1Module01Content = Get-Content -Raw -LiteralPath $app1Module01Spec
$app1Module01Sections = [regex]::Matches($app1Module01Content, '(?m)^## \d+\.').Count
if (
    $app1Module01Sections -ne 21 -or
    $app1Module01Content -match '[—–]' -or
    $app1Module01Content -match '(?im)[A-Z]:\\Users\\' -or
    $app1Module01Content -notmatch 'Commons release target: 0\.49\.1' -or
    $app1Module01Content -notmatch '132 complete-reference checks' -or
    $app1Module01Content -notmatch '95 learner-starter checks' -or
    $app1Module01Content -notmatch '4f57b0bbf3e510967c5e42691eee990ce523974b7f6ea877f15f46903aa8c147'
) {
    throw 'APP-1 Module 01 must define 21 plain-ASCII sections with the exact release, validation, and manifest contract.'
}
$app1Module01Release = Get-Content -Raw -LiteralPath (Join-Path $app1Module01Root 'release.json') | ConvertFrom-Json
$app1InventoryPath = Join-Path $app1Module01Root 'data\source-table-inventory.csv'
$app1FeasibilityPath = Join-Path $app1Module01Root 'data\source-feasibility.csv'
$app1Inventory = @(Import-Csv -LiteralPath $app1InventoryPath)
$app1Feasibility = @(Import-Csv -LiteralPath $app1FeasibilityPath)
if (
    $app1Module01Release.module.id -ne 'oclc-app1-01' -or
    $app1Module01Release.module.version -ne '0.2.0' -or
    $app1Module01Release.module.commons_release -ne '0.49.1' -or
    $app1Module01Release.module.hours -ne 15.5 -or
    $app1Module01Release.source.tables -ne 16 -or
    $app1Module01Release.source.rows -ne 471836 -or
    $app1Module01Release.source.uncompressed_bytes -ne 82293440 -or
    $app1Module01Release.fixed_evidence.initial_index_cohort -ne 518 -or
    $app1Module01Release.fixed_evidence.index_deaths -ne 9 -or
    $app1Module01Release.fixed_evidence.early_deaths -ne 8 -or
    $app1Module01Release.fixed_evidence.early_acute_returns -ne 25 -or
    $app1Module01Release.fixed_evidence.landmark_eligible -ne 476 -or
    $app1Module01Release.fixed_evidence.scheduled_followup -ne 129 -or
    $app1Module01Release.fixed_evidence.later_acute_returns -ne 87 -or
    $app1Module01Release.fixed_evidence.exposed_later_acute_returns -ne 25 -or
    $app1Module01Release.fixed_evidence.unexposed_later_acute_returns -ne 62 -or
    $app1Module01Release.fixed_evidence.distinct_index_organizations -ne 64 -or
    $app1Module01Release.fixed_evidence.raw_site_comparison -ne 'not ready' -or
    $app1Module01Release.package.immutable_manifest_rows -ne 9 -or
    $app1Module01Release.package.editable_records -ne 9 -or
    $app1Module01Release.package.assembled_files -ne 19 -or
    $app1Module01Release.package.manifest_bytes -ne 1063 -or
    $app1Module01Release.package.manifest_sha256 -ne '4f57b0bbf3e510967c5e42691eee990ce523974b7f6ea877f15f46903aa8c147' -or
    $app1Module01Release.validation.complete_reference_checks -ne 132 -or
    $app1Module01Release.validation.starter_checks -ne 95 -or
    $app1Module01Release.progression.reference -ne 'continue with conditions' -or
    $app1Module01Release.progression.module02_permission -ne 'permitted for curriculum construction' -or
    $app1Inventory.Count -ne 16 -or
    (($app1Inventory | Measure-Object -Property source_rows -Sum).Sum) -ne 471836 -or
    (($app1Inventory | Measure-Object -Property source_bytes -Sum).Sum) -ne 82293440 -or
    $app1Feasibility.Count -ne 12 -or
    (Get-Item -LiteralPath $app1InventoryPath).Length -ne 1842 -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath $app1InventoryPath).Hash.ToLowerInvariant() -ne '15efc286e19c1c6640775770be8993fadc684656262e852c599356751ab922bd' -or
    (Get-Item -LiteralPath $app1FeasibilityPath).Length -ne 1658 -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath $app1FeasibilityPath).Hash.ToLowerInvariant() -ne '8b04bb0f1bc258d8eefae2e04a934f7408baed02a62574c281f8f8513bda5a65'
) {
    throw 'APP-1 Module 01 release metadata or frozen source evidence does not match the 0.2.0 care-pathway decision contract.'
}
& python (Join-Path $app1Module01Root 'profile_source.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'APP-1 Module 01 source profiler self-check failed.'
}
& python (Join-Path $app1Module01Root 'build_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'APP-1 Module 01 builder self-check failed.'
}
& python (Join-Path $app1Module01Root 'validate_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'APP-1 Module 01 validator self-check failed.'
}

$app1Module02Root = Join-Path $repo 'courses\clinical-care\modules\02-longitudinal-cohorts-followup'
$app1Module02Spec = Join-Path $repo 'docs\curriculum\courses\APP-1\modules\02-longitudinal-cohorts-followup-spec.md'
$app1Module02Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'extension-contract.json', 'source-record.yml',
    'data-dictionary.csv', 'phenotype-spec.md', 'transformation-record.md', 'validation-notes.md',
    'reproducibility-check.md', 'ai-use.md', 'progression-decision.md', 'assessment.md',
    'instructor-notes.md', 'build_longitudinal.py', 'build_workspace.py',
    'validate_longitudinal.py', 'release.json',
    'sql\01-index-cohort.sql', 'sql\02-event-audit.sql',
    'sql\03-longitudinal-cohort.sql', 'sql\04-validation.sql',
    'outputs\analysis-cohort.csv', 'outputs\build-report.json',
    'outputs\censoring-summary.csv', 'outputs\cohort-flow.csv',
    'outputs\event-audit.csv', 'outputs\index-cohort.csv',
    'outputs\longitudinal-cohort.csv', 'outputs\query-checks.csv',
    'outputs\site-assignment.csv', 'outputs\site-support.csv',
    'template\README.md', 'template\phenotype-spec.md',
    'template\transformation-record.md', 'template\validation-notes.md',
    'template\reproducibility-check.md', 'template\ai-use.md',
    'template\progression-decision.md',
    'template\sql\01-index-cohort.sql', 'template\sql\02-event-audit.sql',
    'template\sql\03-longitudinal-cohort.sql', 'template\sql\04-validation.sql'
)
$app1Module02Missing = @($app1Module02Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $app1Module02Root $_))
})
if (-not (Test-Path -LiteralPath $app1Module02Spec) -or $app1Module02Missing.Count -gt 0) {
    throw "APP-1 Module 02 is missing its specification or package files: $($app1Module02Missing -join ', ')."
}
$app1Module02Content = Get-Content -Raw -LiteralPath $app1Module02Spec
$app1Module02Sections = [regex]::Matches($app1Module02Content, '(?m)^## \d+\.').Count
if (
    $app1Module02Sections -ne 21 -or
    $app1Module02Content -match '[—–]' -or
    $app1Module02Content -match '(?im)[A-Z]:\\Users\\' -or
    $app1Module02Content -notmatch 'Commons release target: 0\.50\.0' -or
    $app1Module02Content -notmatch '1,140 complete reference checks' -or
    $app1Module02Content -notmatch '82 learner-starter checks' -or
    $app1Module02Content -notmatch '1,150 checks when the complete source database is reproduced' -or
    $app1Module02Content -notmatch '9d78f888753b39797ad421d2576eef377ba0bc01fcca02d9ef3c9da388057c10'
) {
    throw 'APP-1 Module 02 must define 21 plain-ASCII sections with the exact release, validation, and manifest contract.'
}
$app1Module02Release = Get-Content -Raw -LiteralPath (Join-Path $app1Module02Root 'release.json') | ConvertFrom-Json
$app1Module02Outputs = @{
    'analysis-cohort.csv' = @(476, 49, 200699, '558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5')
    'build-report.json' = @($null, $null, 2926, '8829cb8c99e175abc4d9212ff0d3a1ccf6b1b73318ad28e5a5b9c8dd65ceb02f')
    'censoring-summary.csv' = @(6, 6, 372, '46dba77dca430105431b40a1dccb478de0043496193d55ffbc42205435910f95')
    'cohort-flow.csv' = @(5, 6, 446, 'bb9c0828260a5e613a56c97b8fc701d5a9043e72cc2b205cd9df3bddc0635aed')
    'event-audit.csv' = @(1018, 11, 210154, '8491e4c02d33771a904bcc095982cccd6265c3d301c10fc79ac259ceede6fe9c')
    'index-cohort.csv' = @(518, 15, 101751, 'f6f4311cfb617c55c31bb97afac38d328d161bd8e7ec17bb558735abeadf0107')
    'longitudinal-cohort.csv' = @(518, 40, 166746, 'ff684f8dce203c73a4f83e4ee781fe5eff15c0bc3c89652ded9acae906c2f1db')
    'query-checks.csv' = @(26, 2, 640, 'aecd10a6e122dcc34990fac08069cb3cf2339d61ed3eb0cce02beb899861988f')
    'site-assignment.csv' = @(476, 10, 64967, '8cfbd4137e5f9ab8688a2fc88082f283443a913cba1167510e397f09e138964b')
    'site-support.csv' = @(6, 15, 641, 'b76f1ad7f77752e96060ade82d023695afa40d3a24128d2cd191ed0e53cf9088')
}
$app1Module02OutputFailures = @($app1Module02Outputs.GetEnumerator() | Where-Object {
    $path = Join-Path $app1Module02Root "outputs\$($_.Key)"
    $released = $app1Module02Release.outputs.PSObject.Properties[$_.Key].Value
    ($null -ne $_.Value[0] -and $released.rows -ne $_.Value[0]) -or
    ($null -ne $_.Value[1] -and $released.fields -ne $_.Value[1]) -or
    $released.bytes -ne $_.Value[2] -or
    $released.sha256 -ne $_.Value[3] -or
    (Get-Item -LiteralPath $path).Length -ne $_.Value[2] -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash.ToLowerInvariant() -ne $_.Value[3]
})
if (
    $app1Module02Release.module.id -ne 'oclc-app1-02' -or
    $app1Module02Release.module.version -ne '0.1.0' -or
    $app1Module02Release.module.commons_release -ne '0.50.0' -or
    $app1Module02Release.module.hours -ne 16 -or
    $app1Module02Release.upstream.module_version -ne '0.2.0' -or
    $app1Module02Release.upstream.manifest_sha256 -ne '4f57b0bbf3e510967c5e42691eee990ce523974b7f6ea877f15f46903aa8c147' -or
    $app1Module02Release.cohort.initial_people -ne 518 -or
    $app1Module02Release.cohort.landmark_eligible -ne 476 -or
    $app1Module02Release.cohort.later_acute_returns -ne 87 -or
    $app1Module02Release.event_audit.rows -ne 1018 -or
    $app1Module02Release.extension.sites -ne 6 -or
    $app1Module02Release.package.manifest_sha256 -ne '9d78f888753b39797ad421d2576eef377ba0bc01fcca02d9ef3c9da388057c10' -or
    $app1Module02Release.package.data_dictionary_rows -ne 87 -or
    $app1Module02Release.validation.complete_reference_checks -ne 1140 -or
    $app1Module02Release.validation.starter_checks -ne 82 -or
    $app1Module02Release.validation.full_database_reproduction_checks -ne 1150 -or
    $app1Module02Release.validation.copied_workspace_validator_manifest_check -ne 'pass' -or
    $app1Module02Release.progression.reference -ne 'continue with conditions' -or
    $app1Module02Release.progression.module03_permission -ne 'permitted for curriculum construction' -or
    $app1Module02OutputFailures.Count -gt 0
) {
    throw "APP-1 Module 02 release metadata or frozen outputs do not match the longitudinal-cohort contract: $($app1Module02OutputFailures.Key -join ', ')."
}
& python (Join-Path $app1Module02Root 'build_longitudinal.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'APP-1 Module 02 cohort builder self-check failed.'
}
& python (Join-Path $app1Module02Root 'build_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'APP-1 Module 02 workspace builder self-check failed.'
}
& python (Join-Path $app1Module02Root 'validate_longitudinal.py') --self-check
if ($LASTEXITCODE -ne 0) {
    throw 'APP-1 Module 02 validator self-check failed.'
}

$app1Module03Root = Join-Path $repo 'courses\clinical-care\modules\03-survival-time-to-event'
$app1Module03Spec = Join-Path $repo 'docs\curriculum\courses\APP-1\modules\03-survival-time-to-event-spec.md'
$app1Module03Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'source-record.yml', 'analysis-contract.json',
    'environment.yml', 'assessment.md', 'instructor-notes.md', 'paired-survival.R',
    'build_survival.py', 'build_workspace.py', 'validate_survival.py', 'release.json',
    'survival-interpretation.md', 'ph-assessment.md', 'competing-events-note.md',
    'accessibility-review.md', 'reproducibility-check.md', 'ai-use.md', 'progression-decision.md',
    'outputs\analysis-checks.csv', 'outputs\build-report.json', 'outputs\cohort-summary.csv',
    'outputs\cox-model.csv', 'outputs\death-audit.csv', 'outputs\fixed-time-comparison.csv',
    'outputs\km-curve.svg', 'outputs\km-event-table.csv', 'outputs\km-risk-table.csv',
    'outputs\logrank.csv', 'outputs\ph-check.csv',
    'template\README.md', 'template\survival-interpretation.md', 'template\ph-assessment.md',
    'template\competing-events-note.md', 'template\accessibility-review.md',
    'template\reproducibility-check.md', 'template\ai-use.md', 'template\progression-decision.md'
)
$app1Module03Missing = @($app1Module03Files | Where-Object { -not (Test-Path -LiteralPath (Join-Path $app1Module03Root $_)) })
if (-not (Test-Path -LiteralPath $app1Module03Spec) -or $app1Module03Missing.Count -gt 0) {
    throw "APP-1 Module 03 is missing its specification or package files: $($app1Module03Missing -join ', ')."
}
$app1Module03Content = Get-Content -Raw -LiteralPath $app1Module03Spec
$app1Module03Sections = [regex]::Matches($app1Module03Content, '(?m)^## \d+\.').Count
if (
    $app1Module03Sections -ne 21 -or
    $app1Module03Content -match '[—–]' -or
    $app1Module03Content -match '(?im)[A-Z]:\\Users\\' -or
    $app1Module03Content -notmatch 'Commons release target: 0\.51\.0' -or
    $app1Module03Content -notmatch '476-person risk set' -or
    $app1Module03Content -notmatch 'Schoenfeld residual' -or
    $app1Module03Content -notmatch 'cumulative Week 3 checkpoint' -or
    $app1Module03Content -notmatch '067e1953d7fe7bcfaf878880bef2edf44788b846f71c478282ebe34f1a5d4d52' -or
    $app1Module03Content -notmatch '131 checks' -or
    $app1Module03Content -notmatch '74 checks'
) {
    throw 'APP-1 Module 03 must define 21 plain-ASCII sections with the exact frozen cohort, PH-screen, validation, and manifest contracts.'
}
$app1Module03Release = Get-Content -Raw -LiteralPath (Join-Path $app1Module03Root 'release.json') | ConvertFrom-Json
$app1Module03OutputNames = @('analysis-checks.csv', 'build-report.json', 'cohort-summary.csv', 'cox-model.csv', 'death-audit.csv', 'fixed-time-comparison.csv', 'km-curve.svg', 'km-event-table.csv', 'km-risk-table.csv', 'logrank.csv', 'ph-check.csv')
$app1Module03OutputFailures = @($app1Module03OutputNames | Where-Object {
    $path = Join-Path $app1Module03Root "outputs\$_"
    $metadata = $app1Module03Release.outputs.PSObject.Properties[$_].Value
    -not $metadata -or (Get-Item -LiteralPath $path).Length -ne $metadata.bytes -or (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash.ToLowerInvariant() -ne $metadata.sha256
})
if (
    $app1Module03Release.module.id -ne 'oclc-app1-03' -or
    $app1Module03Release.module.version -ne '0.1.0' -or
    $app1Module03Release.module.commons_release -ne '0.51.0' -or
    $app1Module03Release.module.hours -ne 16.5 -or
    $app1Module03Release.module.new_course_points -ne 0 -or
    $app1Module03Release.upstream.analysis_cohort_sha256 -ne '558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5' -or
    $app1Module03Release.cohort.people -ne 476 -or
    $app1Module03Release.cohort.events -ne 87 -or
    $app1Module03Release.cohort.administrative_censors -ne 389 -or
    $app1Module03Release.reference_results.logrank_p_value -ne '0.67258471' -or
    $app1Module03Release.reference_results.cox_hazard_ratio -ne '1.10542457' -or
    $app1Module03Release.reference_results.ph_p_value -ne '0.00636020' -or
    $app1Module03Release.reference_results.ph_screen_result -ne 'fail' -or
    $app1Module03Release.package.output_files -ne 11 -or
    $app1Module03Release.package.output_bytes -ne 70204 -or
    $app1Module03Release.package.manifest_sha256 -ne '067e1953d7fe7bcfaf878880bef2edf44788b846f71c478282ebe34f1a5d4d52' -or
    $app1Module03Release.validation.complete_reference_checks -ne 131 -or
    $app1Module03Release.validation.starter_checks -ne 74 -or
    $app1Module03Release.progression.reference -ne 'continue with conditions' -or
    $app1Module03Release.progression.module04_permission -ne 'permitted for curriculum construction' -or
    $app1Module03OutputFailures.Count -gt 0
) {
    throw "APP-1 Module 03 release metadata or frozen outputs do not match the survival contract: $($app1Module03OutputFailures -join ', ')."
}
& python (Join-Path $app1Module03Root 'build_survival.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-1 Module 03 survival builder self-check failed.' }
& python (Join-Path $app1Module03Root 'build_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-1 Module 03 workspace builder self-check failed.' }
& python (Join-Path $app1Module03Root 'validate_survival.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-1 Module 03 validator self-check failed.' }

$app1Checkpoint01Root = Join-Path $repo 'courses\clinical-care\checkpoints\01-longitudinal-survival-readiness'
$app1Checkpoint01Spec = Join-Path $repo 'docs\curriculum\courses\APP-1\checkpoints\01-longitudinal-survival-readiness-spec.md'
$app1Checkpoint01Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'checkpoint-contract.json', 'assessment.md',
    'instructor-notes.md', 'build_checkpoint.py', 'validate_checkpoint.py', 'release.json',
    'evidence-index.csv', 'survival-readiness-review.md', 'reproducibility-check.md',
    'ai-use.md', 'progression-decision.md',
    'template\README.md', 'template\evidence-index.csv', 'template\survival-readiness-review.md',
    'template\reproducibility-check.md', 'template\ai-use.md', 'template\progression-decision.md'
)
$app1Checkpoint01Missing = @($app1Checkpoint01Files | Where-Object { -not (Test-Path -LiteralPath (Join-Path $app1Checkpoint01Root $_)) })
if (-not (Test-Path -LiteralPath $app1Checkpoint01Spec) -or $app1Checkpoint01Missing.Count -gt 0) {
    throw "APP-1 Checkpoint 1 is missing its specification or package files: $($app1Checkpoint01Missing -join ', ')."
}
$app1Checkpoint01Content = Get-Content -Raw -LiteralPath $app1Checkpoint01Spec
$app1Checkpoint01Sections = [regex]::Matches($app1Checkpoint01Content, '(?m)^## \d+\.').Count
if (
    $app1Checkpoint01Sections -ne 17 -or
    $app1Checkpoint01Content -match '[—–]' -or
    $app1Checkpoint01Content -match '(?im)[A-Z]:\\Users\\' -or
    $app1Checkpoint01Content -notmatch 'Commons release target: 0\.51\.0' -or
    $app1Checkpoint01Content -notmatch 'ef5ace3d6b450473f5b7ab8c1b53bf24f63aa42910b1fdab5d72c617f4f57860' -or
    $app1Checkpoint01Content -notmatch '394 checks' -or
    $app1Checkpoint01Content -notmatch '379 checks'
) {
    throw 'APP-1 Checkpoint 1 must define 17 plain-ASCII sections with exact component, score, manifest, and validation contracts.'
}
$app1Checkpoint01Release = Get-Content -Raw -LiteralPath (Join-Path $app1Checkpoint01Root 'release.json') | ConvertFrom-Json
if (
    $app1Checkpoint01Release.checkpoint.id -ne 'oclc-app1-cp01' -or
    $app1Checkpoint01Release.checkpoint.version -ne '0.1.0' -or
    $app1Checkpoint01Release.checkpoint.commons_release -ne '0.51.0' -or
    $app1Checkpoint01Release.checkpoint.course_points -ne 20 -or
    $app1Checkpoint01Release.accepted_modules.Count -ne 3 -or
    $app1Checkpoint01Release.evidence.landmark_people -ne 476 -or
    $app1Checkpoint01Release.evidence.events -ne 87 -or
    $app1Checkpoint01Release.evidence.ph_screen_result -ne 'fail' -or
    $app1Checkpoint01Release.assessment.checkpoint_score -ne '20.00 of 20.00' -or
    $app1Checkpoint01Release.package.accepted_component_files -ne 78 -or
    $app1Checkpoint01Release.package.reference_files -ne 91 -or
    $app1Checkpoint01Release.package.candidate_manifest_sha256 -ne 'ef5ace3d6b450473f5b7ab8c1b53bf24f63aa42910b1fdab5d72c617f4f57860' -or
    $app1Checkpoint01Release.validation.reference_checks -ne 394 -or
    $app1Checkpoint01Release.validation.learner_checks -ne 379 -or
    $app1Checkpoint01Release.progression.reference -ne 'continue with conditions' -or
    $app1Checkpoint01Release.progression.module04_permission -ne 'permitted for curriculum construction'
) {
    throw 'APP-1 Checkpoint 1 release metadata does not match the cumulative Week 3 contract.'
}
& python (Join-Path $app1Checkpoint01Root 'build_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-1 Checkpoint 1 builder self-check failed.' }
& python (Join-Path $app1Checkpoint01Root 'validate_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-1 Checkpoint 1 validator self-check failed.' }

$app1Module04Root = Join-Path $repo 'courses\clinical-care\modules\04-risk-adjustment-fair-comparison'
$app1Module04Spec = Join-Path $repo 'docs\curriculum\courses\APP-1\modules\04-risk-adjustment-fair-comparison-spec.md'
$app1Module04Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'source-record.yml', 'adjustment-contract.json',
    'environment.yml', 'assessment.md', 'field-role-contract.csv', 'instructor-notes.md',
    'paired-risk-adjustment.R', 'build_adjustment.py', 'build_workspace.py',
    'validate_adjustment.py', 'release.json', 'risk-adjustment-memo.md', 'model-assessment.md',
    'support-suppression-review.md', 'fair-comparison-interpretation.md',
    'reproducibility-check.md', 'ai-use.md', 'progression-decision.md',
    'outputs\adjusted-association.csv', 'outputs\analysis-checks.csv',
    'outputs\bootstrap-stability.csv', 'outputs\build-report.json',
    'outputs\calibration-quintiles.csv', 'outputs\comparison-figure.svg',
    'outputs\expected-outcomes.csv', 'outputs\exposure-comparison.csv',
    'outputs\field-role-summary.csv', 'outputs\model-coefficients.csv',
    'outputs\model-performance.csv', 'outputs\site-case-mix.csv', 'outputs\site-comparison.csv',
    'template\README.md', 'template\risk-adjustment-memo.md', 'template\model-assessment.md',
    'template\support-suppression-review.md', 'template\fair-comparison-interpretation.md',
    'template\reproducibility-check.md', 'template\ai-use.md', 'template\progression-decision.md'
)
$app1Module04Missing = @($app1Module04Files | Where-Object { -not (Test-Path -LiteralPath (Join-Path $app1Module04Root $_)) })
if (-not (Test-Path -LiteralPath $app1Module04Spec) -or $app1Module04Missing.Count -gt 0) {
    throw "APP-1 Module 04 is missing its specification or package files: $($app1Module04Missing -join ', ')."
}
$app1Module04Content = Get-Content -Raw -LiteralPath $app1Module04Spec
$app1Module04Sections = [regex]::Matches($app1Module04Content, '(?m)^## \d+\.').Count
if (
    $app1Module04Sections -ne 21 -or
    $app1Module04Content -match '[—–]' -or
    $app1Module04Content -match '(?im)[A-Z]:\\Users\\' -or
    $app1Module04Content -notmatch 'Commons release target: 0\.52\.0' -or
    $app1Module04Content -notmatch 'fixed 335-day outcome' -or
    $app1Module04Content -notmatch 'all 49 fields classified' -or
    $app1Module04Content -notmatch '300 person-level bootstrap samples' -or
    $app1Module04Content -notmatch '5eaf8ba19e965b437cd4c586a1811b6d4aeb0f5cc82ea585dae2405432c9a8bb' -or
    $app1Module04Content -notmatch '155 checks' -or
    $app1Module04Content -notmatch '85 checks' -or
    $app1Module04Content -notmatch '122 checks'
) {
    throw 'APP-1 Module 04 must define 21 plain-ASCII sections with the exact field-role, adjustment, support, validation, and manifest contracts.'
}
$app1Module04Release = Get-Content -Raw -LiteralPath (Join-Path $app1Module04Root 'release.json') | ConvertFrom-Json
$app1Module04OutputNames = @(
    'adjusted-association.csv', 'analysis-checks.csv', 'bootstrap-stability.csv', 'build-report.json',
    'calibration-quintiles.csv', 'comparison-figure.svg', 'expected-outcomes.csv',
    'exposure-comparison.csv', 'field-role-summary.csv', 'model-coefficients.csv',
    'model-performance.csv', 'site-case-mix.csv', 'site-comparison.csv'
)
$app1Module04OutputFailures = @($app1Module04OutputNames | Where-Object {
    $path = Join-Path $app1Module04Root "outputs\$_"
    $metadata = $app1Module04Release.outputs.PSObject.Properties[$_].Value
    -not $metadata -or (Get-Item -LiteralPath $path).Length -ne $metadata.bytes -or (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash.ToLowerInvariant() -ne $metadata.sha256
})
if (
    $app1Module04Release.module.id -ne 'oclc-app1-04' -or
    $app1Module04Release.module.version -ne '0.1.0' -or
    $app1Module04Release.module.commons_release -ne '0.52.0' -or
    $app1Module04Release.module.hours -ne 16.5 -or
    $app1Module04Release.module.cumulative_component_points -ne 25 -or
    $app1Module04Release.upstream.checkpoint_manifest_sha256 -ne 'ef5ace3d6b450473f5b7ab8c1b53bf24f63aa42910b1fdab5d72c617f4f57860' -or
    $app1Module04Release.upstream.analysis_cohort_sha256 -ne '558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5' -or
    $app1Module04Release.cohort.people -ne 476 -or
    $app1Module04Release.cohort.events -ne 87 -or
    $app1Module04Release.reference_results.brier_score_apparent -ne '0.13490621' -or
    $app1Module04Release.reference_results.roc_auc_apparent -ne '0.66585409' -or
    $app1Module04Release.reference_results.adjusted_exposure_odds_ratio -ne '1.16353250' -or
    $app1Module04Release.reference_results.sites_report_with_caution -ne 6 -or
    $app1Module04Release.reference_results.known_direct_site_effect -ne 0 -or
    $app1Module04Release.outputs.'expected-outcomes.csv'.rows -ne 476 -or
    $app1Module04Release.outputs.'site-comparison.csv'.rows -ne 6 -or
    $app1Module04Release.package.output_files -ne 13 -or
    $app1Module04Release.package.output_bytes -ne 128209 -or
    $app1Module04Release.package.manifest_sha256 -ne '5eaf8ba19e965b437cd4c586a1811b6d4aeb0f5cc82ea585dae2405432c9a8bb' -or
    $app1Module04Release.validation.complete_reference_checks -ne 155 -or
    $app1Module04Release.validation.starter_checks -ne 85 -or
    $app1Module04Release.validation.module_root_checks -ne 122 -or
    $app1Module04Release.assessment.reference_gates_passed -ne 18 -or
    $app1Module04Release.progression.reference -ne 'continue with conditions' -or
    $app1Module04Release.progression.module05_permission -ne 'permitted for curriculum construction' -or
    $app1Module04OutputFailures.Count -gt 0
) {
    throw "APP-1 Module 04 release metadata or frozen outputs do not match the risk-adjustment contract: $($app1Module04OutputFailures -join ', ')."
}
& python (Join-Path $app1Module04Root 'build_adjustment.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-1 Module 04 adjustment builder self-check failed.' }
& python (Join-Path $app1Module04Root 'build_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-1 Module 04 workspace builder self-check failed.' }
& python (Join-Path $app1Module04Root 'validate_adjustment.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-1 Module 04 validator self-check failed.' }

$app1Module05Root = Join-Path $repo 'courses\clinical-care\modules\05-clinical-variation-patterns-of-care'
$app1Module05Spec = Join-Path $repo 'docs\curriculum\courses\APP-1\modules\05-clinical-variation-patterns-of-care-spec.md'
$app1Module05Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'source-record.yml', 'variation-contract.json',
    'environment.yml', 'assessment.md', 'measure-contract.csv', 'instructor-notes.md',
    'build_variation.py', 'build_workspace.py', 'validate_variation.py', 'release.json',
    'variation-memo.md', 'measure-interpretation.md', 'support-suppression-review.md',
    'claim-audit.csv', 'handoff-to-module06.md', 'reproducibility-check.md', 'ai-use.md',
    'progression-decision.md', 'outputs\analysis-checks.csv', 'outputs\build-report.json',
    'outputs\care-patterns.csv', 'outputs\clinical-subgroup-variation.csv',
    'outputs\exposure-variation.csv', 'outputs\measure-summary.csv', 'outputs\record-mix.csv',
    'outputs\site-summary.csv', 'outputs\site-variation.csv', 'outputs\time-variation.csv',
    'outputs\variation-figure.svg', 'template\README.md', 'template\variation-memo.md',
    'template\measure-interpretation.md', 'template\support-suppression-review.md',
    'template\claim-audit.csv', 'template\handoff-to-module06.md',
    'template\reproducibility-check.md', 'template\ai-use.md', 'template\progression-decision.md'
)
$app1Module05Missing = @($app1Module05Files | Where-Object { -not (Test-Path -LiteralPath (Join-Path $app1Module05Root $_)) })
if (-not (Test-Path -LiteralPath $app1Module05Spec) -or $app1Module05Missing.Count -gt 0) {
    throw "APP-1 Module 05 is missing its specification or package files: $($app1Module05Missing -join ', ')."
}
$app1Module05Content = Get-Content -Raw -LiteralPath $app1Module05Spec
$app1Module05Sections = [regex]::Matches($app1Module05Content, '(?m)^## \d+\.').Count
if (
    $app1Module05Sections -ne 21 -or
    $app1Module05Content -match '[—–]' -or
    $app1Module05Content -match '(?im)[A-Z]:\\Users\\' -or
    $app1Module05Content -notmatch 'Commons release target: 0\.53\.0' -or
    $app1Module05Content -notmatch 'medication order is treatment-record exposure and not medication adherence' -or
    $app1Module05Content -notmatch '0\.14816372' -or
    $app1Module05Content -notmatch '0\.27993975' -or
    $app1Module05Content -notmatch '7106a0ec0b412c61768eff72f03062e60cb3d9dfc0a887bb81be8f4475e7363e' -or
    $app1Module05Content -notmatch '129 checks' -or
    $app1Module05Content -notmatch '159 checks' -or
    $app1Module05Content -notmatch '82 checks'
) {
    throw 'APP-1 Module 05 must define 21 plain-ASCII sections with the exact source, measure, variation, support, validation, and manifest contracts.'
}
$app1Module05Release = Get-Content -Raw -LiteralPath (Join-Path $app1Module05Root 'release.json') | ConvertFrom-Json
$app1Module05OutputNames = @(
    'analysis-checks.csv', 'build-report.json', 'care-patterns.csv', 'clinical-subgroup-variation.csv',
    'exposure-variation.csv', 'measure-summary.csv', 'record-mix.csv', 'site-summary.csv',
    'site-variation.csv', 'time-variation.csv', 'variation-figure.svg'
)
$app1Module05OutputFailures = @($app1Module05OutputNames | Where-Object {
    $path = Join-Path $app1Module05Root "outputs\$_"
    $metadata = $app1Module05Release.outputs.PSObject.Properties[$_].Value
    -not $metadata -or (Get-Item -LiteralPath $path).Length -ne $metadata.bytes -or (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash.ToLowerInvariant() -ne $metadata.sha256
})
if (
    $app1Module05Release.module.id -ne 'oclc-app1-05' -or
    $app1Module05Release.module.version -ne '0.1.0' -or
    $app1Module05Release.module.commons_release -ne '0.53.0' -or
    $app1Module05Release.module.hours -ne 16.0 -or
    $app1Module05Release.module.course_points -ne 20 -or
    $app1Module05Release.upstream.module04_manifest_sha256 -ne '5eaf8ba19e965b437cd4c586a1811b6d4aeb0f5cc82ea585dae2405432c9a8bb' -or
    $app1Module05Release.upstream.analysis_cohort_sha256 -ne '558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5' -or
    $app1Module05Release.upstream.expected_outcomes_sha256 -ne 'e6c4efbe845bc1047040d27760aa22cf63a462ba4cca6709d6bdff8578af840e' -or
    $app1Module05Release.source.synthea_sqlite_sha256 -ne '1116dda22c4297fcfeab6bf2c99bb3dbfaf9f9b5e04041b96be90719c76e704a' -or
    $app1Module05Release.source.generated_clinical_rows -ne 0 -or
    $app1Module05Release.reference_results.people -ne 476 -or
    $app1Module05Release.reference_results.recorded_followup -ne 129 -or
    $app1Module05Release.reference_results.later_acute_returns -ne 87 -or
    $app1Module05Release.reference_results.site_recorded_followup_range -ne '0.14816372' -or
    $app1Module05Release.reference_results.site_recorded_followup_global_p -ne '0.27993975' -or
    $app1Module05Release.reference_results.known_direct_site_effect -ne 0 -or
    $app1Module05Release.outputs.'care-patterns.csv'.rows -ne 476 -or
    $app1Module05Release.outputs.'site-variation.csv'.rows -ne 36 -or
    $app1Module05Release.package.output_files -ne 11 -or
    $app1Module05Release.package.output_bytes -ne 180851 -or
    $app1Module05Release.package.manifest_sha256 -ne '7106a0ec0b412c61768eff72f03062e60cb3d9dfc0a887bb81be8f4475e7363e' -or
    $app1Module05Release.validation.complete_reference_checks -ne 159 -or
    $app1Module05Release.validation.starter_checks -ne 82 -or
    $app1Module05Release.validation.module_root_checks -ne 129 -or
    $app1Module05Release.assessment.reference_gates_passed -ne 18 -or
    $app1Module05Release.progression.reference -ne 'continue with conditions' -or
    $app1Module05Release.progression.module06_permission -ne 'permitted for curriculum construction' -or
    $app1Module05OutputFailures.Count -gt 0
) {
    throw "APP-1 Module 05 release metadata or frozen outputs do not match the clinical-variation contract: $($app1Module05OutputFailures -join ', ')."
}
& python (Join-Path $app1Module05Root 'build_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-1 Module 05 workspace builder self-check failed.' }
& python (Join-Path $app1Module05Root 'validate_variation.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-1 Module 05 validator self-check failed.' }

$app1Module06Root = Join-Path $repo 'courses\clinical-care\modules\06-equity-improvement-embedded-ml'
$app1Module06Spec = Join-Path $repo 'docs\curriculum\courses\APP-1\modules\06-equity-improvement-embedded-ml-spec.md'
$app1Module06Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'source-record.yml', 'equity-contract.csv',
    'model-contract.json', 'feature-contract.csv', 'environment.yml', 'assessment.md',
    'instructor-notes.md', 'build_equity_improvement.py', 'build_workspace.py',
    'validate_equity_improvement.py', 'release.json', 'equity-review.md',
    'pathway-display.md', 'improvement-brief.md', 'driver-diagram.csv',
    'improvement-measures.csv', 'ml-comparison.md', 'failure-case-review.md',
    'reproducibility-check.md', 'ai-use.md', 'progression-decision.md',
    'outputs\analysis-checks.csv', 'outputs\bootstrap-comparison.csv',
    'outputs\build-report.json', 'outputs\calibration-bins.csv', 'outputs\equity-summary.csv',
    'outputs\failure-cases.csv', 'outputs\feature-importance.csv',
    'outputs\model-performance.csv', 'outputs\model-predictions.csv',
    'outputs\pathway-edges.csv', 'outputs\pathway-figure.svg', 'outputs\pathway-nodes.csv',
    'outputs\split-registry.csv', 'outputs\subgroup-model-audit.csv',
    'outputs\threshold-errors.csv', 'template\README.md', 'template\equity-review.md',
    'template\pathway-display.md', 'template\improvement-brief.md',
    'template\driver-diagram.csv', 'template\improvement-measures.csv',
    'template\ml-comparison.md', 'template\failure-case-review.md',
    'template\reproducibility-check.md', 'template\ai-use.md',
    'template\progression-decision.md'
)
$app1Module06Missing = @($app1Module06Files | Where-Object { -not (Test-Path -LiteralPath (Join-Path $app1Module06Root $_)) })
if (-not (Test-Path -LiteralPath $app1Module06Spec) -or $app1Module06Missing.Count -gt 0) {
    throw "APP-1 Module 06 is missing its specification or package files: $($app1Module06Missing -join ', ')."
}
$app1Module06Content = Get-Content -Raw -LiteralPath $app1Module06Spec
$app1Module06Sections = [regex]::Matches($app1Module06Content, '(?m)^## \d+\.').Count
if (
    $app1Module06Sections -ne 21 -or
    $app1Module06Content -match '[—–]' -or
    $app1Module06Content -match '(?im)[A-Z]:\\Users\\' -or
    $app1Module06Content -notmatch 'Commons release at first runnable release: `0\.54\.0`' -or
    $app1Module06Content -notmatch 'b7127dbfac9e7a9549ea682499a1ca5d368a4acbbc20da2e307324be5813b978' -or
    $app1Module06Content -notmatch '0\.09609243' -or
    $app1Module06Content -notmatch '0\.10745654' -or
    $app1Module06Content -notmatch 'Module 06 earns no additional points' -or
    $app1Module06Content -notmatch '153 checks' -or
    $app1Module06Content -notmatch '189 checks' -or
    $app1Module06Content -notmatch '100 starter checks'
) {
    throw 'APP-1 Module 06 must define 21 plain-ASCII sections with the exact equity, improvement, ML, score, validation, and manifest contracts.'
}
$app1Module06Release = Get-Content -Raw -LiteralPath (Join-Path $app1Module06Root 'release.json') | ConvertFrom-Json
$app1Module06OutputNames = @(
    'analysis-checks.csv', 'bootstrap-comparison.csv', 'build-report.json', 'calibration-bins.csv',
    'equity-summary.csv', 'failure-cases.csv', 'feature-importance.csv', 'model-performance.csv',
    'model-predictions.csv', 'pathway-edges.csv', 'pathway-figure.svg', 'pathway-nodes.csv',
    'split-registry.csv', 'subgroup-model-audit.csv', 'threshold-errors.csv'
)
$app1Module06OutputFailures = @($app1Module06OutputNames | Where-Object {
    $path = Join-Path $app1Module06Root "outputs\$_"
    $metadata = $app1Module06Release.outputs.PSObject.Properties[$_].Value
    -not $metadata -or (Get-Item -LiteralPath $path).Length -ne $metadata.bytes -or (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash.ToLowerInvariant() -ne $metadata.sha256
})
if (
    $app1Module06Release.module.id -ne 'oclc-app1-06' -or
    $app1Module06Release.module.version -ne '0.1.0' -or
    $app1Module06Release.module.commons_release -ne '0.54.0' -or
    $app1Module06Release.module.hours -ne 16.0 -or
    $app1Module06Release.module.course_points -ne 0 -or
    $app1Module06Release.module.checkpoint_points -ne 45 -or
    $app1Module06Release.upstream.module05_manifest_sha256 -ne '7106a0ec0b412c61768eff72f03062e60cb3d9dfc0a887bb81be8f4475e7363e' -or
    $app1Module06Release.upstream.care_patterns_sha256 -ne 'c5d372e777ff3b190859e7c418b87c4f165776b84fb86346db700fa39f516a6e' -or
    $app1Module06Release.reference_results.people -ne 476 -or
    $app1Module06Release.reference_results.training_rows -ne 333 -or
    $app1Module06Release.reference_results.evaluation_rows -ne 143 -or
    $app1Module06Release.reference_results.evaluation_events -ne 17 -or
    $app1Module06Release.reference_results.transparent_brier -ne '0.09609243' -or
    $app1Module06Release.reference_results.bounded_rf_brier -ne '0.10745654' -or
    $app1Module06Release.reference_results.transparent_auc -ne '0.66363212' -or
    $app1Module06Release.reference_results.bounded_rf_auc -ne '0.62371615' -or
    $app1Module06Release.reference_results.ml_changes_decision -ne 'no' -or
    $app1Module06Release.reference_results.clinical_implementation -ne 'prohibited' -or
    $app1Module06Release.reference_results.model_deployment -ne 'prohibited' -or
    $app1Module06Release.package.output_files -ne 15 -or
    $app1Module06Release.package.output_bytes -ne 78042 -or
    $app1Module06Release.package.manifest_sha256 -ne 'b7127dbfac9e7a9549ea682499a1ca5d368a4acbbc20da2e307324be5813b978' -or
    $app1Module06Release.validation.module_root_checks -ne 153 -or
    $app1Module06Release.validation.complete_reference_checks -ne 189 -or
    $app1Module06Release.validation.starter_checks -ne 100 -or
    $app1Module06Release.assessment.reference_gates_passed -ne 24 -or
    $app1Module06Release.progression.reference -ne 'continue with conditions' -or
    $app1Module06Release.progression.module07_permission -ne 'permitted for curriculum construction' -or
    $app1Module06OutputFailures.Count -gt 0
) {
    throw "APP-1 Module 06 release metadata or frozen outputs do not match the equity, improvement, and bounded-ML contract: $($app1Module06OutputFailures -join ', ')."
}
& python (Join-Path $app1Module06Root 'build_equity_improvement.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-1 Module 06 analysis builder self-check failed.' }
& python (Join-Path $app1Module06Root 'build_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-1 Module 06 workspace builder self-check failed.' }
& python (Join-Path $app1Module06Root 'validate_equity_improvement.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-1 Module 06 validator self-check failed.' }

$app1Checkpoint02Root = Join-Path $repo 'courses\clinical-care\checkpoints\02-adjusted-variation-improvement-release'
$app1Checkpoint02Spec = Join-Path $repo 'docs\curriculum\courses\APP-1\checkpoints\02-adjusted-variation-improvement-release-spec.md'
$app1Checkpoint02Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'checkpoint-contract.json', 'assessment.md',
    'instructor-notes.md', 'build_checkpoint.py', 'validate_checkpoint.py', 'release.json',
    'evidence-index.csv', 'adjusted-variation-improvement-review.md',
    'reproducibility-check.md', 'ai-use.md', 'progression-decision.md',
    'template\README.md', 'template\evidence-index.csv',
    'template\adjusted-variation-improvement-review.md',
    'template\reproducibility-check.md', 'template\ai-use.md',
    'template\progression-decision.md'
)
$app1Checkpoint02Missing = @($app1Checkpoint02Files | Where-Object { -not (Test-Path -LiteralPath (Join-Path $app1Checkpoint02Root $_)) })
if (-not (Test-Path -LiteralPath $app1Checkpoint02Spec) -or $app1Checkpoint02Missing.Count -gt 0) {
    throw "APP-1 Checkpoint 2 is missing its specification or package files: $($app1Checkpoint02Missing -join ', ')."
}
$app1Checkpoint02Content = Get-Content -Raw -LiteralPath $app1Checkpoint02Spec
$app1Checkpoint02Sections = [regex]::Matches($app1Checkpoint02Content, '(?m)^## \d+\.').Count
if (
    $app1Checkpoint02Sections -ne 15 -or
    $app1Checkpoint02Content -match '[—–]' -or
    $app1Checkpoint02Content -match '(?im)[A-Z]:\\Users\\' -or
    $app1Checkpoint02Content -notmatch 'Commons release: `0\.54\.0`' -or
    $app1Checkpoint02Content -notmatch 'f5f892c2b5f6c193f5389c10f7e60df81b1400ca5a163734a103efa745c54ed1' -or
    $app1Checkpoint02Content -notmatch '496 checks' -or
    $app1Checkpoint02Content -notmatch '473 checks'
) {
    throw 'APP-1 Checkpoint 2 must define 15 plain-ASCII sections with exact component, score, manifest, evidence, and validation contracts.'
}
$app1Checkpoint02Release = Get-Content -Raw -LiteralPath (Join-Path $app1Checkpoint02Root 'release.json') | ConvertFrom-Json
if (
    $app1Checkpoint02Release.checkpoint.id -ne 'oclc-app1-cp02' -or
    $app1Checkpoint02Release.checkpoint.version -ne '0.1.0' -or
    $app1Checkpoint02Release.checkpoint.commons_release -ne '0.54.0' -or
    $app1Checkpoint02Release.checkpoint.course_points -ne 45 -or
    $app1Checkpoint02Release.accepted_modules.Count -ne 3 -or
    $app1Checkpoint02Release.score.module04 -ne 25 -or
    $app1Checkpoint02Release.score.module05 -ne 20 -or
    $app1Checkpoint02Release.score.module06 -ne 0 -or
    $app1Checkpoint02Release.score.total -ne 45 -or
    $app1Checkpoint02Release.package.candidate_files -ne 100 -or
    $app1Checkpoint02Release.package.assembled_files -ne 113 -or
    $app1Checkpoint02Release.package.candidate_manifest_bytes -ne 17062 -or
    $app1Checkpoint02Release.package.candidate_manifest_sha256 -ne 'f5f892c2b5f6c193f5389c10f7e60df81b1400ca5a163734a103efa745c54ed1' -or
    $app1Checkpoint02Release.reference_decision.score -ne '45.00 of 45.00' -or
    $app1Checkpoint02Release.reference_decision.progression -ne 'continue with conditions' -or
    $app1Checkpoint02Release.reference_decision.module07_permission -ne 'permitted for curriculum construction' -or
    $app1Checkpoint02Release.reference_decision.clinical_implementation -ne 'prohibited' -or
    $app1Checkpoint02Release.reference_decision.model_deployment -ne 'prohibited' -or
    $app1Checkpoint02Release.validation.reference_checks -ne 496 -or
    $app1Checkpoint02Release.validation.learner_checks -ne 473
) {
    throw 'APP-1 Checkpoint 2 release metadata does not match the cumulative Week 6 contract.'
}
& python (Join-Path $app1Checkpoint02Root 'build_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-1 Checkpoint 2 builder self-check failed.' }
& python (Join-Path $app1Checkpoint02Root 'validate_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-1 Checkpoint 2 validator self-check failed.' }

$app1Module07Root = Join-Path $repo 'courses\clinical-care\modules\07-clinician-leadership-defense'
$app1Module07Spec = Join-Path $repo 'docs\curriculum\courses\APP-1\modules\07-clinician-leadership-defense-spec.md'
$app1Module07Records = @(
    'README.md', 'evidence-synthesis.md', 'improvement-recommendation.md', 'people-equity-safety.md',
    'stakeholder-roles.csv', 'workflow-feasibility.md', 'bounded-test-plan.md', 'measures-monitoring.csv',
    'stop-escalation-rules.csv', 'leadership-reflection.md', 'technical-appendix.md', 'evidence-index.csv',
    'accessibility-review.md', 'reproducibility-check.md', 'ai-use.md', 'component-score.csv',
    'gate-results.csv', 'conditions-register.csv', 'technical-defense.md', 'reviewer-record.md',
    'progression-decision.md'
)
$app1Module07Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'leadership-contract.json', 'clinician-profile.md',
    'clinician-session-plan.md', 'assessment.md', 'instructor-notes.md', 'assemble_candidate.py',
    'validate_candidate.py', 'release.json'
) + @($app1Module07Records | ForEach-Object { "reference\$_" }) + @($app1Module07Records | ForEach-Object { "template\$_" })
$app1Module07Missing = @($app1Module07Files | Where-Object { -not (Test-Path -LiteralPath (Join-Path $app1Module07Root $_)) })
if (-not (Test-Path -LiteralPath $app1Module07Spec) -or $app1Module07Missing.Count -gt 0) {
    throw "APP-1 Module 07 is missing its specification or package files: $($app1Module07Missing -join ', ')."
}
$app1Module07Content = Get-Content -Raw -LiteralPath $app1Module07Spec
$app1Module07Sections = [regex]::Matches($app1Module07Content, '(?m)^## \d+\.').Count
$app1Module07Release = Get-Content -Raw -LiteralPath (Join-Path $app1Module07Root 'release.json') | ConvertFrom-Json
$app1Module07Scores = @(Import-Csv -LiteralPath (Join-Path $app1Module07Root 'reference\component-score.csv'))
$app1Module07Gates = @(Import-Csv -LiteralPath (Join-Path $app1Module07Root 'reference\gate-results.csv'))
$app1Module07Measures = @(Import-Csv -LiteralPath (Join-Path $app1Module07Root 'reference\measures-monitoring.csv'))
$app1Module07Profile = Get-Content -Raw -LiteralPath (Join-Path $app1Module07Root 'clinician-profile.md')
if (
    $app1Module07Sections -ne 21 -or
    $app1Module07Content -match '[—–]' -or
    $app1Module07Content -match '(?im)[A-Z]:\\Users\\' -or
    $app1Module07Content -notmatch 'Commons release target: 0\.55\.0' -or
    $app1Module07Content -notmatch '2c90713fb220b6fdc1af492898e89605051b0dffed44b2fb2883b2942aefde62' -or
    $app1Module07Content -notmatch '1,233 checks' -or
    $app1Module07Content -notmatch '1,185 checks' -or
    $app1Module07Content -notmatch 'Twenty-four noncompensable gates' -or
    $app1Module07Release.module.id -ne 'oclc-app1-07' -or
    $app1Module07Release.module.version -ne '0.1.0' -or
    $app1Module07Release.module.commons_release -ne '0.55.0' -or
    $app1Module07Release.module.hours -ne 16.0 -or
    $app1Module07Release.module.course_points -ne 35 -or
    $app1Module07Release.clinician_of_record.name -ne 'Joe Joseph, MD, SFHM' -or
    $app1Module07Release.package.immutable_manifest_rows -ne 214 -or
    $app1Module07Release.package.candidate_files -ne 236 -or
    $app1Module07Release.package.manifest_bytes -ne 40140 -or
    $app1Module07Release.package.manifest_sha256 -ne '2c90713fb220b6fdc1af492898e89605051b0dffed44b2fb2883b2942aefde62' -or
    $app1Module07Release.reference_decision.candidate_score -ne '35.00 of 35.00' -or
    $app1Module07Release.reference_decision.candidate_status -ne 'accept with conditions' -or
    $app1Module07Release.reference_decision.clinical_recommendation -ne 'revise before testing' -or
    $app1Module07Release.reference_decision.clinical_implementation -ne 'prohibited' -or
    $app1Module07Release.reference_decision.model_deployment -ne 'prohibited' -or
    $app1Module07Release.reference_decision.patient_targeting -ne 'prohibited' -or
    $app1Module07Release.validation.complete_reference_checks -ne 1233 -or
    $app1Module07Release.validation.starter_checks -ne 1185 -or
    $app1Module07Scores.Count -ne 5 -or
    ($app1Module07Scores | Measure-Object -Property maximum -Sum).Sum -ne 35 -or
    ($app1Module07Scores | Measure-Object -Property score -Sum).Sum -ne 35 -or
    $app1Module07Gates.Count -ne 24 -or
    @($app1Module07Gates | Where-Object { $_.result -eq 'fail' }).Count -ne 0 -or
    $app1Module07Measures.Count -ne 11 -or
    $app1Module07Profile -notmatch 'makes no claim about Dr\. Joseph''s current employer or title' -or
    $app1Module07Profile -notmatch 'soundphysicians\.com/press-release/sound-physicians-thought-leaders-presenting-at-hospital-medicine-2017-annual-conference/'
) {
    throw 'APP-1 Module 07 release metadata, specification, clinician identity, score, gates, measures, validation, or manifest facts do not match the 0.1.0 contract.'
}
& python (Join-Path $app1Module07Root 'assemble_candidate.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-1 Module 07 assembler self-check failed.' }
& python (Join-Path $app1Module07Root 'validate_candidate.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-1 Module 07 validator self-check failed.' }

$app1Checkpoint03Root = Join-Path $repo 'courses\clinical-care\checkpoints\03-clinical-care-improvement-package'
$app1Checkpoint03Spec = Join-Path $repo 'docs\curriculum\courses\APP-1\checkpoints\03-clinical-care-improvement-package-spec.md'
$app1Checkpoint03Records = @(
    'submission-record.md', 'final-score.csv', 'gate-results.csv', 'final-defense.md',
    'reviewer-record.md', 'final-reproduction.md', 'conditions-register.csv',
    'final-audit.md', 'final-decision.md', 'release-acceptance.md'
)
$app1Checkpoint03Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'final-contract.json', 'assessment.md',
    'instructor-guide.md', 'assemble_final.py', 'validate_final.py', 'release.json'
) + @($app1Checkpoint03Records | ForEach-Object { "reference\$_" }) + @($app1Checkpoint03Records | ForEach-Object { "template\$_" })
$app1Checkpoint03Missing = @($app1Checkpoint03Files | Where-Object { -not (Test-Path -LiteralPath (Join-Path $app1Checkpoint03Root $_)) })
if (-not (Test-Path -LiteralPath $app1Checkpoint03Spec) -or $app1Checkpoint03Missing.Count -gt 0) {
    throw "APP-1 final checkpoint is missing its specification or package files: $($app1Checkpoint03Missing -join ', ')."
}
$app1Checkpoint03Content = Get-Content -Raw -LiteralPath $app1Checkpoint03Spec
$app1Checkpoint03Sections = [regex]::Matches($app1Checkpoint03Content, '(?m)^## \d+\.').Count
$app1Checkpoint03Release = Get-Content -Raw -LiteralPath (Join-Path $app1Checkpoint03Root 'release.json') | ConvertFrom-Json
$app1Checkpoint03Scores = @(Import-Csv -LiteralPath (Join-Path $app1Checkpoint03Root 'reference\final-score.csv'))
$app1Checkpoint03Gates = @(Import-Csv -LiteralPath (Join-Path $app1Checkpoint03Root 'reference\gate-results.csv'))
if (
    $app1Checkpoint03Sections -ne 17 -or
    $app1Checkpoint03Content -match '[—–]' -or
    $app1Checkpoint03Content -match '(?im)[A-Z]:\\Users\\' -or
    $app1Checkpoint03Content -notmatch 'Commons release target: 0\.55\.0' -or
    $app1Checkpoint03Content -notmatch 'aab1eef0c746700b6322ac1300c5dac3571d861f0fb283c86a0602e3dad9a54b' -or
    $app1Checkpoint03Content -notmatch '1,276 checks' -or
    $app1Checkpoint03Content -notmatch '1,231 checks' -or
    $app1Checkpoint03Release.checkpoint.id -ne 'oclc-app1-cp03' -or
    $app1Checkpoint03Release.checkpoint.version -ne '0.1.0' -or
    $app1Checkpoint03Release.checkpoint.commons_release -ne '0.55.0' -or
    $app1Checkpoint03Release.checkpoint.course_points -ne 35 -or
    $app1Checkpoint03Release.accepted_candidate.candidate_files -ne 236 -or
    $app1Checkpoint03Release.accepted_candidate.immutable_manifest_rows -ne 214 -or
    $app1Checkpoint03Release.accepted_candidate.immutable_manifest_sha256 -ne '2c90713fb220b6fdc1af492898e89605051b0dffed44b2fb2883b2942aefde62' -or
    $app1Checkpoint03Release.package.candidate_manifest_rows -ne 236 -or
    $app1Checkpoint03Release.package.candidate_manifest_bytes -ne 38238 -or
    $app1Checkpoint03Release.package.candidate_manifest_sha256 -ne 'aab1eef0c746700b6322ac1300c5dac3571d861f0fb283c86a0602e3dad9a54b' -or
    $app1Checkpoint03Release.package.assembled_files -ne 251 -or
    $app1Checkpoint03Release.course_score.total -ne 100 -or
    $app1Checkpoint03Release.reference_decision.package_disposition -ne 'accept with conditions' -or
    $app1Checkpoint03Release.reference_decision.clinical_recommendation -ne 'revise before testing' -or
    $app1Checkpoint03Release.reference_decision.tag_status -ne 'proposed - not created' -or
    $app1Checkpoint03Release.validation.complete_reference_checks -ne 1276 -or
    $app1Checkpoint03Release.validation.starter_checks -ne 1231 -or
    $app1Checkpoint03Scores.Count -ne 5 -or
    ($app1Checkpoint03Scores | Measure-Object -Property maximum -Sum).Sum -ne 35 -or
    ($app1Checkpoint03Scores | Measure-Object -Property score -Sum).Sum -ne 35 -or
    $app1Checkpoint03Gates.Count -ne 24 -or
    @($app1Checkpoint03Gates | Where-Object { $_.result -eq 'fail' }).Count -ne 0
) {
    throw 'APP-1 final checkpoint release metadata, specification, score, gates, validation, manifest, or separate decisions do not match the 0.1.0 contract.'
}
& python (Join-Path $app1Checkpoint03Root 'assemble_final.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-1 final checkpoint assembler self-check failed.' }
& python (Join-Path $app1Checkpoint03Root 'validate_final.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-1 final checkpoint validator self-check failed.' }

$app2 = Join-Path $repo 'docs\curriculum\courses\APP-2\course-spec.md'
$app2Source = Join-Path $repo 'docs\source\app-2-patient-experience-engagement-source-record.md'
$app2Package = Join-Path $repo 'courses\patient-experience-engagement\README.md'
if (-not (Test-Path -LiteralPath $app2) -or -not (Test-Path -LiteralPath $app2Source) -or -not (Test-Path -LiteralPath $app2Package)) {
    throw 'APP-2 must include its course specification, source record, and course package README.'
}
$app2Content = Get-Content -Raw -LiteralPath $app2
$app2SourceContent = Get-Content -Raw -LiteralPath $app2Source
$app2PackageContent = Get-Content -Raw -LiteralPath $app2Package
$app2ModuleCount = [regex]::Matches($app2Content, '(?m)^## \d+\. Module \d{2} brief:').Count
$app2HourMatches = [regex]::Matches(
    $app2Content,
    '(?m)^\| \d{2} \| [^|]+ \| \d \| (?<hours>\d+(?:\.\d+)?) \|'
)
$app2Hours = ($app2HourMatches | ForEach-Object { [decimal]$_.Groups['hours'].Value } | Measure-Object -Sum).Sum
$app2CheckpointCount = [regex]::Matches($app2Content, '(?m)^### (?:Checkpoint \d|Final checkpoint):').Count
if (
    $app2ModuleCount -ne 7 -or
    $app2HourMatches.Count -ne 7 -or
    $app2Hours -ne [decimal]112.5 -or
    $app2CheckpointCount -ne 3
) {
    throw "APP-2 must define seven modules, seven schedule rows totaling 112.5 hours, and three checkpoints; found $app2ModuleCount modules, $($app2HourMatches.Count) rows, $app2Hours hours, and $app2CheckpointCount checkpoints."
}
if (
    $app2Content -match '[—–]' -or
    $app2SourceContent -match '[—–]' -or
    $app2PackageContent -match '[—–]' -or
    $app2Content -match '(?im)[A-Z]:\\Users\\' -or
    $app2SourceContent -match '(?im)[A-Z]:\\Users\\' -or
    $app2PackageContent -match '(?im)[A-Z]:\\Users\\' -or
    $app2Content -notmatch 'Current Commons release: 0\.64\.0' -or
    $app2PackageContent -notmatch 'Current Commons release: 0\.64\.0' -or
    $app2PackageContent -notmatch 'all seven modules and all three cumulative checkpoints are runnable release candidates' -or
    $app2Content -notmatch '3feff30f5128587a482a3f4ca42979a46059bbe98e3febc98f4556c4cfafc009' -or
    $app2SourceContent -notmatch '3feff30f5128587a482a3f4ca42979a46059bbe98e3febc98f4556c4cfafc009' -or
    $app2SourceContent -notmatch '25,906' -or
    $app2Content -notmatch 'b70e598f29552df302e30ed649d178abd1b3d3c868ae97cf8e55453dd33898fc' -or
    $app2Content -notmatch '56c6c11f1d61820f367417a00b1e2abaaf02d0b7104d7a5429031e750332503c' -or
    $app2Content -notmatch 'https://meps\.ahrq\.gov/data_stats/download_data_files_detail\.jsp\?cboPufNumber=HC-256' -or
    $app2Content -notmatch 'eight-hour ML extension' -or
    $app2Content -notmatch 'Joe Joseph, MD, SFHM' -or
    $app2Content -notmatch 'patient/caregiver partner co-lead' -or
    $app2Content -notmatch 'https://www\.mghihp\.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current\.pdf' -or
    $app2SourceContent -notmatch '20%' -or
    $app2SourceContent -notmatch '25%' -or
    ([regex]::Matches($app2SourceContent, '20%')).Count -lt 2 -or
    $app2SourceContent -notmatch '35%'
) {
    throw 'APP-2 is missing its source, version, ownership, workload, assessment, public-data, ML, leadership, or plain-ASCII contract.'
}

$app2Module01Root = Join-Path $repo 'courses\patient-experience-engagement\modules\01-patient-experience-decision'
$app2Module01Spec = Join-Path $repo 'docs\curriculum\courses\APP-2\modules\01-patient-experience-decision-spec.md'
$app2Module01Files = @(
    '.gitattributes',
    'README.md',
    'VERSION',
    'assessment.md',
    'build_workspace.py',
    'data-spec.md',
    'decision-contract.json',
    'instructor-notes.md',
    'profile_source.py',
    'source-record.yml',
    'validate_workspace.py',
    'release.json',
    'data\raw\HCAHPS-Hospital.csv.gz',
    'data\source-profile.csv',
    'data\measure-inventory.csv',
    'data\discharge-measure-profile.csv',
    'template\patient-experience-decision-charter.md',
    'template\construct-map.csv',
    'template\patient-journey-map.csv',
    'template\evidence-needs.csv',
    'template\stakeholder-partnership-map.csv',
    'template\claim-boundary.csv',
    'template\source-feasibility-interpretation.md',
    'template\ai-use.md',
    'template\progression-decision.md',
    'reference\patient-experience-decision-charter.md',
    'reference\construct-map.csv',
    'reference\patient-journey-map.csv',
    'reference\evidence-needs.csv',
    'reference\stakeholder-partnership-map.csv',
    'reference\claim-boundary.csv',
    'reference\source-feasibility-interpretation.md',
    'reference\ai-use.md',
    'reference\progression-decision.md'
)
$app2Module01Missing = @()
if (-not (Test-Path -LiteralPath $app2Module01Spec)) { $app2Module01Missing += 'specification' }
foreach ($relative in $app2Module01Files) {
    if (-not (Test-Path -LiteralPath (Join-Path $app2Module01Root $relative))) {
        $app2Module01Missing += $relative
    }
}
if ($app2Module01Missing.Count -gt 0) {
    throw "APP-2 Module 01 is missing its specification or package files: $($app2Module01Missing -join ', ')."
}
$app2Module01Content = Get-Content -Raw -LiteralPath $app2Module01Spec
$app2Module01Sections = [regex]::Matches($app2Module01Content, '(?m)^## \d+\.').Count
$app2Module01Release = Get-Content -Raw -LiteralPath (Join-Path $app2Module01Root 'release.json') | ConvertFrom-Json
$app2Module01Profile = @(Import-Csv -LiteralPath (Join-Path $app2Module01Root 'data\source-profile.csv'))
$app2Module01Measures = @(Import-Csv -LiteralPath (Join-Path $app2Module01Root 'data\measure-inventory.csv'))
$app2Module01Discharge = @(Import-Csv -LiteralPath (Join-Path $app2Module01Root 'data\discharge-measure-profile.csv'))
if (
    $app2Module01Sections -ne 21 -or
    $app2Module01Content -match '[—–]' -or
    $app2Module01Content -match '(?im)[A-Z]:\\Users\\' -or
    $app2Module01Content -notmatch '325,720 rows' -or
    $app2Module01Content -notmatch '4,790 facilities' -or
    $app2Module01Content -notmatch '68 measure IDs' -or
    $app2Module01Content -notmatch '1,787 bytes' -or
    $app2Module01Content -notmatch 'c693e04592994f6f7bef14459b83669a5c824d0bf0b027a0624bab12a3cb4862' -or
    $app2Module01Content -notmatch '173 checks' -or
    $app2Module01Content -notmatch '134 checks' -or
    $app2Module01Release.module.id -ne 'oclc-app2-01' -or
    $app2Module01Release.module.version -ne '0.1.0' -or
    $app2Module01Release.module.commons_release -ne '0.56.0' -or
    $app2Module01Release.source.raw_bytes -ne 105461119 -or
    $app2Module01Release.source.raw_sha256 -ne 'b70e598f29552df302e30ed649d178abd1b3d3c868ae97cf8e55453dd33898fc' -or
    $app2Module01Release.source.gzip_bytes -ne 2195547 -or
    $app2Module01Release.source.gzip_sha256 -ne '56c6c11f1d61820f367417a00b1e2abaaf02d0b7104d7a5429031e750332503c' -or
    $app2Module01Release.source.rows -ne 325720 -or
    $app2Module01Release.source.facilities -ne 4790 -or
    $app2Module01Release.source.measure_ids -ne 68 -or
    $app2Module01Release.source.patient_level_rows -ne 0 -or
    $app2Module01Release.package.immutable_manifest_rows -ne 15 -or
    $app2Module01Release.package.assembled_files -ne 25 -or
    $app2Module01Release.package.manifest_bytes -ne 1787 -or
    $app2Module01Release.package.manifest_sha256 -ne 'c693e04592994f6f7bef14459b83669a5c824d0bf0b027a0624bab12a3cb4862' -or
    $app2Module01Release.validation.complete_reference_checks -ne 173 -or
    $app2Module01Release.validation.starter_checks -ne 134 -or
    $app2Module01Release.progression.reference -ne 'continue with conditions' -or
    $app2Module01Release.progression.clinical_action -ne 'prohibited' -or
    $app2Module01Release.progression.hospital_ranking -ne 'prohibited' -or
    $app2Module01Profile.Count -ne 20 -or
    $app2Module01Measures.Count -ne 68 -or
    $app2Module01Discharge.Count -ne 4 -or
    @($app2Module01Discharge | Where-Object { $_.measure_id -eq 'H_COMP_6_Y_P' -and $_.reported_percent_rows -eq '3949' -and $_.unavailable_percent_rows -eq '841' }).Count -ne 1
) {
    throw 'APP-2 Module 01 release metadata, specification, source, profiles, validation, manifest, or progression facts do not match the 0.1.0 contract.'
}
& python (Join-Path $app2Module01Root 'profile_source.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 01 source profiler self-check failed.' }
& python (Join-Path $app2Module01Root 'build_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 01 builder self-check failed.' }
& python (Join-Path $app2Module01Root 'validate_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 01 validator self-check failed.' }

$app2Module02Root = Join-Path $repo 'courses\patient-experience-engagement\modules\02-patient-reported-measurement'
$app2Module02Spec = Join-Path $repo 'docs\curriculum\courses\APP-2\modules\02-patient-reported-measurement-spec.md'
$app2Module02Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'assessment.md', 'build_measurement.py',
    'build_workspace.py', 'data-spec.md', 'instructor-notes.md', 'measurement-contract.json',
    'rights-record.md', 'source-record.yml', 'validate_workspace.py', 'release.json',
    'data\source-inventory.csv', 'data\mode-language-inventory.csv', 'data\version-crosswalk.csv',
    'data\item-map.csv', 'data\scoring-rules.csv', 'data\synthetic\patient-measurement-responses.csv',
    'outputs\synthetic-score-summary.csv', 'outputs\reliability-diagnostics.csv',
    'outputs\published-concordance.csv', 'outputs\published-concordance-summary.csv',
    'outputs\invariant-checks.csv', 'build-report.json',
    'template\instrument-comparison.csv', 'template\construct-content-validity.md',
    'template\scoring-reproduction.csv', 'template\reliability-interpretation.md',
    'template\meaningful-interpretation.md', 'template\language-mode-access.csv',
    'template\proxy-burden-record.md', 'template\rights-naming-decision.md',
    'template\measurement-decision.md', 'template\measurement-score.csv',
    'template\gate-results.csv', 'template\ai-use.md', 'template\progression-decision.md',
    'reference\instrument-comparison.csv', 'reference\construct-content-validity.md',
    'reference\scoring-reproduction.csv', 'reference\reliability-interpretation.md',
    'reference\meaningful-interpretation.md', 'reference\language-mode-access.csv',
    'reference\proxy-burden-record.md', 'reference\rights-naming-decision.md',
    'reference\measurement-decision.md', 'reference\measurement-score.csv',
    'reference\gate-results.csv', 'reference\ai-use.md', 'reference\progression-decision.md'
)
$app2Module02Missing = @()
if (-not (Test-Path -LiteralPath $app2Module02Spec)) { $app2Module02Missing += 'specification' }
foreach ($relative in $app2Module02Files) {
    if (-not (Test-Path -LiteralPath (Join-Path $app2Module02Root $relative))) {
        $app2Module02Missing += $relative
    }
}
if ($app2Module02Missing.Count -gt 0) {
    throw "APP-2 Module 02 is missing its specification or package files: $($app2Module02Missing -join ', ')."
}
$app2Module02Content = Get-Content -Raw -LiteralPath $app2Module02Spec
$app2Module02Sections = [regex]::Matches($app2Module02Content, '(?m)^## \d+\.').Count
$app2Module02Release = Get-Content -Raw -LiteralPath (Join-Path $app2Module02Root 'release.json') | ConvertFrom-Json
$app2Module02Sources = @(Import-Csv -LiteralPath (Join-Path $app2Module02Root 'data\source-inventory.csv'))
$app2Module02Modes = @(Import-Csv -LiteralPath (Join-Path $app2Module02Root 'data\mode-language-inventory.csv'))
$app2Module02Scores = @(Import-Csv -LiteralPath (Join-Path $app2Module02Root 'outputs\synthetic-score-summary.csv'))
$app2Module02Concordance = @(Import-Csv -LiteralPath (Join-Path $app2Module02Root 'outputs\published-concordance.csv'))
$app2Module02Invariants = @(Import-Csv -LiteralPath (Join-Path $app2Module02Root 'outputs\invariant-checks.csv'))
if (
    $app2Module02Sections -ne 21 -or
    $app2Module02Content -match '[—–]' -or
    $app2Module02Content -match '(?im)[A-Z]:\\Users\\' -or
    $app2Module02Content -notmatch '25,032,907 bytes' -or
    $app2Module02Content -notmatch '6,890 bytes' -or
    $app2Module02Content -notmatch 'c261307b45be842c00c9ded66614a3770f379d41a1d7efecb68032f9c090a870' -or
    $app2Module02Content -notmatch '239 checks' -or
    $app2Module02Content -notmatch '202 immutable-package checks' -or
    $app2Module02Release.module.id -ne 'oclc-app2-02' -or
    $app2Module02Release.module.version -ne '0.1.0' -or
    $app2Module02Release.module.commons_release -ne '0.57.0' -or
    $app2Module02Release.source_suite.files -ne 28 -or
    $app2Module02Release.source_suite.bytes -ne 25032907 -or
    $app2Module02Release.source_suite.pdf_pages -ne 1343 -or
    $app2Module02Release.source_suite.instrument_files -ne 22 -or
    $app2Module02Release.public_dataset.gzip_sha256 -ne '56c6c11f1d61820f367417a00b1e2abaaf02d0b7104d7a5429031e750332503c' -or
    $app2Module02Release.generated_evidence.synthetic_fixture.rows -ne 240 -or
    $app2Module02Release.generated_evidence.published_concordance.rows -ne 3610 -or
    $app2Module02Release.generated_evidence.published_concordance.nonexact_matches -ne 1876 -or
    $app2Module02Release.fixed_measurement_results.question_weighted_composite_percent -ne 81.17588933 -or
    $app2Module02Release.fixed_measurement_results.person_weighted_mean_percent -ne 80.0 -or
    $app2Module02Release.package.immutable_manifest_rows -ne 52 -or
    $app2Module02Release.package.editable_records -ne 13 -or
    $app2Module02Release.package.assembled_files -ne 66 -or
    $app2Module02Release.package.manifest_bytes -ne 6890 -or
    $app2Module02Release.package.manifest_sha256 -ne 'c261307b45be842c00c9ded66614a3770f379d41a1d7efecb68032f9c090a870' -or
    $app2Module02Release.validation.copied_validator -ne 'pass' -or
    $app2Module02Release.validation.complete_reference_checks -ne 239 -or
    $app2Module02Release.validation.starter_checks -ne 202 -or
    $app2Module02Release.progression.reference -ne 'continue with conditions' -or
    $app2Module02Release.progression.clinical_action -ne 'prohibited' -or
    $app2Module02Release.progression.hospital_ranking -ne 'prohibited' -or
    $app2Module02Release.progression.response_weighting -ne 'reserved for Module 03' -or
    $app2Module02Sources.Count -ne 28 -or
    ($app2Module02Sources | Measure-Object -Property bytes -Sum).Sum -ne 25032907 -or
    $app2Module02Modes.Count -ne 22 -or
    @($app2Module02Modes | Where-Object { $_.mode -eq 'mail' }).Count -ne 9 -or
    @($app2Module02Modes | Where-Object { $_.mode -eq 'phone' }).Count -ne 4 -or
    @($app2Module02Modes | Where-Object { $_.mode -eq 'web' }).Count -ne 9 -or
    $app2Module02Scores.Count -ne 5 -or
    @($app2Module02Scores | Where-Object { $_.metric_id -eq 'S04' -and $_.value -eq '81.17588933' }).Count -ne 1 -or
    $app2Module02Concordance.Count -ne 3610 -or
    $app2Module02Invariants.Count -ne 18 -or
    @($app2Module02Invariants | Where-Object { $_.status -ne 'pass' }).Count -ne 0
) {
    throw 'APP-2 Module 02 release metadata, specification, sources, scoring, validation, manifest, or progression facts do not match the 0.1.0 contract.'
}
& python (Join-Path $app2Module02Root 'build_measurement.py') --verify-committed
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 02 committed measurement reproduction failed.' }
& python (Join-Path $app2Module02Root 'build_measurement.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 02 measurement builder self-check failed.' }
& python (Join-Path $app2Module02Root 'build_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 02 workspace builder self-check failed.' }
& python (Join-Path $app2Module02Root 'validate_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 02 validator self-check failed.' }

$app2Module03Root = Join-Path $repo 'courses\patient-experience-engagement\modules\03-response-representation-bias'
$app2Module03Spec = Join-Path $repo 'docs\curriculum\courses\APP-2\modules\03-response-representation-bias-spec.md'
$app2Module03Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'assessment.md', 'build_response_evidence.py',
    'build_workspace.py', 'data-spec.md', 'instructor-notes.md', 'response-contract.json',
    'source-record.yml', 'validate_workspace.py', 'release.json', 'build-report.json',
    'data\source-inventory.csv', 'data\field-map.csv', 'data\category-map.csv',
    'data\raw\h256dat.zip', 'data\raw\h256doc.pdf', 'data\raw\h256cb.pdf',
    'data\raw\h256su.txt', 'data\raw\h256ru.txt',
    'data\public\adult-inpatient-frame.csv', 'data\synthetic\response-study.csv',
    'outputs\source-profile.csv', 'outputs\public-saq-response.csv', 'outputs\response-flow.csv',
    'outputs\subgroup-response.csv', 'outputs\item-missingness.csv', 'outputs\weight-cells.csv',
    'outputs\weight-diagnostics.csv', 'outputs\estimate-comparison.csv', 'outputs\invariant-checks.csv',
    'template\target-frame.md', 'template\response-flow.csv', 'template\subgroup-representation.csv',
    'template\item-missingness.csv', 'template\mode-coverage-interpretation.md',
    'template\weighting-decision.md', 'template\bias-recovery.csv', 'template\privacy-consent.md',
    'template\reproducibility-check.md', 'template\gate-results.csv', 'template\ai-use.md',
    'template\progression-decision.md',
    'reference\target-frame.md', 'reference\response-flow.csv', 'reference\subgroup-representation.csv',
    'reference\item-missingness.csv', 'reference\mode-coverage-interpretation.md',
    'reference\weighting-decision.md', 'reference\bias-recovery.csv', 'reference\privacy-consent.md',
    'reference\reproducibility-check.md', 'reference\gate-results.csv', 'reference\ai-use.md',
    'reference\progression-decision.md'
)
$app2Module03Missing = @()
if (-not (Test-Path -LiteralPath $app2Module03Spec)) { $app2Module03Missing += 'specification' }
foreach ($relative in $app2Module03Files) {
    if (-not (Test-Path -LiteralPath (Join-Path $app2Module03Root $relative))) {
        $app2Module03Missing += $relative
    }
}
if ($app2Module03Missing.Count -gt 0) {
    throw "APP-2 Module 03 is missing its specification or package files: $($app2Module03Missing -join ', ')."
}
$app2Module03Content = Get-Content -Raw -LiteralPath $app2Module03Spec
$app2Module03Sections = [regex]::Matches($app2Module03Content, '(?m)^## \d+\.').Count
$app2Module03Release = Get-Content -Raw -LiteralPath (Join-Path $app2Module03Root 'release.json') | ConvertFrom-Json
$app2Module03Sources = @(Import-Csv -LiteralPath (Join-Path $app2Module03Root 'data\source-inventory.csv'))
$app2Module03Frame = @(Import-Csv -LiteralPath (Join-Path $app2Module03Root 'data\public\adult-inpatient-frame.csv'))
$app2Module03Response = @(Import-Csv -LiteralPath (Join-Path $app2Module03Root 'data\synthetic\response-study.csv'))
$app2Module03Subgroups = @(Import-Csv -LiteralPath (Join-Path $app2Module03Root 'outputs\subgroup-response.csv'))
$app2Module03Missingness = @(Import-Csv -LiteralPath (Join-Path $app2Module03Root 'outputs\item-missingness.csv'))
$app2Module03Cells = @(Import-Csv -LiteralPath (Join-Path $app2Module03Root 'outputs\weight-cells.csv'))
$app2Module03Estimates = @(Import-Csv -LiteralPath (Join-Path $app2Module03Root 'outputs\estimate-comparison.csv'))
$app2Module03Invariants = @(Import-Csv -LiteralPath (Join-Path $app2Module03Root 'outputs\invariant-checks.csv'))
if (
    $app2Module03Sections -ne 21 -or
    $app2Module03Content -match '[—–]' -or
    $app2Module03Content -match '(?im)[A-Z]:\\Users\\' -or
    $app2Module03Content -notmatch '12,353,779 bytes' -or
    $app2Module03Content -notmatch '4,045 bytes' -or
    $app2Module03Content -notmatch '3d7787a975335518cf4a4f50b5561a323707e2acea6bd1724b1c92a565f64a30' -or
    $app2Module03Content -notmatch '190 checks' -or
    $app2Module03Content -notmatch '175 checks' -or
    $app2Module03Release.module.id -ne 'oclc-app2-03' -or
    $app2Module03Release.module.version -ne '0.1.0' -or
    $app2Module03Release.module.commons_release -ne '0.58.0' -or
    $app2Module03Release.source_suite.files -ne 5 -or
    $app2Module03Release.source_suite.bytes -ne 12353779 -or
    $app2Module03Release.source_suite.pdf_pages -ne 869 -or
    $app2Module03Release.source_suite.source_rows -ne 19140 -or
    $app2Module03Release.source_suite.positive_person_weight_rows -ne 18683 -or
    $app2Module03Release.public_target.rows -ne 1255 -or
    $app2Module03Release.public_target.base_weighted_population -ne 18879474.284615 -or
    $app2Module03Release.synthetic_response.respondents -ne 782 -or
    $app2Module03Release.synthetic_response.q22_answered -ne 585 -or
    $app2Module03Release.synthetic_response.q23_answered -ne 589 -or
    $app2Module03Release.weighting.teaching_response_cells -ne 13 -or
    $app2Module03Release.weighting.cap_hits -ne 1 -or
    $app2Module03Release.known_truth_comparison.composite_adjusted_absolute_bias_pp -ne 4.20274444 -or
    $app2Module03Release.generated_evidence.files -ne 12 -or
    $app2Module03Release.generated_evidence.bytes -ne 583571 -or
    $app2Module03Release.package.immutable_manifest_rows -ne 31 -or
    $app2Module03Release.package.editable_records -ne 12 -or
    $app2Module03Release.package.assembled_files -ne 44 -or
    $app2Module03Release.package.manifest_bytes -ne 4045 -or
    $app2Module03Release.package.manifest_sha256 -ne '3d7787a975335518cf4a4f50b5561a323707e2acea6bd1724b1c92a565f64a30' -or
    $app2Module03Release.validation.complete_reference_checks -ne 190 -or
    $app2Module03Release.validation.starter_checks -ne 175 -or
    $app2Module03Release.progression.reference -ne 'continue with conditions' -or
    $app2Module03Release.progression.module04_permission -ne 'permitted for linked analysis' -or
    $app2Module03Release.progression.real_fielding -ne 'prohibited' -or
    $app2Module03Sources.Count -ne 5 -or
    ($app2Module03Sources | Measure-Object -Property bytes -Sum).Sum -ne 12353779 -or
    $app2Module03Frame.Count -ne 1255 -or
    $app2Module03Response.Count -ne 1255 -or
    @($app2Module03Response | Where-Object { $_.response_status -eq 'respondent' }).Count -ne 782 -or
    $app2Module03Subgroups.Count -ne 40 -or
    $app2Module03Missingness.Count -ne 20 -or
    $app2Module03Cells.Count -ne 13 -or
    @($app2Module03Cells | Where-Object { $_.bound_hit -eq 'yes' }).Count -ne 1 -or
    $app2Module03Estimates.Count -ne 12 -or
    @($app2Module03Estimates | Where-Object { $_.measure -eq 'teaching_composite' -and $_.estimator -eq 'respondent_response_adjusted' -and $_.absolute_bias_pp -eq '4.20274444' }).Count -ne 1 -or
    $app2Module03Invariants.Count -ne 23 -or
    @($app2Module03Invariants | Where-Object { $_.status -ne 'pass' }).Count -ne 0
) {
    throw 'APP-2 Module 03 release metadata, specification, sources, response, weighting, validation, manifest, or progression facts do not match the 0.1.0 contract.'
}
& python (Join-Path $app2Module03Root 'build_response_evidence.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 03 evidence builder self-check failed.' }
& python (Join-Path $app2Module03Root 'build_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 03 workspace builder self-check failed.' }
& python (Join-Path $app2Module03Root 'validate_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 03 validator self-check failed.' }

$app2Module04Root = Join-Path $repo 'courses\patient-experience-engagement\modules\04-linked-patient-evidence'
$app2Module04Spec = Join-Path $repo 'docs\curriculum\courses\APP-2\modules\04-linked-patient-evidence-spec.md'
$app2Module04Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'assessment.md', 'build_linked_evidence.py',
    'build_workspace.py', 'build-report.json', 'data-spec.md', 'instructor-notes.md',
    'linkage-contract.json', 'release.json', 'source-record.yml', 'validate_workspace.py',
    'data\source-inventory.csv', 'data\upstream-inventory.csv',
    'data\upstream\checkpoint01-release.json', 'data\upstream\module03-adult-inpatient-frame.csv',
    'data\upstream\module03-response-study.csv', 'data\public\linked-persons.csv',
    'data\public\linked-events.csv', 'outputs\access-communication-estimates.csv',
    'outputs\denominator-registry.csv', 'outputs\digital-engagement.csv',
    'outputs\invariant-checks.csv', 'outputs\linkage-reconciliation.csv',
    'outputs\linked-evidence-patterns.csv', 'outputs\service-use-estimates.csv',
    'outputs\source-profile.csv'
)
foreach ($sourceStem in @('h256', 'h254d', 'h254e', 'h254f', 'h254g')) {
    foreach ($sourceSuffix in @('dat.zip', 'doc.pdf', 'cb.pdf', 'su.txt', 'ru.txt')) {
        $app2Module04Files += "data\raw\$sourceStem$sourceSuffix"
    }
}
foreach ($editable in @(
    'access-communication-interpretation.md', 'ai-use.md', 'denominator-decisions.csv',
    'digital-engagement-interpretation.md', 'gate-results.csv', 'linkage-audit.csv',
    'linkage-plan.md', 'linked-evidence-analysis.md', 'progression-decision.md',
    'reproducibility-check.md', 'responsible-claims.md', 'service-use-interpretation.md'
)) {
    $app2Module04Files += "template\$editable", "reference\$editable"
}
$app2Module04Missing = @()
if (-not (Test-Path -LiteralPath $app2Module04Spec)) { $app2Module04Missing += 'specification' }
foreach ($relative in $app2Module04Files) {
    if (-not (Test-Path -LiteralPath (Join-Path $app2Module04Root $relative))) {
        $app2Module04Missing += $relative
    }
}
if ($app2Module04Missing.Count -gt 0) {
    throw "APP-2 Module 04 is missing its specification or package files: $($app2Module04Missing -join ', ')."
}
$app2Module04Content = Get-Content -Raw -LiteralPath $app2Module04Spec
$app2Module04Sections = [regex]::Matches($app2Module04Content, '(?m)^## \d+\.').Count
$app2Module04Release = Get-Content -Raw -LiteralPath (Join-Path $app2Module04Root 'release.json') | ConvertFrom-Json
$app2Module04Sources = @(Import-Csv -LiteralPath (Join-Path $app2Module04Root 'data\source-inventory.csv'))
$app2Module04People = @(Import-Csv -LiteralPath (Join-Path $app2Module04Root 'data\public\linked-persons.csv'))
$app2Module04Events = @(Import-Csv -LiteralPath (Join-Path $app2Module04Root 'data\public\linked-events.csv'))
$app2Module04Reconciliation = @(Import-Csv -LiteralPath (Join-Path $app2Module04Root 'outputs\linkage-reconciliation.csv'))
$app2Module04Denominators = @(Import-Csv -LiteralPath (Join-Path $app2Module04Root 'outputs\denominator-registry.csv'))
$app2Module04Access = @(Import-Csv -LiteralPath (Join-Path $app2Module04Root 'outputs\access-communication-estimates.csv'))
$app2Module04Services = @(Import-Csv -LiteralPath (Join-Path $app2Module04Root 'outputs\service-use-estimates.csv'))
$app2Module04Digital = @(Import-Csv -LiteralPath (Join-Path $app2Module04Root 'outputs\digital-engagement.csv'))
$app2Module04Patterns = @(Import-Csv -LiteralPath (Join-Path $app2Module04Root 'outputs\linked-evidence-patterns.csv'))
$app2Module04Invariants = @(Import-Csv -LiteralPath (Join-Path $app2Module04Root 'outputs\invariant-checks.csv'))
$app2Module04Gates = @(Import-Csv -LiteralPath (Join-Path $app2Module04Root 'reference\gate-results.csv'))
if (
    $app2Module04Sections -ne 21 -or
    $app2Module04Content -match '[—–]' -or
    $app2Module04Content -match '(?im)[A-Z]:\\Users\\' -or
    $app2Module04Content -notmatch '18,206,634 bytes' -or
    $app2Module04Content -notmatch '6,529 bytes' -or
    $app2Module04Content -notmatch 'bc0592acd18b8524be907fd42483e85af4180e0b6f6de35d40e82ea3eae46aa8' -or
    $app2Module04Content -notmatch '249 checks' -or
    $app2Module04Content -notmatch '234 checks' -or
    $app2Module04Release.module.id -ne 'oclc-app2-04' -or
    $app2Module04Release.module.version -ne '0.1.0' -or
    $app2Module04Release.module.commons_release -ne '0.59.0' -or
    $app2Module04Release.module.course_points -ne 25 -or
    $app2Module04Release.source_suite.files -ne 25 -or
    $app2Module04Release.source_suite.bytes -ne 18206634 -or
    $app2Module04Release.source_suite.pdf_pages -ne 1101 -or
    $app2Module04Release.source_suite.person_rows -ne 19140 -or
    $app2Module04Release.source_suite.event_rows -ne 174231 -or
    $app2Module04Release.source_suite.event_weight_mismatches -ne 0 -or
    $app2Module04Release.upstream.checkpoint_candidate_manifest_sha256 -ne '5734df858d79721f3efd6766df6299f56d0df49c0aee8b8728b22c284255c903' -or
    $app2Module04Release.target.people -ne 1255 -or
    $app2Module04Release.target.linked_events -ne 28455 -or
    $app2Module04Release.target.synthetic_complete_linked_analysis_rows -ne 538 -or
    $app2Module04Release.linkage.event_rows.inpatient -ne 1692 -or
    $app2Module04Release.linkage.event_rows.emergency -ne 1601 -or
    $app2Module04Release.linkage.event_rows.outpatient -ne 4651 -or
    $app2Module04Release.linkage.event_rows.office_based -ne 20511 -or
    $app2Module04Release.linkage.inpatient_2023_carry_in_starts -ne 12 -or
    $app2Module04Release.measurement.provider_language_valid_rows -ne 45 -or
    $app2Module04Release.measurement.portal_preference_denominator -ne 0 -or
    $app2Module04Release.generated_evidence.invariants_passed -ne 25 -or
    $app2Module04Release.package.immutable_manifest_rows -ne 52 -or
    $app2Module04Release.package.editable_records -ne 12 -or
    $app2Module04Release.package.assembled_files -ne 65 -or
    $app2Module04Release.package.manifest_bytes -ne 6529 -or
    $app2Module04Release.package.manifest_sha256 -ne 'bc0592acd18b8524be907fd42483e85af4180e0b6f6de35d40e82ea3eae46aa8' -or
    $app2Module04Release.validation.complete_reference_checks -ne 249 -or
    $app2Module04Release.validation.starter_checks -ne 234 -or
    $app2Module04Release.progression.reference -ne 'continue with conditions' -or
    $app2Module04Release.progression.module05_permission -ne 'permitted for patient-voice and equity analysis' -or
    $app2Module04Release.progression.machine_learning -ne 'reserved for Module 06' -or
    $app2Module04Sources.Count -ne 25 -or
    ($app2Module04Sources | Measure-Object -Property bytes -Sum).Sum -ne 18206634 -or
    ($app2Module04Sources | Measure-Object -Property pages -Sum).Sum -ne 1101 -or
    $app2Module04People.Count -ne 1255 -or
    $app2Module04Events.Count -ne 28455 -or
    $app2Module04Reconciliation.Count -ne 5 -or
    @($app2Module04Reconciliation | Where-Object { $_.status -ne 'pass' -or $_.difference -ne '0' }).Count -ne 0 -or
    $app2Module04Denominators.Count -ne 14 -or
    @($app2Module04Denominators | Where-Object { $_.denominator_id -eq 'D022' -and $_.unweighted_n -eq '0' }).Count -ne 1 -or
    $app2Module04Access.Count -ne 10 -or
    @($app2Module04Access | Where-Object { $_.measure -eq 'provider_language_match' -and $_.eligible_persons -eq '45' -and $_.support_flag -eq 'limited_support' }).Count -ne 1 -or
    $app2Module04Services.Count -ne 8 -or
    $app2Module04Digital.Count -ne 7 -or
    @($app2Module04Digital | Where-Object { $_.evidence_id -eq 'DE03' -and $_.denominator_n -eq '25162' -and $_.numerator_n -eq '1813' -and $_.weighted_percent -eq '7.37866394' }).Count -ne 1 -or
    $app2Module04Patterns.Count -ne 14 -or
    $app2Module04Invariants.Count -ne 25 -or
    @($app2Module04Invariants | Where-Object { $_.status -ne 'pass' }).Count -ne 0 -or
    $app2Module04Gates.Count -ne 20 -or
    @($app2Module04Gates | Where-Object { $_.status -ne 'pass' }).Count -ne 0
) {
    throw 'APP-2 Module 04 release metadata, specification, sources, linkage, denominators, measures, validation, manifest, or progression facts do not match the 0.1.0 contract.'
}
& python (Join-Path $app2Module04Root 'build_linked_evidence.py') --verify-committed
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 04 committed evidence reproduction failed.' }
& python (Join-Path $app2Module04Root 'build_linked_evidence.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 04 evidence builder self-check failed.' }
& python (Join-Path $app2Module04Root 'build_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 04 workspace builder self-check failed.' }
& python (Join-Path $app2Module04Root 'validate_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 04 validator self-check failed.' }

$app2Module05Root = Join-Path $repo 'courses\patient-experience-engagement\modules\05-patient-voice-equity'
$app2Module05Spec = Join-Path $repo 'docs\curriculum\courses\APP-2\modules\05-patient-voice-equity-spec.md'
$app2Module05Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'assessment.md', 'build-report.json',
    'build_patient_voice.py', 'build_workspace.py', 'data-spec.md', 'instructor-notes.md',
    'release.json', 'source-record.yml', 'validate_workspace.py', 'voice-equity-contract.json',
    'data\upstream-inventory.csv', 'data\upstream\module04-release.json',
    'data\upstream\module04-linked-persons.csv', 'data\upstream\module04-linked-events.csv',
    'data\upstream\module04-source-inventory.csv', 'data\upstream\module04-denominator-registry.csv',
    'data\synthetic\comment-opportunities.csv', 'data\synthetic\synthetic-comments.csv',
    'data\synthetic\double-coding-sample.csv', 'instructor\comment-truth.csv',
    'instructor\double-coded-comments.csv', 'instructor\assisted-comment-labels.csv',
    'outputs\source-profile.csv', 'outputs\comment-codebook.csv', 'outputs\comment-flow.csv',
    'outputs\agreement-summary.csv', 'outputs\assisted-classification-audit.csv',
    'outputs\theme-summary.csv', 'outputs\comment-examples.csv', 'outputs\group-support.csv',
    'outputs\group-estimates.csv', 'outputs\group-contrasts.csv',
    'outputs\channel-exclusion-audit.csv', 'outputs\invariant-checks.csv'
)
foreach ($editable in @(
    'comment-provenance.md', 'codebook-decisions.csv', 'double-coding-review.csv',
    'agreement-interpretation.md', 'assisted-classification-review.md', 'group-analysis-plan.md',
    'group-support-decisions.csv', 'group-difference-interpretation.md',
    'channel-exclusion-review.md', 'equity-patient-voice-memo.md', 'responsible-claims.md',
    'reproducibility-check.md', 'gate-results.csv', 'ai-use.md', 'progression-decision.md'
)) {
    $app2Module05Files += "template\$editable", "reference\$editable"
}
$app2Module05Missing = @()
if (-not (Test-Path -LiteralPath $app2Module05Spec)) { $app2Module05Missing += 'specification' }
foreach ($relative in $app2Module05Files) {
    if (-not (Test-Path -LiteralPath (Join-Path $app2Module05Root $relative))) {
        $app2Module05Missing += $relative
    }
}
if ($app2Module05Missing.Count -gt 0) {
    throw "APP-2 Module 05 is missing its specification or package files: $($app2Module05Missing -join ', ')."
}
$app2Module05Content = Get-Content -Raw -LiteralPath $app2Module05Spec
$app2Module05Sections = [regex]::Matches($app2Module05Content, '(?m)^## \d+\.').Count
$app2Module05Release = Get-Content -Raw -LiteralPath (Join-Path $app2Module05Root 'release.json') | ConvertFrom-Json
$app2Module05Upstream = @(Import-Csv -LiteralPath (Join-Path $app2Module05Root 'data\upstream-inventory.csv'))
$app2Module05Opportunities = @(Import-Csv -LiteralPath (Join-Path $app2Module05Root 'data\synthetic\comment-opportunities.csv'))
$app2Module05Comments = @(Import-Csv -LiteralPath (Join-Path $app2Module05Root 'data\synthetic\synthetic-comments.csv'))
$app2Module05CodingSample = @(Import-Csv -LiteralPath (Join-Path $app2Module05Root 'data\synthetic\double-coding-sample.csv'))
$app2Module05Truth = @(Import-Csv -LiteralPath (Join-Path $app2Module05Root 'instructor\comment-truth.csv'))
$app2Module05Agreement = @(Import-Csv -LiteralPath (Join-Path $app2Module05Root 'outputs\agreement-summary.csv'))
$app2Module05Assisted = @(Import-Csv -LiteralPath (Join-Path $app2Module05Root 'outputs\assisted-classification-audit.csv'))
$app2Module05Estimates = @(Import-Csv -LiteralPath (Join-Path $app2Module05Root 'outputs\group-estimates.csv'))
$app2Module05Contrasts = @(Import-Csv -LiteralPath (Join-Path $app2Module05Root 'outputs\group-contrasts.csv'))
$app2Module05Exclusion = @(Import-Csv -LiteralPath (Join-Path $app2Module05Root 'outputs\channel-exclusion-audit.csv'))
$app2Module05Invariants = @(Import-Csv -LiteralPath (Join-Path $app2Module05Root 'outputs\invariant-checks.csv'))
$app2Module05Gates = @(Import-Csv -LiteralPath (Join-Path $app2Module05Root 'reference\gate-results.csv'))
if (
    $app2Module05Sections -ne 21 -or
    $app2Module05Content -match '[—–]' -or
    $app2Module05Content -match '(?im)[A-Z]:\\Users\\' -or
    $app2Module05Content -notmatch '5,297,691' -or
    $app2Module05Content -notmatch '4,598-byte' -or
    $app2Module05Content -notmatch '6f3d93a1a08458cb39fa8d321a67f10dad1ee45b2a8a2742a969ab969f35c8fa' -or
    $app2Module05Content -notmatch '217 checks' -or
    $app2Module05Content -notmatch '199 checks' -or
    $app2Module05Release.module.id -ne 'oclc-app2-05' -or
    $app2Module05Release.module.version -ne '0.1.0' -or
    $app2Module05Release.module.commons_release -ne '0.60.0' -or
    $app2Module05Release.module.course_points -ne 20 -or
    $app2Module05Release.upstream.files -ne 5 -or
    $app2Module05Release.upstream.bytes -ne 5297691 -or
    $app2Module05Release.upstream.module_manifest_sha256 -ne 'bc0592acd18b8524be907fd42483e85af4180e0b6f6de35d40e82ea3eae46aa8' -or
    $app2Module05Release.synthetic_comments.opportunities -ne 782 -or
    $app2Module05Release.synthetic_comments.received -ne 420 -or
    $app2Module05Release.synthetic_comments.themes -ne 8 -or
    $app2Module05Release.synthetic_comments.ambiguous -ne 84 -or
    $app2Module05Release.synthetic_comments.double_coded -ne 120 -or
    $app2Module05Release.synthetic_comments.coder_agreements -ne 96 -or
    $app2Module05Release.synthetic_comments.cohens_kappa -ne 0.77142857 -or
    $app2Module05Release.synthetic_comments.real_patient_text_rows -ne 0 -or
    $app2Module05Release.assisted_classification.accuracy -ne 0.78333333 -or
    $app2Module05Release.assisted_classification.suggested_labels_requiring_human_review -ne 420 -or
    $app2Module05Release.group_review.estimate_rows -ne 52 -or
    $app2Module05Release.group_review.supported_estimates -ne 35 -or
    $app2Module05Release.group_review.contrast_rows -ne 36 -or
    $app2Module05Release.group_review.supported_contrasts -ne 19 -or
    $app2Module05Release.generated_evidence.files -ne 19 -or
    $app2Module05Release.generated_evidence.bytes -ne 364354 -or
    $app2Module05Release.generated_evidence.invariants_passed -ne 28 -or
    $app2Module05Release.package.immutable_manifest_rows -ne 33 -or
    $app2Module05Release.package.editable_records -ne 15 -or
    $app2Module05Release.package.assembled_files -ne 49 -or
    $app2Module05Release.package.manifest_bytes -ne 4598 -or
    $app2Module05Release.package.manifest_sha256 -ne '6f3d93a1a08458cb39fa8d321a67f10dad1ee45b2a8a2742a969ab969f35c8fa' -or
    $app2Module05Release.validation.complete_reference_checks -ne 217 -or
    $app2Module05Release.validation.starter_checks -ne 199 -or
    $app2Module05Release.progression.reference -ne 'continue with conditions' -or
    $app2Module05Release.progression.module06_permission -ne 'permitted for partnered improvement and embedded ML' -or
    $app2Module05Release.progression.comment_text_machine_learning -ne 'prohibited' -or
    $app2Module05Upstream.Count -ne 5 -or
    ($app2Module05Upstream | Measure-Object -Property bytes -Sum).Sum -ne 5297691 -or
    $app2Module05Opportunities.Count -ne 782 -or
    @($app2Module05Opportunities | Where-Object { $_.comment_returned -eq 'yes' }).Count -ne 420 -or
    $app2Module05Comments.Count -ne 420 -or
    @($app2Module05Comments | Where-Object { $_.data_class -ne 'fully_synthetic_comment_linked_to_public_derived_meps' }).Count -ne 0 -or
    $app2Module05CodingSample.Count -ne 120 -or
    $app2Module05Truth.Count -ne 420 -or
    @($app2Module05Truth | Where-Object { $_.ambiguous -eq 'yes' }).Count -ne 84 -or
    $app2Module05Agreement.Count -ne 9 -or
    @($app2Module05Agreement | Where-Object { $_.scope -eq 'overall_eight_theme' -and $_.agreements -eq '96' -and $_.cohens_kappa -eq '0.77142857' }).Count -ne 1 -or
    $app2Module05Assisted.Count -ne 9 -or
    @($app2Module05Assisted | Where-Object { $_.scope -eq 'overall' -and $_.accuracy -eq '0.78333333' }).Count -ne 1 -or
    $app2Module05Estimates.Count -ne 52 -or
    @($app2Module05Estimates | Where-Object { $_.support_status -eq 'supported' }).Count -ne 35 -or
    $app2Module05Contrasts.Count -ne 36 -or
    @($app2Module05Contrasts | Where-Object { $_.support_status -eq 'supported' }).Count -ne 19 -or
    $app2Module05Exclusion.Count -ne 13 -or
    $app2Module05Invariants.Count -ne 28 -or
    @($app2Module05Invariants | Where-Object { $_.status -ne 'pass' }).Count -ne 0 -or
    $app2Module05Gates.Count -ne 22 -or
    @($app2Module05Gates | Where-Object { $_.status -ne 'pass' }).Count -ne 0
) {
    throw 'APP-2 Module 05 release metadata, specification, handoff, synthetic comments, coding, group evidence, validation, manifest, or progression facts do not match the 0.1.0 contract.'
}
& python (Join-Path $app2Module05Root 'build_patient_voice.py') --verify-committed
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 05 committed evidence reproduction failed.' }
& python (Join-Path $app2Module05Root 'build_patient_voice.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 05 evidence builder self-check failed.' }
& python (Join-Path $app2Module05Root 'build_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 05 workspace builder self-check failed.' }
& python (Join-Path $app2Module05Root 'validate_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 05 validator self-check failed.' }

$app2Module06Root = Join-Path $repo 'courses\patient-experience-engagement\modules\06-partnered-improvement-embedded-ml'
$app2Module06Spec = Join-Path $repo 'docs\curriculum\courses\APP-2\modules\06-partnered-improvement-embedded-ml-spec.md'
$app2Module06Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'assessment.md',
    'build_partnered_improvement_ml.py', 'build_workspace.py', 'environment.yml',
    'feature-contract.csv', 'module06-contract.json', 'partner-contract.csv',
    'release.json', 'source-record.yml', 'validate_workspace.py',
    'outputs\upstream-inventory.csv', 'outputs\analysis-checks.csv',
    'outputs\improvement-evidence.csv', 'outputs\partner-question-register.csv',
    'outputs\transparent-weight-cells.csv', 'outputs\split-registry.csv',
    'outputs\model-predictions.csv', 'outputs\model-performance.csv',
    'outputs\calibration-bins.csv', 'outputs\threshold-errors.csv',
    'outputs\response-weight-diagnostics.csv', 'outputs\estimate-recovery.csv',
    'outputs\subgroup-model-audit.csv', 'outputs\feature-importance.csv',
    'outputs\failure-cases.csv', 'outputs\invariant-checks.csv', 'outputs\build-report.json'
)
foreach ($editable in @(
    'README.md', 'engagement-status.md', 'patient-partner-session.md',
    'interpretation-disagreement.csv', 'improvement-brief.md', 'driver-diagram.csv',
    'workflow.csv', 'measure-registry.csv', 'burden-access-review.md',
    'feedback-accountability.md', 'ml-comparison.md', 'failure-case-review.md',
    'responsible-claims.md', 'reproducibility-check.md', 'ai-use.md',
    'gate-results.csv', 'progression-decision.md'
)) {
    $app2Module06Files += "template\$editable", "reference\$editable"
}
$app2Module06Missing = @()
if (-not (Test-Path -LiteralPath $app2Module06Spec)) { $app2Module06Missing += 'specification' }
foreach ($relative in $app2Module06Files) {
    if (-not (Test-Path -LiteralPath (Join-Path $app2Module06Root $relative))) {
        $app2Module06Missing += $relative
    }
}
if ($app2Module06Missing.Count -gt 0) {
    throw "APP-2 Module 06 is missing its specification or package files: $($app2Module06Missing -join ', ')."
}
$app2Module06Content = Get-Content -Raw -LiteralPath $app2Module06Spec
$app2Module06Sections = [regex]::Matches($app2Module06Content, '(?m)^## \d+\.').Count
$app2Module06Release = Get-Content -Raw -LiteralPath (Join-Path $app2Module06Root 'release.json') | ConvertFrom-Json
$app2Module06Upstream = @(Import-Csv -LiteralPath (Join-Path $app2Module06Root 'outputs\upstream-inventory.csv'))
$app2Module06Checks = @(Import-Csv -LiteralPath (Join-Path $app2Module06Root 'outputs\analysis-checks.csv'))
$app2Module06Cells = @(Import-Csv -LiteralPath (Join-Path $app2Module06Root 'outputs\transparent-weight-cells.csv'))
$app2Module06Split = @(Import-Csv -LiteralPath (Join-Path $app2Module06Root 'outputs\split-registry.csv'))
$app2Module06Predictions = @(Import-Csv -LiteralPath (Join-Path $app2Module06Root 'outputs\model-predictions.csv'))
$app2Module06Performance = @(Import-Csv -LiteralPath (Join-Path $app2Module06Root 'outputs\model-performance.csv'))
$app2Module06Calibration = @(Import-Csv -LiteralPath (Join-Path $app2Module06Root 'outputs\calibration-bins.csv'))
$app2Module06Diagnostics = @(Import-Csv -LiteralPath (Join-Path $app2Module06Root 'outputs\response-weight-diagnostics.csv'))
$app2Module06Recovery = @(Import-Csv -LiteralPath (Join-Path $app2Module06Root 'outputs\estimate-recovery.csv'))
$app2Module06Subgroups = @(Import-Csv -LiteralPath (Join-Path $app2Module06Root 'outputs\subgroup-model-audit.csv'))
$app2Module06Failures = @(Import-Csv -LiteralPath (Join-Path $app2Module06Root 'outputs\failure-cases.csv'))
$app2Module06Invariants = @(Import-Csv -LiteralPath (Join-Path $app2Module06Root 'outputs\invariant-checks.csv'))
$app2Module06Gates = @(Import-Csv -LiteralPath (Join-Path $app2Module06Root 'reference\gate-results.csv'))
$app2Module06Disagreements = @(Import-Csv -LiteralPath (Join-Path $app2Module06Root 'reference\interpretation-disagreement.csv'))
$app2Module06Measures = @(Import-Csv -LiteralPath (Join-Path $app2Module06Root 'reference\measure-registry.csv'))
$app2Module06Progression = Get-Content -Raw -LiteralPath (Join-Path $app2Module06Root 'reference\progression-decision.md')
$app2Module06Engagement = Get-Content -Raw -LiteralPath (Join-Path $app2Module06Root 'reference\engagement-status.md')
if (
    $app2Module06Files.Count -ne 64 -or
    $app2Module06Sections -ne 22 -or
    $app2Module06Content -match '[—–]' -or
    $app2Module06Content -match '(?im)[A-Z]:\\Users\\' -or
    $app2Module06Content -notmatch '283,224 bytes' -or
    $app2Module06Content -notmatch '4,361 bytes' -or
    $app2Module06Content -notmatch '0cb7f2d0ffc6d5ae8cbcd0cf206a61f143dcd603b5b34eb312972d2ecc2f0938' -or
    $app2Module06Content -notmatch '155 checks' -or
    $app2Module06Content -notmatch '242 checks' -or
    $app2Module06Content -notmatch '220 checks' -or
    $app2Module06Release.module.id -ne 'oclc-app2-06' -or
    $app2Module06Release.module.version -ne '0.1.0' -or
    $app2Module06Release.module.commons_release -ne '0.61.0' -or
    $app2Module06Release.module.hours -ne 16 -or
    $app2Module06Release.module.application_hours -ne 8 -or
    $app2Module06Release.module.embedded_ml_hours -ne 8 -or
    $app2Module06Release.module.course_points -ne 0 -or
    $app2Module06Release.module.checkpoint_points -ne 45 -or
    $app2Module06Release.upstream.accepted_files -ne 13 -or
    $app2Module06Release.upstream.accepted_bytes -ne 610595 -or
    $app2Module06Release.upstream.frame_rows -ne 1255 -or
    $app2Module06Release.upstream.synthetic_respondents -ne 782 -or
    $app2Module06Release.upstream.synthetic_nonrespondents -ne 473 -or
    $app2Module06Release.partnership_and_improvement.actual_patient_or_caregiver_statements -ne 0 -or
    $app2Module06Release.partnership_and_improvement.partner_requirements -ne 12 -or
    $app2Module06Release.partnership_and_improvement.simulated_interpretation_records -ne 8 -or
    $app2Module06Release.partnership_and_improvement.driver_diagram_rows -ne 14 -or
    $app2Module06Release.partnership_and_improvement.workflow_steps -ne 12 -or
    $app2Module06Release.partnership_and_improvement.measures -ne 14 -or
    $app2Module06Release.response_model.training_rows -ne 878 -or
    $app2Module06Release.response_model.training_respondents -ne 547 -or
    $app2Module06Release.response_model.evaluation_rows -ne 377 -or
    $app2Module06Release.response_model.evaluation_respondents -ne 235 -or
    $app2Module06Release.response_model.transparent_cells -ne 13 -or
    $app2Module06Release.response_model.comment_text_features -ne 0 -or
    $app2Module06Release.reference_results.transparent_brier -ne '0.22962545' -or
    $app2Module06Release.reference_results.bounded_rf_brier -ne '0.23135127' -or
    $app2Module06Release.reference_results.ml_minus_transparent_brier -ne '0.00172582' -or
    $app2Module06Release.reference_results.transparent_auc -ne '0.54335192' -or
    $app2Module06Release.reference_results.bounded_rf_auc -ne '0.53869891' -or
    $app2Module06Release.reference_results.composite_absolute_bias_improvement_pp -ne '0.08367520' -or
    $app2Module06Release.reference_results.ml_changes_response_adjustment_decision -ne 'no' -or
    $app2Module06Release.reference_results.teaching_adjustment -ne 'retain transparent benchmark' -or
    $app2Module06Release.generated_evidence.files -ne 17 -or
    $app2Module06Release.generated_evidence.bytes -ne 283224 -or
    $app2Module06Release.generated_evidence.analysis_checks_passed -ne 22 -or
    $app2Module06Release.generated_evidence.invariants_passed -ne 30 -or
    $app2Module06Release.package.immutable_manifest_rows -ne 28 -or
    $app2Module06Release.package.editable_records -ne 17 -or
    $app2Module06Release.package.assembled_files -ne 46 -or
    $app2Module06Release.package.manifest_bytes -ne 4361 -or
    $app2Module06Release.package.manifest_sha256 -ne '0cb7f2d0ffc6d5ae8cbcd0cf206a61f143dcd603b5b34eb312972d2ecc2f0938' -or
    $app2Module06Release.assessment.week6_points -ne 45 -or
    $app2Module06Release.assessment.noncompensable_gates -ne 24 -or
    $app2Module06Release.progression.reference -ne 'continue with conditions' -or
    $app2Module06Release.progression.checkpoint02_permission -ne 'permitted for cumulative Week 6 assembly' -or
    $app2Module06Release.progression.comment_text_machine_learning -ne 'prohibited' -or
    $app2Module06Upstream.Count -ne 13 -or
    ($app2Module06Upstream | Measure-Object -Property bytes -Sum).Sum -ne 610595 -or
    $app2Module06Checks.Count -ne 22 -or
    @($app2Module06Checks | Where-Object { $_.status -ne 'pass' }).Count -ne 0 -or
    $app2Module06Cells.Count -ne 13 -or
    @($app2Module06Cells | Where-Object { $_.bound_hit -eq 'yes' }).Count -ne 1 -or
    $app2Module06Split.Count -ne 1255 -or
    @($app2Module06Split | Where-Object { $_.split -eq 'training' }).Count -ne 878 -or
    @($app2Module06Split | Where-Object { $_.split -eq 'evaluation' }).Count -ne 377 -or
    $app2Module06Predictions.Count -ne 377 -or
    $app2Module06Performance.Count -ne 2 -or
    @($app2Module06Performance | Where-Object { $_.method -eq 'transparent_benchmark' -and $_.base_weighted_brier -eq '0.22962545' }).Count -ne 1 -or
    @($app2Module06Performance | Where-Object { $_.method -eq 'bounded_random_forest' -and $_.base_weighted_brier -eq '0.23135127' }).Count -ne 1 -or
    $app2Module06Calibration.Count -ne 10 -or
    $app2Module06Diagnostics.Count -ne 3 -or
    @($app2Module06Diagnostics | Where-Object { $_.stability_status -ne 'pass' }).Count -ne 0 -or
    $app2Module06Recovery.Count -ne 12 -or
    @($app2Module06Recovery | Where-Object { $_.measure -eq 'teaching_composite' -and $_.estimator -eq 'bounded_ml_adjusted' -and $_.absolute_bias_pp -eq '2.39922466' }).Count -ne 1 -or
    $app2Module06Subgroups.Count -ne 26 -or
    @($app2Module06Subgroups | Where-Object { $_.support_status -like 'suppress:*' }).Count -ne 8 -or
    $app2Module06Failures.Count -ne 22 -or
    $app2Module06Invariants.Count -ne 30 -or
    @($app2Module06Invariants | Where-Object { $_.status -ne 'pass' }).Count -ne 0 -or
    $app2Module06Gates.Count -ne 24 -or
    @($app2Module06Gates | Where-Object { $_.status -ne 'pass' }).Count -ne 0 -or
    $app2Module06Disagreements.Count -ne 8 -or
    @($app2Module06Disagreements | Where-Object { $_.data_class -ne 'simulated_reference' }).Count -ne 0 -or
    $app2Module06Measures.Count -ne 14 -or
    $app2Module06Engagement -notmatch 'Actual patient or caregiver statements in this package: `0`' -or
    $app2Module06Progression -notmatch 'Week 6 score: `45.00 of 45.00`' -or
    $app2Module06Progression -notmatch 'ML changes response-adjustment decision: `no`'
) {
    throw 'APP-2 Module 06 release metadata, specification, partnership, improvement, model, validation, manifest, or progression facts do not match the 0.1.0 contract.'
}
& python (Join-Path $app2Module06Root 'build_partnered_improvement_ml.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 06 evidence builder self-check failed.' }
& python (Join-Path $app2Module06Root 'build_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 06 workspace builder self-check failed.' }
& python (Join-Path $app2Module06Root 'validate_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 06 validator self-check failed.' }

$app2Checkpoint01Root = Join-Path $repo 'courses\patient-experience-engagement\checkpoints\01-measurement-representation-readiness'
$app2Checkpoint01Spec = Join-Path $repo 'docs\curriculum\courses\APP-2\checkpoints\01-measurement-representation-readiness-spec.md'
$app2Checkpoint01Files = @(
    '.gitattributes', 'VERSION', 'assessment.md', 'instructor-notes.md', 'checkpoint-contract.json',
    'build_checkpoint.py', 'validate_checkpoint.py', 'release.json',
    'template\README.md', 'template\evidence-index.csv', 'template\measurement-representation-review.md',
    'template\reproducibility-check.md', 'template\ai-use.md', 'template\progression-decision.md',
    'reference\README.md', 'reference\evidence-index.csv', 'reference\measurement-representation-review.md',
    'reference\reproducibility-check.md', 'reference\ai-use.md', 'reference\progression-decision.md'
)
$app2Checkpoint01Missing = @()
if (-not (Test-Path -LiteralPath $app2Checkpoint01Spec)) { $app2Checkpoint01Missing += 'specification' }
foreach ($relative in $app2Checkpoint01Files) {
    if (-not (Test-Path -LiteralPath (Join-Path $app2Checkpoint01Root $relative))) {
        $app2Checkpoint01Missing += $relative
    }
}
if ($app2Checkpoint01Missing.Count -gt 0) {
    throw "APP-2 Checkpoint 01 is missing its specification or package files: $($app2Checkpoint01Missing -join ', ')."
}
$app2Checkpoint01Content = Get-Content -Raw -LiteralPath $app2Checkpoint01Spec
$app2Checkpoint01Sections = [regex]::Matches($app2Checkpoint01Content, '(?m)^## \d+\.').Count
$app2Checkpoint01Release = Get-Content -Raw -LiteralPath (Join-Path $app2Checkpoint01Root 'release.json') | ConvertFrom-Json
if (
    $app2Checkpoint01Sections -ne 17 -or
    $app2Checkpoint01Content -match '[—–]' -or
    $app2Checkpoint01Content -match '(?im)[A-Z]:\\Users\\' -or
    $app2Checkpoint01Content -notmatch '23,489 bytes' -or
    $app2Checkpoint01Content -notmatch '5734df858d79721f3efd6766df6299f56d0df49c0aee8b8728b22c284255c903' -or
    $app2Checkpoint01Content -notmatch '714 checks' -or
    $app2Checkpoint01Content -notmatch '683 checks' -or
    $app2Checkpoint01Release.checkpoint.id -ne 'oclc-app2-cp01' -or
    $app2Checkpoint01Release.checkpoint.version -ne '0.1.0' -or
    $app2Checkpoint01Release.checkpoint.commons_release -ne '0.58.0' -or
    $app2Checkpoint01Release.checkpoint.course_points -ne 20 -or
    $app2Checkpoint01Release.accepted_modules.Count -ne 3 -or
    ($app2Checkpoint01Release.accepted_modules | Measure-Object -Property points -Sum).Sum -ne 20 -or
    $app2Checkpoint01Release.accepted_evidence.component_files -ne 135 -or
    $app2Checkpoint01Release.accepted_evidence.synthetic_respondents -ne 782 -or
    $app2Checkpoint01Release.accepted_evidence.response_cells -ne 13 -or
    $app2Checkpoint01Release.package.candidate_manifest_rows -ne 135 -or
    $app2Checkpoint01Release.package.candidate_manifest_bytes -ne 23489 -or
    $app2Checkpoint01Release.package.candidate_manifest_sha256 -ne '5734df858d79721f3efd6766df6299f56d0df49c0aee8b8728b22c284255c903' -or
    $app2Checkpoint01Release.package.assembled_files -ne 149 -or
    $app2Checkpoint01Release.validation.complete_reference_checks -ne 714 -or
    $app2Checkpoint01Release.validation.starter_checks -ne 683 -or
    $app2Checkpoint01Release.progression.reference -ne 'continue with conditions' -or
    $app2Checkpoint01Release.progression.module04_permission -ne 'permitted for linked analysis' -or
    $app2Checkpoint01Release.progression.real_fielding -ne 'prohibited'
) {
    throw 'APP-2 Checkpoint 01 release metadata, specification, candidate manifest, point, validation, or progression facts do not match the 0.1.0 contract.'
}
& python (Join-Path $app2Checkpoint01Root 'build_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Checkpoint 01 builder self-check failed.' }
& python (Join-Path $app2Checkpoint01Root 'validate_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Checkpoint 01 validator self-check failed.' }

$app2Checkpoint02Spec = Join-Path $repo 'docs\curriculum\courses\APP-2\checkpoints\02-linked-evidence-patient-voice-release-spec.md'
$app2Checkpoint02Root = Join-Path $repo 'courses\patient-experience-engagement\checkpoints\02-linked-evidence-patient-voice-release'
$app2Checkpoint02Files = @(
    '.gitattributes', 'VERSION', 'assessment.md', 'build_checkpoint.py',
    'checkpoint-contract.json', 'instructor-notes.md', 'release.json', 'validate_checkpoint.py',
    'template\README.md', 'template\evidence-index.csv',
    'template\linked-evidence-patient-voice-review.md', 'template\reproducibility-check.md',
    'template\ai-use.md', 'template\progression-decision.md',
    'reference\README.md', 'reference\evidence-index.csv',
    'reference\linked-evidence-patient-voice-review.md', 'reference\reproducibility-check.md',
    'reference\ai-use.md', 'reference\progression-decision.md'
)
$app2Checkpoint02Missing = @()
if (-not (Test-Path -LiteralPath $app2Checkpoint02Spec)) { $app2Checkpoint02Missing += 'specification' }
foreach ($relative in $app2Checkpoint02Files) {
    if (-not (Test-Path -LiteralPath (Join-Path $app2Checkpoint02Root $relative))) {
        $app2Checkpoint02Missing += $relative
    }
}
if ($app2Checkpoint02Missing.Count -gt 0) {
    throw "APP-2 Checkpoint 02 is missing its specification or package files: $($app2Checkpoint02Missing -join ', ')."
}
$app2Checkpoint02Content = Get-Content -Raw -LiteralPath $app2Checkpoint02Spec
$app2Checkpoint02Sections = [regex]::Matches($app2Checkpoint02Content, '(?m)^## \d+\.').Count
$app2Checkpoint02Release = Get-Content -Raw -LiteralPath (Join-Path $app2Checkpoint02Root 'release.json') | ConvertFrom-Json
if (
    $app2Checkpoint02Sections -ne 17 -or
    $app2Checkpoint02Content -match '[—–]' -or
    $app2Checkpoint02Content -match '(?im)[A-Z]:\\Users\\' -or
    $app2Checkpoint02Content -notmatch '27,594-byte' -or
    $app2Checkpoint02Content -notmatch '67248e989888cdabeb050c970e85d091ece68018047ef6f0bec7ba26441cfed1' -or
    $app2Checkpoint02Content -notmatch '826 complete-reference checks' -or
    $app2Checkpoint02Content -notmatch '797 learner checks' -or
    $app2Checkpoint02Release.checkpoint.id -ne 'oclc-app2-cp02' -or
    $app2Checkpoint02Release.checkpoint.version -ne '0.1.0' -or
    $app2Checkpoint02Release.checkpoint.commons_release -ne '0.62.0' -or
    $app2Checkpoint02Release.checkpoint.course_points -ne 45 -or
    $app2Checkpoint02Release.accepted_week3.candidate_manifest_sha256 -ne '5734df858d79721f3efd6766df6299f56d0df49c0aee8b8728b22c284255c903' -or
    $app2Checkpoint02Release.accepted_modules.Count -ne 3 -or
    ($app2Checkpoint02Release.accepted_modules | Measure-Object -Property assembled_files -Sum).Sum -ne 160 -or
    ($app2Checkpoint02Release.accepted_modules | Measure-Object -Property points -Sum).Sum -ne 45 -or
    $app2Checkpoint02Release.accepted_modules[2].manifest_sha256 -ne '0cb7f2d0ffc6d5ae8cbcd0cf206a61f143dcd603b5b34eb312972d2ecc2f0938' -or
    $app2Checkpoint02Release.score.total -ne 45 -or
    $app2Checkpoint02Release.score.double_counted_components -ne 0 -or
    $app2Checkpoint02Release.reference_evidence.target_people -ne 1255 -or
    $app2Checkpoint02Release.reference_evidence.linked_events -ne 28455 -or
    $app2Checkpoint02Release.reference_evidence.synthetic_comments -ne 420 -or
    $app2Checkpoint02Release.reference_evidence.actual_patient_or_caregiver_statements -ne 0 -or
    $app2Checkpoint02Release.reference_evidence.improvement_measures -ne 14 -or
    $app2Checkpoint02Release.reference_evidence.ml_changes_response_adjustment_decision -ne 'no' -or
    $app2Checkpoint02Release.package.candidate_files -ne 160 -or
    $app2Checkpoint02Release.package.checkpoint_editable_records -ne 6 -or
    $app2Checkpoint02Release.package.assembled_files -ne 174 -or
    $app2Checkpoint02Release.package.candidate_manifest_bytes -ne 27594 -or
    $app2Checkpoint02Release.package.candidate_manifest_sha256 -ne '67248e989888cdabeb050c970e85d091ece68018047ef6f0bec7ba26441cfed1' -or
    $app2Checkpoint02Release.validation.reference_checks -ne 826 -or
    $app2Checkpoint02Release.validation.learner_checks -ne 797 -or
    $app2Checkpoint02Release.progression.reference -ne 'continue with conditions' -or
    $app2Checkpoint02Release.progression.module07_permission -ne 'permitted for curriculum construction' -or
    $app2Checkpoint02Release.progression.patient_partner_status -notmatch 'simulated reference only' -or
    $app2Checkpoint02Release.progression.clinical_action -ne 'prohibited' -or
    $app2Checkpoint02Release.progression.model_deployment -ne 'prohibited'
) {
    throw 'APP-2 Checkpoint 02 release metadata, specification, accepted identities, score, gates, validation, manifest, or progression facts do not match the 0.1.0 contract.'
}
& python (Join-Path $app2Checkpoint02Root 'build_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Checkpoint 02 builder self-check failed.' }
& python (Join-Path $app2Checkpoint02Root 'validate_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Checkpoint 02 validator self-check failed.' }

$app2Module07Spec = Join-Path $repo 'docs\curriculum\courses\APP-2\modules\07-clinician-patient-leadership-defense-spec.md'
$app2Module07Root = Join-Path $repo 'courses\patient-experience-engagement\modules\07-clinician-patient-leadership-defense'
$app2Module07Files = @(
    '.gitattributes', 'VERSION', 'assessment.md', 'assemble_candidate.py', 'clinician-profile.md',
    'instructor-notes.md', 'leadership-contract.json', 'leadership-session-plan.md',
    'patient-partner-role.md', 'README.md', 'release.json', 'validate_candidate.py',
    'reference\README.md', 'reference\evidence-synthesis.md', 'reference\patient-facing-summary.md',
    'reference\leadership-recommendation.md', 'reference\patient-partner-decision-record.md',
    'reference\stakeholder-roles.csv', 'reference\workflow-feasibility.md',
    'reference\bounded-test-plan.md', 'reference\measures-monitoring.csv',
    'reference\feedback-accountability.md', 'reference\stop-escalation-rules.csv',
    'reference\leadership-reflection.md', 'reference\technical-appendix.md',
    'reference\evidence-index.csv', 'reference\accessibility-language-review.md',
    'reference\reproducibility-check.md', 'reference\ai-use.md', 'reference\component-score.csv',
    'reference\gate-results.csv', 'reference\conditions-register.csv',
    'reference\leadership-defense.md', 'reference\reviewer-record.md',
    'reference\progression-decision.md',
    'template\README.md', 'template\evidence-synthesis.md', 'template\patient-facing-summary.md',
    'template\leadership-recommendation.md', 'template\patient-partner-decision-record.md',
    'template\stakeholder-roles.csv', 'template\workflow-feasibility.md',
    'template\bounded-test-plan.md', 'template\measures-monitoring.csv',
    'template\feedback-accountability.md', 'template\stop-escalation-rules.csv',
    'template\leadership-reflection.md', 'template\technical-appendix.md',
    'template\evidence-index.csv', 'template\accessibility-language-review.md',
    'template\reproducibility-check.md', 'template\ai-use.md', 'template\component-score.csv',
    'template\gate-results.csv', 'template\conditions-register.csv',
    'template\leadership-defense.md', 'template\reviewer-record.md',
    'template\progression-decision.md'
)
$app2Module07Missing = @()
if (-not (Test-Path -LiteralPath $app2Module07Spec)) { $app2Module07Missing += 'specification' }
foreach ($relative in $app2Module07Files) {
    if (-not (Test-Path -LiteralPath (Join-Path $app2Module07Root $relative))) {
        $app2Module07Missing += $relative
    }
}
if ($app2Module07Missing.Count -gt 0) {
    throw "APP-2 Module 07 is missing its specification or package files: $($app2Module07Missing -join ', ')."
}
$app2Module07Content = Get-Content -Raw -LiteralPath $app2Module07Spec
$app2Module07Sections = [regex]::Matches($app2Module07Content, '(?m)^## \d+\.').Count
$app2Module07Release = Get-Content -Raw -LiteralPath (Join-Path $app2Module07Root 'release.json') | ConvertFrom-Json
$app2Module07Scores = Import-Csv -LiteralPath (Join-Path $app2Module07Root 'reference\component-score.csv')
$app2Module07Gates = Import-Csv -LiteralPath (Join-Path $app2Module07Root 'reference\gate-results.csv')
$app2Module07Measures = Import-Csv -LiteralPath (Join-Path $app2Module07Root 'reference\measures-monitoring.csv')
$app2Module07Stops = Import-Csv -LiteralPath (Join-Path $app2Module07Root 'reference\stop-escalation-rules.csv')
if (
    $app2Module07Sections -ne 22 -or
    $app2Module07Content -match '[—–]' -or
    $app2Module07Content -match '(?im)[A-Z]:\\Users\\' -or
    $app2Module07Content -notmatch '64,149 bytes' -or
    $app2Module07Content -notmatch '53bd306692145df85d1b2a709615000f80829099a916659c6a8cfd3bd994697f' -or
    $app2Module07Content -notmatch '1,847 checks' -or
    $app2Module07Content -notmatch '1,794 checks' -or
    $app2Module07Release.module.id -ne 'oclc-app2-07' -or
    $app2Module07Release.module.version -ne '0.1.0' -or
    $app2Module07Release.module.commons_release -ne '0.63.0' -or
    $app2Module07Release.module.hours -ne 16 -or
    $app2Module07Release.module.course_points -ne 35 -or
    $app2Module07Release.clinician_of_record.name -ne 'Joe Joseph, MD, SFHM' -or
    $app2Module07Release.clinician_of_record.current_employer_claim -ne 'none' -or
    $app2Module07Release.patient_partner_co_lead.status -ne 'pending before alpha' -or
    $app2Module07Release.patient_partner_co_lead.actual_statements_in_reference -ne 0 -or
    $app2Module07Release.accepted_inputs.Count -ne 2 -or
    ($app2Module07Release.accepted_inputs | Measure-Object -Property assembled_files -Sum).Sum -ne 323 -or
    $app2Module07Release.accepted_inputs[0].candidate_manifest_sha256 -ne '5734df858d79721f3efd6766df6299f56d0df49c0aee8b8728b22c284255c903' -or
    $app2Module07Release.accepted_inputs[1].candidate_manifest_sha256 -ne '67248e989888cdabeb050c970e85d091ece68018047ef6f0bec7ba26441cfed1' -or
    $app2Module07Release.reference_decision.candidate_status -ne 'accept with conditions' -or
    $app2Module07Release.reference_decision.organizational_recommendation -ne 'revise before testing' -or
    $app2Module07Release.reference_decision.final_checkpoint -ne 'permitted for curriculum construction' -or
    $app2Module07Release.reference_decision.patient_contact_and_fielding -ne 'prohibited' -or
    $app2Module07Release.reference_decision.clinical_implementation -ne 'prohibited' -or
    $app2Module07Release.reference_decision.model_deployment -ne 'prohibited' -or
    $app2Module07Release.reference_facts.target_people -ne 1255 -or
    $app2Module07Release.reference_facts.linked_events -ne 28455 -or
    $app2Module07Release.reference_facts.synthetic_comments -ne 420 -or
    $app2Module07Release.reference_facts.actual_patient_or_caregiver_statements -ne 0 -or
    $app2Module07Release.reference_facts.prospective_measures -ne 14 -or
    $app2Module07Release.reference_facts.stop_rules -ne 14 -or
    $app2Module07Release.reference_facts.ml_changes_response_adjustment_decision -ne 'no' -or
    $app2Module07Release.package.immutable_controls -ne 9 -or
    $app2Module07Release.package.accepted_evidence_files -ne 325 -or
    $app2Module07Release.package.immutable_manifest_rows -ne 334 -or
    $app2Module07Release.package.leadership_records -ne 23 -or
    $app2Module07Release.package.candidate_files -ne 358 -or
    $app2Module07Release.package.manifest_bytes -ne 64149 -or
    $app2Module07Release.package.manifest_sha256 -ne '53bd306692145df85d1b2a709615000f80829099a916659c6a8cfd3bd994697f' -or
    $app2Module07Release.validation.complete_reference_checks -ne 1847 -or
    $app2Module07Release.validation.starter_checks -ne 1794 -or
    ($app2Module07Scores | Measure-Object -Property maximum -Sum).Sum -ne 35 -or
    ($app2Module07Scores | Measure-Object -Property score -Sum).Sum -ne 35 -or
    $app2Module07Gates.Count -ne 26 -or
    @($app2Module07Gates | Where-Object { $_.result -eq 'fail' }).Count -ne 0 -or
    $app2Module07Measures.Count -ne 14 -or
    $app2Module07Stops.Count -ne 14
) {
    throw 'APP-2 Module 07 release metadata, specification, clinician and patient roles, accepted evidence, score, gates, monitoring, validation, or manifest facts do not match the 0.1.0 contract.'
}
& python (Join-Path $app2Module07Root 'assemble_candidate.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 07 assembler self-check failed.' }
& python (Join-Path $app2Module07Root 'validate_candidate.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 Module 07 validator self-check failed.' }

$app2Checkpoint03Root = Join-Path $repo 'courses\patient-experience-engagement\checkpoints\03-patient-experience-engagement-package'
$app2Checkpoint03Spec = Join-Path $repo 'docs\curriculum\courses\APP-2\checkpoints\03-patient-experience-engagement-package-spec.md'
$app2Checkpoint03Records = @(
    'submission-record.md', 'final-score.csv', 'gate-results.csv', 'final-defense.md',
    'reviewer-record.md', 'final-reproduction.md', 'conditions-register.csv',
    'final-audit.md', 'final-decision.md', 'release-acceptance.md'
)
$app2Checkpoint03Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'final-contract.json', 'assessment.md',
    'instructor-guide.md', 'assemble_final.py', 'validate_final.py', 'release.json'
) + @($app2Checkpoint03Records | ForEach-Object { "reference\$_" }) + @($app2Checkpoint03Records | ForEach-Object { "template\$_" })
$app2Checkpoint03Missing = @($app2Checkpoint03Files | Where-Object { -not (Test-Path -LiteralPath (Join-Path $app2Checkpoint03Root $_)) })
if (-not (Test-Path -LiteralPath $app2Checkpoint03Spec) -or $app2Checkpoint03Missing.Count -gt 0) {
    throw "APP-2 final checkpoint is missing its specification or package files: $($app2Checkpoint03Missing -join ', ')."
}
$app2Checkpoint03Content = Get-Content -Raw -LiteralPath $app2Checkpoint03Spec
$app2Checkpoint03Sections = [regex]::Matches($app2Checkpoint03Content, '(?m)^## \d+\.').Count
$app2Checkpoint03Release = Get-Content -Raw -LiteralPath (Join-Path $app2Checkpoint03Root 'release.json') | ConvertFrom-Json
$app2Checkpoint03Scores = @(Import-Csv -LiteralPath (Join-Path $app2Checkpoint03Root 'reference\final-score.csv'))
$app2Checkpoint03Gates = @(Import-Csv -LiteralPath (Join-Path $app2Checkpoint03Root 'reference\gate-results.csv'))
if (
    $app2Checkpoint03Sections -ne 17 -or
    $app2Checkpoint03Content -match '[—–]' -or
    $app2Checkpoint03Content -match '(?im)[A-Z]:\\Users\\' -or
    $app2Checkpoint03Content -notmatch 'Commons release target: 0\.64\.0' -or
    $app2Checkpoint03Content -notmatch 'a3ca6bbacd22ab82d6679feb674f061ee98db9e681fc18deba5cc8ee9a93183b' -or
    $app2Checkpoint03Content -notmatch '1,890 checks' -or
    $app2Checkpoint03Content -notmatch '1,841 checks' -or
    $app2Checkpoint03Release.checkpoint.id -ne 'oclc-app2-cp03' -or
    $app2Checkpoint03Release.checkpoint.version -ne '0.1.0' -or
    $app2Checkpoint03Release.checkpoint.commons_release -ne '0.64.0' -or
    $app2Checkpoint03Release.checkpoint.course_points -ne 35 -or
    $app2Checkpoint03Release.accepted_candidate.candidate_files -ne 358 -or
    $app2Checkpoint03Release.accepted_candidate.immutable_manifest_rows -ne 334 -or
    $app2Checkpoint03Release.accepted_candidate.immutable_manifest_bytes -ne 64149 -or
    $app2Checkpoint03Release.accepted_candidate.immutable_manifest_sha256 -ne '53bd306692145df85d1b2a709615000f80829099a916659c6a8cfd3bd994697f' -or
    $app2Checkpoint03Release.accepted_candidate.release_sha256 -ne '2a30f59869be0041b813ce6005c226a9bcd3cd28632222464a5defc1586ca317' -or
    $app2Checkpoint03Release.package.candidate_manifest_rows -ne 358 -or
    $app2Checkpoint03Release.package.candidate_manifest_bytes -ne 60523 -or
    $app2Checkpoint03Release.package.candidate_manifest_sha256 -ne 'a3ca6bbacd22ab82d6679feb674f061ee98db9e681fc18deba5cc8ee9a93183b' -or
    $app2Checkpoint03Release.package.assembled_files -ne 373 -or
    $app2Checkpoint03Release.course_score.total -ne 100 -or
    $app2Checkpoint03Release.course_score.double_counted_components -ne 0 -or
    $app2Checkpoint03Release.reference_decision.package_disposition -ne 'accept with conditions' -or
    $app2Checkpoint03Release.reference_decision.organizational_recommendation -ne 'revise before testing' -or
    $app2Checkpoint03Release.reference_decision.actual_patient_or_caregiver_statements -ne 0 -or
    $app2Checkpoint03Release.reference_decision.patient_partner_status -ne 'pending before alpha' -or
    $app2Checkpoint03Release.reference_decision.patient_contact_and_fielding -ne 'prohibited' -or
    $app2Checkpoint03Release.reference_decision.official_hcahps_reporting -ne 'prohibited' -or
    $app2Checkpoint03Release.reference_decision.patient_or_group_targeting -ne 'prohibited' -or
    $app2Checkpoint03Release.reference_decision.clinical_implementation -ne 'prohibited' -or
    $app2Checkpoint03Release.reference_decision.model_deployment -ne 'prohibited' -or
    $app2Checkpoint03Release.reference_decision.tag_status -ne 'proposed - not created' -or
    $app2Checkpoint03Release.validation.complete_reference_checks -ne 1890 -or
    $app2Checkpoint03Release.validation.starter_checks -ne 1841 -or
    $app2Checkpoint03Scores.Count -ne 5 -or
    ($app2Checkpoint03Scores | Measure-Object -Property maximum -Sum).Sum -ne 35 -or
    ($app2Checkpoint03Scores | Measure-Object -Property score -Sum).Sum -ne 35 -or
    $app2Checkpoint03Gates.Count -ne 26 -or
    @($app2Checkpoint03Gates | Where-Object { $_.result -eq 'fail' }).Count -ne 0
) {
    throw 'APP-2 final checkpoint release metadata, specification, score, gates, partnership status, validation, manifest, or separate decisions do not match the 0.1.0 contract.'
}
& python (Join-Path $app2Checkpoint03Root 'assemble_final.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 final checkpoint assembler self-check failed.' }
& python (Join-Path $app2Checkpoint03Root 'validate_final.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-2 final checkpoint validator self-check failed.' }

$app3 = Join-Path $repo 'docs\curriculum\courses\APP-3\course-spec.md'
$app3Source = Join-Path $repo 'docs\source\app-3-clinical-performance-improvement-source-record.md'
$app3Package = Join-Path $repo 'courses\clinical-performance-improvement\README.md'
if (-not (Test-Path -LiteralPath $app3) -or -not (Test-Path -LiteralPath $app3Source) -or -not (Test-Path -LiteralPath $app3Package)) {
    throw 'APP-3 must include its course specification, source record, and course package README.'
}
$app3Content = Get-Content -Raw -LiteralPath $app3
$app3SourceContent = Get-Content -Raw -LiteralPath $app3Source
$app3PackageContent = Get-Content -Raw -LiteralPath $app3Package
$app3Sections = [regex]::Matches($app3Content, '(?m)^## \d+\.').Count
$app3ModuleCount = [regex]::Matches($app3Content, '(?m)^## \d+\. Module \d{2} brief:').Count
$app3HourMatches = [regex]::Matches(
    $app3Content,
    '(?m)^\| \d{2} \| [^|]+ \| \d \| (?<hours>\d+(?:\.\d+)?) \|'
)
$app3Hours = ($app3HourMatches | ForEach-Object { [decimal]$_.Groups['hours'].Value } | Measure-Object -Sum).Sum
$app3CheckpointCount = [regex]::Matches($app3Content, '(?m)^### (?:Checkpoint \d|Final checkpoint):').Count
$app3SourceModuleRows = [regex]::Matches($app3SourceContent, '(?m)^\| [1-7] \| [^|]+ \| (?<hours>\d+(?:\.\d+)?) \|').Count
if (
    $app3Sections -ne 24 -or
    $app3ModuleCount -ne 7 -or
    $app3HourMatches.Count -ne 7 -or
    $app3Hours -ne [decimal]112.5 -or
    $app3CheckpointCount -ne 3 -or
    $app3SourceModuleRows -ne 7
) {
    throw "APP-3 must define 24 course sections, seven modules, seven schedule rows totaling 112.5 hours, three checkpoints, and seven source rows; found $app3Sections sections, $app3ModuleCount modules, $($app3HourMatches.Count) schedule rows, $app3Hours hours, $app3CheckpointCount checkpoints, and $app3SourceModuleRows source rows."
}
if (
    $app3Content -match '[—–]' -or
    $app3SourceContent -match '[—–]' -or
    $app3PackageContent -match '[—–]' -or
    $app3Content -match '(?im)[A-Z]:\\Users\\' -or
    $app3SourceContent -match '(?im)[A-Z]:\\Users\\' -or
    $app3PackageContent -match '(?im)[A-Z]:\\Users\\' -or
    $app3Content -notmatch 'Current Commons release: 0\.73\.0' -or
    $app3PackageContent -notmatch 'Current Commons release: 0\.73\.0' -or
    $app3Content -notmatch '084a412054c77169ea065cf15ed3cc7097e412a6017fbb58a260e909d17717e3' -or
    $app3SourceContent -notmatch '084a412054c77169ea065cf15ed3cc7097e412a6017fbb58a260e909d17717e3' -or
    $app3SourceContent -notmatch '26,907' -or
    $app3SourceContent -notmatch 'Curriculum-30-Credits-2026-08-29\.zip' -or
    $app3SourceContent -notmatch 'OneDrive_2026-08-29 \(1\)\.zip' -or
    ([regex]::Matches($app3SourceContent, '20%')).Count -ne 2 -or
    $app3SourceContent -notmatch '25%' -or
    $app3SourceContent -notmatch '35%' -or
    $app3Content -notmatch '40 \+ 25 \+ 35 = 100' -or
    $app3Content -notmatch 'CGH-ED-01' -or
    $app3SourceContent -notmatch 'CGH-ED-01' -or
    $app3PackageContent -notmatch 'CGH-ED-01' -or
    $app3Content -notmatch '1e5a1ca803c2b09468fe3ae3fe60fef3e910f5f5300630a24791c88a1abff516' -or
    $app3SourceContent -notmatch '1e5a1ca803c2b09468fe3ae3fe60fef3e910f5f5300630a24791c88a1abff516' -or
    $app3Content -notmatch 'f28f5d56e5e0e29001c7a275b01306762e673c9a21459dc7a68ff1aea782943b' -or
    $app3Content -notmatch 'https://data\.cms\.gov/provider-data/dataset/yv7e-xc69' -or
    $app3Content -notmatch 'https://data\.cms\.gov/provider-data/dataset/ynj2-r877' -or
    $app3Content -notmatch 'https://healthdata\.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/anag-cw7u' -or
    $app3Content -notmatch 'Application and monitoring block: 8\.0 hours' -or
    $app3Content -notmatch 'Embedded ML extension: 8\.0 hours' -or
    $app3Content -notmatch 'gradient-boosted' -or
    $app3Content -notmatch 'Joe Joseph, MD, SFHM' -or
    $app3Content -notmatch 'https://www\.mghihp\.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current\.pdf' -or
    $app3Content -notmatch 'Module 01 pins all three complete public snapshots' -or
    $app3PackageContent -notmatch 'Modules 01 through 06, and Checkpoints 01 and 02 complete' -or
    $app3Content -notmatch '26dc5ada150a735fa1807cebc3274619a14495b2286fd34e9083b4508cfa367d' -or
    $app3SourceContent -notmatch '26dc5ada150a735fa1807cebc3274619a14495b2286fd34e9083b4508cfa367d' -or
    $app3Content -notmatch 'b3ef37e7e8d9888ff241caab83ec43be7e26be3c592a5a4e120acbf541edea7f' -or
    $app3SourceContent -notmatch 'b3ef37e7e8d9888ff241caab83ec43be7e26be3c592a5a4e120acbf541edea7f' -or
    (Get-Content -Raw -LiteralPath (Join-Path $repo 'VERSION')).Trim() -ne '0.73.0'
) {
    throw 'APP-3 is missing its source, version, workload, 40/25/35 assessment, public-data, synthetic-service, ML, leadership, calendar, build-status, or plain-ASCII contract.'
}

$app3Module01Root = Join-Path $repo 'courses\clinical-performance-improvement\modules\01-clinical-performance-decision'
$app3Module01Spec = Join-Path $repo 'docs\curriculum\courses\APP-3\modules\01-clinical-performance-decision-spec.md'
$app3Module01Files = @(
    '.gitattributes',
    'README.md',
    'VERSION',
    'assessment.md',
    'build_workspace.py',
    'data-spec.md',
    'decision-contract.json',
    'instructor-notes.md',
    'profile_sources.py',
    'release.json',
    'source-record.yml',
    'validate_workspace.py',
    'data\capacity-source-profile.csv',
    'data\measure-family-anchors.csv',
    'data\source-inventory.csv',
    'data\raw\Complications_and_Deaths-Hospital.csv.gz',
    'data\raw\HHS-Capacity-Massachusetts.csv.gz',
    'data\raw\Timely_and_Effective_Care-Hospital.csv.gz',
    'reference\ai-use.md',
    'reference\claim-boundary.csv',
    'reference\clinical-performance-charter.md',
    'reference\measure-family.csv',
    'reference\process-boundary.csv',
    'reference\progression-decision.md',
    'reference\source-feasibility-interpretation.md',
    'reference\stakeholder-accountability-map.csv',
    'reference\synthetic-service-declaration.md',
    'reference\unit-of-flow.csv',
    'template\ai-use.md',
    'template\claim-boundary.csv',
    'template\clinical-performance-charter.md',
    'template\measure-family.csv',
    'template\process-boundary.csv',
    'template\progression-decision.md',
    'template\source-feasibility-interpretation.md',
    'template\stakeholder-accountability-map.csv',
    'template\synthetic-service-declaration.md',
    'template\unit-of-flow.csv'
)
$app3Module01Missing = @($app3Module01Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $app3Module01Root $_))
})
if (-not (Test-Path -LiteralPath $app3Module01Spec) -or $app3Module01Missing.Count -gt 0) {
    throw "APP-3 Module 01 is missing its specification or package files: $($app3Module01Missing -join ', ')."
}
$app3Module01Content = Get-Content -Raw -LiteralPath $app3Module01Spec
$app3Module01Sections = [regex]::Matches($app3Module01Content, '(?m)^## \d+\.').Count
$app3Module01Release = Get-Content -Raw -LiteralPath (Join-Path $app3Module01Root 'release.json') | ConvertFrom-Json
$app3Module01Contract = Get-Content -Raw -LiteralPath (Join-Path $app3Module01Root 'decision-contract.json') | ConvertFrom-Json
if (
    $app3Module01Sections -ne 21 -or
    $app3Module01Content -match '[—–]' -or
    $app3Module01Content -match '(?im)[A-Z]:\\Users\\' -or
    $app3Module01Content -notmatch '15\.5 hours' -or
    $app3Module01Content -notmatch '138,084' -or
    $app3Module01Content -notmatch '95,800' -or
    $app3Module01Content -notmatch '1,045,406' -or
    $app3Module01Content -notmatch 'CGH-ED-01' -or
    $app3Module01Content -notmatch 'course points awarded here: 0' -or
    $app3Module01Content -notmatch 'continue with conditions' -or
    $app3Module01Content -notmatch 'operational diagnosis' -or
    $app3Module01Content -notmatch 'staffing change' -or
    $app3Module01Release.module_id -ne 'oclc-app3-01' -or
    $app3Module01Release.module_version -ne '0.1.0' -or
    $app3Module01Release.commons_release -ne '0.66.0' -or
    $app3Module01Release.source_snapshots.cms_timely_rows -ne 138084 -or
    $app3Module01Release.source_snapshots.cms_complications_rows -ne 95800 -or
    $app3Module01Release.source_snapshots.hhs_capacity_rows -ne 1045406 -or
    $app3Module01Release.workspace.immutable_manifest_rows -ne 14 -or
    $app3Module01Release.workspace.editable_records -ne 10 -or
    $app3Module01Release.workspace.assembled_files -ne 25 -or
    $app3Module01Release.reference_decision.progression -ne 'continue with conditions' -or
    $app3Module01Release.reference_decision.staffing_change -ne 'prohibited' -or
    $app3Module01Release.reference_decision.public_to_synthetic_linkage -ne 'prohibited' -or
    $app3Module01Contract.sources.timely.sha256 -ne '1e5a1ca803c2b09468fe3ae3fe60fef3e910f5f5300630a24791c88a1abff516' -or
    $app3Module01Contract.sources.complications.sha256 -ne '26dc5ada150a735fa1807cebc3274619a14495b2286fd34e9083b4508cfa367d' -or
    $app3Module01Contract.sources.capacity.sha256 -ne 'b3ef37e7e8d9888ff241caab83ec43be7e26be3c592a5a4e120acbf541edea7f' -or
    $app3Module01Contract.assessment.course_points_awarded_here -ne 0 -or
    $app3Module01Contract.assessment.week3_measure_component_points -ne 20 -or
    $app3Module01Contract.assessment.week3_performance_diagnostic_points -ne 20
) {
    throw 'APP-3 Module 01 specification, source identities, workspace contract, assessment handoff, progression, or responsible-claim boundary does not match the 0.1.0 contract.'
}
& python (Join-Path $app3Module01Root 'profile_sources.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 01 source profiler self-check failed.' }
& python (Join-Path $app3Module01Root 'build_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 01 builder self-check failed.' }
& python (Join-Path $app3Module01Root 'validate_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 01 validator self-check failed.' }

$app3Module02Root = Join-Path $repo 'courses\clinical-performance-improvement\modules\02-measures-operational-metrics'
$app3Module02Spec = Join-Path $repo 'docs\curriculum\courses\APP-3\modules\02-measures-operational-metrics-spec.md'
$app3Module02Files = @(
    '.gitattributes',
    'README.md',
    'VERSION',
    'assessment.md',
    'build_measures.py',
    'build_workspace.py',
    'data-spec.md',
    'freeze_upstream.py',
    'generate_operational_release.py',
    'instructor-notes.md',
    'operational-contract.json',
    'release.json',
    'source-record.yml',
    'validate_workspace.py',
    'data\data-dictionary.csv',
    'data\operational-source-manifest.csv',
    'data\raw\calendar-demand.csv.gz',
    'data\raw\defect-register.csv.gz',
    'data\raw\encounters.csv.gz',
    'data\raw\known-truth.csv.gz',
    'data\raw\process-events.csv.gz',
    'data\raw\queue-snapshots.csv.gz',
    'data\raw\safety-events.csv.gz',
    'data\raw\scenarios.csv.gz',
    'data\raw\staffing.csv.gz',
    'outputs\build-report.json',
    'outputs\defect-impact.csv',
    'outputs\encounter-measures.csv.gz',
    'outputs\query-checks.csv',
    'outputs\safety-diagnostics.csv',
    'outputs\shift-metrics.csv',
    'outputs\source-reconciliation.csv',
    'outputs\subgroup-support.csv',
    'outputs\weekly-metrics.csv',
    'upstream\module01-handoff-manifest.csv',
    'reference\measure-specifications.csv',
    'reference\defect-repair-log.csv',
    'reference\event-validation.md',
    'reference\operational-interpretation.md',
    'reference\subgroup-support-interpretation.md',
    'reference\measure-score.csv',
    'reference\gate-results.csv',
    'reference\ai-use.md',
    'reference\progression-decision.md',
    'reference\reproducibility-check.md',
    'reference\sql\01-clean-operational-sources.sql',
    'reference\sql\02-encounter-measures.sql',
    'reference\sql\03-operational-measures.sql',
    'reference\sql\04-validation-and-defects.sql',
    'template\measure-specifications.csv',
    'template\defect-repair-log.csv',
    'template\event-validation.md',
    'template\operational-interpretation.md',
    'template\subgroup-support-interpretation.md',
    'template\measure-score.csv',
    'template\gate-results.csv',
    'template\ai-use.md',
    'template\progression-decision.md',
    'template\reproducibility-check.md',
    'template\sql\01-clean-operational-sources.sql',
    'template\sql\02-encounter-measures.sql',
    'template\sql\03-operational-measures.sql',
    'template\sql\04-validation-and-defects.sql'
)
$app3Module02Missing = @($app3Module02Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $app3Module02Root $_))
})
if (-not (Test-Path -LiteralPath $app3Module02Spec) -or $app3Module02Missing.Count -gt 0) {
    throw "APP-3 Module 02 is missing its specification or package files: $($app3Module02Missing -join ', ')."
}
$app3Module02Content = Get-Content -Raw -LiteralPath $app3Module02Spec
$app3Module02Sections = [regex]::Matches($app3Module02Content, '(?m)^## \d+\.').Count
$app3Module02Release = Get-Content -Raw -LiteralPath (Join-Path $app3Module02Root 'release.json') | ConvertFrom-Json
$app3Module02Contract = Get-Content -Raw -LiteralPath (Join-Path $app3Module02Root 'operational-contract.json') | ConvertFrom-Json
$app3Module02Report = Get-Content -Raw -LiteralPath (Join-Path $app3Module02Root 'outputs\build-report.json') | ConvertFrom-Json
$app3Module02Manifest = @(Import-Csv -LiteralPath (Join-Path $app3Module02Root 'data\operational-source-manifest.csv'))
$app3Module02Measures = @(Import-Csv -LiteralPath (Join-Path $app3Module02Root 'reference\measure-specifications.csv'))
$app3Module02Defects = @(Import-Csv -LiteralPath (Join-Path $app3Module02Root 'reference\defect-repair-log.csv'))
$app3Module02Gates = @(Import-Csv -LiteralPath (Join-Path $app3Module02Root 'reference\gate-results.csv'))
if (
    $app3Module02Sections -ne 21 -or
    $app3Module02Content -match '[—–]' -or
    $app3Module02Content -notmatch '318,732' -or
    $app3Module02Content -notmatch '43,628' -or
    $app3Module02Content -notmatch '75.2796' -or
    $app3Module02Content -notmatch 'continue with conditions' -or
    $app3Module02Release.module_id -ne 'oclc-app3-02' -or
    $app3Module02Release.module_version -ne '0.1.0' -or
    $app3Module02Release.commons_release -ne '0.67.0' -or
    $app3Module02Release.reference_score -ne 20 -or
    $app3Module02Release.reference_gates_passed -ne 15 -or
    $app3Module02Contract.module.hours -ne 16.0 -or
    $app3Module02Contract.source.rows -ne 318732 -or
    $app3Module02Contract.source.defects -ne 12 -or
    $app3Module02Contract.measures.specifications -ne 17 -or
    $app3Module02Contract.measures.query_checks -ne 30 -or
    $app3Module02Manifest.Count -ne 9 -or
    ($app3Module02Manifest | Measure-Object -Property rows -Sum).Sum -ne 318732 -or
    $app3Module02Measures.Count -ne 17 -or
    $app3Module02Defects.Count -ne 12 -or
    $app3Module02Gates.Count -ne 15 -or
    @($app3Module02Gates | Where-Object { $_.status -ne 'pass' }).Count -ne 0 -or
    $app3Module02Report.findings.accepted_encounters -ne 43628 -or
    $app3Module02Report.findings.query_checks -ne 30 -or
    $app3Module02Report.findings.failed_query_checks -ne 0 -or
    @($app3Module02Report.outputs.PSObject.Properties).Count -ne 8
) {
    throw 'APP-3 Module 02 specification, source release, measure outputs, assessment, progression, or responsible-claim boundary does not match the 0.1.0 contract.'
}
& python (Join-Path $app3Module02Root 'generate_operational_release.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 02 source-generator self-check failed.' }
& python (Join-Path $app3Module02Root 'freeze_upstream.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 02 upstream self-check failed.' }
& python (Join-Path $app3Module02Root 'build_measures.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 02 measure-builder self-check failed.' }
& python (Join-Path $app3Module02Root 'build_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 02 workspace-builder self-check failed.' }
& python (Join-Path $app3Module02Root 'validate_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 02 validator self-check failed.' }

$app3Module03Root = Join-Path $repo 'courses\clinical-performance-improvement\modules\03-variation-safety-bottlenecks'
$app3Module03Spec = Join-Path $repo 'docs\curriculum\courses\APP-3\modules\03-variation-safety-bottlenecks-spec.md'
$app3Module03Files = @(
    '.gitattributes',
    'README.md',
    'VERSION',
    'assessment.md',
    'build_diagnostic.py',
    'build_workspace.py',
    'data-spec.md',
    'diagnostic-contract.json',
    'freeze_upstream.py',
    'instructor-notes.md',
    'release.json',
    'source-record.yml',
    'validate_workspace.py',
    'verify_control_charts.R',
    'upstream\module02-handoff-manifest.csv',
    'upstream\module02-release.json',
    'upstream\module02-operational-contract.json',
    'upstream\operational-source-manifest.csv',
    'upstream\encounter-measures.csv.gz',
    'upstream\weekly-metrics.csv',
    'upstream\shift-metrics.csv',
    'upstream\safety-events.csv.gz',
    'upstream\safety-diagnostics.csv',
    'upstream\subgroup-support.csv',
    'outputs\variation-series.csv',
    'outputs\control-limits.csv',
    'outputs\signal-audit.csv',
    'outputs\weekly-safety.csv',
    'outputs\safety-surveillance.csv',
    'outputs\process-stage-comparison.csv',
    'outputs\bottleneck-reconciliation.csv',
    'outputs\subgroup-window-support.csv',
    'outputs\diagnostic-findings.json',
    'outputs\weekly-arrival-to-clinician-xmr.svg',
    'outputs\weekly-left-before-seen-p-chart.svg',
    'outputs\weekly-incident-report-u-chart.svg',
    'outputs\process-stage-comparison.svg',
    'reference\process-map.csv',
    'reference\chart-selection.csv',
    'reference\signal-rules.csv',
    'reference\performance-diagnostic.md',
    'reference\safety-interpretation.md',
    'reference\bottleneck-interpretation.md',
    'reference\subgroup-support-interpretation.md',
    'reference\escalation-rule.md',
    'reference\week3-score.csv',
    'reference\gate-results.csv',
    'reference\ai-use.md',
    'reference\progression-decision.md',
    'reference\reproducibility-check.md',
    'template\process-map.csv',
    'template\chart-selection.csv',
    'template\signal-rules.csv',
    'template\performance-diagnostic.md',
    'template\safety-interpretation.md',
    'template\bottleneck-interpretation.md',
    'template\subgroup-support-interpretation.md',
    'template\escalation-rule.md',
    'template\week3-score.csv',
    'template\gate-results.csv',
    'template\ai-use.md',
    'template\progression-decision.md',
    'template\reproducibility-check.md'
)
$app3Module03Missing = @($app3Module03Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $app3Module03Root $_))
})
if (-not (Test-Path -LiteralPath $app3Module03Spec) -or $app3Module03Missing.Count -gt 0) {
    throw "APP-3 Module 03 is missing its specification or package files: $($app3Module03Missing -join ', ')."
}
$app3Module03Content = Get-Content -Raw -LiteralPath $app3Module03Spec
$app3Module03Sections = [regex]::Matches($app3Module03Content, '(?m)^## \d+\.').Count
$app3Module03Release = Get-Content -Raw -LiteralPath (Join-Path $app3Module03Root 'release.json') | ConvertFrom-Json
$app3Module03Contract = Get-Content -Raw -LiteralPath (Join-Path $app3Module03Root 'diagnostic-contract.json') | ConvertFrom-Json
$app3Module03Findings = Get-Content -Raw -LiteralPath (Join-Path $app3Module03Root 'outputs\diagnostic-findings.json') | ConvertFrom-Json
$app3Module03Variation = @(Import-Csv -LiteralPath (Join-Path $app3Module03Root 'outputs\variation-series.csv'))
$app3Module03Signals = @(Import-Csv -LiteralPath (Join-Path $app3Module03Root 'outputs\signal-audit.csv'))
$app3Module03Safety = @(Import-Csv -LiteralPath (Join-Path $app3Module03Root 'outputs\safety-surveillance.csv'))
$app3Module03Stages = @(Import-Csv -LiteralPath (Join-Path $app3Module03Root 'outputs\process-stage-comparison.csv'))
$app3Module03Bottlenecks = @(Import-Csv -LiteralPath (Join-Path $app3Module03Root 'outputs\bottleneck-reconciliation.csv'))
$app3Module03Subgroups = @(Import-Csv -LiteralPath (Join-Path $app3Module03Root 'outputs\subgroup-window-support.csv'))
$app3Module03Gates = @(Import-Csv -LiteralPath (Join-Path $app3Module03Root 'reference\gate-results.csv'))
$app3Module03Score = @(Import-Csv -LiteralPath (Join-Path $app3Module03Root 'reference\week3-score.csv'))
if (
    $app3Module03Sections -ne 21 -or
    $app3Module03Content -match '[—–]' -or
    $app3Module03Content -notmatch '97\.636958' -or
    $app3Module03Content -notmatch '75\.2796' -or
    $app3Module03Content -notmatch 'continue with conditions' -or
    $app3Module03Content -notmatch '259' -or
    $app3Module03Content -notmatch '130' -or
    $app3Module03Release.module_id -ne 'oclc-app3-03' -or
    $app3Module03Release.module_version -ne '0.1.0' -or
    $app3Module03Release.commons_release -ne '0.68.0' -or
    $app3Module03Release.reference_score -ne 20 -or
    $app3Module03Release.reference_gates_passed -ne 18 -or
    $app3Module03Release.reference_progression -ne 'continue with conditions' -or
    $app3Module03Contract.module.hours -ne 16.5 -or
    $app3Module03Contract.upstream.accepted_encounters -ne 43628 -or
    $app3Module03Contract.diagnostic.charts -ne 4 -or
    $app3Module03Contract.diagnostic.signal_rules -ne 3 -or
    $app3Module03Contract.diagnostic.signal_records -ne 9 -or
    $app3Module03Contract.diagnostic.outputs -ne 13 -or
    $app3Module03Contract.diagnostic.target_stage_median_minutes -ne 66.0 -or
    $app3Module03Contract.assessment.week3_total_points -ne 40 -or
    $app3Module03Findings.control_charts.signal_records -ne 9 -or
    $app3Module03Findings.bounded_diagnosis.target_median_minutes -ne 66.0 -or
    $app3Module03Findings.safety.known_true_events -ne 894 -or
    $app3Module03Findings.subgroup.target_window_claim_status -ne 'not supported' -or
    $app3Module03Variation.Count -ne 208 -or
    $app3Module03Signals.Count -ne 9 -or
    $app3Module03Safety.Count -ne 6 -or
    $app3Module03Stages.Count -ne 20 -or
    $app3Module03Bottlenecks.Count -ne 8 -or
    $app3Module03Subgroups.Count -ne 6 -or
    $app3Module03Gates.Count -ne 18 -or
    @($app3Module03Gates | Where-Object { $_.status -ne 'pass' }).Count -ne 0 -or
    $app3Module03Score.Count -ne 6 -or
    [int]($app3Module03Score | Where-Object { $_.criterion_id -eq 'TOTAL' }).points_awarded -ne 20
) {
    throw 'APP-3 Module 03 specification, frozen handoff, diagnostic outputs, assessment, progression, or responsible-claim boundary does not match the 0.1.0 contract.'
}
& python (Join-Path $app3Module03Root 'freeze_upstream.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 03 upstream self-check failed.' }
& python (Join-Path $app3Module03Root 'build_diagnostic.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 03 diagnostic self-check failed.' }
& python (Join-Path $app3Module03Root 'build_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 03 workspace-builder self-check failed.' }
& python (Join-Path $app3Module03Root 'validate_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 03 validator self-check failed.' }

$app3Checkpoint01Root = Join-Path $repo 'courses\clinical-performance-improvement\checkpoints\01-measures-variation-readiness'
$app3Checkpoint01Spec = Join-Path $repo 'docs\curriculum\courses\APP-3\checkpoints\01-measures-variation-readiness-spec.md'
$app3Checkpoint01Files = @(
    '.gitattributes',
    'VERSION',
    'assessment.md',
    'build_checkpoint.py',
    'checkpoint-contract.json',
    'instructor-notes.md',
    'release.json',
    'validate_checkpoint.py',
    'reference\README.md',
    'reference\evidence-index.csv',
    'reference\measures-variation-readiness-review.md',
    'reference\checkpoint-gates.csv',
    'reference\checkpoint-defense.md',
    'reference\reproducibility-check.md',
    'reference\ai-use.md',
    'reference\progression-decision.md',
    'template\README.md',
    'template\evidence-index.csv',
    'template\measures-variation-readiness-review.md',
    'template\checkpoint-gates.csv',
    'template\checkpoint-defense.md',
    'template\reproducibility-check.md',
    'template\ai-use.md',
    'template\progression-decision.md'
)
$app3Checkpoint01Missing = @($app3Checkpoint01Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $app3Checkpoint01Root $_))
})
if (-not (Test-Path -LiteralPath $app3Checkpoint01Spec) -or $app3Checkpoint01Missing.Count -gt 0) {
    throw "APP-3 Checkpoint 01 is missing its specification or package files: $($app3Checkpoint01Missing -join ', ')."
}
$app3Checkpoint01Content = Get-Content -Raw -LiteralPath $app3Checkpoint01Spec
$app3Checkpoint01Sections = [regex]::Matches($app3Checkpoint01Content, '(?m)^## \d+\.').Count
$app3Checkpoint01Release = Get-Content -Raw -LiteralPath (Join-Path $app3Checkpoint01Root 'release.json') | ConvertFrom-Json
$app3Checkpoint01Contract = Get-Content -Raw -LiteralPath (Join-Path $app3Checkpoint01Root 'checkpoint-contract.json') | ConvertFrom-Json
$app3Checkpoint01Index = @(Import-Csv -LiteralPath (Join-Path $app3Checkpoint01Root 'reference\evidence-index.csv'))
$app3Checkpoint01Gates = @(Import-Csv -LiteralPath (Join-Path $app3Checkpoint01Root 'reference\checkpoint-gates.csv'))
$app3Checkpoint01Progression = Get-Content -Raw -LiteralPath (Join-Path $app3Checkpoint01Root 'reference\progression-decision.md')
if (
    $app3Checkpoint01Sections -ne 17 -or
    $app3Checkpoint01Content -match '[—–]' -or
    $app3Checkpoint01Content -notmatch '137' -or
    $app3Checkpoint01Content -notmatch '153' -or
    $app3Checkpoint01Content -notmatch '40 of 40' -or
    $app3Checkpoint01Content -notmatch '742' -or
    $app3Checkpoint01Content -notmatch '700' -or
    $app3Checkpoint01Content -notmatch '9f4dbbf58fdef8ac0935f298de26ae04b87b8722c3be2d3b2b6e2aefbc147656' -or
    $app3Checkpoint01Release.checkpoint.id -ne 'oclc-app3-cp01' -or
    $app3Checkpoint01Release.checkpoint.version -ne '0.1.0' -or
    $app3Checkpoint01Release.checkpoint.commons_release -ne '0.69.0' -or
    $app3Checkpoint01Release.checkpoint.course_points -ne 40 -or
    $app3Checkpoint01Release.package.candidate_manifest_rows -ne 137 -or
    $app3Checkpoint01Release.package.candidate_manifest_bytes -ne 23862 -or
    $app3Checkpoint01Release.package.candidate_manifest_sha256 -ne '9f4dbbf58fdef8ac0935f298de26ae04b87b8722c3be2d3b2b6e2aefbc147656' -or
    $app3Checkpoint01Release.package.checkpoint_editable_records -ne 8 -or
    $app3Checkpoint01Release.package.defense_questions -ne 12 -or
    $app3Checkpoint01Release.package.assembled_files -ne 153 -or
    $app3Checkpoint01Release.validation.complete_reference_checks -ne 742 -or
    $app3Checkpoint01Release.validation.starter_checks -ne 700 -or
    $app3Checkpoint01Release.validation.failure_routes_rejected -ne 18 -or
    $app3Checkpoint01Release.progression.reference -ne 'continue with conditions' -or
    $app3Checkpoint01Release.progression.module04_permission -ne 'permitted for demand forecasting and capacity analysis' -or
    $app3Checkpoint01Contract.accepted_component_files -ne 137 -or
    $app3Checkpoint01Contract.course_points -ne 40 -or
    @($app3Checkpoint01Contract.accepted_modules).Count -ne 3 -or
    ($app3Checkpoint01Contract.accepted_modules | Measure-Object -Property points -Sum).Sum -ne 40 -or
    $app3Checkpoint01Index.Count -ne 3 -or
    ($app3Checkpoint01Index | Measure-Object -Property checkpoint_points -Sum).Sum -ne 40 -or
    $app3Checkpoint01Gates.Count -ne 18 -or
    @($app3Checkpoint01Gates | Where-Object { $_.status -ne 'pass' }).Count -ne 0 -or
    $app3Checkpoint01Progression -notmatch 'Module 02 20 points once plus Module 03 20 points once' -or
    $app3Checkpoint01Progression -notmatch 'permitted for demand forecasting and capacity analysis'
) {
    throw 'APP-3 Checkpoint 01 specification, frozen candidates, point accounting, gates, defense, progression, or responsible-claim boundary does not match the 0.1.0 contract.'
}
& python (Join-Path $app3Checkpoint01Root 'build_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Checkpoint 01 builder self-check failed.' }
& python (Join-Path $app3Checkpoint01Root 'validate_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Checkpoint 01 validator self-check failed.' }

$app3Module04Root = Join-Path $repo 'courses\clinical-performance-improvement\modules\04-demand-forecasting-capacity'
$app3Module04Spec = Join-Path $repo 'docs\curriculum\courses\APP-3\modules\04-demand-forecasting-capacity-spec.md'
$app3Module04RecordNames = @(
    'forecast-plan.md', 'fold-audit.csv', 'model-comparison.md',
    'failure-period-review.md', 'capacity-interpretation.md',
    'littles-law-interpretation.md', 'accessible-output-review.md',
    'gate-results.csv', 'module05-handoff.md', 'ai-use.md',
    'progression-decision.md', 'reproducibility-check.md'
)
$app3Module04Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'assessment.md',
    'build_forecast.py', 'build_workspace.py', 'data-spec.md',
    'forecast-contract.json', 'freeze_upstream.py', 'instructor-notes.md',
    'release.json', 'source-record.yml', 'validate_workspace.py',
    'verify_forecast.R', 'upstream\checkpoint-handoff-manifest.csv',
    'upstream\shift-metrics.csv', 'outputs\folds.csv',
    'outputs\forecast-predictions.csv', 'outputs\error-summary.csv',
    'outputs\error-slices.csv', 'outputs\week53-forecast.csv',
    'outputs\capacity-implication.csv', 'outputs\littles-law-check.csv',
    'outputs\forecast-findings.json', 'outputs\forecast-error-comparison.svg',
    'outputs\week53-demand-forecast.svg'
) + @($app3Module04RecordNames | ForEach-Object { "reference\$_" }) + @($app3Module04RecordNames | ForEach-Object { "template\$_" })
$app3Module04Missing = @($app3Module04Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $app3Module04Root $_))
})
if (-not (Test-Path -LiteralPath $app3Module04Spec) -or $app3Module04Missing.Count -gt 0) {
    throw "APP-3 Module 04 is missing its specification or package files: $($app3Module04Missing -join ', ')."
}
$app3Module04Content = Get-Content -Raw -LiteralPath $app3Module04Spec
$app3Module04Sections = [regex]::Matches($app3Module04Content, '(?m)^## \d+\.').Count
$app3Module04Release = Get-Content -Raw -LiteralPath (Join-Path $app3Module04Root 'release.json') | ConvertFrom-Json
$app3Module04Contract = Get-Content -Raw -LiteralPath (Join-Path $app3Module04Root 'forecast-contract.json') | ConvertFrom-Json
$app3Module04Findings = Get-Content -Raw -LiteralPath (Join-Path $app3Module04Root 'outputs\forecast-findings.json') | ConvertFrom-Json
$app3Module04Folds = @(Import-Csv -LiteralPath (Join-Path $app3Module04Root 'outputs\folds.csv'))
$app3Module04Predictions = @(Import-Csv -LiteralPath (Join-Path $app3Module04Root 'outputs\forecast-predictions.csv'))
$app3Module04Errors = @(Import-Csv -LiteralPath (Join-Path $app3Module04Root 'outputs\error-summary.csv'))
$app3Module04Slices = @(Import-Csv -LiteralPath (Join-Path $app3Module04Root 'outputs\error-slices.csv'))
$app3Module04Week53 = @(Import-Csv -LiteralPath (Join-Path $app3Module04Root 'outputs\week53-forecast.csv'))
$app3Module04Capacity = @(Import-Csv -LiteralPath (Join-Path $app3Module04Root 'outputs\capacity-implication.csv'))
$app3Module04Little = @(Import-Csv -LiteralPath (Join-Path $app3Module04Root 'outputs\littles-law-check.csv'))
$app3Module04Gates = @(Import-Csv -LiteralPath (Join-Path $app3Module04Root 'reference\gate-results.csv'))
$app3Module04Selected = $app3Module04Errors | Where-Object { $_.selected_flag -eq '1' }
if (
    $app3Module04Sections -ne 21 -or
    $app3Module04Content -match '[—–]' -or
    $app3Module04Content -notmatch 'Student effort: 16\.5 hours' -or
    $app3Module04Content -notmatch '5\.937283' -or
    $app3Module04Content -notmatch '876\.924084' -or
    $app3Module04Content -notmatch '805\.136639' -or
    $app3Module04Content -notmatch '970\.733035' -or
    $app3Module04Content -notmatch '255 checks' -or
    $app3Module04Content -notmatch '151 checks' -or
    $app3Module04Content -notmatch '19 rejected' -or
    $app3Module04Release.module_id -ne 'oclc-app3-04' -or
    $app3Module04Release.module_version -ne '0.1.0' -or
    $app3Module04Release.commons_release -ne '0.70.0' -or
    $app3Module04Release.reference_score -ne 0 -or
    $app3Module04Release.reference_gates_passed -ne 18 -or
    $app3Module04Release.reference_progression -ne 'continue with conditions' -or
    $app3Module04Release.selected_method -ne 'seasonal_exponential_smoothing' -or
    $app3Module04Release.outputs.files -ne 10 -or
    $app3Module04Release.outputs.folds -ne 28 -or
    $app3Module04Release.outputs.prediction_rows -ne 1764 -or
    $app3Module04Release.workspace.learner_files -ne 49 -or
    $app3Module04Release.workspace.learner_manifest_rows -ne 36 -or
    $app3Module04Release.workspace.reference_files -ne 59 -or
    $app3Module04Release.workspace.reference_manifest_rows -ne 46 -or
    $app3Module04Release.workspace.learner_records -ne 12 -or
    $app3Module04Release.validation.complete_checks -ne 255 -or
    $app3Module04Release.validation.starter_checks -ne 151 -or
    $app3Module04Release.validation.failure_routes_rejected -ne 19 -or
    $app3Module04Release.module05_permission -ne 'permitted for improvement scenario and evaluation construction' -or
    $app3Module04Release.staffing_recommendation_authorized -ne $false -or
    $app3Module04Release.base_r_verification -notmatch 'pending before alpha' -or
    $app3Module04Contract.module.hours -ne 16.5 -or
    $app3Module04Contract.module.course_points -ne 0 -or
    $app3Module04Contract.upstream.candidate_files -ne 137 -or
    $app3Module04Contract.upstream.frozen_files -ne 23 -or
    $app3Module04Contract.forecast.rolling_folds -ne 28 -or
    $app3Module04Contract.forecast.evaluation_rows_per_method -ne 588 -or
    $app3Module04Contract.forecast.horizon_shifts -ne 21 -or
    $app3Module04Contract.forecast.seasonal_period_shifts -ne 21 -or
    $app3Module04Contract.forecast.alpha -ne 0.3 -or
    $app3Module04Contract.forecast.gamma -ne 0.2 -or
    $app3Module04Contract.assessment.noncompensable_gates -ne 18 -or
    $app3Module04Findings.selected_method -ne 'seasonal_exponential_smoothing' -or
    $app3Module04Findings.method_metrics.seasonal_exponential_smoothing.mae -ne 5.937283 -or
    $app3Module04Findings.week53.raw_forecast_arrivals -ne 876.924084 -or
    $app3Module04Findings.week53.empirical_actual_equivalent_lower -ne 805.136639 -or
    $app3Module04Findings.week53.empirical_actual_equivalent_upper -ne 970.733035 -or
    $app3Module04Findings.capacity.staffing_recommendation -ne 'not authorized' -or
    $app3Module04Findings.littles_law.equilibrium_status -ne 'not established' -or
    $app3Module04Folds.Count -ne 28 -or
    $app3Module04Predictions.Count -ne 1764 -or
    $app3Module04Errors.Count -ne 3 -or
    $app3Module04Slices.Count -ne 17 -or
    $app3Module04Week53.Count -ne 21 -or
    $app3Module04Capacity.Count -ne 13 -or
    $app3Module04Little.Count -ne 4 -or
    @($app3Module04Selected).Count -ne 1 -or
    $app3Module04Selected.method -ne 'seasonal_exponential_smoothing' -or
    [decimal]$app3Module04Selected.mae_arrivals -ne [decimal]5.937283 -or
    $app3Module04Gates.Count -ne 18 -or
    @($app3Module04Gates | Where-Object { $_.status -ne 'pass' }).Count -ne 0
) {
    throw 'APP-3 Module 04 specification, checkpoint handoff, forecast outputs, capacity limits, assessment, progression, or responsible-claim boundary does not match the 0.1.0 contract.'
}
& python (Join-Path $app3Module04Root 'freeze_upstream.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 04 upstream self-check failed.' }
& python (Join-Path $app3Module04Root 'build_forecast.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 04 forecast self-check failed.' }
& python (Join-Path $app3Module04Root 'build_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 04 workspace-builder self-check failed.' }
& python (Join-Path $app3Module04Root 'validate_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 04 validator self-check failed.' }

$app3Module05Root = Join-Path $repo 'courses\clinical-performance-improvement\modules\05-improvement-scenarios-evaluation'
$app3Module05Spec = Join-Path $repo 'docs\curriculum\courses\APP-3\modules\05-improvement-scenarios-evaluation-spec.md'
$app3Module05RecordNames = @(
    'scenario-assumption-register.csv', 'scenario-validation.md',
    'scenario-comparison.md', 'sensitivity-interpretation.md',
    'access-workforce-safety-review.md', 'evaluation-design.md',
    'evaluation-threat-audit.csv', 'gaming-unintended-effects.md',
    'week6-score.csv', 'gate-results.csv', 'module06-handoff.md',
    'ai-use.md', 'progression-decision.md', 'reproducibility-check.md'
)
$app3Module05Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'assessment.md',
    'build_scenarios.py', 'build_workspace.py', 'data-spec.md',
    'scenario-contract.json', 'freeze_upstream.py', 'instructor-notes.md',
    'release.json', 'source-record.yml', 'validate_workspace.py',
    'upstream\module05-handoff-manifest.csv', 'outputs\input-profile.csv',
    'outputs\condition-register.csv', 'outputs\validation-checks.csv',
    'outputs\replication-results.csv', 'outputs\scenario-summary.csv',
    'outputs\paired-effects.csv', 'outputs\sensitivity-review.csv',
    'outputs\evaluation-measures.csv', 'outputs\evaluation-threats.csv',
    'outputs\scenario-findings.json', 'outputs\point-demand-tradeoffs.svg',
    'outputs\sensitivity-wait-effects.svg'
) + @($app3Module05RecordNames | ForEach-Object { "reference\$_" }) + @($app3Module05RecordNames | ForEach-Object { "template\$_" })
$app3Module05Missing = @($app3Module05Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $app3Module05Root $_))
})
if (-not (Test-Path -LiteralPath $app3Module05Spec) -or $app3Module05Missing.Count -gt 0) {
    throw "APP-3 Module 05 is missing its specification or package files: $($app3Module05Missing -join ', ')."
}
$app3Module05Content = Get-Content -Raw -LiteralPath $app3Module05Spec
$app3Module05Sections = [regex]::Matches($app3Module05Content, '(?m)^## \d+\.').Count
$app3Module05Release = Get-Content -Raw -LiteralPath (Join-Path $app3Module05Root 'release.json') | ConvertFrom-Json
$app3Module05Contract = Get-Content -Raw -LiteralPath (Join-Path $app3Module05Root 'scenario-contract.json') | ConvertFrom-Json
$app3Module05Findings = Get-Content -Raw -LiteralPath (Join-Path $app3Module05Root 'outputs\scenario-findings.json') | ConvertFrom-Json
$app3Module05Profiles = @(Import-Csv -LiteralPath (Join-Path $app3Module05Root 'outputs\input-profile.csv'))
$app3Module05Conditions = @(Import-Csv -LiteralPath (Join-Path $app3Module05Root 'outputs\condition-register.csv'))
$app3Module05Validations = @(Import-Csv -LiteralPath (Join-Path $app3Module05Root 'outputs\validation-checks.csv'))
$app3Module05Replications = @(Import-Csv -LiteralPath (Join-Path $app3Module05Root 'outputs\replication-results.csv'))
$app3Module05Summaries = @(Import-Csv -LiteralPath (Join-Path $app3Module05Root 'outputs\scenario-summary.csv'))
$app3Module05Paired = @(Import-Csv -LiteralPath (Join-Path $app3Module05Root 'outputs\paired-effects.csv'))
$app3Module05Sensitivity = @(Import-Csv -LiteralPath (Join-Path $app3Module05Root 'outputs\sensitivity-review.csv'))
$app3Module05Measures = @(Import-Csv -LiteralPath (Join-Path $app3Module05Root 'outputs\evaluation-measures.csv'))
$app3Module05Threats = @(Import-Csv -LiteralPath (Join-Path $app3Module05Root 'outputs\evaluation-threats.csv'))
$app3Module05Gates = @(Import-Csv -LiteralPath (Join-Path $app3Module05Root 'reference\gate-results.csv'))
$app3Module05Score = @(Import-Csv -LiteralPath (Join-Path $app3Module05Root 'reference\week6-score.csv'))
$app3Module05Failed = @($app3Module05Sensitivity | Where-Object { $_.effect_status -eq 'null or failed improvement' })
if (
    $app3Module05Sections -ne 21 -or
    $app3Module05Content -match '[—–]' -or
    $app3Module05Content -notmatch 'Student effort: 16\.0 hours' -or
    $app3Module05Content -notmatch '4,000' -or
    $app3Module05Content -notmatch '60\.035963' -or
    $app3Module05Content -notmatch '21\.244986' -or
    $app3Module05Content -notmatch '86\.671644' -or
    $app3Module05Content -notmatch '271 checks' -or
    $app3Module05Content -notmatch '166 structural checks' -or
    $app3Module05Content -notmatch '12 failure routes' -or
    $app3Module05Release.module_id -ne 'oclc-app3-05' -or
    $app3Module05Release.module_version -ne '0.1.0' -or
    $app3Module05Release.commons_release -ne '0.71.0' -or
    $app3Module05Release.reference_score -ne 25 -or
    $app3Module05Release.reference_gates_passed -ne 20 -or
    $app3Module05Release.reference_progression -ne 'continue with conditions' -or
    $app3Module05Release.selected_option -ne 'none' -or
    $app3Module05Release.outputs.files -ne 12 -or
    $app3Module05Release.outputs.replication_rows -ne 4000 -or
    $app3Module05Release.outputs.summary_rows -ne 20 -or
    $app3Module05Release.outputs.paired_effect_rows -ne 15 -or
    $app3Module05Release.workspace.learner_files -ne 56 -or
    $app3Module05Release.workspace.learner_manifest_rows -ne 41 -or
    $app3Module05Release.workspace.reference_files -ne 68 -or
    $app3Module05Release.workspace.reference_manifest_rows -ne 53 -or
    $app3Module05Release.workspace.learner_records -ne 14 -or
    $app3Module05Release.validation.complete_checks -ne 271 -or
    $app3Module05Release.validation.starter_checks -ne 166 -or
    $app3Module05Release.validation.failure_routes_rejected -ne 12 -or
    $app3Module05Release.implementation_authorized -ne $false -or
    $app3Module05Contract.module.hours -ne 16.0 -or
    $app3Module05Contract.module.course_points -ne 25 -or
    $app3Module05Contract.simulation.warmup_days -ne 7 -or
    $app3Module05Contract.simulation.measurement_days -ne 7 -or
    $app3Module05Contract.simulation.replications_per_scenario_condition -ne 200 -or
    $app3Module05Contract.simulation.base_seed -ne 7300500 -or
    $app3Module05Contract.simulation.base_clinician_slots.night -ne 2 -or
    $app3Module05Contract.simulation.base_clinician_slots.day -ne 6 -or
    $app3Module05Contract.simulation.base_clinician_slots.evening -ne 4 -or
    $app3Module05Contract.assessment.noncompensable_gates -ne 20 -or
    $app3Module05Findings.selection.selected_option -ne 'none' -or
    $app3Module05Findings.sensitivity.null_or_failed_rows -ne 6 -or
    $app3Module05Findings.point_demand.S00.median_wait_minutes -ne 60.035963 -or
    $app3Module05Findings.point_paired_effects.S01.p90_wait_improvement_minutes -ne 21.244986 -or
    $app3Module05Findings.point_paired_effects.S02.median_wait_improvement_minutes -ne -5.803341 -or
    $app3Module05Findings.evaluation.causal_status -ne 'not established by simulation' -or
    $app3Module05Profiles.Count -ne 45 -or
    $app3Module05Conditions.Count -ne 5 -or
    $app3Module05Validations.Count -ne 24 -or
    @($app3Module05Validations | Where-Object { $_.status -ne 'pass' }).Count -ne 0 -or
    $app3Module05Replications.Count -ne 4000 -or
    $app3Module05Summaries.Count -ne 20 -or
    $app3Module05Paired.Count -ne 15 -or
    $app3Module05Sensitivity.Count -ne 15 -or
    $app3Module05Failed.Count -ne 6 -or
    $app3Module05Measures.Count -ne 12 -or
    $app3Module05Threats.Count -ne 8 -or
    $app3Module05Gates.Count -ne 20 -or
    @($app3Module05Gates | Where-Object { $_.status -ne 'pass' }).Count -ne 0 -or
    $app3Module05Score.Count -ne 7 -or
    [decimal]$app3Module05Score[-1].points_awarded -ne [decimal]25
) {
    throw 'APP-3 Module 05 specification, scenario outputs, sensitivity, evaluation, assessment, progression, or responsible-claim boundary does not match the 0.1.0 contract.'
}
& python (Join-Path $app3Module05Root 'freeze_upstream.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 05 upstream self-check failed.' }
& python (Join-Path $app3Module05Root 'build_scenarios.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 05 scenario self-check failed.' }
& python (Join-Path $app3Module05Root 'build_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 05 workspace-builder self-check failed.' }
& python (Join-Path $app3Module05Root 'validate_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 05 validator self-check failed.' }

$app3Module06Root = Join-Path $repo 'courses\clinical-performance-improvement\modules\06-feasibility-monitoring-embedded-ml'
$app3Module06Spec = Join-Path $repo 'docs\curriculum\courses\APP-3\modules\06-feasibility-monitoring-embedded-ml-spec.md'
$app3Module06RecordNames = @(
    'feasibility-review.md', 'quality-safety-review.md',
    'access-equity-review.md', 'workforce-review.md', 'dashboard-review.md',
    'escalation-fallback-review.md', 'monitoring-stewardship.md',
    'accountability-map.csv', 'ml-contract-review.md', 'model-comparison.md',
    'failure-review.md', 'week6-score.csv', 'gate-results.csv',
    'module07-handoff.md', 'ai-use.md', 'progression-decision.md',
    'reproducibility-check.md'
)
$app3Module06OutputNames = @(
    'upstream-inventory.csv', 'feasibility-screen.csv', 'monitoring-measures.csv',
    'escalation-fallback.csv', 'dashboard-data.csv', 'ml-split-registry.csv',
    'ml-predictions.csv', 'model-performance.csv', 'fold-comparison.csv',
    'model-error-slices.csv', 'feature-importance.csv', 'failure-cases.csv',
    'leakage-tests.csv', 'week53-model-comparison.csv', 'decision-change.csv',
    'invariant-checks.csv', 'build-report.json', 'forecast-comparison.svg',
    'monitoring-dashboard.html'
)
$app3Module06Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'assessment.md',
    'build_evidence.py', 'build_workspace.py', 'data-spec.md',
    'ml-contract.json', 'freeze_upstream.py', 'instructor-notes.md',
    'release.json', 'source-record.yml', 'validate_workspace.py',
    'upstream\module06-handoff-manifest.csv'
) + @($app3Module06OutputNames | ForEach-Object { "outputs\$_" }) + @($app3Module06RecordNames | ForEach-Object { "reference\$_" }) + @($app3Module06RecordNames | ForEach-Object { "template\$_" })
$app3Module06Missing = @($app3Module06Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $app3Module06Root $_))
})
if (-not (Test-Path -LiteralPath $app3Module06Spec) -or $app3Module06Missing.Count -gt 0) {
    throw "APP-3 Module 06 is missing its specification or package files: $($app3Module06Missing -join ', ')."
}
$app3Module06Content = Get-Content -Raw -LiteralPath $app3Module06Spec
$app3Module06Sections = [regex]::Matches($app3Module06Content, '(?m)^## \d+\.').Count
$app3Module06Release = Get-Content -Raw -LiteralPath (Join-Path $app3Module06Root 'release.json') | ConvertFrom-Json
$app3Module06Contract = Get-Content -Raw -LiteralPath (Join-Path $app3Module06Root 'ml-contract.json') | ConvertFrom-Json
$app3Module06Report = Get-Content -Raw -LiteralPath (Join-Path $app3Module06Root 'outputs\build-report.json') | ConvertFrom-Json
$app3Module06Inventory = @(Import-Csv -LiteralPath (Join-Path $app3Module06Root 'outputs\upstream-inventory.csv'))
$app3Module06Feasibility = @(Import-Csv -LiteralPath (Join-Path $app3Module06Root 'outputs\feasibility-screen.csv'))
$app3Module06Monitoring = @(Import-Csv -LiteralPath (Join-Path $app3Module06Root 'outputs\monitoring-measures.csv'))
$app3Module06Escalation = @(Import-Csv -LiteralPath (Join-Path $app3Module06Root 'outputs\escalation-fallback.csv'))
$app3Module06Splits = @(Import-Csv -LiteralPath (Join-Path $app3Module06Root 'outputs\ml-split-registry.csv'))
$app3Module06Predictions = @(Import-Csv -LiteralPath (Join-Path $app3Module06Root 'outputs\ml-predictions.csv'))
$app3Module06Performance = @(Import-Csv -LiteralPath (Join-Path $app3Module06Root 'outputs\model-performance.csv'))
$app3Module06Folds = @(Import-Csv -LiteralPath (Join-Path $app3Module06Root 'outputs\fold-comparison.csv'))
$app3Module06Slices = @(Import-Csv -LiteralPath (Join-Path $app3Module06Root 'outputs\model-error-slices.csv'))
$app3Module06Importance = @(Import-Csv -LiteralPath (Join-Path $app3Module06Root 'outputs\feature-importance.csv'))
$app3Module06Failures = @(Import-Csv -LiteralPath (Join-Path $app3Module06Root 'outputs\failure-cases.csv'))
$app3Module06Leakage = @(Import-Csv -LiteralPath (Join-Path $app3Module06Root 'outputs\leakage-tests.csv'))
$app3Module06Week53 = @(Import-Csv -LiteralPath (Join-Path $app3Module06Root 'outputs\week53-model-comparison.csv'))
$app3Module06Decisions = @(Import-Csv -LiteralPath (Join-Path $app3Module06Root 'outputs\decision-change.csv'))
$app3Module06Invariants = @(Import-Csv -LiteralPath (Join-Path $app3Module06Root 'outputs\invariant-checks.csv'))
$app3Module06Gates = @(Import-Csv -LiteralPath (Join-Path $app3Module06Root 'reference\gate-results.csv'))
$app3Module06Score = @(Import-Csv -LiteralPath (Join-Path $app3Module06Root 'reference\week6-score.csv'))
$app3Module06Transparent = @($app3Module06Performance | Where-Object { $_.method -eq 'seasonal_exponential_smoothing' })
$app3Module06Ml = @($app3Module06Performance | Where-Object { $_.method -eq 'gradient_boosted' })
$app3Module06Difficult = @($app3Module06Folds | Where-Object { $_.difficult_fold -eq '1' })
if (
    $app3Module06Sections -ne 26 -or
    $app3Module06Content -match '[—–]' -or
    $app3Module06Content -notmatch 'Student effort: 16\.0 hours' -or
    $app3Module06Content -notmatch '0\.731788' -or
    $app3Module06Content -notmatch '0\.018212' -or
    $app3Module06Content -notmatch '860\.277096' -or
    $app3Module06Content -notmatch 'retain transparent forecast' -or
    $app3Module06Content -notmatch '354 complete checks' -or
    $app3Module06Content -notmatch '183 structural checks' -or
    $app3Module06Content -notmatch '18 failure routes' -or
    $app3Module06Release.module_id -ne 'oclc-app3-06' -or
    $app3Module06Release.module_version -ne '0.1.0' -or
    $app3Module06Release.commons_release -ne '0.72.0' -or
    $app3Module06Release.reference_score -ne 25 -or
    $app3Module06Release.points_added_here -ne 0 -or
    $app3Module06Release.reference_gates_passed -ne 22 -or
    $app3Module06Release.reference_progression -ne 'continue with conditions' -or
    $app3Module06Release.selected_option -ne 'none' -or
    $app3Module06Release.accepted_forecast -ne 'seasonal_exponential_smoothing' -or
    $app3Module06Release.ml_decision -ne 'retain transparent forecast' -or
    $app3Module06Release.outputs.files -ne 19 -or
    $app3Module06Release.outputs.feasibility_rows -ne 28 -or
    $app3Module06Release.outputs.monitoring_measures -ne 12 -or
    $app3Module06Release.outputs.prediction_rows -ne 1176 -or
    $app3Module06Release.outputs.common_evaluation_rows -ne 588 -or
    $app3Module06Release.workspace.learner_files -ne 63 -or
    $app3Module06Release.workspace.learner_manifest_rows -ne 45 -or
    $app3Module06Release.workspace.reference_files -ne 82 -or
    $app3Module06Release.workspace.reference_manifest_rows -ne 64 -or
    $app3Module06Release.workspace.learner_records -ne 17 -or
    $app3Module06Release.validation.complete_checks -ne 354 -or
    $app3Module06Release.validation.starter_checks -ne 183 -or
    $app3Module06Release.validation.failure_routes_rejected -ne 18 -or
    $app3Module06Release.implementation_authorized -ne $false -or
    $app3Module06Contract.module.hours -ne 16.0 -or
    $app3Module06Contract.module.application_hours -ne 8.0 -or
    $app3Module06Contract.module.machine_learning_hours -ne 8.0 -or
    $app3Module06Contract.module.course_points_added -ne 0 -or
    $app3Module06Contract.module.week6_points -ne 25 -or
    $app3Module06Contract.comparison.folds -ne 28 -or
    $app3Module06Contract.comparison.evaluation_rows -ne 588 -or
    $app3Module06Contract.comparison.horizon_shifts -ne 21 -or
    $app3Module06Contract.model.n_estimators -ne 100 -or
    $app3Module06Contract.model.learning_rate -ne 0.05 -or
    $app3Module06Contract.model.max_depth -ne 2 -or
    $app3Module06Contract.model.min_samples_leaf -ne 15 -or
    $app3Module06Contract.model.random_state -ne 7300600 -or
    $app3Module06Contract.model.tuning -ne 'prohibited' -or
    $app3Module06Contract.decision_rules.minimum_mae_improvement -ne 0.75 -or
    $app3Module06Contract.assessment.noncompensable_gates -ne 22 -or
    $app3Module06Report.outputs -ne 19 -or
    $app3Module06Report.feasibility_rows -ne 28 -or
    $app3Module06Report.monitoring_measures -ne 12 -or
    $app3Module06Report.rolling_folds -ne 28 -or
    $app3Module06Report.prediction_rows -ne 1176 -or
    $app3Module06Report.common_evaluation_rows -ne 588 -or
    $app3Module06Report.mae_improvement_arrivals -ne 0.731788 -or
    $app3Module06Report.week53_ml_arrivals -ne 860.277096 -or
    $app3Module06Report.decision_rules_passed -ne 7 -or
    $app3Module06Report.ml_decision -ne 'retain transparent forecast' -or
    $app3Module06Report.implementation_authorized -ne $false -or
    $app3Module06Inventory.Count -ne 33 -or
    @($app3Module06Inventory | Where-Object { $_.verification_status -ne 'pass' }).Count -ne 0 -or
    $app3Module06Feasibility.Count -ne 28 -or
    @($app3Module06Feasibility | Where-Object { $_.implementation_authorized -ne '0' }).Count -ne 0 -or
    $app3Module06Monitoring.Count -ne 12 -or
    @($app3Module06Monitoring | Where-Object { $_.value -eq 'unavailable' }).Count -ne 3 -or
    $app3Module06Escalation.Count -ne 10 -or
    @($app3Module06Escalation | Where-Object { $_.automatic_action -ne '0' }).Count -ne 0 -or
    $app3Module06Splits.Count -ne 28 -or
    $app3Module06Predictions.Count -ne 1176 -or
    @($app3Module06Predictions | Where-Object { $_.method -eq 'seasonal_exponential_smoothing' }).Count -ne 588 -or
    @($app3Module06Predictions | Where-Object { $_.method -eq 'gradient_boosted' }).Count -ne 588 -or
    $app3Module06Transparent.Count -ne 1 -or
    [decimal]$app3Module06Transparent[0].mae_arrivals -ne [decimal]5.937283 -or
    $app3Module06Transparent[0].selected_flag -ne '1' -or
    $app3Module06Ml.Count -ne 1 -or
    [decimal]$app3Module06Ml[0].mae_arrivals -ne [decimal]5.205494 -or
    $app3Module06Ml[0].selected_flag -ne '0' -or
    $app3Module06Folds.Count -ne 28 -or
    $app3Module06Difficult.Count -ne 4 -or
    @($app3Module06Difficult | Where-Object { $_.difficult_fold_rule_status -ne 'pass' }).Count -ne 0 -or
    $app3Module06Slices.Count -ne 38 -or
    $app3Module06Importance.Count -ne 30 -or
    $app3Module06Failures.Count -ne 10 -or
    $app3Module06Leakage.Count -ne 12 -or
    @($app3Module06Leakage | Where-Object { $_.status -ne 'pass' }).Count -ne 0 -or
    $app3Module06Week53.Count -ne 22 -or
    [decimal]$app3Module06Week53[-1].ml_forecast_arrivals -ne [decimal]860.277096 -or
    $app3Module06Decisions.Count -ne 9 -or
    $app3Module06Decisions[0].rule_id -ne 'R01' -or
    $app3Module06Decisions[0].status -ne 'fail' -or
    [decimal]$app3Module06Decisions[0].observed -ne [decimal]0.731788 -or
    $app3Module06Decisions[-1].decision_effect -ne 'retain transparent forecast' -or
    $app3Module06Invariants.Count -ne 20 -or
    @($app3Module06Invariants | Where-Object { $_.status -ne 'pass' }).Count -ne 0 -or
    $app3Module06Gates.Count -ne 22 -or
    @($app3Module06Gates | Where-Object { $_.status -ne 'pass' }).Count -ne 0 -or
    $app3Module06Score.Count -ne 5 -or
    [decimal]$app3Module06Score[-1].points_awarded -ne [decimal]25
) {
    throw 'APP-3 Module 06 specification, feasibility, monitoring, dashboard, ML comparison, assessment, progression, or responsible-claim boundary does not match the 0.1.0 contract.'
}
& python (Join-Path $app3Module06Root 'freeze_upstream.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 06 upstream self-check failed.' }
& python (Join-Path $app3Module06Root 'build_evidence.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 06 evidence-builder self-check failed.' }
& python (Join-Path $app3Module06Root 'build_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 06 workspace-builder self-check failed.' }
& python (Join-Path $app3Module06Root 'validate_workspace.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Module 06 validator self-check failed.' }

$app3Checkpoint02Root = Join-Path $repo 'courses\clinical-performance-improvement\checkpoints\02-forecast-scenario-monitoring-release'
$app3Checkpoint02Spec = Join-Path $repo 'docs\curriculum\courses\APP-3\checkpoints\02-forecast-scenario-monitoring-release-spec.md'
$app3Checkpoint02Files = @(
    '.gitattributes',
    'VERSION',
    'checkpoint-contract.json',
    'assessment.md',
    'instructor-notes.md',
    'build_checkpoint.py',
    'validate_checkpoint.py',
    'release.json',
    'reference\README.md',
    'reference\evidence-index.csv',
    'reference\forecast-scenario-monitoring-review.md',
    'reference\checkpoint-gates.csv',
    'reference\checkpoint-defense.md',
    'reference\reproducibility-check.md',
    'reference\ai-use.md',
    'reference\progression-decision.md',
    'reference\module07-handoff.md',
    'template\README.md',
    'template\evidence-index.csv',
    'template\forecast-scenario-monitoring-review.md',
    'template\checkpoint-gates.csv',
    'template\checkpoint-defense.md',
    'template\reproducibility-check.md',
    'template\ai-use.md',
    'template\progression-decision.md',
    'template\module07-handoff.md'
)
$app3Checkpoint02Missing = @($app3Checkpoint02Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $app3Checkpoint02Root $_))
})
if (-not (Test-Path -LiteralPath $app3Checkpoint02Spec) -or $app3Checkpoint02Missing.Count -gt 0) {
    throw "APP-3 Checkpoint 02 is missing its specification or package files: $($app3Checkpoint02Missing -join ', ')."
}
$app3Checkpoint02Content = Get-Content -Raw -LiteralPath $app3Checkpoint02Spec
$app3Checkpoint02Sections = [regex]::Matches($app3Checkpoint02Content, '(?m)^## \d+\.').Count
$app3Checkpoint02Release = Get-Content -Raw -LiteralPath (Join-Path $app3Checkpoint02Root 'release.json') | ConvertFrom-Json
$app3Checkpoint02Contract = Get-Content -Raw -LiteralPath (Join-Path $app3Checkpoint02Root 'checkpoint-contract.json') | ConvertFrom-Json
$app3Checkpoint02Index = Import-Csv -LiteralPath (Join-Path $app3Checkpoint02Root 'reference\evidence-index.csv')
$app3Checkpoint02Gates = Import-Csv -LiteralPath (Join-Path $app3Checkpoint02Root 'reference\checkpoint-gates.csv')
$app3Checkpoint02Progression = Get-Content -Raw -LiteralPath (Join-Path $app3Checkpoint02Root 'reference\progression-decision.md')
$app3Checkpoint02Handoff = Get-Content -Raw -LiteralPath (Join-Path $app3Checkpoint02Root 'reference\module07-handoff.md')
if (
    $app3Checkpoint02Sections -ne 17 -or
    $app3Checkpoint02Content -match '[—–]' -or
    $app3Checkpoint02Content -match '(?im)[A-Z]:\\Users\\' -or
    $app3Checkpoint02Content -notmatch 'Commons release: `0\.73\.0`' -or
    $app3Checkpoint02Content -notmatch '209-row `candidate-manifest\.csv`' -or
    $app3Checkpoint02Content -notmatch '36,654' -or
    $app3Checkpoint02Content -notmatch '4f2a303bc5626ea58139aa935da157f524db1d25b5a158a927ef5daec197958a' -or
    $app3Checkpoint02Content -notmatch '1,102 checks' -or
    $app3Checkpoint02Content -notmatch '1,061 checks' -or
    $app3Checkpoint02Content -notmatch '25 failure routes' -or
    $app3Checkpoint02Release.checkpoint.id -ne 'oclc-app3-cp02' -or
    $app3Checkpoint02Release.checkpoint.version -ne '0.1.0' -or
    $app3Checkpoint02Release.checkpoint.commons_release -ne '0.73.0' -or
    $app3Checkpoint02Release.checkpoint.course_points -ne 25 -or
    $app3Checkpoint02Release.package.candidate_manifest_rows -ne 209 -or
    $app3Checkpoint02Release.package.candidate_manifest_bytes -ne 36654 -or
    $app3Checkpoint02Release.package.candidate_manifest_sha256 -ne '4f2a303bc5626ea58139aa935da157f524db1d25b5a158a927ef5daec197958a' -or
    $app3Checkpoint02Release.package.assembled_files -ne 226 -or
    $app3Checkpoint02Release.validation.complete_reference_checks -ne 1102 -or
    $app3Checkpoint02Release.validation.starter_checks -ne 1061 -or
    $app3Checkpoint02Release.validation.failure_routes_rejected -ne 25 -or
    $app3Checkpoint02Contract.checkpoint_id -ne 'oclc-app3-cp02' -or
    $app3Checkpoint02Contract.accepted_component_files -ne 209 -or
    @($app3Checkpoint02Contract.accepted_modules).Count -ne 3 -or
    [decimal]($app3Checkpoint02Contract.accepted_modules | Measure-Object -Property points -Sum).Sum -ne [decimal]25 -or
    $app3Checkpoint02Contract.required_gates.module04_forecast -ne 18 -or
    $app3Checkpoint02Contract.required_gates.module05_scenario_evaluation -ne 20 -or
    $app3Checkpoint02Contract.required_gates.module06_feasibility_monitoring_ml -ne 22 -or
    $app3Checkpoint02Contract.required_gates.checkpoint_integrity -ne 20 -or
    $app3Checkpoint02Index.Count -ne 3 -or
    [decimal]($app3Checkpoint02Index | Measure-Object -Property checkpoint_points -Sum).Sum -ne [decimal]25 -or
    @($app3Checkpoint02Index | Where-Object { $_.gates -notmatch '^(18|20|22) of \1 pass$' }).Count -ne 0 -or
    $app3Checkpoint02Gates.Count -ne 20 -or
    @($app3Checkpoint02Gates | Where-Object { $_.status -ne 'pass' }).Count -ne 0 -or
    $app3Checkpoint02Progression -notmatch 'Module 05 25 points once' -or
    $app3Checkpoint02Progression -notmatch 'continue with conditions' -or
    $app3Checkpoint02Progression -notmatch 'retain transparent forecast' -or
    $app3Checkpoint02Progression -notmatch 'Implementation: `prohibited`' -or
    $app3Checkpoint02Handoff -notmatch 'Joe Joseph, MD' -or
    $app3Checkpoint02Handoff -notmatch 'Selected scenario: `none`' -or
    $app3Checkpoint02Handoff -notmatch '0\.731788 versus required 0\.750000'
) {
    throw 'APP-3 Checkpoint 02 specification, candidate identity, point accounting, gates, progression, or leadership handoff does not match the 0.1.0 contract.'
}
& python (Join-Path $app3Checkpoint02Root 'build_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Checkpoint 02 builder self-check failed.' }
& python (Join-Path $app3Checkpoint02Root 'validate_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'APP-3 Checkpoint 02 validator self-check failed.' }

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

$fnd1Module06Root = Join-Path $repo 'courses\healthcare-data-foundations\modules\06-accessible-charts-time-data'
$fnd1Module06Spec = Join-Path $repo 'docs\curriculum\courses\FND-1\modules\06-accessible-charts-time-data-spec.md'
$fnd1Module06Files = @(
    '.gitattributes', '.gitignore', 'README.md', 'VERSION', 'accessibility-check.md',
    'ai-use.md', 'assessment.md', 'figure-registry.csv', 'figure-spec.md',
    'instructor-notes.md', 'release.json', 'render-report.json', 'render_figures.py',
    'reproducibility-check.md', 'source-record.yml', 'transformation-record.md',
    'validate_figures.py', 'data\missingness-profile.csv', 'data\rates.csv',
    'data\denominator-registry.csv', 'data\resolved-analytic-table.csv',
    'tables\quality-missingness.csv', 'tables\descriptive-rates.csv',
    'tables\quarterly-index-counts.csv', 'figures\quality-missingness.png',
    'figures\quality-missingness.svg', 'figures\descriptive-rates.png',
    'figures\descriptive-rates.svg', 'figures\quarterly-index-counts.png',
    'figures\quarterly-index-counts.svg', 'alt-text\quality-missingness.md',
    'alt-text\descriptive-rates.md', 'alt-text\quarterly-index-counts.md',
    'learner-template\VERSION', 'learner-template\README.md',
    'learner-template\source-record.yml', 'learner-template\figure-spec.md',
    'learner-template\accessibility-check.md', 'learner-template\transformation-record.md',
    'learner-template\reproducibility-check.md', 'learner-template\ai-use.md'
)
$fnd1Module06Missing = @($fnd1Module06Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $fnd1Module06Root $_))
})
if (-not (Test-Path -LiteralPath $fnd1Module06Spec) -or $fnd1Module06Missing.Count -gt 0) {
    throw "FND-1 Module 06 is missing its specification or package files: $($fnd1Module06Missing -join ', ')."
}
$fnd1Module06Content = Get-Content -Raw -LiteralPath $fnd1Module06Spec
$fnd1Module06Sections = [regex]::Matches($fnd1Module06Content, '(?m)^## \d+\.').Count
$fnd1Module06Release = Get-Content -Raw -LiteralPath (Join-Path $fnd1Module06Root 'release.json') | ConvertFrom-Json
$fnd1Module06Quality = Import-Csv -LiteralPath (Join-Path $fnd1Module06Root 'tables\quality-missingness.csv')
$fnd1Module06Rates = Import-Csv -LiteralPath (Join-Path $fnd1Module06Root 'tables\descriptive-rates.csv')
$fnd1Module06Quarters = Import-Csv -LiteralPath (Join-Path $fnd1Module06Root 'tables\quarterly-index-counts.csv')
$fnd1Module06Registry = Import-Csv -LiteralPath (Join-Path $fnd1Module06Root 'figure-registry.csv')
if (
    $fnd1Module06Sections -ne 21 -or
    $fnd1Module06Content -match '[—–]' -or
    $fnd1Module06Content -match '(?im)[A-Z]:\\Users\\' -or
    $fnd1Module06Release.module.version -ne '0.1.0' -or
    $fnd1Module06Release.module.commons_release -ne '0.34.0' -or
    $fnd1Module06Release.module.hours -ne 16 -or
    $fnd1Module06Release.module.checkpoint_component_weight_percent -ne 20 -or
    $fnd1Module06Release.package.release_validation_checks -ne 616 -or
    $fnd1Module06Release.package.complete_submission_checks -ne 615 -or
    $fnd1Module06Quality.Count -ne 8 -or
    $fnd1Module06Rates.Count -ne 6 -or
    $fnd1Module06Quarters.Count -ne 20 -or
    $fnd1Module06Registry.Count -ne 3 -or
    @($fnd1Module06Registry[0].PSObject.Properties).Count -ne 25 -or
    (($fnd1Module06Quarters | Measure-Object -Property total_index_n -Sum).Sum) -ne 374 -or
    (($fnd1Module06Quarters | Measure-Object -Property emergency_index_n -Sum).Sum) -ne 314 -or
    (($fnd1Module06Quarters | Measure-Object -Property inpatient_index_n -Sum).Sum) -ne 60 -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $fnd1Module06Root 'tables\quality-missingness.csv')).Hash.ToLowerInvariant() -ne '52e6960cda5d4981a647683ea202e47a1a1ad5afde0e91fb8900adf0b0521134' -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $fnd1Module06Root 'tables\quarterly-index-counts.csv')).Hash.ToLowerInvariant() -ne '0f5e2f8d9b163ad4b68a8f73505fdd4b34f44936eec4fb0c88c3853f58d86fb6' -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $fnd1Module06Root 'figure-registry.csv')).Hash.ToLowerInvariant() -ne '5cdd846d9318d6dc8c2f3da41a6be6ce172b7c91d6465dc085e9f3790732d62b'
) {
    throw 'FND-1 Module 06 release metadata, specification, output counts, or fingerprints do not match the 0.1.0 contract.'
}
& python (Join-Path $fnd1Module06Root 'render_figures.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 Module 06 renderer self-check failed.' }
& python (Join-Path $fnd1Module06Root 'validate_figures.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 Module 06 validator self-check failed.' }

$fnd1Module07Root = Join-Path $repo 'courses\healthcare-data-foundations\modules\07-reproducible-handoff-ai-audit'
$fnd1Module07Spec = Join-Path $repo 'docs\curriculum\courses\FND-1\modules\07-reproducible-handoff-ai-audit-spec.md'
$fnd1Module07RecordFiles = @(
    '.gitattributes', 'README.md', 'CHANGELOG.md', 'release-notes.md',
    'component-score.csv', 'release-checklist.md', 'reproducibility-check.md',
    'review-disposition.md', 'documentation\data-brief.md', 'documentation\limitations.md',
    'documentation\ai-audit.md', 'audit\prompt-log.csv', 'defense\handoff-brief.md',
    'defense\questions-and-responses.md'
)
$fnd1Module07Files = @(
    '.gitattributes', '.gitignore', 'VERSION', 'README.md', 'pipeline-contract.csv',
    'assemble_toolkit.py', 'validate_toolkit.py', 'assessment.md', 'instructor-notes.md', 'release.json'
) + @($fnd1Module07RecordFiles | ForEach-Object { "template\$_" }) + @($fnd1Module07RecordFiles | ForEach-Object { "reference\$_" })
$fnd1Module07Missing = @($fnd1Module07Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $fnd1Module07Root $_))
})
if (-not (Test-Path -LiteralPath $fnd1Module07Spec) -or $fnd1Module07Missing.Count -gt 0) {
    throw "FND-1 Module 07 is missing its specification or package files: $($fnd1Module07Missing -join ', ')."
}
$fnd1Module07Content = Get-Content -Raw -LiteralPath $fnd1Module07Spec
$fnd1Module07Sections = [regex]::Matches($fnd1Module07Content, '(?m)^## \d+\.').Count
$fnd1Module07Release = Get-Content -Raw -LiteralPath (Join-Path $fnd1Module07Root 'release.json') | ConvertFrom-Json
$fnd1Module07ContractPath = Join-Path $fnd1Module07Root 'pipeline-contract.csv'
$fnd1Module07Contract = Import-Csv -LiteralPath $fnd1Module07ContractPath
$fnd1Module07Scores = Import-Csv -LiteralPath (Join-Path $fnd1Module07Root 'reference\component-score.csv')
if (
    $fnd1Module07Sections -ne 21 -or
    $fnd1Module07Content -match '[—–]' -or
    $fnd1Module07Content -match '(?im)[A-Z]:\\Users\\' -or
    $fnd1Module07Release.module.version -ne '0.1.0' -or
    $fnd1Module07Release.module.commons_release -ne '0.36.0' -or
    $fnd1Module07Release.module.hours -ne 16 -or
    $fnd1Module07Release.module.cumulative_hours -ne 112.5 -or
    $fnd1Module07Release.module.final_component_points -ne 35 -or
    $fnd1Module07Release.pipeline_contract.rows -ne 23 -or
    $fnd1Module07Release.package.assembled_files -ne 90 -or
    $fnd1Module07Release.package.immutable_manifest_rows -ne 74 -or
    $fnd1Module07Release.package.manifest_sha256 -ne '804d454dcdf43d0f625c90130b9bd5c698b51451ddcc1fd0910ca52e1bbd9111' -or
    $fnd1Module07Release.validation.starter_checks -ne 585 -or
    $fnd1Module07Release.validation.complete_reference_checks -ne 657 -or
    $fnd1Module07Contract.Count -ne 23 -or
    @($fnd1Module07Contract | Where-Object { $_.source_unit -eq 'M02' }).Count -ne 13 -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath $fnd1Module07ContractPath).Hash.ToLowerInvariant() -ne 'd61f208046663b80f8a591be66cc4f22fecbf0c5be7803786f75fd74cdd1d783' -or
    ($fnd1Module07Scores | Measure-Object -Property course_points -Sum).Sum -ne 35 -or
    ($fnd1Module07Scores | Measure-Object -Property score -Sum).Sum -ne 35
) {
    throw 'FND-1 Module 07 release metadata, specification, pipeline contract, score, or validation facts do not match the 0.1.0 contract.'
}
& python (Join-Path $fnd1Module07Root 'assemble_toolkit.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 Module 07 assembler self-check failed.' }
& python (Join-Path $fnd1Module07Root 'validate_toolkit.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 Module 07 validator self-check failed.' }

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

$fnd1Checkpoint02Root = Join-Path $repo 'courses\healthcare-data-foundations\checkpoints\02-quality-descriptive-accessible-release'
$fnd1Checkpoint02Spec = Join-Path $repo 'docs\curriculum\courses\FND-1\checkpoints\02-quality-descriptive-accessible-release-spec.md'
$fnd1Checkpoint02Files = @(
    '.gitattributes', 'README.md', 'VERSION', 'artifact-contract.csv', 'assessment.md',
    'assemble_checkpoint.py', 'instructor-notes.md', 'release.json', 'validate_checkpoint.py',
    'template\.gitattributes', 'template\README.md', 'template\component-score.csv',
    'template\quality-decision.md', 'template\interpretation-memo.md',
    'template\accessibility-synthesis.md', 'template\source-record.yml',
    'template\transformation-record.md', 'template\reproducibility-check.md',
    'template\ai-use.md', 'template\review-disposition.md',
    'reference\.gitattributes', 'reference\README.md', 'reference\component-score.csv',
    'reference\quality-decision.md', 'reference\interpretation-memo.md',
    'reference\accessibility-synthesis.md', 'reference\source-record.yml',
    'reference\transformation-record.md', 'reference\reproducibility-check.md',
    'reference\ai-use.md', 'reference\review-disposition.md'
)
$fnd1Checkpoint02Missing = @($fnd1Checkpoint02Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $fnd1Checkpoint02Root $_))
})
if (-not (Test-Path -LiteralPath $fnd1Checkpoint02Spec) -or $fnd1Checkpoint02Missing.Count -gt 0) {
    throw "FND-1 Checkpoint 2 is missing its specification or package files: $($fnd1Checkpoint02Missing -join ', ')."
}
$fnd1Checkpoint02Content = Get-Content -Raw -LiteralPath $fnd1Checkpoint02Spec
$fnd1Checkpoint02Sections = [regex]::Matches($fnd1Checkpoint02Content, '(?m)^## \d+\.').Count
if ($fnd1Checkpoint02Sections -ne 17 -or $fnd1Checkpoint02Content -match '[—–]' -or $fnd1Checkpoint02Content -match '(?im)[A-Z]:\\Users\\') {
    throw "FND-1 Checkpoint 2 must define 17 plain-ASCII contract sections without local absolute paths; found $fnd1Checkpoint02Sections sections."
}
$fnd1Checkpoint02Release = Get-Content -Raw -LiteralPath (Join-Path $fnd1Checkpoint02Root 'release.json') | ConvertFrom-Json
$fnd1Checkpoint02ContractPath = Join-Path $fnd1Checkpoint02Root 'artifact-contract.csv'
$fnd1Checkpoint02Contract = Import-Csv -LiteralPath $fnd1Checkpoint02ContractPath
$fnd1Checkpoint02Scores = Import-Csv -LiteralPath (Join-Path $fnd1Checkpoint02Root 'reference\component-score.csv')
if (
    $fnd1Checkpoint02Release.checkpoint.version -ne '0.1.0' -or
    $fnd1Checkpoint02Release.checkpoint.commons_release -ne '0.35.0' -or
    $fnd1Checkpoint02Release.checkpoint.course_weight_percent -ne 25 -or
    $fnd1Checkpoint02Release.checkpoint.cumulative_hours -ne 96.5 -or
    ($fnd1Checkpoint02Release.components | Measure-Object -Property course_points -Sum).Sum -ne 25 -or
    $fnd1Checkpoint02Release.package.assembled_files -ne 50 -or
    $fnd1Checkpoint02Release.package.immutable_artifacts -ne 35 -or
    $fnd1Checkpoint02Release.package.artifact_contract_sha256 -ne 'ec031d23a50628b07ce15091c90a76f03241e3f4c4a17927211b74b854754a6b' -or
    $fnd1Checkpoint02Release.package.manifest_sha256 -ne 'd7bb0e561309f4b61353f4485fe1d647d8a15c47e064f93acd816a77e512489d' -or
    $fnd1Checkpoint02Release.validation.starter_checks -ne 363 -or
    $fnd1Checkpoint02Release.validation.complete_reference_checks -ne 389 -or
    $fnd1Checkpoint02Contract.Count -ne 35 -or
    @($fnd1Checkpoint02Contract | Where-Object { $_.source_module -eq 'M04' }).Count -ne 11 -or
    @($fnd1Checkpoint02Contract | Where-Object { $_.source_module -eq 'M05' }).Count -ne 9 -or
    @($fnd1Checkpoint02Contract | Where-Object { $_.source_module -eq 'M06' }).Count -ne 15 -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath $fnd1Checkpoint02ContractPath).Hash.ToLowerInvariant() -ne 'ec031d23a50628b07ce15091c90a76f03241e3f4c4a17927211b74b854754a6b' -or
    ($fnd1Checkpoint02Scores | Measure-Object -Property course_points -Sum).Sum -ne 25 -or
    ($fnd1Checkpoint02Scores | Measure-Object -Property score -Sum).Sum -ne 25
) {
    throw 'FND-1 Checkpoint 2 release metadata, component weights, artifact contract, or validation facts do not match the 0.1.0 contract.'
}
& python (Join-Path $fnd1Checkpoint02Root 'assemble_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 Checkpoint 2 assembler self-check failed.' }
& python (Join-Path $fnd1Checkpoint02Root 'validate_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 Checkpoint 2 validator self-check failed.' }

$fnd1Checkpoint03Root = Join-Path $repo 'courses\healthcare-data-foundations\checkpoints\03-reproducible-toolkit'
$fnd1Checkpoint03Spec = Join-Path $repo 'docs\curriculum\courses\FND-1\checkpoints\03-reproducible-toolkit-spec.md'
$fnd1Checkpoint03Records = @(
    'submission-record.md', 'final-score.csv', 'gate-results.csv', 'defense-score.csv',
    'reviewer-record.md', 'final-disposition.md', 'handoff-acceptance.md', 'final-reproduction.md'
)
$fnd1Checkpoint03Files = @(
    '.gitattributes', '.gitignore', 'VERSION', 'README.md', 'assessment.md',
    'assemble_checkpoint.py', 'instructor-notes.md', 'release.json', 'validate_checkpoint.py'
) + @($fnd1Checkpoint03Records | ForEach-Object { "template\$_" }) + @($fnd1Checkpoint03Records | ForEach-Object { "reference\$_" })
$fnd1Checkpoint03Missing = @($fnd1Checkpoint03Files | Where-Object {
    -not (Test-Path -LiteralPath (Join-Path $fnd1Checkpoint03Root $_))
})
if (-not (Test-Path -LiteralPath $fnd1Checkpoint03Spec) -or $fnd1Checkpoint03Missing.Count -gt 0) {
    throw "FND-1 final checkpoint is missing its specification or package files: $($fnd1Checkpoint03Missing -join ', ')."
}
$fnd1Checkpoint03Content = Get-Content -Raw -LiteralPath $fnd1Checkpoint03Spec
$fnd1Checkpoint03Sections = [regex]::Matches($fnd1Checkpoint03Content, '(?m)^## \d+\.').Count
if ($fnd1Checkpoint03Sections -ne 17 -or $fnd1Checkpoint03Content -match '[—–]' -or $fnd1Checkpoint03Content -match '(?im)[A-Z]:\\Users\\') {
    throw "FND-1 final checkpoint must define 17 plain-ASCII contract sections without local absolute paths; found $fnd1Checkpoint03Sections sections."
}
$fnd1Checkpoint03Release = Get-Content -Raw -LiteralPath (Join-Path $fnd1Checkpoint03Root 'release.json') | ConvertFrom-Json
$fnd1Checkpoint03Scores = Import-Csv -LiteralPath (Join-Path $fnd1Checkpoint03Root 'reference\final-score.csv')
$fnd1Checkpoint03Gates = Import-Csv -LiteralPath (Join-Path $fnd1Checkpoint03Root 'reference\gate-results.csv')
$fnd1Checkpoint03Defense = Import-Csv -LiteralPath (Join-Path $fnd1Checkpoint03Root 'reference\defense-score.csv')
if (
    $fnd1Checkpoint03Release.checkpoint.version -ne '0.1.0' -or
    $fnd1Checkpoint03Release.checkpoint.commons_release -ne '0.37.0' -or
    $fnd1Checkpoint03Release.checkpoint.course_weight_percent -ne 35 -or
    $fnd1Checkpoint03Release.checkpoint.cumulative_hours -ne 112.5 -or
    $fnd1Checkpoint03Release.package.assembled_files -ne 100 -or
    $fnd1Checkpoint03Release.package.candidate_files -ne 90 -or
    $fnd1Checkpoint03Release.package.final_review_files -ne 10 -or
    $fnd1Checkpoint03Release.package.candidate_manifest_rows -ne 90 -or
    $fnd1Checkpoint03Release.package.candidate_manifest_bytes -ne 11804 -or
    $fnd1Checkpoint03Release.package.candidate_manifest_sha256 -ne '200df43e17926e29cc09aa89427a04205fd39ac289aebdf1217f952b188b89a0' -or
    $fnd1Checkpoint03Release.package.assembler_sha256 -ne '04bb5fc700dfb2a65bb486b26ad95a65f98fd4463926d76835371220d198ab07' -or
    $fnd1Checkpoint03Release.package.validator_sha256 -ne '27a347d0fb8a6f231d87f968b58c2cf689e39123760f58295645ad4d14442910' -or
    $fnd1Checkpoint03Release.validation.starter_checks -ne 404 -or
    $fnd1Checkpoint03Release.validation.complete_reference_checks -ne 493 -or
    $fnd1Checkpoint03Scores.Count -ne 8 -or
    ($fnd1Checkpoint03Scores | Measure-Object -Property points_available -Sum).Sum -ne 35 -or
    ($fnd1Checkpoint03Scores | Measure-Object -Property points_earned -Sum).Sum -ne 34 -or
    $fnd1Checkpoint03Gates.Count -ne 20 -or
    @($fnd1Checkpoint03Gates | Where-Object { $_.result -eq 'fail' }).Count -ne 0 -or
    $fnd1Checkpoint03Defense.Count -ne 5 -or
    ($fnd1Checkpoint03Defense | Measure-Object -Property points_available -Sum).Sum -ne 6 -or
    ($fnd1Checkpoint03Defense | Measure-Object -Property points_earned -Sum).Sum -ne 5.5 -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $fnd1Checkpoint03Root 'assemble_checkpoint.py')).Hash.ToLowerInvariant() -ne '04bb5fc700dfb2a65bb486b26ad95a65f98fd4463926d76835371220d198ab07' -or
    (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $fnd1Checkpoint03Root 'validate_checkpoint.py')).Hash.ToLowerInvariant() -ne '27a347d0fb8a6f231d87f968b58c2cf689e39123760f58295645ad4d14442910'
) {
    throw 'FND-1 final checkpoint release metadata, score, gates, defense, fingerprints, or validation facts do not match the 0.1.0 contract.'
}
& python (Join-Path $fnd1Checkpoint03Root 'assemble_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 final-checkpoint assembler self-check failed.' }
& python (Join-Path $fnd1Checkpoint03Root 'validate_checkpoint.py') --self-check
if ($LASTEXITCODE -ne 0) { throw 'FND-1 final-checkpoint validator self-check failed.' }

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
Write-Output "FND-1 Module 06 passed: $fnd1Module06Sections contract sections and $($fnd1Module06Files.Count) required files."
Write-Output "FND-1 Module 07 passed: $fnd1Module07Sections contract sections and $($fnd1Module07Files.Count) required files."
Write-Output "FND-1 Checkpoint 1 passed: $fnd1Checkpoint01Sections contract sections and $($fnd1Checkpoint01Files.Count) required files."
Write-Output "FND-1 Checkpoint 2 passed: $fnd1Checkpoint02Sections contract sections and $($fnd1Checkpoint02Files.Count) required files."
Write-Output "FND-1 final checkpoint passed: $fnd1Checkpoint03Sections contract sections and $($fnd1Checkpoint03Files.Count) required files."
Write-Output "FND-2 specification passed: $fnd2ModuleCount modules, $fnd2Hours hours, $fnd2CheckpointCount checkpoints."
Write-Output "FND-2 Module 01 passed: $fnd2Module01Sections contract sections and $($fnd2Module01Files.Count) required files."
Write-Output "FND-2 Module 02 passed: $fnd2Module02Sections contract sections and $($fnd2Module02Files.Count) required files."
Write-Output "FND-2 Module 03 passed: $fnd2Module03Sections contract sections and $($fnd2Module03Files.Count) required files."
Write-Output "FND-2 Module 04 passed: $fnd2Module04Sections contract sections and $($fnd2Module04Files.Count) required files."
Write-Output "FND-2 Module 05 passed: $fnd2Module05Sections contract sections and $($fnd2Module05Files.Count) required files."
Write-Output "FND-2 Module 06 passed: $fnd2Module06Sections contract sections and $($fnd2Module06Files.Count) required files."
Write-Output "FND-2 Module 07 passed: $fnd2Module07Sections contract sections and $($fnd2Module07Files.Count) required files."
Write-Output "FND-2 Checkpoint 1 passed: $fnd2Checkpoint01Sections contract sections and $($fnd2Checkpoint01Files.Count) required files."
Write-Output "FND-2 Checkpoint 2 passed: $fnd2Checkpoint02Sections contract sections and $($fnd2Checkpoint02Files.Count) required files."
Write-Output "FND-2 final checkpoint passed: $fnd2Checkpoint03Sections contract sections and $($fnd2Checkpoint03Files.Count) required files."
Write-Output "APP-1 specification passed: $app1ModuleCount modules, $app1Hours hours, and $app1CheckpointCount checkpoints."
Write-Output "APP-1 Module 01 passed: $app1Module01Sections contract sections and $($app1Module01Files.Count) required files."
Write-Output "APP-1 Module 02 passed: $app1Module02Sections contract sections and $($app1Module02Files.Count) required files."
Write-Output "APP-1 Module 03 passed: $app1Module03Sections contract sections and $($app1Module03Files.Count) required files."
Write-Output "APP-1 Checkpoint 1 passed: $app1Checkpoint01Sections contract sections and $($app1Checkpoint01Files.Count) required files."
Write-Output "APP-1 Module 04 passed: $app1Module04Sections contract sections and $($app1Module04Files.Count) required files."
Write-Output "APP-1 Module 05 passed: $app1Module05Sections contract sections and $($app1Module05Files.Count) required files."
Write-Output "APP-1 Module 06 passed: $app1Module06Sections contract sections and $($app1Module06Files.Count) required files."
Write-Output "APP-1 Checkpoint 2 passed: $app1Checkpoint02Sections contract sections and $($app1Checkpoint02Files.Count) required files."
Write-Output "APP-1 Module 07 passed: $app1Module07Sections contract sections and $($app1Module07Files.Count) required files."
Write-Output "APP-1 final checkpoint passed: $app1Checkpoint03Sections contract sections and $($app1Checkpoint03Files.Count) required files."
Write-Output "APP-2 specification passed: $app2ModuleCount modules, $app2Hours hours, and $app2CheckpointCount checkpoints."
Write-Output "APP-2 Module 01 passed: $app2Module01Sections contract sections and $($app2Module01Files.Count) required files."
Write-Output "APP-2 Module 02 passed: $app2Module02Sections contract sections and $($app2Module02Files.Count) required non-source files plus 28 verified source files."
Write-Output "APP-2 Module 03 passed: $app2Module03Sections contract sections and $($app2Module03Files.Count) required files."
Write-Output "APP-2 Module 04 passed: $app2Module04Sections contract sections and $($app2Module04Files.Count) required files."
Write-Output "APP-2 Module 05 passed: $app2Module05Sections contract sections and $($app2Module05Files.Count) required files."
Write-Output "APP-2 Module 06 passed: $app2Module06Sections contract sections and $($app2Module06Files.Count) required files."
Write-Output "APP-2 Checkpoint 01 passed: $app2Checkpoint01Sections contract sections and $($app2Checkpoint01Files.Count) required files."
Write-Output "APP-2 Checkpoint 02 passed: $app2Checkpoint02Sections contract sections and $($app2Checkpoint02Files.Count) required files."
Write-Output "APP-2 Module 07 passed: $app2Module07Sections contract sections and $($app2Module07Files.Count) required files."
Write-Output "APP-2 final checkpoint passed: $app2Checkpoint03Sections contract sections and $($app2Checkpoint03Files.Count) required files."
Write-Output "APP-3 course architecture passed: $app3Sections sections, $app3ModuleCount modules, $app3Hours hours, and $app3CheckpointCount checkpoints."
Write-Output "APP-3 Module 02 passed: $app3Module02Sections contract sections and $($app3Module02Files.Count) required files."
Write-Output "APP-3 Module 03 passed: $app3Module03Sections contract sections and $($app3Module03Files.Count) required files."
Write-Output "APP-3 Checkpoint 01 passed: $app3Checkpoint01Sections contract sections and $($app3Checkpoint01Files.Count) required files."
Write-Output "APP-3 Module 04 passed: $app3Module04Sections contract sections and $($app3Module04Files.Count) required files."
Write-Output "APP-3 Module 05 passed: $app3Module05Sections contract sections and $($app3Module05Files.Count) required files."
Write-Output "APP-3 Module 06 passed: $app3Module06Sections contract sections and $($app3Module06Files.Count) required files."
Write-Output "APP-3 Checkpoint 02 passed: $app3Checkpoint02Sections contract sections and $($app3Checkpoint02Files.Count) required files."
