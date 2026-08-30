# FND-2: Modeling, Inference, and Reproducible Analytics

- Status: course specification complete; module packages not yet built
- Course specification version: 0.1.0
- Commons release: 0.38.0
- Credits: 3
- Delivery: asynchronous online half-term with scheduled model clinics and review
- Planning model: seven instructional weeks mapped to official half-term dates
- Total learner workload: 112.5 hours
- Prerequisite: accepted FND-1 final technical toolkit
- Position: second technical foundation in the 30-credit program
- Final deliverable: reproducible model or agent-assisted analytics package, model card, monitoring plan, and technical defense
- Source record: `docs/source/fnd-2-modeling-inference-reproducible-analytics-source-record.md`
- Course package: `courses/modeling-inference-reproducible-analytics/`

## Course purpose

FND-2 teaches the decisions that begin after a trustworthy analytic table exists. Learners translate a healthcare request into an analytic aim, name the target quantity, choose a suitable method family, fit bounded regression and prediction workflows, check assumptions and validity, evaluate performance, communicate uncertainty, and govern the resulting analysis.

The course does not reward a complicated model for being complicated. Every modeling path starts with a declared decision, prediction time, outcome, baseline, split, and failure rule. A more complex method earns a place only when it improves decision-relevant evidence without hiding calibration, subgroup weakness, instability, leakage, or uncertainty.

The final course question has two parts:

> Is this analytics package technically correct, reproducible, accessible, and honest about what the evidence supports?

> What use, if any, may the fitted model support now?

These decisions are separate. A learner can release an excellent technical package that concludes `do not deploy` because the data are synthetic, small, sparse, stale, or otherwise unfit for real clinical use.

## Audience and final decision

### Primary learner

The primary learner is a clinician, researcher, analyst, quality professional, or health-system staff member who completed FND-1 and can work with a checked analytic table but needs a disciplined foundation in modeling, inference, validation, and model governance.

### Final decision owner

The final decision owner is a clinical analytics model-risk lead or senior quantitative analyst who is independent of the learner and responsible for deciding whether an analysis may move into further validation.

### Secondary readers

- an applied-course instructor receiving the learner's method foundation;
- a clinical informatician checking outcome, prediction time, and use meaning;
- a biostatistician checking assumptions, uncertainty, and validity;
- a model-risk or data-science reviewer checking evaluation and failure analysis;
- a forecasting reviewer checking temporal validation;
- a data steward checking source rights and prohibited data;
- an accessibility reviewer checking model evidence and defense materials; and
- an independent instructor checking reproduction and teachability.

### Package dispositions

| Disposition | Meaning | Course result |
|---|---|---|
| `accept` | Every package gate passes and no material condition remains. | The learner completes FND-2 and may carry the package as foundations evidence. |
| `accept with conditions` | Every noncompensable package gate passes and bounded conditions have owners, due points, evidence, and escalation rules. | The learner completes FND-2 under the recorded conditions. |
| `revise` | A recoverable analytic, code, interpretation, accessibility, documentation, or reproduction defect remains. | The package returns for correction. |
| `refer` | A rights, privacy, integrity, safety, governance, or model-risk concern needs program review. | The package is held from downstream use. |

### Model-use recommendations

| Recommendation | Meaning |
|---|---|
| `teaching use only` | The model supports technical education and method development but no operational or clinical action. |
| `silent prospective validation only` | A future model with appropriate real data and governance may be evaluated without affecting care or operations. The public reference cannot authorize this step by itself. |
| `revise before further validation` | The model or evaluation has a correctable defect that prevents meaningful prospective work. |
| `stop model use` | Evidence is insufficient, unsafe, or outside the declared purpose. |

The reference course package is expected to receive an acceptable package disposition and a `teaching use only` model recommendation. No public-course artifact authorizes deployment, patient-level action, clinical decision support, staffing, capacity action, or performance judgment.

## Place in the curriculum

FND-1 and FND-2 are separate straight-through technical foundations.

### FND-1 handoff

FND-2 begins from an accepted FND-1 toolkit. FND-2 may read the source, schema, cohort, analytic table, quality records, descriptive evidence, access routes, provenance, and retained conditions. It may create a separately versioned modeling derivation, but it cannot silently change the upstream cohort, grain, denominator, source facts, or quality decision.

FND-1 remains the owner of:

- source retrieval and relational construction;
- cohort SQL and one-row-per-person analytic grain;
- data cleaning, quality rules, missingness profile, and retained conditions;
- descriptive rates, denominators, exact tables, figures, and text alternatives;
- source and transformation records; and
- technical data handoff.

### FND-2 ownership

FND-2 owns:

- decision-to-aim translation and estimands;
- prediction-time, outcome, feature, split, and baseline contracts;
- regression foundations and model-conditional interpretation;
- prediction workflows, discrimination, calibration, thresholds, and class imbalance;
- confounding, selection, leakage, missing-data strategy, repeated measures, and longitudinal-method boundaries;
- forecasting aims, temporal validation, benchmarks, and error metrics;
- model tests, failure analysis, agent-assisted verification, and human sign-off;
- model cards, subgroup and equity review, monitoring, drift, retraining, rollback, stop, retirement, and defense; and
- the distinction between package acceptance and model-use permission.

### Applied-course boundary

FND-2 teaches the general method judgment needed before domain specialization. Applied courses do not repeat these modules. They extend them through a distinct decision:

| Course | FND-2 skill extended | Applied ownership |
|---|---|---|
| APP-1: Clinical Care | longitudinal structure, censoring, survival recognition, adjustment | care-pathway and treatment questions, risk adjustment, clinically meaningful effects |
| APP-2: Patient Experience and Engagement | missingness, selection, subgroup validity | survey scales, patient-reported evidence, response bias, representation, patient partnership |
| APP-3: Clinical Performance and Improvement | temporal validation, forecasting foundations | operational rates, statistical process control, capacity, simulation, balancing measures |
| APP-4: Clinical Decision Support | prediction, thresholds, calibration, subgroup performance, monitoring | workflow logic, alert burden, human factors, safety case, sandbox validation |
| APP-5: Population Health and Equity | adjustment, subgroup evaluation, uncertainty | population denominators, standardization, geography, targeting, fairness, community accountability |
| APP-6: Health Research and Innovation | estimands, DAGs, validity threats, sensitivity | study design, causal identification, protocols, preregistration, reporting, next-study logic |
| APP-7: Strategy, Finance, and Value | scenario uncertainty, model comparison, forecasting | finance, utilization, value, investment, executive decision, implementation monitoring |

DA-730 remains the owner of visualization concepts. FND-2 requires readable and accessible evaluation displays but does not reteach the full visualization course.

## Source fidelity and approved normalization

### Source identity

- Source: `04-FND-2-Modeling-Inference-Reproducible-Analytics.docx`.
- Bytes: 21,850.
- SHA-256: `eef6fbb36cb27917f8b48b61e705895a5cb5eaad64bd0f0d38bf153525528c03`.
- Verified identical in both supplied curriculum ZIP files on 2026-08-30.
- Source credits: 3.
- Source schedule: seven-week online block.
- Source workload: 112.5 hours.
- Source prerequisite: FND-1.

### Preserved source decisions

- seven straight-through technical modules;
- exact module names and hours;
- Python as the graded modeling language;
- SQL as the model-ready extraction layer;
- R as read-run-interpret rather than from-scratch graded programming;
- Core, Guided, and Recognize mastery levels;
- regression, prediction, adjustment, longitudinal structure, missing data, forecasting, agent use, tests, model cards, monitoring, and defense;
- source assessment weights of 15%, 25%, 25%, and 35%; and
- the final model or agent-assisted analytics package with model card.

### Approved Commons normalization

The Commons makes the requested Week 3, Week 6, and official-end-date checkpoint cadence explicit without changing source weight:

| Commons checkpoint | Source components preserved | Course points |
|---|---|---:|
| End of instructional Week 3 | Week 1 setup and aim classification, 15 points; Week 3 regression and prediction, 25 points | 40 |
| End of instructional Week 6 | Week 5 validity, longitudinal, and forecasting work, with Week 6 tests and agent-accountability evidence | 25 |
| Official last day of assigned half-term | Final analytics package, model card, governance, reproducibility audit, and defense | 35 |
| Total |  | 100 |

The source calls several regression coefficients effects. The Commons uses association language unless design and identification support a causal claim. Odds, risks, probabilities, and risk differences remain distinct. Confidence intervals are interpreted under the stated model and design assumptions. A synthetic technical case does not become evidence about a real patient population.

The 7.5-week phrase is a planning model. The official MGH Institute calendar controls the start, checkpoint placement, and final due date.

## Course learning outcomes

By the end of FND-2, a learner can:

| ID | Assessable course outcome | Source alignment |
|---|---|---|
| CLO-1 | Classify a request as descriptive, associational, predictive, causal, longitudinal, or forecasting and write the decision, population, time zero, estimand or target, horizon, and success criterion. | Source CLO-1 |
| CLO-2 | Create a versioned model-ready derivation with a declared prediction time, allowed predictors, prohibited leakage fields, split registry, baseline, environment, tests, and reproducible build. | Source CLO-2 |
| CLO-3 | Fit and interpret bounded linear and logistic regression workflows, check assumptions, distinguish odds from risk, report uncertainty, and separate statistical from practical meaning. | Source CLO-3 |
| CLO-4 | Evaluate a prediction model using untouched test data, discrimination, calibration, thresholds, confusion measures, class prevalence, uncertainty, subgroup evidence, and comparison with a simple baseline. | Source CLO-3 |
| CLO-5 | Diagnose confounding, selection, leakage, missingness, repeated measures, clustering, sparse outcomes, and transport limits, then choose a remedy, caveat, specialist referral, or stop decision. | Source CLO-4 |
| CLO-6 | Build and backtest an introductory forecast against declared naive benchmarks, choose decision-relevant error metrics, and recognize when stationarity, ARIMA, or operational process assumptions need deeper expertise. | Source CLO-5 |
| CLO-7 | Use an analytic agent within bounded tasks, write data and model tests, audit hallucinated or unsupported output, preserve a prompt and trace log, and record human sign-off. | Source CLO-6 |
| CLO-8 | Release and defend an accessible analytics package with a model card, intended and prohibited use, subgroup review, monitoring, drift signals, retraining triggers, rollback, stop, retirement, and model-use recommendation. | Source CLO-6 |

## Program-outcome mapping

| Program outcome | FND-2 evidence |
|---|---|
| PLO-1 | Reproducible Python modeling workflow, regression, prediction, tests, and package release. |
| PLO-2 | Analytic aim, method choice, model evaluation, forecasting, and decision-relevant metrics. |
| PLO-3 | Confounding, selection, missingness, subgroup evidence, temporal validation, uncertainty, and stop decisions. |
| PLO-4 | Versioned code, environment, split registry, model card, trace log, clean reproduction, and monitoring. |
| PLO-5 | Honest interpretation, accessible evidence, technical handoff, decision recommendation, and defense. |
| PLO-6 | Data boundaries, agent accountability, model governance, human review, and prohibited-use controls. |

## Academic calendar rule

The official academic calendar is:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The calendar labels the relevant offerings as half-terms. Verified 2026-2027 half-term spans range from 49 to 52 elapsed days, which is approximately seven to seven and one-half weeks depending on the term. Therefore:

- the seven source weeks define instructional order and workload;
- the registrar's published dates define actual openings and closings;
- Checkpoint 1 is due at the end of instructional Week 3;
- Checkpoint 2 is due at the end of instructional Week 6; and
- the final checkpoint is due on the official last day of the assigned half-term.

No course release may calculate a final date merely by adding 7.5 weeks to the start date.

## Schedule and workload

| Module | Technical module | Source week | Hours | Cumulative hours | Primary release |
|---:|---|---:|---:|---:|---|
| 01 | Analytic aims and a reproducible modeling workspace | 1 | 15.5 | 15.5 | Aim, method, split, baseline, and workspace release |
| 02 | Regression models and interpretation | 2 | 16.0 | 31.5 | Regression assumption and interpretation release |
| 03 | Prediction workflows and evaluation | 3 | 16.5 | 48.0 | Prediction evaluation release and Week 3 checkpoint |
| 04 | Adjustment, missing data, and longitudinal structure | 4 | 16.5 | 64.5 | Validity and method-boundary release |
| 05 | Forecasting and temporal validation | 5 | 16.0 | 80.5 | Forecast and backtesting release |
| 06 | Agent-assisted modeling and testing | 6 | 16.0 | 96.5 | Tests, trace, adjudication, and Week 6 checkpoint |
| 07 | Model cards, governance, and defense | 7 | 16.0 | 112.5 | Final analytics-package candidate and defense |
| Total |  |  | 112.5 | 112.5 |  |

### Workload categories

| Category | Course hours |
|---|---:|
| Direct instruction, walkthroughs, clinics, and feedback | 18.0 |
| Readings, videos, and guided preparation | 18.0 |
| Labs, coding practice, modeling, and testing | 28.0 |
| Drafting, revision, peer review, and reflection | 18.5 |
| Signature analytics package | 30.0 |
| Total | 112.5 |

The 112.5-hour total is fixed. A calendar with an extra partial week does not add another module or more learner work.

## Instructional tools

### Graded core

- SQL for selecting the accepted FND-1 modeling frame without redefining the upstream cohort;
- Python for fitting, evaluation, tests, reproducible notebooks or scripts, and final packaging;
- pandas for explicit table operations;
- a tested statistical modeling package for regression and introductory forecasting;
- a tested machine-learning package for pipelines, resampling, metrics, calibration, and bounded baselines;
- notebooks or scripts that run noninteractively;
- Git commits and annotated semantic-version tags;
- environment and dependency records;
- standard text, CSV, JSON, Markdown, PNG, and SVG artifacts; and
- a prompt and trace log for material agent use.

### R role

Learners read, run, and interpret paired R Markdown or Quarto examples for regression, mixed models, and survival work. They are not graded on writing R from scratch. A module that supplies R code must include pinned package versions, an instructor-tested output, an accessible interpretation, and a Python-side concept mapping.

### Agent role

An agent may explain code, suggest tests, critique a model, draft documentation, or diagnose an error. It may not choose the final analytic aim, invent results, inspect prohibited data, make the model-use decision, or replace the learner's defense. Material assistance is logged and independently checked.

### Dependency rule

Each module pins only packages it actually runs. A package is not added because it might be useful later. Module validators use the Python standard library when practical and invoke the released analysis only when result reproduction requires its declared packages.

## Continuing healthcare modeling system

FND-2 uses two linked but distinct cases.

### Case A: synthetic acute-return modeling

The primary modeling case starts from the accepted FND-1 resolved analytic table:

- path: `courses/healthcare-data-foundations/modules/04-cleaning-profiling/outputs/resolved-analytic-table.csv`;
- version: inherited from accepted FND-1 Module 04 and final toolkit 0.1.0;
- bytes: 121,787;
- SHA-256: `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a`;
- rows: 374;
- fields: 29;
- grain: one selected synthetic adult and one unique index encounter per row;
- prediction time: index encounter stop;
- binary outcome: any emergency or inpatient acute return within 90 days;
- outcome counts: 36 positive and 338 negative;
- source: Synthea April 2020 public synthetic sample; and
- permitted use: technical education and method development only.

The course creates a separate FND-2 modeling release. It does not edit the accepted FND-1 file.

### Case B: public respiratory forecasting

The forecasting case uses the pinned CDC NHSN weekly hospital respiratory release already present in the Commons:

- full path: `courses/data-visualization/modules/08-time-process-variation/data/nhsn_hospital_capacity_jurisdiction_2024_2026.csv`;
- full rows: 6,208;
- full fields: 14;
- jurisdictions: 67;
- full SHA-256: `8a492c3d2d3dae07c42e89ef35ed714d23acab32596f42037dcf8dd0284531d1`;
- Massachusetts path: `courses/data-visualization/modules/08-time-process-variation/data/ma_hospital_capacity_time_2024_2026.csv`;
- Massachusetts rows: 94 consecutive weeks;
- Massachusetts fields: 21;
- Massachusetts SHA-256: `394d9b02d2cc9b4fbf0d9f415db3da6b04393dd9430816973e81fef86fb0e616`;
- observed period: 2024-11-09 through 2026-08-22;
- unit: jurisdiction-week aggregate across a changing set of reporting hospitals; and
- source landing page: https://data.cdc.gov/Public-Health-Surveillance/Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/rhwp-grxi

FND-2 preserves all 6,208 source-selection rows in its provenance chain. The Massachusetts series supports guided forecasting because its 94 weeks are consecutive. It does not represent one hospital's stable process, and changing reporting coverage remains a model limitation.

## Data layers and provenance

| Layer | Owner | Required identity | FND-2 action |
|---|---|---|---|
| FND-1 final technical toolkit | FND-1 | accepted commit, tag, conditions, 90-file candidate, 100-file final state | read and verify only |
| Accepted analytic table | FND-1 Module 04 | 374 rows, 29 fields, exact SHA-256 | copy through registered derivation input |
| Modeling cohort | FND-2 Module 01 | source fingerprint, prediction time, feature roles, split assignment, label counts | build and version |
| Regression evidence | FND-2 Module 02 | formulas, reference levels, estimates, intervals, diagnostics, interpretation | build and version |
| Prediction evidence | FND-2 Module 03 | pipeline, baseline, resampling, validation, untouched test evidence, calibration, thresholds | build and version |
| Validity evidence | FND-2 Module 04 | DAG, threat register, missingness comparison, clustered or longitudinal boundary, specialist referrals | build and version |
| CDC forecasting source | DA-730 source release and CDC | full and Massachusetts fingerprints, source URL, coverage limits | reuse without source-value changes |
| Forecast evidence | FND-2 Module 05 | forecast aim, horizon, temporal folds, benchmarks, errors, residual and limitation record | build and version |
| Test and agent evidence | FND-2 Module 06 | tests, seeded failures, prompt and trace log, critique adjudication, human sign-off | build and version |
| Final model release | FND-2 Module 07 and final checkpoint | model card, monitoring, version, defense, disposition, model-use decision | assemble, audit, and freeze |

Every copied source keeps its source version, byte count, SHA-256, row count, field count, role, and permitted-use note. Silent refresh is prohibited.

## Prediction-time and feature contract

### Unit and prediction time

One modeling row represents one selected synthetic adult at the stop of one index emergency or inpatient encounter. The prediction question is whether a different emergency or inpatient encounter occurs within the next 90 days.

### Allowed baseline predictors

The initial model may use only fields known at or before prediction time:

- age at index;
- source gender;
- source race;
- source ethnicity;
- index encounter class;
- prior 365-day encounter count;
- prior 365-day acute count;
- prior 365-day condition count; and
- prior 365-day medication count.

The synthetic patient ID and index encounter ID may support joins and exact row tracking but cannot be model predictors. Index code, description, and optional reason fields require a separate high-cardinality and missingness decision before use; they are excluded from the default core model.

### Prohibited leakage predictors

The following fields occur after prediction time or encode the outcome and cannot enter predictors:

- `next_30d_state`;
- `next_30d_encounter_id`;
- `next_30d_start`;
- `next_30d_days_after_index_stop`;
- `acute_return_90d` except as the label;
- `death_90d`;
- `endpoint_90d`;
- `followup_90d_complete` as a predictor;
- any feature calculated using future encounters; and
- any split, outcome, metric, or reviewer decision field.

A deliberate leaked model appears only as a critique fixture. It must be labeled invalid and must never become the accepted model.

### Temporal split

Rows are ordered by `index_start`, then `patient_id`, and assigned once:

| Split | Rows | Acute-return positives | Negatives | Index-start range |
|---|---:|---:|---:|---|
| Train | 224 | 25 | 199 | 2015-01-01 through 2017-04-02 |
| Validation | 75 | 7 | 68 | 2017-04-05 through 2018-04-03 |
| Test | 75 | 4 | 71 | 2018-04-18 through 2019-12-28 |
| Total | 374 | 36 | 338 | 2015-01-01 through 2019-12-28 |

The split assignment is an immutable Module 01 artifact. Test labels are not used for feature selection, threshold choice, tuning, imputation fitting, scaling, or model selection. The four positive test outcomes are a major precision and subgroup limitation, not a reason to resplit until the result looks better.

### Baselines and candidate models

The required prediction baseline is the training-set outcome prevalence applied as a constant probability. The required interpretable candidate is a bounded logistic-regression pipeline. A provided regularized or tree-based machine-learning baseline may be compared in Module 03, but added complexity must not replace the baseline, calibration, threshold, uncertainty, or subgroup review.

### Linear-regression teaching subset

Module 02 also uses the 111 rows with a recorded different encounter within 30 days. The continuous outcome is days from index stop to that next encounter, ranging from 0.9 to 29.958333 days in the accepted table. This is a selected conditional sample. The lab must state that it does not model time to encounter for all 374 people and cannot treat the 263 structural blanks as zero.

## Forecast contract

The primary forecast target is weekly total new reported COVID-19, influenza, and RSV admissions in the Massachusetts jurisdiction aggregate. The target is already recorded as `total_respiratory_new_admissions` in the 94-week teaching series and remains traceable to the three exact source counts.

The forecast contract must declare:

- issue date and information cutoff;
- horizon;
- training and test dates;
- rolling-origin or expanding-window folds;
- last-value and seasonal-naive benchmarks when the training history supports them;
- one guided smoothing model;
- one provided ARIMA-family example for recognition, not mastery;
- error metrics with units and zero-value behavior;
- reporting-coverage context;
- no manual replacement of unavailable source fields;
- no claim about one hospital's capacity or admissions; and
- a `do not use operationally` boundary for the public teaching result.

The course does not borrow the exploratory process-limit claim from DA-730 as forecast truth. Visualization and forecasting are different decisions.

## Module sequence

| Module | Technical decision | Main input | Required handoff |
|---:|---|---|---|
| 01 | What is the analytic aim, target, prediction time, split, and baseline? | accepted FND-1 toolkit and 374-row table | immutable modeling cohort and aim contract |
| 02 | What do bounded regression estimates mean, and which assumptions fail? | Module 01 modeling cohort | regression evidence and interpretation limits |
| 03 | Does the prediction workflow beat its baseline and hold up on untouched data? | Modules 01 and 02 | evaluation release and Week 3 checkpoint |
| 04 | Which validity threats change the claim, method, or stop decision? | accepted prediction evidence and provided method examples | validity and specialist-referral record |
| 05 | Does an introductory forecast beat declared temporal benchmarks? | pinned CDC NHSN public release | forecast evidence and time limits |
| 06 | Can tests and bounded agent use find failures without shifting accountability? | accepted model, validity, and forecast evidence | tested Week 6 integration release |
| 07 | Can another reviewer understand, reproduce, govern, and stop the model? | all accepted FND-2 evidence | final analytics-package candidate and defense |

