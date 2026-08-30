# FND-2 Module 03: Prediction workflows and evaluation

This runnable module teaches one complete prediction workflow: preserve the accepted aim and temporal split, fit preprocessing inside training only, compare a constant baseline, the Module 02 logistic model, and one bounded machine-learning model, reject a deliberately leaked model, choose and lock a threshold on validation data, and open the 75-row test split once.

## Release identity

- Module ID: `oclc-fnd2-03`
- Module version: 0.1.0
- Commons release: 0.41.0
- Source week: 3
- Learner work: 16.5 hours
- Week 3 share: 15 of 40 cumulative course points
- Data: synthetic Synthea teaching records; no real patients
- Use: education only; no clinical or deployment claim

## Decision

The clinical prediction and model-risk reviewer decides whether the locked workflow beats its simple baseline and has credible enough evidence to enter validity review. Allowed recommendations are `continue to validity review`, `revise`, or `stop`.

The reference recommendation is `continue to validity review with conditions`. `ML01` passes the declared validation rule, but the test set contains only four outcomes. At the locked threshold, it has 2 true positives, 2 false negatives, 23 false positives, and 48 true negatives. That is teaching evidence, not deployment evidence.

## What is included

| Path | Purpose |
|---|---|
| `model-contract.json` | Frozen models, features, preprocessing, selection rule, threshold rule, seed, and use boundary. |
| `outputs/resampling-results.csv` | Five training-only stratified folds for the baseline and two eligible candidates. |
| `outputs/validation-comparison.csv` | Same-row validation evidence for all four models. |
| `outputs/model-selection-record.csv` | Mechanical application of the predeclared selection rule. |
| `outputs/threshold-table.csv` | Exact validation confusion evidence at every observed `ML01` probability. |
| `outputs/threshold-decision.csv` | The locked threshold and the rule that selected it. |
| `outputs/test-predictions.csv` | The single locked prediction for every test row. |
| `outputs/test-metrics.csv` | Baseline and selected-model point estimates with stratified bootstrap intervals. |
| `outputs/confusion-table.csv` | Exact selected-model test counts. |
| `outputs/calibration-table.csv` | Five equal-size teaching groups with exact predictions and outcomes. |
| `outputs/subgroup-metrics.csv` | Counts first, suppression flags, and bounded descriptive metrics. |
| `outputs/leaked-model-failure.csv` | Evidence that the apparently perfect leaked model is prohibited. |
| `outputs/transformed-feature-names.csv` | Fifteen columns learned by the training-only feature pipeline. |
| `outputs/calibration.svg` | Accessible calibration display backed by the exact CSV table. |
| `outputs/threshold.svg` | Accessible threshold display backed by the exact CSV table. |
| `prediction-evaluation-report.md` | Completed reference interpretation and decision. |
| `assessment.md` | Fifteen-point rubric and noncompensable gates. |
| `instructor-notes.md` | Teaching sequence, answer key, and common failures. |

The durable implementation and teaching contract is:

`docs/curriculum/courses/FND-2/modules/03-prediction-evaluation-spec.md`

## Build a learner workspace

From the repository root:

```powershell
python courses/modeling-inference-reproducible-analytics/modules/03-prediction-evaluation/build_prediction_evidence.py learner-workspace
```

The builder copies the seven fingerprinted upstream inputs, prompts, contract, code, and exact reference outputs. It refuses to overwrite an existing target.

To reproduce only the evidence from inside the copied workspace:

```powershell
python build_prediction_evidence.py reproduced-outputs --outputs-only
```

## Validate

```powershell
python courses/modeling-inference-reproducible-analytics/modules/03-prediction-evaluation/build_prediction_evidence.py --self-check
python courses/modeling-inference-reproducible-analytics/modules/03-prediction-evaluation/validate_prediction_evidence.py --self-check
```

For a completed learner package:

```powershell
python validate_prediction_evidence.py . --mode submission
```

## Hard boundary

The random forest is the selected teaching candidate because it is the only eligible candidate that meets the frozen validation rule. Selection does not mean the model is clinically useful, fair, transportable, calibrated for care, or ready to deploy. Module 04 receives these limitations as required validity-review inputs.
