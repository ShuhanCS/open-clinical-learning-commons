# FND-2 Module 06: Agent-assisted modeling and testing

## 1. Module identity and place in the course

### Release identity

- Course: FND-2, Modeling, Inference, and Reproducible Analytics.
- Module: 06 of 07.
- Source week: 6.
- Learner work: 16.0 hours.
- Module ID: `oclc-fnd2-06`.
- Module version: 0.1.0.
- Commons release target: 0.45.0.
- Course points: no added weight; evidence is required for the 25-point Week 6 checkpoint and final 35-point package.
- Prerequisites: accepted Modules 03, 04, and 05.

### Purpose

Module 06 teaches the learner to use an agent as a bounded assistant whose work is inspected, tested, and owned by a person. The release tests accepted prediction, validity, and forecasting contracts; injects ten known failures; proves that each failure is rejected for the intended reason; maps agent claims to evidence; independently recalculates material results; and requires human sign-off.

### Relationship to earlier modules

The module does not refit or improve prior models. It treats 13 accepted artifacts as immutable inputs. Tests must expose drift, leakage, arithmetic errors, incomplete evidence, unsupported claims, and data-sharing violations without silently repairing them.

### Relationship to Checkpoint 2

Checkpoint 2 freezes Module 04's 15-point validity share, Module 05's 10-point forecasting share, and Module 06's required gate evidence into one cumulative 25-point Week 6 release.

### Relationship to Module 07

Module 07 receives accepted models, forecast, tests, failures, trace log, human decisions, and use boundaries only after Checkpoint 2 accepts the package.

### Required ending state

- 13-row immutable artifact manifest;
- 18 passing accepted-contract tests;
- ten deterministic failure fixtures;
- ten intended rejections;
- three independent material recalculations;
- four adjudicated agent claims;
- seven data-class rules;
- accessible summary;
- prompt and trace evidence;
- human sign-off; and
- Checkpoint 2 progression disposition.

## 2. Decision, owner, audience, and dispositions

### Decision owner

The decision owner is a responsible-AI and model-validation reviewer. The learner remains the accountable analyst. Data governance, privacy, security, clinical, forecasting, accessibility, and independent-instructor reviewers may be consulted.

### Decision

Do the data, feature, split, prediction, metric, calibration, validity, temporal, documentation, and agent-audit tests pass accepted evidence and reject every seeded failure for its intended reason, with an accountable human for every material assisted step?

### Allowed dispositions

1. `accept Week 6 gate and continue to Checkpoint 2 with conditions`;
2. `revise Module 06`;
3. `return affected upstream module`;
4. `refer responsible-AI or validation design`; or
5. `stop`.

### Reference disposition

The reference is `accept Week 6 gate and continue to Checkpoint 2 with conditions`. All accepted tests, seeded failure rejections, independent recalculations, and summary gates pass. Human review remains pending and no model-use permission expands.

### What this decision does not approve

- an agent as reviewer of record;
- repeated prompting as independent verification;
- patient or restricted data sharing;
- automatic repair of accepted evidence;
- model deployment;
- clinical use;
- staffing or capacity use;
- governance approval; or
- Module 07 progression before Checkpoint 2.

## 3. Foundation skill and assurance hierarchy

### Foundation skill

The learner can decompose an analytic task into allowed inputs, bounded actions, required evidence, deterministic tests, expected failures, independent checks, and human decisions.

### Assurance hierarchy

1. Artifact identity: exact upstream bytes and hashes.
2. Contract test: accepted evidence satisfies declared invariants.
3. Negative test: known bad evidence is rejected.
4. Reason check: rejection occurs for the intended failure.
5. Independent verification: a material result is recalculated from lower-level evidence.
6. Claim adjudication: agent prose is accepted, modified, or rejected.
7. Human sign-off: a named person owns the release decision.

### Stop principle

If a test passes bad evidence, rejects good evidence, fails for the wrong reason, or depends on the same unsupported agent claim it is meant to check, work stops.

### Test versus evidence

A test result is evidence about a declared contract, not proof that a model is clinically safe, causally valid, fair, useful, or deployable.

### Agent boundary

An agent may propose, implement, explain, or critique a test. It may not decide the data class, waive a gate, invent evidence, approve a model, or sign on behalf of a person.

## 4. Assessable outcomes and evidence map

### Outcomes

The learner can:

1. decompose tasks into inputs, actions, outputs, checks, and decisions;
2. classify shared data;
3. constrain file scope and output format;
4. state prohibited claims;
5. verify accepted artifact fingerprints;
6. test split counts and labels;
7. test feature timing;
8. test prediction schema;
9. recalculate confusion counts;
10. test calibration group completeness;
11. test validity invariants;
12. test forecast folds and future-row exclusion;
13. recalculate forecast error;
14. seed ten failure types;
15. require intended rejection codes;
16. audit an agent claim against evidence;
17. reject invented approval;
18. modify an overstated diagnostic claim;
19. preserve prompt and trace logs;
20. record corrections;
21. sign as accountable analyst; and
22. decide Checkpoint 2 progression.

### Evidence map

| Outcome group | Evidence |
|---|---|
| Immutable inputs | accepted-artifact manifest |
| Positive tests | 18-row contract-test table |
| Negative tests | failure fixtures and ten-result registry |
| Data governance | seven-row data-class table and prompt constraints |
| Independent check | three-row verification table |
| Agent audit | four-row claim adjudication and trace log |
| Human ownership | sign-off and progression decision |
| Accessibility | Markdown summary and structured tables |
| Reproduction | standard-library suite, builder, validator |

### Minimum explanation

For every material test, state what contract it protects, what input it reads, what bad case it rejects, what exact evidence proves behavior, and who decides what happens next.

## 5. Concept ownership and out-of-scope boundaries

### Module 06 owns

- agent-safe task decomposition;
- prompt constraints;
- data-class rules;
- source and artifact fingerprint tests;
- split, feature, prediction, metric, and calibration tests;
- validity and forecast tests;
- deterministic failure mutations;
- rejection-code verification;
- bounded agent critique;
- claim-to-evidence mapping;
- hallucination audit;
- independent recalculation;
- prompt and trace logs;
- correction records;
- human sign-off; and
- Checkpoint 2 handoff.

### Module 06 introduces but does not own

- formal model validation;
- security penetration testing;
- privacy threat modeling;
- regulated software assurance;
- fairness validation;
- production incident response;
- continuous monitoring; and
- organizational AI governance.

### Module 06 does not own

- changing accepted models;
- changing forecast folds;
- choosing clinical use;
- waiving a prior limitation;
- accessing restricted data;
- model-card approval; or
- final course defense.

### No test theater

The release keeps the smallest suite that covers the declared contracts and all ten required failures. Test count is not a quality claim; observable protection and failure behavior matter.

## 6. Lesson sequence and learner time

| Lesson | Focus | Evidence | Hours |
|---|---|---|---:|
| 06.1 | Task decomposition | agent-safe plan | 1.5 |
| 06.2 | Data classes and prompts | rules and constraints | 1.5 |
| 06.3 | Artifact and data contracts | manifest and data tests | 2.0 |
| 06.4 | Prediction and metric tests | feature, confusion, calibration | 2.0 |
| 06.5 | Forecast and temporal tests | folds, future-row exclusion, error | 2.0 |
| 06.6 | Seeded failures | ten deterministic mutations | 2.5 |
| 06.7 | Agent critique and hallucination audit | adjudication table | 1.5 |
| 06.8 | Independent verification | three recalculations | 1.0 |
| 06.9 | Trace, sign-off, and progression | accountable release | 2.0 |
| Total | | | 16.0 |

### Within-module gates

- Data-class gate before sharing.
- Prompt-constraint gate before an agent task.
- Accepted-test gate before failure injection.
- Intended-reason gate after each failure.
- Independent-check gate before accepting a material claim.
- Human-sign-off gate before Checkpoint 2.

## 7. Accepted artifact architecture

### Immutable manifest

The package fingerprints 13 artifacts:

- Module 03 prediction model contract;
- Module 01 split registry used by Module 03;
- Module 03 test predictions, confusion table, calibration table, and transformed features;
- Module 04 release and 16-row validity checks;
- Module 05 release and forecast contract;
- Module 05 temporal folds, forecast predictions, and aggregate metrics.

### Exact inherited facts

- 374 split rows and 224/75/75 partitions;
- four test outcomes;
- `ML01` and threshold 0.08513264;
- 15 train-only transformed features;
- test confusion 48/23/2/2;
- five calibration groups covering 75 rows;
- 16 passing validity checks;
- five forecast origins with zero future rows;
- 60 forecast predictions on 20 common targets; and
- damped-Holt MAE 14.99587157 below both benchmarks.

