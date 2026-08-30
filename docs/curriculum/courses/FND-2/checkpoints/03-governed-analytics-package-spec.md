# FND-2 Final checkpoint: Governed analytics package and model-use decision

## 1. Checkpoint identity and place in the course

- Checkpoint ID: `oclc-fnd2-cp3`.
- Checkpoint version: 0.1.0.
- Commons release target: 0.48.0.
- Course: FND-2, Modeling, Inference, and Reproducible Analytics.
- Due: official last day of the assigned MGH Institute half-term.
- Course weight: 35 percent, or 35 course points.
- Cumulative learner work: 112.5 hours.
- Required input: accepted or conditionally accepted Module 07 governed candidate version 0.1.0.
- Proposed annotated tag: `fnd2-governed-candidate-v0.1.0`.
- Status: runnable release candidate.

The official calendar controls the submission date:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The 7.5-week phrase is a planning model. The checkpoint is due on the published last day of the assigned half-term, not on a date inferred by adding 7.5 weeks.

The checkpoint freezes the complete 168-file Module 07 candidate, verifies the final defense and release decision, and closes FND-2. It does not fit another model, rerun model selection, refresh a public source, add another 35 points, or treat an accepted package as deployment permission. The Module 07 score is the draft for this same source assessment component; the final checkpoint score is the course record.

## 2. Decision, audience, and review question

### Decision owner

The final decision owner is a clinical analytics model-risk lead. The review panel includes:

- FND-2 faculty owner;
- biostatistical methods reviewer;
- clinical informatics reviewer;
- model evaluation reviewer;
- forecasting reviewer;
- accessibility reviewer;
- privacy and data-governance reviewer;
- responsible-AI reviewer; and
- independent reproducer.

One person may cover more than one role when expertise and independence are recorded. The learner cannot be the final decision owner or independent reproducer.

### Receiving audience

The receiver is an applied-course instructor, analyst, clinician, or governance reviewer who did not build the candidate. They need one exact package with traceable source, model and forecast evidence, limits, access routes, monitoring conditions, and a defensible use recommendation.

### Final review questions

1. Is the governed analytics package technically correct, reproducible, accessible, and honestly bounded?
2. What use, if any, may the fitted model support?

These are separate decisions. An accepted package can still receive `teaching use only`.

### Allowed package dispositions

- `accept`;
- `accept with conditions`;
- `revise`; or
- `refer` for rights, privacy, integrity, clinical meaning, accessibility, model risk, responsible AI, or governance review.

Only `accept` and `accept with conditions` pass the final package gate. Neither authorizes deployment, clinical action, real-patient use, or a claim of benefit.

### Allowed model-use recommendations

- `teaching use only`;
- `silent prospective validation only`;
- `revise before further validation`; or
- `stop model use`.

The reference package disposition is `accept with conditions`. The separate reference model-use recommendation is `teaching use only`.

## 3. Course-point preservation and final score map

The checkpoint preserves the source curriculum's 35-percent final analytics-package assessment exactly once.

| ID | Criterion | Course points |
|---|---|---:|
| M01 | Aim, target, prediction time, model design, and baseline | 5.00 |
| R01 | Reproducible pipeline, environment, manifest, tests, and exact refit | 6.00 |
| E01 | Evaluation, calibration, thresholds, subgroup evidence, and failure analysis | 7.00 |
| V01 | Validity, uncertainty, data limits, forecast limits, and claim boundary | 5.00 |
| G01 | Model card, monitoring, drift, retraining, rollback, stop, retirement, and use decision | 6.00 |
| H01 | Responsible-agent evidence, accessible handoff, defense, reviewers, and disposition | 6.00 |
| Total |  | 35.00 |

Passing requires at least 28.00 points, every noncompensable gate, an adequate defense, `accept` or `accept with conditions`, and an explicit model-use recommendation.

The final score does not reward apparent model performance by itself. It rewards a correct decision contract, reproducible evidence, honest evaluation, validity limits, governance, and accountable communication.

