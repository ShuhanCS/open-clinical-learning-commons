# FND-2 Checkpoint 2: Validity, forecast, testing, and agent-accountability release

## 1. Checkpoint identity and place in the course

### Release identity

| Field | Value |
|---|---|
| Checkpoint ID | `oclc-fnd2-cp2` |
| Version | `0.1.0` |
| Commons release | `0.46.0` |
| Course | FND-2: Modeling, Inference, and Reproducible Analytics |
| Due | End of instructional Week 6 |
| Cumulative learner time | 96.5 hours |
| Course points | 25.00 |
| Minimum points | 20.00 |
| Required tag | `fnd2-checkpoint2-v0.1.0` |
| Progression target | Module 07 |

### Purpose

Checkpoint 2 is the Week 6 decision package. It asks whether evidence from validity analysis, longitudinal and survival reasoning, public-data forecasting, contract testing, failure testing, and agent accountability is coherent enough to enter final governance packaging. It does not reward a high-performing model in isolation. It rewards a defensible evidence chain whose limits remain attached.

### Cumulative boundary

The checkpoint preserves the accepted Checkpoint 1 identity and conditions, then adds accepted evidence from Modules 04 through 06. It does not recompute or silently repair an upstream artifact. A changed upstream artifact returns to its owner and receives a new version before reassembly.

### Required starting state

- Checkpoint 1 version `0.1.0` has disposition `accept with conditions`.
- The 374-row modeling cohort and 224/75/75 split remain unchanged.
- Module 04 version `0.1.0` has a bounded validity disposition.
- Module 05 version `0.1.0` has an accepted public-source forecast with declared use limits.
- Module 06 version `0.1.0` has 18 accepted tests, ten correctly rejected seeded failures, three independent checks, and four adjudicated agent claims.

### Required ending state

The learner submits one assembled, validated package containing 117 immutable manifest members and 12 completed checkpoint records. The package receives a 25-point score, all 25 noncompensable gates, a 12-question technical defense, named human accountability, and one explicit progression disposition.

## 2. Decision, owners, audience, and review question

### Decision owner

The accountable decision owner is the biostatistical validity and responsible-modeling panel. Before alpha, the panel must include named biostatistical-validity, causal-inference, longitudinal or survival, forecasting, responsible-AI, clinical-informatics, accessibility, privacy or security, clinician, and independent-instructor reviewers. One person may cover more than one role only when competence and conflicts are recorded.

### Primary audience

The package is written for a reviewer deciding whether the learner can preserve a modeling claim through validity threats, temporal validation, failure testing, and human accountability. It is not a portfolio brochure, clinical recommendation, or deployment approval.

### Review question

May the accepted prediction, validity, and forecast evidence enter final governance packaging with threats, failure tests, AI trace, source identity, use limits, and human ownership intact?

### Allowed dispositions

- `accept`
- `accept with conditions`
- `revise`
- `refer`

Only `accept` and `accept with conditions` permit Module 07. A numeric passing score never overrides a failed gate, inadequate defense, missing human sign-off, or changed immutable artifact.

### Reference disposition

The runnable teaching reference is `accept with conditions`. It demonstrates the complete technical contract, while live learner defense and named program review remain required for a real course decision.

### Acceptance does not mean

Acceptance does not establish a causal treatment effect in practice, a reliable single-hospital forecast, a staffing or capacity tool, clinical safety, fairness, generalizability, regulatory compliance, or deployment readiness.

## 3. Component map and weight preservation

### Source weights

Module 04 contributes 15.00 course points. Module 05 contributes 10.00 course points. Module 06 is a required gate and contributes no additional course points. This preserves the course specification exactly.

### Twenty-five-point map

| ID | Criterion | Points |
|---|---|---:|
| V01 | Aim, estimand, DAG, variable roles, and causal boundary | 4.00 |
| V02 | Confounding, overlap, balance, selection, and adjustment | 3.00 |
| V03 | Missingness, sensitivity, repeated measures, survival, and referral | 5.00 |
| F01 | Forecast aim, horizon, cutoff, folds, source, and benchmarks | 4.00 |
| F02 | Candidate, errors, residuals, coverage, and use limit | 4.00 |
| T01 | Accepted data, model, forecast, and documentation test coverage | 2.00 |
| AI01 | Seeded failures, trace, adjudication, independent checks, and human sign-off | 2.00 |
| H01 | Accessible cumulative memo, defense, conditions, and progression | 1.00 |
| Total |  | 25.00 |

### Numeric pass threshold

The numeric minimum is 20.00 of 25.00. All 25 gates must also pass. Point compensation cannot cure a failed gate.

### Feedback milestones

Checkpoint 1 at Week 3, Checkpoint 2 at Week 6, and the final release at Week 7.5 are formal feedback and disposition moments. Each produces a concrete package, score, conditions register, and next-module decision.

## 4. Competencies and assessable outcomes

At Checkpoint 2, the learner can:

1. distinguish descriptive, predictive, causal, longitudinal, survival, and forecasting aims;
2. translate an estimand into a visual and structured DAG with explicit variable roles;
3. explain confounding, mediation, collision, post-outcome variables, and selection by purpose;
4. inspect overlap and balance without claiming that adjustment removes all bias;
5. preserve structural blanks and state missingness assumptions;
6. compare sensitivity analyses on the same target and population;
7. recognize dependence, clustering, repeated measures, and censoring;
8. define a forecast target, unit, horizon, cutoff, folds, benchmarks, and error measures;
9. keep all future observations out of each forecast fit;
10. interpret forecast errors, residual checks, reporting coverage, and failure periods;
11. test data, model, forecast, and documentation contracts;
12. demonstrate that ten known failures reject for their intended reasons;
13. distinguish an agent-generated claim from independent evidence;
14. document prompt, trace, critique, correction, adjudication, and human ownership;
15. defend source identity, transformation, reproduction, access, privacy, and use limits; and
16. make a bounded progression recommendation that preserves every unresolved condition.

### Minimum defense standard

An adequate defense names the target, population, time boundary, assumptions, denominators, failure modes, and use limits without reading a prepared paragraph as a substitute for reasoning. The reviewer may ask for a row-level or artifact-level demonstration.

### Unsupported defense

A defense is inadequate when it conflates prediction and causation, treats missing values as zero, uses random cross-validation for the forecast, hides a weak fold, treats an agent assertion as evidence, omits the source fingerprint, or expands the package into clinical or operational use.

## 5. Concept ownership and out-of-scope boundaries

### Checkpoint-owned integration

Checkpoint 2 owns reconciliation across the accepted evidence. It owns the cumulative interpretation, package manifest, score, gates, technical defense, reviewer record, conditions register, human sign-off, and Module 07 progression decision.

### Module 04 ownership retained

Module 04 owns analytic-aim classification, estimand framing, causal-claim screening, DAG structure, variable roles, overlap, balance, adjustment readings, selection, missingness, sensitivity, repeated measures, mixed-model interpretation, survival, censoring, and specialist referral.

### Module 05 ownership retained

Module 05 owns the CDC NHSN source release, Massachusetts series, target, temporal folds, naive benchmarks, damped-Holt candidate, ARIMA recognition example, predictions, errors, residual readings, reporting-coverage context, accessible forecast display, and use boundary.

### Module 06 ownership retained

Module 06 owns the accepted contract-test suite, failure mutations, prompt constraints, trace, critique, claim adjudication, independent verification, prohibited-data classes, and learner/reviewer sign-off requirement.

### Checkpoint 1 ownership retained

Checkpoint 1 owns the modeling cohort, split, outcome counts, prediction time, regression formulas, selected model, locked threshold, untouched test evidence, and prior conditions. Checkpoint 2 may cite but not revise them.

### Out of scope

- collecting identifiable patient data;
- inferring individual or hospital performance from jurisdiction aggregates;
- selecting a treatment for a patient;
- staffing, capacity, or procurement decisions;
- production model training, monitoring, or deployment;
- fairness, safety, transportability, or causal-effect claims not supported by the evidence;
- treating missingness labels as verified real-world mechanisms;
- replacing accountable human review with an agent summary; and
- silently changing an upstream version, fingerprint, target, fold, test, or condition.

## 6. Checkpoint sequence and learner work

### Assembly sequence

1. Verify the accepted Checkpoint 1 release and the three module release fingerprints.
2. Verify the two public CDC data fingerprints and row counts.
3. Copy the declared immutable artifacts into their namespaced locations.
4. Copy the learner checkpoint records.
5. Generate the sorted immutable manifest.
6. Complete the cumulative interpretation from cited artifacts.
7. Score the eight criteria without changing available points.
8. adjudicate all 25 gates.
9. complete the conditions register and human sign-off.
10. defend the package through all 12 questions.
11. validate the assembled package.
12. record one allowed disposition and explicit Module 07 permission.

