# APP-4 Module 05 specification: Sandbox prototype and failure modes

## 1. Module identity, purpose, timing, and workload

- Module ID: `oclc-app4-05`.
- Course: `APP-4: Data for Clinical Decision Support`.
- Title: `Sandbox prototype and failure modes`.
- Hours: `16.0`.
- Module points: `0`.
- Assessment role: required zero-point gate for Checkpoint 02.
- Module version: `0.1.0`.
- Commons release: `0.82.0`.
- Package path: `courses/clinical-decision-support/modules/05-sandbox-prototype-failure-modes/`.

Module 05 asks whether the accepted Module 04 teaching fixture behaves as specified and fails visibly enough to enter safety and monitoring work. Learners build and inspect a local, nonnetworked sandbox. They trace FHIR R4-shaped prefetch resources through CDS Hooks 2.0.1-shaped requests, branch logic, responses, visible failures, and one seeded silent failure.

The course uses a 7.5-week planning model. Week 6 is the cumulative workflow, sandbox, safety, and monitoring checkpoint. The official section calendar controls the actual due date:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

Module 05 adds no points. The accepted 25-point Module 04 score is carried into Checkpoint 02 exactly once. Module 05 must pass every gate before Module 06 can construct the safety and monitoring case.

## 2. Source authority, provenance, and teaching standards

### Accepted upstream release

Module 05 freezes the complete Module 04 reference workspace:

- module: `oclc-app4-04@0.1.0`;
- Commons release: `0.81.0`;
- files: `302`;
- immutable manifest rows: `285`;
- manifest bytes: `60,302`;
- manifest SHA-256: `41692b01fa2c339068fcdbf5fbc6f3e301a79ba4535d9ecb94d602cb2e4b3bf9`;
- nested Week 3 immutable rows: `204`;
- accepted Module 04 score: `25.00 of 25.00`;
- accepted Module 04 gates: `20 of 20 pass`;
- design fixture: `panel-t003`; and
- threshold fixture: `0.03000000`, unaccepted.

The builder verifies exact byte counts and SHA-256 values for the Module 04 release, decision contract, build report, patient frame, encounter opportunities, and candidate events before producing a sandbox release.

### Teaching standards

FHIR R4 supplies resource shapes:

https://hl7.org/fhir/R4/

FHIR R4 Patient:

https://hl7.org/fhir/R4/patient.html

FHIR R4 Encounter:

https://hl7.org/fhir/R4/encounter.html

FHIR R4 Observation:

https://hl7.org/fhir/R4/observation.html

FHIR R4 Condition:

https://hl7.org/fhir/R4/condition.html

FHIR R4 Bundle:

https://hl7.org/fhir/R4/bundle.html

FHIR R4 Parameters:

https://hl7.org/fhir/R4/parameters.html

FHIR R4 OperationOutcome:

https://hl7.org/fhir/R4/operationoutcome.html

CDS Hooks supplies teaching request and response shapes:

https://cds-hooks.hl7.org/

ONC SAFER Guides supply safety review prompts:

https://www.healthit.gov/topic/safety/safer-guides

These sources define teaching shapes and review questions. They do not certify the package, prove conformance, validate a clinical workflow, or grant implementation authority.

## 3. Decision, owner, and authority boundary

### Decision

Does the local nonproduction prototype behave as specified and fail visibly enough to enter Module 06 safety, monitoring, governance, and embedded-ML work?

### Decision owner

The fictional `CGH-GIM-01` clinical decision support governance council owns the disposition. A learner or agent may present evidence, but the council decides whether to continue with conditions, revise, refer, or stop.

### Permitted next action

The reference permits nonproduction Module 06 curriculum construction. Module 06 may build a safety case, monitoring measures, governance records, and one fixed gradient-boosted challenger comparison from the frozen evidence.

### Prohibited authority

The package does not permit:

- real-patient scoring;
- clinical threshold selection or acceptance;
- clinical alerting;
- diagnosis, testing, ordering, treatment, outreach, or follow-up;
- silent-mode evaluation;
- implementation;
- production connection;
- deployment;
- FHIR or CDS Hooks conformance claims;
- security, regulatory, medical-device, or vendor-readiness claims; or
- an agent-owned progression decision.

