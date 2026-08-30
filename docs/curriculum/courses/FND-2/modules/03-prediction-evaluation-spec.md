# FND-2 Module 03: Prediction workflows and evaluation

## 1. Module identity and place in the course

### Release identity

- Course: FND-2, Modeling, Inference, and Reproducible Analytics.
- Module: 03 of 07.
- Module ID: `oclc-fnd2-03`.
- Module version: 0.1.0.
- Commons release: 0.41.0.
- Source week: 3.
- Learner work: 16.5 hours.
- Week 3 assessment share: 15 of 40 cumulative course points.
- Package: `courses/modeling-inference-reproducible-analytics/modules/03-prediction-evaluation/`.
- Status: runnable release candidate.
- Data class: synthetic public teaching records.
- Clinical use: prohibited.

### Purpose

Module 03 is the first place in FND-2 where an eligible candidate model is selected with held-out evidence and then evaluated on untouched test data. The learner carries forward the accepted analytic aim, split, baseline, feature roles, regression model, and assumption conditions. The learner does not reopen those decisions silently.

The module teaches the sequence that protects prediction evidence:

1. verify the upstream contract;
2. fit preprocessing and candidate parameters on training data only;
3. inspect training-only resampling;
4. compare candidates on the fixed validation partition;
5. reject a leaked critique model before performance review;
6. apply a predeclared model-selection rule;
7. choose and lock a threshold using validation consequences;
8. open the test partition once;
9. report discrimination, probability error, calibration, exact confusion counts, and subgroup limits; and
10. issue a bounded progression recommendation.

### Relationship to Module 01

Module 01 owns the prediction question, index time, outcome, horizon, population, field roles, temporal split, baseline, and package identity. Module 03 verifies their exact files and fingerprints. If any of those facts changes, the work returns to Module 01.

### Relationship to Module 02

Module 02 owns the declared `LOG01` regression formula, transformations, model matrix, diagnostic evidence, and quantity-correct interpretation. Module 03 receives `LOG01` as an eligible prediction candidate. It does not select a model from coefficient significance, training likelihood, or causal language.

### Relationship to Checkpoint 1

Module 03 completes the evidence assembled at the end of Week 3:

| Component | Points |
|---|---:|
| Module 01 analytic aim and reproducible workspace | 15 |
| Module 02 regression evidence and interpretation | 10 |
| Module 03 prediction workflow and evaluation | 15 |
| Total | 40 |

Checkpoint 1 freezes all three modules. A favorable module score alone does not permit progression when any noncompensable gate fails.

### Relationship to Module 04

Module 04 receives the exact selected pipeline, locked threshold, one-time test evidence, subgroup suppression, uncertainty, and claim boundary. It reviews validity, missing data, selection, dependence, and longitudinal structure. It must not treat the selected predictor set as a causal adjustment set.

### Required starting state

The learner begins only when:

- Module 01 disposition permits progression;
- Module 02 disposition permits prediction evaluation;
- all seven upstream artifacts match their registered byte counts and SHA-256 values;
- the temporal split remains 224 training, 75 validation, and 75 test rows;
- outcome counts remain 25, 7, and 4;
- the training-prevalence baseline remains 0.111607142857;
- `LOG01` remains the declared regression candidate;
- all Module 02 assumption conditions remain visible; and
- no one has used the test split to alter the Module 03 contract.

### Required ending state

The learner ends with:

- training-only resampling evidence;
- an audited 15-column selected feature pipeline;
- same-row validation evidence for four declared models;
- one rejected leakage fixture;
- one mechanically selected eligible candidate;
- one threshold locked before test;
- exactly 75 frozen test predictions;
- baseline and selected-model test metrics;
- exact test confusion counts;
- calibration and threshold tables with accessible SVG companions;
- subgroup counts and suppression decisions;
- a reproducible package;
- a human-owned recommendation; and
- an explicit Module 04 handoff or return decision.

## 2. Technical decision, owner, and audiences

### Decision owner

The primary decision owner is a clinical prediction and model-risk reviewer. The owner may consult a biostatistician, clinical informatician, clinician, accessibility reviewer, privacy reviewer, responsible-AI reviewer, and instructor, but remains accountable for the final recommendation.

### Technical decision

The decision is:

> Does the locked prediction pipeline beat its simple baseline and provide credible enough evidence for validity review, without claiming deployment readiness?

This is narrower than deciding whether the model should be used in care. It tests whether the workflow is coherent enough to justify the next educational validity review.

### Evidence the owner must use

The owner must consider:

- source and split fingerprints;
- training-only fit evidence;
- resampling variability;
- the constant baseline;
- validation comparison on identical rows;
- the predeclared selection rule;
- leakage failure evidence;
- threshold consequences and lock timing;
- untouched test metrics and exact counts;
- calibration evidence;
- test outcome scarcity;
- subgroup counts and suppression;
- reproducibility and environment records;
- accessibility evidence; and
- the synthetic-data and nondeployment boundaries.

### What the decision does not approve

No Module 03 disposition approves:

- real patient use;
- integration with a clinical workflow;
- prospective validation;
- external validation;
- treatment or triage recommendations;
- autonomous decisions;
- fairness across protected groups;
- causal interpretation;
- transport to another population or time;
- production monitoring;
- a stable calibration claim; or
- deployment readiness.

### Allowed recommendations

| Recommendation | Meaning | Next action |
|---|---|---|
| `continue to validity review` | All gates pass and remaining limits are carried forward. | Assemble Checkpoint 1 and begin Module 04 after approval. |
| `revise` | The aim remains viable, but a correctable workflow or explanation defect remains. | Return to the owning module and version material changes. |
| `stop` | Leakage, invalid test use, unsupported aim, or another blocking defect invalidates the evidence. | Do not assemble an accepted checkpoint. |

The reference package uses `continue to validity review with conditions`, a conditional form of the first allowed recommendation.

### Primary learner audience

The learner is a health-data practitioner who has completed FND-1 and the first two FND-2 modules. The learner is expected to:

- read Python and structured output;
- distinguish descriptive, inferential, and predictive questions;
- understand the fixed temporal split;
- interpret regression quantities correctly;
- reason about prediction time;
- explain counts and proportions; and
- defend a reproducible evidence package.

The learner is not expected to invent a new machine-learning algorithm, optimize a production system, or conduct a full model-risk audit independently.

### Review audiences

