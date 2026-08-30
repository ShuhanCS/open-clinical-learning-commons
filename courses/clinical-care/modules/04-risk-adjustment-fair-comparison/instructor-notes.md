# Instructor notes

## Teaching center

Start with the difference between expected outcomes and deserved outcomes. The model estimates expected event counts from four baseline fields. It does not say what a patient or site should experience, and it does not make a site comparison fair by itself.

Ask learners to trace one person from baseline fields to predicted probability, then aggregate probabilities into an exposure group and a site. Follow that route before introducing O/E ratios or standardized rates.

## Required corrections

- Apparent AUC and Brier results are not external validation.
- The sum of expected events matching 87 is a fitted-intercept property, not proof of calibration.
- The adjusted odds ratio is not a risk ratio, hazard ratio, or causal effect.
- SITE-B and SITE-C only just meet the observed-event threshold.
- A site that passes suppression is reported with caution and is never ranked.
- Exact Poisson count intervals here treat expected counts as fixed.
- The six site labels are synthetic and have a known direct outcome effect of zero.
- Excluding demographic fields from expected outcomes does not prove fairness.
- The failed Module 03 proportional-hazards screen remains part of the evidence.

## Progression

Return a package that changes the cohort, selects predictors after fitting, leaks exposure or outcomes into expected values, hides bootstrap instability, changes site order, or uses causal, fairness, ranking, or deployment language. A learner may proceed with conditions when the field roles, support limits, uncertainty, and synthetic provenance stay visible.
