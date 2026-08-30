# FND-2 Module 05: Forecasting and temporal validation

## 1. Module identity and place in the course

### Release identity

- Course: FND-2, Modeling, Inference, and Reproducible Analytics.
- Course role: second straight-through technical foundation.
- Module: 05 of 07.
- Source week: 5.
- Learner work: 16.0 hours.
- Module ID: `oclc-fnd2-05`.
- Module version: 0.1.0.
- Commons release target: 0.44.0.
- Week 6 assessment share: 10 of 25 course points.
- Prerequisite: accepted Module 04 version 0.1.0 and its conditions.

### Purpose

Module 05 teaches a learner to forecast a public weekly healthcare series without allowing the future to train the past. The learner defines the target, horizon, cutoff, refresh cadence, decision, and minimum benchmarks before fitting; backtests all eligible methods on identical expanding-window folds; reads error and interval evidence in source units; and refuses operational claims that a short changing-reporting aggregate cannot support.

### Relationship to Module 04

Module 04 establishes that model validity depends on aim, timing, selection, missingness, dependence, censoring, and supported scope. Module 05 applies that habit to a new data shape. It does not carry a treatment effect or person-level prediction into forecasting. It receives only the accepted validity conditions, threat register, provenance, and progression permission.

### Relationship to Module 06

Module 06 tests the exact prediction and forecasting pipelines, expected failures, source fingerprints, and responsible-agent records. It may not silently change the Module 05 folds, methods, outputs, or recommendation.

### Required starting state

- all 6,208 public CDC NHSN jurisdiction-week rows match their accepted fingerprint;
- all 94 Massachusetts weeks match their accepted fingerprint;
- Module 04 release, progression decision, and threat register match exact fingerprints;
- the target reconciles to COVID-19, influenza, and RSV counts; and
- dates remain unique, ordered, and seven days apart.

### Required ending state

- one exact forecast contract;
- five expanding-window folds;
- three eligible model routes evaluated on 20 common targets;
- one ARIMA-family recognition route kept outside selection;
- fold, horizon, aggregate, residual, interval, failure, and reporting-context evidence;
- an accessible forecast display with exact table and text route;
- a 10-point assessment and gates;
- a Module 06 progression decision; and
- a reproducible learner workspace.

## 2. Decision, owner, audience, and dispositions

### Decision owner

The decision owner is a healthcare forecasting and operations-methods reviewer. A time-series specialist, public-health surveillance expert, clinical operations leader, data steward, accessibility reviewer, responsible-AI reviewer, and independent instructor may be consulted.

### Decision

Does the introductory damped-trend forecast improve on both declared temporal benchmarks across the exact rolling-origin backtest, what failures remain, and what use does this public aggregate not support?

### Allowed dispositions

1. `continue to Module 06 with conditions`;
2. `revise Module 05`;
3. `refer forecasting design`; or
4. `stop`.

### Reference disposition

The reference is `continue to Module 06 with conditions`. `HOLT_DAMPED` has the best aggregate MAE and RMSE on the frozen folds, but it loses to last-value in one low-count fold, nearly ties it in another, has very wide illustrative intervals, and uses a public jurisdiction aggregate with changing reporting coverage. It supports teaching and testing, not staffing, capacity, care, or deployment.

### Audiences

- learner producing the evidence;
- instructor teaching temporal reasoning;
- reviewer scoring the 10-point share;
- Module 06 learner testing accepted behavior;
- source steward checking provenance; and
- operations or time-series specialist receiving a referral.

### What this decision does not approve

- single-hospital demand prediction;
- staffing or bed-capacity action;
- clinical-care forecasting;
- causal attribution of trend or seasonality;
- correction for changing reporters;
- deployment or automated refresh;
- an ARIMA model-selection claim; or
- future performance beyond the released source period.

## 3. Foundation skill and claim hierarchy

### Foundation skill

The learner can build and defend a small time-ordered forecast comparison whose target, information cutoff, folds, benchmarks, errors, source limitations, and stopping conditions are explicit.

### Claim hierarchy