| Reviewer | Primary review question |
|---|---|
| Clinical prediction reviewer | Does the evidence sequence protect against optimistic selection? |
| Model-risk reviewer | Are leakage, threshold, uncertainty, and use boundaries explicit? |
| Biostatistician | Are metrics, resampling, intervals, and counts used correctly? |
| Clinical informatician | Are prediction time and field availability credible? |
| Clinician | Does the threshold consequence have understandable meaning? |
| Accessibility reviewer | Can exact evidence be obtained without reading the plots visually? |
| Privacy reviewer | Does the release contain only synthetic, nonsecret material? |
| Responsible-AI reviewer | Are automation, accountability, and unsupported uses visible? |
| Instructor | Can a learner reproduce, explain, revise, and defend the work? |

### Evidence classes

The package separates five evidence classes:

1. source evidence, which proves what inputs were used;
2. process evidence, which proves where fitting and selection occurred;
3. performance evidence, which quantifies the locked workflow;
4. interpretation evidence, which explains what the values mean; and
5. decision evidence, which records whether and how progression is allowed.

No one artifact substitutes for all five.

### Oral clarification route

An oral defense may clarify learner reasoning but may not replace missing files, change a metric, invent an unseen test result, or waive a gate. Any material clarification is recorded in the reviewer record or returned artifact.

## 3. Foundation skill and exact handoff

### Foundation skill

The durable skill is to protect a prediction workflow from leakage and test-guided optimism while translating its evidence into a bounded decision.

The learner must be able to say:

- what was fit;
- on which rows it was fit;
- what was selected;
- by which rule it was selected;
- when the threshold was chosen;
- when the test was opened;
- what every reported metric measures;
- what the exact consequences were; and
- what the evidence does not permit.

### Why this belongs in FND-2

Prediction evaluation is a general analytic foundation used across clinical research, quality improvement, operations, epidemiology, informatics, and applied AI. Later applied courses revisit it in domain-specific ways. FND-2 owns the common technical workflow straight through.

### Upstream input contract

| Artifact | Bytes | SHA-256 | Owning module |
|---|---:|---|---|
| `modeling-cohort.csv` | 138503 | `6556ed149e69589253ab58572b2f08535899ae12c3e84dc7bafc7da2ebe6f332` | Module 01 |
| `split-registry.csv` | 51910 | `05ea7ed9f37b20ba9cba4bb2a36d4c95af96cd2f8e5cc82a5bc8eb74c91474c1` | Module 01 |
| `baseline-metrics.csv` | 306 | `613651013e397beeadc84b17482026ca7cb4674abf61bf521699d79af0a3c9af` | Module 01 |
| `feature-role-contract.csv` | 3766 | `599f29ca612cb5f23aed277c56937af78c488ba952c2926faa94166f33449c83` | Module 01 |
| `formula-registry.csv` | 771 | `fc69d6146eec729969b571b535c13027e9b875d34dd99637f0dc0d9b934239a6` | Module 02 |
| `model-matrix-fields.csv` | 1535 | `7a91e166796ae1030518da95e49f6a19ecc687d7cf5784f76718509c0abc9c38` | Module 02 |
| `assumption-register.csv` | 2181 | `7c6322667a383458a34aea49b687d1a6716aaaf0f780ccf060f1c99d671956e3` | Module 02 |

The builder stops before fitting if any file is missing or changed.

### Exact Checkpoint 1 handoff

Checkpoint 1 receives:

- all seven upstream artifacts;
- the frozen model contract;
- 15 training resampling rows;
- 300 validation prediction rows;
- four validation comparison rows;
- four selection records;
- 71 validation threshold rows;
- one threshold decision;
- 75 test prediction rows;
- 16 test metric rows;
- four exact confusion rows;
- five calibration groups;
- ten subgroup rows;
- 15 transformed feature rows;
- one leaked-model failure row;
- 22 passing invariant rows;
- two accessible SVG files;
- the interpretation report;
- the progression recommendation; and
- the reproduction, environment, accessibility, and AI-use records.

### Exact Module 04 handoff

Module 04 receives these fixed facts:

| Fact | Value |
|---|---|
| Selected model | `ML01` |
| Selected model type | bounded random forest classifier |
| Fitted feature count | 15 |
| Validation threshold | 0.08513264 |
| Test rows | 75 |
| Test outcomes | 4 |
| Test TN / FP / FN / TP | 48 / 23 / 2 / 2 |
| Test ROC AUC | 0.58802817 |
| Test average precision | 0.14682471 |
| Test Brier score | 0.05097579 |
| Test log loss | 0.21218264 |
| Subgroup rule | counts first; suppress under declared limits |
| Use boundary | synthetic teaching evidence only |

### Return conditions

Return to Module 01 for a changed:

- decision question;
- population;
- index or prediction time;
- outcome or horizon;
- field role;
- eligibility rule;
- temporal split; or
- baseline definition.

Return to Module 02 for a changed:

- regression formula;
- transform;
- reference group;
- coefficient quantity;
- assumption record; or
- regression interpretation.

Return to Module 03 for a changed:

- prediction feature set;
- preprocessing step;
- imputation rule;
- resampling plan;
- candidate model;
- validation metric;
- selection rule;
- threshold consequence;
- threshold tie-break;
- test-use rule;
- calibration grouping;
- uncertainty method;
- subgroup definition; or
- suppression rule.

Every material return requires a semantic-version decision and must preserve the original release evidence.

## 4. Assessable outcomes and evidence map

### Outcomes

By the end of Module 03, the learner can:

1. verify a model-development input contract;
2. explain training, resampling, validation, and test roles;
3. fit preprocessing within training-only boundaries;
4. inspect transformed feature names;
5. run and interpret training-only stratified resampling;
6. compare models on identical validation rows;
7. retain a simple baseline;
8. reject post-index and outcome-derived leakage;
9. apply a predeclared model-selection rule;
10. choose a threshold from an explicit validation consequence;
11. lock a selected pipeline and threshold before test;
12. evaluate the untouched test partition once;
13. distinguish discrimination, probability error, calibration, and threshold consequences;
14. report exact confusion numerators and denominators;
15. interpret class imbalance without relying on accuracy;
16. carry uncertainty into the recommendation;
17. report subgroup counts and suppress unsupported metrics;
18. produce accessible visual and structured evidence;
19. reproduce the package from exact inputs; and
20. issue a bounded progression recommendation.

### Outcome-to-evidence map

| Outcome group | Required evidence |
|---|---|
| Input protection | source record, hashes, split and outcome checks |
| Fit protection | model contract, resampling rows, transformed features |
| Selection | validation predictions, comparison, selection record |
| Leakage reasoning | leaked-model failure table and written explanation |
| Threshold | full threshold table and decision row |
| Test evaluation | 75 predictions, 16 metrics, exact confusion table |
| Calibration | five-group table, SVG, structured description |
| Subgroups | ten count-first rows and suppression flags |
| Reproduction | build report, reproduction record, validator result |
| Decision | report, oral defense, progression recommendation |

