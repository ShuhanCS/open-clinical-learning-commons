# Reference cumulative interpretation

## Decision and supported use

The exact synthetic teaching workflow is technically coherent enough to enter validity review with conditions. The package supports instruction in reproducible modeling and evidence review. It does not support real clinical performance, treatment, triage, fairness, safety, or deployment claims.

## Source, cohort, and timing

Module 01 preserves the accepted FND-1 374-row analytic table and creates a 374-row, 34-field modeling cohort with one selected index encounter per synthetic person. Prediction time is the end of the index encounter. The target is emergency or inpatient return within 90 days. Post-index next-event fields, outcomes, endpoints, follow-up fields, identifiers, and split metadata are blocked from eligible prediction features.

## Split and baseline

The deterministic temporal split contains 224 training, 75 validation, and 75 test rows with 25, 7, and 4 outcomes. The constant training-prevalence baseline is 25/224 = 0.111607142857. Validation and test do not estimate that baseline.

## Regression evidence

The linear timing case contains 111 rows with a recorded different encounter in 30 days, but only 69 training rows are fit. The other 263 cohort rows have structural blanks, not zero-day events. `LOG01` fits 224 training rows and 25 outcomes. Its prior-acute-count odds ratio is 2.20423495, a conditional odds quantity rather than a risk multiplier, probability change, or causal effect. Residual, influence, extreme-probability, sparse-category, and pending R-execution conditions remain visible.

## Prediction selection and threshold

Training-only resampling refits preprocessing within every fold. Validation compares the constant baseline, `LOG01`, bounded random forest `ML01`, and prohibited `LEAK01` on the same 75 rows. `LEAK01` is rejected before performance review because it uses post-index and outcome-derived fields. `ML01` is the only eligible candidate meeting the frozen Brier, ROC AUC, and average-precision rule. The threshold rule requires at least 5 of 7 validation outcomes, then minimizes false positives, then chooses the highest tied threshold. It locks 0.08513264 before test.

## Untouched test evidence

`ML01` test ROC AUC is 0.58802817, average precision 0.14682471, Brier score 0.05097579, and log loss 0.21218264. At the locked threshold, there are 48 true negatives, 23 false positives, 2 false negatives, and 2 true positives. Sensitivity is 2/4, specificity is 48/71, PPV is 2/25, and NPV is 48/50. The high NPV does not establish safety because the outcome is rare and half the observed outcomes are missed.

## Calibration, uncertainty, and subgroups

Five 15-row calibration groups contain only four outcomes and do not support a stable calibration curve, slope, or intercept. The stratified bootstrap ROC AUC interval is 0.26760563 to 0.91549296. Subgroup rows report counts first; five of ten rows suppress metrics for small or outcome-sparse cells. No subgroup ranking or fairness conclusion is supported.

## Reproduction, accessibility, and AI

All module outputs reproduce under their pinned environments. The checkpoint copies them byte for byte into a 78-row immutable manifest. Calibration and threshold SVGs have exact CSV alternatives. OpenAI Codex assisted with specifications, code, validation, and teaching records; humans remain responsible for meaning, scoring, review, and progression.

## Supported and unsupported claims

Supported: the exact versioned teaching package follows its declared fit, selection, threshold, and test rules and can proceed to validity instruction.

Unsupported: the model is clinically useful, causally valid, calibrated for care, fair, safe, transportable, or ready to deploy.

## Module 04 questions

Module 04 must examine confounding versus prediction adjustment, selection in the 111-row timing subset, missingness assumptions, repeated and clustered structure, time-to-event alternatives, and how those issues change the claim or require referral. It must preserve the original locked test evidence.