The `0.03000000` value remains an unaccepted sandbox fixture. `panel-t003` remains a passive-panel mechanics fixture. A passing test cannot change either role.

## 4. Prerequisite handoff and protected evidence

Module 05 begins only after Module 04 passes. It receives the full Module 04 reference workspace, not a selected set of convenient files.

Protected evidence includes:

- the complete Module 04 release manifest;
- the exact nested Week 3 chain;
- all six Module 03 evidence candidates;
- the rejected Module 02 `0.20` fixture;
- all 12 positive `0.03` workflow cases;
- the one repeat positive case;
- all unavailable-input states;
- every suppressed access and equity result;
- `workflow-evidence-release.md`;
- `candidate-design-review.md`;
- `automation-bias-controls.csv`;
- `access-equity-privacy-review.csv`;
- `override-stop-conditions.md`;
- `module-score.csv`;
- `gate-results.csv`; and
- `progression-module05-handoff.md`.

Learners cannot refit the model, retune a score, replace an upstream failure, fill a suppressed result, change the alert budget, or accept a threshold inside this module.

## 5. Assessable learning outcomes

By the end of Module 05, learners can:

1. freeze and verify a cumulative upstream release before prototype work;
2. distinguish FHIR R4 and CDS Hooks teaching shapes from conformance claims;
3. trace a request through context, prefetch, ordered logic, response, terminal state, and notice;
4. reproduce normal positive, normal negative, boundary, repeat, and suppression behavior;
5. test missing, stale, inconsistent, delayed, duplicate, terminology, unit, service, latency, and version failures;
6. distinguish a visible failure from a request that disappears without response, terminal trace, or notice;
7. detect silent failure by reconciling independent ledgers;
8. block a structurally inaccessible card before release;
9. explain why an empty card array is not evidence of low risk or safe nonaction;
10. preserve the zero-point gate and 25-point score carryforward without duplication;
11. make a human-owned progression decision with stop conditions; and
12. hand an immutable sandbox result to Module 06 without expanding clinical authority.

## 6. Assessment role, evidence, and checkpoint relationship

Module 05 contributes zero course points. Its evidence is mandatory for Checkpoint 02.

| Component | Course points | Checkpoint 02 role |
|---|---:|---|
| Module 04 workflow, burden, human factors, and equity | 25.00 | carried once |
| Module 05 sandbox prototype and failures | 0.00 | required gate |
| Module 06 safety, monitoring, governance, and embedded ML | 0.00 | required gate |
| Checkpoint 02 total | 25.00 | cumulative release |

Required Module 05 evidence includes:

- exact upstream identity;
- local architecture and trust boundary;
- FHIR-shaped prefetch contract;
- CDS Hooks-shaped request and response contract;
- complete 31-case matrix;
- expected and observed results;
- request and terminal traces;
- visible-failure review;
- silent-failure review;
- latency and version review;
- accessibility review;
- failure-mode register;
- prototype release;
- score carryforward;
- 20 gate results;
- reproduction evidence;
- AI-use record; and
- protected Module 06 handoff.

A numeric score cannot compensate for a failed gate. The module does not create bonus points, partial credit, or a second copy of the Module 04 score.

## 7. Data, resource, request, and response contract

### Generated release

The deterministic release is `APP4-M05-LOCAL-SANDBOX-2026-08-31-v1`.

| File | Grain | Rows | Purpose |
|---|---|---:|---|
| `data/sandbox/requests.ndjson.gz` | one sandbox case | 31 | request wrapper, hook, context, and embedded prefetch |
| `data/sandbox/prefetch-resources.ndjson.gz` | one prefetch key per case | 184 | separately inspectable FHIR R4-shaped resources |
| `data/sandbox/responses.ndjson.gz` | one sandbox case | 31 | transport, body, notice, and observed outcome |
| `outputs/trace-events.csv.gz` | one trace event | 61 | request receipt and terminal branch ledger |
| `outputs/test-matrix.csv` | one case | 31 | expected outcome, visibility, and authority |
| `outputs/test-results.csv` | one case | 31 | expected-versus-observed execution result |
| `outputs/visibility-audit.csv` | one case | 31 | four-ledger reconciliation |
| `outputs/accessibility-checks.csv` | one case | 31 | card structure and blocking result |
| `outputs/invariant-checks.csv` | one invariant | 20 | release-level acceptance checks |
| `build-report.json` | one release | 1 | sources, outputs, counts, runtime, and authority |

