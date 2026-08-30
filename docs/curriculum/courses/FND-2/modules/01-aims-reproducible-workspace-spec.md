# FND-2 Module 01: Analytic aims and a reproducible modeling workspace

## 1. Module identity and place in the course

- Course: FND-2, Modeling, Inference, and Reproducible Analytics.
- Course role: second straight-through technical foundation after FND-1.
- Module: 01 of 07.
- Source week: 1.
- Learner work: 15.5 hours.
- Course credits: 3.
- Prerequisite: accepted FND-1 technical toolkit or an instructor-approved equivalent.
- Module ID: `oclc-fnd2-01`.
- Module version: 0.1.0.
- Commons release: 0.39.0.
- Status: runnable release candidate; required human reviews pending.
- Assessment role: 15 course points carried into the cumulative 40-point Week 3 checkpoint.
- Package: `courses/modeling-inference-reproducible-analytics/modules/01-aims-reproducible-workspace/`.
- Required learner tag: `fnd2-aims-v0.1.0`.
- Decision owner: senior quantitative analyst acting as modeling-workflow reviewer.
- Primary technical tools: Python 3.12, Python standard library, Git, CSV, JSON, Markdown, and the pinned FND-2 scientific environment.

FND-1 and FND-2 are separate straight-through technical foundations. FND-1 owns the trustworthy data layer: source retrieval, relational structure, cohort construction, cleaning, descriptive evidence, accessible handoff, and reproducible technical state. FND-2 begins only after that state is accepted. It owns the reasoning and controls required before fitting, interpreting, evaluating, testing, or governing statistical and machine-learning models.

Module 01 establishes the modeling contract. Learners do not begin with logistic regression, a notebook, or a package call. They begin with the decision that needs evidence, classify the analytic aim, state the target or estimand, freeze prediction time, declare field roles, make information leakage visible, assign a temporal split once, and register the minimum baseline.

The release question is:

> May this aim, data role, prediction-time boundary, feature contract, temporal split, baseline, and repository state enter regression and prediction work?

An affirmative answer allows Module 02 to use the exact artifacts. It does not approve a real clinical model or any operational use.

### Relationship to the course checkpoints

The accepted Module 01 state is frozen as the 15-point setup and aim-classification component of Checkpoint 1. Modules 02 and 03 later contribute the separate 25-point regression and prediction component. The cumulative Week 3 checkpoint is therefore 40 course points.

Module 01 is not rescored as a new assignment at Week 3. The accepted tag, exact outputs, disposition, and unresolved conditions are assembled into the checkpoint package.

The Week 6 checkpoint adds Modules 04 through 06 without changing the Module 01 source, split, or feature roles. The final checkpoint carries the same immutable contract into the governed analytics package.

### Relationship to the official half-term calendar

The curriculum uses seven instructional modules within official MGH Institute half-terms that span 49 to 52 elapsed days in the 2026-2027 academic calendar. "Seven and a half weeks" is the planning label. Submission dates must use the published start and last day for the actual offering.

Official calendar:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

### Required starting condition

The learner begins with:

- an accepted FND-1 toolkit and its conditions;
- the exact 374-row resolved analytic table;
- working knowledge of repository-relative paths, Python execution, Git state, CSV inspection, and reproducibility records;
- permission to use the synthetic source for open teaching; and
- no real patient record, credential, private URL, or restricted dataset in the workspace.

If a learner enters with equivalent preparation rather than the Commons FND-1 package, the instructor must provide a compatibility record that maps the local source, grain, fields, quality decision, and reproducibility state to this module's gates. An equivalent prerequisite does not permit silent substitution of the teaching data.

### Required ending condition

At the end of the module, the learner release must:

- identify the decision and analytic aim before naming a method;
- define the population, unit, time zero, prediction time, target, and 90-day horizon;
- verify the exact FND-1 input by byte count and SHA-256;
- preserve 374 unique people and 374 unique index encounters;
- classify all 29 source fields and five derivation fields;
- allow exactly nine default predictors;
- block post-index, outcome-derived, split, identity, and unsupported high-cardinality fields;
- preserve the deterministic 224/75/75 temporal split;
- reconcile 25/7/4 acute-return positives;
- freeze the training-prevalence baseline at `0.111607142857`;
- preserve an exact dependency and environment record;
- rebuild into a clean target without overwrite;
- pass submission validation;
- state an allowed progression disposition; and
- identify every condition inherited by Module 02.

## 2. Technical decision, owner, and audiences

### Decision owner

The decision owner is a senior quantitative analyst acting as modeling-workflow reviewer. The role may be filled by course faculty or a delegated reviewer with enough statistical and data-governance knowledge to evaluate the question, information boundary, and release evidence.

The owner is accountable for the disposition. Automated checks, teaching assistants, AI systems, and peer reviewers may supply evidence but do not own the release decision.

### Technical decision

The reviewer decides whether the package is coherent and reproducible enough for Module 02 to estimate and interpret bounded regression models without silently changing the accepted cohort or using information that was unavailable at prediction time.

The decision covers:

1. question and decision fit;
2. aim classification;
3. target or estimand completeness;
4. method-family fit;
5. source identity and grain;
6. prediction time;
7. feature roles;
8. leakage controls;
9. split roles and assignments;
10. baseline definition;
11. environment and build reproducibility;
12. responsible AI and data boundaries; and
13. exact downstream handoff.

It does not decide:

- whether a real person will return for acute care;
- whether an intervention would prevent a return;
- whether a hospital or clinician performs well;
- whether the synthetic data represent a real population;
- whether a candidate model is calibrated, fair, useful, or deployable;
- whether a forecast is operationally reliable; or
- whether an analytic package may be used in clinical care.

### Allowed dispositions

| Disposition | Meaning | Required next action |
|---|---|---|
| `accept` | Every gate passes and no material condition remains for Module 02. | Freeze the tagged state and begin Module 02. |
| `accept with conditions` | Every gate passes but bounded source, precision, reporting, or review conditions remain. | Name each condition, owner, and effect; freeze the state and begin Module 02 under those conditions. |
| `revise` | A correctable question, role, split, documentation, environment, or reproduction defect prevents safe progression. | Correct the defect, rerun all outputs and checks, make a version decision, and resubmit. |
| `refer` | The package contains or may expose protected data, credentials, unauthorized access, material integrity concerns, or a decision outside the reviewer's authority. | Stop reuse and send the issue to the appropriate privacy, security, access, integrity, clinical, or methods process. |

Only `accept` and `accept with conditions` allow Module 02 progression.

### Primary learner audience

The primary audience is a clinician, researcher, quality professional, analyst, or health-system staff member entering graduate healthcare analytics after FND-1. Learners may have uneven prior exposure to statistics and modeling. The module therefore requires precision without assuming that learners already know the vocabulary needed to ask the right question.

The module assumes learners can execute supplied Python and inspect data. It does not assume they can already:

- distinguish an estimand from a prediction target;
- tell association from causation;
- recognize that forecasting and person-level prediction are different data structures;
- identify when a date or label leaks future information;
- explain train, validation, and test responsibilities;
- preserve a split as a versioned artifact;
- establish a baseline before fitting a candidate; or
- constrain an AI system to the same information boundary as a human analyst.

### Review and receiving audiences

The release must also make sense to:

- an instructor scoring the 15-point component;
- a teaching assistant diagnosing an aim or leakage error;
- a quantitative methods reviewer checking target and method fit;
- a clinical informatics reviewer checking timing and field meaning;
- a data engineer checking source, grain, and transformations;
- a privacy reviewer checking identifiers and data boundaries;
- a responsible-AI reviewer checking disclosure and human control;
- an accessibility reviewer checking alternate routes and readable records;
- a second learner reproducing the package; and
- the Module 02 instructor inheriting the exact modeling contract.

### Decision evidence

The reviewer uses six evidence classes:

1. analytic evidence in the aim plan and target registry;
2. data evidence in the source record, fingerprint, cohort, and field-role contract;
3. temporal evidence in prediction time, split assignment, and date reconciliation;
4. baseline evidence calculated from training rows only;
5. reproducibility evidence from code, environment, outputs, and clean-target checks; and
6. accountability evidence in the progression, AI-use, and review records.

A passing validator is necessary technical evidence. It cannot determine whether the aim is worth pursuing, whether an unmeasured clinical concept matters, or whether a human decision owner accepts the claim boundary.

### Oral clarification route

When authorship or understanding is unclear, the reviewer may ask the learner to:

- classify one unfamiliar request and reject a mismatched method;
- identify prediction time for a selected row;
- explain why `next_30d_state` is invalid even when highly predictive;
- show which training rows establish the baseline;
- explain what validation may influence and what test may not influence;
- state what four positive test outcomes imply;
- distinguish source verification from model validity;
- explain one AI-generated suggestion and its independent check; and
- identify a change that forces a versioned return to Module 01.

The oral check clarifies submitted evidence. It is not an unannounced extra grading category.

## 3. Foundation skill and exact handoff

### Foundation skill

The learner turns an accepted analytic table and a broad healthcare request into a bounded, versioned modeling contract. The contract connects the question to the evidence without allowing method availability to redefine the question.

The foundation skill has eight connected habits:

1. name the decision and audience;
2. classify the analytic aim;
3. register the target or estimand;
4. freeze the information boundary at prediction time;
5. assign every field a role;
6. partition data according to the use case and preserve the split;
7. establish a minimum baseline before candidate modeling; and
8. make the entire state reproducible and reviewable.

### Why this belongs in FND-2

FND-2 owns modeling and inference fundamentals. A technically clean table is not automatically suitable for regression, prediction, causal inference, longitudinal analysis, or forecasting. Each aim asks a different question and requires different data structure, assumptions, evaluation, and interpretation.

This module prevents a common failure: selecting a familiar method and then rewriting the question to fit the output. It also prevents a second failure: allowing information created after the decision time to enter a model and inflate apparent performance.

### Upstream FND-1 handoff

The exact upstream artifact is:

`courses/healthcare-data-foundations/modules/04-cleaning-profiling/outputs/resolved-analytic-table.csv`

Its immutable contract is:

- 374 rows;
- 29 fields;
- one unique synthetic patient per row;
- one unique selected index encounter per row;
- 121787 bytes;
- SHA-256 `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a`;
- source release `synthea-csv-apr2020`;
- cohort definition 0.1.0;
- upstream disposition `proceed with conditions`; and
- no real patient records.

Module 01 may verify, copy, order, label, and append registered metadata. It may not:

- change cohort eligibility;
- delete supported rows;
- impute source fields;
- edit an accepted value;
- recalculate follow-up states;
- resolve a natural source condition silently;
- substitute a refreshed source; or
- claim the synthetic cohort represents a real population.

### Handoff into Module 02

Module 02 receives:

- `modeling-cohort.csv`;
- `split-registry.csv`;
- `baseline-metrics.csv`;
- `feature-role-contract.csv`;
- `estimand-target-registry.csv`;
- `aim-and-method-plan.md`;
- `source-record.yml`;
- `data-spec.md`;
- `requirements.txt`;
- `environment-note.md`;
- `reproducibility-check.md`;
- `progression-decision.md`;
- `outputs/build-report.json`;
- `outputs/modeling-checks.csv`;
- builder and validator code;
- module version 0.1.0; and
- every unresolved condition.

Module 02 may assume the exact source, roles, temporal split, and baseline. It may not assume that an association is causal, a coefficient is a prediction metric, the data are representative, the test split is precise, or an accepted package is suitable for deployment.

### Return conditions

Work returns to Module 01 when any of the following changes:

- decision or primary aim;
- population or unit;
- time zero or prediction time;
- label or horizon;
- source row, field, byte count, or fingerprint;
- allowed predictor set;
- excluded or leakage-field role;
- split ordering or assignment;
- baseline definition;
- source-use permission;
- package contract; or
- a condition that materially changes progression.

A return requires a new reviewer disposition and semantic-version decision. Rebuilding unchanged outputs after a software patch does not automatically change the analytic contract, but the environment record and checks must still be updated.

## 4. Assessable outcomes and evidence map

By the end of Module 01, the learner can:

1. state a healthcare analytics decision without starting from a software method;
2. identify who decides, what action is possible, what evidence is needed, and what the analysis will not decide;
3. distinguish descriptive, associational, predictive, causal, longitudinal, and forecasting aims;
4. classify a new request and explain why at least one attractive method is mismatched;
5. distinguish a prediction target from an estimand that includes a contrast;
6. state population, unit, time zero, exposure or predictors, outcome, horizon, and success criterion;
7. match an aim to a bounded method family;
8. recognize when the available data structure cannot support the stated aim;
9. verify source byte count, SHA-256, row count, field count, and grain;
10. distinguish source values from registered derivation metadata;
11. state prediction time before examining candidate predictors;
12. identify post-index, outcome-derived, split-derived, preprocessing, identity, and duplicate leakage;
13. assign all 29 source fields and five derivation fields one explicit role;
14. defend the nine-field default predictor set;
15. explain why high-cardinality codes and optional reasons require a separate plan;
16. build a deterministic temporal ordering by `index_start` and `patient_id`;
17. reconcile 224 train, 75 validation, and 75 test rows;
18. reconcile 25, 7, and 4 positive outcomes without using test outcomes for selection;
19. explain the distinct responsibility of train, validation, and test data;
20. explain why a small test event count narrows claims rather than authorizing resplitting;
21. calculate and freeze the training-prevalence baseline;
22. distinguish a baseline definition from later performance metrics;
23. create and use an exact dependency record;
24. rebuild all deterministic artifacts from a clean target;
25. demonstrate existing-target refusal;
26. interpret validator evidence without equating it with clinical validity;
27. disclose material AI assistance and describe an independent check;
28. keep protected data, credentials, and local absolute paths out of the release;
29. make one allowed progression disposition; and
30. hand Module 02 an exact versioned package with conditions.

### Outcome-to-evidence map

| Outcome area | Direct evidence | Supporting evidence |
|---|---|---|
| Decision and aim | `aim-and-method-plan.md` | oral classification check |
| Six aim classes | `estimand-target-registry.csv` | twelve practice requests |
| Source identity | `source-record.yml` and build report | copied source and validator |
| Prediction time | aim plan and feature contract | row-level oral explanation |
| Field roles | `feature-role-contract.csv` | leakage critique discussion |
| Temporal split | `split-registry.csv` | modeling cohort and checks |
| Baseline | `baseline-metrics.csv` | learner calculation explanation |
| Reproducibility | build code and environment note | clean-target record |
| Accountability | AI-use and progression records | reviewer disposition |
| Module 02 handoff | tagged package and file list | checkpoint assembly record |

### Minimum explanation standard

An answer must name the mechanism or evidence. "The field leaks" is incomplete unless the learner states what information it contains, when it becomes known, and how using it would change the apparent result. "The split is reproducible" is incomplete unless the learner states the ordering, positions, counts, date ranges, and conditions that would force a new version.

## 5. Concept ownership and out-of-scope boundaries

### Module 01 owns

- decision statements;
- analytic question classification;
- descriptive, associational, predictive, causal, longitudinal, and forecasting distinctions;
- target and estimand elements;
- method-family matching;
- data-sufficiency recognition;
- unit of analysis;
- time zero and prediction time;
- outcome horizon;
- source identity and immutable handoff verification;
- field roles;
- allowed predictors;
- default exclusions;
- leakage detection and blocking;
- temporal partition design;
- train, validation, and test responsibilities;
- split immutability;
- training-prevalence baseline registration;
- exact environment and ordered build state;
- AI-use disclosure at the modeling boundary; and
- Module 02 progression disposition.