### Minimum explanation standard

A metric explanation must include:

- partition;
- row count;
- positive-outcome count;
- model and threshold when relevant;
- numerator and denominator when a rate is reported;
- direction of better performance;
- uncertainty or sample limit; and
- the decision it can and cannot inform.

A statement such as "the model performed well" does not meet the standard.

### Mastery levels

| Concept | Level |
|---|---|
| Training-only feature pipeline | Guided |
| Resampling versus validation | Guided |
| Temporal test protection | Core |
| Baseline retention | Core |
| Leakage rejection | Core |
| Model-selection rule | Core |
| Threshold consequence | Core |
| Exact confusion measures | Core |
| Discrimination | Guided |
| Calibration | Guided |
| Machine-learning baseline | Recognize and run |
| Subgroup evidence restraint | Core |

## 5. Concept ownership and out-of-scope boundaries

### Module 03 owns

- prediction pipeline fit boundaries;
- training-only resampling;
- validation model comparison;
- leakage critique;
- candidate eligibility;
- model-selection rules;
- threshold selection and lock;
- one-time test evaluation;
- discrimination metrics;
- probability-error metrics;
- exact confusion evidence;
- small-sample calibration displays;
- bootstrap teaching intervals;
- count-first subgroup summaries;
- subgroup suppression;
- accessible evidence alternatives;
- model-use boundary; and
- Checkpoint 1 prediction recommendation.

### Module 03 introduces but does not own

- broader clinical utility analysis;
- decision curves and net benefit;
- probability recalibration;
- fairness assessment;
- external validation;
- prospective validation;
- drift monitoring;
- model updating;
- causal validity;
- survival prediction;
- clustered validation; and
- production governance.

### Module 03 does not own

- the original cohort construction;
- the prediction outcome definition;
- the temporal split;
- the regression coefficient interpretation;
- causal adjustment;
- repeated-measures methods;
- missing-data sensitivity analysis;
- deployment architecture;
- clinical workflow integration;
- model registry operations;
- protected health information; or
- real patient decisions.

### Separation from regression inference

Module 03 does not use coefficient p-values, training likelihood, or confidence intervals to select the prediction model. `LOG01` is evaluated using the same validation performance metrics and rows as `ML01`.

### Separation from causal inference

Predictors that improve prediction do not automatically control confounding. No feature importance, coefficient, or model-selection result is a causal effect.

### Separation from fairness assessment

Subgroup summaries reveal where evidence is sparse. They do not establish fairness, equal performance, or inequity. A fairness conclusion requires a purpose, protected-group review, adequate sample, uncertainty, consequence analysis, and governance beyond this module.

### Separation from deployment

A reproducible model is not a deployable model. Deployment would require real clinical validation, workflow design, safety review, monitoring, accountability, privacy, security, maintenance, and prospective evidence.

## 6. Lesson sequence and learner time

| Sequence | Activity | Hours | Evidence produced |
|---:|---|---:|---|
| 1 | Upstream handoff and partition roles | 1.0 | fingerprint and split defense |
| 2 | Pipeline fit and feature audit | 2.0 | transformed feature review |
| 3 | Training-only resampling | 2.0 | 15 fold rows |
| 4 | Validation metrics and selection | 2.0 | comparison and selection records |
| 5 | Leaked-model failure | 1.0 | leakage critique |
| 6 | Threshold consequences and lock | 2.0 | 71-row table and lock record |
| 7 | One-time test evaluation | 2.0 | predictions, metrics, confusion |
| 8 | Calibration and uncertainty | 1.5 | table, plot, interval interpretation |
| 9 | Subgroups and accessibility | 1.5 | suppression and access records |
| 10 | Reproduction and defense | 1.5 | validation and recommendation |
| Total |  | 16.5 | complete package |

### Lesson 1 gate

The learner may not fit a model until all upstream fingerprints, split counts, outcome counts, prediction time, and field roles are explained and pass.

### Lesson 2 gate

The learner must show that the selected pipeline learns 15 transformed columns from training only. Unknown categories must be handled without fitting on later data.

### Lesson 3 gate

Every resampling fold must refit preprocessing and model parameters. A transform fit once on all 224 training rows and reused inside folds fails the resampling gate.

### Lesson 4 gate

All candidates must use the same 75 validation rows and four declared metrics. No test result may appear in the selection record.

### Lesson 5 gate

The learner must reject `LEAK01` from field timing before describing its apparent performance.

### Lesson 6 gate

The threshold consequence, selection rule, and 0.08513264 lock must be recorded before test interpretation.

### Lesson 7 gate

The test partition is evaluated once. If the learner changes anything in response, the original result remains visible and the work returns to the owning module.

### Lesson 8 gate

Calibration discussion must name all four outcomes and may not claim a stable calibration curve.

### Lesson 9 gate

Subgroup denominators and outcomes must appear before rates. Suppressed rows may not be ranked.

### Lesson 10 gate

The copied workspace must rebuild outputs into a new directory, refuse an existing target, pass validation, and end with a human-owned recommendation.

## 7. Data partitions and fit boundaries

### Frozen temporal split

| Partition | Rows | Outcomes | Primary use |
|---|---:|---:|---|
| Training | 224 | 25 | parameter and preprocessing fitting |
| Validation | 75 | 7 | candidate and threshold selection |
| Test | 75 | 4 | one-time locked evaluation |

### Training rules

Training data may:

- estimate the baseline prevalence;
- fit centering and scaling;
- learn one-hot categories;
- fit model parameters;
- support stratified resampling; and
- expose training instability.

Training data may not replace validation for candidate selection or test for final locked evaluation.

### Validation rules

Validation data may:

- compute the four declared selection metrics;
- determine whether an eligible model meets the selection rule;
- compare exact threshold consequences; and
- lock one threshold.

Validation data may not fit model parameters, add a predictor after the fact, rewrite the outcome, or justify the leaked model.

### Test rules

Test data may:

- receive predictions from the frozen pipeline;
- receive labels from the locked threshold;
- produce final teaching metrics;
- produce exact confusion counts;
- produce the bounded calibration display; and
- produce count-first subgroup evidence.

Test data may not:

- select the model;
- tune the threshold;
- choose a metric after seeing results;
- change the feature set;
- change the subgroup rule;
- create a new calibration method; or
- rewrite the recommendation standard.

### One-time test policy