The sandbox output-manifest digest is `e34f75bdcba3d2474912f587b54f81b7038b65790c51435bb10810d40643c97f`.

### Request wrapper

Each request row contains:

| Field | Meaning | Validation |
|---|---|---|
| `caseId` | unique curriculum case | 31 unique IDs |
| `category` | declared normal or failure route | must match test matrix |
| `fixtureOrigin` | Module 04 event or seeded mutation | required |
| `serviceId` | local fictional service | `CGH-GIM-01` unless mismatch test |
| `hookVersion` | teaching version | `1.0` unless mismatch test |
| `request.hookInstance` | request-ledger identity | required; duplicate case reuses one ID |
| `request.hook` | hook name | `patient-view` |
| `request.context.patientId` | synthetic subject | must start with `SP` |
| `request.context.encounterId` | synthetic opportunity | must start with `WF-E` |
| `request.context.userId` | fictional role | no real clinician |
| `request.context.decisionTime` | event-time cutoff | fixed synthetic timestamp |
| `request.context.explicitSynthetic` | data status | must be `true` |
| `request.prefetch` | local teaching resources | no server retrieval |

No request contains `fhirServer`, credentials, tokens, or a live endpoint.

### Prefetch resources

| Key | Teaching shape | Required behavior |
|---|---|---|
| `patient` | Patient | synthetic tag and `SP` ID |
| `encounter` | Encounter | patient reference and decision time |
| `bmi` | Observation | LOINC `39156-5`, UCUM `kg/m2`, positive value, acceptable date |
| `conditions` | collection Bundle | active scripted diabetes entry suppresses the fixture |
| `hba1c` | collection Bundle | recent scripted HbA1c entry suppresses the fixture |
| `prediction` | Parameters | fixed model version, offline score, threshold, and unaccepted status |

The prediction Parameters resource uses a local teaching code path. It is not a clinical FHIR profile or validated model output.

### Response shapes

| Result | Shape | Human notice | Meaning |
|---|---|---:|---|
| candidate panel | HTTP 200 with card | false | synthetic branch at or above fixture |
| empty card | HTTP 200 with empty cards | false | declared negative, duplicate, or suppression branch |
| visible input or semantic state | HTTP 200 with information card | true | fixture could not be evaluated |
| unsupported request | HTTP 400 OperationOutcome-shaped body | true | service or hook contract rejected |
| service unavailable | HTTP 503 OperationOutcome-shaped body | true | seeded visible service failure |
| timeout | HTTP 504 OperationOutcome-shaped body | true | seeded visible latency failure |
| accessibility blocked | HTTP 422 OperationOutcome-shaped body | true | malformed card stopped |
| silent failure | status 0 and null body | false | no response, terminal trace, or notice |

Cards contain a plain summary, detail, indicator, and synthetic source label. They contain no suggestion, order, link, or clinical action.

## 8. Local runtime and architecture

`build_sandbox.py` uses the Python standard library. It reads accepted local files, constructs deterministic cases, evaluates ordered branches, writes deterministic gzip files with a fixed modification time, and verifies every generated output.

The runtime has:

- no network listener;
- no network client;
- no FHIR server;
- no authentication;
- no external Python dependency;
- no real patient data;
- no real clinician or encounter identity;
- no message delivery; and
- no external link or action suggestion.

The data path is:

1. verify Module 04 source identities;
2. select the 12 accepted positive synthetic fixtures and one accepted negative fixture;
3. construct seeded boundary and failure mutations;
4. assemble local FHIR-shaped prefetch;
5. wrap it in CDS Hooks-shaped request records;
6. run the ordered local evaluator;
7. write response and trace ledgers;
8. reconcile visibility;
9. run accessibility checks;
10. verify expected behavior and invariants; and
11. freeze the output identities.

The evaluator is a curriculum mechanism. It is not a deployable service architecture.

## 9. Complete case matrix and expected behavior

The 31 cases cover 21 categories.

