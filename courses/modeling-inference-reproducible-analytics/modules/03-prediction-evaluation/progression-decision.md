# Reference Checkpoint 1 progression recommendation

## Recommendation

`continue to validity review with conditions`

## Accepted handoff

- The Module 01 aim, field roles, 374-row cohort, 224/75/75 temporal split, and baseline are unchanged.
- The Module 02 formula, matrix, and assumption records are fingerprinted and preserved.
- Preprocessing and model fitting used training rows only.
- `ML01` is the only eligible model that passes the declared validation rule.
- `LEAK01` is rejected before performance review.
- The threshold 0.08513264 was selected on validation and locked before test.
- All 75 test predictions, four outcomes, exact confusion counts, calibration groups, and subgroup suppression decisions are preserved.
- The evidence is reproducible under the pinned teaching environment.

## Conditions

1. Preserve the one-time test result: 48 TN, 23 FP, 2 FN, and 2 TP.
2. Keep the four test outcomes and wide uncertainty visible.
3. Do not treat the high NPV as evidence of safety.
4. Do not treat selected predictive features as causal adjustment variables.
5. Keep suppressed subgroup metrics suppressed and make no fairness ranking.
6. Retain exact table alternatives for both figures.
7. Make no real-clinical, operational, or deployment claim.
8. Module 04 must review validity threats before any broader model-use recommendation.

## Return conditions

A changed aim, population, timing, outcome, horizon, field role, split, formula, feature set, preprocessing step, candidate, selection rule, threshold rule, metric, resampling rule, subgroup rule, or test-use policy returns to the owning module and requires a semantic-version decision.