"One-time" means one use for this versioned model contract. The deterministic builder may reproduce the exact evaluation for verification. Reproduction is not a new model-selection use. Any substantive change creates a new versioned development cycle and cannot silently recycle the original test as if untouched.

### Fit-boundary evidence

The contract and code must show:

- training indices passed to every fit;
- fold-specific preprocessing during resampling;
- validation passed only to prediction methods;
- test passed only to the frozen selected model; and
- no post-index field in an eligible feature set.

## 8. Candidate model contracts

### Shared rules

All models predict `acute_return_90d` at the end of the index encounter. Eligible candidates are fit on the same 224 training rows and evaluated on the same 75 validation rows. The seed is 20260830.

### `BASE`

| Property | Contract |
|---|---|
| Type | constant probability |
| Probability | 25/224 = 0.111607142857 |
| Inputs | none |
| Role | retained comparator |
| Selection | never called a complex candidate |

The baseline is not removed when a candidate looks promising. It anchors average precision, Brier score, and log loss to the outcome rate.

### `LOG01`

| Property | Contract |
|---|---|
| Type | unpenalized logistic regression |
| Features | centered age decade, prior acute count, inpatient indicator |
| Preprocessing | standard scaling fit inside training |
| Solver | LBFGS |
| Maximum iterations | 10000 |
| Role | eligible interpretable candidate from Module 02 |

Its Module 02 coefficient interpretation does not guarantee useful validation performance.

### `ML01`

| Property | Contract |
|---|---|
| Type | random forest classifier |
| Trees | 300 |
| Maximum depth | 4 |
| Minimum leaf rows | 20 |
| Class weights | none |
| Workers | 1 |
| Random state | 20260830 |
| Role | bounded machine-learning comparison |

Numeric fields are standardized for one consistent pipeline even though the tree model does not require scale normalization. Categorical fields are one-hot encoded. The resulting 15 columns are recorded.

The depth and leaf limits keep the exercise bounded. Learners do not run a hyperparameter search.

### `LEAK01`

| Property | Contract |
|---|---|
| Type | logistic critique fixture |
| Fields | `next_30d_state`, `endpoint_90d` |
| Defect | post-index and outcome-derived information |
| Eligible | never |
| Required action | reject before performance review |

Its near-perfect validation evidence is intentionally preserved to teach that data timing dominates leaderboard position.

### No silent model expansion

Adding a new model, hyperparameter grid, ensemble, feature-selection method, imputer, calibration method, or class-weighting rule changes the contract and returns to Module 03 design before test use.

### Deterministic refit artifact

The package does not serialize a binary model object. It preserves:

- exact source fingerprints;
- pinned dependencies;
- full model parameters;
- feature lists;
- preprocessing rules;
- fixed seed;
- deterministic build code; and
- exact reference predictions.

That deterministic refit contract is smaller, reviewable, and adequate for this teaching package. A production registry is out of scope.

## 9. Training-only resampling

### Purpose

Resampling shows how candidate evidence varies across training subsets. It does not decide the final model and does not replace the later temporal partitions.

### Method

- five stratified folds;
- shuffling within training only;
- random state 20260830;
- 44 or 45 holdout rows per fold;
- five positive outcomes per holdout fold;
- fold-specific baseline prevalence;
- fold-specific preprocessing and model fitting; and
- four metrics per model.

### Output contract

`resampling-results.csv` contains 15 rows:

- five for `BASE`;
- five for `LOG01`; and
- five for `ML01`.

Each row records model, fold, fit rows, holdout rows, holdout outcomes, fold baseline probability, ROC AUC, average precision, Brier score, log loss, and the partition rule.

### Reference variability

`LOG01` fold ROC AUC ranges from 0.50512821 to 0.83500000. `ML01` ranges from 0.58500000 to 0.88000000. That variation prevents a simple "best model" story from training resampling alone.

### Leakage-safe pipeline gate

For each fold:

1. select training-fit indices;
2. clone the candidate pipeline;
3. fit transforms and model on those rows;
4. predict the fold holdout; and
5. discard the fitted fold object.

Any transform learned before step 1 fails.

### Interpretation boundary

Stratification balances the rare outcome across folds for teaching. It does not reproduce the temporal ordering of future use. Validation and test remain date ordered.

## 10. Validation comparison and selection rule

### Same-row comparison

All four models produce predictions for the same 75 validation rows with 7 outcomes and 68 nonoutcomes.

### Declared metrics

| Metric | Question | Better direction | Does not establish |
|---|---|---|---|
| ROC AUC | How well are outcomes ranked above nonoutcomes? | higher | calibration or threshold utility |
| Average precision | How concentrated are outcomes among higher scores under imbalance? | higher | calibrated probabilities |
| Brier score | How close are probabilities to binary outcomes by squared error? | lower | a clinical consequence threshold |
| Log loss | How strongly are wrong confident probabilities penalized? | lower | subgroup fairness |

### Reference validation results

| Model | ROC AUC | Average precision | Brier | Log loss | Eligibility |
|---|---:|---:|---:|---:|---|
| `BASE` | 0.50000000 | 0.09333333 | 0.08495615 | 0.31195460 | comparator |
| `LOG01` | 0.44957983 | 0.09196407 | 0.08615760 | 0.31945157 | eligible |
| `ML01` | 0.58613445 | 0.15806484 | 0.08468750 | 0.30994807 | eligible |
| `LEAK01` | 1.00000000 | 1.00000000 | 0.00000014 | 0.00015329 | prohibited |

### Candidate rule

An eligible candidate passes only when all three conditions hold:

1. Brier score is no worse than `BASE`;
2. ROC AUC is at least 0.55; and
3. average precision is no worse than `BASE`.

### Mechanical result

| Model | Brier rule | ROC rule | AP rule | Result |
|---|---|---|---|---|
| `LOG01` | fail | fail | fail | not selected |
| `ML01` | pass | pass | pass | selected |

Exactly one eligible candidate passes. If zero or more than one passed, the reference code would stop instead of inventing a tie-break.

### Why `LOG01` still matters

`LOG01` remains valuable because it tests whether the interpretable Module 02 model generalizes as a predictor. Its failure under the frozen rule is a learning result, not a reason to rewrite its coefficient interpretation.

### Why `ML01` is not declared superior

The correct statement is:

> `ML01` is the only eligible candidate that meets this version's validation rule on these 75 synthetic validation rows.

"Superior model" would imply a broader comparison, stronger evidence, or stable external result that this module does not provide.

## 11. Leakage failure case

### Field timing

`next_30d_state` describes what happens after the index encounter. `endpoint_90d` is derived from the outcome follow-up endpoint. Neither is available as a valid pre-outcome predictor at the Module 01 prediction time.

