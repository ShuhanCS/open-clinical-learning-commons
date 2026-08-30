# Assessment: modeling-readiness release

## Submission

Submit one protected workspace tagged `fnd2-aims-v0.1.0`. Build it into a new target, complete every `REPLACE` prompt, rerun the deterministic outputs from the copied accepted source, validate the package in submission mode, and make an explicit Module 02 progression decision.

The submission must include:

- the exact copied 374-row and 29-field FND-1 source;
- the 374-row and 34-field derived modeling cohort;
- the fixed 224/75/75 split registry;
- all 29 source fields and five derived fields in the feature-role contract;
- the six-row estimand or target registry;
- all twelve classified practice requests;
- the training-prevalence baseline;
- the aim and method plan;
- environment, reproduction, AI-use, and progression records;
- the executed validator result; and
- a clean tagged Git state.

## Required explanation

In a short technical defense, explain:

1. why aim classification comes before method selection;
2. the difference between a target and an estimand;
3. the exact decision, unit, time zero, prediction time, label, and horizon;
4. why the nine default predictors are available at prediction time;
5. why IDs, dates, high-cardinality fields, next-event fields, labels, and split fields are excluded or blocked;
6. why temporal ordering is used and why the split cannot be repaired after seeing outcomes;
7. what validation data may influence and what test data may not influence;
8. how `25 / 224` creates the frozen baseline;
9. why four positive test outcomes limit precision but do not authorize resplitting;
10. why this synthetic package cannot support a real clinical estimate; and
11. what exact artifacts Module 02 may inherit.

## Fifteen-point course rubric

| Criterion | Points |
|---|---:|
| Decision, aim, target, population, time zero, and horizon | 4.00 |
| Exact FND-1 input, feature roles, and leakage boundary | 4.00 |
| Deterministic split, outcome reconciliation, and baseline | 3.00 |
| Reproducible repository, environment, build, and tests | 3.00 |
| Responsible agent disclosure and plain-language handoff | 1.00 |
| Total | 15.00 |

The minimum numeric score is 12.00 of 15.00. Every noncompensable gate must also pass.

## Noncompensable gates

1. The accepted FND-1 input is exact by byte count and SHA-256.
2. The grain remains 374 unique people and 374 unique index encounters.
3. Prediction time is stated before feature selection.
4. All 34 source and derived fields have one explicit role.
5. Every post-index and outcome-derived field is blocked from predictors.
6. The label is used only as the label.
7. Train, validation, and test rows reconcile to 224, 75, and 75.
8. Positive outcomes reconcile to 25, 7, and 4.
9. Test information does not guide preprocessing, fitting, selection, tuning, or threshold choice.
10. The baseline is fit from training data before candidate comparison.
11. The builder refuses an existing target.
12. The exact environment record and ordered commands are present.
13. The package contains no real patient data, credentials, private URL, or local absolute path.
14. Material AI use is disclosed and independently checked.
15. The progression disposition is `accept`, `accept with conditions`, `revise`, or `refer`.

Failure of a gate requires correction or referral even when the numeric score is 12.00 or higher.

## Week 3 checkpoint role

The accepted Module 01 state contributes 15 course points to Checkpoint 1. Modules 02 and 03 later contribute the separate 25-point regression and prediction component. The Week 3 checkpoint therefore totals 40 course points without rescoring Module 01 as a new assignment.