### Module 01 introduces but does not teach to mastery

- regression as an associational or predictive method family;
- logistic regression as a bounded candidate pipeline;
- regularization and tree methods as later machine-learning baselines;
- calibration, discrimination, thresholding, and subgroup review as later evaluation responsibilities;
- causal identification as more than adding covariates;
- repeated-measures methods as requiring repeated observations;
- forecasting as requiring ordered aggregate time; and
- model governance as a later release responsibility.

These ideas appear so learners can reject mismatched methods. Their technical execution belongs to later modules.

### Module 01 does not own

- coefficient estimation or regression diagnostics;
- p-values, inferential intervals, or multiplicity;
- logistic-regression fitting;
- resampling, cross-validation, or hyperparameter tuning;
- candidate-model comparison;
- test-set performance calculation;
- calibration curves or threshold selection;
- machine-learning training;
- causal graph construction or identification;
- missing-data modeling or imputation;
- clustered, repeated, or longitudinal estimation;
- time-series forecasting;
- model cards, monitoring, deployment, or clinical decision support;
- the concept-first data-visualization curriculum; or
- leadership teaching by the clinician faculty member.

### Separation from FND-1

FND-1 owns whether the source, relational structure, cohort, cleaning, descriptive evidence, and technical handoff are trustworthy. Module 01 does not reteach that sequence. It verifies and inherits the accepted result, then asks what modeling question that result can support.

If the source or grain is wrong, the work returns to FND-1. FND-2 does not repair upstream facts inside a model pipeline.

### Separation from DA-730

DA-730 teaches visual perception, encoding, chart selection, uncertainty display, accessibility, dashboards, and decision stories. This module may display a readable table or simple count for inspection, but it does not assess visual-design competence.

### Separation from application courses

Application courses revisit statistics and modeling through different domain decisions. This foundation owns the general aim and information-boundary contract. An application course may specialize the population, outcome, workflow, or public clinical source. It may not silently redefine these fundamentals.

## 6. Lesson sequence and learner time

| Sequence | Learning activity | Hours | Required evidence |
|---:|---|---:|---|
| 1 | Course and FND-1 handoff orientation | 0.75 | prerequisite and source-use check |
| 2 | Source fingerprint and grain verification | 0.75 | exact byte, hash, row, field, and key evidence |
| 3 | Six-way aim taxonomy seminar | 1.50 | worked classifications and method rejections |
| 4 | Decision, target, and estimand workshop | 1.50 | draft aim and target registry |
| 5 | Prediction time and information-availability lab | 1.25 | row-level timing annotation |
| 6 | Leakage families and deliberate failure critique | 1.25 | leakage findings and corrected boundary |
| 7 | Feature-role contract lab | 2.00 | 34-row role table |
| 8 | Temporal ordering and split build | 1.50 | modeling cohort and split registry |
| 9 | Split-role and small-test discussion | 0.75 | train/validation/test explanation |
| 10 | Baseline registration | 0.50 | exact training-prevalence record |
| 11 | Reproducible environment and clean build | 1.25 | environment note and rerun evidence |
| 12 | Twelve-request independent practice | 1.00 | completed exercise table |
| 13 | Release assembly, validation, and defense | 1.50 | passing package and progression decision |
| Total |  | 15.50 |  |

### Suggested teaching rhythm

Use short explanations followed by immediate classification or field decisions. Learners should repeatedly answer four questions:

1. What decision is being made?
2. What type of analytic aim is this?
3. What information exists at the decision time?
4. What claim can the available data support?

The week should not become a lecture-only taxonomy. Every concept must reach a concrete row, field, split, artifact, or decision.

### Checkpoints within the week

| Point | Instructor check | Required correction before continuing |
|---|---|---|
| After aim workshop | primary request classified and target complete | aim or target mismatch |
| After prediction-time lab | prediction time and blocked future fields explicit | missing or shifting information boundary |
| After role lab | all 34 fields assigned exactly once | unassigned field or leakage allowed |
| After split build | counts and date ranges reconcile | changed order, count, or assignment |
| Before release | baseline and build state frozen | baseline fit outside train or unresolved prompts |

## 7. Aim taxonomy and method-family map

### Descriptive aim

A descriptive aim asks what was observed in a defined dataset, population, place, and time. It requires explicit denominators and measurement boundaries. It does not estimate what would happen to a new person, what would happen under an intervention, or what will occur at a future aggregate time.

Example:

> Among the 374 accepted synthetic cohort members, how many and what proportion had a recorded acute return within 90 days?

Appropriate method family: counts, proportions, distributions, and descriptive uncertainty when justified.

### Associational aim

An associational aim asks how an outcome varies with one or more variables under a declared model. The coefficient is conditional on the model, coding, reference groups, and included adjustment set. Association does not become causation because the model contains many covariates.

Example:

> In the accepted synthetic cohort, what is the conditional association between index encounter class and recorded 90-day acute return under a declared adjustment model?

Appropriate method family: regression with explicit formula, coding, assumptions, diagnostics, and bounded interpretation.

### Predictive aim

A predictive aim asks how well information available at a defined prediction time estimates a later outcome for new or held-out rows from a declared use context. Evaluation, calibration, threshold consequences, and information leakage matter more than coefficient significance.

Example:

> At index encounter stop, what is the estimated probability of a different emergency or inpatient encounter within 90 days?

Appropriate method family: a reproducible prediction pipeline compared with a declared baseline using validation evidence and one final untouched test evaluation.

### Causal aim

A causal aim asks what outcome would differ under one intervention, exposure, or strategy compared with another. It requires a causal contrast, time order, consistency, exchangeability or an alternative identification strategy, positivity, and a design that supports the claim.

Example:

> What would the 90-day acute-return rate have been if every eligible person received discharge navigation compared with usual care?

The current source does not contain the required intervention assignment or design. Ordinary regression cannot create the missing causal identification.

### Longitudinal aim

A longitudinal aim asks about within-person or clustered change across repeated observations. It requires repeated measurements, a time scale, correlation structure, missingness reasoning, and a distinction between within-person and between-person information.

Example:

> How does utilization change within a person over quarterly observations, and do trajectories differ by a declared group?

The current 374-row cohort has one modeling row per person. It cannot answer this aim without a separate repeated-measures structure.

### Forecasting aim

A forecasting aim asks about future values of an ordered aggregate series using information available by an issue date. It requires a time index, forecast horizon, temporal folds, benchmarks, errors with units, and context about reporting changes.

Example:

> How many Massachusetts aggregate respiratory admissions will be reported one to four weeks after a declared issue date?

This aim uses the separate pinned CDC NHSN weekly series in Module 05. The person-level FND-1 table is not converted into a forecast series for convenience.

### Method-family rejection rule

For every classified request, the learner must name at least one method family that appears plausible but does not answer the question. A valid rejection states the mismatch:

- wrong unit;
- wrong time structure;
- no intervention contrast;
- no repeated observations;
- no held-out prediction decision;
- descriptive output mistaken for inference; or
- prediction performance mistaken for causal effect.

The goal is not to prove that only one algorithm could ever be used. The goal is to prevent a method from answering a different question without acknowledgment.

## 8. Worked case and guided practice

### Continuing case

The continuing prediction case uses the exact accepted FND-1 table. One row represents one selected synthetic adult and one emergency or inpatient index encounter. The decision time is the stop of that encounter. The registered outcome is a different emergency or inpatient encounter within the next 90 days.

The source contains 36 positive and 338 negative labels. The case is intentionally small. It is large enough to demonstrate the full workflow and small enough for learners to inspect every field and reconcile every split.

### Worked request 1: descriptive

Request:

> Tell the service team how often a recorded acute return occurred in the accepted cohort.

Instructor reasoning:

- Decision: understand what the accepted synthetic cohort contains.
- Aim: descriptive.
- Unit: person-index row.
- Outcome: `acute_return_90d`.
- Horizon: 90 days after index stop.
- Method family: count and proportion with exact denominator.
- Rejected method: a classifier is unnecessary because no new-row prediction is requested.
- Claim boundary: the result describes this synthetic cohort only.

### Worked request 2: associational

Request:

> Estimate how recorded 90-day acute return varies with index class after declared adjustment.

Instructor reasoning:

- Decision: explain a bounded conditional relationship.
- Aim: associational.
- Unit: person-index row.
- Exposure: `index_class`.
- Outcome: `acute_return_90d`.
- Method family: regression with reference levels, formula, uncertainty, assumptions, and diagnostics.
- Rejected method: a causal effect model is not identified by covariate adjustment alone.
- Claim boundary: no claim that changing index class would change the outcome.

### Worked request 3: predictive

Request:

> At index stop, estimate which synthetic cohort members will have a recorded acute return within 90 days.

Instructor reasoning:

- Decision: compare a future-outcome probability with a predeclared baseline.
- Aim: predictive.
- Prediction time: `index_stop`.
- Predictors: nine approved pre-prediction fields.
- Label: `acute_return_90d`.
- Horizon: 90 days.
- Method family: a pipeline fit on train, selected with validation, and evaluated once on test.
- Rejected method: p-values from an associational model do not establish prediction performance.
- Claim boundary: teaching use only.

### Worked request 4: causal

Request:

> Determine whether discharge navigation would prevent acute returns.

Instructor reasoning:

- Decision: choose or evaluate an intervention.
- Aim: causal.
- Contrast: navigation versus a declared comparison strategy.
- Outcome: 90-day acute return.
- Required evidence: intervention definition, assignment mechanism, confounding plan, time ordering, and identification assumptions.
- Current status: unsupported by the accepted table.
- Rejected method: adding the nine predictors to logistic regression does not create intervention exchangeability.

### Worked request 5: longitudinal

Request:

> Determine whether a person's utilization changes across quarterly follow-up.

Instructor reasoning:

- Decision: understand repeated within-person change.
- Aim: longitudinal.
- Required unit: person-time row with repeated scheduled observations.
- Current unit: one row per person-index encounter.
- Current status: unsupported.
- Rejected method: treating four prior-use counts as repeated outcome observations.

### Worked request 6: forecasting

Request:

> Forecast Massachusetts respiratory admissions four weeks ahead.

Instructor reasoning:

- Decision: anticipate future aggregate reported values.
- Aim: forecasting.
- Required unit: jurisdiction-week.
- Source: pinned CDC NHSN weekly release used in Module 05.
- Required time boundary: issue date and information cutoff.
- Rejected method: person-level classification using the synthetic cohort.
- Claim boundary: public teaching forecast and no operational use.

### Guided source verification

Learners run the supplied builder's source verification and then explain the evidence rather than copying the pass marker. Required observed facts are:

- file size 121787 bytes;
- SHA-256 `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a`;
- 374 data rows;
- 29 fields in the registered order;
- 374 distinct patient IDs;
- 374 distinct index encounter IDs;
- 36 positive and 338 negative acute-return labels;
- source release `synthea-csv-apr2020`; and
- cohort-definition version 0.1.0.

### Guided prediction-time walk-through

Select one source row and draw a simple timeline:

```text
birth and pre-index history -> index start -> index stop / prediction time -> 90-day outcome window
```

For that row, learners place each field on or around the timeline. They must distinguish:

- facts already known;
- identifiers used only to track the row;
- fields that define the time boundary;
- fields occurring after prediction time;
- the registered label;
- metadata added by the modeling build; and
- fields whose use requires a separate approval.

### Guided leakage critique

The instructor provides an invalid candidate list that includes:

- `next_30d_state`;
- `endpoint_90d`;
- `split`;
- `patient_id`; and
- a standardized age value fit on all rows.

Learners identify five different failures:

1. post-index leakage;
2. outcome-derived leakage;
3. split-derived leakage;
4. identity or memorization risk; and
5. preprocessing leakage.

The invalid list is a critique fixture. It is never labeled a candidate for release.

### Guided split build

Learners inspect the sort keys and assignment positions. The instructor asks them to predict why a random stratified split would be attractive and why it would answer a different transport question. The class then reconciles:

- train positions 1 through 224;
- validation positions 225 through 299;
- test positions 300 through 374;
- date boundaries;
- row totals;
- label totals; and
- stable row IDs.

### Guided baseline build

Learners calculate:

```text
training positives / training rows = 25 / 224 = 0.111607142857
```

They record the value before seeing a candidate model. They explain that it is a constant probability, not an accurate clinical risk model and not a final threshold recommendation.

## 9. Independent practice and transfer tasks

### Twelve-request classification task

Learners complete `aim-classification-exercises.csv`. Each row requires:

- one of the six aim classes;
- a reason tied to decision, unit, time, contrast, or evaluation;
- one rejected method family; and
- an explanation of the mismatch.

The twelve requests contain two examples of each aim class. The instructor answer key is in `instructor-notes.md`. A learner may reject a different method than the key when the reasoning is correct.

### Six-row target or estimand registry

Learners complete one row for each aim class. Each row must state:

- request;
- aim;
- population;
- unit;
- time zero;
- exposure or predictors;
- outcome;
- horizon;
- contrast or success criterion;
- method family; and
- whether the current data support the aim.

For descriptive, predictive, and forecasting aims, the `contrast_or_success_criterion` field states the exact comparison or evaluation rule. For associational and causal aims, it states the coefficient or counterfactual contrast. For longitudinal work, it states the within-person or trajectory contrast.

### Feature-role defense

The learner completes all 34 rows without grouping unreviewed fields into "other." For five instructor-selected fields, the learner must defend:

- when the value becomes known;
- whether it can enter the default model;
- whether it is blocked or conditionally excluded;
- what failure would occur if the role changed; and
- which later module may revisit it.

At least one defense must cover an ID, a time field, a high-cardinality field, a post-index field, and a derived split field.

### Split reconstruction task

Without copying counts from prose, learners use the generated registry to calculate split rows, positive outcomes, negative outcomes, and date ranges. Their values must reconcile with the build report and checks.

The learner then answers:

1. Why is the split temporal rather than random?
2. Why does `patient_id` appear as a tie breaker?
3. What may validation evidence change?
4. What may test evidence change?
5. When is the test set opened?
6. Why are four positives a limitation rather than a defect?

### Transfer scenario

Provide a new open healthcare dataset description without its records. Ask learners to draft only:

- the decision statement;
- likely unit;
- time zero;
- candidate outcome and horizon;
- prediction time;
- three likely leakage risks;
- an appropriate split family; and
- evidence required before modeling.

The learner must not fabricate a model, result, or performance claim from the description.

### Reproduction task

The learner builds the package into a new target, confirms that a second build to the same target is refused, validates starter state, completes the records, and validates submission state. The reproduction record preserves failed commands and their resolution.

## 10. Data source, provenance, rights, and claim boundary

### Source lineage

The original source system is Synthea, an open synthetic-patient generator. FND-1 pinned and transformed the source into an accepted analytic table. FND-2 does not return to the raw archive for this case; it inherits the accepted table through a registered handoff.

Source landing page:

https://synthea.mitre.org/downloads

Source CSV dictionary:

https://github.com/synthetichealth/synthea/wiki/CSV-File-Data-Dictionary

### Exact input identity

| Property | Value |
|---|---|
| Repository path | `courses/healthcare-data-foundations/modules/04-cleaning-profiling/outputs/resolved-analytic-table.csv` |
| Rows | 374 |
| Fields | 29 |
| Bytes | 121787 |
| SHA-256 | `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a` |
| Grain | one selected synthetic adult and one selected index encounter |
| Source release | `synthea-csv-apr2020` |
| Cohort definition | 0.1.0 |
| Upstream disposition | proceed with conditions |
| Real patients | none |

### Permitted teaching use