## Module 01 brief: Analytic aims and a reproducible modeling workspace

- Source week: 1.
- Learner work: 15.5 hours.
- Module ID target: `oclc-fnd2-01`.
- Initial module version target: 0.1.0.
- Source assessment component: 15 course points.
- Decision owner: senior quantitative analyst acting as modeling-workflow reviewer.
- Decision: may this aim, data role, prediction-time, feature, split, baseline, and repository contract enter regression and prediction work?

### Technical outcome

The learner can classify an analytic request before selecting a method and can release a reproducible modeling workspace that makes future information unavailable to the training process.

### Content and mastery

| Concept | Required understanding | Mastery |
|---|---|---|
| Decision statement | Name who decides, what action is possible, what evidence is needed, and what the analysis will not decide. | Core |
| Aim taxonomy | Distinguish descriptive, associational, predictive, causal, longitudinal, and forecasting aims. | Core |
| Estimand or target | State population, unit, time zero, exposure or predictors, outcome, horizon, contrast or success criterion. | Core |
| Method-family map | Match the aim to a method family and reject mismatched alternatives. | Core |
| Prediction time | Freeze what information is available when a prediction would be made. | Core |
| Leakage | Detect post-index, outcome-derived, split-derived, preprocessing, and identity leakage. | Core |
| Temporal split | Assign train, validation, and test roles once and explain why the test set stays untouched. | Core |
| SQL-to-model derivation | Build a registered modeling table without changing the accepted FND-1 cohort. | Guided |
| Reproducible environment | Pin the code, packages, seed policy, file tree, and ordered commands. | Core |
| Simple baseline | Fit or compute the minimum comparison every later model must beat. | Guided |

### Worked case

The instructor walks through six requests that use the same synthetic cohort but require different aims. The class converts one request into the acute-return prediction contract, identifies prediction time at index stop, labels every source field by role, and catches the post-index fields that would make an invalid model appear excellent.

The instructor then builds the fixed temporal split. Learners inspect the outcome counts of 25, 7, and 4 in train, validation, and test. The correct first conclusion is that test and subgroup estimates will be imprecise.

### Guided practice

Learners:

1. classify twelve healthcare requests by aim;
2. write the target or estimand for six;
3. explain why at least two attractive methods do not fit;
4. verify the accepted FND-1 table fingerprint;
5. label all 29 fields as key, allowed predictor, excluded default field, label, post-index leakage, or metadata;
6. build the deterministic split registry;
7. compute the training-prevalence baseline;
8. create environment and seed records; and
9. rerun the workspace from a new target.

### Exact learner release

The future runnable package must produce at least:

- `README.md`;
- `VERSION`;
- environment and exact dependency record;
- source and FND-1 handoff record;
- `aim-and-method-plan.md`;
- `estimand-target-registry.csv`;
- `feature-role-contract.csv` with all 29 source fields;
- `modeling-cohort.csv` with 374 rows plus registered FND-2 derivation fields;
- `split-registry.csv` with 224 train, 75 validation, and 75 test rows;
- `baseline-metrics.csv`;
- SQL or source-to-model build code;
- a noninteractive build or executed notebook;
- `reproducibility-check.md`;
- `ai-use.md` or prompt-log starter; and
- validator output.

### Fifteen-point draft rubric

| Criterion | Points |
|---|---:|
| Decision, aim, target, population, time zero, and horizon | 4.00 |
| Exact FND-1 input, feature roles, and leakage boundary | 4.00 |
| Deterministic split, outcome reconciliation, and baseline | 3.00 |
| Reproducible repository, environment, build, and tests | 3.00 |
| Responsible agent disclosure and plain-language handoff | 1.00 |
| Total | 15.00 |

### Noncompensable gates

- exact accepted FND-1 input and conditions;
- exact 374-row grain and source fingerprint;
- prediction time stated before feature selection;
- every post-index and outcome field blocked from predictors;
- split rows and positive counts reconcile exactly;
- test data unused by fitting or selection;
- baseline recorded before candidate-model comparison;
- no restricted or real patient data;
- protected output target and clean reproduction; and
- explicit Module 02 progression disposition.

### Handoff to Module 02

Module 02 receives the exact modeling cohort, split registry, feature roles, baseline, environment, and aim contract. A changed row, split, label, or role returns to Module 01 and requires a version decision.

## Module 02 brief: Regression models and interpretation

- Source week: 2.
- Learner work: 16.0 hours.
- Module ID target: `oclc-fnd2-02`.
- Initial module version target: 0.1.0.
- Week 3 assessment share: 10 of the 25 regression-and-prediction course points.
- Decision owner: biostatistical methods reviewer.
- Decision: are the fitted regression evidence, diagnostics, uncertainty, and interpretation accurate enough to enter prediction evaluation?

### Technical outcome

The learner can fit bounded linear and logistic models from declared formulas, check assumptions, interpret estimates and uncertainty in the quantity actually modeled, and stop at association when design does not support a causal claim.

### Content and mastery

| Concept | Required understanding | Mastery |
|---|---|---|
| Linear regression | Fit a declared model, interpret a coefficient conditionally, and evaluate whether the continuous-outcome setup is defensible. | Guided |
| Logistic regression | Fit a binary-outcome model and distinguish log odds, odds ratios, risks, and predicted probabilities. | Guided |
| Assumptions | Check functional form, independence, variance, influential observations, separation, sparsity, and model specification. | Core |
| Reference groups and encoding | Record categorical reference levels and prevent silent coding changes. | Core |
| Nonlinear terms | Use a bounded transformation or spline example and explain the changed interpretation. | Guided |
| Interactions | Fit one declared interaction and avoid reading unsupported subgroup effects into it. | Guided |
| Uncertainty | Report coefficient and prediction uncertainty under stated assumptions. | Core |
| Statistical and practical meaning | Separate numerical evidence, uncertainty, and decision relevance. | Core |
| R interpretation | Read a paired R summary and reconcile it with the Python model. | Guided |

### Worked cases

The linear case uses the 111 people with a recorded different encounter within 30 days and models days to that encounter. The instructor makes the selection condition visible: 263 people have no recorded next encounter, and their structural blanks cannot become zero. The result describes a selected conditional sample and is not a time-to-event analysis for all 374 people.

The logistic case models 90-day acute return from pre-index and index-time fields. The instructor begins with a small formula, checks coding and sparse cells, and reports model-conditional associations. Causal language fails the interpretation gate.

### Guided practice

Learners:

1. write formulas before fitting;
2. create a reference-level registry;
3. fit the linear and logistic templates on training data;
4. inspect residual and influence evidence appropriate to each model;
5. check sparse categories and separation warnings;
6. add one nonlinear term and one interaction separately;
7. compare estimates and intervals with the simpler model;
8. translate log odds, odds ratios, and probabilities without substitution;
9. read paired R output; and
10. write supported, unsupported, and decision-relevant interpretations.

### Exact learner release

The future runnable package must produce at least:

- declared formulas and reference levels;
- linear-model coefficient and diagnostic tables;
- logistic-model coefficient and diagnostic tables;
- model matrices or feature-name records;
- uncertainty intervals with method stated;
- nonlinear-term comparison;
- interaction comparison;
- sparse-cell and separation checks;
- Python and paired R interpretation records;
- `regression-interpretation.md`;
- `assumption-register.csv`;
- exact code or executed notebooks;
- reproduction and AI-use records; and
- validation output.

### Ten-point Week 3 share

| Criterion | Course points |
|---|---:|
| Declared formulas, encodings, and reference levels | 2.00 |
| Correct linear and logistic fitting evidence | 2.50 |
| Assumption, sparse-data, influence, and failure checks | 2.50 |
| Quantity-correct uncertainty and interpretation | 2.00 |
| Reproduction, R reading, and responsible agent record | 1.00 |
| Total | 10.00 |

### Noncompensable gates

- Module 01 contract and split unchanged;
- structural blanks not changed to zero;
- test split not used for fitting or interpretation development;
- formulas and encodings declared;
- logistic quantities named correctly;
- no causal effect language from an associational model;
- sparse and unstable estimates remain visible;
- diagnostics are evidence, not automatic approval;
- Python and R outputs reconcile within declared numeric tolerance; and
- explicit Module 03 handoff.

### Handoff to Module 03

Module 03 receives the accepted aim, split, baseline, feature pipeline, bounded logistic formula, regression evidence, and assumption conditions. It evaluates prediction performance rather than grading coefficients again.

## Module 03 brief: Prediction workflows and evaluation

- Source week: 3.
- Learner work: 16.5 hours.
- Module ID target: `oclc-fnd2-03`.
- Initial module version target: 0.1.0.
- Week 3 assessment share: 15 of the 25 regression-and-prediction course points.
- Decision owner: clinical prediction and model-risk reviewer.
- Decision: does the locked prediction pipeline beat its simple baseline and provide credible enough evidence for validity review, without claiming deployment readiness?

### Technical outcome

The learner can fit preprocessing only on training data, select a candidate with validation evidence, lock the threshold before test evaluation, and judge discrimination, calibration, threshold behavior, class imbalance, uncertainty, and subgroup evidence on untouched data.

### Content and mastery

| Concept | Required understanding | Mastery |
|---|---|---|
| Feature pipeline | Fit encoding, scaling, imputation, and selection only on allowed training data. | Guided |
| Resampling | Use training-only resampling and distinguish it from final temporal validation and test evaluation. | Guided |
| Temporal validation | Respect the fixed date-ordered split and expected distribution change. | Guided |
| Discrimination | Interpret ranking ability without treating it as calibration or utility. | Guided |
| Calibration | Compare predicted risk with observed frequency using tables, plots, intercept, slope, and uncertainty suited to the sample. | Guided |
| Thresholds | Choose one threshold from the decision and validation evidence before opening test results. | Core |
| Confusion measures | Report sensitivity, specificity, PPV, NPV, false counts, prevalence, and denominator together. | Core |
| Class imbalance | Reject accuracy as a sufficient metric and keep the 36 total outcomes visible. | Guided |
| Machine-learning baseline | Run one bounded provided regularized or tree-based comparison and ask whether complexity changes the decision. | Recognize |
| Subgroup performance | Report exact subgroup counts and uncertainty and suppress unsupported rankings or fairness claims. | Core |

### Required comparisons

The learner compares:

1. training-prevalence constant baseline;
2. accepted logistic-regression candidate;
3. one provided bounded machine-learning baseline; and
4. one deliberately leaked critique model that must fail.

The leaked model is never eligible for selection. The test set has only four positive outcomes. A high or low point estimate cannot erase that limitation.

### Guided practice

Learners:

1. build a single preprocessing and model pipeline;
2. inspect transformed feature names;
3. run training-only resampling;
4. compare models on validation evidence;
5. declare the selection rule and threshold;
6. freeze the selected pipeline;
7. run the test set once;
8. compute exact metric numerators and denominators;
9. produce calibration and threshold tables with accessible displays;
10. report subgroup counts before metrics;
11. demonstrate why the leaked model fails; and
12. issue a `continue to validity review`, `revise`, or `stop` recommendation.

### Exact learner release

The future runnable package must produce at least:

- registered feature and preprocessing pipeline;
- training resampling results;
- validation comparison table;
- model-selection record;
- threshold-decision record;
- locked test predictions for all 75 test rows;
- baseline and candidate test metrics;
- exact confusion table;
- calibration table and accessible plot plus structured alternative;
- threshold table and accessible plot plus structured alternative;
- subgroup counts, metrics, uncertainty, and suppression flags;
- leaked-model failure evidence;
- `prediction-evaluation-report.md`;
- model artifact or deterministic refit contract;
- reproduction and AI-use records; and
- validation output.

### Fifteen-point Week 3 share

| Criterion | Course points |
|---|---:|
| Leakage-safe preprocessing, resampling, and model lock | 3.00 |
| Baseline, validation comparison, and selection rule | 2.50 |
| Untouched test discrimination and calibration evidence | 3.00 |
| Threshold, confusion measures, prevalence, and decision meaning | 2.50 |
| Subgroup counts, uncertainty, sparse-outcome limits, and failure analysis | 2.50 |
| Accessible evidence, reproduction, and responsible agent record | 1.50 |
| Total | 15.00 |

### Noncompensable gates

- fixed split and Module 01 fingerprints preserved;
- preprocessing fit only on training data;
- no test-guided feature, model, threshold, or documentation choice;
- simple baseline retained;
- leaked critique model rejected;
- model comparison uses the same rows and declared metrics;
- calibration reported, not replaced by AUC;
- threshold chosen against an explicit decision consequence;
- exact confusion numerators and denominators present;
- test positive count of four remains visible;
- subgroup results show counts and unsupported cells are not ranked;
- accessible exact tables accompany plots;
- no deployment or real clinical performance claim; and
- explicit Checkpoint 1 disposition.

### Handoff to Checkpoint 1 and Module 04

Checkpoint 1 freezes Modules 01 through 03 as the 40-point modeling-readiness release. Module 04 may begin only after an allowed disposition. It receives the exact aim, data roles, split, baseline, regression conditions, selected prediction pipeline, test evidence, sparse-outcome limits, and model-use boundary.

## Module 04 brief: Adjustment, missing data, and longitudinal structure

- Source week: 4.
- Learner work: 16.5 hours.
- Module ID target: `oclc-fnd2-04`.
- Initial module version target: 0.1.0.
- Week 6 assessment share: 15 of the 25 validity, longitudinal, and forecasting course points.
- Decision owner: biostatistical validity reviewer with clinical-informatics support.
- Decision: which validity threats change the claim, method, uncertainty, or model-use recommendation, and which require specialist referral or a stop decision?

### Technical outcome

The learner can identify when a clean table and correctly executed model still fail to answer the intended question. The learner distinguishes a predictive model from a causal comparison, diagnoses missingness and selection, recognizes repeated and time-to-event structure, and documents the remedy or boundary.

### Content and mastery

| Concept | Required understanding | Mastery |
|---|---|---|
| DAG and role reasoning | Draw a basic directed acyclic graph and label candidate confounders, colliders, mediators, selection variables, exposure, and outcome. | Core |
| Causal claim screen | Decide whether design and data can support the requested causal contrast. | Core |
| Confounding | Explain why prediction adjustment and causal adjustment are different decisions. | Core |
| Propensity methods | Read overlap, balance, matching, or weighting evidence from a provided example. | Guided |
| Selection | Identify conditioning introduced by the 111-row recorded-next-encounter regression subset and other eligibility choices. | Core |
| Missingness mechanisms | Propose plausible MCAR, MAR, or MNAR structures as assumptions, not facts learned from the observed table alone. | Core |
| Missing-data sensitivity | Compare complete-case and bounded imputation results without treating imputation as truth. | Guided |
| Repeated measures and clustering | Recognize dependence and read a provided clustered or repeated-measures template. | Guided |
| Mixed models | Read fixed and random effects in paired R output and state what the hierarchy adds. | Recognize |
| Survival methods | Recognize censoring and when Kaplan-Meier or Cox methods are needed instead of deleting unobserved times or setting them to zero. | Recognize |

### Three teaching cases

1. The 111-row regression subset demonstrates selection: an analysis conditional on a recorded next encounter cannot describe time to next encounter for all 374 people.
2. A provided confounded treatment-comparison fixture demonstrates why a predictive feature set is not a causal adjustment set. Learners use a DAG, overlap, and balance evidence but do not claim mastery of causal inference.
3. A provided repeated-measures and survival fixture demonstrates why ordinary independent-row regression can understate uncertainty and why censoring requires a time-to-event method.

The causal, repeated-measures, and survival fixtures must be public, synthetic, or generated from documented public aggregates. They cannot introduce a restricted clinical dataset.

### Guided practice

Learners:

1. classify twelve validity threats by design stage;
2. draw and narrate a DAG in both visual and structured text form;
3. decide whether a requested causal claim is supportable;
4. inspect overlap and covariate-balance evidence;
5. compare prediction and causal adjustment sets;
6. diagnose observed missingness patterns and state untestable assumptions;
7. compare complete-case and bounded imputation sensitivity results;
8. identify the cluster or repeated unit in three examples;
9. read one mixed-model output and one survival output;
10. update the prediction package threat register; and
11. issue a remedy, caveat, specialist referral, or stop recommendation for every material threat.

### Exact learner release

The future runnable package must produce at least:

- `analytic-aim-validity-map.csv`;
- visual DAG in an editable format;
- structured DAG node and edge tables or equivalent text;
- causal-claim screen;
- confounder, collider, mediator, and selection register;
- propensity example overlap and balance evidence;
- missingness profile and mechanism-assumption record;
- complete-case versus imputation sensitivity table;
- repeated-measures interpretation record;
- paired R mixed-model reading record;
- survival and censoring recognition record;
- `validity-threat-register.csv`;
- `validity-adjustment-longitudinal-memo.md`;
- specialist-referral and stop decisions;
- reproduction, accessibility, and AI-use records; and
- validation output.

### Fifteen-point Week 6 share

| Criterion | Course points |
|---|---:|
| Aim, estimand, DAG, and causal-claim boundary | 4.00 |
| Confounding, overlap, balance, and adjustment reasoning | 3.00 |
| Missingness assumptions and sensitivity evidence | 3.00 |
| Selection, repeated measures, mixed-model, survival, and specialist boundaries | 3.00 |
| Clear memo, accessible DAG, reproduction, and agent disclosure | 2.00 |
| Total | 15.00 |

### Noncompensable gates

- Checkpoint 1 accepted input unchanged;
- prediction and causal aims remain distinct;
- DAG roles and adjustment choices are explicit;
- no collider or post-outcome variable added without a defensible reason;
- overlap and balance evidence shown for the propensity example;
- missingness mechanisms labeled assumptions;
- structural blanks not converted to zero;
- sensitivity comparison uses the same declared target and population;
- repeated or clustered observations not treated as independent without a recorded limit;
- censoring not handled as ordinary missingness;
- no causal, treatment, survival, or transport claim beyond the design;
- visual DAG has an equivalent structured route; and
- explicit Module 05 progression disposition.

### Handoff to Module 05

Module 05 receives the accepted validity register, claim boundaries, specialist referrals, and testing implications. It starts a distinct public time-series forecast and does not treat the prediction model's row-level split as a forecast split.

## Module 05 brief: Forecasting and temporal validation

- Source week: 5.
- Learner work: 16.0 hours.
- Module ID target: `oclc-fnd2-05`.
- Initial module version target: 0.1.0.
- Week 6 assessment share: 10 of the 25 validity, longitudinal, and forecasting course points.
- Decision owner: healthcare forecasting and operations-methods reviewer.
- Decision: does the introductory forecast beat its declared temporal benchmarks under a reproducible backtest, and what use does the public series not support?

### Technical outcome

The learner can define a forecast target and horizon, preserve time order, backtest against naive benchmarks, fit a guided smoothing model, choose error metrics, read an ARIMA-family example, and refuse operational claims that the source and evaluation cannot support.

### Content and mastery

| Concept | Required understanding | Mastery |
|---|---|---|
| Forecast aim and horizon | State target, unit, cutoff, horizon, refresh cadence, decision, and benchmark. | Core |
| Temporal split | Use only past information to predict later periods. | Core |
| Rolling-origin backtesting | Refit across declared time folds and preserve fold-level evidence. | Guided |
| Last-value baseline | Use the most recent observation as a minimum benchmark. | Guided |
| Seasonal-naive baseline | Use the same seasonal position when enough prior history exists and record when it does not. | Guided |
| Decomposition | Describe trend and seasonality without treating a decomposition as causal explanation. | Guided |
| Exponential smoothing | Fit a bounded trended or seasonal template and retain its parameters. | Guided |
| Stationarity | Explain why some model families need stable statistical structure and interpret a provided test. | Recognize |
| ARIMA family | Read autoregressive, moving-average, differencing, seasonal, and residual-check concepts from a provided example. | Recognize |
| Error metrics | Report MAE or RMSE in source units and use percentage metrics only when their denominator behavior is acceptable. | Guided |

### Forecast case

The learner forecasts Massachusetts weekly total respiratory new admissions in the pinned 94-week CDC NHSN series. Exact COVID-19, influenza, and RSV counts remain available, as do reporting-hospital counts and coverage percentages.

The final weeks are held out in time. The module will declare exact backtest folds during implementation after testing that every model has sufficient history. The source values, 94-row order, and 6,208-row full-release provenance cannot change to improve a result.

### Guided practice

Learners:

1. state the forecast aim, horizon, information cutoff, and possible decision;
2. define last-value and seasonal-naive eligibility;
3. create expanding-window folds;
4. fit each benchmark;
5. decompose the training series;
6. fit a guided exponential-smoothing candidate;
7. read a provided ARIMA-family result and residual checks;
8. report fold-level and aggregate errors;
9. inspect underprediction, overprediction, and seasonal failures;
10. relate errors to reporting coverage without applying an invented correction; and
11. issue a teaching-use, revise, specialist-referral, or stop recommendation.

### Exact learner release

The future runnable package must produce at least:

- source and rights record for the 6,208-row full release;
- exact 94-row Massachusetts modeling series;
- forecast target and horizon contract;
- temporal-fold registry;
- last-value predictions;
- seasonal-naive predictions or an explicit ineligibility record;
- smoothing-model predictions and parameters;
- provided ARIMA-family reading record;
- fold-level prediction table;
- benchmark and candidate error table;
- residual and failure table;
- exact reporting-coverage context;
- accessible forecast plot plus exact table and structured alternative;
- `forecasting-temporal-validation-memo.md`;
- reproduction and AI-use records; and
- validation output.

### Ten-point Week 6 share

| Criterion | Course points |
|---|---:|
| Forecast aim, target, horizon, cutoff, and time-ordered folds | 2.00 |
| Naive benchmarks and exact fold-level predictions | 2.00 |
| Guided model, error metrics, residuals, and comparison | 2.50 |
| Reporting coverage, failure analysis, limits, and recommendation | 2.00 |
| Accessible evidence, reproduction, and responsible agent record | 1.50 |
| Total | 10.00 |

### Noncompensable gates

- exact full and Massachusetts source fingerprints;
- all 94 weeks retained in order;
- future rows excluded from each fit;
- benchmark eligibility declared before candidate comparison;
- candidate compared on the same folds and targets;
- errors retain source units and denominators;
- no manual revision of source values or forecast misses;
- reporting coverage shown as context, not an invented correction weight;
- no single-hospital, stable-process, staffing, capacity, or operational claim;
- accessible exact table accompanies every forecast display;
- ARIMA remains recognition unless the released module explicitly expands mastery; and
- explicit Module 06 progression disposition.

