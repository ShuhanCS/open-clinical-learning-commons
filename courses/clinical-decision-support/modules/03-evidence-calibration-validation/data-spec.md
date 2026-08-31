# APP-4 Module 03 data specification

## Inherited chain of custody

The workspace freezes the exact 73 immutable files accepted by APP-4 Module 02. That inheritance contains all 16 public NHANES XPT files and profiles from Module 01 plus the complete Synthea and Commons logic release from Module 02.

The evidence builder checks the 16 XPT gzip byte counts and SHA-256 identities before parsing. The files contain 145,563 component rows and 3,149,043 committed gzip bytes. No public source row is rewritten in place.

## Historical cohort

The reference teaching cohort follows this order:

1. age 35 through 70;
2. valid source-recorded sex;
3. `DIQ010 = 2`, meaning no self-reported diabetes;
4. nonpregnant or pregnancy status not applicable;
5. observed BMI;
6. BMI at least 25 kg/m2;
7. observed `LBXGH`; and
8. positive analytic weight, stratum, and PSU.

Pregnant and unknown pregnancy states are excluded when the pregnancy question applies. Missing values are not imputed. The audit frame retains all 14,892 age-eligible rows so every exclusion and unavailable field can be counted.

The resulting model cohort has 7,544 rows and 328 outcomes. The outcome is `LBXGH >= 6.5%`. It is an observed laboratory cut-point indicator, not a diagnosis, confirmed disease, local event, treatment indication, or patient-level recommendation. NIDDK describes 6.5% or higher as a diabetes-range A1C result and requires repeat confirmation when symptoms are absent.

## Partition and weight contract

| Partition | Cycles | Weight | Use |
| --- | --- | --- | --- |
| Development | 2013-2014 and 2015-2016 | `WTMEC2YR / 2` | Fit the fixed transparent model |
| Temporal holdout | 2017-2018 | `WTMEC2YR` | Evaluate once without tuning |
| Transport stress | August 2021-August 2023 | `WTPH2YR` | Separate later-cycle stress test |

`SDMVSTRA` and `SDMVPSU` remain attached to every model row. The 2021-2023 release uses the phlebotomy weight because HbA1c is a blood analyte. It is not pooled with the earlier cycles. The 500-replicate stratified-PSU bootstrap is a deterministic teaching sensitivity method, not an NCHS-endorsed publication variance estimator.

## Model contract

The fixed model is a survey-weighted binomial GLM with logit link:

`logit(P(LBXGH >= 6.5%)) = intercept + age centered at 50 per 10 years + BMI centered at 30 per 5 kg/m2 + female indicator`

Race and Hispanic-origin category is not a predictor. It is retained only for descriptive support review. The model is not retuned, recalibrated, refit, or selected on the holdout or transport partitions. Model coefficient uncertainty remains unavailable pending a named complex-survey methods review.

## Evidence files

`data/evidence/evidence-manifest.csv` fingerprints 17 derived files:

- full cohort audit, final model cohort, and participant-level fixed predictions;
- cohort flow, missingness, and survey-design tables;
- coefficient, performance, calibration, and score-range calibration tables;
- threshold, net-benefit, subgroup, bootstrap, and transport tables;
- invariant checks; and
- the machine-readable build report.

Every display concept must use one of these exact tables as its accessible alternative.

## Threshold and claim contract

The evidence candidates are `0.02`, `0.03`, `0.04`, `0.05`, `0.075`, and `0.10`. They expose different candidate-card and missed-case tradeoffs. None is selected or accepted. The `0.20` Module 02 value is a rejected mechanics comparison.

Decision-curve output applies only to the declared threshold odds. It does not estimate patient benefit, harm, preference, cost, workflow fit, or clinical utility. NHANES does not establish local calibration, prospective performance, workflow burden, safety, fairness, or deployment readiness.