The complete accepted 374-row table may be copied into learner workspaces for this open synthetic teaching case. Learners may inspect, sort, derive registered metadata, and use it in later bounded modeling labs.

The source does not authorize:

- claims about real people;
- clinical risk estimates;
- hospital performance comparisons;
- intervention recommendations;
- operational planning;
- deployment;
- identification attempts; or
- replacement with restricted clinical data in a public repository.

### No silent refresh

The source is identified by bytes and SHA-256, not by a mutable filename alone. A changed download, row, field, transformation, or cohort definition requires:

1. a new source record;
2. upstream FND-1 review when applicable;
3. rerun of all Module 01 derivations;
4. review of date ranges, label counts, sparse categories, and split suitability;
5. semantic-version decision; and
6. new progression disposition.

### Public clinical data principle

The Commons should teach with complete public or openly permitted clinical data whenever the decision and rights support it. This module uses the full accepted synthetic cohort, not an invented five-row toy. Later modules add the pinned public CDC NHSN source for forecasting. Public availability does not remove the need for provenance, version control, claim boundaries, or subgroup caution.

## 11. Prediction-time and feature-role contract

### Modeling unit

One modeling row represents one selected synthetic adult at the stop of one selected index emergency or inpatient encounter.

The unit is not:

- an encounter event in general;
- a hospital;
- a clinician;
- a calendar week;
- a repeated person-time observation; or
- an intervention episode.

### Prediction question

At `index_stop`, estimate the probability that a different emergency or inpatient encounter occurs within the next 90 days.

### Allowed default predictors

| Field | Why available | Required caution |
|---|---|---|
| `age_at_index` | derived at the index event | preserve supported extremes; do not add birth date by default |
| `gender` | source value known before prediction | source vocabulary is limited and not universal |
| `race` | source value known before prediction | sparse categories make subgroup estimates unstable |
| `ethnicity` | source value known before prediction | source vocabulary is limited and not universal |
| `index_class` | property of the selected encounter | do not interpret as a modifiable intervention |
| `prior_365d_encounter_count` | defined pre-index lookback | source row counts do not equal all real services |
| `prior_365d_acute_count` | defined pre-index lookback | preserve definition and time window |
| `prior_365d_condition_count` | defined pre-index lookback | count is not a validated burden scale |
| `prior_365d_medication_count` | defined pre-index lookback | count is not a unique therapy count |

Exactly these nine fields have `default_predictor=yes` in the reference contract.

### Tracking keys

`patient_id`, `index_encounter_id`, and derived `model_row_id` support row identity, joins, deduplication, and audit. They are never predictors.

The rule remains even though the IDs are synthetic. Teaching a model to memorize an identifier is methodologically invalid and would transfer badly to real data.

### Time and contract metadata

`index_start`, `index_stop`, `prediction_time`, `outcome_horizon_days`, `source_release`, and `cohort_definition_version` define ordering, timing, provenance, or contract state. They are not default predictors.

Calendar time may become a justified predictor in another use case, but that requires an explicit transport, drift, and deployment-time availability plan. It is excluded here.

### High-cardinality and optional fields

`index_code`, `index_description`, `index_reason_code`, and `index_reason_description` are excluded from the default model. Their use requires a separate plan covering:

- clinical meaning;
- vocabulary stability;
- missingness;
- rare levels;
- text handling;
- dimensionality;
- train-only preprocessing;
- disclosure and memorization risk;
- transport to future coding periods; and
- interpretation.

Exclusion is not a claim that the fields are useless. It is a bounded default for a small teaching cohort.

### Prohibited future and outcome fields

The following fields are blocked:

- `next_30d_state`;
- `next_30d_encounter_id`;
- `next_30d_start`;
- `next_30d_days_after_index_stop`;
- `acute_return_90d` except as the label;
- `death_90d`;
- `endpoint_90d`;
- `followup_90d_complete` as a predictor;
- any feature calculated using future events;
- `split`;
- `split_order`;
- any performance metric; and
- any reviewer disposition.

### Leakage families

| Leakage family | Example | Why invalid | Control |
|---|---|---|---|
| Post-index | next encounter state | value occurs after prediction time | block by field contract |
| Outcome-derived | 90-day endpoint | encodes the event being predicted | block by field contract |
| Preprocessing | scaler fit on all rows | validation and test influence transform | fit transform on train only |
| Split-derived | test membership | partition encodes calendar and evaluation role | never use as predictor |
| Identity | patient ID | permits memorization rather than generalization | tracking only |
| Duplicate | same person or event across partitions | held-out evidence is no longer independent | unique grain and registry checks |

### Role-change procedure

A learner may propose a different role, but cannot implement it silently. The proposal must state:

1. new role;
2. information availability;
3. analytic reason;
4. preprocessing plan;
5. leakage and disclosure review;
6. expected effect on the question;
7. reviewer owner; and
8. version impact.

Until approved, the reference role remains authoritative.

## 12. Temporal split and test-use policy

### Ordering rule

Sort all rows by `index_start` ascending and then by `patient_id` ascending. The patient ID is only a deterministic tie breaker. The sort uses the registered ISO timestamps without randomization.

### Assignment rule

| Split | Positions | Rows | Positives | Negatives | First date | Last date |
|---|---|---:|---:|---:|---|---|
| Train | 1-224 | 224 | 25 | 199 | 2015-01-01 | 2017-04-02 |
| Validation | 225-299 | 75 | 7 | 68 | 2017-04-05 | 2018-04-03 |
| Test | 300-374 | 75 | 4 | 71 | 2018-04-18 | 2019-12-28 |
| Total | 1-374 | 374 | 36 | 338 | 2015-01-01 | 2019-12-28 |

### Split responsibilities

Train data may be used to:

- estimate parameters;
- fit imputers, scalers, encoders, and feature transformations;
- fit resampling folds inside training when a later module authorizes them; and
- estimate the baseline prevalence.

Validation data may be used to:

- compare declared candidate pipelines;
- compare train-fit preprocessing alternatives;
- tune bounded hyperparameters;
- select a threshold under a declared consequence framework; and
- choose one final pipeline before test evaluation.

Test data may be used to:

- run one final evaluation after the pipeline and threshold are frozen;
- report uncertainty and subgroup limitations; and
- inform whether the final package needs revision, narrower claims, or a stop decision.

Test data may not be used to:

- select features;
- choose transformations;
- fit preprocessing;
- tune a parameter;
- select a threshold;
- choose among candidates;
- repair a subgroup result;
- choose the most flattering metric; or
- trigger resplitting until the output looks stable.

### Public artifact clarification

The source and split registry are open teaching artifacts, so a learner can physically inspect test labels. "Untouched" is a workflow and accountability rule: the labels cannot influence selection. Learners record when the final test evaluation is opened and what state was frozen first.

### Why not random stratification

A random stratified split would create similar outcome proportions and might make evaluation numerically easier. It would also mix earlier and later records and answer a less realistic transport question for this case. The temporal split asks whether a workflow developed on earlier synthetic records holds on later records.

### Small test-event consequence

Only four test rows are positive. This means:

- sensitivity estimates move sharply when one row changes status;
- calibration evidence is sparse;
- subgroup performance may be uninterpretable;
- confidence or bootstrap intervals may be wide or unstable; and
- model-use recommendations must stay narrow.

It does not mean:

- the split failed;
- rows should be moved;
- positive cases should be duplicated;
- synthetic examples should be added to test; or
- uncertainty should be hidden.

### Split immutability

`split-registry.csv` is a versioned artifact. Module 02 and later modules join to it by stable tracking fields. Any changed assignment returns to Module 01.

## 13. Baseline and pre-model comparison contract

### Required baseline

The baseline is a constant predicted probability equal to training prevalence:

```text
25 positive training labels / 224 training rows = 0.111607142857
```

The value is fit from train only and is applied unchanged in later comparisons.

### Why the baseline exists

The baseline establishes the minimum comparison. It answers:

> Does a candidate extract useful held-out information beyond returning the training event rate for every row?

Without the baseline, a complex model can appear impressive because it produces differentiated probabilities, uses advanced vocabulary, or achieves high accuracy in an imbalanced dataset.

### What Module 01 records

`baseline-metrics.csv` records:

- baseline ID;
- fitting split;
- application scope;
- training rows;
- training positives and negatives;
- constant probability;
- a documented default 0.5 classification threshold;
- the threshold rule; and
- the fact that the baseline was frozen before candidate comparison.

The threshold is recorded for transparency. It is not endorsed as the clinically useful threshold and it is not tuned in this module.

### What Module 01 does not calculate

Module 01 does not calculate validation or test:

- area under the ROC curve;
- area under the precision-recall curve;
- Brier score;
- log loss;
- calibration slope or intercept;
- sensitivity or specificity;
- predictive values;
- decision consequences; or
- subgroup metrics.

Module 03 owns metric choice, validation comparison, threshold consequences, uncertainty, and the final test evaluation.

### Baseline change rule

Changing the baseline family or fitting population requires a written reason. A second baseline may be added later, such as a simple rules-based or regularized model, but it cannot erase the training-prevalence comparison.

## 14. Reproducible workspace and technical implementation

### Package design

The release uses one standard-library builder and one standard-library validator. The builder owns deterministic derivation. The validator independently reconstructs expected rows and compares every output field.

No database, notebook framework, or machine-learning dependency is required to verify the source, split, and baseline. The pinned scientific environment is still established in Module 01 because Module 02 depends on it.

### Reference package tree

```text
01-aims-reproducible-workspace/
  README.md
  VERSION
  requirements.txt
  build_modeling_workspace.py
  validate_modeling_workspace.py
  data-spec.md
  source-record.yml
  aim-classification-exercises.csv
  aim-and-method-plan.md
  estimand-target-registry.csv
  feature-role-contract.csv
  environment-note.md
  reproducibility-check.md
  ai-use.md
  progression-decision.md
  assessment.md
  instructor-notes.md
  release.json
  learner-template/
  outputs/
    modeling-cohort.csv
    split-registry.csv
    baseline-metrics.csv
    modeling-checks.csv
    build-report.json
```

### Learner build behavior

The command:

```text
python courses/modeling-inference-reproducible-analytics/modules/01-aims-reproducible-workspace/build_modeling_workspace.py learner-workspace
```

must:

1. refuse a target that already exists;
2. verify the upstream source;
3. copy the learner template;
4. copy portable technical and teaching records;
5. copy the exact source into `data/`;
6. derive outputs into a new `outputs/` directory;
7. write deterministic UTF-8 and LF files; and
8. print the machine-readable build report.

The builder never merges into an existing submission and never repairs a partially completed target.

Inside a copied learner workspace, the portable output-only command is:

```text
python build_modeling_workspace.py reproduced-outputs --outputs-only
```

It reads the copied exact source, creates a new output target, and refuses an existing target. The learner compares those outputs with the packaged `outputs/` directory and records the result.

### Deterministic derivation

The builder:

1. verifies source bytes and SHA-256;
2. verifies exact source field names and order;
3. verifies row and key grain;
4. verifies binary label values;
5. sorts by `index_start` and `patient_id`;
6. assigns stable `FND2-0001` through `FND2-0374` row IDs;
7. copies `index_stop` into `prediction_time`;
8. writes a constant 90-day horizon;
9. assigns split and split order;
10. calculates the training baseline;
11. runs 24 release invariants; and
12. writes output metadata and fingerprints.

### Scientific environment

`requirements.txt` pins:

- JupyterLab;
- matplotlib;
- nbclient;
- NumPy;
- pandas;
- scikit-learn;
- SciPy;
- seaborn; and
- statsmodels.

These pins define the shared FND-2 analysis environment. A later security or compatibility update may change them through a module or Commons patch/minor release, but the exact installed environment must be recorded.

### Git state

The learner release should preserve:

- a clean primary branch;
- specific commits for aim, data contract, split, and final release work;
- no committed virtual environment or cache;
- module version 0.1.0;
- annotated tag `fnd2-aims-v0.1.0`; and
- an environment and reproduction record matching the tagged state.

### Semantic-version rule

- Patch: correction that does not change the aim, source, role set, split, baseline, deliverable, or scoring contract.
- Minor: backward-compatible addition such as an alternate exercise or optional supported environment.
- Major: change to the decision, aim, source, target, prediction time, role contract, split, baseline, required evidence, or scoring meaning.

Learner filenames do not carry version numbers. `VERSION`, release metadata, Git history, and the annotated tag identify state.

## 15. Exact learner deliverables and release assembly

### Required top-level records

| File | Learner responsibility | Acceptance evidence |
|---|---|---|
| `README.md` | state decision, aim, data boundary, split, baseline, reproduction, and handoff | no unresolved prompt and allowed disposition |
| `VERSION` | preserve module version | exact `0.1.0` |
| `requirements.txt` | preserve declared pins or document approved change | exact package/version pairs |
| `data-spec.md` | preserve the source and derivation contract | exact source, fields, split, and output roles |
| `source-record.yml` | preserve source identity, rights, and claim limit | exact bytes, SHA-256, URLs, and synthetic flag |
| `aim-classification-exercises.csv` | classify twelve requests with reason and rejected method | twelve complete rows |
| `aim-and-method-plan.md` | define primary decision, question, method family, timing, and disposition | complete bounded plan |
| `estimand-target-registry.csv` | complete all six aim classes | six complete rows and correct aim sequence |
| `feature-role-contract.csv` | assign all source and derived fields | 34 unique rows and exact default predictor set |
| `environment-note.md` | record actual environment and ordered commands | no hidden executable or unresolved difference |
| `reproducibility-check.md` | document a clean rerun and failures | exact observed facts and disposition |
| `ai-use.md` | disclose material assistance and checks | data shared, advice used, human verification, owner |
| `progression-decision.md` | decide whether Module 02 may proceed | allowed disposition, conditions, and handoff |
| `assessment.md` | preserve assignment and gates | unchanged scoring meaning |
| builder and validator | preserve executable release logic | self-check and submission validation pass |

### Required data and output records

| File | Exact release requirement |
|---|---|
| `data/resolved-analytic-table.csv` | 374 rows, 29 fields, 121787 bytes, exact source SHA-256 |
| `outputs/modeling-cohort.csv` | 374 rows, 34 fields, deterministic ordering and derivations |
| `outputs/split-registry.csv` | 374 unique rows, exact split positions, labels, and times |
| `outputs/baseline-metrics.csv` | one training-prevalence baseline row |
| `outputs/modeling-checks.csv` | 24 passing release invariants |
| `outputs/build-report.json` | source, output, split, baseline, and decision metadata |

### Required output fingerprints for reference version 0.1.0

| Output | Bytes | SHA-256 |
|---|---:|---|
| `modeling-cohort.csv` | 138503 | `6556ed149e69589253ab58572b2f08535899ae12c3e84dc7bafc7da2ebe6f332` |
| `split-registry.csv` | 51910 | `05ea7ed9f37b20ba9cba4bb2a36d4c95af96cd2f8e5cc82a5bc8eb74c91474c1` |
| `baseline-metrics.csv` | 306 | `613651013e397beeadc84b17482026ca7cb4674abf61bf521699d79af0a3c9af` |
| `modeling-checks.csv` | 3869 | `e04dea1392d1cde03823f34b1e2548d7275bdd2a9ff55814e5e1ae6b6f04f24b` |
| `build-report.json` | 1653 | `468e494314a8d7326d81d8e6ed17a42a81f025642c4a58b5b4a10fd5bd5b6c67` |

Output fingerprints apply to the reference release. A learner's completed prose and exercise files will differ. The deterministic data outputs must remain exact unless an approved version change is made.

### Exact handoff statement

