# FND-2 Checkpoint 1: Modeling-readiness and prediction-evaluation release

## 1. Checkpoint identity and place in the course

### Release identity

- Course: FND-2, Modeling, Inference, and Reproducible Analytics.
- Checkpoint: 01 of 03.
- Checkpoint ID: `oclc-fnd2-cp1`.
- Checkpoint version: 0.1.0.
- Commons release target: 0.42.0.
- Due: end of instructional Week 3.
- Cumulative learner work: 48.0 hours.
- Course points: 40.
- Required tag: `fnd2-checkpoint1-v0.1.0`.
- Package: `courses/modeling-inference-reproducible-analytics/checkpoints/01-modeling-readiness-release/`.
- Status target: runnable release candidate.
- Data class: synthetic public teaching data.
- Real clinical use: prohibited.

### Purpose

Checkpoint 1 is the first cumulative FND-2 decision. It freezes the accepted work from Modules 01 through 03 and asks whether the modeling question, reproducible workspace, regression evidence, prediction pipeline, held-out evaluation, and use boundary are coherent enough to enter validity review.

The checkpoint assembles evidence. It does not recompute models, choose a new threshold, edit module outputs, or hide a weak result. Its job is to preserve provenance, reconcile the three modules, test cumulative gates, assess a technical defense, and issue an explicit Module 04 progression decision.

### Why the checkpoint is cumulative

A prediction result cannot be reviewed safely without its earlier decisions. The selected model depends on:

- the decision and analytic aim;
- population and time zero;
- outcome and horizon;
- feature roles and prediction-time availability;
- the deterministic split;
- the simple baseline;
- regression formulas and interpretation;
- training-only preprocessing;
- validation selection; and
- the threshold lock.

The checkpoint keeps those dependencies in one reviewable package.

### Relationship to Module 01

Module 01 contributes the aim, target, population, prediction time, feature-role contract, split, baseline, environment, source identity, and reproducibility evidence. These artifacts remain immutable in the checkpoint.

### Relationship to Module 02

Module 02 contributes formulas, encodings, reference levels, regression results, uncertainty, diagnostics, sparse-data evidence, R reading, interpretation, and the accepted `LOG01` handoff. These artifacts remain immutable.

### Relationship to Module 03

Module 03 contributes the training resampling, validation predictions, model comparison, leakage failure, model lock, threshold lock, test predictions, metrics, confusion counts, calibration, subgroup evidence, accessible figures, and prediction recommendation. These artifacts remain immutable.

### Relationship to Module 04

Only `accept` and `accept with conditions` permit Module 04. Module 04 receives the exact checkpoint identity, module versions, manifest, cumulative interpretation, conditions, and progression decision. It may add validity evidence but may not rewrite the original test result.

### Required starting state

Checkpoint assembly begins only when:

- Module 01 version 0.1.0 is accepted;
- Module 02 version 0.1.0 is accepted;
- Module 03 version 0.1.0 is accepted;
- every module validator passes;
- the accepted FND-1 source identity remains present;
- the 374-row modeling cohort fingerprint is unchanged;
- the 224/75/75 split and 25/7/4 outcome counts are unchanged;
- the Module 03 test result remains untouched; and
- no cumulative record has been used to alter module evidence.

### Required ending state

The checkpoint ends with:

- 72 immutable upstream module artifacts;
- 6 immutable checkpoint control files;
- a 78-row immutable release manifest;
- 10 completed cumulative records;
- exactly 89 assembled files;
- a reconciled 40-point score;
- 23 passing noncompensable gates;
- an adequate 12-question technical defense;
- a reviewer record;
- a reproduction record;
- an explicit disposition; and
- an exact Module 04 handoff or return instruction.

## 2. Decision, owners, audience, and review question

### Decision owners

The primary decision owner is a clinical prediction and model-risk reviewer with biostatistical support. A course instructor acts as the release maintainer. Named clinical-informatics, accessibility, privacy, responsible-AI, and independent-instructor reviewers remain required before alpha.

### Primary audience

The checkpoint is written for:

- the learner defending the work;
- the technical reviewer deciding progression;
- the instructor giving cumulative feedback;
- a later Module 04 learner or reviewer needing exact starting evidence; and
- maintainers verifying what was accepted.

### Review question

> May the locked modeling cohort, split, regression evidence, prediction pipeline, evaluation, and use boundary enter validity review?

### Decision sequence

The owner decides in this order:

1. Is the package complete and reproducible?
2. Are all module identities and fingerprints intact?
3. Are the aim and prediction-time boundaries still coherent?
4. Are regression quantities and limits represented correctly?
5. Was the prediction workflow leakage safe?
6. Was selection and threshold locking completed before test?
7. Are the test counts, uncertainty, and sparse subgroups visible?
8. Does the learner defend the evidence adequately?
9. Are all 23 gates satisfied?
10. What disposition and Module 04 conditions follow?

### Allowed dispositions

| Disposition | Meaning | Module 04 |
|---|---|---|
| `accept` | Evidence and defense satisfy the checkpoint without additional technical conditions. | permitted |
| `accept with conditions` | Evidence and defense satisfy the checkpoint with explicit limits carried forward. | permitted |
| `revise` | Correctable cumulative or module-owned defect remains. | not permitted |
| `refer` | A specialist decision is needed before progression. | not permitted |

### Reference disposition

The reference disposition is `accept with conditions`. The package is technically coherent for validity teaching, but all data are synthetic, the test split has four outcomes, the threshold yields 23 false positives and 2 false negatives, subgroup evidence is sparse, and no clinical or deployment claim is supported.

### What acceptance does not mean

Acceptance does not approve:

- clinical use;
- model deployment;
- external validity;
- causal validity;
- stable calibration;
- fairness;
- prospective performance;
- patient-level benefit;
- workflow fit;
- safety; or
- operational monitoring.

## 3. Component map and weight preservation

### Source weights

The checkpoint preserves 40 course points:

- Module 01 setup and aim classification: 15 points;
- Module 02 regression evidence: 10 points; and
- Module 03 prediction evidence plus cumulative handoff: 15 points.

No artifact earns points twice.

### Corrected forty-point map

| ID | Criterion | Owner | Points |
|---|---|---|---:|
| A01 | Decision, aim, target, population, time zero, and horizon | Module 01 | 4.00 |
| A02 | Exact input, feature roles, prediction-time boundary, and leakage control | Module 01 | 4.00 |
| A03 | Deterministic split, outcome reconciliation, and simple baseline | Module 01 | 3.00 |
| A04 | Reproducible workspace, environment, build, and initial agent record | Module 01 | 4.00 |
| R01 | Declared formulas, encodings, references, and correct regression fitting | Module 02 | 4.50 |
| R02 | Assumptions, sparse data, influence, uncertainty, and interpretation | Module 02 | 5.50 |
| P01 | Leakage-safe pipeline, resampling, validation comparison, and model lock | Module 03 | 4.50 |
| P02 | Untouched test discrimination, calibration, threshold, and confusion evidence | Module 03 | 4.50 |
| P03 | Subgroup counts, uncertainty, failure analysis, access, and use boundary | Module 03 | 3.50 |
| H01 | Cumulative handoff, defense, reviewer evidence, and progression decision | Checkpoint | 2.50 |
| Total |  |  | 40.00 |

### Source correction record

The normalized course specification originally assigned H01 1.50 while displaying a 40.00 total. The rows therefore summed to 39.00. Checkpoint 1 corrects H01 to 2.50. This preserves the declared 15/10/15 module shares and makes the displayed total arithmetically true.

The correction changes no learner outcome, module evidence, or course weight. It repairs a one-point rubric transcription error.

### Component totals

| Component | Criteria | Points |
|---|---|---:|
| Module 01 | A01-A04 | 15.00 |
| Module 02 | R01-R02 | 10.00 |
| Module 03 and checkpoint handoff | P01-P03, H01 | 15.00 |
| Total |  | 40.00 |

### Score preservation rule

The checkpoint may record a lower cumulative score after review, but it may not change the points available, transfer points between criteria, create bonus points, or compensate for a failed gate.

### Numeric pass threshold

Passing requires at least 32.00 of 40.00, equivalent to 80 percent, plus every gate and an adequate defense.

### Feedback milestone rule

The Week 3 checkpoint is a scored release and a progression decision. Earlier module feedback remains visible. The cumulative review focuses on integration and does not erase module-specific returns.

## 4. Competencies and assessable outcomes

### Cumulative competencies

The learner can:

1. state the decision, prediction time, outcome, horizon, and population;
2. verify accepted source and cohort fingerprints;
3. explain every field role and leakage boundary;
4. reproduce the deterministic temporal split;
5. reconcile training, validation, and test outcome counts;
6. retain and interpret the training-prevalence baseline;
7. read the declared regression formulas and references;
8. interpret linear and logistic quantities correctly;
9. explain structural blanks and sparse-data conditions;
10. preserve diagnostic and uncertainty evidence;
11. audit training-only preprocessing and resampling;
12. apply the validation model-selection rule;
13. reject the deliberately leaked model;
14. explain the validation threshold consequence;
15. prove the model and threshold were locked before test;
16. interpret discrimination and probability error separately;
17. report exact confusion numerators and denominators;
18. interpret calibration with four outcomes;
19. report subgroup counts before metrics and respect suppression;
20. navigate the release manifest;
21. reproduce the cumulative package;
22. disclose material AI assistance;
23. defend the supported claim and use boundary; and
24. issue an explicit progression recommendation.