1. Source fact: the release contains 94 consecutive Massachusetts jurisdiction-weeks.
2. Derived fact: total respiratory admissions equal three reported components in every week.
3. Backtest fact: each model predicts the same 20 later weeks from earlier data only.
4. Comparative fact: damped Holt has lower aggregate MAE and RMSE on these folds.
5. Limited recommendation: retain the candidate for Module 06 testing with conditions.
6. Prohibited leap: use the candidate for real operations or claim stable future accuracy.

### Stop principle

If target meaning, week order, fold timing, source identity, reporter context, common test rows, or error denominators cannot be defended, comparison stops before model complexity increases.

### Forecast versus explanation

A pattern that helps prediction does not explain the causes of admissions. Decomposition, lag behavior, or trend cannot establish an intervention, seasonal mechanism, reporting effect, or biological cause.

### Specialist boundary

ARIMA-family fitting is recognition. Production-grade probabilistic forecasting, hierarchy reconciliation, exogenous covariates, count distributions, structural breaks, ensemble design, and operational decision analysis require specialist work.

## 4. Assessable outcomes and evidence map

### Outcomes

By the end, a learner can:

1. name the forecast unit and target;
2. define information cutoff and four-week horizon;
3. preserve all 94 source weeks;
4. explain why random splitting fails;
5. construct five expanding-window folds;
6. prove zero future rows entered a fit;
7. define last-value before comparison;
8. define 52-week seasonal-naive eligibility;
9. fit damped Holt inside each fold;
10. read fitted smoothing parameters;
11. calculate MAE and RMSE in admission counts;
12. interpret signed bias;
13. explain MAPE instability at small denominators;
14. compare fold-specific failures;
15. compare error by horizon;
16. read an illustrative interval without calling it calibrated;
17. describe a training-only decomposition;
18. read level and differenced stationarity diagnostics;
19. read supplied ARIMA parameters and residual checks;
20. use reporting coverage as context only;
21. distinguish aggregate backtest performance from operational utility;
22. make a supported progression disposition; and
23. reproduce the package without overwrite.

### Evidence map

| Outcome group | Evidence |
|---|---|
| Target and use | `forecast-target.csv`, `forecast-contract.json`, memo |
| Time order | `temporal-folds.csv`, predictions, checks |
| Benchmarks | `benchmark-registry.csv`, exact predictions |
| Candidate | `holt-parameters.csv`, fold and aggregate metrics |
| Uncertainty | interval reading, horizon metrics, failure analysis |
| Time-series recognition | decomposition, stationarity, ARIMA, residual tables |
| Source context | full-release and Massachusetts fingerprints, coverage table |
| Access | SVG, exact CSV, text alternative |
| Accountability | reproduction, AI-use, progression records |

### Minimum explanation

Every conclusion names model, fold or aggregation level, horizon, metric, unit, comparison, and limit. "Better forecast" without those qualifiers fails.

## 5. Concept ownership and out-of-scope boundaries

### Module 05 owns

- forecast aim and horizon;
- temporal cutoff;
- expanding-window backtesting;
- non-overlapping test folds;
- last-value benchmark;
- seasonal-naive benchmark;
- guided damped Holt candidate;
- fold refitting;
- MAE, RMSE, signed bias, and MAPE boundary;
- horizon and fold failure analysis;
- illustrative interval reading;
- training-only decomposition;
- ADF and ARIMA recognition;
- residual autocorrelation recognition;
- reporting-coverage context;
- forecast display accessibility; and
- Module 06 handoff.

### Module 05 introduces but does not own

- forecast-distribution calibration;
- state-space uncertainty;
- count time-series models;
- external regressors;
- structural breaks;
- hierarchical forecasts;
- ensembles;
- probabilistic scoring;
- intervention analysis; and
- production monitoring.

### Module 05 does not own

- person-level prediction;
- causal adjustment;
- clinical intervention effects;
- hospital staffing policy;
- capacity thresholds;
- real-time data engineering;
- source correction;
- autonomous deployment; or
- model-card governance, which belongs to Module 07.

### No complexity theater

The release uses two essential baselines and one guided candidate. ARIMA appears only as a supplied reading. More models are not added merely to make the exercise look advanced.