## 4. Competencies and assessable outcomes

By completing the checkpoint, the learner can:

1. identify the exact repository, full commit, semantic version, release notes, and proposed tag;
2. prove that the reviewed candidate contains exactly 168 files;
3. freeze every candidate file in a 168-row manifest with bytes and SHA-256;
4. identify the exact accepted versions of Checkpoints 1 and 2 and Module 07;
5. trace every final claim to an evidence path and owner;
6. defend the analytic aim, target, prediction time, horizon, and one-row-per-person grain;
7. explain the 224/75/75 temporal split and 25/7/4 outcome counts;
8. distinguish allowed features from prohibited post-index or outcome fields;
9. compare the constant baseline and candidate on identical declared rows;
10. explain discrimination, calibration, threshold, confusion counts, prevalence, and uncertainty separately;
11. state why four positive test outcomes and five suppressed subgroup rows sharply limit model use;
12. defend the structured DAG, selection conditions, missingness sensitivity, longitudinal boundaries, and specialist referrals;
13. defend the public forecast target, time-ordered folds, benchmarks, failures, residuals, and reporting limits;
14. show that 18 accepted tests pass and ten seeded failures reject as intended;
15. distinguish agent output from independently verified evidence and human accountability;
16. explain the model card, ten monitoring signals, retraining rules, rollback, stop, and retirement;
17. provide equivalent access routes for tables, displays, and DAGs;
18. complete a clean reproduction and exact comparison;
19. answer all 15 defense questions without relying on prepared text;
20. separate package disposition from model-use recommendation; and
21. defend conditions, owners, due points, stop triggers, and the final release decision.

## 5. Ownership and out-of-scope boundaries

### Final checkpoint owns

- whole-candidate freeze and 168-row candidate manifest;
- accepted-release identity check for Checkpoints 1 and 2 and Module 07;
- final 35-point score;
- 27 noncompensable gate results;
- 15-question defense record;
- named reviewer and independence record;
- final clean-reproduction record;
- source, rights, accessibility, and AI-accountability audit;
- conditions and owners;
- package disposition;
- separate model-use recommendation;
- proposed annotated-tag record; and
- final release-acceptance statement.

### Module 07 ownership retained

Module 07 owns the governed candidate, model card, evidence appendix, subgroup review, monitoring plan, lifecycle rules, release notes, AI record, human sign-off, handoff brief, candidate score, gates, and progression decision. The final checkpoint freezes and adjudicates these records; it does not silently edit them.

### Upstream ownership retained

Modules 01 through 06 and Checkpoints 1 and 2 retain ownership of model-ready data, splits, features, formulas, fitted artifacts, evaluation, validity, forecast, testing, and agent-accountability evidence.

### Out of scope

- fitting, selecting, tuning, or recalibrating a model;
- changing the cohort, target, prediction time, split, feature roles, threshold, or evaluation rows;
- refreshing or replacing the public forecast source;
- changing an accepted upstream artifact without a new version and renewed review;
- deployment, live integration, clinical action, or silent use in care;
- claims of clinical efficacy, causal effect, fairness certification, stable process, or real-population performance;
- patient, workplace, restricted, secret, credential, key, or identity-expanding data; and
- creating the annotated tag before named human acceptance of the exact reviewed commit.

## 6. Final workflow, workload, and defense

The checkpoint uses work already included in Module 07's 16 hours:

1. validate the complete Module 07 candidate;
2. assemble it into a new final target without changing candidate bytes;
3. inspect the generated 168-row candidate manifest;
4. compare the manifest to the exact reviewed commit;
5. confirm accepted Checkpoint 1, Checkpoint 2, and Module 07 release identities;
6. complete the final score, 27 gates, reviewer, reproduction, audit, conditions, and decision records;
7. deliver an accessible technical handoff;
8. answer all 15 final defense questions;
9. record package disposition and model-use recommendation separately;
10. validate the complete final package;
11. commit the exact reviewed state; and
12. create the annotated tag only after named human authorization.

