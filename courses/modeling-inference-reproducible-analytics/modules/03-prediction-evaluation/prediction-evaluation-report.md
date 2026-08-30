# Reference prediction evaluation report

## Decision and use

Recommendation: `continue to validity review with conditions`.

The locked `ML01` workflow passes the predeclared validation selection rule and modestly improves probability-error measures over the constant baseline on the untouched test split. It does not show stable clinical utility, calibration, fairness, safety, or transportability. All evidence comes from synthetic Synthea records and is for teaching only.

## Preserved design

The prediction question, 90-day acute-return outcome, end-of-index prediction time, 374-row cohort, 224/75/75 temporal split, training-prevalence baseline, feature roles, and Module 02 regression conditions were accepted before this module. Their exact fingerprints were verified before fitting.

Training contains 25 outcomes, validation contains 7, and test contains 4. Preprocessing is fit only within each allowed training fit. Validation selects the model and threshold. Test is opened once after both are locked.

## Training evidence

Five-fold stratified training resampling was used to inspect variability, not to replace temporal validation. Each holdout fold contained five outcomes. All scaling and encoding were refit within the fold. The fold results vary materially, which is expected with few outcomes and keeps the later validation and test roles visible.

## Validation selection

The retained constant baseline has validation ROC AUC 0.50000000, average precision 0.09333333, Brier score 0.08495615, and log loss 0.31195460.

`LOG01` has ROC AUC 0.44957983, average precision 0.09196407, Brier score 0.08615760, and log loss 0.31945157. It does not meet any of the three candidate requirements.

`ML01` has ROC AUC 0.58613445, average precision 0.15806484, Brier score 0.08468750, and log loss 0.30994807. It is the only eligible candidate with Brier no worse than baseline, ROC AUC at least 0.55, and average precision no worse than baseline. It is selected by that rule.

`LEAK01` appears nearly perfect because it uses post-index and outcome-derived fields. It is never eligible. Its apparent validation performance is evidence of leakage, not model quality.

## Locked threshold

The threshold was chosen on validation data only. The rule required detection of at least 5 of the 7 validation outcomes, then minimized false positives, then chose the highest threshold if tied. The resulting threshold is 0.08513264. It was locked before test evaluation.

## Untouched test evidence

The selected model's test ROC AUC is 0.58802817, compared with 0.50000000 for the constant baseline. Average precision is 0.14682471, compared with the 0.05333333 test prevalence and baseline average precision. Brier score is 0.05097579, compared with 0.05388473 for baseline. Log loss is 0.21218264, compared with 0.22897744.

These point estimates are not stable proof. The stratified bootstrap interval for ROC AUC is 0.26760563 to 0.91549296 and the average-precision interval is 0.05532198 to 0.58716356. The small test outcome count drives that uncertainty.

At the locked threshold, the exact test table is:

| | Predicted negative | Predicted positive | Total |
|---|---:|---:|---:|
| Observed negative | 48 | 23 | 71 |
| Observed positive | 2 | 2 | 4 |
| Total | 50 | 25 | 75 |

Sensitivity is 2/4 or 0.50000000. Specificity is 48/71 or 0.67605634. PPV is 2/25 or 0.08000000. NPV is 48/50 or 0.96000000. The workflow misses two of four outcomes and flags 23 people who do not have the outcome. A high NPV does not override those counts or the low prevalence.

## Calibration

Five equal-size test groups contain 15 rows each. Their mean predicted probabilities are 0.07065743, 0.07692731, 0.08033173, 0.09035687, and 0.14452712. Their observed proportions are 0, 0.13333333, 0, 0.06666667, and 0.06666667. The pattern does not establish stable calibration. Exact rows are in `outputs/calibration-table.csv`; the SVG is only a visual companion.

## Subgroups

Every subgroup row reports its denominator and outcome count first. Metrics are suppressed for small or outcome-sparse cells. Five of ten rows are suppressed. The remaining estimates are descriptive and too limited for ranking or fairness claims. No subgroup changes the reference recommendation.

## Conditions for Module 04

1. Preserve the original locked test result and do not tune against it.
2. Carry forward the four-outcome test limitation and exact confusion counts.
3. Treat `ML01` features as predictors, not a causal adjustment set.
4. Review selection, missingness, repeated structure, and time-to-event alternatives before broadening any claim.
5. Preserve subgroup suppression and make no fairness conclusion.
6. Use no real patient, clinical workflow, or deployment claim.

## Return rules

A changed aim, population, prediction time, outcome, horizon, or field role returns to Module 01. A changed regression formula or interpretation returns to Module 02. A changed feature set, preprocessing step, candidate model, selection rule, threshold consequence, metric set, resampling rule, subgroup rule, or test-use policy returns to Module 03 and requires a semantic-version decision.
