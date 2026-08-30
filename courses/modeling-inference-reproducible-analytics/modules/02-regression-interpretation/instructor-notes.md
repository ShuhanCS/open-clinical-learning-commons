# Instructor notes

## Suggested 16-hour sequence

| Activity | Hours |
|---|---:|
| Module 01 handoff and formula declaration | 1.0 |
| Linear regression concept and fit | 2.0 |
| Linear residual, influence, and uncertainty lab | 2.0 |
| Logistic regression quantities and fit | 2.5 |
| Logistic diagnostics, sparsity, and extreme probabilities | 2.0 |
| Reference levels, centering, and model matrices | 1.0 |
| Nonlinear-term and interaction labs | 1.5 |
| Python and paired R reading | 1.5 |
| Interpretation, reproduction, and defense | 2.5 |
| Total | 16.0 |

## Core teaching move

Ask "what quantity is this?" before asking whether it is large, significant, or useful. Learners should point to the outcome scale, predictor unit, reference, conditioning variables, fitting population, and uncertainty method.

## Linear case answer key

- Fit rows: 69 training rows.
- All available timing rows: 111.
- Structural blanks: 263.
- Outcome range: 0.9 to 29.958333 days.
- R-squared: 0.07951657.
- Prior-encounter coefficient: -0.10110471 days per one-count increase.
- Classical 95-percent interval: -0.19973978 to -0.00246963.
- Jarque-Bera p-value: 0.04655734.
- Breusch-Pagan p-value: 0.14825876.
- Maximum Cook distance: 0.07408089.
- Maximum leverage: 0.58620136.

Do not let the nominal prior-encounter p-value become the story. The selection condition, small sample, residual normality result, influence, source meaning, and tiny effect scale all change the interpretation.

## Logistic case answer key

- Fit rows: 224 training rows.
- Positive outcomes: 25.
- Age center: 46.245535714286 years.
- Prior-acute log-odds estimate: 0.79038049.
- Prior-acute odds ratio: 2.20423495.
- Model-based 95-percent odds-ratio interval: 1.34053977 to 3.62439954.
- Inpatient odds ratio: 0.92176105.
- Inpatient interval: 0.24698931 to 3.44000081.
- Maximum fitted probability: 0.99962269.
- `LOG02` added-term likelihood-ratio p-value: 0.81417483.
- `LOG03` added-term likelihood-ratio p-value: 0.55542782.

## Odds versus risk exercise

Have learners translate odds to probability with `p = odds / (1 + odds)` for a declared starting value. Show that multiplying odds by 2.204 does not multiply probability by 2.204. Require a scenario probability table for probability language.

## Interaction exercise

For `LOG03`, the prior-acute coefficient is the slope for the emergency reference. The interaction is the added slope for inpatient rows. The inpatient prior-acute slope on log odds is their sum. Neither coefficient alone is the inpatient slope.

Do not permit learners to call a nonsignificant interaction proof of identical effects. It is uncertain evidence from a small training sample.

## Nonlinear exercise

For `LOG02`, the age slope changes with centered age. There is no single age odds ratio that applies everywhere. Ask learners to compare predicted probabilities at two ages while holding the other fields fixed.

## Sparse-cell review

The `other` race category has zero training rows. `native` has three training rows and zero positive outcomes. Race is not in the bounded formula. This is deliberate: a general permission in Module 01 does not require every allowed predictor to enter every small model.

## R route

The course assesses reading and reconciliation, not from-scratch R programming. Learners run the supplied script, record R version and commands, and compare the eight base-model rows with `r-reading-fixture.csv` at tolerance 0.000001.

R may differ in display precision and term names. The script normalizes term names. Default OLS and GLM coefficients and standard errors should reconcile. If an environment or version differs, the learner resolves the reason rather than hiding the difference.

The release author machine has no R runtime. Named R execution remains a condition before alpha.

## Common failures

- fitting all 111 timing rows because the outcome is available;
- converting missing timing to zero;
- using validation or test to improve a coefficient story;
- reading `exp(beta)` as a risk ratio;
- interpreting the intercept without reference and centering;
- calling p greater than 0.05 "no effect";
- calling p less than 0.05 important or causal;
- deleting influential rows automatically;
- merging sparse categories without a clinical and reporting plan;
- selecting `LOG02` or `LOG03` from training AIC;
- treating convergence as model validity; and
- treating Python/R agreement as proof of a correct analytic question.

## Oral check

Give the learner one coefficient and ask for a one-sentence interpretation containing the outcome, unit, predictor change, reference, conditioning set, fit partition, and causal boundary. Then ask what evidence could invalidate that interpretation.

## Reference disposition

`accept with conditions`. `LOG01` may enter Module 03 prediction evaluation. The linear case remains conditional, diagnostics remain visible, R execution remains pending, sparse cells are not ranked, and no real clinical or causal claim is permitted.
