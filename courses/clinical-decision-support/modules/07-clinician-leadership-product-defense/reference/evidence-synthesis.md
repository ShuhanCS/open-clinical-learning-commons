# Evidence synthesis

## Accepted evidence chain

Checkpoint 01 freezes 263 files and the exact Module 01 through Module 03 record. Its 245-row candidate manifest has SHA-256 `4e78d2313ce324fd372e6fc187afee333b27ed0cc0270c6ab8c08354dd5c3151`. The Week 3 score is 40 of 40. All six evidence thresholds remain unselected and unaccepted.

Checkpoint 02 freezes 1,047 files and the exact Module 04 through Module 06 record. Its 1,030-row candidate manifest has SHA-256 `14ac12dd890045dce21cdc44a9b614770b8b2428bd71a1d4f5eb9cc9de63d642`. The Week 6 score is 25.00 of 25.00, counted once.

## Historical evidence

- Sixteen complete NHANES XPT files contain 34,221,200 raw bytes and 145,563 component rows.
- The age-eligible audit has 14,892 rows.
- The fixed model cohort has 7,544 rows and 328 observed HbA1c outcomes.
- Development has 3,652 rows and 156 outcomes.
- Temporal holdout has 1,806 rows and 97 outcomes.
- Transport stress has 2,086 rows and 75 outcomes.
- The target `LBXGH >= 6.5%` is an observed laboratory cut-point indicator, not a diagnosis.
- The transparent model uses age, BMI, and a female indicator. Race and Hispanic origin remain audit dimensions, not predictors.
- NHANES supports historical teaching evidence. It does not establish local validity, clinical utility, or causal explanation.

## Threshold and workflow evidence

The six candidates are `0.020`, `0.030`, `0.040`, `0.050`, `0.075`, and `0.100`. None is accepted. The Module 02 `0.20` value remains a rejected mechanics fixture.

Module 04 constructed 1,200 synthetic encounter opportunities and 7,200 candidate event rows. It selected `panel-t003` only as a passive mechanics fixture and used `0.03000000` only to generate bounded sandbox cases.

## Prototype, safety, and monitoring evidence

The local sandbox contains 31 cases, 184 prefetch resources, 31 responses, and 61 trace events. All tests produce their declared expected behavior. Seventeen failures remain visible, including one silent failure detected through independent ledgers and one malformed-card accessibility defect blocked from release.

Module 06 retains 22 hazards, 20 monitoring measures, eight seeded scenarios, 12 human-owned escalation routes, and zero automatic actions. Monitoring thresholds are teaching triggers, not validated clinical control limits.

## Embedded ML evidence

The fixed challenger uses the same 7,544 rows, three predictors, weights, splits, threshold candidates, and alert budgets. Eight of 11 replacement rules pass. R03 fails with temporal-holdout AUC difference `-0.00743486`. R04 fails with transport-stress AUC difference `-0.01928938`. R08 fails with worst supported subgroup AUC degradation `0.10385240`. The transparent model remains retained.

## Leadership meaning

The evidence is complete enough to support a bounded curriculum defense. It is not complete enough to support a request for local silent-mode approval. The unresolved threshold, accessibility, local evidence, and governance conditions require revision first.
