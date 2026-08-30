# Reference technical defense

- Learner: reference answer key, not a real learner
- Reviewer: reference technical review
- Date: 2026-08-30
- Status: `adequate`

1. What decision, aim, target, prediction time, and horizon define the work? The package asks whether a reproducible synthetic prediction workflow is governable for teaching. It predicts emergency or inpatient return within 90 days at index-encounter stop, not treatment effect or operational action. Evidence: `model-card.md` and evidence index E02.
2. What does one modeling row represent, and which features are prohibited? One row is one synthetic adult's accepted index encounter. IDs, outcomes, post-index and future fields, follow-up fields, split metadata, and unsupported high-cardinality fields are prohibited. Evidence: E02 and the nested Module 03 model contract.
3. What baseline and exact test evidence support the selected model? Training prevalence is 25/224 = 0.111607142857. Validation selected `ML01`; untouched test has 75 rows, four outcomes, and 48/23/2/2 confusion. Evidence: `performance-appendix.csv`.
4. What do discrimination, calibration, and threshold consequences each say? ROC AUC 0.58802817 concerns ranking with a wide interval; Brier 0.05097579 concerns probability error versus 0.05388473 baseline; threshold 0.08513264 yields 23 false positives and two true positives. None establishes utility. Evidence: performance appendix.
5. Why are subgroup and equity conclusions limited? Five of ten group rows are suppressed and remaining rows have sparse outcomes. Missing metrics are not zero. Evidence: `subgroup-equity-review.md`.
6. Which validity and forecast limits most narrow the claim? Prediction is not causal; the 111-row timing subset is selected with 263 structural blanks; missingness assumptions remain assumptions; the forecast is a changing-reporting jurisdiction aggregate and loses a fold to last-value. Evidence: E04 and E05.
7. Which test or seeded failure most protects the release? `TEST_ROW_IN_FIT` protects the untouched prediction test and `FUTURE_ROW_IN_FIT` protects forecast time order. Both reject for intended codes. Evidence: E06.
8. Which monitoring signal would trigger review first, with what denominator? S01 checks every input field and source file on every simulated run. Any changed fingerprint or prohibited field stops immediately before scoring. Evidence: `monitoring-plan.csv`.
9. What requires retraining, rollback, immediate stop, retirement, and a new version? Retraining needs new justified data and evaluation with approval; any retraining creates a new version. Identity drift, leakage, failed tests, prohibited data or claims stop immediately. Rollback must be to a still-valid accepted version; otherwise fallback is no model. Retirement follows ended purpose or unresolved evidence. Evidence: lifecycle records.
10. What did the agent contribute, who checked it, and why do package disposition and model use differ? Codex assisted construction. Row-level checks retained one bounded forecast claim and rejected or narrowed three claims. Shuhan He owns construction. The package can be complete while sparse synthetic evidence limits use to teaching. Evidence: `ai-use.md`, `human-sign-off.md`, and `model-use-recommendation.md`.

## Follow-up

The answer key is technically adequate. Actual learner reasoning, named panel review, independent reproduction, and final-checkpoint defense remain required before alpha.
