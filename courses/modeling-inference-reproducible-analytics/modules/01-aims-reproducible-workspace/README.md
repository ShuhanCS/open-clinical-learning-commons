# FND-2 Module 01: Analytic aims and a reproducible modeling workspace

Module 01 asks one release question: may this analytic aim, prediction-time boundary, feature contract, temporal split, baseline, and repository state enter regression and prediction work?

- Course: FND-2 Modeling, Inference, and Reproducible Analytics
- Week: 1
- Learner work: 15.5 hours
- Module version: 0.1.0
- Commons release: 0.39.0
- Status: runnable release candidate; human review pending
- Graded role: 15 course points carried into the cumulative Week 3 checkpoint
- Decision owner: senior quantitative analyst acting as modeling-workflow reviewer
- Allowed dispositions: `accept`, `accept with conditions`, `revise`, or `refer`

The package uses the exact accepted FND-1 synthetic analytic table. It contains 374 people and 29 source fields and supports no claim about real patients or clinical performance.

## What learners prove

Learners classify descriptive, associational, predictive, causal, longitudinal, and forecasting questions before choosing a method. They define the acute-return prediction target, freeze prediction time at index stop, assign every field a role, block future information, create the deterministic temporal split, and record the training-prevalence baseline before any candidate model is fit.

The frozen split is:

| Split | Rows | Positives | Negatives | Index-start dates |
|---|---:|---:|---:|---|
| Train | 224 | 25 | 199 | 2015-01-01 through 2017-04-02 |
| Validation | 75 | 7 | 68 | 2017-04-05 through 2018-04-03 |
| Test | 75 | 4 | 71 | 2018-04-18 through 2019-12-28 |

The constant baseline probability is fit from training data only: `25 / 224 = 0.111607142857`.

## Package map

| Path | Purpose |
|---|---|
| `build_modeling_workspace.py` | Verifies the FND-1 source and creates a protected learner workspace or reference outputs. |
| `validate_modeling_workspace.py` | Validates the reference release or a starter or completed learner package. |
| `outputs/` | Exact modeling cohort, split registry, baseline, checks, and build report. |
| `aim-and-method-plan.md` | Completed reference decision and method-family plan. |
| `estimand-target-registry.csv` | Six aim-specific target or estimand contracts. |
| `feature-role-contract.csv` | All 29 source fields and five derived fields with allowed or blocked roles. |
| `aim-classification-exercises.csv` | Twelve independent classification prompts. |
| `learner-template/` | Prompted records copied into a new learner workspace. |
| `assessment.md` | Exact 15-point scoring and noncompensable gates. |
| `instructor-notes.md` | Timing, answer key, misconceptions, and review guidance. |
| `release.json` | Machine-readable release and validation record. |

Durable module specification:

`docs/curriculum/courses/FND-2/modules/01-aims-reproducible-workspace-spec.md`

## Build a clean learner copy

From the repository root:

```text
python courses/modeling-inference-reproducible-analytics/modules/01-aims-reproducible-workspace/build_modeling_workspace.py learner-workspace
```

The target must not exist. The builder verifies the upstream byte count and SHA-256, copies the complete accepted source into the workspace, and refuses to merge with or overwrite another folder.

## Validate

```text
python courses/modeling-inference-reproducible-analytics/modules/01-aims-reproducible-workspace/validate_modeling_workspace.py --self-check
python courses/modeling-inference-reproducible-analytics/modules/01-aims-reproducible-workspace/validate_modeling_workspace.py learner-workspace --mode starter
python courses/modeling-inference-reproducible-analytics/modules/01-aims-reproducible-workspace/validate_modeling_workspace.py learner-workspace --mode submission
```

Starter validation allows visible `REPLACE` prompts. Submission validation rejects them and requires the learner's progression decision and accountability records.

Inside a copied learner workspace, rebuild the deterministic data outputs into a new target with:

```text
python build_modeling_workspace.py reproduced-outputs --outputs-only
```

Compare that target with `outputs/`, then record the result in `reproducibility-check.md`. The target must not already exist.

## Boundary

This module does not fit regression, logistic regression, machine-learning, causal, longitudinal, or forecasting models. It makes the question and information boundary safe enough for those later decisions. Test labels may be counted to reconcile the frozen artifact, but they may not guide feature selection, preprocessing, tuning, threshold choice, or model selection.

## Authoritative references

- Synthea downloads: https://synthea.mitre.org/downloads
- Synthea CSV data dictionary: https://github.com/synthetichealth/synthea/wiki/CSV-File-Data-Dictionary
- scikit-learn common pitfalls: https://scikit-learn.org/stable/common_pitfalls.html
- scikit-learn model selection: https://scikit-learn.org/stable/model_selection.html
- Python virtual environments: https://docs.python.org/3/library/venv.html
- Semantic Versioning 2.0.0: https://semver.org/spec/v2.0.0.html
- MGH Institute 2026-2027 academic calendar: https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf
