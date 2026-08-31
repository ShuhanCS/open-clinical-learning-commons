# Data and evidence specification

## Frozen inputs

- Complete APP-4 Module 05 reference workspace: 341 files, 324 immutable manifest rows, 75,019 manifest bytes, SHA-256 `6bc3e7c0040b8ae93d273d1464459ae8d500913e0e8a423ca1e5b120256c8baf`.
- Module 03 model cohort: 7,544 historical public NHANES teaching rows.
- Module 03 transparent predictions: the same 7,544 aligned rows.
- Module 03 subgroup-support audit: the same groups, partitions, and support states.

## Model contract

The target is the observed HbA1c result at or above 6.5 percent, not a diagnosis. The predictors are age centered at 50 per ten years, BMI centered at 30 per five units, and the source-recorded female indicator. Development uses 2013-2014 and 2015-2016. The untouched temporal holdout is 2017-2018. The later transport stress set is 2021-2023.

The challenger is one fixed `GradientBoostingClassifier` with 80 estimators, learning rate 0.05, depth 2, minimum leaf size 50, full sampling, and random state 7400600. Survey weights are normalized within development only for fitting. There is no search, resampling, calibration fit, or tuning after holdout inspection.

## Safety evidence

The hazard register carries all 17 Module 05 failure modes and adds five prospective monitoring and governance hazards. The monitoring register contains 20 measures, eight seeded scenarios, and 12 human escalation routes. These are teaching designs, not observed clinical incident rates or validated control limits.

## Authority boundary

The data may be used to teach reproducible analysis, safety reasoning, monitoring design, and model comparison. It may not be used for real-patient scoring, diagnosis, threshold acceptance, clinical alerting or action, silent-mode evaluation, implementation, production connection, or deployment.