### Required handoff topics

1. decision, analytic aim, target, prediction time, and horizon;
2. row grain, cohort, split, feature boundary, and outcome counts;
3. baseline, selected model, threshold, test evidence, and uncertainty;
4. calibration, subgroup support, and most important failure condition;
5. validity, missingness, longitudinal, and causal-claim limits;
6. public forecast source, validation design, error, and reporting limits;
7. accepted tests, seeded failures, agent trace, and independent audit;
8. model card and intended, prohibited, and unsupported use;
9. monitoring, retraining, rollback, stop, and retirement; and
10. package disposition, model-use recommendation, conditions, owners, and tag status.

## 7. Accepted input and immutable facts

### Release identities

| Unit | Version | Accepted release SHA-256 |
|---|---:|---|
| Checkpoint 1, modeling-readiness release | 0.1.0 | `03c147d2e75cd446a43b9d56e49495df69af90d42d2b14ad4d860aea9d67239f` |
| Checkpoint 2, validity/forecast/testing release | 0.1.0 | `b58316081496f42d473b823fac88ed8e6c981e47afb11d0c4856c9f39627d761` |
| Module 07, governed candidate | 0.1.0 | `a2fccdcd096a066337f1de856cb9610f6b389db15c90dff1627af1cbf30ac96e` |

The accepted Module 07 source commit is `31c69e9152d797f49e5d8968eb1dd5ea53090568`.

### Candidate identity

| Item | Accepted fact |
|---|---|
| candidate files | 168 |
| immutable Module 07 manifest rows | 143 |
| Module 07 manifest bytes | 27,316 |
| Module 07 manifest SHA-256 | `ab2537e278ea549b8152434df0a21438394d28caa6031b03e9a570a27db07c1b` |
| Checkpoint 2 files | 130 |
| Checkpoint 2 manifest rows | 117 |
| Checkpoint 2 manifest SHA-256 | `16733c55e8a9930f4903006c81e5fb1acb9e75386507f1aa46867daac89f6ccc` |
| reference package disposition | `accept with conditions` |
| reference model-use recommendation | `teaching use only` |

### Modeling and evaluation facts

- Modeling rows: 374, one row per synthetic person and index encounter.
- Temporal split: 224 training, 75 validation, 75 test.
- Positive outcomes: 25 training, 7 validation, 4 test.
- Training-prevalence baseline: 0.111607142857.
- Selected candidate: ML01.
- Locked threshold: 0.08513264.
- Test ROC AUC: 0.58802817, stratified bootstrap interval 0.26760563 to 0.91549296.
- Test Brier score: 0.05097579.
- Test confusion: 48 true negatives, 23 false positives, 2 false negatives, 2 true positives.
- Subgroup evidence: ten rows, five suppressed for inadequate support.

### Validity, forecast, and accountability facts

- Selection-timing evidence has 111 rows and 263 structural blanks.
- The public forecast teaching series has 94 rows.
- The accepted damped-Holt candidate MAE is 14.99587157.
- Eighteen accepted contract tests pass.
- Ten seeded failures reject for the intended reason.
- Three material results have independent checks.
- Four agent-assisted claims have adjudication records.
- Ten simulated monitoring signals have explicit denominators, windows, owners, triggers, actions, and stop conditions.

### Rights and claim boundary

The patient-level modeling source is synthetic. The forecast source is public CDC NHSN jurisdiction-week data. The package supports technical education and method review only. It does not establish performance in a real clinical population or authorize clinical use.

CDC source:

https://data.cdc.gov/Public-Health-Surveillance/Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/rhwp-grxi

## 8. Exact final package and freeze contract

The final package preserves the entire Module 07 candidate at unchanged paths and adds only `final-review/`.