### Handoff to Module 06

Module 06 receives the exact prediction and forecast pipelines, validity register, expected failures, source fingerprints, environment, metrics, and provisional recommendations. It tests them and audits agent assistance without changing accepted outputs silently.

## Module 06 brief: Agent-assisted modeling and testing

- Source week: 6.
- Learner work: 16.0 hours.
- Module ID target: `oclc-fnd2-06`.
- Initial module version target: 0.1.0.
- Course points: no added weight; its evidence is required inside the 25-point Week 6 checkpoint and the final 35-point package.
- Decision owner: responsible-AI and model-validation reviewer.
- Decision: do the model, data, metric, leakage, temporal, documentation, and agent-audit tests catch the failures they claim to catch, with a human owner for every material assisted step?

### Technical outcome

The learner can break an analytic task into bounded agent-safe steps, constrain prompts, test data and model invariants, seed known failures, adjudicate an agent critique, detect invented evidence, preserve a trace log, and sign off as the accountable analyst.

### Content and mastery

| Concept | Required understanding | Mastery |
|---|---|---|
| Task decomposition | Separate a modeling workflow into inputs, actions, evidence, and human decisions. | Core |
| Prompt constraints | State allowed files, data class, task, output format, prohibited claims, and required checks. | Core |
| Generation limits | Recognize unreliable statistical, causal, citation, metric, and code claims. | Guided |
| Data tests | Test grain, split, labels, roles, missingness, ranges, source fingerprints, and time order. | Guided |
| Model tests | Test pipeline fitting, prediction schema, metric arithmetic, calibration bins, threshold logic, and deterministic behavior. | Guided |
| Failure fixtures | Prove that tests fail on leakage, split contamination, future time, label inversion, wrong denominator, and fabricated evidence. | Core |
| Agent critique | Ask for bounded critique, map each claim to evidence, and accept, modify, or reject it. | Guided |
| Hallucination audit | Detect invented results, paths, citations, packages, performance, or approvals. | Core |
| Prompt and trace log | Preserve material prompts, summarized output, affected artifact, risk, independent check, result, action, and human owner. | Core |
| Human sign-off | Record that the learner, not the agent, owns the released decision. | Core |

### Required seeded failures

At minimum, the test suite must reject:

1. a post-index leakage field in predictors;
2. one test row included in fitting;
3. an outcome label inversion;
4. a changed split assignment;
5. a forecast fit that reads a future row;
6. a confusion matrix with a wrong denominator;
7. a calibration table that omits empty or sparse bins without disclosure;
8. a changed source fingerprint;
9. a missing model-card use boundary; and
10. an agent claim with no independent evidence.

### Guided practice

Learners:

1. write an agent-safe task plan;
2. classify every shared input by data class;
3. prompt an agent to suggest tests without sharing restricted data;
4. implement and run data and model tests;
5. inject each seeded failure and record expected rejection;
6. request one bounded model critique;
7. map every critique claim to evidence;
8. independently recalculate one material metric or data claim;
9. reject one unsupported agent statement; and
10. complete human sign-off.

### Exact learner release

The future runnable package must produce at least:

- agent task-decomposition plan;
- prompt constraints and data-class rules;
- prompt and trace log;
- data-test suite;
- model-test suite;
- forecast-test suite;
- ten seeded failure fixtures or deterministic mutations;
- failure-results registry;
- agent-critique record;
- claim-to-evidence adjudication table;
- one material independent verification record;
- human-sign-off record;
- test environment and ordered commands;
- accessible test summary;
- reproduction record; and
- validation output.

### Week 6 gate contribution

Module 06 adds no new course points. Checkpoint 2 cannot pass without:

- all declared tests passing on accepted work;
- all seeded failures being rejected;
- complete prompt and trace evidence;
- no prohibited data class shared;
- one material independent verification;
- explicit correction or retained action;
- a named human owner; and
- a signed recommendation that preserves all Module 04 and 05 conditions.

### Noncompensable gates

- accepted Module 03 through 05 evidence unchanged;
- tests inspect exact source, split, feature, prediction, metric, and time contracts;
- seeded failures fail for the intended reason;
- no test is rewritten merely to accept a failing artifact;
- agent critique is not treated as evidence;
- independent verification does not repeat the same prompt to the same system;
- material assistance is disclosed;
- protected, identifiable, workplace, restricted, secret, and credential data are prohibited;
- human sign-off is explicit; and
- explicit Week 6 checkpoint and Module 07 progression disposition.

### Handoff to Checkpoint 2 and Module 07

Checkpoint 2 freezes the exact Module 04 validity, Module 05 forecast, and Module 06 test and agent-accountability evidence as one 25-point release. Module 07 receives the accepted model, forecast, validity, tests, trace log, failures, conditions, and model-use boundary.

## Module 07 brief: Model cards, governance, and defense

- Source week: 7.
- Learner work: 16.0 hours.
- Module ID target: `oclc-fnd2-07`.
- Initial module version target: 0.1.0.
- Final assessment component: 35 course points.
- Decision owner: clinical analytics model-risk lead.
- Decision: can another reviewer reproduce, understand, govern, monitor, stop, and honestly limit the analysis, and what model use is permitted?

### Technical outcome

The learner can assemble accepted analytic evidence into a versioned package, write a model card, separate technical performance from use permission, define monitoring and stop rules, conduct a clean reproduction audit, and defend the package without overstating sparse synthetic evidence.

### Content and mastery

| Concept | Required understanding | Mastery |
|---|---|---|
| Model card | Record purpose, users, data, target, prediction time, model, evaluation, uncertainty, limitations, ethics, and ownership. | Core |
| Intended and prohibited use | Define what the model is for and what it must never decide. | Core |
| Performance evidence | Present baseline, discrimination, calibration, threshold, exact counts, uncertainty, and failure cases together. | Core |
| Subgroup and equity review | Preserve group definitions, sample and outcome counts, performance uncertainty, missingness, and unsupported comparisons. | Core |
| Monitoring | Define input, missingness, prevalence, calibration, performance, subgroup, system, and data-quality signals with owners. | Core |
| Drift | Distinguish data, label, calibration, concept, workflow, and population change. | Core |
| Retraining and versioning | State triggers, evidence, approval, comparison, rollback, and new-version requirements. | Core |
| Rollback, stop, and retirement | Name immediate stop events, safe fallback, notification, investigation, and retirement conditions. | Core |
| Reproducibility audit | Rebuild the package from a clean checkout and compare registered outputs. | Core |
| Technical defense | Explain aim, data, model, validity, performance, limits, agent use, governance, and recommendation under questioning. | Core |

### Model-card rule

The model card is not marketing copy. It must state that the case is synthetic, the test set contains four acute-return outcomes, subgroup estimates are sparse, and no clinical or operational use is authorized. It must show baseline and model evidence and may conclude that complexity does not improve the use decision.

### Monitoring-plan rule

The monitoring plan is a governed simulation for teaching. It must define signals, denominators, windows, thresholds or review triggers, owners, actions, and stop conditions. It cannot imply a deployed model or access to real patient outcomes.

### Guided practice

Learners:

1. reconcile every accepted component and condition;
2. draft the model card from registered evidence;
3. build a compact accessible performance appendix;
4. state intended, prohibited, and unsupported use;
5. write subgroup and equity limits;
6. define monitoring signals and data contracts;
7. define drift, retraining, rollback, stop, and retirement rules;
8. assemble a clean final candidate;
9. reproduce it from a new checkout or target;
10. deliver an eight-minute technical handoff;
11. answer ten required defense questions; and
12. recommend package disposition and model use separately.

### Exact learner release

The future runnable package must produce at least:

- repository README and navigation;
- semantic version, change log, release notes, commit, and proposed tag;
- exact environment and ordered commands;
- source, rights, and FND-1 handoff records;
- immutable input and output manifest;
- aim, estimand or target, prediction-time, feature, and split contracts;
- regression, prediction, calibration, threshold, subgroup, validity, and forecast evidence;
- tests, seeded-failure results, prompt and trace log, material AI audit, and human sign-off;
- `model-card.md`;
- `monitoring-plan.md`;
- `drift-retraining-versioning.md`;
- `rollback-stop-retirement.md`;
- `model-use-recommendation.md`;
- `reproducibility-audit.md`;
- accessible handoff brief and exact evidence tables;
- defense questions and responses;
- component score and release checklist;
- reviewer-ready disposition record; and
- complete validation output.

### Thirty-five-point draft rubric

| Criterion | Course points |
|---|---:|
| Aim, target, prediction time, model design, and baseline | 5.00 |
| Reproducible pipeline, environment, manifest, tests, and exact refit | 6.00 |
| Evaluation, calibration, thresholds, subgroup evidence, and failure analysis | 7.00 |
| Validity, uncertainty, data limits, and claim boundary | 5.00 |
| Model card, monitoring, drift, retraining, rollback, stop, and use recommendation | 6.00 |
| Responsible agent evidence, accessible handoff, defense, and final disposition | 6.00 |
| Total | 35.00 |

### Noncompensable gates

- accepted Checkpoint 1 and Checkpoint 2 inputs preserved;
- exact source, modeling cohort, split, label, feature, and pipeline identities;
- no leaked or future predictor;
- baseline and untouched-test evidence retained;
- exact metric numerators, denominators, and uncertainty retained;
- calibration and threshold evidence present;
- sparse test and subgroup outcomes visible;
- all validity conditions and specialist boundaries carried forward;
- forecast remains a separate public aggregate case;
- all tests and seeded-failure rejections pass;
- complete AI trace and material audit with human owner;
- model card states synthetic source and prohibited use;
- monitoring, retraining, rollback, stop, and retirement have owners and actions;
- accessible exact tables and structured alternatives accompany displays;
- clean reproduction and immutable manifest pass;
- defense is adequate;
- package disposition and model-use recommendation are separate; and
- no deployment, clinical efficacy, causal effect, fairness, or real-population claim.

### Handoff to the final checkpoint

The final checkpoint receives one complete Module 07 candidate. It freezes and adjudicates the candidate; it does not tune, refit, rewrite, or improve the model after defense. A material change returns to the owning module and requires a version decision.

## Checkpoint 1: Modeling-readiness and prediction-evaluation release

- Due: end of instructional Week 3.
- Cumulative hours: 48.0.
- Course points: 40.
- Components: Module 01 setup and aim classification, 15 points; Modules 02 and 03 regression and prediction, 25 points.
- Future package path: `courses/modeling-inference-reproducible-analytics/checkpoints/01-modeling-readiness-release/`.
- Decision owner: clinical prediction and model-risk reviewer with biostatistical support.
- Decision: may the locked modeling cohort, split, regression evidence, prediction pipeline, evaluation, and use boundary enter validity review?

### Exact checkpoint package

The cumulative release must contain:

- exact Module 01 through 03 IDs and versions;
- accepted FND-1 input identity and conditions;
- modeling cohort and data dictionary;
- aim, target, prediction-time, feature-role, and split contracts;
- baseline evidence;
- regression formulas, reference levels, coefficients, uncertainty, and diagnostics;
- registered preprocessing and prediction pipeline;
- training-resampling and validation comparison evidence;
- model-selection and threshold records;
- untouched test predictions and exact metrics;
- calibration, threshold, confusion, and subgroup tables;
- accessible displays and structured alternatives;
- leaked-model failure evidence;
- source, transformation, reproduction, accessibility, and AI-use records;
- cumulative interpretation memo;
- technical-defense record;
- 40-point component score;
- gate results; and
- `accept`, `accept with conditions`, `revise`, or `refer` disposition with Module 04 progression.

### Forty-point map

| ID | Criterion | Course points |
|---|---|---:|
| A01 | Decision, aim, target, population, time zero, and horizon | 4.00 |
| A02 | Exact input, feature roles, prediction-time boundary, and leakage control | 4.00 |
| A03 | Deterministic split, outcome reconciliation, and simple baseline | 3.00 |
| A04 | Reproducible workspace, environment, build, and initial agent record | 4.00 |
| R01 | Declared formulas, encodings, references, and correct regression fitting | 4.50 |
| R02 | Assumptions, sparse data, influence, uncertainty, and interpretation | 5.50 |
| P01 | Leakage-safe pipeline, resampling, validation comparison, and model lock | 4.50 |
| P02 | Untouched test discrimination, calibration, threshold, and confusion evidence | 4.50 |
| P03 | Subgroup counts, uncertainty, failure analysis, access, and use boundary | 3.50 |
| H01 | Cumulative handoff, defense, reviewer evidence, and progression decision | 1.50 |
| Total |  | 40.00 |

### Noncompensable gates

1. accepted FND-1 source, version, analytic-table fingerprint, and conditions;
2. one-row-per-person 374-row grain;
3. prediction time at index stop;
4. every source field assigned a role;
5. post-index and outcome leakage blocked;
6. exact 224, 75, and 75 split rows;
7. exact 25, 7, and 4 positive outcomes;
8. test split isolated from preprocessing, fitting, selection, and threshold choice;
9. training-prevalence baseline retained;
10. regression formulas and categorical references declared;
11. structural blanks not changed to zero;
12. odds, risks, and probabilities distinguished;
13. no causal effect claim from associational regression;
14. preprocessing and model represented as one reproducible pipeline;
15. validation comparison and selection rule recorded before test evaluation;
16. calibration, discrimination, threshold, confusion, prevalence, and exact counts reported;
17. subgroup sample and outcome counts reported before metrics;
18. leaked critique model rejected;
19. sparse four-positive test result visible in every decision summary;
20. source, transformation, reproduction, accessibility, and AI records complete;
21. no restricted data or real clinical performance claim;
22. adequate defense; and
23. explicit Module 04 progression.

### Defense questions

1. What decision is the model intended to inform in this teaching case?
2. What is the prediction time, outcome, and horizon?
3. Which fields are prohibited predictors and why?
4. How were the three temporal splits assigned and what are their positive counts?
5. What baseline must the candidate beat?
6. What does one linear or logistic coefficient mean here?
7. Which regression assumption or sparse-data condition matters most?
8. How did validation evidence select and lock the model and threshold?
9. What do discrimination and calibration each add?
10. What exact test counts support the threshold metrics?
11. Why are subgroup conclusions limited?
12. What would force revision before Module 04?

Only `accept` and `accept with conditions` permit Module 04.

## Checkpoint 2: Validity, forecast, testing, and agent-accountability release

- Due: end of instructional Week 6.
- Cumulative hours: 96.5.
- Course points: 25.
- Components: Module 04 validity and longitudinal work, 15 points; Module 05 forecasting, 10 points; Module 06 tests and agent evidence as required gates without added weight.
- Future package path: `courses/modeling-inference-reproducible-analytics/checkpoints/02-validity-forecast-testing-release/`.
- Decision owner: biostatistical validity and responsible-modeling panel.
- Decision: may the model and forecast evidence enter final governance packaging with their validity threats, failure tests, AI trace, and use limits intact?

### Exact checkpoint package

The cumulative release must contain:

- accepted Checkpoint 1 identity and conditions;
- aim and validity map;
- visual and structured DAG;
- causal-claim screen and variable-role register;
- overlap and balance evidence for the provided propensity example;
- missingness mechanism assumptions and sensitivity comparison;
- selection, repeated-measures, mixed-model, survival, and specialist-referral records;
- full 6,208-row CDC NHSN source identity and 94-row Massachusetts forecast series;
- forecast target, horizon, temporal folds, benchmarks, candidate, predictions, errors, residuals, and coverage context;
- accessible forecast display, exact table, and structured alternative;
- data, model, forecast, and documentation tests;
- ten seeded-failure results;
- prompt and trace log;
- agent critique and claim adjudication;
- material independent verification and human sign-off;
- source, transformation, reproduction, accessibility, and AI records;
- 25-point component score;
- gate results and defense record; and
- final-package progression disposition.

### Twenty-five-point map

| ID | Criterion | Course points |
|---|---|---:|
| V01 | Aim, estimand, DAG, variable roles, and causal-claim boundary | 4.00 |
| V02 | Confounding, overlap, balance, selection, and adjustment reasoning | 3.00 |
| V03 | Missingness assumptions, sensitivity, repeated measures, survival, and referral | 5.00 |
| F01 | Forecast aim, horizon, cutoff, folds, source fidelity, and benchmarks | 4.00 |
| F02 | Candidate forecast, errors, residuals, coverage context, and use limit | 4.00 |
| T01 | Data, model, forecast, and documentation test coverage | 2.00 |
| AI01 | Seeded failures, agent trace, adjudication, independent check, and human sign-off | 2.00 |
| H01 | Accessible cumulative memo, defense, conditions, and progression | 1.00 |
| Total |  | 25.00 |

### Noncompensable gates

1. accepted Checkpoint 1 input and split unchanged;
2. prediction and causal aims separated;
3. DAG has equivalent structured access;
4. variable roles and adjustment choice explicit;
5. no collider, mediator, post-outcome, or selection variable used without a defensible purpose;
6. propensity overlap and balance evidence present;
7. missingness mechanisms labeled assumptions;
8. structural blanks not changed to zero;
9. sensitivity analyses use the same target and declared population;
10. clustered, repeated, and censored structures handled or referred appropriately;
11. exact CDC source and Massachusetts fingerprints;
12. all 94 forecast weeks ordered and preserved;
13. every forecast fit excludes its future assessment period;
14. naive benchmarks retained;
15. errors use the same folds, targets, and units;
16. reporting coverage remains visible;
17. no single-hospital, stable-process, staffing, capacity, causal, or operational claim;
18. all accepted data, model, forecast, and documentation tests pass;
19. all ten seeded failures are rejected for the intended reason;
20. agent critique is adjudicated against independent evidence;
21. material assistance and data class are disclosed;
22. human sign-off is complete;
23. no restricted, identifiable, workplace, secret, or credential data;
24. adequate defense; and
25. explicit Module 07 progression.

### Defense questions

1. Which validity threat most changes the prediction claim?
2. Why is the DAG adjustment set not simply the prediction feature set?
3. What do overlap and balance show, and what do they not prove?
4. Which missingness assumptions are unverifiable from observed data?
5. Why do repeated measures or censoring require a different method?
6. What is the forecast target, horizon, and information cutoff?
7. Which naive benchmark is eligible and why?
8. How does temporal backtesting differ from random cross-validation?
9. How does reporting coverage limit the forecast?
10. Which seeded failure was most consequential?
11. What material agent claim was independently checked?
12. What must Module 07 preserve?

Only `accept` and `accept with conditions` permit Module 07.

## Final checkpoint: Governed analytics package and model-use decision

- Due: official last day of the assigned half-term.
- Cumulative hours: 112.5.
- Course points: 35.
- Future package path: `courses/modeling-inference-reproducible-analytics/checkpoints/03-governed-analytics-package/`.
- Decision owner: clinical analytics model-risk lead.
- Review panel: FND-2 faculty owner, biostatistical methods, clinical informatics, model evaluation, forecasting, accessibility, privacy and data governance, responsible AI, and independent reproduction.
- Decision: is the final package acceptable, and what use may the model support?

### Exact final package

The final release must freeze:

- accepted Checkpoint 1 and Checkpoint 2 evidence;
- exact Module 07 candidate and manifest;
- repository, full commit, semantic version, change log, release notes, and proposed annotated tag;
- ordered environment and reproduction commands;
- model-ready data, split, feature, prediction-time, and label contracts;
- formulas, pipelines, model parameters or deterministic refit contract;
- baseline, validation, test, calibration, threshold, subgroup, uncertainty, and failure evidence;
- DAG, validity threats, missingness sensitivity, longitudinal boundaries, and specialist referrals;
- forecast target, backtests, benchmarks, predictions, errors, residuals, and coverage limits;
- tests, seeded failures, prompt and trace log, material AI audit, and human sign-off;
- model card;
- intended, prohibited, and unsupported use;
- subgroup and equity review;
- monitoring plan;
- drift, retraining, version, rollback, stop, and retirement rules;
- source, rights, transformation, accessibility, reproduction, and reviewer records;
- accessible handoff brief, exact evidence appendix, and defense responses;
- final 35-point score;
- final gate results;
- package disposition; and
- separate model-use recommendation.

### Thirty-five-point map

| ID | Criterion | Course points |
|---|---|---:|
| M01 | Aim, target, prediction time, model design, and baseline | 5.00 |
| R01 | Reproducible pipeline, environment, manifest, tests, and exact refit | 6.00 |
| E01 | Evaluation, calibration, thresholds, subgroup evidence, and failure analysis | 7.00 |
| V01 | Validity, uncertainty, data limits, forecast limits, and claim boundary | 5.00 |
| G01 | Model card, monitoring, drift, retraining, rollback, stop, retirement, and use decision | 6.00 |
| H01 | Responsible agent evidence, accessible handoff, defense, reviewers, and disposition | 6.00 |
| Total |  | 35.00 |

Passing requires at least 28.00 points, every noncompensable gate, an adequate defense, an `accept` or `accept with conditions` package disposition, and an explicit model-use recommendation.

### Noncompensable gates

1. exact accepted versions of both cumulative checkpoints and Module 07;
2. exact final candidate manifest and protected assembly;
3. repository, full commit, semantic version, release notes, and proposed annotated tag;
4. exact synthetic and public source fingerprints and rights;
5. exact modeling cohort, prediction time, split, feature roles, and outcome counts;
6. no leakage or test contamination;
7. baseline and candidate comparisons use identical declared evaluation rows;
8. exact discrimination, calibration, threshold, confusion, prevalence, uncertainty, and subgroup evidence;
9. four-positive test limitation visible;
10. exact validity, DAG, missingness, longitudinal, and referral conditions;
11. exact forecast source, folds, benchmarks, errors, and coverage conditions;
12. all tests pass and all seeded failures are rejected;
13. complete agent trace, material independent audit, and human sign-off;
14. model card matches registered evidence;
15. intended and prohibited use explicit;
16. subgroup and equity review shows counts, missingness, uncertainty, and unsupported comparisons;
17. monitoring signals have denominators, windows, owners, triggers, and actions;
18. retraining requires new data, comparison, review, and semantic-version decision;
19. rollback, stop, and retirement identify safe fallback and notification;
20. accessible exact tables and structured alternatives accompany displays and DAGs;
21. no prohibited file, data class, personal path, secret, key, credential, or hidden dependency;
22. clean reproduction and output comparison pass;
23. named reviewer roles and condition ownership complete;
24. adequate technical defense;
25. package disposition recorded;
26. model-use recommendation recorded separately; and
27. no deployment, clinical efficacy, causal effect, fairness certification, stable-process, or real-population claim.

