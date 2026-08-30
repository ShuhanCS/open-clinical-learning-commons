# Final technical defense

- Status: `adequate`
- Reviewer: `curriculum-construction panel; live learner defense pending under C05`
- Date: `2026-08-30`
- Access route used: `accessible written reference response with exact evidence paths`

1. Decision, aim, target, prediction time, and horizon: The teaching decision is whether index-encounter information can estimate a synthetic adult's 90-day acute-return label at index-encounter stop. The package is a governed method example, not a clinical decision tool.
2. Modeling row grain: One row is one synthetic adult and their deterministic index encounter. There are 374 unique rows, not repeated encounters or person-time intervals.
3. Allowed and prohibited features and enforcement: Only pre-index and index-time predictors are allowed. Post-index next-encounter, outcome, endpoint, and follow-up fields are label or evaluation fields and are blocked by the feature-role registry, model contract, transformed-name record, and leakage tests.
4. Fixed temporal split and outcome counts: The split is time ordered and fixed before candidate comparison to preserve future-facing evaluation. It contains 224/75/75 rows and 25/7/4 positive outcomes in train/validation/test.
5. Baseline comparison: The candidate is compared with the training-prevalence baseline on the same fixed validation and test rows. The evidence does not support a deployment claim; the four-positive test set makes any apparent advantage fragile.
6. Discrimination, calibration, and threshold: ROC AUC 0.58802817 describes limited ranking, Brier 0.05097579 describes probability error in this low-prevalence test, and threshold 0.08513264 turns probabilities into labels. None answers the other question, and none establishes clinical utility.
7. Fragile counts and uncertainty: The test confusion is 48 TN, 23 FP, 2 FN, and 2 TP. Only four positives produce a ROC interval from 0.26760563 to 0.91549296, so the result is compatible with poor through apparently strong ranking.
8. Least supportable subgroup comparison: Five of ten subgroup rows are suppressed, so comparisons involving those rows are least supportable. Sparse outcomes and missingness make fairness or parity claims inappropriate.
9. Validity threat that most narrows the claim: Synthetic selection and outcome construction limit external validity most. The DAG and sensitivity evidence teach adjustment reasoning but cannot establish a causal or real-population effect.
10. Public forecast support and prohibition: The 94-week Massachusetts series supports time-ordered forecasting practice and benchmark comparison. Changing jurisdiction reporting and one last-value fold failure prohibit a stable-process or operational-capacity claim.
11. Most protective test or seeded failure: The prohibited-feature and test-contamination failures protect the release by rejecting post-index predictors and attempts to reuse held-out evidence for selection.
12. Agent contribution and independent check: An agent helped structure tests, evidence records, and claims. Three material results were recalculated independently from accepted files, and four claims were adjudicated with human ownership; agent text was not treated as evidence.
13. First monitoring trigger: Outcome-availability delay would trigger review first because unavailable or delayed labels make calibration, subgroup, and error monitoring uninterpretable. The data steward owns the check and can stop evaluation.
14. Rollback or immediate-stop event: Any leakage, wrong prediction time, changed label, restricted data, manifest mismatch, or missing safe fallback requires immediate stop. The fallback is no model or forecast action while owners are notified.
15. Why package acceptance and teaching-only model use can coexist: Package acceptance says the evidence is reproducible, accessible, and honestly governed. Teaching-only use says the evidence is too sparse and synthetic to support clinical or operational action. Those are intentionally different decisions.