### Change rule

Any upstream byte or hash change stops Module 06. The affected upstream module must explain and version the change before tests are rebased.

## 8. Task decomposition and prompt contract

### Required task fields

- task ID;
- decision question;
- allowed files;
- data class;
- requested action;
- exact output schema;
- prohibited actions;
- prohibited claims;
- required checks;
- independent verification;
- human owner; and
- stop condition.

### Prompt constraints

An acceptable prompt names a bounded task such as "suggest assertions for these published CSV contracts." It does not say "review everything," grant filesystem-wide access, ask an agent to decide approval, or include secrets or restricted records.

### Output rule

Every material claim must cite an available artifact or be labeled as a proposal. A path, citation, package, result, or approval that cannot be independently found is rejected.

### Human-decision fields

The prompt must reserve data classification, claim scope, clinical meaning, waiver, score, recommendation, and sign-off for a person.

## 9. Data classes and sharing controls

### Seven released classes

| Class | Agent sharing in this release |
|---|---|
| Public aggregate | allowed with source record |
| Documented synthetic | allowed with synthetic boundary |
| Deidentified research | prohibited; use approved governance route |
| Protected health information | prohibited |
| Workplace confidential | prohibited |
| Credential or secret | prohibited |
| Restricted licensed | prohibited unless explicitly approved |

### Secret rule

Tokens, passwords, keys, cookies, connection strings, and credentials are never prompt content. If exposure is suspected, stop and follow the relevant rotation and incident process.

### Minimum disclosure

The trace log records the class and a description of what was shared, not a duplicate of sensitive content.

## 10. Accepted contract-test suite

### Test families

The 18 tests cover data, model, leakage, metric, calibration, validity, forecast, and documentation contracts.

### Positive-test principle

Accepted evidence must pass unchanged. A test that rejects the release is not automatically correct; first determine whether the test, input fingerprint, or accepted contract changed.

### Exact checks

- split rows, counts, and outcomes;
- selected model and locked threshold;
- leakage fixture ineligibility;
- train-only feature fit;
- unique test prediction rows;
- confusion denominator and positives;
- calibration group completeness;
- validity invariant status;
- forecast origins and horizon;
- future-row exclusion;
- common target set;
- candidate metric ranking; and
- prediction and forecast use boundaries.

### Reference result

All 18 accepted-contract tests pass. The result means the suite reads accepted evidence correctly at release time.

## 11. Seeded failure fixtures

### Required failures

| ID | Mutation | Expected code |
|---|---|---|
| F01 | post-index predictor | `LEAKAGE_FIELD` |
| F02 | test row in fit | `TEST_ROW_IN_FIT` |
| F03 | label inversion | `LABEL_INVERTED` |
| F04 | changed split counts | `SPLIT_CHANGED` |
| F05 | future forecast row in fit | `FUTURE_ROW_IN_FIT` |
| F06 | confusion denominator 74 instead of 75 | `CONFUSION_DENOMINATOR` |
| F07 | omitted calibration bin without disclosure | `CALIBRATION_BIN_OMITTED` |
| F08 | changed source fingerprint | `FINGERPRINT_CHANGED` |
| F09 | missing use boundary | `USE_BOUNDARY_MISSING` |
| F10 | unsupported agent claim | `AGENT_CLAIM_UNVERIFIED` |

### Deterministic mutation rule

Fixtures are compact structured objects, not altered accepted files. The runner constructs each known-bad case and applies the relevant guard. It records expected code, observed code, rejection, intended reason, and status.

### Intended-reason rule

A failure that is rejected for a different reason does not pass. This prevents a broken parser or missing file from masquerading as the target safeguard.

### Reference result

All ten fixtures are rejected with their exact expected codes.

## 12. Metric and model independent verification

### Prediction recalculation

The suite reads 75 row-level observed and selected labels, independently rebuilds the four confusion cells, and obtains 48 true negatives, 23 false positives, two false negatives, and two true positives.

### Forecast recalculation

The suite reads the 20 damped-Holt prediction rows, recalculates absolute and squared errors, and obtains MAE 14.99587157 and RMSE 21.07855007.

### Independence standard

The check derives a result from lower-level rows with separate code. Repeating the same prompt to the same agent is not independent verification.

### Scope