The final README and progression record must say whether Module 02 receives the package. An acceptable handoff names:

- version and tag;
- source fingerprint;
- model unit;
- prediction time;
- target and horizon;
- allowed predictor set;
- blocked field families;
- split counts and dates;
- baseline value;
- release disposition;
- inherited conditions; and
- changes that require return.

### No screenshot-only evidence

Screenshots may illustrate a problem but do not replace files, machine-readable records, code, or validator output. Every assessed fact must remain available to a text reader and to the release checker.

## 16. Assessment, rubric, gates, and checkpoint freeze

### Fifteen-point rubric

| Criterion | Full-credit evidence | Points |
|---|---|---:|
| Decision and aim contract | owner, action, nondecision, correct aim, complete target or estimand, justified method family | 4.00 |
| Source, field roles, and leakage boundary | exact FND-1 verification, 34 complete roles, nine predictors, all future and outcome fields blocked | 4.00 |
| Temporal split and baseline | exact ordering, 224/75/75 rows, 25/7/4 positives, role explanation, training-only baseline | 3.00 |
| Reproducible package | exact environment, protected builder, clean rerun, deterministic outputs, passing validation | 3.00 |
| Responsible handoff | clear AI-use record, plain-language disposition, exact Module 02 conditions | 1.00 |
| Total |  | 15.00 |

### Performance levels

| Level | Numeric range | Meaning |
|---|---:|---|
| Ready | 13.50-15.00 | precise and independently defensible; all gates pass |
| Ready with bounded revision | 12.00-13.49 | meets minimum; all gates pass; a documented nonblocking condition remains |
| Revise | 0.00-11.99 | numeric evidence is incomplete or inaccurate |
| Gate failure | any score | one or more noncompensable conditions prevent progression |

The minimum score is 12.00. Numeric credit never compensates for a failed gate.

### Noncompensable gates

1. Exact accepted FND-1 input and upstream conditions are present.
2. Source bytes and SHA-256 match.
3. Grain is 374 unique people and 374 unique index encounters.
4. Prediction time is stated before feature selection.
5. All 34 fields have one explicit role.
6. The nine default predictors match the contract.
7. Every post-index and outcome-derived field is blocked.
8. `acute_return_90d` appears only as the label.
9. Train, validation, and test rows reconcile to 224, 75, and 75.
10. Positive labels reconcile to 25, 7, and 4.
11. Test evidence does not influence preprocessing, fitting, selection, tuning, or threshold choice.
12. The baseline is estimated from 25 of 224 training rows before candidate comparison.
13. The protected builder refuses an existing target.
14. Environment, reproduction, and validator evidence are complete.
15. The release contains no real patient data, secret, private URL, or local absolute path.
16. Material AI assistance is disclosed and independently checked.
17. The progression disposition is allowed and owned by a human reviewer.
18. Module 02 receives exact artifacts and conditions rather than copied numbers in prose.

### Scoring notes

- A correct aim label without a reason earns no more than half of the relevant evidence credit.
- A field role copied from the reference without an oral or written defense may be checked through the clarification route.
- A correct split count created by a different or undocumented assignment procedure fails the split gate.
- A baseline calculated from all rows fails the baseline gate.
- A package that runs only from an absolute local path fails reproducibility.
- A passing validator with an incoherent decision statement can still require revision.

### Week 3 freeze

After acceptance:

1. create annotated tag `fnd2-aims-v0.1.0`;
2. record the accepted commit;
3. record the reviewer and disposition;
4. preserve exact deterministic output fingerprints;
5. preserve unresolved conditions; and
6. register the state for Checkpoint 1 assembly.

Modules 02 and 03 build from the frozen state. A later correction must identify whether the checkpoint component is superseded and why.

## 17. Feedback, revision, recovery, and support

### Feedback order

Reviewers should return feedback in this order:

1. privacy, access, or integrity stop;
2. wrong decision or aim;
3. unsupported target, contrast, unit, or time boundary;
4. source or grain mismatch;
5. leakage or field-role error;
6. split or baseline error;
7. reproducibility failure;
8. incomplete explanation or accountability record; and
9. clarity, formatting, or minor documentation issue.

This order prevents learners from polishing prose around a broken analytic contract.

### Revision cycle

For a `revise` disposition, the learner must:

1. preserve the failed submission or commit;
2. name each defect and its affected artifact;
3. identify whether the correction changes meaning or only implementation;
4. make the semantic-version decision;
5. rebuild into a new target;
6. rerun the validator;
7. update reproduction and AI-use records;
8. update progression conditions; and
9. resubmit with a concise change log.

The instructor does not ask a learner to delete inconvenient evidence. The ability to explain a failed approach and its correction is part of reproducible work.

### Common revision routes

| Failure | Normal correction | Return farther upstream? |
|---|---|---|
| aim mismatched to decision | rewrite the contract and reassess method family | no unless source cannot support new aim |
| target missing time boundary | complete time zero, prediction time, and horizon | no |
| source fingerprint mismatch | stop and obtain exact accepted input | yes when upstream artifact changed |
| field-role error | correct role table and inspect all downstream uses | no if no later work began |
| split changed | restore registry or approve a new version | possibly checkpoint re-freeze |
| baseline used all rows | recalculate from train and invalidate later comparisons | return any later model work |
| test used for selection | discard contaminated selection evidence and restart from frozen pre-test state | return Module 03 work |
| real patient data found | stop access and refer | privacy/security process |
| incomplete AI record | reconstruct use and verification where possible | integrity review when material history cannot be established |

### Supported environment route

A learner without local installation permission may use an institution-managed environment. The same file, version, source, output, and validation contracts apply. The environment record must identify the managed runtime and any differences from the reference pins.

### Accessibility recovery route

All assessed evidence can be completed without drag-and-drop interaction, color discrimination, or image-only output. A learner who cannot use a notebook interface may run the standard-library command-line path and submit the same files.

### Extension principle

Time accommodations change due dates, not the source, gates, or claim boundary. Faculty should prioritize aim, prediction time, field roles, split, baseline, and reproducibility over optional enrichment.

## 18. Responsible AI, privacy, security, and integrity

### AI may assist with

- generating alternative examples for aim classification;
- explaining unfamiliar statistical vocabulary;
- drafting a field-role rationale for human review;
- suggesting checks for a deterministic builder;
- debugging repository-relative commands;
- editing prose for clarity; and
- identifying possible leakage for adjudication.

### AI may not own

- the analytic decision;
- data-use permission;
- source identity;
- prediction time;
- feature roles;
- split assignment;
- baseline definition;
- test-set access decision;
- progression disposition; or
- clinical or operational interpretation.

### Data-sharing boundary

This module uses synthetic open teaching data. Learners still practice the stricter rule needed for real healthcare work:

- do not send protected data to an unapproved system;
- do not send credentials, tokens, private URLs, or access details;
- do not assume a public interface has an institutional agreement;
- minimize the data in prompts;
- use field descriptions or synthetic examples when possible; and
- record what was shared.

### Required AI-use record

For each material use, record:

- tool or system;
- purpose;
- data shared;
- advice or output used;
- independent human check;
- changed or rejected content; and
- decision owner.

If no AI system was used, the learner states that directly and records other material help or documentation.

### AI leakage trap

An AI system can recommend an invalid field, compute a statistic on all rows, or use test labels in feature selection. Human review applies the same information boundary to agent-generated work as to hand-written work. "The tool suggested it" is not a justification.

### Privacy and security gates

The release must contain no:

- real patient record;
- name, address, medical record number, or direct real identifier;
- credential or token;
- private storage path or signed URL;
- absolute personal filesystem path;
- executable downloaded from an unverified source; or
- claim that synthetic IDs make identity leakage acceptable in modeling.

Discovery of protected or secret material triggers `refer`, not a normal resubmission.

### Academic integrity