### Evidence map

| Competency group | Primary evidence |
|---|---|
| Aim and source | Module 01 plans, registries, role contract, source record |
| Split and baseline | Module 01 outputs and build report |
| Regression | Module 02 formula, reference, coefficient, diagnostic, and assumption evidence |
| Prediction selection | Module 03 resampling, validation, leakage, and lock records |
| Test evaluation | Module 03 predictions, metrics, confusion, calibration, and subgroups |
| Integration | cumulative interpretation and defense |
| Accountability | manifest, reproduction, AI-use, accessibility, reviewer, and disposition records |

### Minimum defense standard

An adequate defense:

- answers all 12 required questions;
- cites exact artifact paths;
- names counts and denominators;
- distinguishes prediction from causation;
- explains at least one material regression condition;
- explains why leakage invalidates performance;
- explains the threshold consequence;
- keeps four test outcomes visible;
- describes at least one return condition;
- does not rely on a screenshot or agent-generated summary; and
- is assessed by a named or explicitly pending accountable reviewer.

### Unsupported defense

The defense is inadequate when the learner:

- says only that validation passed;
- calls `ML01` clinically accurate;
- cannot identify prediction time;
- reads an odds ratio as a risk ratio;
- selects from test evidence;
- cannot state the confusion counts;
- hides the leaked model;
- ranks sparse subgroups;
- treats NPV as proof of safety; or
- cannot state what Module 04 must review.

## 5. Concept ownership and out-of-scope boundaries

### Checkpoint-owned integration

Checkpoint 1 owns:

- module identity reconciliation;
- artifact freezing;
- the immutable manifest;
- the cumulative 40-point score;
- the 23-gate record;
- the cumulative interpretation;
- the technical defense;
- reviewer evidence;
- cumulative reproduction;
- the progression disposition; and
- the exact Module 04 handoff.

### Module ownership retained

Module 01 still owns changes to:

- question;
- target;
- population;
- prediction time;
- outcome;
- horizon;
- field roles;
- split; and
- baseline.

Module 02 still owns changes to:

- formula;
- reference level;
- transformation;
- variance method;
- regression diagnostics;
- coefficient quantity; and
- regression interpretation.

Module 03 still owns changes to:

- candidate features;
- preprocessing;
- resampling;
- candidate models;
- selection metrics or rule;
- threshold rule;
- test-use policy;
- calibration display;
- uncertainty method;
- subgroup definitions; and
- suppression.

### Out of scope

The checkpoint does not add:

- new source rows;
- a new cohort;
- a new outcome;
- a new model;
- feature importance;
- hyperparameter tuning;
- recalibration;
- causal adjustment;
- missing-data analysis;
- longitudinal methods;
- forecasting;
- fairness testing;
- production code;
- monitoring; or
- deployment approval.

### No recomputation rule

The assembler copies accepted artifacts byte for byte and computes only their manifest metadata. Any analytic recomputation belongs to the owning module and must be completed before checkpoint assembly.

### No reinterpretation rule

The cumulative memo may synthesize accepted evidence but may not change its quantity, partition, conditions, or claim boundary.

## 6. Checkpoint sequence and learner work

### Assembly sequence

1. Confirm accepted Module 01 through 03 roots.
2. Verify required module files exist.
3. Verify module versions are all 0.1.0.
4. Verify the key source and output fingerprints.
5. Create a new checkpoint target.
6. Copy 72 module artifacts under preserved module namespaces.
7. Copy 6 checkpoint control files.
8. Copy 10 prompted cumulative records.
9. Generate the sorted 78-row immutable manifest.
10. Refuse any existing target.
11. Complete cumulative records.
12. Run checkpoint validation.
13. Complete the technical defense.
14. Record reviewer decisions and conditions.
15. Tag the accepted package.

### Reference sequence

The reference assembler uses the repository Module 01 through 03 release roots and completed checkpoint reference records. It creates the same folder contract as learner assembly.

### Learner sequence

The learner assembler accepts three completed module workspace paths. It copies only the checkpoint artifact contract, so unrelated notebooks, caches, environments, and scratch files do not enter the release.

### Protected target

The assembler refuses an existing path. This prevents a prior checkpoint, learner edit, or stale file from being silently overwritten.

### Cumulative writing sequence

The learner completes cumulative records in this order:

1. cumulative interpretation;
2. component score;
3. gate results;
4. technical defense;
5. reproduction record;
6. accessibility review;
7. AI-use record;
8. reviewer record; and
9. progression decision.