| Category | Cases | Expected behavior |
|---|---:|---|
| normal positive | 11 | candidate panel |
| repeat positive | 1 | candidate panel with repeat disclosure |
| normal negative | 1 | empty card with below-fixture trace |
| threshold boundary | 1 | candidate panel at exactly `0.03000000` |
| missing input | 1 | visible unavailable state |
| stale input | 1 | visible stale state |
| inconsistent input | 1 | visible inconsistent state |
| delayed input | 1 | visible delayed state |
| duplicate request | 1 | empty card with duplicate trace |
| terminology mismatch | 1 | visible terminology state |
| hook version mismatch | 1 | HTTP 400 visible failure |
| unit mismatch | 1 | visible unit state |
| unsupported service | 1 | HTTP 400 visible failure |
| missing score | 1 | visible unavailable score |
| known diabetes suppression | 1 | empty card with suppression trace |
| recent HbA1c suppression | 1 | empty card with suppression trace |
| service unavailable | 1 | HTTP 503 visible failure |
| response timeout | 1 | HTTP 504 visible failure |
| silent failure | 1 | detected missing response, terminal trace, and notice |
| accessibility defect | 1 | malformed card blocked with HTTP 422 |
| model version mismatch | 1 | visible version state |

Twelve cases reproduce the exact Module 04 positive fixture set. One of those is the accepted repeat opportunity. The boundary and failure cases are labeled seeded synthetic mutations; they do not change Module 04 evidence.

### Ordered branch contract

The local evaluator checks:

1. duplicate request identity;
2. seeded silent drop;
3. service availability;
4. response latency;
5. service identity;
6. hook and hook version;
7. input delay;
8. required BMI presence;
9. BMI date;
10. BMI range;
11. terminology;
12. unit;
13. known-diabetes suppression;
14. recent-HbA1c suppression;
15. prediction presence;
16. model version;
17. score presence;
18. threshold identity;
19. below-fixture result;
20. candidate result; and
21. accessibility blocking.

Branch order is part of the test contract. Learners may not reorder failures to make one expected case pass while changing another.

## 10. Worked example

### Example A: visible timeout

`M05-F14` is a seeded response-delay case.

1. The request ledger records `M05-REQ-M05-F14`.
2. The synthetic response delay is 2,001 milliseconds.
3. The teaching latency budget is 2,000 milliseconds.
4. The evaluator emits a visible timeout branch.
5. The response envelope records HTTP 504 and an OperationOutcome-shaped body.
6. The terminal trace is present.
7. Human notice is present.
8. The visibility audit classifies the case as visible, not silent.

This result does not measure real latency or availability. It confirms the declared local branch.

### Example B: silent failure

`M05-F15` uses `drop_after_receive`.

1. The request ledger proves receipt.
2. The response body is absent.
3. The terminal trace is absent.
4. Human notice is absent.
5. The visibility audit compares the four independent fields.
6. The audit flags exactly one silent failure.

A request log alone would miss the problem. A response envelope alone would also be insufficient because the silent case still has a curriculum envelope with a null body. The audit uses the body, terminal trace, and notice evidence separately.

### Example C: malformed card

`M05-F16` removes the summary from an otherwise candidate-shaped card.

1. The card structure audit sees a missing summary.
2. The malformed card is not released.
3. The response becomes an HTTP 422 OperationOutcome-shaped body.
4. A terminal trace and human notice remain visible.

Blocking this fixture does not prove the final interface is accessible. It proves that one declared structural defect is caught.

## 11. Guided practice

### Practice A: upstream chain

Reproduce the 285-row Module 04 manifest identity and the 29, 73, and 102-row nested manifests. Explain why the full 302-file release is frozen instead of copying only the Module 04 score and design review.

### Practice B: request anatomy

Choose `M05-P01`. Trace its hook instance, patient, encounter, user, decision time, BMI, conditions, HbA1c, prediction version, score, threshold status, response, and terminal branch. Label each field as standard-shaped, local teaching metadata, or authority statement.

### Practice C: empty-card interpretation

Compare `M05-N01`, `M05-F05`, `M05-F11`, and `M05-F12`. Each returns an empty card array for a different reason. Write one supported statement and one prohibited statement for each case.