Arithmetic agreement does not verify clinical usefulness, source completeness, or deployment readiness.

## 13. Agent critique and claim adjudication

### Four reference claims

1. Lower candidate MAE than both benchmarks: accept after V02.
2. Ready for staffing decisions: reject because no evidence and prohibited use.
3. Ljung-Box p-values prove residual independence: modify to a bounded failure-to-reject reading.
4. Perfect leaked-model performance should win: reject because timing makes the model ineligible before performance.

### Adjudication values

- `accept`: supported and correctly scoped;
- `modify`: evidence exists but quantity or scope is overstated;
- `reject`: unsupported, contradicted, prohibited, or fabricated;
- `refer`: specialist judgment is needed.

### Agent critique is not evidence

An agent statement starts a review task. It becomes a retained claim only after the human owner links it to accepted evidence and records an independent check when material.

## 14. Hallucination and invention audit

### Audit targets

- paths that do not exist;
- citations not present in source records;
- package APIs not installed or tested;
- metrics absent from outputs;
- performance numbers not reproducible;
- reviews or approvals not signed;
- claims beyond use boundaries; and
- changes attributed to a tool without a trace.

### Default response

Do not silently repair invented evidence. Record the unsupported statement, reject or modify it, identify the required source, and name the human owner.

### High-risk invention

Invented clinical approval, data provenance, privacy permission, or model performance is an automatic stop and referral.

## 15. Prompt, trace, correction, and sign-off records

### Trace log fields

- trace ID and time;
- tool;
- bounded task;
- data class;
- inputs shared;
- prompt or exact reusable summary;
- output retained;
- affected artifact;
- material risk;
- independent check;
- result;
- correction or action; and
- human owner.

### Correction record

If agent output changes an artifact, record what changed, why, evidence used, who verified it, and whether versioning or upstream return is required.

### Human sign-off

The signatory confirms that no prohibited class was shared, every material claim is evidenced, all corrections are recorded, all failures behave as declared, and the person owns the recommendation.

### No simulated signature

Reference material may show a teaching disposition, but named reviewer and learner signatures remain pending until actual humans sign.

## 16. Exact learner deliverables and package contract

### Required core files

- README, VERSION, requirements;
- source and data specifications;
- test contract and prompt constraints;
- assessment and instructor notes;
- runner, builder, validator;
- release metadata; and
- learner template.

### Required learner records

- `agent-task-plan.md`;
- `prompt-trace-log.csv`;
- `agent-critique.md`;
- `claim-adjudication.csv`;
- `independent-verification.md`;
- `human-sign-off.md`;
- `reproducibility-check.md`;
- `accessibility-review.md`;
- `ai-use.md`; and
- `progression-decision.md`.

### Required generated evidence

- 13-row artifact manifest;
- 18-row accepted-test table;
- ten failure fixtures;
- ten-row failure-results table;
- three-row independent verification;
- four-row reference claim adjudication;
- seven-row data-class rules;
- seven-row summary gates;
- accessible summary; and
- build report.

### Portable build

The learner workspace copies the 13 accepted inputs, standard-library test runner, builder, validator, reference outputs, prompts, and contracts. It rebuilds into a new target and refuses overwrite.

## 17. Assessment and noncompensable gates

### Week 6 gate contribution

Module 06 adds no course points. Checkpoint 2 cannot pass unless every gate below passes.

### Gates

1. Accepted Modules 03 through 05 evidence unchanged.
2. Tests inspect exact source, split, feature, prediction, metric, validity, and time contracts.
3. All accepted tests pass.
4. All ten seeded failures reject.
5. Every rejection uses the intended code.
6. No test is weakened to accept a bad artifact.
7. Agent critique is not treated as evidence.
8. Independent verification uses lower-level evidence and separate code.
9. Material assistance is disclosed.
10. Protected, identifiable, workplace, restricted, secret, and credential data are prohibited.
11. Unsupported agent statement is rejected or corrected.
12. Human owner is explicit.
13. Human sign-off is complete.
14. Week 6 checkpoint and Module 07 progression disposition is explicit.

### Automatic return

- fingerprint mismatch;
- accepted test failure without adjudication;
- seeded failure accepted;
- wrong rejection reason;
- test rewritten solely to pass;
- prompt with prohibited data;
- missing material trace;
- repeated prompt called independent verification;
- invented evidence retained;
- agent approval substituted for human sign-off; or
- expanded model use.

