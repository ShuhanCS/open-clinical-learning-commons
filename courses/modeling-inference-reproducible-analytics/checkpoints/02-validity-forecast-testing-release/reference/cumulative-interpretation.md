# Reference cumulative interpretation

## Decision and use boundary

The reference decision is `accept with conditions` for continued curriculum construction. The package shows that accepted prediction, validity, forecast, and agent-accountability evidence can enter Module 07 with its threats and use limits intact. It does not establish a real causal effect, individual or hospital performance, staffing or capacity utility, clinical safety, fairness, or deployment readiness.

## Preserved Checkpoint 1 identity

Checkpoint 1 remains version 0.1.0 with release SHA-256 `03c147d2e75cd446a43b9d56e49495df69af90d42d2b14ad4d860aea9d67239f`. Its 374-row cohort and 224/75/75 split are unchanged, with 25/7/4 positive outcomes. `ML01` and threshold 0.08513264 remain locked before test. The 75-row test set still yields 48 true negatives, 23 false positives, 2 false negatives, and 2 true positives from four outcomes. These facts are preserved under `prior-checkpoint/` and independently tested in Module 06.

## Aims, DAG, roles, and causal boundary

Module 04 keeps descriptive, predictive, causal, longitudinal, and survival aims separate in `modules/04-validity-adjustment-longitudinal/outputs/analytic-aim-validity-map.csv`. Its causal teaching fixture asks a different question from the 90-day prediction model. The visual `outputs/dag.svg`, structured `outputs/dag-nodes.csv` and `outputs/dag-edges.csv`, source `dag.mmd`, and `dag-narrative.md` encode equivalent roles.

Baseline age, severity, and prior utilization are treated as pre-exposure common causes in the treatment fixture. Mediators, colliders, post-outcome variables, and selection indicators are not included merely because they predict the outcome. Prediction features optimize a future-risk task; a causal adjustment set is selected for an estimand under a graph and assumptions. Neither set can be substituted for the other without a new rationale.

The causal-claim screen allows a bounded synthetic demonstration of adjustment behavior. It does not transport the known fixture ATE of -6.00000000 into a clinical claim.

## Overlap, balance, selection, and adjustment

The 600-row treatment fixture contains 255 treated rows and 91 missing severity values. The unadjusted contrast is -1.27214587, far from the known fixture ATE. The full-data IPTW audit is -6.10110832. Complete-case IPTW is -6.17942841, median-plus-indicator is -5.62153010, and the two delta readings are -5.62177960 and -5.62199963. These analyses preserve the same fixture target and population where declared; their differences expose assumption sensitivity rather than choose a clinically correct answer.

All weighted absolute standardized mean differences for the declared common causes are below 0.10. That supports a balance reading inside the fixture, but it does not prove exchangeability, correct graph structure, positivity outside the observed range, or absence of unmeasured confounding. `outputs/overlap-table.csv`, `outputs/balance-table.csv`, and `outputs/adjustment-estimates.csv` remain visible.

The Checkpoint 1 timing case has 111 selected rows and 263 structural blanks among 374 rows. Selection on a recorded next encounter changes the population. Those blanks remain blank, not zero, and the selected timing analysis supports no full-cohort time-to-event claim.

## Missingness, repeated measures, and survival

Missingness labels in `outputs/missingness-mechanisms.csv` are teaching scenarios, not verified real-world mechanisms. The package makes assumptions explicit and retains sensitivity readings. It does not claim that observed variables make the data missing at random.

The repeated fixture has 2,400 rows from 600 people and four visits per person. The ICC is 0.83598751, so row independence is untenable. The treatment-by-week reading is -0.23518501. `outputs/longitudinal-models.csv` and `outputs/mixed-variance.csv` distinguish naive, clustered, and mixed-model quantities rather than presenting one interchangeable estimate.

The survival fixture has 600 rows, 449 events, and 151 censored observations. The treatment hazard-ratio reading is 0.67945425 with interval 0.55144790 to 0.83717443. It is a conditional rate comparison in a synthetic fixture, not a risk ratio, constant treatment benefit, or recommendation. Unmet graph, dependence, censoring, proportional-hazards, or clinical-context needs route through `specialist-referrals.md`.

## Public source and forecast contract

Module 05 uses CDC's public Weekly Hospital Respiratory Data, NHSN dataset `rhwp-grxi`. The full all-jurisdiction file has 6,208 rows, 14 fields, 67 jurisdictions, and SHA-256 `8a492c3d2d3dae07c42e89ef35ed714d23acab32596f42037dcf8dd0284531d1`. The Massachusetts teaching series has 94 rows, 21 fields, dates 2024-11-09 through 2026-08-22, and SHA-256 `394d9b02d2cc9b4fbf0d9f415db3da6b04393dd9430816973e81fef86fb0e616`. Both full files are preserved under `public-data/`.