## 6. Lesson sequence and learner time

| Lesson | Focus | Guided activity | Independent evidence | Hours |
|---|---|---|---|---:|
| 05.1 | Target and cutoff | define unit, target, horizon, use | forecast contract | 1.5 |
| 05.2 | Time order | draw fold boundaries | temporal registry | 2.0 |
| 05.3 | Benchmarks | hand-calculate one fold | benchmark defense | 2.0 |
| 05.4 | Damped smoothing | fit within folds | parameters and predictions | 2.5 |
| 05.5 | Error evidence | compute MAE, RMSE, bias, MAPE | fold and aggregate comparison | 2.0 |
| 05.6 | Failure and coverage | inspect misses and reporter context | failure analysis | 1.5 |
| 05.7 | Decomposition and stationarity | read supplied tables | quantity defense | 1.5 |
| 05.8 | ARIMA recognition | read parameters, intervals, residual checks | recognition record | 1.0 |
| 05.9 | Recommendation and defense | synthesize limits | memo, review, progression | 2.0 |
| Total | | | | 16.0 |

### Within-module gates

- Target gate before folds.
- Fold gate before fitting.
- Benchmark gate before candidate comparison.
- Common-target gate before metric aggregation.
- Quantity gate before recommendation.
- Source-and-use boundary before progression.

## 7. Source, rights, and release architecture

### Authoritative public source

- Publisher: Centers for Disease Control and Prevention.
- System: National Healthcare Safety Network.
- Dataset: Weekly Hospital Respiratory Data, HRD Metrics by Jurisdiction.
- Dataset ID: `rhwp-grxi`.
- Landing page: https://data.cdc.gov/Public-Health-Surveillance/Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/rhwp-grxi
- Selected period: 2024-11-09 through 2026-08-22.
- Retrieval date: 2026-08-29.
- Access: public aggregate surveillance data.

### Reused Commons releases

| Release | Rows | Fields | SHA-256 |
|---|---:|---:|---|
| All jurisdictions | 6,208 | 14 | `8a492c3d2d3dae07c42e89ef35ed714d23acab32596f42037dcf8dd0284531d1` |
| Massachusetts | 94 | 21 | `394d9b02d2cc9b4fbf0d9f415db3da6b04393dd9430816973e81fef86fb0e616` |

The source values are reused, not downloaded again or copied into a divergent release. The learner workspace receives exact fingerprinted copies.

### Module 04 handoff

The builder verifies Module 04 release, progression decision, and 12-row threat register. This proves the module started from the accepted validity decision without changing it.

### Rights

The source is United States government public-health surveillance data. Source terms remain at https://data.cdc.gov/. Commons documentation uses CC BY 4.0 and code uses MIT under the repository license plan.

### Privacy

Rows are jurisdiction-week aggregates across reporting hospitals. There are no patient records, direct identifiers, or single-hospital observations.

## 8. Forecast target and horizon contract

### Unit

One row is one Massachusetts jurisdiction-week aggregate across the hospitals contributing to the public report.

### Target

`total_respiratory_new_admissions` is the sum of reported confirmed COVID-19, influenza, and RSV new admissions for the week. The builder reconciles the three components for all 94 rows.

### Information cutoff

For a fold with training end index `t`, only rows 1 through `t` may initialize, optimize, fit, diagnose, or forecast that fold. Rows `t+1` through `t+4` are test evidence only.

### Horizon

Each origin predicts the next four weekly targets. Horizon-specific errors remain visible. A four-week exercise does not establish performance at longer horizons.

### Refresh cadence

The teaching contract describes a weekly refresh only after source verification and versioning. This release does not implement automated ingestion.

### Decision

Compare introductory methods and decide whether the exact pipeline should enter Module 06 testing. No operational decision is made from the forecast.

## 9. Temporal folds and leakage prevention

### Frozen fold registry