### Required reasoning order

The learner must:

1. inspect field meaning and timing;
2. declare both fields prohibited;
3. mark `LEAK01` ineligible;
4. only then view its metrics; and
5. explain why the strong metrics are expected from leakage.

### Reference evidence

- ROC AUC: 1.00000000.
- Average precision: 1.00000000.
- Brier score: 0.00000014.
- Required status: never eligible.

### Failure principle

Performance cannot repair an invalid prediction-time contract. A model can be computationally correct and analytically useless because it knows the future.

### Integrity trap

Placing `LEAK01` on an ordinary leaderboard without a prominent eligibility failure encourages the wrong inference. The release separates performance evidence from selection eligibility.

## 12. Threshold selection and decision consequences

### Purpose

The model outputs probabilities. A binary action requires a threshold. The threshold must follow a stated consequence rather than defaulting to 0.5 or being tuned on test.

### Declared consequence

On validation, the teaching rule requires sensitivity of at least 5 of 7 outcomes. This permits no more than 2 false negatives in the 7-outcome validation set.

### Tie-break

Among thresholds meeting the minimum sensitivity:

1. choose the fewest false positives; and
2. if tied, choose the highest threshold.

### Candidate threshold set

The candidate set contains every distinct validation probability emitted by `ML01`. There are 71 distinct thresholds. The table preserves exact TN, FP, FN, TP, sensitivity, specificity, PPV, NPV, and rule status at each one.

### Locked result

- Threshold: 0.08513264.
- Validation minimum sensitivity: 5/7 = 0.71428571.
- Validation TN: 38.
- Validation FP: 30.
- Validation FN: 2.
- Validation TP: 5.
- Locked before test: yes.

### Why not 0.5

The selected model's test probabilities range only from 0.06366790 to 0.19038825. A default 0.5 threshold would label every test row negative. A threshold must match the score distribution and decision consequence.

### Why the threshold is not clinical guidance

The validation consequence is an instructional fixture. It has not been elicited from a clinical workflow, patient preference, capacity limit, harm analysis, or utility study. Module 03 teaches the method of locking a consequence-based threshold, not a deployable cutoff.

### Return rule

Changing the minimum sensitivity, false-positive preference, tie-break, or candidate threshold set after seeing test results invalidates the lock and returns to Module 03 design.

## 13. Test discrimination and probability error

### One-time evaluation

The selected training-fit `ML01` pipeline produces one probability for each of the 75 test rows. The locked threshold is applied without refitting or adjustment.

### Baseline test evidence

| Metric | `BASE` |
|---|---:|
| ROC AUC | 0.50000000 |
| Average precision | 0.05333333 |
| Brier score | 0.05388473 |
| Log loss | 0.22897744 |

The baseline average precision equals the 4/75 test prevalence because every score is identical.

### Selected-model test evidence

| Metric | Point | Lower 95% | Upper 95% |
|---|---:|---:|---:|
| ROC AUC | 0.58802817 | 0.26760563 | 0.91549296 |
| Average precision | 0.14682471 | 0.05532198 | 0.58716356 |
| Brier score | 0.05097579 | 0.04638885 | 0.05459675 |
| Log loss | 0.21218264 | 0.19050467 | 0.22977890 |

### Bootstrap contract

- method: outcome-stratified percentile bootstrap;
- replicates: 2000;
- seed: 20260830;
- resample four outcomes with replacement;
- resample 71 nonoutcomes with replacement;
- recompute each metric and threshold rate; and
- report the 2.5th and 97.5th percentiles.

### Interpretation

`ML01` has better point estimates than baseline for all four probability metrics on this test set. The evidence is weakly determined because only four outcomes exist. The wide ROC AUC and average-precision intervals prevent a stable superiority claim.

### No significance substitution

The module does not add a p-value for model superiority. The decision uses the predeclared workflow, point estimates, intervals, exact consequences, and limitations together.

## 14. Confusion measures, prevalence, and class imbalance

### Exact table

| | Predicted negative | Predicted positive | Total |
|---|---:|---:|---:|
| Observed negative | 48 | 23 | 71 |
| Observed positive | 2 | 2 | 4 |
| Total | 50 | 25 | 75 |

### Required calculations

| Measure | Calculation | Value |
|---|---|---:|
| Prevalence | 4/75 | 0.05333333 |
| Sensitivity | 2/(2+2) | 0.50000000 |
| Specificity | 48/(48+23) | 0.67605634 |
| PPV | 2/(2+23) | 0.08000000 |
| NPV | 48/(48+2) | 0.96000000 |

### Consequence language

At the locked threshold:

- 2 of 4 outcome rows are flagged;
- 2 of 4 outcome rows are missed;
- 23 of 71 nonoutcome rows are flagged; and
- 48 of 71 nonoutcome rows are not flagged.

Counts come before labels such as acceptable or poor because acceptability depends on clinical consequences not established here.

### Accuracy trap

Accuracy is (48+2)/75 = 0.66666667. A model that labels every row negative would be 71/75 = 0.94666667 accurate while missing all outcomes. Accuracy alone therefore fails the module's class-imbalance requirement.

### NPV trap

NPV is high because outcomes are rare and 48 true negatives dominate its denominator. The workflow still misses half of the observed outcomes. NPV does not prove safety.

### Baseline threshold illustration

The constant baseline probability equals its threshold and the implementation uses greater than or equal to. It therefore labels all test rows positive: sensitivity 1, specificity 0, and PPV equal to prevalence. This illustrates threshold behavior and is not a proposed policy.

## 15. Calibration, uncertainty, and accessible displays

### Calibration table construction

Test rows are ordered by selected probability and divided into five groups of 15. Each group reports:

- rows;
- outcomes;
- mean predicted probability;
- observed outcome proportion;
- minimum probability;
- maximum probability; and
- a small-sample interpretation limit.

### Reference groups

| Group | Rows | Outcomes | Mean probability | Observed proportion |
|---:|---:|---:|---:|---:|
| 1 | 15 | 0 | 0.07065743 | 0.00000000 |
| 2 | 15 | 2 | 0.07692731 | 0.13333333 |
| 3 | 15 | 0 | 0.08033173 | 0.00000000 |
| 4 | 15 | 1 | 0.09035687 | 0.06666667 |
| 5 | 15 | 1 | 0.14452712 | 0.06666667 |

### Interpretation boundary

The observed proportions are not monotonic. Four outcomes cannot support a stable calibration curve, intercept, or slope. The table demonstrates how to compare predicted and observed values while teaching when not to overfit a calibration narrative.