### Learner work

The learner writes synthesis, not a second set of module results. Every material numeric statement cites a checkpoint-relative artifact. Contradictions are returned to the owning module instead of being reconciled by prose.

### Protected target

The assembler refuses an existing target. Learners must build into a new directory so a prior submission cannot be partially overwritten.

### Defense prompts

The defense asks about the most consequential validity threat, DAG adjustment versus prediction features, overlap, missingness, dependence or censoring, forecast target and cutoff, benchmark choice, temporal validation, reporting coverage, seeded failures, independent checking of agent claims, and Module 07 preservation.

## 7. Upstream release inventory and immutable facts

### Checkpoint 1 identity

- Release SHA-256: `03c147d2e75cd446a43b9d56e49495df69af90d42d2b14ad4d860aea9d67239f`
- Modeling rows: 374
- Split: 224 train, 75 validation, 75 test
- Positive outcomes: 25, 7, and 4
- Selected model: `ML01`
- Locked threshold: `0.08513264`
- Test confusion: 48 true negatives, 23 false positives, 2 false negatives, and 2 true positives

### Module 04 identity

- Release SHA-256: `ffcf57c30d77be5c2271488a4d2dd08cc44d430cc590025e918c0ec8f1c4e12e`
- Selection case: 374 cohort rows, 111 timing rows, 263 structural blanks
- Treatment fixture: 600 rows, 91 missing severity values, known ATE -6.00000000
- Repeated fixture: 2,400 rows, 600 people, ICC 0.83598751
- Survival fixture: 600 rows, 449 events, 151 censored
- Treatment hazard ratio: 0.67945425, with reading interval 0.55144790 to 0.83717443
- Accepted validity checks: 16

### Module 05 identity

- Release SHA-256: `d81bcc3ac2ac2971cb1a03467673d86a905a125f7aed859f2e7669e9c7003f6d`
- CDC NHSN source: 6,208 rows, 14 fields, 67 jurisdictions
- Full-source SHA-256: `8a492c3d2d3dae07c42e89ef35ed714d23acab32596f42037dcf8dd0284531d1`
- Massachusetts series: 94 ordered weekly rows, 21 fields
- Series SHA-256: `394d9b02d2cc9b4fbf0d9f415db3da6b04393dd9430816973e81fef86fb0e616`
- Five expanding-window folds, four-week horizon, weeks 75 through 94
- Sixty prediction rows across three eligible models and 20 common targets
- Damped-Holt MAE 14.99587157; last-value MAE 28.20000000; seasonal-naive MAE 93.15000000
- Accepted forecast checks: 20

### Module 06 identity

- Release SHA-256: `bfc137523817e57b9eab6baf5729222f5a8021df203c36ba1162f4f7757e824e`
- Accepted artifacts: 13
- Accepted contract tests: 18
- Seeded failures: 10
- Independent verifications: 3
- Adjudicated agent claims: 4
- Summary gates: 7

### Required failure codes

`LEAKAGE_FIELD`, `TEST_ROW_IN_FIT`, `LABEL_INVERTED`, `SPLIT_CHANGED`, `FUTURE_ROW_IN_FIT`, `CONFUSION_DENOMINATOR`, `CALIBRATION_BIN_OMITTED`, `FINGERPRINT_CHANGED`, `USE_BOUNDARY_MISSING`, and `AGENT_CLAIM_UNVERIFIED`.

## 8. Exact folder and file contract

### Root structure

```text
02-validity-forecast-testing-release/
  .gitattributes
  .gitignore
  VERSION
  README.md
  checkpoint-contract.json
  assessment.md
  validate_checkpoint.py
  release-manifest.csv
  cumulative-interpretation.md
  technical-defense.md
  component-score.csv
  gate-results.csv
  conditions-register.csv
  reviewer-record.md
  reproduction-record.md
  accessibility-review.md
  ai-use.md
  human-sign-off.md
  progression-decision.md
  prior-checkpoint/
  modules/
    04-validity-adjustment-longitudinal/
    05-forecasting-temporal-validation/
    06-agent-assisted-modeling-testing/
  public-data/
```

### Immutable namespace

