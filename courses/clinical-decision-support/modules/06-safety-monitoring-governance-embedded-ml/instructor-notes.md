# Instructor notes

## Teaching purpose

This module asks learners to make failure evidence useful without erasing it. The safety block begins with the seeded sandbox failures and ends with named controls, monitoring, escalation, fallback, stop, restart, and retirement. The ML block asks whether a more flexible model earns replacement under rules fixed before evaluation.

Do not reveal the challenger results until learners have frozen the model settings and 11 replacement rules. Ask which result would change the recommendation, then apply every rule rather than choosing the most favorable metric.

## Suggested facilitation

1. Assign the 17 inherited failure modes across groups. Each group must define consequence, detection, control, owner, escalation, fallback, stop, restart, and retirement.
2. Reconcile the groups into one safety case. Missing ownership or an unavailable detection source blocks release.
3. Trace M09 across the four independent ledgers. A service log alone cannot detect the seeded silent failure.
4. Test each of the eight monitoring scenarios. Every response is human owned and no row creates an automatic action.
5. Freeze `ml-contract.json`, then run the challenger once.
6. Compare development, temporal holdout, and transport results. Discuss why better development AUC does not answer the replacement question.
7. Apply R03, R04, and R08 last. The class should see the Brier and calibration gains before the discrimination and subgroup failures.
8. Defend the Week 6 disposition without selecting a threshold or excusing a prototype defect.

## Expected reference discussion

- All 22 hazards have controls and life-cycle rules.
- All 20 measures name a cadence, owner, threshold origin, unavailable state, and human action.
- The fixed challenger passes 8 of 11 replacement rules and fails holdout discrimination, stress discrimination, and the supported subgroup rule.
- The transparent model remains accepted for the comparison. `0.03000000` remains an unaccepted sandbox fixture.
- The 25 Module 04 points are carried once. Module 06 adds no points and all 22 gates remain required.
- Progression is `continue with conditions` to the cumulative Week 6 checkpoint.

Joe Joseph, MD, leads the clinician leadership block after the Week 6 checkpoint is frozen. Module 07 must use this exact safety and model decision without rewriting the evidence.