### Practice D: visible input failures

Compare missing, stale, inconsistent, delayed, terminology, unit, and score failures. Identify the field that changes, the first rejecting branch, the human notice, and the owner needed in Module 06.

### Practice E: version controls

Compare the hook-version and model-version mismatch cases. Explain why interface version and model version need separate monitoring and stewardship.

### Practice F: silence reconciliation

Use `visibility-audit.csv` to reproduce the single silent failure. Then remove one ledger conceptually and describe which false assurance becomes possible.

### Practice G: accessibility blocking

Inspect `M05-F16`. Explain why summary, detail, source label, no suggestions, and no external links are release checks, and why those checks still do not prove usability or accessibility in practice.

## 12. Independent exercise

Learners complete all 16 records without changing an immutable file.

1. Verify the complete Module 04 release and nested Week 3 chain.
2. Draw the local architecture and trust boundaries.
3. Classify every request and prefetch field.
4. Classify every response body and transport state.
5. Reproduce all 31 expected results.
6. Trace the 12 positive cases and the repeat.
7. Explain normal negative, duplicate, and suppression empty-card states.
8. Review all 12 visible-failure cases.
9. Reproduce the silent-failure rule from independent ledgers.
10. Review latency, hook version, model version, and threshold status separately.
11. Confirm that the malformed card is blocked.
12. Assign an owner and Module 06 control to every failure mode.
13. Carry the 25 Module 04 points once and add zero Module 05 points.
14. Record AI assistance and independent verification.
15. Make a human-owned progression decision.
16. Freeze the complete Module 06 handoff and every authority prohibition.

A learner may recommend revision, referral, or stop. A learner may not change a failed fixture, add an action suggestion, connect a server, use real data, call the messages conformant, accept a threshold, or start silent-mode evaluation.

## 13. Visualization and communication requirements

The primary communication artifact is an accessible trace table. It must show:

- case ID and category;
- request receipt;
- response presence;
- HTTP or local transport status;
- terminal trace presence;
- human notice presence;
- observed outcome;
- accessibility status;
- design and threshold roles; and
- claim limit.

A flow diagram may supplement the table but cannot replace exact evidence. Any diagram must distinguish:

- local file boundaries from network boundaries;
- a request wrapper from a CDS Hooks field;
- a FHIR-shaped resource from a conformance claim;
- a response envelope from delivery evidence;
- an empty card from a failure;
- a visible failure from a silent failure; and
- curriculum progression from clinical authority.

Communication rules:

- use direct labels and text equivalents;
- do not rely on color alone;
- keep denominators beside counts;
- show all 31 cases, including the null response;
- label seeded mutations;
- label `0.03000000` unaccepted every time it appears in a decision context;
- state that `panel-t003` is a mechanics fixture;
- do not call an empty card low risk;
- do not call a passing test safe, conformant, or production ready; and
- end with the human disposition and prohibited authority.

For clinicians, lead with visible nonaction, unavailable states, and repeat behavior. For informatics reviewers, lead with field shape, branch order, trace, version, and latency. For patient and accessibility reviewers, lead with wording, access, notice, recourse, and what the card does not authorize. For governance, lead with chain of custody, failure detection, owners, stop rules, and evidence needed before reconsideration.

## 14. Exact learner submission package and filenames

Each learner or reference workspace contains 341 files:

- 324 immutable manifest rows;
- 16 editable records; and
- `release-manifest.csv`.

The final immutable manifest is 75,019 bytes with SHA-256 `6bc3e7c0040b8ae93d273d1464459ae8d500913e0e8a423ca1e5b120256c8baf`.

The 324 immutable rows consist of 12 module controls, 10 sandbox evidence files, and all 302 Module 04 reference files.

Learners complete exactly these records:

1. `prototype-architecture.md`
2. `request-prefetch-contract.csv`
3. `response-card-contract.csv`
4. `test-matrix-review.csv`
5. `traceability-audit.csv`
6. `visible-failure-review.csv`
7. `silent-failure-review.md`
8. `latency-version-review.csv`
9. `accessibility-review.csv`
10. `failure-mode-register.csv`
11. `prototype-release.md`
12. `checkpoint-score-carryforward.csv`
13. `gate-results.csv`
14. `reproducibility-check.md`
15. `ai-use.md`
16. `progression-module06-handoff.md`

