# Reference technical defense

- Learner: reference answer key, not a real learner
- Reviewer: reference technical review
- Date: 2026-08-30
- Status: `adequate`

## Questions and answers

1. Which validity threat most changes the prediction claim? Selection most directly changes the timing claim: only 111 of 374 rows have a recorded next encounter, while 263 values are structural blanks. A model for time among observed next encounters cannot be presented as a full-cohort time-to-event result. Evidence: `modules/04-validity-adjustment-longitudinal/outputs/selection-profile.csv` and `validity-adjustment-longitudinal-memo.md`.

2. How does the DAG adjustment set differ from prediction features? The adjustment set follows the causal estimand and blocks declared backdoor paths without conditioning on mediators, colliders, post-outcome fields, or selection by accident. Prediction features are chosen for information available at prediction time and may include variables useful for prediction that do not identify a causal effect. Evidence: Module 04 `dag-narrative.md`, `outputs/dag-nodes.csv`, and `causal-claim-screen.md`; prior-checkpoint model contract.

3. What do overlap and balance show, and what can they not establish? The overlap table shows where treated and untreated propensity ranges coexist. Weighted absolute SMDs below 0.10 show balance on declared measured common causes in the fixture. They do not prove the DAG, exchangeability, positivity outside observed data, or absence of unmeasured confounding. Evidence: Module 04 `outputs/overlap-table.csv` and `outputs/balance-table.csv`.

4. Which missingness assumption remains unverifiable? The missing-at-random teaching scenario cannot be verified from observed rows alone because dependence on unobserved severity or outcomes is not testable in the observed data. Sensitivity readings therefore remain conditions, not proof. Evidence: Module 04 `outputs/missingness-mechanisms.csv` and `outputs/adjustment-estimates.csv`.

5. How are repeated measures, clustering, or censoring handled? The 2,400 repeated rows are tied to 600 people, and ICC 0.83598751 rules out naive row independence; clustered and mixed readings are reported. The survival case preserves 449 events and 151 censored rows, with Kaplan-Meier and Cox readings plus referral conditions. Evidence: Module 04 `outputs/longitudinal-models.csv`, `outputs/mixed-variance.csv`, `outputs/kaplan-meier-table.csv`, and `outputs/cox-reading.csv`.

6. What are the forecast target, unit, horizon, and cutoff? The target is weekly Massachusetts total respiratory new admissions. The unit is a jurisdiction-week aggregate across reporting hospitals. Each fold has a four-week horizon and cuts fitting at origins 74, 78, 82, 86, or 90. Evidence: Module 05 `outputs/forecast-target.csv`, `outputs/temporal-folds.csv`, and `forecast-contract.json`.

7. Why is each naive benchmark retained? `LAST` tests whether the newest level is enough; `SNAIVE52` tests whether the same week one year earlier is enough. They are credible low-complexity alternatives and reveal that damped Holt loses fold F04 to last-value even while winning aggregate MAE. Evidence: Module 05 `outputs/benchmark-registry.csv`, `outputs/aggregate-metrics.csv`, and `outputs/fold-metrics.csv`.

8. Why is temporal validation used instead of random cross-validation? Forecasting occurs forward in time. Expanding windows preserve order and prevent future values from influencing earlier fits. Random folds would mix later reporting patterns into earlier training. Evidence: Module 05 `outputs/temporal-folds.csv` and `forecasting-temporal-validation-memo.md`.

9. How does reporting coverage change interpretation? Jurisdiction totals can change because the contributing hospitals change. Reporting counts and gaps are context, not denominators or correction weights. Therefore the series is not one stable hospital process and cannot justify staffing or capacity use. Evidence: Module 05 `outputs/reporting-coverage-context.csv` and `failure-and-referral.md`.

10. Which seeded failure is most consequential and why? `FUTURE_ROW_IN_FIT` is most consequential for the forecast because one future row can make evaluation look accurate while invalidating the deployment-time information boundary. `TEST_ROW_IN_FIT` is the parallel prediction failure. Evidence: Module 06 `outputs/seeded-failure-results.csv` and `outputs/failure-fixtures.json`.

11. Which agent claim was independently checked, and how? The claim that damped Holt has lower aggregate MAE than both benchmarks was checked by recalculating absolute errors from the 20 row-level candidate predictions. It reproduced 14.99587157, while accepted benchmark outputs are 28.20000000 and 93.15000000. Evidence: Module 06 `outputs/independent-verification.csv` and `outputs/claim-adjudication.csv`.

12. What must Module 07 preserve? It must preserve the 117 manifest members, Checkpoint 1 split and test counts, DAG and causal boundary, structural blanks, missingness and dependence limits, source fingerprints, 94 ordered weeks, temporal folds, benchmarks, weak-fold and coverage evidence, all tests and failures, agent trace, independent checks, human ownership, and the no-clinical/no-operational/no-deployment boundary. Evidence: `conditions-register.csv` and `progression-decision.md`.

## Follow-up and corrections

The reference clarifies that Gate 22 is complete only for the curriculum-construction disposition signed by the Commons sponsor. A live course run must supersede the reference sign-off with actual learner and reviewer sign-off. The answer key is adequate for technical construction; named panel review remains pending before alpha.
