# Reference model card

## Purpose and users

This synthetic teaching model demonstrates a reproducible 90-day acute-return prediction workflow for learners and technical reviewers. It does not guide patient care, workflow, staffing, capacity, payment, performance judgment, or deployment.

## Data, target, prediction time, and horizon

One row represents one synthetic adult's accepted index encounter. The modeling cohort has 374 rows. Prediction occurs at index-encounter stop; the binary target is emergency or inpatient return within 90 days. The fixed split is 224 train, 75 validation, and 75 test with 25, 7, and 4 outcomes. IDs, outcomes, post-index fields, future fields, follow-up fields, split metadata, and unsupported high-cardinality fields are prohibited predictors.

## Model, baseline, and evaluation design

Training prevalence 25/224 = 0.111607142857 is the retained probability baseline. Preprocessing is fit on training only. Validation selects `ML01` and locks threshold 0.08513264 before the untouched 75-row test is opened. `LEAK01` remains ineligible regardless of apparent performance.

## Performance, calibration, threshold, and uncertainty

Test ROC AUC is 0.58802817 with stratified-bootstrap interval 0.26760563 to 0.91549296. Average precision is 0.14682471. Brier score is 0.05097579 versus baseline 0.05388473. At the locked threshold there are 48 TN, 23 FP, 2 FN, and 2 TP: sensitivity 0.50000000, specificity 0.67605634, PPV 0.08000000, and NPV 0.96000000. Four outcomes make discrimination, calibration, threshold, and interval conclusions fragile.

## Subgroup and equity evidence

The test appendix has ten group rows. Five of ten are suppressed for fewer than 20 rows or fewer than two outcomes/nonoutcomes. The remaining rows have sparse outcomes. These descriptive teaching estimates do not support group ranking, fairness certification, absence-of-harm claims, or differential action.

## Validity and forecast boundaries

Prediction is not causal. The Module 04 treatment, repeated, and survival cases are synthetic teaching fixtures. The 111-row timing subset is selected; 263 structural blanks remain blank. Missingness assumptions are not facts. The public CDC forecast is a 94-week Massachusetts jurisdiction aggregate across changing reporting hospitals, not one hospital or a staffing model.

## Intended, prohibited, and unsupported use

Intended use is technical education and method development. Prohibited uses include patient-level action, clinical decision support, clinical efficacy claims, treatment claims, staffing, capacity, operations, performance judgment, fairness certification, safety claims, causal effects, stable-process claims, real-population claims, silent validation, and deployment. Silent prospective validation would require a new real-data protocol and named governance that this reference cannot authorize.

## Monitoring, stop, and safe fallback

`monitoring-plan.csv` is a governed simulation. It defines review triggers but contains no live data. Any identity drift, prohibited field, leakage, failed test, unsupported claim, or missing accountable owner stops the teaching candidate. Safe fallback is no model or forecast action while evidence is quarantined and reviewed.

## Agent use, ownership, and review

An agent assisted with bounded curriculum construction. The lower aggregate forecast MAE claim was independently recalculated; staffing readiness was rejected; residual independence was narrowed; the leaked-model claim was rejected. Shuhan He owns the reference construction disposition. Actual learner and named panel approval remain required before alpha.