Editable records stay outside the immutable manifest. The validator checks their structure, required evidence, gate results, score carryforward, and progression authority. The builder refuses an existing target, and learner and reference immutable manifests must be byte-identical.

## 15. Gate rubric and pass conditions

Module 05 uses 20 noncompensable pass-or-revise gates.

| Gate | Requirement |
|---:|---|
| 1 | exact Module 04 release identity |
| 2 | exact nested Week 3 chain |
| 3 | local nonnetworked runtime |
| 4 | FHIR-shaped resource disclosure |
| 5 | CDS Hooks-shaped message disclosure |
| 6 | all 31 cases |
| 7 | all 12 positive fixtures and the repeat |
| 8 | normal and boundary behavior |
| 9 | missing, stale, inconsistent, and delayed input |
| 10 | duplicate, suppression, and no-card interpretation |
| 11 | terminology and unit mismatch |
| 12 | hook and model version mismatch |
| 13 | service unavailability and timeout |
| 14 | request-to-terminal trace completeness |
| 15 | silent-failure detection from independent ledgers |
| 16 | accessibility defect detected and blocked |
| 17 | no suggestion, order, action, or external link |
| 18 | reproduction and AI accountability |
| 19 | Module 04 score carried once with no Module 05 points |
| 20 | human progression and unchanged authority |

Pass conditions:

- all 20 gates pass;
- all 16 records are complete;
- all immutable files match their manifest;
- all 31 test results pass;
- all 20 release invariants pass;
- exactly one silent failure is detected;
- exactly one accessibility defect is blocked;
- the disposition is allowed;
- Module 06 permission stays nonproduction; and
- every clinical and deployment prohibition remains.

The reference disposition is `continue with conditions`.

## 16. Common errors, failure modes, and instructor response

| Error | Why it matters | Instructor response |
|---|---|---|
| Calling the fixture an implementation | confuses local files with a service | restore the runtime boundary |
| Adding a local web server | expands the attack and authority surface without instructional need | remove the listener and use file execution |
| Adding a FHIR server URL | implies connection and retrieval authority | remove the endpoint and restore local prefetch |
| Using a real identifier | violates the synthetic-only contract | stop, remove the data, and audit provenance |
| Calling a shaped resource conformant | makes an unsupported standards claim | rewrite as FHIR R4-shaped teaching data |
| Calling a shaped response CDS Hooks compliant | skips formal profile and conformance review | restore the teaching-shape claim |
| Treating `0.03` as selected | converts a fixture into a clinical threshold | stop progression and restore unaccepted status |
| Treating an empty card as low risk | hides negative, duplicate, and suppression reasons | require the terminal reason |
| Treating a duplicate as a repeat encounter | collapses transport and workflow concepts | compare hook instance and encounter IDs |
| Imputing missing or stale input | creates false certainty | return the visible unavailable state |
| Converting an unknown unit silently | hides semantic risk | stop evaluation and refer the mapping |
| Monitoring only HTTP status | misses null-body and silent routes | reconcile all four ledgers |
| Calling a request log delivery evidence | misses downstream disappearance | require response, terminal trace, and notice evidence |
| Calling the seeded silence rate clinical | turns one fixture into an incidence estimate | limit the claim to detection mechanics |
| Releasing the malformed card | fails a declared accessibility gate | block the output and record the defect |
| Adding a suggestion or order | creates a clinical action route | remove it and stop progression review |
| Giving Module 05 points | changes the source assessment plan | restore zero points and carry Module 04 once |
| Letting an agent approve progression | removes human accountability | require the named governance owner |
| Passing Module 06 a cleaned result | hides failure evidence needed for safety work | freeze the complete release |
| Treating validation as deployment approval | confuses package integrity with clinical authority | restate every prohibited route |

## 17. Accessibility, equity, privacy, and responsible-claim checks

### Accessibility

Every released card requires a summary, detail, synthetic source label, no suggestion, and no external link. `M05-F16` intentionally removes the summary; the release blocks it. Learners must also review semantic order, headings, labels, equivalent text, contrast, zoom, keyboard operation, target size, timing independence, error recovery, and plain language in any explanatory artifact.