| Fold | Training weeks | Cutoff | Test weeks | Test dates |
|---|---:|---|---:|---|
| F01 | 1-74 | 2026-04-04 | 75-78 | 2026-04-11 to 2026-05-02 |
| F02 | 1-78 | 2026-05-02 | 79-82 | 2026-05-09 to 2026-05-30 |
| F03 | 1-82 | 2026-05-30 | 83-86 | 2026-06-06 to 2026-06-27 |
| F04 | 1-86 | 2026-06-27 | 87-90 | 2026-07-04 to 2026-07-25 |
| F05 | 1-90 | 2026-07-25 | 91-94 | 2026-08-01 to 2026-08-22 |

### Why these folds

Five non-overlapping four-week test blocks use the final 20 source weeks. The first origin retains 74 training weeks, so every target has 52-week benchmark history. Expanding windows match a method refit as more verified public weeks arrive.

### Leakage controls

- fold dates are declared before candidate comparison;
- all methods use identical test rows;
- every parameter fit occurs inside the fold training range;
- decomposition uses only final-origin training rows 1-90;
- ARIMA recognition fits rows 1-90 and reads weeks 91-94;
- source weeks are never shuffled;
- errors never tune an earlier prediction; and
- the validator reconstructs every value.

### No hidden holdout claim

The final four weeks are part of a repeated backtest design, not a permanently untouched deployment test. The language must not copy person-level train-validation-test claims from Module 03.

## 10. Benchmark and candidate contract

### LAST

`LAST` repeats the final observed training value for all four horizons. It is the minimum persistence benchmark.

### SNAIVE52

`SNAIVE52` uses the target exactly 52 weeks before each forecasted week. It is eligible because all 20 targets have lag-52 history available before their origins. It is not assumed to win merely because respiratory admissions are seasonal.

### HOLT_DAMPED

`HOLT_DAMPED` is the sole guided candidate. It uses additive level and damped trend, estimated separately inside each fold with statsmodels. The release retains smoothing level, smoothing trend, damping, initial level, initial trend, and SSE for each fit.

### Selection rule

The candidate may continue only if its aggregate MAE is lower than both eligible benchmarks, its aggregate RMSE is lower than both, all common-target and timing checks pass, and its failure evidence supports a bounded teaching recommendation. There is no requirement that it win every fold.

### ARIMA exclusion

`ARIMA111` is fit once at the final origin as a recognition example. It is ineligible for selection because the course specifies recognition, not guided ARIMA model search. Its wide interval output is retained, not used to choose it or reject another candidate.

## 11. Error metrics, denominators, and comparison

### Primary metrics

- MAE: mean absolute error in reported admissions per week.
- RMSE: root mean squared error in the same source unit.
- Bias: mean actual minus prediction; positive means average underprediction.

### Percentage metric

MAPE is reported for teaching but is not primary. Actual targets range from 13 to 182 in the backtest. A small denominator can make percentage error look extreme even when the absolute miss is modest. Zero actuals would make ordinary MAPE undefined; no zero occurs in these 20 targets.

### Aggregate reference

| Model | MAE | RMSE | Bias actual minus prediction | MAPE |
|---|---:|---:|---:|---:|
| HOLT_DAMPED | 14.99587157 | 21.07855007 | -5.97261489 | 46.93627714% |
| LAST | 28.20000000 | 39.44363066 | -22.50000000 | 71.00841979% |
| SNAIVE52 | 93.15000000 | 96.43002644 | -93.15000000 | 352.83355181% |

### Interpretation

Actual minus prediction is negative for all three aggregate biases, so each overpredicts on average across a steep seasonal decline. The candidate reduces, but does not eliminate, that behavior.

## 12. Fold, horizon, and failure evidence

### Fold behavior

The candidate has MAE 11.30390302 in F01, 37.05756050 in F02, 6.47452320 in F03, 7.41230761 in F04, and 12.73106354 in F05. It loses to `LAST` in F04, where last-value MAE is 1.00000000, and narrowly wins F05, where last-value MAE is 13.25000000.

### Worst misses

- `LAST`: 86.00000000 admissions on 2026-05-23.
- `SNAIVE52`: 133.00000000 admissions on 2026-06-13.
- `HOLT_DAMPED`: 58.96408576 admissions on 2026-05-23.

### Direction counts