The 117 manifest members are immutable after assembly: six checkpoint controls and 111 upstream evidence artifacts. The prior checkpoint, each module, and public data remain in separate namespaces. Basenames are never flattened into one shared directory.

### Editable records

The 12 non-manifest records are `README.md`, `cumulative-interpretation.md`, `technical-defense.md`, `component-score.csv`, `gate-results.csv`, `conditions-register.csv`, `reviewer-record.md`, `reproduction-record.md`, `accessibility-review.md`, `ai-use.md`, `human-sign-off.md`, and `progression-decision.md`.

### Total file count

An assembled package contains exactly 130 files: 117 manifest members, 12 editable records, and one generated manifest.

### Encoding and path rules

Text is UTF-8. CSV uses comma separation and LF line endings. Learner-facing records use plain ASCII hyphens and checkpoint-relative paths. Personal absolute paths, credentials, secrets, caches, virtual environments, and editor state are prohibited.

## 9. Assembly and immutable-manifest rules

### Inputs

The assembler accepts one Checkpoint 1 root, one root for each of Modules 04 through 06, and one public-data root. `--reference` selects the repository's accepted roots. Learner assembly requires all five explicit roots.

### Pre-copy verification

Before creating the target, the assembler verifies required files, source versions, the four release fingerprints, the modeling and split fingerprints, the two CDC fingerprints, the accepted split counts, Module 04 case counts, Module 05 fold contract, and Module 06 test counts.

### Manifest schema

```text
relative_path,source_unit,source_version,bytes,sha256
```

Paths are unique, safe, and sorted by `relative_path`. Bytes and lowercase SHA-256 are computed after copying. The manifest itself is not self-listed.

### Existing-target refusal

Assembly fails if the target already exists. It never merges, cleans, or overwrites a target.

### Determinism

Two assemblies from unchanged accepted inputs must have byte-identical manifests. Metadata timestamps do not enter the manifest.

### Change control

Any immutable change requires a new owning-unit version, an updated checkpoint contract, and a new checkpoint version. Editing the generated manifest is prohibited.

## 10. Cumulative interpretation contract

### Required sections

The cumulative interpretation contains:

1. decision and use boundary;
2. preserved Checkpoint 1 identity;
3. analytic aims and causal boundary;
4. DAG roles and adjustment logic;
5. overlap, balance, and selection;
6. missingness and sensitivity;
7. repeated measures, mixed models, survival, and referral;
8. CDC source identity and reporting coverage;
9. forecast target, folds, benchmarks, and candidate;
10. aggregate, fold, horizon, residual, interval, and failure readings;
11. accepted tests and seeded failures;
12. prompt, trace, critique, adjudication, and independent evidence;
13. source, transformation, reproduction, accessibility, privacy, and AI boundaries;
14. unresolved conditions; and
15. progression recommendation.

### Exact facts

The reference validator requires the central row counts, fingerprints, model IDs, thresholds, confusion counts, ATE, structural blanks, missing count, ICC, event/censor counts, forecast fold and horizon, three MAEs, test/failure/check counts, and no-deployment boundary.

### Required synthesis

The interpretation must explain why predictive features are not automatically an adjustment set, why balance diagnostics do not prove exchangeability, why the 111 selected timing rows cannot represent the full cohort, why temporal folds replace random cross-validation, why aggregate MAE does not erase a weak fold, and why an independently checked bounded claim can survive while an unsupported staffing claim is rejected.

### Prohibited synthesis

The learner may not claim that the DAG proves causality, weighting removes all bias, missingness is known to be at random, the hazard ratio is a treatment recommendation, the CDC series represents one stable hospital, residual tests prove independence, forecast intervals are calibrated, aggregate accuracy proves operations utility, agent review replaces human review, or checkpoint acceptance authorizes deployment.

## 11. Reproduction, accessibility, AI, privacy, and integrity

### Reproduction record

The record identifies operating system, Python, package versions where relevant, commands run, return codes, check totals, output differences, and independent verifier. It distinguishes manifest verification from recomputation. A changed result is documented and returned to its owner.

### Accessibility review

The reviewer confirms heading order, descriptive links, readable tables, non-color encoding, keyboard-readable records, forecast SVG title and description, equivalent forecast table, text alternative, equivalent DAG node/edge tables, and DAG narrative. Accessibility is a release gate.

### AI-use record

The record identifies the tool, task, data class, prompt or instruction reference, outputs used, rejected claims, corrections, independent checks, and human owner. Agent output is assistance, not evidence.