The README is completed as a navigation and release summary.

### Defense prompts

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

## 7. Upstream release inventory and immutable facts

### Module 01 identity

- ID: `oclc-fnd2-01`.
- Version: 0.1.0.
- Commons release: 0.39.0.
- Hours: 15.5.
- Checkpoint points: 15.
- Accepted FND-1 table: 374 rows, 29 fields.
- Accepted FND-1 SHA-256: `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a`.
- Modeling cohort: 374 rows, 34 fields.
- Modeling cohort SHA-256: `6556ed149e69589253ab58572b2f08535899ae12c3e84dc7bafc7da2ebe6f332`.
- Split: 224/75/75.
- Outcomes: 25/7/4.
- Baseline: 0.111607142857.
- Reference checks: 15937.

### Module 01 immutable artifacts

The checkpoint copies 17 Module 01 artifacts:

- module version;
- requirements;
- data and source specifications;
- aim-classification exercises;
- aim and method plan;
- estimand and target registry;
- feature-role contract;
- environment, reproduction, AI-use, and progression records;
- modeling cohort;
- split registry;
- baseline metrics;
- modeling checks; and
- build report.

### Module 02 identity

- ID: `oclc-fnd2-02`.
- Version: 0.1.0.
- Commons release: 0.40.0.
- Hours: 16.0.
- Checkpoint points: 10.
- Linear rows available: 111.
- Linear training rows: 69.
- Structural timing blanks: 263.
- Logistic training rows: 224.
- Logistic outcomes: 25.
- `LOG01` prior-acute odds ratio: 2.20423495.
- Regression checks: 24.
- Reference checks: 2025.

### Module 02 immutable artifacts

The checkpoint copies 27 Module 02 artifacts:

- module version;
- requirements, data spec, and source record;
- formula, reference, and interpretation registries;
- regression interpretation and R run record;
- environment, reproduction, AI-use, and progression records; and
- all 14 generated output files including the build report.

### Module 03 identity

- ID: `oclc-fnd2-03`.
- Version: 0.1.0.
- Commons release: 0.41.0.
- Hours: 16.5.
- Checkpoint points including H01: 15.
- Selected model: `ML01`.
- Locked threshold: 0.08513264.
- Test rows and outcomes: 75 and 4.
- Test TN/FP/FN/TP: 48/23/2/2.
- Prediction checks: 22.
- Reference checks: 4601.

### Module 03 immutable artifacts

The checkpoint copies 28 Module 03 artifacts:

- module version;
- requirements, data spec, source record, and model contract;
- prediction evaluation and accessibility records;
- environment, reproduction, AI-use, and progression records; and
- all 17 generated output files including two SVGs and the build report.

### Combined inventory

| Source | Immutable files |
|---|---:|
| Module 01 | 17 |
| Module 02 | 27 |
| Module 03 | 28 |
| Upstream subtotal | 72 |
| Checkpoint control | 6 |
| Manifest rows | 78 |

### Source and rights boundary

The modeling cohort is derived from Synthea synthetic records. No real patient data enter the checkpoint. Original Commons documentation and code follow repository license terms. Imported source terms remain with their source records.

## 8. Exact folder and file contract

### Root structure

```text
checkpoint-1/
  .gitattributes
  .gitignore
  README.md
  VERSION
  checkpoint-contract.json
  assessment.md
  validate_checkpoint.py
  cumulative-interpretation.md
  technical-defense.md
  component-score.csv
  gate-results.csv
  reviewer-record.md
  reproduction-record.md
  accessibility-review.md
  ai-use.md
  progression-decision.md
  release-manifest.csv
  modules/
    01-aims-reproducible-workspace/
    02-regression-interpretation/
    03-prediction-evaluation/
```

### Immutable namespace rule

Every upstream artifact is copied under its module directory with its original relative path. Module filenames are never flattened into the checkpoint root. This prevents collisions among `VERSION`, `source-record.yml`, `outputs/build-report.json`, and shared record names.

### Checkpoint control files

The six immutable control files are:

1. `.gitattributes`;
2. `.gitignore`;
3. `VERSION`;
4. `checkpoint-contract.json`;
5. `assessment.md`; and
6. `validate_checkpoint.py`.

### Editable cumulative records

The ten cumulative records are not included in the immutable manifest because learners and reviewers must complete them:

1. `README.md`;
2. `cumulative-interpretation.md`;
3. `technical-defense.md`;
4. `component-score.csv`;
5. `gate-results.csv`;
6. `reviewer-record.md`;
7. `reproduction-record.md`;
8. `accessibility-review.md`;
9. `ai-use.md`; and
10. `progression-decision.md`.