- `LAST`: seven underpredictions, 12 overpredictions, one exact.
- `SNAIVE52`: zero underpredictions and 20 overpredictions.
- `HOLT_DAMPED`: 11 underpredictions and nine overpredictions.

### Meaning

Aggregate victory does not erase regime-specific weakness. The series moves from high winter admissions through a rapid decline to a low-count turn. A reviewer must see fold and horizon tables before accepting the aggregate recommendation.

## 13. Intervals and uncertainty recognition

### Supplied interval

The damped-Holt reading uses the fitted training residual RMSE multiplied by 1.96 and square root of horizon, truncated below at zero. This is a transparent teaching calculation, not a calibrated forecast distribution.

### Reference behavior

Intervals are very wide because training residual variability includes the large seasonal wave and because a small trend model is misspecified for the full series. At final origin, the four upper readings exceed 306, 427, 520, and 598 admissions while point predictions remain near 15.

### Required interpretation

Wide intervals are evidence against confident operational use, not a reason to hide uncertainty. Interval coverage in 20 backtest targets is descriptive and cannot prove future calibration.

### Prohibited interpretation

- do not call the interval a clinical confidence interval;
- do not call 95% a guaranteed future coverage rate;
- do not narrow it manually;
- do not use negative lower values, which are truncated for the nonnegative target; and
- do not equate point-forecast ranking with probabilistic adequacy.

## 14. Decomposition, stationarity, ARIMA, and residual recognition

### Decomposition

`decomposition-reading.csv` contains the 90 final-origin training weeks, a centered 13-week trend where available, and observed-minus-trend remainder. Centering is allowed for post-fit description inside the training range; it is not an online feature and never crosses into weeks 91-94.

### Stationarity

The level-series ADF statistic is -2.46060654 with p-value 0.12535568. The first-difference statistic is -3.59240055 with p-value 0.00590799. Learners read these as diagnostics under assumptions, not as mechanical proof or a complete model-selection rule.

### ARIMA-family reading

The supplied final-origin example is ARIMA(1,1,1) with drift. It exposes drift, autoregressive, moving-average, and innovation-variance estimates plus four forecasts and model intervals. It is not optimized across alternative orders and is not eligible in the candidate comparison.

### Residual check

The supplied Ljung-Box p-values are 0.35732989 at lag 4 and 0.32516289 at lag 8. These do not prove white noise, stationarity, good forecasting, or operational adequacy. They are one bounded residual-autocorrelation reading.

## 15. Reporting coverage and public-source limits

### Coverage evidence

Each of the 20 target rows retains the number and percent of hospitals reporting occupancy plus `reporting_gap_pct`. The percentages provide context about a changing reporting aggregate.

### No invented correction

Reporting coverage is not a denominator for respiratory admissions in this release. The module does not divide counts by occupancy reporting percentage, weight errors, impute absent hospitals, or claim a fixed hospital cohort.

### Source behavior

- Massachusetts is a jurisdiction aggregate.
- Hospital participation may change over time.
- Reporting context may move independently of true underlying admissions.
- The source began in November 2024 for this release.
- Only 94 weeks are available.
- The released values are preserved even when inconvenient for a forecast.

### Decision boundary

The backtest compares methods on exactly what was publicly reported. It does not estimate a complete Massachusetts burden, hospital demand, population rate, or staffing need.

## 16. Exact learner deliverables and package contract

### Required core files

- `README.md`;
- `VERSION`;
- `requirements.txt`;
- `source-record.yml`;
- `data-spec.md`;
- `forecast-contract.json`;
- `assessment.md`;
- deterministic builder;
- independent validator;
- release metadata; and
- learner template.

### Required decision files

- `forecasting-temporal-validation-memo.md`;
- `benchmark-defense.md`;
- `arima-reading.md`;
- `forecast-text-alternative.md`;
- `failure-and-referral.md`;
- `reproducibility-check.md`;
- `accessibility-review.md`;
- `ai-use.md`; and
- `progression-decision.md`.

### Required generated evidence

