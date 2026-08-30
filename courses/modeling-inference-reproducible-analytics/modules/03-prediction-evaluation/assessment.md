# Assessment: locked prediction evidence

## Submission

Submit one protected package tagged `fnd2-prediction-v0.1.0`. Preserve the seven upstream fingerprints, complete every prompted decision record, rebuild the evidence into a new target, validate the package, and defend whether the workflow should continue to validity review, be revised, or stop.

## Required defense

Explain:

1. why preprocessing must be fit separately inside each training resample;
2. why resampling, validation, and test serve different purposes;
3. why the training-prevalence baseline stays in every comparison;
4. why `LEAK01` is rejected even though its validation metrics are nearly perfect;
5. why `ML01`, rather than `LOG01`, passes the frozen selection rule;
6. how ROC AUC, average precision, Brier score, and log loss answer different questions;
7. how the locked threshold follows the stated consequence of missing no more than two of seven validation outcomes;
8. every numerator and denominator in the test confusion table;
9. why accuracy alone would hide the class imbalance;
10. why the test result is uncertain with only four positive outcomes;
11. what the calibration table does and does not establish;
12. why subgroup counts and suppression precede any comparison;
13. why a deterministic refit contract is acceptable for this teaching package;
14. which facts trigger a return to Modules 01, 02, or 03; and
15. why selection does not imply deployment readiness.

## Fifteen-point Week 3 share

| Criterion | Course points |
|---|---:|
| Leakage-safe preprocessing, resampling, and model lock | 3.00 |
| Baseline, validation comparison, and selection rule | 2.50 |
| Untouched test discrimination and calibration evidence | 3.00 |
| Threshold, confusion measures, prevalence, and decision meaning | 2.50 |
| Subgroup counts, uncertainty, sparse-outcome limits, and failure analysis | 2.50 |
| Accessible evidence, reproduction, and responsible agent record | 1.50 |
| Total | 15.00 |

The minimum numeric score is 12.00 of 15.00. Every gate must pass.

## Noncompensable gates

1. All seven upstream fingerprints and the 224/75/75 split are unchanged.
2. Training, validation, and test outcome counts remain 25, 7, and 4.
3. Every preprocessing fit occurs inside allowed training rows.
4. Validation does not fit model parameters.
5. Test does not choose a feature, model, metric, threshold, plot, subgroup rule, or narrative.
6. The training-prevalence baseline remains in resampling, validation, and test evidence.
7. All eligible candidates use the same validation rows and metrics.
8. `LEAK01` is rejected before its performance is considered.
9. Exactly one eligible candidate passes the declared selection rule.
10. The threshold rule is linked to validation counts and locked before test.
11. Every test row has exactly one locked selected-model prediction.
12. The exact confusion table sums to 75 and preserves four outcomes.
13. Discrimination, probability accuracy, calibration, and threshold utility are not substituted for one another.
14. Point estimates are paired with the four-outcome limitation.
15. Subgroup rows and outcomes appear before metrics, and unsupported cells are suppressed.
16. Exact tables accompany both plots.
17. The learner makes no real-clinical, fairness, safety, causal, or deployment claim.
18. Reproduction, environment, and material AI assistance are recorded.
19. The builder refuses existing targets and the validator passes.
20. The reviewer records an allowed Checkpoint 1 recommendation.

## Checkpoint role

This module contributes 15 of the 25 regression-and-prediction points in the Week 3 checkpoint. Module 02 contributes the other 10. Module 01 contributes 15 separate analytic-aim and reproducibility points, producing the 40-point cumulative decision.