### Deliberate omission

The package does not add a calibration intercept, slope, Hosmer-Lemeshow test, or recalibration model. Those outputs would be fragile with four outcomes and would not change the progression decision.

### Calibration SVG requirements

The SVG must include:

- an internal title;
- an internal description;
- named axes;
- a reference diagonal;
- a line and points for the five groups; and
- a statement that exact values are in the CSV.

### Threshold SVG requirements

The SVG must include:

- an internal title;
- an internal description;
- named axes;
- labeled sensitivity and specificity lines;
- a visible locked-threshold marker; and
- a statement that exact counts are in the CSV.

### Structured alternatives

The SVG files are never the sole assessment evidence. `calibration-table.csv` and `threshold-table.csv` are the authoritative exact alternatives.

### Color boundary

Color distinguishes series but does not carry exact meaning alone. Text labels, line position, threshold marker, titles, descriptions, and tables remain available.

## 16. Subgroup evidence and suppression

### Fields

The module reports observed test categories for:

- gender;
- race;
- ethnicity; and
- index class.

There are ten observed subgroup rows.

### Count-first contract

Every row must report:

- subgroup field;
- category;
- total rows;
- positive outcomes;
- negative outcomes;
- suppression status; and
- reason.

Only then may it report ROC AUC, sensitivity, specificity, and PPV.

### Suppression rule

Metrics are suppressed when:

- total rows are fewer than 20; or
- positive outcomes are fewer than 2; or
- negative outcomes are fewer than 2.

### Reference suppression

Suppressed rows are:

- Asian race: 7 rows, 0 outcomes;
- Black race: 8 rows, 0 outcomes;
- Native race: 1 row, 0 outcomes;
- Hispanic ethnicity: 7 rows, 0 outcomes; and
- inpatient index class: 6 rows, 1 outcome.

### Unsuppressed does not mean stable

The remaining five rows pass the mechanical reporting rule but still contain few outcomes. Their metrics are descriptive teaching estimates. The release does not rank them or test differences.

### Prohibited claims

The learner may not claim:

- equal performance;
- unfair performance;
- absence of bias;
- protected-group safety;
- subgroup superiority;
- subgroup calibration; or
- a need to remove a protected attribute solely from these rows.

### Required language

The learner may say:

> The available test evidence is too sparse for a fairness conclusion. Counts and suppression identify where additional evidence and governance would be required.

### Future route

A later fairness assessment would require a purpose-specific group definition, adequate outcomes, uncertainty, consequences, stakeholder review, and a real validation population. It is not added speculatively here.

## 17. Exact learner deliverables and package contract

### Required teaching and decision files

| File | Required content |
|---|---|
| `README.md` | learner workflow and boundary |
| `VERSION` | module version 0.1.0 |
| `requirements.txt` | pinned Python environment |
| `data-spec.md` | source, grain, timing, fields, and boundary |
| `source-record.yml` | exact source identity and fingerprints |
| `model-contract.json` | models, features, parameters, rules, and seed |
| `assessment.md` | rubric and gates |
| `prediction-evaluation-report.md` | complete interpretation and recommendation |
| `figure-accessibility.md` | visual and structured-alternative checks |
| `environment-note.md` | actual execution environment |
| `reproducibility-check.md` | commands, results, facts, and differences |
| `ai-use.md` | assistance, shared data, checks, and accountability |
| `progression-decision.md` | Checkpoint 1 recommendation and conditions |
| `build_prediction_evidence.py` | deterministic build |
| `validate_prediction_evidence.py` | release and submission validation |

### Required copied inputs

The learner workspace contains all seven upstream artifacts in `data/`. Their bytes and hashes must remain exact.

### Required CSV outputs

| File | Rows | Fields | Purpose |
|---|---:|---:|---|
| `resampling-results.csv` | 15 | 11 | training variability |
| `validation-predictions.csv` | 300 | 8 | exact same-row predictions |
| `validation-comparison.csv` | 4 | 10 | selection metrics |
| `model-selection-record.csv` | 4 | 7 | rule application |
| `threshold-table.csv` | 71 | 10 | validation consequences |
| `threshold-decision.csv` | 1 | 5 | locked threshold |
| `test-predictions.csv` | 75 | 8 | one prediction per test row |
| `test-metrics.csv` | 16 | 9 | baseline and selected evidence |
| `confusion-table.csv` | 4 | 4 | exact locked counts |
| `calibration-table.csv` | 5 | 8 | grouped probability evidence |
| `subgroup-metrics.csv` | 10 | 11 | counts and suppression |
| `transformed-feature-names.csv` | 15 | 4 | pipeline audit |
| `leaked-model-failure.csv` | 1 | 8 | leakage critique |
| `prediction-checks.csv` | 22 | 5 | fixed release invariants |

### Required non-CSV outputs

| File | Purpose |
|---|---|
| `calibration.svg` | accessible visual companion |
| `threshold.svg` | accessible visual companion |
| `build-report.json` | source, partition, selection, decision, and fingerprint record |

### Reference output fingerprints

| Output | SHA-256 |
|---|---|
| `resampling-results.csv` | `d4fa7767dc2c9ff5d393eb1835574642074ff3c7ad9bdeb5e9e5d837598caefa` |
| `validation-predictions.csv` | `ae486033900b22367f1055244d03961c05f37c030ec8462d721e66350a9221e3` |
| `validation-comparison.csv` | `c5d1375989cbf1cca9cd5664c1dbffa2d139081e01faa9b37997ab055a3127b1` |
| `model-selection-record.csv` | `477a1527d42ade4f6c5259492ea7b28838dc20fbe757ac3539f33d7b4d77b4d0` |
| `threshold-table.csv` | `0855e495d327e51ddde4428e09ecb0a567997b61a4135156ae3f3be1d7086d76` |
| `threshold-decision.csv` | `e953fac6d048bb095b83691492da764a72bd597e5bd7a3b6d2a4994f57ba5af8` |
| `test-predictions.csv` | `531c00d310292aeeaea476d1c94e128f5c81c34c2fc60e014d2c157e152b7438` |
| `test-metrics.csv` | `9d43a8085e835cbf368962acc37b0bed00bdfacf68e73ce87d0b359dee490bc9` |
| `confusion-table.csv` | `a899fc8ebaee87fd2990354f6310c6feb87f748e17545c5c39c5a413e630be87` |
| `calibration-table.csv` | `fce4d9b0a05085ab51cb5af1c9a2dcb209a9fb2d099b3245650543a09c461b5c` |
| `subgroup-metrics.csv` | `7f95ec1f99a1f9f9bae6af566798a4f3aab9107681fe7e79c1ce27a821e07d24` |
| `transformed-feature-names.csv` | `da0ce00b3c2f8d36dbe4e3741c66991f46b97d205368e2508d6c44d741e36acf` |
| `leaked-model-failure.csv` | `facbda4fcd1e88e81798c7c6b484c1c4ad8f359b26200a6a768bf38a7b3d3c5e` |
| `prediction-checks.csv` | `5c741ed9c8e5b0d7490109abdb491bf279037dadedd398534dafbf0c9f7c079a` |
| `calibration.svg` | `00b4b3d047d5cff97e1d9d78d69169d07d85227e209666eeaa85bdc319f38181` |
| `threshold.svg` | `658858993937ac7af53efb51ada89bf7459c978d2d8480caee4809b09c6aa386` |
| `build-report.json` | `72cb42773dc535cb67180f3b0a069b2cdd1c3cc0e01b4926f885b9cfe83d6959` |

