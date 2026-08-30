# Reference aim and method plan

## Decision statement

A senior quantitative analyst decides whether this synthetic modeling package is technically ready to enter bounded regression and prediction teaching. The immediate action is either to permit Module 02 work or to return the package for correction. This module does not decide whether a real patient needs care, whether an intervention works, whether a hospital performs well, or whether a model should be deployed.

## Primary prediction question

At the stop of a selected synthetic adult's index emergency or inpatient encounter, what is the estimated probability that a different emergency or inpatient encounter will occur within the next 90 days?

## Contract

| Element | Registered value |
|---|---|
| Aim | predictive |
| Population | 374 selected synthetic adults in the accepted FND-1 cohort |
| Unit | one selected adult and one index encounter |
| Time zero | index encounter stop |
| Prediction time | index encounter stop |
| Predictors | nine allowed pre-prediction fields in `feature-role-contract.csv` |
| Outcome | `acute_return_90d` |
| Horizon | 90 days after index stop |
| Success criterion | candidate models must be compared with the frozen training-prevalence baseline using validation evidence before one untouched test evaluation |
| Intended use | graduate teaching of reproducible prediction workflow |
| Prohibited use | clinical decisions real risk estimates operations ranking or deployment |

## Method-family decision

The primary aim is predictive, so Module 03 may compare a bounded logistic-regression pipeline and a supplied machine-learning baseline. Descriptive summaries alone cannot answer individual prediction. An associational regression coefficient is not prediction performance. A causal model is unsupported because no intervention contrast or exchangeability design exists. A longitudinal model is unsupported because the accepted cohort has one modeling row per person. A forecast model is unsupported because these rows are not an aggregate equally spaced time series.

## Prediction-time rule

Only information available at or before `index_stop` may be considered. Feature roles are fixed before model fitting. The four next-30-day fields and all future or outcome-derived 90-day fields are blocked. `acute_return_90d` is used only as the label. IDs, source metadata, split fields, and reviewer decisions are not predictors.

## Split rule

Rows are ordered by `index_start` and then `patient_id`. Positions 1-224 are training, 225-299 are validation, and 300-374 are test. Test labels do not guide preprocessing, feature selection, tuning, threshold choice, model selection, or revision. Four positive test outcomes mean the final estimate will be imprecise; they do not justify resplitting.

## Baseline rule

The first comparison is a constant probability equal to the training prevalence: 25 positive outcomes divided by 224 training rows, or `0.111607142857`. It is frozen before any candidate model is compared.

## Reference disposition

`accept with conditions`

Module 02 may proceed with the exact cohort, field roles, split, and baseline. Conditions: the source remains synthetic and older; the test set has only four positives; race categories include sparse groups; high-cardinality code and reason fields remain excluded; and no result may be presented as a real clinical or deployment estimate.