The target is weekly Massachusetts total respiratory new admissions, defined as the sum of COVID-19, influenza, and RSV new admissions. The unit is a jurisdiction-week aggregate across changing reporting hospitals, not one hospital. Five expanding windows end at week indexes 74, 78, 82, 86, and 90. Each forecasts the next four weeks. Together the test blocks cover weeks 75 through 94. Every fit stops at its origin and has zero future rows.

`LAST` retains the last observed value; `SNAIVE52` retains the 52-week seasonal value; `HOLT_DAMPED` is the eligible candidate; `ARIMA111` is a recognition example and is not eligible for selection. The naive models remain visible because they expose whether added complexity earns its place.

## Forecast results and failures

Across the same 20 targets and units, damped Holt has MAE 14.99587157 and RMSE 21.07855007. Last-value has MAE 28.20000000. Seasonal naive has MAE 93.15000000. Aggregate improvement is real within these folds, but it does not erase failure: in fold F04, damped-Holt MAE is 7.41230761 while last-value MAE is 1.00000000, and the candidate's worst absolute error is 58.96408576.

Level ADF p = 0.12535568 and first-difference ADF p = 0.00590799 are recognition readings, not proof of a stable generative process. Residual p-values are failure-to-reject results, not proof of independence. Supplied intervals are illustrative, not calibrated predictive distributions.

`outputs/reporting-coverage-context.csv` keeps changing hospital reporting visible. Coverage fields are context, not correction weights or admission denominators. Thus the forecast cannot support single-hospital process, causal, staffing, capacity, care, operational, or deployment claims. The accessible `outputs/forecast.svg`, forecast table, and `forecast-text-alternative.md` present equivalent core findings.

## Tests, failures, and independent checks

Module 06 preserves 13 accepted artifacts and runs 18 accepted data, leakage, model, metric, calibration, validity, forecast, and documentation tests. All pass in `modules/06-agent-assisted-modeling-testing/outputs/accepted-contract-tests.csv`.

Ten seeded failures reject with their intended codes: `LEAKAGE_FIELD`, `TEST_ROW_IN_FIT`, `LABEL_INVERTED`, `SPLIT_CHANGED`, `FUTURE_ROW_IN_FIT`, `CONFUSION_DENOMINATOR`, `CALIBRATION_BIN_OMITTED`, `FINGERPRINT_CHANGED`, `USE_BOUNDARY_MISSING`, and `AGENT_CLAIM_UNVERIFIED`. This shows that the test suite can detect its named failures; it does not prove that every possible error is covered.

Three independent standard-library checks recount 48/23/2/2 from 75 test predictions and recalculate candidate MAE 14.99587157 and RMSE 21.07855007 from 20 forecast rows. They verify arithmetic and row use, not utility.

## Agent trace and adjudication

The agent task plan, prompt constraints, prompt-trace log, critique, claim-adjudication table, and human ownership remain attached. Four claims are adjudicated. The bounded statement that damped Holt has lower aggregate MAE than both declared benchmarks is retained after independent calculation. The staffing-readiness claim is rejected. The residual-independence claim is modified. The leaked-model claim is rejected before performance comparison.

Agent output is assistance, not evidence. The source records, row-level outputs, deterministic checks, independent calculations, and accountable human disposition support the final text.

## Reproduction, accessibility, privacy, and integrity

The immutable manifest verifies 117 files by path, bytes, source unit, source version, and SHA-256. Reproduction and validator self-checks distinguish hash verification from recomputation. The reference includes equivalent text or tabular access for the DAG and forecast. Public aggregate and synthetic teaching data contain no patient-level direct identifiers. Personal paths, secrets, credentials, and undisclosed restricted data are prohibited.

## Conditions and progression

The reference is technically adequate and earns 25.00 of 25.00 with all 25 reference gates passing. Module 07 is permitted for curriculum construction. It must preserve all 117 immutable members, Checkpoint 1 test counts, causal and prediction distinction, structural blanks, missingness and dependence limits, both CDC fingerprints, all 94 ordered weeks, every benchmark and weak-fold result, reporting coverage, all accepted and failure tests, agent trace, independent checks, and the no-deployment boundary.

Named program review, paired R execution, live learner defense, and live learner/reviewer sign-off remain conditions before alpha. Any changed upstream fact returns to its owner; an unsupported clinical or operational claim stops progression.