```text
fnd2-governed-analytics-final/
  [all 168 Module 07 candidate files at unchanged paths]
  final-review/
    CHECKPOINT-VERSION
    checkpoint2-release.json
    module07-release.json
    candidate-manifest.csv
    submission-record.md
    final-score.csv
    gate-results.csv
    final-defense.md
    reviewer-record.md
    final-reproduction.md
    conditions-register.csv
    final-audit.md
    final-decision.md
    release-acceptance.md
```

The package contains exactly 182 files. `candidate-manifest.csv` has exactly 168 rows, one for every Module 07 candidate file before final-review records are added.

Each manifest row records:

- relative path;
- byte count;
- SHA-256; and
- source role.

The copied `checkpoint2-release.json` and `module07-release.json` preserve accepted release identities that are not themselves inside the 168-file candidate. The Checkpoint 1 release remains at its accepted nested candidate path.

The final-review records are reviewer-owned and are not part of the candidate manifest. After disposition, the exact 182-file Git state is identified by the reviewed commit. The proposed annotated tag remains uncreated until named human authorization.

The deterministic 168-row candidate manifest is 27,695 bytes with SHA-256 `4fd5b52c94aa038a10faf07372847c5229a394fca0776f8e13f4fc42166dd641`.

## 9. Assembly, manifest, and change-control rules

### Protected assembly

The assembler accepts one complete Module 07 candidate and one new target. It runs the Module 07 validator in complete mode before copying. It refuses a target that already exists, a target inside the candidate, or an incomplete candidate.

### Candidate freeze

The assembler:

1. validates the exact 168-file candidate;
2. requires the 143-row Module 07 manifest fingerprint;
3. enumerates all 168 files at safe relative paths;
4. records bytes and SHA-256 for every candidate file;
5. copies candidate bytes unchanged;
6. writes a sorted 168-row candidate manifest;
7. copies the exact Module 07 release record;
8. adds checkpoint version and reviewer templates or reference records; and
9. reports exactly 182 files.

### Change control

Any change to one of the 168 candidate files invalidates the candidate manifest and returns the work to Module 07 for a semantic-version decision. A final-review correction requires renewed validation. A change after defense requires renewed defense when it can affect evidence, score, gates, conditions, disposition, model use, or tag authorization.

### Tag rule

The proposed annotated tag is `fnd2-governed-candidate-v0.1.0`. It must point to the exact reviewed commit after an allowed package disposition and named human authorization. A lightweight, early, mismatched, or automatically created tag fails the gate. The reference package records the proposed tag and exact candidate source commit but does not create the tag.

## 10. Final technical evidence contract

The final review verifies:

- exact repository, full commit, semantic versions, change log, release notes, and proposed tag;
- exact accepted Checkpoint 1, Checkpoint 2, and Module 07 identities;
- model-ready data, row grain, cohort, prediction time, split, feature roles, and label contract;
- formulas, pipelines, model parameters, or deterministic refit contract;
- baseline, validation, test, calibration, threshold, subgroup, uncertainty, and failure evidence;
- DAG, validity threats, missingness sensitivity, longitudinal boundaries, and referrals;
- forecast target, source, folds, benchmarks, predictions, errors, residuals, and coverage limits;
- accepted tests, seeded failures, trace log, material AI audit, and human sign-off;
- model card and intended, prohibited, and unsupported use;
- subgroup and equity counts, missingness, uncertainty, and suppressed comparisons;
- ten monitoring signals and full lifecycle rules;
- source, rights, transformation, access, reproduction, and reviewer records;
- accessible handoff brief, exact evidence appendix, and defense responses;
- final score, gates, conditions, disposition, and model-use recommendation; and
- absence of prohibited files, personal paths, secrets, credentials, and hidden dependencies.

Automation verifies structure, fingerprints, row counts, arithmetic, required fields, and decision consistency. Human reviewers decide whether explanations, clinical meaning, access, accountability, conditions, and the final recommendation are credible.

## 11. Defense, accessibility, privacy, and AI gates