- forecast target;
- temporal folds;
- benchmark registry;
- 60 exact eligible-method predictions;
- five candidate parameter rows;
- 20 candidate interval readings;
- three aggregate metric rows;
- 15 fold metric rows;
- 12 horizon metric rows;
- three failure rows;
- 20 reporting-coverage rows;
- 90 decomposition rows;
- two stationarity rows;
- four ARIMA parameter rows;
- four ARIMA forecast rows;
- two residual diagnostic rows;
- 20 invariant checks;
- accessible forecast SVG; and
- build report.

### No screenshot-only evidence

The SVG is redundant. Every exact plotted value is in `forecast-predictions.csv`; the title and description are embedded; and the learner writes a structured text alternative.

### Portable build

The learner workspace contains exact copies of the 6,208-row source release, 94-row Massachusetts series, Module 04 handoff, builder, validator, prompts, and outputs. It rebuilds into a new target and refuses overwrite.

## 17. Assessment, rubric, and noncompensable gates

### Ten-point Week 6 share

| Criterion | Points |
|---|---:|
| Forecast aim, target, horizon, cutoff, and time-ordered folds | 2.00 |
| Naive benchmarks and exact fold-level predictions | 2.00 |
| Guided model, error metrics, residuals, and comparison | 2.50 |
| Reporting coverage, failure analysis, limits, and recommendation | 2.00 |
| Accessible evidence, reproduction, and responsible agent record | 1.50 |
| Total | 10.00 |

The minimum numeric score is 8.00 of 10.00. Every gate must pass.

### Gates

1. Exact full-source fingerprint.
2. Exact Massachusetts fingerprint.
3. All 94 weeks retained in order.
4. Target reconciles to three source counts.
5. Future rows excluded from every fit.
6. Benchmark eligibility declared before comparison.
7. Candidate compared on identical folds and targets.
8. Errors retain source units and valid denominators.
9. No source values or misses manually revised.
10. Reporting coverage remains context only.
11. No single-hospital, stable-process, staffing, capacity, clinical, or deployment claim.
12. Accessible exact table accompanies display.
13. ARIMA remains recognition.
14. Explicit Module 06 progression disposition.

### Automatic return

- changed source or week order;
- random split;
- overlapping training and test rows;
- unavailable lag-52 prediction disguised as zero;
- candidate trained once on all 94 weeks for backtesting;
- benchmark omitted after seeing results;
- metric computed on different targets;
- MAPE used without denominator discussion;
- reporting percentage used as an invented weight;
- interval called calibrated without evidence;
- ARIMA promoted through an undeclared search;
- inaccessible plot;
- unresolved learner prompt; or
- unsupported operational claim.

## 18. Feedback, revision, recovery, and support

### Feedback order

1. target and use;
2. cutoff and folds;
3. benchmarks;
4. candidate fit boundary;
5. metrics and denominators;
6. failures and intervals;
7. source context;
8. claim boundary;
9. reproduction and access;
10. prose.

### Revision examples

| Defect | Response |
|---|---|
| Random split | rebuild temporal folds |
| Candidate sees future | stop and rebuild every affected fit |
| Seasonal-naive starts without 52 weeks | mark ineligible or move origins |
| Aggregate hides fold loss | restore fold and horizon evidence |
| MAPE dominates at low counts | return to source-unit metrics |
| Interval is manually narrowed | restore declared calculation and limitation |
| Coverage used as correction | remove correction and treat it as context |
| ARIMA order search is hidden | return to recognition or version expanded mastery |
| Staffing claim appears | stop and refer operations design |

### Supported route

The pinned Python environment runs the exact builder and validator. Learners may use structured CSV evidence without rendering SVG. The exercise requires no live API access because the public releases are already fingerprinted.

### Accessibility route

Exact tables and Markdown are primary. The SVG is a supplemental display with title, description, high contrast, and a text equivalent.

### Extension

An extension may deepen one declared failure or compare a specialist-approved method on the same frozen folds. It may not change folds or target after seeing results without a new version.

## 19. Responsible AI, privacy, accessibility, and integrity

### AI may assist

- check fold code;
- explain forecast vocabulary;
- compare exact tables;
- draft a text alternative;
- classify residual failures;
- format a disclosure; and
- suggest test cases.