### Human sign-off

A real submission requires learner and reviewer names, roles, dates, scope, disposition, conditions, and ownership statement. Typed placeholders and simulated signatures fail. The technical reference may identify itself as a reference record, but it cannot impersonate a real learner or reviewer.

### Privacy and security

Only public aggregate or synthetic teaching data may enter the package. Restricted, identifiable, workplace-confidential, credential, secret, or token content is prohibited. Source rights and access conditions remain visible.

## 12. Twenty-five-point score contract

### Schema

```text
criterion_id,component,course_points_available,points_earned,status,evidence
```

### Required rows

Rows occur once and in this order: `V01`, `V02`, `V03`, `F01`, `F02`, `T01`, `AI01`, `H01`. Available points are exactly 4.00, 3.00, 5.00, 4.00, 4.00, 2.00, 2.00, and 1.00.

### Scoring rules

Earned points are decimals from zero through the available value. Status is `pass`, `pass with conditions`, `revise`, or `refer`. Every row cites evidence. A passing package earns at least 20.00 and has only passing statuses, but gates remain controlling.

### Reference score

The technical reference earns 25.00 of 25.00 because it supplies the accepted instructional evidence. Conditions concern named human and live-course approval, not hidden point deductions.

## 13. Twenty-five-gate contract

### Schema

```text
gate_id,gate,status,evidence,reviewer_note
```

### Exact gates

1. Checkpoint 1 input and split are unchanged.
2. Prediction and causal aims remain distinct.
3. The accessible DAG equivalents match the visual DAG.
4. Variable roles and adjustment purpose are explicit.
5. Collider, mediator, post-outcome, and selection variables are handled by purpose.
6. Overlap and balance are examined.
7. Missingness assumptions are explicit.
8. Structural blanks are not coded as zero.
9. Sensitivity analyses preserve target and population.
10. Clustered, repeated, and censored outcomes are handled or referred.
11. Exact CDC and Massachusetts fingerprints are preserved.
12. All 94 weeks are ordered and unique.
13. Forecast fits exclude future rows.
14. Naive baselines remain visible.
15. Errors compare the same folds, targets, and units.
16. Reporting coverage is visible.
17. No single-hospital, stable-process, staffing, capacity, causal, operational, or deployment claim is made.
18. All accepted tests pass.
19. All ten failures reject for their intended reason.
20. Agent critique is adjudicated against independent evidence.
21. Assistance and data class are disclosed.
22. Human sign-off is complete for the decision being made.
23. No restricted, identifiable, workplace-confidential, secret, or credential data appear.
24. Technical defense is adequate.
25. Module 07 progression is explicit and consistent with disposition.

### Status and evidence

Every gate status is `pass` or `fail`. A passing gate cites immutable or checkpoint evidence and includes a reviewer note. Any failed or incomplete gate returns the package without progression.

## 14. Technical-defense and reviewer contract

### Twelve questions

1. Which validity threat most changes the prediction claim?
2. How does the DAG adjustment set differ from prediction features?
3. What do overlap and balance show, and what can they not establish?
4. Which missingness assumption remains unverifiable?
5. How are repeated measures, clustering, or censoring handled?
6. What are the forecast target, unit, horizon, and cutoff?
7. Why is each naive benchmark retained?
8. Why is temporal validation used instead of random cross-validation?
9. How does reporting coverage change interpretation?
10. Which seeded failure is most consequential and why?
11. Which agent claim was independently checked, and how?
12. What must Module 07 preserve?

### Adequacy

The defense record has exactly 12 numbered answers and a status of `adequate` or `inadequate`. Each answer cites checkpoint-relative evidence. A live reviewer can mark the reference answer key inadequate if the learner cannot reproduce its reasoning.

### Reviewer record

The reviewer record names roles, people, dates, status, scope, conditions, conflicts, and referrals. `pending named human review` is honest for a curriculum reference but cannot support a real learner's Gate 22.

### Reference accountability distinction

The reference package's human-sign-off record is a signed curriculum-construction disposition by the Commons sponsor, not a simulated learner assessment. A live course run replaces it with actual learner and reviewer accountability.

## 15. Progression and return contract

### Progression record

The record states checkpoint ID/version, disposition, score, gates, defense, human sign-off scope, Module 07 permission, evidence, conditions, and return triggers.

### Reference progression

