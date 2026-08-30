# Reference technical defense

- Learner: reference answer key, not a real learner
- Reviewer: reference technical review; named human review pending
- Date: 2026-08-30
- Status: `adequate`

## Questions and answers

1. What decision is the model intended to inform? It tests whether a synthetic 90-day acute-return prediction workflow is coherent enough for validity review, not whether care should change. Evidence: `modules/01-aims-reproducible-workspace/aim-and-method-plan.md` and `cumulative-interpretation.md`.

2. What is prediction time, outcome, and horizon? Prediction occurs at index-encounter stop; the outcome is an emergency or inpatient return within 90 days; the horizon is 90 days. Evidence: Module 01 plan, estimand registry, and feature-role contract.

3. Which fields are prohibited predictors and why? IDs, unsupported high-cardinality fields, post-index next-event fields, outcome fields, endpoint and follow-up fields, and split metadata are blocked because they are identifiers, unavailable at prediction time, derived from the outcome, or evaluation controls. Evidence: Module 01 `feature-role-contract.csv`.

4. How were the splits assigned and what are their positive counts? Rows are ordered by index start and patient ID, then assigned 224 training, 75 validation, and 75 test rows with 25, 7, and 4 outcomes. Evidence: Module 01 `outputs/split-registry.csv` and `outputs/build-report.json`.

5. What baseline must the candidate beat? The retained comparator is the training prevalence, 25/224 = 0.111607142857. Candidate selection requires Brier no worse than baseline, ROC AUC at least 0.55, and average precision no worse than baseline. Evidence: Module 01 baseline and Module 03 model-selection record.

6. What does one linear or logistic coefficient mean? In `LOG01`, the prior-acute coefficient exponentiates to a conditional odds ratio of 2.20423495 per one-count increase while holding centered age and index class fixed. It is not a risk ratio, probability multiplier, or causal effect. Evidence: Module 02 logistic coefficients and interpretation.

7. Which regression condition matters most? The linear case is conditional on a recorded next encounter: 69 training rows are fit within 111 available timing rows while 263 structural blanks remain blank. Influence, residual normality, extreme probabilities, sparse cells, and pending R reconciliation also remain conditions. Evidence: Module 02 assumption register and diagnostics.

8. How did validation select and lock model and threshold? `ML01` alone passes the frozen three-part validation rule. The threshold is chosen from validation probabilities to detect at least 5 of 7 outcomes, minimize false positives, and choose the highest tie, producing 0.08513264 before test. Evidence: Module 03 selection and threshold records.

9. What do discrimination and calibration each add? ROC AUC and average precision describe ranking; Brier and log loss describe probability error; calibration groups compare predicted probability with observed frequency. None alone establishes threshold utility. Four test outcomes make all calibration conclusions unstable. Evidence: Module 03 test metrics and calibration table.

10. What exact test counts support threshold metrics? There are 48 TN, 23 FP, 2 FN, and 2 TP among 75 rows with 4 outcomes. Thus sensitivity is 2/4, specificity 48/71, PPV 2/25, and NPV 48/50. Evidence: Module 03 confusion table.

11. Why are subgroup conclusions limited? Five of ten subgroup rows are suppressed, and even unsuppressed rows contain few outcomes. The package provides descriptive counts but cannot rank groups or establish fairness. Evidence: Module 03 subgroup metrics.

12. What would force revision before Module 04? A changed source, aim, population, prediction time, outcome, split, formula, feature set, selection rule, threshold, test-use rule, missing immutable artifact, failed gate, inadequate defense, or unsupported claim forces return to the owning module or checkpoint. Evidence: checkpoint contract and progression decision.

## Follow-up and corrections

The normalized course rubric was corrected from H01 = 1.50 to H01 = 2.50 because the displayed 40-point rubric otherwise summed to 39. The correction preserves the declared 15/10/15 component shares. No module evidence changed.

Final technical note: the reference answer key is adequate for runnable curriculum construction. A real learner defense and named human reviewer decisions remain required before alpha.