### AI may not own

- forecast target;
- operational use;
- benchmark eligibility;
- source correction;
- metric interpretation;
- interval calibration claim;
- specialist referral;
- score; or
- progression decision.

### Required AI-use record

Record tool, task, data shared, output retained, independent check, correction, and accountable human. Public aggregate data may be shared, but source identity and limits remain required.

### Privacy

No patient or single-hospital record exists. Learners may not add local patient or hospital-confidential data to the release.

### Accessibility

- tables use labeled fields and source units;
- color is not the only series identifier;
- the SVG embeds title and description;
- exact values are available without a graphic;
- headings preserve navigation; and
- percentage fields retain the percent sign in prose.

### Integrity traps

- modifying a miss to improve a metric;
- choosing folds after performance review;
- hiding a losing fold;
- using future source data in decomposition or fit;
- reporting model output without source-unit meaning;
- treating an agent recommendation as human approval; and
- claiming the public aggregate represents a stable hospital system.

## 20. Validation and acceptance tests

### Builder self-check

The builder must:

- verify five upstream fingerprints;
- verify 6,208 and 94 source rows;
- verify 67 jurisdictions through the accepted source release record;
- reconcile the target;
- preserve 93 seven-day gaps;
- generate five folds and 20 targets;
- refit every candidate fold;
- generate exactly 60 eligible-method predictions;
- verify zero future rows in fit;
- reproduce all outputs from a copied learner workspace;
- refuse an existing target; and
- pass all 20 invariant checks.

### Validator self-check

The validator must:

- require every release and learner file;
- rebuild every output independently;
- compare field order, row counts, and exact values;
- compare SVG bytes and build report;
- verify source fingerprints;
- verify exact fold and model facts;
- reject unresolved prompts;
- reject a missing prediction table;
- verify release metadata and output fingerprints; and
- report separate release and starter check counts.

### Acceptance commands

```text
python courses/modeling-inference-reproducible-analytics/modules/05-forecasting-temporal-validation/build_forecast_evidence.py --self-check
python courses/modeling-inference-reproducible-analytics/modules/05-forecasting-temporal-validation/validate_forecast_evidence.py --self-check
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/check-curriculum-specs.ps1
```

### Repository acceptance

- Commons 0.44.0;
- module version 0.1.0;
- clean source fingerprints;
- exact output fingerprints;
- 21 plain-ASCII sections;
- full curriculum gate;
- current-task commit; and
- pushed branch.

## 21. Release, handoff, and resume contract

### Semantic-version decision

Module 05 begins at 0.1.0 and advances the Commons minor release from 0.43.0 to 0.44.0. Module 04 and earlier releases remain unchanged.

### Release facts to freeze

- 6,208 all-jurisdiction rows and 94 Massachusetts rows;
- five folds, four-week horizon, and weeks 75-94;
- 60 eligible-method predictions;
- prediction-table SHA-256 `dfc91a5e38e2255437dc17a5227cccdb14d4970eb79e14b0260ab203aec8de7a`;
- MAE, RMSE, bias, and MAPE for three methods;
- candidate fold losses and worst misses;
- 20 interval readings;
- 90 decomposition rows;
- ADF, ARIMA, and Ljung-Box readings;
- 20 reporting-context rows;
- 20 passing invariants;
- all output hashes;
- builder self-check, 2,666 release validator checks, and 2,604 starter validator checks; and
- progression disposition.

### Module 06 handoff

Module 06 receives exact source fingerprints, fold registry, benchmark registry, prediction table, candidate parameters, interval limitations, fold and horizon errors, failure evidence, reporting context, ARIMA recognition boundary, environment, responsible-agent record, and `continue to Module 06 with conditions` disposition.

### Return triggers

Return to Module 05 for any target, fold, model, benchmark, metric, interval, source, or recommendation change. Return to Module 04 if the intended claim changes enough to reopen the validity map. Use a semantic version for every accepted change.

### Resume record

Module 05 is complete only after the specification, public-source package, exact forecast evidence, learner template, validator, curriculum gate, Commons 0.44.0 update, commit, and push pass. Resume with Module 06 only.