### Final defense questions

1. What decision, aim, target, prediction time, and horizon define the work?
2. What does one modeling row represent?
3. Which features are allowed, which are prohibited, and where is that enforced?
4. Why is the temporal split fixed, and what are the outcome counts?
5. Does the model beat the simple baseline, and on which evidence?
6. What do discrimination, calibration, and the selected threshold each say?
7. Which exact counts and uncertainty make the test result fragile?
8. Which subgroup comparison is least supportable and why?
9. Which validity threat most narrows the claim?
10. What does the public forecast support and prohibit?
11. Which test or seeded failure most protects the release?
12. What did an agent contribute and how was the material claim checked independently?
13. Which monitoring signal would trigger review first?
14. What event requires rollback or immediate stop?
15. Why can the package pass while the model recommendation remains `teaching use only`?

### Final outputs and tag rule

The final annotated tag target is defined when Module 07 and the final checkpoint are built. The tag must point to the exact reviewed commit after an allowed package disposition. A lightweight, early, or mismatched tag fails the release.

The final record states package disposition and model-use recommendation on separate machine-readable lines. An accepting package disposition cannot be read as deployment permission.

## Assessment weights

The Commons preserves every source assessment point exactly once:

| Source assessment | Feedback milestone | Cumulative checkpoint | Course points |
|---|---|---|---:|
| Reproducible modeling setup and aim classification | End of Week 1 | Checkpoint 1 at Week 3 | 15 |
| Regression and prediction labs | End of Week 3 | Checkpoint 1 at Week 3 | 25 |
| Validity, longitudinal, and forecasting memo | End of Week 5 | Checkpoint 2 at Week 6 with Module 06 accountability gates | 25 |
| Model or agent-assisted analytics package with model card | End of Week 7 | Final checkpoint on official half-term last day | 35 |
| Total |  |  | 100 |

Checkpoint packaging does not create extra grades. Module component scores are drafts until accepted inside the cumulative checkpoint that owns them.

## Shared grading criteria

The source names five criteria. The Commons operationalizes them without changing their meaning.

### Correct modeling

Evidence includes:

- correct target, unit, time zero, horizon, formula, pipeline, and comparison rows;
- correct fitting and prediction workflow;
- correct metric arithmetic and denominators;
- correct calibration, threshold, and forecast calculations;
- explicit assumptions and diagnostics; and
- tests that fail on known invalid work.

### Reproducible

Evidence includes:

- exact source, version, bytes, hashes, rows, and field identities;
- declared environment and ordered commands;
- code and configuration separated from generated outputs;
- fixed split and seed policy;
- protected output targets;
- immutable manifests;
- clean reruns and exact or explicitly tolerant comparisons; and
- semantic-version and change records.

### Sound analytic reasoning

Evidence includes:

- aim and method match;
- estimand or target clarity;
- prediction-time and leakage control;
- distinction among association, prediction, causation, longitudinal, and forecasting questions;
- validity-threat diagnosis;
- baseline comparison;
- uncertainty and sparse-data reasoning;
- specialist referral and stop decisions; and
- model-use recommendation tied to evidence.

### Clear and honest communication

Evidence includes:

- quantities, units, denominators, windows, and populations named;
- odds, risks, probabilities, rates, and forecast errors kept distinct;
- model and source limits prominent;
- accessible exact tables and structured alternatives;
- model card and monitoring plan written for the receiving reviewer;
- no promotional language or deployment implication; and
- unsupported conclusions stated explicitly.

### Responsible AI use

Evidence includes:

- permitted task and data class;
- prompt and trace record;
- material claim identification;
- independent method and exact evidence;
- result and correction or retained action;
- human owner and sign-off;
- no AI output used as evidence by itself; and
- no prohibited data shared.

## Reproducibility policy

Every module release must:

1. identify its accepted upstream versions and conditions;
2. verify every upstream file by byte count and SHA-256 when it crosses a release boundary;
3. build into a new target and refuse overwrite;
4. declare Python, R when used, system tools, packages, and tested platform;
5. record deterministic or bounded-random seed behavior;
6. separate fitting, selection, and untouched evaluation roles;
7. preserve exact formulas, preprocessing, feature names, reference levels, and parameters or a deterministic refit contract;
8. record generated outputs in a manifest;
9. rerun analysis noninteractively;
10. compare exact bytes where deterministic and declared numeric tolerances where a library produces platform-sensitive floating output;
11. explain every allowed tolerance and reject a result that crosses a decision boundary;
12. include source, transformation, reproduction, accessibility, and AI records;
13. refuse personal absolute paths, hidden caches, secrets, keys, local databases, source archives, and virtual environments in the release; and
14. receive a semantic-version decision before commit and push.

An environment that runs only from an instructor's existing machine state does not pass.

## Model and data validation policy

### Data invariants

At minimum, validators check:

- source and accepted upstream fingerprints;
- exact grain and unique keys;
- exact row and field counts;
- label vocabulary and counts;
- predictor timing roles;
- missingness and structural-blank rules;
- split assignments and counts;
- time order;
- subgroup counts;
- forecast dates and gaps;
- source-value preservation; and
- no prohibited field or file.

### Modeling invariants

At minimum, validators check:

- formulas and preprocessing contract;
- fitting rows and fit-time statistics;
- model and threshold selection timing;
- prediction row identities;
- probability range and schema;
- confusion arithmetic;
- metric denominators;
- calibration bin conservation;
- baseline comparison;
- subgroup conservation and suppression rules;
- forecast fold boundaries;
- benchmark eligibility;
- forecast errors; and
- final recommendation against gates.

### Failure tests

Every nontrivial builder or validator leaves a runnable self-check. Module 06 adds seeded failures across leakage, split contamination, label inversion, future-row access, wrong denominators, source changes, missing use boundaries, and unsupported agent claims.

### Statistical validation boundary

Passing automated checks establishes that declared computations and contracts agree. It does not establish clinical validity, causal identification, fairness, external validity, deployment safety, or prospective performance. Those decisions require suitable data, design, human review, and governance outside the public course.

## Accessibility and equity policy

Accessibility is a pass gate, not a style bonus.

### Tables and documents

- Markdown tables use explicit headers and simple reading order.
- CSV files keep stable column names, data dictionaries, and units.
- Model cards and memos use headings, short paragraphs, and links with descriptive text.
- Exact values remain available separately from figures.
- Color never carries the only meaning.

### Model and forecast displays

- calibration, threshold, subgroup, residual, and forecast displays include exact tables;
- PNG and SVG exports are accompanied by structured alternatives;
- axes, units, samples, time windows, thresholds, and source periods are explicit;
- uncertainty is not represented only by color or opacity;
- direct labels, line types, shapes, or text cues supplement color;
- reading order and zoom behavior are reviewed; and
- any point hidden by overplotting remains recoverable through the exact table.

### DAGs and model structures

- every visual DAG has node and edge tables or a complete text adjacency description;
- node roles are stated in text, not only by color;
- equations define every symbol in reading order;
- code output is summarized in accessible prose and tables; and
- a model diagram never replaces the feature and parameter contract.

### Defense access

Defense materials are available before review in accessible digital form. An equivalent written, recorded, or assisted defense route is allowed when needed without lowering the analytic standard.

### Equity and subgroup interpretation

The source race categories contain 308 white, 33 black, 27 Asian, 5 native, and 1 other synthetic person; source gender contains 236 F and 138 M. These are synthetic source values, not an inclusive representation standard. Sparse subgroups and only 36 total outcomes prevent strong comparative claims.

The course requires subgroup counts, outcome counts, missingness, performance uncertainty, and unsupported-comparison flags. It prohibits ranking sparse groups, treating absent categories as evidence of equity, or certifying fairness from the public reference.

## Privacy, security, rights, and data governance

### Allowed data

- accepted FND-1 Synthea synthetic data and documented derivations;
- public CDC NHSN aggregate data under its source terms;
- documented synthetic or public method fixtures; and
- learner-created tests and generated evidence that contain no real patient or restricted information.

### Prohibited data and files

- protected health information;
- identifiable patient or employee data;
- MGB, MIMIC, partner, workplace, or course data without explicit public-release authority;
- credentials, tokens, secrets, keys, certificates, or connection strings;
- local source ZIP files and generated SQLite databases in final release packages;
- cached model objects that cannot be traced or safely inspected;
- copied text, code, data, or models without source and rights records; and
- any restricted data sent to an external AI service.

### Public-course limitation

The Synthea case contains no real patients. The CDC case is an aggregate public jurisdiction-week release. Neither authorizes clinical action or creates an IRB-exempt path for local patient data.

### Model artifact safety

A serialized model is accepted only when the package documents its library and version, verifies its source, and provides a deterministic refit path. Validators must not load untrusted serialized objects merely to inspect them. Safe tabular parameters or registered formats are preferred when they meet the teaching need.

## Responsible AI and agent policy

### Permitted uses

- explain a bounded code or statistical concept;
- suggest tests;
- critique code, model evidence, model card, or monitoring plan;
- help diagnose an error;
- draft documentation from supplied verified facts; and
- compare code against a declared contract.

### Prohibited uses

- choose the final aim, method, threshold, model, or use recommendation without learner adjudication;
- fabricate code execution, performance, calibration, uncertainty, subgroup, forecast, citation, or review evidence;
- write a final defense response the learner cannot explain;
- bypass graded reasoning or submit unverified output;
- treat agreement from the same model as independent verification; and
- receive protected, identifiable, restricted, workplace, credential, secret, or key data.

### Required disclosure fields

Each material trace entry records:

- entry ID and date;
- tool and model;
- purpose;
- data class shared;
- request and response summary;
- affected artifact;
- risk if wrong;
- independent verification method;
- exact evidence;
- result;
- correction or retained action;
- human owner; and
- disclosure status.

### Material audit

At least one consequential agent-assisted claim must receive an independent audit. The audit names the claim, its analytic consequence, the independent method, exact evidence, result, action, and human owner. AI output is never evidence by itself.

## Healthcare interpretation and claim policy

### Supported teaching claims

The released course may claim that a learner can:

- classify analytic aims;
- enforce prediction-time and split contracts;
- fit and inspect bounded models;
- calculate and interpret declared evaluation evidence;
- recognize validity and specialist boundaries;
- build and backtest an introductory forecast;
- test pipelines and audit agent use;
- write a model card and monitoring plan; and
- defend a package and model-use recommendation.

### Unsupported real-world claims

The public reference cannot establish:

- real acute-return risk or predictor effects;
- a clinically valid score;
- treatment benefit or harm;
- causal identification;
- survival or longitudinal mastery;
- real subgroup equity or fairness;
- prospective calibration or transportability;
- one hospital's respiratory admissions, occupancy, staffing, capacity, quality, or trend;
- real operational forecast accuracy;
- production monitoring effectiveness;
- safe clinical decision support;
- deployment readiness; or
- regulatory, privacy, security, or governance approval.

### Language rules

- Use `association` unless causal design supports `effect`.
- Name odds, odds ratio, risk, probability, rate, count, and error by their actual quantity.
- Pair every metric with population, period, denominator, threshold, and uncertainty when available.
- Use `no encounter recorded` rather than `no encounter` when source coverage cannot prove absence.
- Use `selected synthetic cohort` rather than `patients at this hospital`.
- Use `teaching use only` rather than `ready to deploy` for the reference model.
- Use `reporting jurisdiction aggregate` rather than `hospital process` for the CDC series.