Learners may use collaboration and approved tools when disclosed. They remain responsible for explaining the submitted question, roles, split, and baseline. When authorship is unclear, the oral clarification route tests understanding of the actual release rather than asking for trivia.

## 19. Accessibility and inclusive teaching requirements

### Multiple access routes

Every required task has a text and command-line route. The module does not require visual notebook use. Tables use explicit headers. Decisions and statuses are written as words rather than encoded by color alone.

### Document requirements

- use descriptive headings in a logical hierarchy;
- use plain language before specialized terminology;
- define acronyms at first use;
- use meaningful link text with full visible URLs when the URL must be copied;
- include table headers and units;
- avoid merged cells in assessed CSVs;
- preserve high contrast in any optional display;
- do not rely on color alone;
- provide text descriptions for any optional figure; and
- keep line length and code blocks readable without horizontal scrolling when practical.

### Cognitive access

The module uses one continuing case so learners can focus on changing analytic questions rather than repeatedly learning new data. The six-way taxonomy is paired with a repeated decision template:

```text
decision -> aim -> unit and time -> target or contrast -> method family -> evidence and limitation
```

Learners receive worked examples, guided practice, independent transfer, and an exact release checklist.

### Terminology support

Required terms include:

- decision statement;
- analytic aim;
- target;
- estimand;
- population;
- unit;
- time zero;
- prediction time;
- horizon;
- contrast;
- predictor;
- label;
- leakage;
- train;
- validation;
- test; and
- baseline.

Faculty should correct meaning without penalizing accent, dialect, or nonstandard phrasing when the technical concept is clear.

### Accessible assessment

The learner may provide the technical defense orally, in writing, or through an accessible recorded format approved by the institution. The same evidence and gates apply.

## 20. Validation, acceptance tests, risks, and human review

### Builder self-check

The builder self-check must:

- verify the accepted source;
- build outputs into a temporary target;
- confirm train and test reference facts;
- refuse rebuilding into the existing output target;
- build a complete learner starter in another target;
- verify the copied source; and
- exit with a clear pass marker.

### Validator self-check

The validator self-check must:

- validate the complete reference release;
- build and validate a learner starter;
- reject the prompted starter as a completed submission;
- remove a required output from a copied fixture; and
- reject the broken fixture.

Reference version 0.1.0 passes 15937 release checks and 15907 starter checks.

### Release validation scope

Validation covers:

- required files;
- module version;
- source bytes and SHA-256;
- source row, field, and key grain;
- every value in all four CSV outputs;
- build-report split and baseline facts;
- 34 unique feature-role rows;
- exact default predictors;
- prohibited-field blocking;
- six target-registry rows;
- twelve exercise rows;
- no local personal paths;
- no Unicode em or en dash in release text;
- no unresolved reference prompts;
- allowed progression disposition;
- release metadata; and
- output fingerprints.

### Acceptance commands

From repository root:

```text
python courses/modeling-inference-reproducible-analytics/modules/01-aims-reproducible-workspace/build_modeling_workspace.py --self-check
python courses/modeling-inference-reproducible-analytics/modules/01-aims-reproducible-workspace/validate_modeling_workspace.py --self-check
powershell -ExecutionPolicy Bypass -File scripts/check-curriculum-specs.ps1
```

### Technical acceptance criteria

- both self-checks pass;
- full curriculum checker passes;
- source and output fingerprints match;
- no generated cache or private file is committed;
- module spec contains 21 numbered sections;
- package release metadata matches Commons 0.39.0;
- root Commons version is 0.39.0; and
- Git worktree is clean after commit.

### Known material limitations

1. The source is synthetic and from an older pinned release.
2. The cohort has only 36 positive labels overall.
3. The test split has only four positive labels.
4. Race includes source categories with counts of 5 and 1.
5. Source gender vocabulary contains only F and M.
6. High-cardinality code and reason information is excluded from the default model.
7. The temporal split demonstrates later-record transport only within this synthetic artifact.
8. A deterministic build does not validate the clinical meaning of the target.

These limitations narrow teaching claims. They do not invalidate the module's aim-classification, leakage, split, baseline, and reproducibility lessons.

### Required human reviews before alpha

| Review | Required decision |
|---|---|
| Course faculty | alignment with program outcomes and 15.5-hour workload |
| Quantitative methods | aim taxonomy, target language, split roles, and baseline |
| Clinical informatics | encounter timing, field meaning, and clinical claim boundary |
| Python and reproducibility | code clarity, portability, environment, and validator |
| Accessibility | command, document, table, and assessment access |
| Privacy and security | synthetic source, identifiers, prompt boundary, and referral path |
| Responsible AI | permitted uses, disclosure, verification, and ownership |
| Independent instructor | teachability without release-author context |

### Reference disposition

The automated reference disposition is `accept with conditions` for teaching-package progression. It is not human curriculum approval. The conditions are:

- synthetic teaching use only;
- no real clinical or population estimates;
- test precision and subgroup limitations remain visible;
- high-cardinality fields remain excluded;
- test data remain unavailable for selection; and
- named human reviews are pending.

## 21. References, release record, and continuation contract

### Authoritative references

- Synthea downloads: https://synthea.mitre.org/downloads
- Synthea CSV data dictionary: https://github.com/synthetichealth/synthea/wiki/CSV-File-Data-Dictionary
- Python virtual environments: https://docs.python.org/3/library/venv.html
- Python CSV library: https://docs.python.org/3/library/csv.html
- Python hashing library: https://docs.python.org/3/library/hashlib.html
- scikit-learn common pitfalls and recommended practices: https://scikit-learn.org/stable/common_pitfalls.html
- scikit-learn model selection: https://scikit-learn.org/stable/model_selection.html
- scikit-learn probability calibration: https://scikit-learn.org/stable/modules/calibration.html
- statsmodels documentation: https://www.statsmodels.org/stable/index.html
- Semantic Versioning 2.0.0: https://semver.org/spec/v2.0.0.html
- MGH Institute 2026-2027 academic calendar: https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

### Release record

- Module version: 0.1.0.
- Commons release: 0.39.0.
- Release date: 2026-08-30.
- Reference status: runnable release candidate.
- Reference disposition: accept with conditions.
- Builder self-check: pass.
- Validator self-check: pass.
- Release checks: 15937.
- Starter checks: 15907.
- Existing-target refusal: pass.
- Incomplete-submission rejection: pass.
- Source rows and fields: 374 and 29.
- Modeling rows and fields: 374 and 34.
- Split rows: 224, 75, and 75.
- Positive outcomes: 25, 7, and 4.
- Baseline: `0.111607142857`.
- Real patients: none.

### Contributors

- Shuhan He: Commons sponsor and curriculum direction.
- OpenAI Codex: module specification, deterministic build, validation, and teaching package.

AI assistance is documented in the package. Named faculty and specialist reviewers remain responsible for human approval.

### Module 02 continuation contract

Begin Module 02 only from an accepted or accepted-with-conditions Module 01 state. Module 02 is titled `Regression models and interpretation` and has 16.0 learner hours.

Module 02 must:

1. verify Module 01 version and fingerprints;
2. preserve the exact modeling cohort and split;
3. preserve prediction time and field roles;
4. keep the test partition outside fitting and interpretation exercises;
5. use the 111-row recorded-next-encounter subset only for the declared linear-regression teaching outcome;
6. keep the 263 structural timing blanks out of the linear outcome rather than converting them to zero;
7. use logistic regression for bounded binary-outcome interpretation without calling coefficients causal;
8. state formulas, reference groups, assumptions, uncertainty, and diagnostics;
9. preserve the training-prevalence baseline for later prediction comparison;
10. document every return condition; and
11. commit and push Module 02 as its own versioned unit before Module 03 begins.

### Resume record

FND-2 Module 01 is complete as a runnable reference candidate at Commons 0.39.0 when all acceptance commands pass and the unit is committed and pushed. Resume with Module 02 only. Do not reopen the Module 01 split or source unless a documented return condition occurs.