The reference disposition is `accept with conditions`; score is 25.00; all 25 technical/reference gates pass; defense is adequate; Module 07 is permitted for continued curriculum construction.

### Conditions carried to Module 07

- preserve all 117 immutable manifest members;
- preserve Checkpoint 1 identity and test counts;
- keep prediction and causal claims distinct;
- carry selection, missingness, repeated-measures, and censoring limits;
- keep both CDC fingerprints and all 94 ordered weeks;
- retain all benchmarks, weak-fold evidence, coverage context, and use limits;
- retain 18 accepted tests and all ten intended failure rejections;
- keep prompt, trace, critique, adjudication, and independent checks;
- require real learner and reviewer sign-off in a live run; and
- make no clinical, staffing, capacity, operational, fairness, safety, or deployment claim.

### Return routing

- Changed Checkpoint 1 identity, split, threshold, or test evidence returns to the owning prior module and Checkpoint 1.
- Changed causal structure, missingness, dependence, or censoring evidence returns to Module 04.
- Changed source, series, fold, benchmark, forecast, coverage, or use boundary returns to Module 05.
- Changed test, failure, prompt, trace, adjudication, independent check, or sign-off returns to Module 06.
- Changed cumulative score, gate, defense, condition, or disposition returns to Checkpoint 2.

## 16. Runnable acceptance checks

### Assembler self-check

The self-check assembles two references and one learner starter, verifies identical manifests, confirms 111 upstream artifacts, 117 manifest rows, 130 files, public-source inclusion, and refusal to overwrite an existing target.

### Validator self-check

The self-check validates a complete reference and a prompted starter, then proves rejection of an incomplete record, missing immutable evidence, out-of-range score, failed gate, and inconsistent sign-off or progression.

### Reference validation

The validator checks root files, version, contract, manifest safety and fingerprints, exact file count, upstream releases, data rows and hashes, fixed Module 04 through 06 facts, editable-record completion, ASCII path hygiene, score arithmetic, 25 gates, 12 defense answers, human ownership, and progression consistency.

### Acceptance commands

```powershell
python courses/modeling-inference-reproducible-analytics/checkpoints/02-validity-forecast-testing-release/assemble_checkpoint.py --self-check
python courses/modeling-inference-reproducible-analytics/checkpoints/02-validity-forecast-testing-release/validate_checkpoint.py --self-check
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/check-curriculum-specs.ps1
```

### Technical acceptance

All commands exit zero, two reference manifests match, the complete reference passes, the starter passes only in starter mode, all deliberate invalid packages fail for the intended reason, and the whole-repository curriculum checker recognizes Commons release `0.46.0`.

## 17. Release status, known issues, human review, and resume record

### Semantic-version decision

Checkpoint 2 begins at `0.1.0` because this is its first runnable contract. The Commons release advances from `0.45.0` to `0.46.0` because the repository gains a new cumulative curriculum package without breaking prior releases.

### Reference package status

Status is `runnable-release-candidate`. The package is suitable for continued curriculum construction and technical validation. It is not yet a live-course or production release.

### Measured runnable release

- Upstream artifacts: 111
- Immutable manifest rows: 117
- Editable records: 12
- Assembled files: 130
- Manifest bytes: 17,699
- Manifest SHA-256: `16733c55e8a9930f4903006c81e5fb1acb9e75386507f1aa46867daac89f6ccc`
- Complete reference checks: 735
- Learner starter checks: 689

### Known material limitations

- Named program reviewers and a live learner defense remain pending before alpha.
- Module 04 fixtures are synthetic and support no clinical treatment or transport claim.
- The 111-row timing analysis is selected and does not represent all 374 rows.
- Paired R execution remains pending in a named managed R environment.
- The CDC series is a changing-reporting jurisdiction aggregate, not a stable hospital process.
- The candidate loses one fold to the last-value benchmark, and intervals are illustrative.
- Contract tests establish declared invariants, not clinical safety, fairness, utility, or deployment readiness.

### Contributors

- Shuhan He: Commons sponsor, curriculum direction, and reference construction disposition.
- OpenAI Codex: checkpoint specification, deterministic assembly, reference records, and validation.

### Resume record

After this checkpoint is accepted and pushed, resume with FND-2 Module 07. Module 07 must consume the accepted Checkpoint 2 release without altering its manifest and must turn conditions into governance-ready evidence for the Week 7.5 final checkpoint.
