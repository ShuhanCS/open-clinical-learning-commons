# Assessment: bounded regression evidence

## Submission

Submit one protected package tagged `fnd2-regression-v0.1.0`. Preserve every Module 01 input, complete all prompted records, reproduce the outputs into a new target, run the paired R script in an approved R environment, reconcile Python and R within tolerance, validate the package, and state whether Module 03 may proceed.

## Required defense

Explain:

1. why the linear outcome includes 111 cohort rows but only 69 training rows are fit;
2. why 263 structural blanks are not zero;
3. what each declared coefficient means in its actual unit;
4. the difference among log odds, odds ratios, risks, and probabilities;
5. why the prior-acute odds ratio is not a probability multiplier or causal effect;
6. how reference levels and age centering change interpretation;
7. what classical and HC3 uncertainty each assume;
8. which residual, influence, sparsity, and extreme-probability findings matter;
9. how nonlinear and interaction terms change the formula and coefficient meaning;
10. why training likelihood or p-values do not select a prediction model;
11. how Python and R output were reconciled; and
12. what Module 03 receives and must still evaluate.

## Ten-point Week 3 share

| Criterion | Course points |
|---|---:|
| Declared formulas, encodings, and reference levels | 2.00 |
| Correct linear and logistic fitting evidence | 2.50 |
| Assumption, sparse-data, influence, and failure checks | 2.50 |
| Quantity-correct uncertainty and interpretation | 2.00 |
| Reproduction, R reading, and responsible agent record | 1.00 |
| Total | 10.00 |

The minimum numeric score is 8.00 of 10.00. Every gate must pass.

## Noncompensable gates

1. Module 01 fingerprints, role contract, split, and baseline are unchanged.
2. Linear fitting uses only 69 training rows with recorded timing.
3. All 263 structural blanks remain blank and are never converted to zero.
4. Logistic fitting uses only 224 training rows and 25 outcomes.
5. Validation and test do not shape formulas, fits, uncertainty, or interpretation.
6. Formulas, transforms, encodings, and references are declared before fitting.
7. Linear coefficients are interpreted as conditional mean differences in days.
8. Logistic coefficients, odds ratios, and probabilities are named correctly.
9. No associational estimate is called a causal effect.
10. Classical and robust uncertainty methods are identified.
11. Residual, influence, sparsity, and extreme fitted-value evidence remains visible.
12. Nonlinear and interaction exercises do not silently become selected prediction models.
13. Python and R base-model outputs reconcile within 0.000001 or the difference is resolved before progression.
14. The builder refuses existing targets and the validator passes.
15. Material AI assistance is disclosed and independently checked.
16. The release contains no real patient data, secret, private URL, or local absolute path.
17. An allowed human-owned Module 03 disposition is explicit.

## Checkpoint role

This module contributes 10 of the 25 course points assigned to regression and prediction in the Week 3 checkpoint. Module 03 contributes the other 15 points. Module 01's accepted 15 points are assembled separately, producing the 40-point cumulative checkpoint.