### No screenshot-only evidence

A screenshot, notebook display, or copied metric is not sufficient. The structured outputs, code, inputs, and reproduction record are required.

### File portability

Learner-facing text, code, and metadata must not contain a local absolute path, credential, token, private URL, or real patient identifier.

## 18. Assessment, rubric, gates, and checkpoint assembly

### Fifteen-point rubric

| Criterion | Points |
|---|---:|
| Leakage-safe preprocessing, resampling, and model lock | 3.00 |
| Baseline, validation comparison, and selection rule | 2.50 |
| Untouched test discrimination and calibration evidence | 3.00 |
| Threshold, confusion measures, prevalence, and decision meaning | 2.50 |
| Subgroup counts, uncertainty, sparse-outcome limits, and failure analysis | 2.50 |
| Accessible evidence, reproduction, and responsible agent record | 1.50 |
| Total | 15.00 |

### Numeric threshold

The minimum numeric score is 12.00 of 15.00. The threshold cannot compensate for a failed gate.

### Performance levels

| Level | Description |
|---|---|
| Full | Exact evidence, correct partition reasoning, bounded interpretation, and independent defense. |
| Partial | Mostly correct evidence with a correctable explanation or record defect. |
| Insufficient | Missing, changed, leaked, test-guided, inaccessible, irreproducible, or materially overclaimed evidence. |

### Noncompensable gates

1. Seven upstream fingerprints unchanged.
2. Split counts remain 224/75/75.
3. Outcome counts remain 25/7/4.
4. Preprocessing fit on training only.
5. Validation never fits model parameters.
6. Test never shapes a feature, model, threshold, metric, subgroup rule, plot, or narrative.
7. Constant baseline retained.
8. Candidates compared on identical validation rows and metrics.
9. `LEAK01` rejected before performance review.
10. Exactly one eligible candidate selected by the frozen rule.
11. Threshold consequence and tie-break declared.
12. Threshold locked before test.
13. Exactly one selected prediction per test row.
14. Confusion counts sum to 75 and conserve four outcomes.
15. Discrimination, probability error, calibration, and utility not substituted.
16. Four-outcome limitation remains visible.
17. Counts precede subgroup metrics and unsupported cells are suppressed.
18. Exact tables accompany plots.
19. No real-clinical, fairness, safety, causal, or deployment claim.
20. Reproduction, environment, AI-use, and human decision records complete.

### Scoring notes

- Correct code with an invalid partition receives no fit-protection credit.
- A perfect leaked model fails the leakage gate.
- Correct metric arithmetic without decision meaning earns partial credit only.
- A favorable recommendation that omits four outcomes or 23 false positives fails the interpretation gate.
- An accessible table can preserve evidence when a plot cannot be interpreted visually.
- AI disclosure earns no credit unless independent checking is also recorded.

### Checkpoint assembly

The Week 3 checkpoint may assemble only when:

- Modules 01, 02, and 03 validators pass;
- all three numeric minimums are met;
- every gate passes;
- a reviewer records one allowed recommendation;
- all return conditions are resolved; and
- the release remains within the synthetic teaching boundary.

### Reference score position

The reference package is a technical answer key, not an automatically graded learner submission. A learner must still explain the decisions and limits independently.

## 19. Feedback, revision, recovery, and support

### Feedback order

Reviewers provide feedback in this order:

1. data timing and leakage;
2. partition and fit boundaries;
3. model eligibility and selection;
4. threshold rule and lock;
5. test counts and metric quantities;
6. calibration and uncertainty;
7. subgroup suppression;
8. claim boundaries;
9. reproduction and accessibility; and
10. prose clarity.

Earlier defects can invalidate later interpretation, so cosmetic feedback comes last.

### Revision cycle

1. Classify the defect and owning module.
2. Preserve the original package and test evidence.
3. Correct prompts or explanation when the contract is unchanged.
4. Version the module when the contract changes.
5. Rebuild into a new target.
6. Re-run validation.
7. Record the difference.
8. Obtain a new human recommendation.

### High-impact revision examples

| Defect | Required response |
|---|---|
| Encoder fit on all data | stop, correct pipeline, version, and do not call original test untouched |
| Test used to add a predictor | return to Module 03 design and create a new external evaluation plan |
| Leaked model selected | stop and redo eligibility review |
| Threshold changed after test | preserve original result and return to threshold design |
| Four outcomes omitted | revise interpretation and recommendation |
| Suppressed subgroup ranked | remove ranking and redo subgroup defense |
| Source fingerprint changed | return to owning source module |
| Output does not reproduce | resolve environment, input, or code difference before progression |

### Supported environment route

The primary route uses Python 3.12.10 with pinned packages. If a learner cannot install the environment, an instructor may provide a managed environment. The learner still owns interpretation and records the actual environment.

### Computational accommodation

The reference build uses 300 small trees and 2000 bootstrap replicates and completes on an ordinary laptop. If an accommodation requires supplied reference outputs, the learner may analyze those outputs, but the accommodation and reproduction ownership must be explicit.

### Accessibility route

A learner who cannot use the SVGs may complete the full assessment from the CSV alternatives. No visual reading is required to obtain exact values.

### Extension principle

An extension should deepen reasoning with the existing evidence before adding models. Appropriate extensions include alternate consequence narratives applied to the frozen threshold table or structured critique of subgroup evidence. Hyperparameter searches are out of scope.

## 20. Responsible AI, privacy, accessibility, and integrity

### AI may assist with

- explaining metric definitions;
- checking code structure;
- drafting alternative prose;
- generating questions for an oral defense;
- finding inconsistent counts;
- suggesting accessible descriptions; and
- formatting a decision record.