### Total file count

| Class | Files |
|---|---:|
| Immutable manifest members | 78 |
| Editable cumulative records | 10 |
| Generated release manifest | 1 |
| Total | 89 |

### Required encoding

Generated and supplied text uses UTF-8. Generated CSV files use LF line endings. Learner text uses plain ASCII dashes to prevent rendering and validator ambiguity.

### Prohibited package content

The assembled checkpoint must not contain:

- `.venv`;
- `__pycache__`;
- notebook checkpoints;
- local scratch outputs;
- absolute personal paths;
- credentials or tokens;
- private URLs;
- restricted data;
- real patient data; or
- files outside the explicit contract.

## 9. Assembly and immutable-manifest rules

### Inputs

The assembler receives:

- one Module 01 root;
- one Module 02 root;
- one Module 03 root;
- one empty target path; and
- either reference or learner mode.

### Pre-copy verification

Before creating the target, the assembler verifies:

- each root exists;
- every contracted file exists;
- every module `VERSION` is 0.1.0;
- the modeling-cohort hash is exact;
- the split-registry hash is exact;
- the Module 02 formula-registry hash is exact;
- the Module 03 test-prediction hash is exact;
- the Module 03 selected model and threshold are exact; and
- the target does not exist.

### Copy rules

- use binary-safe file copying;
- preserve module-relative paths;
- create parent directories explicitly;
- never modify a source module;
- never derive an analytic output;
- copy reference or learner cumulative records separately; and
- create the manifest only after all immutable members exist.

### Manifest schema

`release-manifest.csv` has:

| Field | Meaning |
|---|---|
| `relative_path` | safe path inside the checkpoint |
| `source_unit` | Module 01, Module 02, Module 03, or Checkpoint 1 |
| `source_version` | 0.1.0 |
| `bytes` | exact file size |
| `sha256` | exact file hash |

### Manifest ordering

Rows are sorted lexicographically by `relative_path`. Paths are unique, relative, and cannot contain `..`.

### Manifest scope

The manifest freezes all 72 upstream artifacts and 6 checkpoint control files. It does not freeze the ten records that must be completed or signed during checkpoint review.

### Existing-target refusal

Assembly to an existing directory always fails. The learner chooses a new target or intentionally moves the earlier attempt to a preserved archive.

### Change control

A changed immutable file invalidates manifest validation. The learner must return to the owning module or create a new checkpoint version. Editing the manifest to match an unauthorized change is an integrity failure.

### Two-build determinism

Two reference assemblies must produce identical manifest bytes and SHA-256 values. Editable reference records are also deterministic source files, so the complete assembled reference tree should match except for filesystem metadata not stored in Git.

## 10. Cumulative interpretation contract

### Required sections

`cumulative-interpretation.md` contains:

1. decision and supported use;
2. source and cohort identity;
3. prediction time and leakage boundary;
4. regression evidence and conditions;
5. model comparison and selection;
6. threshold decision;
7. untouched test evidence;
8. calibration and uncertainty;
9. subgroup limits;
10. reproducibility and accessibility;
11. supported and unsupported claims; and
12. Module 04 questions.

### Exact facts that must appear

- 374 modeling rows;
- 224/75/75 split;
- 25/7/4 outcomes;
- baseline 0.111607142857;
- 69 linear training rows within 111 timing rows;
- 263 structural blanks;
- `LOG01` prior-acute odds ratio 2.20423495;
- `ML01` selected on validation;
- `LEAK01` rejected for leakage;
- threshold 0.08513264;
- test ROC AUC 0.58802817;
- 48 TN, 23 FP, 2 FN, and 2 TP;
- four-outcome uncertainty;
- subgroup suppression; and
- teaching-only use.

### Required synthesis

The memo must connect the modules rather than list them. It explains how Module 01 decisions constrain Module 02 fitting and Module 03 evaluation, and why Module 04 must review validity before broader claims.

### Prohibited synthesis

The memo may not:

- declare clinical accuracy;
- call the odds ratio a causal effect;
- call `ML01` superior outside the frozen rule;
- imply stable calibration;
- describe suppressed subgroup evidence as fair or unfair;
- omit false positives or false negatives;
- erase pending R execution; or
- imply deployment readiness.

### Reference conclusion

The supported conclusion is:

> The exact synthetic teaching workflow is technically coherent enough to enter validity review with conditions. Its small held-out outcome count and exact error consequences prevent clinical or deployment claims.

## 11. Reproduction, accessibility, AI, privacy, and integrity

### Reproduction record

The cumulative reproduction record includes:

- operating system;
- Python and package versions;
- exact assembly command;
- exact validation command;
- module paths used;
- target path represented relatively where possible;
- manifest rows and hash;
- two-build comparison;
- existing-target refusal result;
- validator check count;
- differences; and
- accountable reproducer.

### Reproduction boundary

Checkpoint assembly reproduces packaging and manifest identity. It does not substitute for the module-level analytic self-checks, which remain preserved as immutable evidence.

### Accessibility review

The checkpoint accessibility record verifies:

- meaningful heading order;
- clear navigation to all three modules;
- exact CSV alternatives for plots;
- SVG title and description;
- no color-only exact meaning;
- readable tables;
- plain-language metric definitions;
- exact threshold and confusion counts in text; and
- no screenshot-only requirement.

### AI-use record

The checkpoint AI-use record distinguishes:

- module-level AI use already preserved;
- checkpoint assembly assistance;
- cumulative writing assistance;
- data shared;
- human verification;
- corrections; and
- accountable decision owner.

### AI may not decide

An agent may not own the final score, gate result, defense adequacy, reviewer identity, progression disposition, clinical meaning, or use boundary.

### Privacy gate

No real patient record, direct identifier, credential, token, private URL, local absolute path, or restricted source may appear anywhere in the checkpoint.

### Integrity protections

- manifest mismatch fails validation;
- unresolved prompts fail complete validation;
- missing artifact fails validation;
- changed module version fails validation;
- changed key fingerprint fails validation;
- incomplete gate record fails validation;
- arithmetic mismatch fails validation;
- inadequate defense fails validation; and
- nonprogression disposition cannot authorize Module 04.

## 12. Forty-point score contract

### Score schema

`component-score.csv` fields are:

- `criterion_id`;
- `component`;
- `course_points_available`;
- `points_earned`;
- `status`; and
- `evidence`.

### Required rows

Rows appear exactly in this order:

`A01`, `A02`, `A03`, `A04`, `R01`, `R02`, `P01`, `P02`, `P03`, `H01`.

### Point arithmetic

The available values are:

`4.00`, `4.00`, `3.00`, `4.00`, `4.50`, `5.50`, `4.50`, `4.50`, `3.50`, `2.50`.

They sum to exactly 40.00.

### Score statuses

Allowed statuses are:

- `pass`;
- `pass with conditions`;
- `revise`; and
- `refer`.

### Earned-point rules

- earned points cannot be negative;
- earned points cannot exceed available points;
- passing total is at least 32.00;
- every row must cite evidence paths;
- a failed gate blocks progression regardless of total; and
- a missing or malformed score blocks complete validation.

### Reference score

The reference answer key earns 40.00 technical points with conditions. The conditions reflect evidence limits and pending named reviews rather than an incorrect reference calculation.

### No rounding ambiguity

The validator uses decimal arithmetic, not binary floating-point addition, for the score.

## 13. Twenty-three-gate contract

### Gate schema

`gate-results.csv` fields are:

- `gate_id`;
- `gate`;
- `status`;
- `evidence`; and
- `reviewer_note`.

### Exact gates

| ID | Gate |
|---|---|
| G01 | Accepted FND-1 source, version, analytic-table fingerprint, and conditions |
| G02 | One-row-per-person 374-row grain |
| G03 | Prediction time at index stop |
| G04 | Every source field assigned a role |
| G05 | Post-index and outcome leakage blocked |
| G06 | Exact 224, 75, and 75 split rows |
| G07 | Exact 25, 7, and 4 positive outcomes |
| G08 | Test isolated from preprocessing, fitting, selection, and threshold choice |
| G09 | Training-prevalence baseline retained |
| G10 | Regression formulas and categorical references declared |
| G11 | Structural blanks not changed to zero |
| G12 | Odds, risks, and probabilities distinguished |
| G13 | No causal effect claim from associational regression |
| G14 | Preprocessing and model represented as one reproducible pipeline |
| G15 | Validation comparison and selection rule recorded before test |
| G16 | Calibration, discrimination, threshold, confusion, prevalence, and counts reported |
| G17 | Subgroup sample and outcome counts reported before metrics |
| G18 | Leaked critique model rejected |
| G19 | Four-positive test result visible in every decision summary |
| G20 | Source, transformation, reproduction, accessibility, and AI records complete |
| G21 | No restricted data or real clinical performance claim |
| G22 | Adequate defense |
| G23 | Explicit Module 04 progression |

### Status

Every gate status must be `pass` for progression. `not applicable`, blank, `partial`, or `waived` is not accepted.

### Evidence standard

Each gate cites at least one checkpoint-relative path. A reviewer note explains any condition or interpretation issue.

### Automatic return

The validator returns the checkpoint without scoring when:

- a required file is missing;
- the manifest changes;
- a module version changes;
- a key source or output fingerprint changes;
- a prompt remains;
- a score row or gate row is missing;
- score arithmetic fails;
- defense status is inadequate;
- an unallowed disposition appears; or
- Module 04 progression contradicts the disposition.

## 14. Technical-defense and reviewer contract

### Defense record

`technical-defense.md` includes:

- learner name or reference role;
- reviewer role;
- date;
- status: `adequate` or `inadequate`;
- 12 numbered questions;
- 12 substantive answers;
- cited evidence for each answer;
- follow-up questions;
- corrections made; and
- final reviewer note.

### Reference answer boundaries

The reference defense demonstrates exact reasoning but does not impersonate a real learner or named human reviewer. It is labeled as a technical answer key pending live defense.

### Reviewer record

`reviewer-record.md` lists:

- decision owner role;
- supporting reviewer roles;
- name or `pending named human review`;
- status;
- date when complete;
- scope reviewed;
- conditions;
- conflicts or referrals; and
- signature or repository identity when available.

### Required reviewer roles before alpha

- FND-2 faculty owner;
- clinical prediction and model-risk reviewer;
- biostatistical reviewer;
- clinical-informatics reviewer;
- clinician threshold-consequence reviewer;
- accessibility reviewer;
- privacy and security reviewer;
- responsible-AI reviewer; and
- independent instructor or reproducer.

### Runnable-candidate boundary

Technical validation may be complete while named human reviews remain pending. The release status remains runnable release candidate, not alpha, until those reviews are recorded.

### Disposition consistency

- `accept` and `accept with conditions` require adequate defense and all gates pass;
- `revise` and `refer` block Module 04;
- a condition must appear in both reviewer and progression records; and
- no reviewer can waive an immutable technical failure without a new version.

## 15. Progression and return contract

### Progression record

`progression-decision.md` contains:

- checkpoint ID and version;
- disposition;
- score;
- gate result;
- defense result;
- accepted module identities;
- exact Module 03 test counts;
- conditions;
- Module 04 permission; and
- return triggers.

### Reference progression

- Disposition: `accept with conditions`.
- Score: 40.00 of 40.00.
- Gates: 23 of 23 pass.
- Defense: adequate reference answer key; live learner defense pending.
- Module 04: permitted for the reference curriculum build.

### Conditions carried to Module 04

1. Preserve the 374-row cohort and source identity.
2. Preserve the 224/75/75 split and 25/7/4 outcomes.
3. Preserve the original locked test evidence.
4. Keep 48 TN, 23 FP, 2 FN, and 2 TP visible.
5. Keep the four-outcome uncertainty visible.
6. Treat prediction features as noncausal until validity review.
7. Keep structural blanks and selected-sample limits visible.
8. Preserve subgroup suppression and make no fairness claim.
9. Preserve the synthetic teaching-only boundary.
10. Complete named human reviews before alpha.

### Return to Module 01

Return for a changed aim, population, prediction time, outcome, horizon, field role, split, baseline, or source identity.

### Return to Module 02

Return for a changed regression formula, reference, transform, uncertainty method, diagnostic treatment, or quantity interpretation.

### Return to Module 03

Return for a changed feature set, pipeline, resampling, candidate, selection rule, threshold, metric, test-use policy, calibration method, subgroup definition, or suppression rule.

### Return to Checkpoint 1

Return for a changed cumulative score, gate evidence, defense result, reviewer record, disposition, or Module 04 handoff that does not change module evidence.

### Version rule

Any material change to immutable evidence requires a semantic-version decision at the owning module and checkpoint. A correction to an editable review record may remain within the same pre-alpha checkpoint version only when the immutable manifest is unchanged and the correction history is visible.

## 16. Runnable acceptance checks

### Assembler self-check

The assembler must prove:

- reference assembly succeeds;
- learner-mode assembly succeeds from copied module workspaces;
- 72 upstream artifacts are copied;
- 78 immutable files enter the manifest;
- 89 total files are created;
- manifest paths are sorted and unique;
- key hashes are exact;
- a second reference assembly has identical manifest bytes;
- an existing target is rejected; and
- no source module is modified.

### Validator self-check

The validator must prove:

- complete reference passes;
- learner starter passes structural checks;
- starter fails complete mode because prompts remain;
- a missing immutable artifact fails;
- a changed immutable byte fails;
- a changed score fails;
- a failed gate blocks progression;
- an inadequate defense fails;
- an invalid disposition fails; and
- Module 04 permission matches disposition.

### Reference validation checks

The validator checks:

- 89 required files;
- checkpoint version and contract;
- manifest schema, count, sorting, uniqueness, safety, bytes, and hashes;
- module versions;
- key source and output hashes;
- split and outcome counts;
- baseline;
- regression structural blanks and odds quantity;
- selected model and threshold;
- test confusion and metrics;
- leaked-model rejection;
- subgroup suppression;
- 10 score rows and 40-point arithmetic;
- 23 passing gates;
- 12 defense answers;
- cumulative claim boundaries;
- record completeness;
- disposition and progression consistency;
- plain ASCII punctuation;
- personal-path absence; and
- synthetic-data boundary.

### Acceptance commands

```powershell
python courses/modeling-inference-reproducible-analytics/checkpoints/01-modeling-readiness-release/assemble_checkpoint.py --self-check
python courses/modeling-inference-reproducible-analytics/checkpoints/01-modeling-readiness-release/validate_checkpoint.py --self-check
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/check-curriculum-specs.ps1
```

### Technical acceptance criteria

- checkpoint version 0.1.0;
- Commons version 0.42.0;
- 17 specification sections;
- 72 upstream artifacts;
- 78 manifest rows;
- 89 assembled files;
- 40.00 available points;
- at least 32.00 passing points;
- 23 gates;
- 12 defense questions;
- builder self-check pass;
- validator self-check pass;
- repository-wide gate pass;
- semantic-version trail complete;
- commit complete; and
- push complete.

### Failure messages

Failure messages name the exact missing file, changed path, arithmetic defect, unresolved prompt, gate, defense field, or disposition inconsistency. The validator does not silently repair a submission.

## 17. Release status, known issues, human review, and resume record

### Semantic-version decision

Checkpoint 1 introduces a new cumulative release package and advances the Commons minor version from 0.41.0 to 0.42.0. The checkpoint begins at 0.1.0. Module versions remain unchanged because their immutable evidence is copied, not modified.

### Reference package status

The reference package is a runnable release candidate when all automated checks pass. It is not alpha until named reviewers complete the required human review.

### Measured runnable release

- Module artifacts: 72.
- Checkpoint control artifacts: 6.
- Immutable manifest rows: 78.
- Assembled files: 89.
- Manifest bytes: 11241.
- Manifest SHA-256: `b3760f43e5852ba90150000a4c807bc3aadfedcc688b40c4f16017dc253ca836`.
- Complete reference validation: 500 checks.
- Learner starter validation: 465 checks.
- Existing-target, incomplete-package, missing-immutable, invalid-score, and failed-gate rejection: pass.

### Known material limitations

1. All model data are synthetic.
2. The test partition has only four positive outcomes.
3. The locked threshold yields 23 false positives and 2 false negatives.
4. Calibration evidence is unstable.
5. Subgroup evidence is sparse and partly suppressed.
6. The threshold consequence is an educational fixture.
7. Module 02 paired R execution remains pending on a named R environment.
8. Named clinical, statistical, accessibility, privacy, responsible-AI, and teaching reviews remain pending.
9. No external or prospective validation has occurred.
10. No clinical, operational, or deployment claim is permitted.

### Required human reviews

| Role | Required before alpha | Primary scope |
|---|---|---|
| FND-2 faculty owner | yes | outcomes, assessment, progression |
| Clinical prediction and model-risk reviewer | yes | development and use boundary |
| Biostatistician | yes | regression, metrics, uncertainty |
| Clinical informatician | yes | timing and field meaning |
| Clinician | yes | threshold consequences |
| Accessibility reviewer | yes | tables, SVGs, navigation |
| Privacy and security reviewer | yes | data and release safety |
| Responsible-AI reviewer | yes | automation and accountability |
| Independent instructor/reproducer | yes | teachability and reproduction |

### Reference handoff

The checkpoint passes the reference curriculum to Module 04 with conditions. Module 04 receives the immutable manifest, cumulative interpretation, technical-defense answer key, score, gates, reviewer conditions, and progression decision. It must review adjustment, missingness, selection, repeated structure, and time-to-event boundaries without changing the original locked test result.

### Contributors

- Shuhan He: Commons sponsor and curriculum direction.
- OpenAI Codex: checkpoint specification, assembly, reference records, and validation.

### Resume record

FND-2 Checkpoint 1 is complete at Commons 0.42.0 when the 17-section specification, 0.1.0 package, 78-row immutable manifest, 40-point score, 23 gates, 12-question defense, reference and starter validation, full curriculum gate, commit, and push all pass.

Resume with FND-2 Module 04 only. Read the accepted checkpoint specification, package release, cumulative progression decision, Module 01 through 03 release records, course specification, master architecture, and build ledger. Do not reopen the cohort, split, formulas, selected model, threshold, or test evidence without a documented return and semantic-version decision.