### Defense gate

The learner must explain the package without reading a prepared script, answer all 15 questions accurately, distinguish evidence from inference, identify fragile evidence, and separate package quality from model-use permission.

### Accessibility gate

- Defense materials are available in accessible digital form before review.
- Tables have headers and logical reading order.
- Displays and DAGs retain exact tables or structured text alternatives.
- Color is never the only carrier of status or meaning.
- The handoff identifies equivalent access routes.
- An equivalent written or recorded defense route may be used without lowering the technical standard.

### Privacy and rights gate

Only the registered synthetic and public sources are allowed. No patient, workplace, restricted, secret, credential, key, identity-expanding, or hidden local file may enter the release or an external AI tool.

### Responsible-AI gate

The trace must disclose each material agent-assisted step. Every material claim needs an independent method, exact evidence, result, retained action or correction, and named human owner. Repeating the task to the same model is not independent verification. Agent output is never evidence by itself.

## 12. Reviewer roles, independence, and conditions

| Role | Required decision |
|---|---|
| FND-2 faculty owner | objectives, workload, score, defense, and course completion |
| Biostatistical methods | estimand, regression interpretation, uncertainty, and validity limits |
| Clinical informatics | grain, prediction time, features, workflow meaning, and prohibited use |
| Model evaluation | baseline, splits, leakage, calibration, threshold, subgroup evidence, and failure analysis |
| Forecasting | target, temporal folds, benchmarks, errors, residuals, and coverage limits |
| Accessibility | exact tables, structured alternatives, handoff, and defense access |
| Privacy and data governance | source rights, excluded data classes, prompts, retention, and allowed use |
| Responsible AI | trace, material audit, independent evidence, and human accountability |
| Independent reproducer | clean checkout, environment, ordered commands, exact comparison, and hidden dependencies |

Every condition names:

- condition ID;
- source;
- status;
- condition;
- owner;
- due point;
- evidence required;
- verifier; and
- escalation trigger.

A condition cannot waive changed immutable evidence, restricted-data exposure, test contamination, a failed accessibility route, an incomplete material AI audit, an inadequate defense, or absent model-use limits.

## 13. Final-review record contracts

### Submission record

Records repository URL, full candidate source commit, checkpoint and Module 07 versions, all three release fingerprints, candidate file and manifest counts, final-manifest fingerprint, official due-date rule, proposed tag, validator result, and submitter.

### Final score

Six rows preserve the exact 35-point rubric. Scores use decimals, remain within each criterion, total at least 28, cite exact evidence, and record status.

### Gate results

Twenty-seven rows record gate ID, gate, result, evidence, reviewer, and condition ID. Results are `pass`, `pass with condition`, or `fail`. A failed gate cannot receive an accepting disposition.

### Final defense

Contains one direct answer to each of the 15 required questions plus an overall status of `adequate` or `inadequate`. The defense must identify exact evidence and limits rather than repeat the model card.

### Reviewer record

Records all nine required roles, reviewer identity or explicit pending condition, independence, date, evidence reviewed, decision, and acknowledgment. Reference construction may show role-based program-review placeholders but cannot represent a completed learner defense or final live approval.

### Final reproduction

Records clean-checkout identity, operating system, Python, ordered commands, exact output comparisons, candidate manifest result, nested validator result, independent reproducer, date, and unresolved platform conditions.

### Conditions register

Records every carried or newly imposed condition with owner, due point, evidence, verifier, status, and escalation trigger.

### Final audit

Combines source and rights confirmation, transformation trace, prohibited-data scan, accessibility routes, agent-use trace, independent material checks, human-accountability scope, and evidence-index coverage.

### Final decision

Records total score, gate result, defense result, package disposition, model-use recommendation, conditions, tag status, and completion decision on separate machine-readable lines.

### Release acceptance

States what the next course or reviewer receives, permitted use, prohibited use, conditions, support owner, change-notification rule, rollback or stop triggers, and whether the proposed tag is authorized.