### AI may not own

- the prediction-time judgment;
- feature eligibility;
- the leakage decision;
- the threshold consequence;
- the clinical interpretation;
- subgroup meaning;
- the final recommendation;
- source verification; or
- independent validation.

### Required AI-use evidence

The learner records:

- tool or model name;
- task supported;
- data shared;
- generated content retained;
- independent checks;
- corrections made; and
- accountable human.

### Prompt boundary

No prompt may include real patient data, credentials, tokens, private URLs, restricted records, or other secrets. This repository contains synthetic teaching data only.

### Integrity traps

- asking an agent to pick the best model from test results;
- copying a metric explanation without checking its denominator;
- hiding leakage because the result is strong;
- replacing a suppressed subgroup cell with an invented estimate;
- claiming reproduction without running the build;
- describing the random forest as clinically intelligent; and
- treating validator success as proof of clinical validity.

### Accessibility requirements

- exact data available in structured tables;
- SVG title and description present;
- axes and series labeled;
- color not the only carrier of meaning;
- no screenshot-only submission;
- meaningful reading order in Markdown;
- plain-language metric explanations; and
- no inaccessible requirement hidden only in a visual.

### Privacy and security gate

The release must contain no real patient record, direct identifier, secret, credential, token, private endpoint, local absolute path, or restricted source. Discovery of one stops release and triggers removal and incident handling.

### Human accountability

Automation can reproduce the calculations and reject known structural failures. A named human remains accountable for the threshold consequence, interpretation, use boundary, and progression decision.

## 21. Validation, acceptance tests, risks, and continuation contract

### Builder self-check

The builder must prove that it can:

- verify all seven upstream fingerprints;
- rebuild every CSV and SVG in a clean temporary directory;
- select `ML01`;
- lock threshold 0.08513264;
- reproduce 48/23/2/2 test confusion counts;
- refuse an existing output target;
- create a copied learner workspace;
- rebuild from copied inputs; and
- reproduce identical output metadata.

### Validator self-check

The validator must prove that it can:

- accept the reference release;
- accept the prompted starter package;
- reject the starter as a completed submission;
- reject a package missing a required output;
- compare every CSV field and value;
- compare both SVG files byte for byte;
- compare the build report;
- verify upstream bytes and hashes;
- verify the model contract;
- verify release metadata; and
- reject unresolved prompts or prohibited paths.

### Acceptance commands

From the repository root:

```powershell
python courses/modeling-inference-reproducible-analytics/modules/03-prediction-evaluation/build_prediction_evidence.py --self-check
python courses/modeling-inference-reproducible-analytics/modules/03-prediction-evaluation/validate_prediction_evidence.py --self-check
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/check-curriculum-specs.ps1
```

The repository's actual full checker command takes precedence if renamed. The release record captures the executed command and result.

### Technical acceptance criteria

- module version is 0.1.0;
- Commons version is 0.41.0;
- package files are complete;
- all upstream fingerprints pass;
- all 22 prediction checks pass;
- builder self-check passes;
- validator self-check passes;
- reference release passes 4601 checks;
- starter package passes 4549 checks;
- incomplete and broken packages are rejected;
- repository-wide curriculum checks pass;
- source and decision boundaries are visible; and
- work is committed and pushed.

### Known material limitations

1. All data are synthetic and do not establish real clinical performance.
2. Training contains 25 outcomes, validation 7, and test 4.
3. Test discrimination and calibration estimates are unstable.
4. The locked threshold yields 23 false positives and 2 false negatives.
5. Subgroup results are sparse and partly suppressed.
6. The threshold consequence is a teaching fixture, not a clinical utility study.
7. The candidate set is deliberately bounded and not an exhaustive search.
8. Named clinical prediction, model-risk, statistical, informatics, accessibility, privacy, responsible-AI, and independent-instructor reviews remain pending.

### Risks and controls

| Risk | Control |
|---|---|
| Optimistic preprocessing | fit inside every training fit |
| Validation overfitting | fixed small candidate set and rule |
| Test-guided tuning | lock model and threshold first |
| Leakage | prohibited fixture and eligibility gate |
| Metric substitution | four metrics plus exact counts |
| Rare-outcome illusion | prevalence and four outcomes visible |
| Calibration overclaim | five groups and explicit instability |
| Subgroup overclaim | counts, suppression, no ranking |
| Reproduction drift | pinned versions, hashes, seed, validator |
| Deployment overclaim | explicit teaching-only boundary |

### Required human reviews before alpha

- clinical prediction review;
- model-risk review;
- biostatistical review;
- clinical-informatics review;
- clinician consequence review;
- accessibility review;
- privacy and security review;
- responsible-AI review; and
- independent instructor dry run.

### Reference recommendation

`continue to validity review with conditions`.

The conditions are:

1. preserve the original locked test result;
2. keep four outcomes and wide uncertainty visible;
3. carry 23 false positives and 2 false negatives forward;
4. treat predictors as predictive rather than causal roles;
5. preserve subgroup suppression;
6. retain accessible exact tables;
7. make no real-clinical or deployment claim; and
8. require Module 04 validity review before broader use language.

### Release record

- Module release: 0.1.0.
- Commons release: 0.41.0.
- Release date: 2026-08-30.
- Reference outputs: 14 CSV files, 2 SVG files, and 1 build report.
- Prediction checks: 22 pass.
- Builder self-check: pass.
- Validator self-check: pass.
- Reference validator checks: 4601.
- Starter validator checks: 4549.
- Existing-target refusal: pass.
- Incomplete-submission rejection: pass.
- Broken-package rejection: pass.
- Reference recommendation: continue to validity review with conditions.

### Contributors

- Shuhan He: Commons sponsor and curriculum direction.
- OpenAI Codex: module specification, prediction build, validator, and teaching package.

### Week 3 continuation contract

After this module is committed and pushed, build FND-2 Checkpoint 1. The checkpoint must assemble rather than recompute Modules 01 through 03. It must preserve every source and output fingerprint, apply the 40-point rubric, enforce all upstream gates, record reviewer and learner defenses, and issue one allowed cumulative disposition.

Do not begin Module 04 from an informal chat summary. Begin from the accepted Checkpoint 1 package and this exact handoff.

### Resume record

FND-2 Module 03 is complete as a runnable reference candidate at Commons 0.41.0 when all acceptance commands pass and the unit is committed and pushed. Resume with FND-2 Checkpoint 1 only. Do not reopen the selected model, validation rule, threshold, test evidence, subgroup rule, or teaching-use boundary without a documented return and semantic-version decision.