The structural check does not prove that the panel is usable or accessible in practice. Language, screen-reader, low-vision, motor-access, and cognitive-support reviews remain human work before alpha.

### Equity and access

Module 04 access and equity results remain frozen. Module 05 cannot fill a suppressed rate, merge groups, create a group-specific threshold, or target a patient group. The sandbox may test interface states, but it cannot convert a synthetic access label into evidence of fairness or equal reach.

### Privacy and data minimization

All patient IDs are Commons synthetic IDs. Requests contain no name, address, contact detail, credential, token, or endpoint. Source synthetic identifiers remain protected inside the upstream release. Synthetic status does not remove retention, access-control, misuse, or review obligations.

### Responsible claims

- A passing case proves only declared local fixture behavior.
- A FHIR-shaped resource is not a conformance result.
- A CDS Hooks-shaped response is not delivery evidence.
- A visible failure does not prove an adequate clinical fallback.
- One seeded silent failure does not estimate an incident rate.
- A blocked malformed card does not prove accessibility.
- A candidate panel is not a clinical alert or recommendation.
- An empty card is not evidence of low risk.
- A threshold fixture is not a threshold decision.
- A local latency branch is not a performance benchmark.
- Curriculum progression is not permission for silent mode, implementation, or deployment.

## 18. AI and agent policy

An agent may help with:

- code drafting;
- deterministic fixture generation;
- file inventory;
- comparison tables;
- prose drafting and editing;
- hash and manifest checks;
- validator execution; and
- consistency checks.

An agent may not:

- alter accepted Module 04 evidence;
- refit or retune the model;
- choose or accept a clinical threshold;
- change `panel-t003` into an approved design;
- hide or rewrite a failed test;
- fill an unavailable or suppressed result;
- infer delivery from one ledger;
- add a suggestion, order, or clinical action;
- use real patient data;
- connect a live endpoint;
- claim FHIR or CDS Hooks conformance;
- approve silent-mode evaluation, implementation, or deployment;
- choose the progression disposition; or
- sign for a human reviewer.

The AI-use record names tools, protected evidence, human-owned decisions, prohibited agent actions, verification, and remaining review. Agent-generated code must pass source identity, deterministic builds, manifests, case results, invariants, learner and reference validation, copied validation, and deliberate failure routes.

## 19. Answer key and instructor findings

### Exact release facts

- Release ID: `APP4-M05-LOCAL-SANDBOX-2026-08-31-v1`.
- Cases: `31`.
- Module 04 positive cases: `12`.
- Repeat positive cases: `1`.
- Prefetch resources: `184`.
- Response envelopes: `31`.
- Trace events: `61`.
- Visible failure cases: `12`.
- Passing declared tests: `31 of 31`.
- Release invariants: `20 of 20`.
- Silent failures detected: `1`.
- Accessibility defects blocked: `1`.
- External Python dependencies: `0`.
- Network listeners: `0`.
- Network clients: `0`.
- FHIR servers: `0`.
- Suggestions: `0`.
- External links: `0`.
- Accepted threshold: `none`.

### Silent-failure answer

`M05-F15` is the only silent case. It has request receipt, no response body, no terminal trace, and no human notice. The visibility audit detects it by comparing independent ledgers. The visible 503 and 504 cases are not silent because they retain a body, terminal trace, and notice.

### Accessibility answer

`M05-F16` removes a required summary. The structural audit detects the defect and replaces the malformed card with a visible HTTP 422 OperationOutcome-shaped response. This is a blocking curriculum control, not proof of full accessibility.

### Score answer

Module 04 contributes 25.00 points once. Module 05 contributes 0.00 points. The Checkpoint 02 subtotal remains 25.00 until Module 06 adds required gates without points.

### Reference decision

The reference disposition is `continue with conditions`. Module 06 may build the nonproduction safety, monitoring, governance, and fixed-challenger package. Every failure remains visible, the design and threshold stay fixtures, and all clinical and deployment routes remain prohibited.

## 20. Runnable acceptance checks

### Sandbox builder

```powershell
python courses/clinical-decision-support/modules/05-sandbox-prototype-failure-modes/build_sandbox.py --self-check
```