## 14. Learner and reviewer workflows

### Learner workflow

1. Freeze the complete Module 07 candidate at a full commit.
2. Assemble the final checkpoint into a new target.
3. Verify the 168-row candidate manifest.
4. Complete submission, reproduction, audit, and conditions records.
5. Propose scores and gate evidence without changing weights.
6. Deliver the accessible handoff and answer 15 questions.
7. Respond to findings in the owning final or upstream record.
8. Rerun complete validation after every correction.
9. Obtain package disposition and model-use recommendation separately.
10. Commit the exact reviewed 182-file state.
11. Create the annotated tag only when named human authorization is recorded.

### Reviewer workflow

1. Confirm the official due date and exact candidate identity.
2. Scan for prohibited files, data classes, paths, secrets, and hidden dependencies.
3. validate Module 07 and the 168-row final freeze.
4. confirm all three accepted release fingerprints.
5. trace modeling, evaluation, validity, forecast, test, access, and accountability evidence.
6. review clean reproduction and exact comparison.
7. conduct the defense and record adequacy.
8. complete all 27 gates and six score rows.
9. record conditions and owners.
10. set package disposition and model-use recommendation separately.
11. decide tag authorization.
12. rerun final validation against the exact reviewed state.

## 15. Pass conditions and noncompensable gates

### Numeric and decision rule

Passing requires:

- at least 28.00 of 35.00 points;
- all 27 gates passed or passed with an allowed condition;
- no failed gate;
- an `adequate` defense;
- package disposition `accept` or `accept with conditions`; and
- an explicit allowed model-use recommendation.

### Twenty-seven noncompensable gates

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

### Automatic return

The package returns for revision when any gate fails, the candidate bytes change, the score is below 28, the defense is inadequate, reviewer ownership is incomplete, a decision record is inconsistent, or the tag was created early or points to another commit.

## 16. Final defense questions and evidence expectations

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

An adequate answer identifies an exact evidence path or registered fact, explains the practical meaning, and states the decision limit. Memorized definitions without package-specific evidence are inadequate.

## 17. Validation, reference status, and release rule

### Automated validation

The validator checks:

- exact 182-file tree and safe relative paths;
- exact 168-row final candidate manifest;
- candidate byte and SHA-256 equality;
- exact 143-row Module 07 manifest and accepted fingerprint;
- complete Module 07 validation after reconstructing the candidate without final-review files;
- exact Checkpoint 1, Checkpoint 2, and Module 07 release identities;
- score arithmetic and 28-point minimum;
- all 27 gates and condition ownership;
- all 15 defense answers and adequate status;
- all nine reviewer roles;
- complete reproduction and final audit records;
- separate and consistent package and model-use decisions;
- exact proposed tag and `proposed - not created` reference status;
- absence of placeholders in complete mode;
- plain ASCII dashes and portable paths; and
- reference, learner-starter, changed evidence, score, gate, tag, and decision failure cases.

### Reference status

The reference package is a curriculum-construction example. It records:

- package disposition: `accept with conditions`;
- model-use recommendation: `teaching use only`;
- proposed tag: `fnd2-governed-candidate-v0.1.0`;
- proposed tag target: `31c69e9152d797f49e5d8968eb1dd5ea53090568`;
- tag status: `proposed - not created`; and
- human sign-off scope: curriculum construction only.

Named program review, a live learner defense, actual learner and reviewer acknowledgment, independent clean reproduction by a person, and final tag authorization remain pending before alpha.

Complete reference validation passes 947 checks. Learner-starter validation passes 901 checks. Self-checks also reject unfinished records, changed candidate evidence, invalid scoring, a failed gate, an early tag, and inconsistent final decisions.

### Release rule

The annotated tag may be created only after an allowed package disposition, complete named human approval, and verification that the tag points to the exact reviewed commit. Package acceptance does not imply deployment permission. The reference model remains for teaching only.