## 18. Feedback, revision, recovery, and support

### Feedback order

1. data class and scope;
2. immutable inputs;
3. positive tests;
4. seeded failures;
5. intended rejection reasons;
6. independent verification;
7. claim adjudication;
8. trace and correction;
9. human sign-off;
10. prose.

### Revision examples

| Defect | Response |
|---|---|
| Test passes post-index field | fix shared timing guard and rerun F01 |
| Failure rejected because parser crashed | repair parser, then require intended code |
| Agent invents path | reject claim and record audit |
| Same prompt repeated | implement independent row-level recalculation |
| PHI included | stop, do not continue package work, follow governance process |
| Test changed to accept bad row | restore contract and review integrity |
| Human signature blank | block Checkpoint 2 |

### Supported route

The runner uses Python's standard library. No model refit or live network call is required. Structured tables and Markdown support keyboard and screen-reader workflows.

### Extension

Add a failure only when it protects an accepted contract and includes a deterministic intended-reason check. Do not chase test count.

## 19. Responsible AI, privacy, security, accessibility, and integrity

### AI may assist

- suggest test cases;
- draft assertions;
- explain failures;
- compare structured evidence;
- draft a trace summary; and
- propose accessible wording.

### AI may not own

- data-class decision;
- secret handling;
- evidence acceptance;
- test waiver;
- model-use scope;
- clinical meaning;
- score;
- sign-off; or
- progression.

### Privacy and security

Only public aggregate and documented synthetic data are allowed in the released exercise. Secrets and credentials are never allowed. Restricted classes require separate approved systems and governance.

### Accessibility

The summary is a Markdown table. Every result has structured CSV or JSON. Status does not depend on color, animation, image, or pointer interaction.

### Integrity traps

- marking a fixture rejected when the observed code differs;
- deleting a failing test;
- citing an agent critique as independent evidence;
- hiding a material prompt;
- signing for another person;
- inventing a reviewer; and
- treating technical test passage as deployment approval.

## 20. Validation and acceptance tests

### Builder self-check

The builder verifies 13 fingerprints, runs 18 accepted tests, rejects ten failures, runs three independent checks, records four adjudications, passes seven summary gates, reproduces a copied learner workspace, and refuses an existing target.

### Validator self-check

The validator must independently rebuild all outputs, compare exact rows and bytes, verify the fixture JSON, check prompt completion by mode, reject a missing failure-results file, verify release metadata, and report release and starter counts.

### Acceptance commands

```text
python courses/modeling-inference-reproducible-analytics/modules/06-agent-assisted-modeling-testing/build_agent_test_evidence.py --self-check
python courses/modeling-inference-reproducible-analytics/modules/06-agent-assisted-modeling-testing/validate_agent_test_evidence.py --self-check
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/check-curriculum-specs.ps1
```

### Repository acceptance

- 21 plain-ASCII sections;
- Commons 0.45.0;
- module 0.1.0;
- exact output hashes;
- full curriculum gate;
- current-task commit; and
- pushed branch.

## 21. Release, handoff, and resume contract

### Semantic-version decision

Module 06 begins at 0.1.0 and advances the Commons minor release from 0.44.0 to 0.45.0. Upstream releases remain unchanged.

### Release record to freeze

- 13 artifact fingerprints;
- 18 accepted tests;
- ten seeded failures and codes;
- three independent recalculations;
- four adjudicated claims;
- seven data-class rules;
- seven summary gates;
- output hashes;
- builder self-check, 519 release validator checks, and 490 starter validator checks;
- seeded-failure result SHA-256 `177f8bab9a8153c884241cbcdf2562b4d8bb53f629068100fa5f48591fc14a2e`;
- human-review status; and
- Checkpoint 2 disposition.

### Checkpoint 2 handoff

Checkpoint 2 receives the exact Module 04 15-point validity evidence, Module 05 10-point forecasting evidence, and Module 06 gate package. It assembles without recomputing accepted results.

### Module 07 handoff

After Checkpoint 2, Module 07 receives accepted model and forecast contracts, tests, failure fixtures, trace log, independent verification, adjudications, conditions, and model-use boundaries.

### Resume record

Module 06 is complete only after its specification, test package, learner records, validator, full gate, Commons 0.45.0 update, commit, and push pass. Resume with FND-2 Checkpoint 2 only.
