# Logic and evidence readiness review

## Cumulative decision

The accepted use case, logic, historical evidence, calibration, threshold comparisons, and claim limits may enter Module 04 curriculum construction with conditions.

The Week 3 score is `40 of 40`. Module 01 contributes zero points and remains a required gate. Module 02 contributes 20 points once, and Module 03 contributes 20 points once.

## Accepted identities

The checkpoint freezes 245 files from three complete reference workspaces. Their nested manifests contain 29, 73, and 102 immutable rows, for 204 immutable rows in total.

Module 01 preserves 16 complete official NHANES XPT files with 34,221,200 raw bytes, 3,149,043 deterministic gzip bytes, 145,563 component rows, 442 inventoried fields, and zero duplicate `SEQN` rows. Its use case remains the explicitly fictional `CGH-GIM-01` adult general internal medicine and primary care service.

The intended support remains a nonbinding candidate advisory asking the clinician responsible for the current adult encounter to consider whether confirmatory HbA1c testing is appropriate. It acts after intake information is available and before encounter close. It does not diagnose, order, treat, message, deny, target, or act automatically.

Module 02 preserves the Synthea 4.0.0 release with 1,000 Massachusetts adults, 25 FHIR R4 files, 811,803 resource rows, zero parse failures, 100,178,478 compressed bytes, and 11,109 repeated provider or organization resource IDs. Its source manifest SHA-256 is `0d3c4c11e5ab29284f312d76413f8e005fb957226039d324912f80af93dcf3c0`.

All 16 synthetic mechanics cases reproduce their expected result and ordered trace. They cover normal, boundary, missing, stale, inconsistent, duplicate, delayed, terminology, version, recent-result suppression, known-condition suppression, unit, context, silent-delivery failure, and missing-score states.

## Mechanics and evidence reconciliation

The Module 02 score values are fixtures, not predictions. Its `0.20` branch value is a rejected mechanics fixture, not an evidence candidate, recommendation, selected threshold, or accepted threshold. It cannot enter Module 04 as evidence.

Module 03 preserves 14,892 age-eligible audit rows and 7,544 model rows with 328 observed HbA1c outcomes. The historical target is `LBXGH >= 6.5%`, an observed laboratory cut-point indicator rather than a diagnosis or confirmation of disease. No imputation is used.

The fixed partitions are:

| Partition | Rows | Outcomes | Role |
|---|---:|---:|---|
| Development | 3,652 | 156 | 2013-2014 and 2015-2016 model fitting with `WTMEC2YR / 2` |
| Temporal holdout | 1,806 | 97 | 2017-2018 evaluation with `WTMEC2YR` and no retuning |
| Transport stress | 2,086 | 75 | 2021-2023 separate evaluation with `WTPH2YR` and no pooling |

The transparent model is one survey-weighted binomial GLM with a logit link. Its predictors are age centered at 50 per 10 years, BMI centered at 30 per 5 kg/m2, and a female indicator. Race and Hispanic origin remain audit dimensions and are not model predictors. Strata and PSUs remain attached to the analytic rows.

The temporal holdout has weighted prevalence `0.02904272`, mean probability `0.03015261`, Brier score `0.02811126`, log loss `0.12694930`, ROC AUC `0.68783144`, calibration-in-the-large `-0.03946013`, and calibration slope `0.88441129`.

The transport stress test has weighted prevalence `0.03274014`, mean probability `0.03041245`, Brier score `0.03175435`, log loss `0.14019059`, ROC AUC `0.68422573`, calibration-in-the-large `0.07788522`, and calibration slope `0.81620710`. These results do not establish a cause for the difference or local validity.

## Threshold consequences

All six evidence candidates remain unselected and unaccepted:

| Candidate | Holdout flags per 1,000 | Holdout sensitivity | Holdout specificity | Holdout missed per 1,000 |
|---:|---:|---:|---:|---:|
| 0.020 | 661.57323641 | 0.89675075 | 0.34546126 | 2.99863880 |
| 0.030 | 325.40301123 | 0.60091129 | 0.68283783 | 11.59062056 |
| 0.040 | 172.19709642 | 0.36288643 | 0.83350669 | 18.50350918 |
| 0.050 | 105.90526558 | 0.22855075 | 0.89776324 | 22.40498219 |
| 0.075 | 36.68485865 | 0.06348936 | 0.96411690 | 27.19881351 |
| 0.100 | 17.08750038 | 0.03841504 | 0.98355044 | 27.92703988 |

These are historical classification tradeoffs. The counts do not measure local card burden, clinician workload, patient benefit, or harm. Decision-curve values depend on declared threshold odds and do not prove patient benefit. Module 04 must compare a less interruptive alternative and no alert.

## Support and uncertainty

The 500-replicate stratified-PSU sensitivity bootstrap uses seed `7400303` and fixed predictions. It remains a teaching method pending formal complex-survey review.

In the temporal holdout, eight subgroup records report performance with a boundary and eight suppress performance because support rules are not met. In the transport stress test, five report with a boundary and 11 suppress performance. Suppressed performance remains blank. No group-specific threshold, action, fairness certification, or trait claim is authorized.

## Progression

The reference decision is `continue with conditions`. Module 04 may compare alert burden, human factors, access, equity, all six unaccepted candidates, a less interruptive alternative, and no alert. Module 04 must not inherit the `0.20` fixture, claim that an evidence candidate is accepted, or use a historical probability to score a real patient.

Prototype work remains gated by Module 04. Real-patient scoring, clinical alerting, diagnosis, ordering, treatment, implementation, production connection, and deployment remain prohibited.