Expected result: 31 cases, 184 prefetch resources, 61 trace events, byte-identical builds, one detected silent failure, and existing-target refusal.

### Workspace builder

```powershell
python courses/clinical-decision-support/modules/05-sandbox-prototype-failure-modes/build_workspace.py --self-check
```

Expected result: 324 immutable rows, all 302 Module 04 files, 16 editable records, 341 assembled files, identical learner and reference manifests, and existing-target refusal.

### Validator

```powershell
python courses/clinical-decision-support/modules/05-sandbox-prototype-failure-modes/validate_workspace.py --self-check
```

Expected result: 2,649 reference checks, 2,558 learner checks, copied validation, and 20 rejected failure routes.

The validator checks:

- every own-manifest file by path, bytes, and SHA-256;
- all 285 Module 04 immutable rows;
- all 204 nested Week 3 immutable rows;
- exact Module 04 score, gates, design, threshold role, and authority;
- all 31 requests, responses, case results, and visibility states;
- all 184 prefetch resources and 61 trace events;
- all 20 invariants;
- all 16 assessed records;
- the zero-point rule and 25-point carryforward;
- all 20 gates;
- the human disposition and Module 06 boundary; and
- copied validator behavior.

The deliberate failures cover missing records, own immutable mutation, Module 04 and nested-manifest mutation, nested-file removal, network-scope expansion, case-count drift, single-ledger substitution, visible-case drift, silent-rule change, version-review change, accessibility-review change, failure-register drift, score inflation, failed gates, expanded agent authority, deployment disposition, threshold acceptance, expanded Module 06 permission, and a learner starter presented as complete.

The complete curriculum checker must also verify the exact 21 sections, package file count, sandbox counts, workspace counts, validation counts, version, gate result, score carryforward, and Module 06 handoff.

## 21. Release status, reviewers, known issues, and Module 06 handoff

- Module version: `0.1.0`.
- Commons release: `0.82.0`.
- Status: runnable release candidate for curriculum construction.
- Module points: `0.00`.
- Module 04 score carried once: `25.00 of 25.00`.
- Reference gates: `20 of 20 pass`.
- Reference progression: `continue with conditions`.
- Accepted clinical threshold: `none`.
- Module 06 permission: nonproduction safety, monitoring, governance, and fixed-challenger curriculum construction only.
- External Python dependencies: `none`.

### Reviews required before alpha

- APP-4 faculty owner;
- primary-care or endocrinology clinician;
- clinical informatics reviewer;
- FHIR and CDS Hooks interoperability reviewer;
- patient-safety reviewer;
- workflow and human-factors reviewer;
- patient and patient-communication reviewer;
- language-access reviewer;
- disability-access and accessibility reviewer;
- equity reviewer;
- privacy and data-stewardship reviewer;
- security reviewer;
- responsible-AI reviewer; and
- independent reproduction instructor.

### Known issues

- The official APP-4 section and half-term dates remain to be assigned from the published calendar.
- The resources and messages are teaching shapes, not reviewed conformance artifacts.
- The failure routes are seeded synthetic fixtures, not observed clinical incidents.
- The latency values are branch fixtures, not performance measurements.
- The structural card audit does not prove usability or accessibility in practice.
- Named human reviews remain pending before alpha.

### Protected Module 06 handoff

Module 06 must freeze the complete Module 05 workspace and release manifest. It must preserve all 302 Module 04 files, all 31 cases, every response and trace, the silent-failure finding, the blocked accessibility defect, the 25-point score carryforward, all 20 Module 05 gates, `panel-t003`, the unaccepted `0.03000000` role, and every authority prohibition.

Module 06 may add hazards, controls, monitoring measures, independent reconciliation, incident response, escalation, fallback, stop, restart, retirement, governance, and one fixed gradient-boosted challenger comparison. The challenger must use the same predictors, target, cutoffs, development cycles, temporal holdout, later-cycle stress test, missing-input rules, threshold candidates, alert budget, and evaluation rows as the accepted transparent model.

Module 06 may not change intended use, choose a threshold, excuse a workflow or prototype defect, automate an action, score a real patient, begin silent-mode evaluation, connect a production system, implement, or deploy.
