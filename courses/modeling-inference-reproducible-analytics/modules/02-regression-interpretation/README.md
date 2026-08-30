# FND-2 Module 02: Regression models and interpretation

Module 02 asks whether bounded linear and logistic regression evidence is accurate, uncertainty-aware, and honestly interpreted enough to enter prediction evaluation.

- Course: FND-2 Modeling, Inference, and Reproducible Analytics
- Week: 2
- Learner work: 16.0 hours
- Module version: 0.1.0
- Commons release: 0.40.0
- Status: runnable release candidate; human review pending
- Week 3 role: 10 of the 25 regression-and-prediction course points
- Decision owner: biostatistical methods reviewer
- Allowed dispositions: `accept`, `accept with conditions`, `revise`, or `refer`

Every fitted model uses training data only. Validation and test rows do not shape formulas, encodings, coefficients, diagnostics, uncertainty, or interpretation in this module.

## Two bounded cases

The linear case uses people with a recorded different encounter within 30 days. There are 111 such rows across the full cohort, but only the 69 training rows are fit and interpreted. The other 263 cohort rows retain structural blanks; they are never changed to zero. The result is conditional on having a recorded next encounter and is not a time-to-event model for all 374 people.

The logistic case uses all 224 training rows and 25 positive outcomes. `LOG01` includes centered age by decade, prior 365-day acute count, and inpatient versus emergency index class. It reports conditional log odds, odds ratios, and scenario probabilities. None is a risk ratio, probability difference, or causal effect.

`LOG02` adds a centered-age squared term. `LOG03` adds an index-class by prior-acute-count interaction. They are interpretation exercises, not validation-based prediction candidates. Module 03 receives the bounded `LOG01` formula for prediction evaluation.

## Package map

| Path | Purpose |
|---|---|
| `build_regression_evidence.py` | Verifies Module 01 inputs and fits the exact training-only models. |
| `validate_regression_evidence.py` | Rebuilds and compares every output and rejects incomplete submissions. |
| `paired-models.R` | Fits matching base linear and logistic formulas for R reading and reconciliation. |
| `formula-registry.csv` | Declares formulas before fitting. |
| `reference-levels.csv` | Freezes encodings, centering, and outcome references. |
| `interpretation-quantity-guide.csv` | Separates coefficients, odds ratios, probabilities, and causal quantities. |
| `outputs/` | Exact coefficients, uncertainty, diagnostics, comparisons, checks, and build report. |
| `regression-interpretation.md` | Completed reference interpretation and stop boundaries. |
| `assessment.md` | Exact ten-point scoring and noncompensable gates. |
| `instructor-notes.md` | Timing, answer key, misconceptions, and review guidance. |

Durable module specification:

`docs/curriculum/courses/FND-2/modules/02-regression-interpretation-spec.md`

## Build a learner copy

From repository root:

```text
python courses/modeling-inference-reproducible-analytics/modules/02-regression-interpretation/build_regression_evidence.py learner-workspace
```

The target must not exist. Inside the copied workspace, reproduce outputs with:

```text
python build_regression_evidence.py reproduced-outputs --outputs-only
```

## Validate

```text
python courses/modeling-inference-reproducible-analytics/modules/02-regression-interpretation/build_regression_evidence.py --self-check
python courses/modeling-inference-reproducible-analytics/modules/02-regression-interpretation/validate_regression_evidence.py --self-check
```

Learner environments with R run:

```text
Rscript paired-models.R data/modeling-cohort.csv outputs/r-coefficients.csv
```

The release machine has no R runtime. The package therefore includes a transparent Python-generated numeric reading target plus the exact R script; named R execution and platform review remain conditions before alpha.

## Reference findings

- Linear training subset: 69 rows.
- Linear outcome: 0.9 through 29.958333 days.
- Linear R-squared: 0.07951657.
- Jarque-Bera p-value: 0.04655734, so normal-error approximation remains a review condition.
- Maximum linear Cook distance: 0.07408089, above the 4/n review threshold.
- Logistic training rows and events: 224 and 25.
- `LOG01` prior-acute-count odds ratio: 2.20423495 with model-based 95-percent interval 1.34053977 to 3.62439954.
- The largest `LOG01` fitted probability is 0.99962269, so extreme prediction and influence checks remain visible.
- Training-only added-term likelihood-ratio p-values are 0.81417483 for `LOG02` and 0.55542782 for `LOG03`.

These are synthetic, model-conditional teaching results. They do not support causal, real-population, clinical, operational, or deployment claims.

## References

- statsmodels regression: https://www.statsmodels.org/stable/regression.html
- statsmodels generalized linear models: https://www.statsmodels.org/stable/glm.html
- R linear models: https://stat.ethz.ch/R-manual/R-devel/library/stats/html/lm.html
- R generalized linear models: https://stat.ethz.ch/R-manual/R-devel/library/stats/html/glm.html
- scikit-learn common pitfalls: https://scikit-learn.org/stable/common_pitfalls.html