## Instructor interaction and feedback

The course includes:

- a weekly model-build walkthrough;
- paired Python and R examples where the source calls for R reading;
- a weekly model clinic that examines one invalid analysis;
- a question and debugging clinic;
- monitored asynchronous help;
- targeted feedback on the Week 1 aim and split;
- targeted feedback on Week 3 prediction evaluation;
- targeted feedback on Week 4 validity reasoning;
- targeted feedback on Week 5 forecast evidence;
- targeted feedback on Week 6 tests and agent adjudication; and
- a final technical defense.

Feedback focuses on the next decision. The instructor does not silently repair learner evidence or tune a model after test results are visible.

## Instructor package contract

Every runnable module must include:

- module README;
- durable 21-section module specification;
- source and rights record;
- data specification and dictionary;
- exact accepted upstream contract;
- worked example;
- guided lab;
- independent exercise;
- deliberately flawed or failure fixture;
- learner template;
- answer key or reference release;
- assessment and exact rubric;
- instructor notes with timing and interventions;
- accessible exact evidence and alternatives;
- build, analysis, and validation commands;
- standard-library validator where practical;
- self-check that rejects one intended failure;
- release metadata;
- required human-review roles;
- semantic version; and
- known issues and next handoff.

The instructor reference is technical evidence, not proof of faculty, clinical, statistical, accessibility, privacy, model-risk, or responsible-AI approval.

## Module specification contract

Each FND-2 module specification uses these 21 sections:

1. identity and role in the course;
2. technical decision and receiving audience;
3. FND-1 input and FND-2 handoff;
4. assessable outcomes;
5. concept ownership and out-of-scope boundaries;
6. lesson sequence and time;
7. readings and sources;
8. dataset inventory, provenance, rights, and teaching purpose;
9. data dictionary, prediction-time roles, and expected structure;
10. worked example;
11. guided practice;
12. independent exercise;
13. evaluation, visualization, or communication requirements;
14. exact submission package;
15. rubric, gates, and pass conditions;
16. common failures and instructor interventions;
17. accessibility, equity, privacy, model-safety, and claim checks;
18. AI policy, trace, independent verification, and human sign-off;
19. answer key and instructor notes;
20. runnable acceptance checks; and
21. release status, reviewers, version, known issues, and context handoff.

Each cumulative checkpoint specification uses a 17-section contract covering identity, decision, points, outcomes, ownership, workflow, accepted inputs, exact package, assembly, evidence, gates, reviewers, records, workflow, pass conditions, runnable checks, and release handoff.

## Release maturity

| Stage | Evidence required |
|---|---|
| Specified | Course or module specification defines outcomes, sources, work, assessment, validation, use boundaries, and handoff. |
| Runnable candidate | Data, code, analysis, tests, assessment, instructor notes, and automated checks run from a clean checkout. |
| Alpha | Faculty, methods, clinical meaning, model-risk, forecasting, accessibility, privacy, responsible-AI, and independent-instructor reviews are recorded. |
| Beta | The course or module has been taught once and timing, defects, model failures, and revisions are recorded without learner identifiers. |
| Stable | A second instructor or program has taught it successfully and no release-blocking issue remains. |

The course specification is complete. No FND-2 module is yet a runnable release candidate.

## Required human review roles

Before alpha promotion, record named decisions for:

- FND-2 faculty owner;
- biostatistics and regression foundations;
- clinical prediction and model-risk evaluation;
- causal, missing-data, and longitudinal-method boundaries;
- healthcare forecasting and temporal validation;
- clinical informatics and outcome meaning;
- Python and R teachability;
- reproducibility and software testing;
- accessibility;
- privacy, rights, and data governance;
- responsible AI and model governance; and
- independent reproduction and teachability.

One reviewer may cover multiple roles only when expertise and independence are recorded. The learner cannot be the final decision owner or independent reproducer.

## Release and version policy

### Course version

- Patch: wording, typo, link, or noncontractual clarification.
- Minor: compatible module, source, checkpoint, scaffold, metric, validator, or review expansion.
- Major: incompatible outcome, ownership, dataset, target, prediction time, split, assessment weight, package disposition, or model-use contract.

### Module version

Every module owns its semantic version. A changed source fingerprint, row role, split assignment, label definition, formula, preprocessing pipeline, metric, threshold, forecast fold, test gate, model-card field, or use rule requires an explicit version decision.

### Model version

A model version identifies source data, feature contract, split, code, package environment, fit configuration, parameters or refit recipe, evaluation, model card, and use recommendation. Retraining is a new model version even when code is unchanged.

### Source change

A source change requires:

- new source URL, access date, rights review, size, and fingerprint;
- row, field, unit, date, and missingness comparison;
- rebuilt modeling or forecast release;
- rerun feature, split, leakage, metric, and forecast validation;
- regenerated outputs and answer keys;
- reconsidered thresholds, subgroup evidence, monitoring, and use decision;
- updated model card and known issues;
- new semantic-version decisions; and
- human review when the decision could change.

Silent source refresh, resplitting, retuning on test evidence, and unrecorded retraining are prohibited.

## Build order

1. Module 01: Analytic aims and a reproducible modeling workspace.
2. Module 02: Regression models and interpretation.
3. Module 03: Prediction workflows and evaluation.
4. Checkpoint 1: Modeling-readiness and prediction-evaluation release.
5. Module 04: Adjustment, missing data, and longitudinal structure.
6. Module 05: Forecasting and temporal validation.
7. Module 06: Agent-assisted modeling and testing.
8. Checkpoint 2: Validity, forecast, testing, and agent-accountability release.
9. Module 07: Model cards, governance, and defense.
10. Final checkpoint: Governed analytics package and model-use decision.
11. Complete course-level human review and release wrapper.

Each completed unit updates `docs/curriculum/BUILD-LEDGER.md`, records source and validation facts, makes a semantic-version decision, runs its checks, commits, and pushes before the next unit begins.

## Runnable acceptance plan

The course-level checker verifies:

- source DOCX size and SHA-256;
- identical source in both supplied archives;
- seven exact module briefs;
- seven schedule rows totaling 112.5 hours;
- three cumulative checkpoints;
- source assessment weights totaling 100;
- separate FND-1 and FND-2 ownership;
- Core, Guided, and Recognize mastery boundaries;
- exact FND-1 analytic-table fingerprint and 374-row contract;
- 36 positive and 338 negative outcomes;
- temporal split rows of 224, 75, and 75;
- split positive counts of 25, 7, and 4;
- exact CDC full and Massachusetts release identities;
- official calendar URL and final-date rule;
- course package and source-record links;
- module and checkpoint paths;
- package and model-use decisions kept separate;
- no Unicode em dash or en dash in contract files;
- no learner-facing local absolute path; and
- release metadata as module packages are added.

Each module adds source, code, result, metric, access, failure, and release checks.

## Course acceptance checklist

- [x] FND-2 is a separate straight-through technical foundations course.
- [x] FND-1 and FND-2 ownership is explicit.
- [x] The source DOCX is fingerprinted and identical across both supplied packages.
- [x] Seven source modules and exact hours are preserved.
- [x] The course totals 112.5 hours.
- [x] Source assessments remain 15%, 25%, 25%, and 35%.
- [x] Week 3, Week 6, and official-end-date cumulative checkpoints are explicit.
- [x] Python is the graded modeling language and SQL supports model-ready extraction.
- [x] R remains read-run-interpret rather than from-scratch graded programming.
- [x] Core, Guided, and Recognize mastery levels are preserved.
- [x] The accepted FND-1 toolkit is the technical data prerequisite.
- [x] The 374-row synthetic prediction case has an exact prediction-time and leakage contract.
- [x] The fixed temporal split and its sparse positive counts are explicit.
- [x] The full public CDC forecasting release and 94-week teaching series are registered.
- [x] Regression, prediction, validity, forecasting, testing, agent use, model cards, governance, and defense are all owned.
- [x] Advanced ML, causal inference, mixed models, survival, and ARIMA-family work have bounded depth.
- [x] Package acceptance and model-use recommendation are separate decisions.
- [x] The reference result can pass technically while remaining teaching use only.
- [x] Model and forecast displays require accessible exact evidence.
- [x] Sparse subgroup evidence cannot become a fairness certification.
- [x] Monitoring and stop plans do not imply production deployment.
- [x] No real patient or restricted data enter the public course or external agents.
- [x] Every module has a future package path and handoff.
- [x] The 21-section module and 17-section checkpoint contracts are defined.
- [ ] Module 01 has a complete specification and runnable package.
- [ ] Module 02 has a complete specification and runnable package.
- [ ] Module 03 has a complete specification and runnable package.
- [ ] Checkpoint 1 is runnable.
- [ ] Module 04 has a complete specification and runnable package.
- [ ] Module 05 has a complete specification and runnable package.
- [ ] Module 06 has a complete specification and runnable package.
- [ ] Checkpoint 2 is runnable.
- [ ] Module 07 has a complete specification and runnable package.
- [ ] The final checkpoint is runnable.
- [ ] Named human reviews are recorded.
- [ ] The course has reached beta after a taught pilot.

## Remaining implementation decisions

These decisions do not block Module 01 specification and build:

1. Pin the smallest tested Python dependency set for each module rather than selecting one oversized course environment.
2. Choose the exact bounded machine-learning comparison in Module 03 after testing whether it adds teaching value beyond logistic regression and a constant baseline.
3. Finalize the decision-cost scenario and threshold rule before Module 03 test evaluation.
4. Select or generate the public or synthetic causal, repeated-measures, and survival fixtures for Module 04 with exact rights and role contracts.
5. Declare the exact Module 05 forecast horizon and expanding-window folds after confirming benchmark eligibility across all folds.
6. Define safe model serialization only if a serialized object is needed; prefer deterministic refit and transparent parameter records.
7. Name the faculty, statistical, clinical, model-risk, forecasting, accessibility, privacy, responsible-AI, and independent-instructor reviewers.

## Context-safe continuation

The FND-2 source is normalized and the course specification is complete at Commons 0.38.0. Resume with Module 01 only.

Read:

- this course specification;
- `docs/source/fnd-2-modeling-inference-reproducible-analytics-source-record.md`;
- `docs/curriculum/courses/FND-1/course-spec.md`;
- `courses/healthcare-data-foundations/checkpoints/03-reproducible-toolkit/release.json`;
- `courses/healthcare-data-foundations/modules/04-cleaning-profiling/release.json`;
- `docs/specs/2026-08-29-curriculum-master-architecture-spec.md`; and
- `docs/curriculum/BUILD-LEDGER.md`.

Then:

1. write the 21-section Module 01 specification;
2. preserve the accepted 374-row FND-1 table and exact fingerprint;
3. build the separate FND-2 modeling-cohort derivation;
4. assign all 29 source fields to explicit roles;
5. implement the fixed 224, 75, and 75 temporal split and reconcile 25, 7, and 4 positive outcomes;
6. compute the training-prevalence baseline;
7. create the aim-and-method exercise, feature contract, learner template, instructor key, and validator;
8. protect new targets and reject leakage, changed splits, and incomplete submissions;
9. update versions, checker, course status, and ledger; and
10. commit and push Module 01 before Module 02 begins.
