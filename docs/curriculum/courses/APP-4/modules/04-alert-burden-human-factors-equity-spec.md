# APP-4 Module 04: Alert burden, human factors, and equity

## 1. Module identity, duration, prerequisites, and place in the course

- Course: APP-4, Data for Clinical Decision Support.
- Module ID: `oclc-app4-04`.
- Module version: `0.1.0`.
- Commons release: `0.81.0`.
- Position: Module 04 of 7.
- Planned week: instructional Week 4.
- Learner work: 16.5 hours.
- Course points: 25, counted once at the Week 6 checkpoint.
- Package: `courses/clinical-decision-support/modules/04-alert-burden-human-factors-equity/`.
- Runnable status: release candidate for curriculum construction.

The prerequisite is the accepted APP-4 Checkpoint 01 reference release, version `0.1.0` at Commons `0.80.0`. The checkpoint contains 263 files. Its 245-row candidate manifest is 45,897 bytes with SHA-256 `4e78d2313ce324fd372e6fc187afee333b27ed0cc0270c6ab8c08354dd5c3151`. The three nested module manifests protect 204 immutable rows.

Module 04 does not refit the model, revise the cohort, select a clinical threshold, or change the 40-point Week 3 score. It carries all accepted evidence forward and asks a different question: what would each candidate mean for a fictional workflow, the people doing the work, and the people affected by it?

Modules 04 through 06 form the application block. Module 04 owns the 25-point workflow, burden, human-factors, access, equity, and privacy component. Module 05 adds the nonproduction sandbox and failure-mode gate. Module 06 adds the safety, monitoring, governance, and embedded-ML gate. The Week 6 checkpoint counts Module 04's 25 points once and adds no new points for Modules 05 or 06.

## 2. Healthcare decision and named audience

The module decision is:

> Is one candidate design supportable enough to enter a nonproduction Module 05 sandbox without accepting a clinical threshold?

The continuing concept is an informational panel for the explicitly fictional `CGH-GIM-01` adult general internal medicine and primary care service. It asks a clinician to consider whether confirmatory HbA1c testing may be worth discussing. It cannot diagnose, place an order, change treatment, deny care, target a patient, or act without clinician review.

The reference recommendation is `panel-t003`, a passive contextual panel using `0.03000000` only as a sandbox fixture. The number remains unaccepted. The recommendation creates enough positive synthetic cases to exercise Module 05 mechanics. It does not establish a clinical threshold, local policy, silent-mode plan, or implementation route.

| Audience | Decision need |
|---|---|
| Receiving clinicians | timing, purpose, nonaction, uncertainty, repeat exposure, override, and burden |
| Patients and patient representatives | purpose, privacy, language access, disability access, recourse, and what the panel cannot do |
| Nursing and workflow leads | task sequence, hidden work, handoffs, competing work, and pause rights |
| Clinical informatics and EHR teams | input readiness, reason codes, traceability, context, version, and the Module 05 test boundary |
| Patient-safety team | automation bias, unresolved cases, stop triggers, fallback, and escalation ownership |
| Data stewards | source identity, information cutoff, missingness, staleness, inconsistency, minimization, and lineage |
| Language and disability-access reviewers | qualified language routes, semantic order, contrast, keyboard use, plain language, and alternative formats |
| Equity reviewer | subgroup support, suppressed estimates, access consequences, and prohibited group targeting |
| CDS governance council | accept, condition, revise, refer, or stop a sandbox proposal without expanding clinical authority |

## 3. Foundation skill being revisited or extended

Module 04 revisits foundation methods only where they change a decision support design.

| Prior skill | Module 04 extension |
|---|---|
| FND-1 source lineage | verify the complete Week 3 chain of custody before using any workflow result |
| FND-1 event-time data | preserve ready, missing, stale, and inconsistent states at the fictional decision moment |
| FND-1 joins and denominators | separate people, encounters, sessions, candidate-frame encounters, ready encounters, and candidate cards |
| FND-1 data-quality rules | treat unavailable input as unavailable rather than zero, below threshold, or no risk |
| FND-2 probability and threshold analysis | connect each unaccepted evidence candidate to historical missed-case evidence and separate synthetic card counts |
| FND-2 calibration and transport | treat the synthetic score-distribution mismatch as a warning, not a reason to retune |
| FND-2 subgroup support | suppress candidate-card rates when support rules fail and prohibit group-specific action |
| DA-730 comparison design | show tradeoffs with clear denominators, direct labels, equivalent tables, and separate axes for unlike quantities |
| APP-3 workflow reasoning | map task, timing, competing work, handoffs, hidden work, pause rights, and unresolved cases |

The module does not reteach SQL, Python syntax, generic descriptive statistics, logistic regression, calibration, or visualization mechanics. Learners use those skills to inspect a sociotechnical decision. A calibrated historical model is not a reason by itself to create an alert.

## 4. Learning outcomes that can be assessed

By the end of Module 04, learners can:

| ID | Assessable outcome | Evidence |
|---|---|---|
| M04-LO1 | Verify the accepted Week 3 identity and explain why its evidence cannot be changed inside a workflow review. | release manifest and workflow evidence release |
| M04-LO2 | Map the user, task, timing, action, nonaction, patient consequence, hidden work, handoffs, and pause rights for a candidate panel. | workflow task analysis and role map |
| M04-LO3 | Compare all six unaccepted thresholds using separate historical consequences and synthetic workflow counts. | candidate design review |
| M04-LO4 | Calculate eligible encounters, cards, cards per session, repeats, unavailable inputs, scripted interactions, response time, unresolved cases, and task minutes with correct denominators. | burden and session evidence |
| M04-LO5 | Compare an interruptive banner, a passive contextual panel, and no alert without treating any design as clinically proven. | design comparison and interpretation |
| M04-LO6 | Identify usability, automation-bias, override, privacy, language, disability-access, patient-communication, and hidden-work concerns. | human-factors records |
| M04-LO7 | Apply support and suppression rules to age, source-recorded gender, language, disability access, and BMI slices without ranking or targeting groups. | access and equity review |
| M04-LO8 | Make a human-owned sandbox recommendation with conditions, stop rules, protected evidence, and explicit authority limits. | progression and Module 05 handoff |

## 5. Concept ownership and explicit out-of-scope boundaries

### Module 04 owns

- workflow task analysis and timing;
- roles, handoffs, competing work, and hidden work;
- candidate cards per encounter and clinician session;
- repeat exposure and unresolved work;
- scripted views, acknowledgments, dismissals, deferments, response time, and task minutes;
- comparison of all six evidence candidates;
- comparison of an interruptive banner, a passive contextual panel, and no alert;
- usability and automation-bias controls;
- human nonaction, override, pause, stop, fallback, and recourse;
- language access, disability access, patient communication, privacy, and minimization;
- equity support and suppression for the workflow question; and
- one human-governed Module 05 sandbox recommendation.

### Module 04 preserves without changing

- the complete public NHANES releases and their provenance;
- the complete Synthea FHIR source release;
- the intended use, logic, trigger, input, terminology, suppression, and trace contracts;
- the fixed model, coefficients, partitions, calibration, performance, decision curves, threshold audit, and subgroup audit;
- the 40-point Week 3 score and 56 cumulative gates;
- all six unaccepted evidence candidates;
- the rejection of `0.20` as a mechanics fixture; and
- every clinical, implementation, and deployment prohibition.

### Reserved for later modules

- Module 05 owns FHIR R4 and CDS Hooks-shaped message construction, response traces, normal and failure cases, latency, version, visible failure, and silent failure.
- Module 06 owns the safety case, monitoring plan, calibration drift, incident route, escalation, stop, restart, retirement, governance, and transparent-versus-ML comparison.
- Module 07 owns clinician leadership, final product brief, communication, stewardship, accountability, and defense.

### Out of scope

- real patient, clinician, employee, protected, workplace, or restricted data;
- connection to a live EHR, identity provider, message bus, terminology service, or clinical network;
- clinical diagnosis, order placement, treatment advice, denial, triage, outreach, or targeting;
- real-patient scoring or a patient-level probability;
- selection or acceptance of a clinical threshold;
- a real alert, silent-mode evaluation, implementation, rollout, production connection, or deployment;
- claims that a scripted interaction measures fatigue, misuse, compliance, trust, workload, or care quality;
- claims that synthetic counts estimate local prevalence, burden, staffing, capacity, benefit, harm, or fairness;
- filling suppressed equity cells, merging groups to evade support rules, ranking groups, or creating group-specific action; and
- claims of FHIR conformance, CDS Hooks conformance, regulatory compliance, safety certification, or vendor readiness.

## 6. Lesson sequence with estimated learner time

| Lesson | Focus | Learner time | Product |
|---:|---|---:|---|
| 1 | Week 3 handoff and authority boundary | 1.5 hours | verified checkpoint identity and evidence map |
| 2 | Task, role, timing, handoff, and hidden-work analysis | 2.0 hours | task analysis, role map, and timing review |
| 3 | Synthetic workflow construction and denominator audit | 2.0 hours | patient, encounter, session, and input-state profile |
| 4 | Six-candidate burden and historical consequence comparison | 2.5 hours | candidate and session burden review |
| 5 | Interruptive, passive, and no-alert alternatives | 1.5 hours | candidate design comparison |
| 6 | Usability, automation bias, override, and stop controls | 2.0 hours | usability and control records |
| 7 | Language, disability access, equity, privacy, and patient communication | 2.5 hours | access, equity, privacy, and hidden-work review |
| 8 | Reproduction, 25-point release, recommendation, and defense | 2.5 hours | complete validated submission and Module 05 handoff |
| Total |  | 16.5 hours |  |

The instructor should pause after Lessons 3, 4, and 7. At each pause, learners state which evidence is public, which is synthetic, which result is unsupported, and what authority remains prohibited.

## 7. Authoritative readings and public clinical sources

### Required course records

- APP-4 source record: `docs/source/app-4-clinical-decision-support-source-record.md`.
- APP-4 course specification: `docs/curriculum/courses/APP-4/course-spec.md`.
- Checkpoint 01 specification: `docs/curriculum/courses/APP-4/checkpoints/01-logic-evidence-validation-readiness-spec.md`.
- Module 02 logic specification: `docs/curriculum/courses/APP-4/modules/02-logic-triggers-data-spec.md`.
- Module 03 evidence specification: `docs/curriculum/courses/APP-4/modules/03-evidence-calibration-validation-spec.md`.

### Public evidence and analytic guidance

- NHANES continuous survey portal: https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/
- NHANES analytic guidelines: https://wwwn.cdc.gov/Nchs/data/nhanes/analyticguidelines/11-16-analytic-guidelines.pdf
- Synthea repository: https://github.com/synthetichealth/synthea
- Synthea 4.0.0 release: https://github.com/synthetichealth/synthea/releases/tag/v4.0.0

### Interoperability, safety, and accessibility

- CDS Hooks 2.0.1: https://cds-hooks.hl7.org/
- FHIR R4: https://hl7.org/fhir/R4/
- ONC SAFER Guides: https://www.healthit.gov/topic/safety/safer-guides
- ONC SAFER Computerized Provider Order Entry with Decision Support guide: https://www.healthit.gov/wp-content/uploads/2025/06/SAFER-Guide-3.-CPOE-Final.pdf
- Web Content Accessibility Guidelines 2.2: https://www.w3.org/TR/WCAG22/

These sources define teaching shapes and review questions. They do not certify the Module 04 design, validate local practice, or grant implementation authority.

## 8. Dataset inventory, provenance, license, and teaching purpose

### Accepted upstream release

| Evidence | Exact identity | Teaching role | Limit |
|---|---|---|---|
| Checkpoint 01 candidate manifest | 245 rows, 45,897 bytes, SHA-256 `4e78d2313ce324fd372e6fc187afee333b27ed0cc0270c6ab8c08354dd5c3151` | complete Week 3 chain of custody | no clinical authority |
| Module 01 manifest | 29 rows, SHA-256 `40ff7384d227a38b0f93832731d984098e6e6f3324a958dafc2319d23f282b45` | intended use and full public-source release | no prediction or workflow evidence |
| Module 02 manifest | 73 rows, SHA-256 `bf3a30d66944a799a1dcbb3bc971bbcc81a6a3986e3e08cacf26fac41ecb9ded` | logic and complete synthetic FHIR release | mechanics only |
| Module 03 manifest | 102 rows, SHA-256 `e67f20599704f83ec1e695f23f571fb57c558109bde3bcc676a64afc3dcf8e22` | historical model, calibration, threshold, transport, and subgroup evidence | no threshold accepted |

NHANES is a public-use federal survey source. Learners retain CDC source links, release identities, survey-design fields, and analytic limits. Synthea is an open-source synthetic-data generator. Its repository license and source notices remain authoritative. The Commons release does not relabel synthetic data as deidentified clinical data.

### Module 04 workflow release

| File | Rows | Bytes | SHA-256 | Teaching purpose |
|---|---:|---:|---|---|
| `patient-frame.csv.gz` | 1,000 | 54,854 | `bfa374fa13c683a5bcc6915c776282b22c98015623db8c1b30562018dd3e7b2d` | candidate-frame and access inputs |
| `encounter-opportunities.csv.gz` | 1,200 | 25,394 | `b71bd822a8bb0d1b1c87430213fcf6e09e056b80ab18366812cbca65e08b4f87` | fictional sessions, input states, and interaction scripts |
| `candidate-events.csv.gz` | 7,200 | 82,953 | `278a9c74294c5ad13b38ade0215a88c8e4af37e7bc5e8d2e7fcc297d781a929f` | six threshold comparisons for every opportunity |
| `workflow-profile.csv` | 10 | 1,935 | `6336dc5e4e98c640dcdd6081c92529b2fa8ef9f835ea23ad384d17d5afe6a078` | release denominators |
| `candidate-burden.csv` | 6 | 1,729 | `8eee3c98314083d4d741dd135fcf84137d1de1c7fb6dcd0bc5e74fef2c57b1ad` | threshold-level burden |
| `design-comparison.csv` | 13 | 4,905 | `c9dbeff717dbc16772521b2ee53481c835d36f90c08cdd52578b4228e43168e8` | banner, panel, and no-alert alternatives |
| `session-burden.csv.gz` | 720 | 3,542 | `6086ad9279575b7406e8ef03215753a47e6dbd7731571720802f889089b2e83c` | threshold by session concentration |
| `equity-slices.csv` | 108 | 34,139 | `bc0ac37d4d56ef5bd7a3b62b499e04e60addd379103f630e76ba1d5ac822a99f` | access support and suppression |
| `invariant-checks.csv` | 20 | 936 | `ef9846bad989c3bd197ad6a5da24719dbaef271629ac55c16da951d7f4b6ec8b` | deterministic build integrity |

The workflow output-manifest digest is `4ab020f4862fe06ea3c877d7302afa988b7069ce5922ddb2f578841d22838911`. Every generated record is explicitly synthetic. No file may enter a live clinical system.

## 9. Data dictionary and expected analytic structure

### Patient frame

| Field | Meaning | Boundary |
|---|---|---|
| `synthetic_patient_id` | Commons teaching identifier | not a patient identifier |
| `source_patient_sha256` | fingerprint of the synthetic source ID | do not attempt reidentification |
| `age` and `age_band` | age at the fixed synthetic reference date | not local population evidence |
| `source_recorded_gender` | source value used by the fixed model | not gender identity or a treatment rule |
| `language_access_group` | English, Spanish, or other-language teaching group | not language proficiency |
| `scripted_disability_access_need` | interface test prompt | not a diagnosis |
| `latest_bmi` and `bmi_band` | latest synthetic BMI carried into the teaching frame | not a clinical assessment |
| `candidate_frame_status` | candidate eligibility before encounter input state | not screening eligibility for a real person |
| `offline_teaching_score` | fixed Module 03 formula applied to ready synthetic source values | not a clinical probability |

### Encounter opportunities

The encounter table has one row per scripted opportunity. It includes visit occurrence, session, fictional clinician, decision time, candidate-frame reason, input state, score when ready, competing-alert script, interaction script, access values, and claim limit. There are 1,200 rows, 200 repeat opportunities, 120 sessions, 12 fictional clinicians, and 10 opportunities per session.

Input states are `ready`, `missing`, `stale`, `inconsistent`, or `not_evaluated`. A candidate-frame encounter with a nonready input has a blank score. No unavailable value is imputed, moved backward in time, or interpreted as below threshold.

### Candidate events

Each encounter is evaluated against six evidence candidates, producing 7,200 rows. A row records candidate threshold, threshold status, result, reason, repeat-card status, scripted interaction, scripted view, scripted response time, scripted task minutes, and claim limit.

The only allowed threshold status is `evidence candidate, not selected or accepted`. The `0.20` fixture never appears. `candidate_card` means an offline synthetic branch result. It is not an alert or recommendation.

### Denominators

| Measure | Denominator |
|---|---|
| candidate-frame people | 1,000 synthetic people |
| candidate-frame encounters | 1,200 opportunities |
| input-unavailable rate | 288 candidate-frame encounters |
| cards per session | 120 scripted sessions |
| repeat-card count | prior card for the same synthetic person at the same threshold |
| candidate-card rate in an equity slice | ready candidate-frame encounters in that slice |
| historical flags or missed cases per 1,000 | NHANES temporal-holdout survey evidence, not synthetic encounters |

## 10. Worked example and instructor walkthrough

### Step 1: verify the handoff

Build the Checkpoint 01 reference workspace and verify its candidate manifest, nested manifests, score, gates, progression, and authority. Stop if any byte changes.

### Step 2: inspect workflow denominators

The release starts with 1,000 synthetic people. The candidate frame contains 238 people. The schedule adds 200 repeat opportunities, producing 1,200 encounters. Of 288 candidate-frame encounters, 39 have scripted missing, stale, or inconsistent inputs. The ready denominator is 249.

### Step 3: compare threshold counts

| Candidate | Synthetic cards | Cards per session | Sessions with cards | Repeat cards |
|---:|---:|---:|---:|---:|
| 0.02000000 | 116 | 0.9667 | 74 | 16 |
| 0.03000000 | 12 | 0.1000 | 10 | 1 |
| 0.04000000 | 3 | 0.0250 | 3 | 0 |
| 0.05000000 | 3 | 0.0250 | 3 | 0 |
| 0.07500000 | 0 | 0.0000 | 0 | 0 |
| 0.10000000 | 0 | 0.0000 | 0 | 0 |

The count is monotone, but it is not a local burden estimate. The scripted score distribution produces no cards at two evidence candidates even though NHANES contains historical events. This is a transport warning.

### Step 4: keep historical and synthetic results separate

At `0.03`, the NHANES temporal holdout reports 325.40301123 weighted flags per 1,000 and 11.59062056 weighted missed cases per 1,000. The synthetic schedule reports 12 cards. These values have different sources, denominators, and meanings. Do not divide or combine them.

### Step 5: compare design modality

The interruptive `banner-t003` script creates 12 interruption events. The passive `panel-t003` script creates zero interruption events but still produces 12 cards, 20.00 scripted task minutes, 10 sessions with cards, and one repeat. Zero scripted interruption does not mean zero attention, cognitive, communication, or documentation burden.

### Step 6: examine access support

At `0.03`, only the English-language synthetic slice reaches the predeclared support rule. Spanish, other-language, disability-access, age, source-recorded gender, and BMI rates remain suppressed. The correct response is more testing and review, not group merging or a group-specific threshold.

### Step 7: make the bounded recommendation

The reference advances `panel-t003` because 12 positive synthetic cases can exercise Module 05 normal and failure routes with no scripted banner interruption. It keeps `0.03` unaccepted and carries every access, equity, human-factors, and authority condition forward.

## 11. Guided practice

### Practice A: denominator trace

Starting from `workflow-profile.csv`, reproduce 1,000 people, 1,200 encounters, 200 repeats, 288 candidate-frame encounters, 39 unavailable inputs, 249 ready encounters, 120 sessions, and 12 fictional clinicians. Explain why each denominator differs.

### Practice B: candidate monotonicity

Use `candidate-events.csv.gz` to reproduce the six candidate-card counts. Verify that card counts do not rise as the threshold rises. Identify the three and zero-case candidates that cannot supply enough positive sandbox mechanics under the predeclared rule.

### Practice C: repeat and session concentration

Use `session-burden.csv.gz` to find sessions with more than one candidate card at `0.02` and `0.03`. Describe repeat exposure and concentration without calling either one fatigue.

### Practice D: interaction interpretation

Reproduce the scripted views, acknowledgments, dismissals, deferments, view-only states, unresolved states, median response seconds, and task minutes. For each, write one supported statement and one prohibited statement.

### Practice E: access support

Filter `equity-slices.csv` to `0.03`. Explain why the English-language rate is reportable with a boundary and why every other candidate-card rate remains blank. Do not combine groups.

### Practice F: alternative design

Compare `banner-t003`, `panel-t003`, and `no-alert`. State what each option changes, what it leaves unresolved, and what evidence would be required before any local evaluation.

## 12. Independent exercise

Learners complete the full 16-record submission without changing any immutable file.

1. Verify the Week 3 release and record its exact identity.
2. Draw the task sequence from session preparation through encounter close.
3. Name every actor, handoff, hidden task, and pause right.
4. Reproduce all six candidate counts and historical consequence fields.
5. Compare the interruptive banner, passive contextual panel, and no alert.
6. Test burden assumptions at half and twice the scripted task minutes.
7. Review usability, automation bias, nonaction, repeat exposure, and unresolved work.
8. Review English, Spanish, other-language, screen-reader, low-vision, motor-access, cognitive-support, age, gender, BMI, privacy, and targeting questions.
9. Make one human-owned recommendation: continue, continue with conditions, revise, refer, or stop.
10. State the selected sandbox design, threshold role, stop conditions, protected handoff, and every prohibited authority route.
11. Run the validator and preserve the result.

A learner may recommend another design or stop the route if the evidence and gates support that decision. A learner may not call a threshold clinically accepted, remove a suppressed result, use real data, or expand Module 05 beyond a nonproduction sandbox.

## 13. Visualization and communication requirements

The candidate design review must provide an accessible comparison table. A visual may supplement the table but cannot replace it.

Required communication rules:

- show all six candidates in ascending order;
- label the threshold status as unaccepted;
- separate NHANES historical consequences from synthetic workflow counts;
- include banner, passive-panel, and no-alert alternatives;
- show denominators next to rates;
- show zero-card candidates rather than dropping them;
- show 39 unavailable candidate inputs;
- show repeat cards and session concentration;
- leave unsupported equity rates blank and label the support rule;
- use direct labels and equivalent text;
- do not rely on color alone;
- state that scripted interactions are not observed behavior; and
- end with the bounded decision and prohibited authority.

Do not place historical missed cases and synthetic cards on one unlabeled axis. Do not imply a smooth benefit curve. Do not use a traffic-light color to suggest clinical acceptability. Do not rank access groups.

For a clinician audience, lead with task, timing, nonaction, and burden. For a patient audience, lead with purpose, limits, privacy, access, choice, and recourse. For governance, lead with source boundaries, unresolved support, owners, stop conditions, and evidence required before reconsideration.

## 14. Exact submission package and filenames

The learner workspace contains 302 files:

- 285 immutable manifest rows;
- 16 editable assessment records; and
- `release-manifest.csv`.

The 285 immutable rows consist of 12 module controls, 10 workflow evidence files, and all 263 Checkpoint 01 files.

Learners complete exactly these records:

1. `workflow-task-analysis.md`
2. `role-handoff-map.csv`
3. `timing-interruption-review.csv`
4. `burden-assumption-register.csv`
5. `candidate-design-review.md`
6. `usability-review.csv`
7. `automation-bias-controls.csv`
8. `access-equity-privacy-review.csv`
9. `patient-communication-hidden-work.md`
10. `override-stop-conditions.md`
11. `workflow-evidence-release.md`
12. `module-score.csv`
13. `gate-results.csv`
14. `reproducibility-check.md`
15. `ai-use.md`
16. `progression-module05-handoff.md`

The workspace builder refuses an existing target. The learner and reference immutable manifests are byte-identical. Editable records are not placed in the immutable manifest so learners can complete them, but the validator checks their structure and content.

## 15. Rubric and pass conditions

| Criterion | Points |
|---|---:|
| Workflow task analysis | 3.00 |
| Roles, handoffs, timing, and interruption | 2.50 |
| Six-candidate comparison | 3.00 |
| Burden and alert-budget review | 3.00 |
| Passive-panel and no-alert comparison | 3.00 |
| Usability and human-factors review | 2.50 |
| Automation-bias, override, and stop controls | 2.00 |
| Access, equity, and privacy review | 3.00 |
| Patient communication and hidden work | 1.50 |
| Reproduction, AI record, decision, and handoff | 1.50 |
| Total | 25.00 |

The reference earns 25.00 of 25.00. A passing score cannot compensate for a failed gate.

The 20 noncompensable gates cover:

1. checkpoint identity;
2. all 204 nested immutable rows;
3. all six evidence candidates;
4. rejection and exclusion of `0.20`;
5. synthetic-only workflow data;
6. complete task analysis;
7. roles, timing, handoffs, and pause rights;
8. burden metrics;
9. repeat and unavailable states;
10. correct interaction interpretation;
11. the less interruptive alternative;
12. no alert;
13. usability and human factors;
14. automation-bias and override controls;
15. language, disability access, and patient communication;
16. equity support and suppression;
17. privacy and minimization;
18. a human recommendation and stop conditions;
19. reproduction and AI accountability; and
20. progression and authority.

Progression requires an allowed disposition, all gates, a complete record set, a protected Module 05 handoff, and every authority prohibition. The reference is `continue with conditions`.

## 16. Common errors, failure modes, and instructor interventions

| Error | Why it matters | Instructor response |
|---|---|---|
| Treating `0.03` as selected or clinically accepted | converts a sandbox fixture into an unauthorized threshold | stop progression and restore the threshold role |
| Using `0.20` in the design comparison | promotes a rejected mechanics fixture | remove it and audit the source chain |
| Combining NHANES flags with synthetic cards | mixes sources and denominators | require a source-denominator table |
| Calling 116 cards a local burden estimate | synthetic script is not local observation | rewrite the claim and state the needed local evidence |
| Calling a dismissal fatigue, misuse, or poor care | assigns motive and quality without evidence | retain the interaction state and remove the inference |
| Treating no card as low risk | hides unavailable, suppressed, and below-candidate states | require explicit reason codes |
| Imputing missing, stale, or inconsistent input | creates false certainty at the decision moment | leave the score blank and route the state to its owner |
| Ignoring repeat cards | hides exposure and hidden work | count repeats by patient and threshold |
| Calling passive panel zero burden | zero scripted interruption is not zero attention or work | report cards, task minutes, sessions, repeats, and access work |
| Dropping zero-card candidates | hides transport mismatch | retain all six candidates |
| Filling a suppressed equity rate | invents unsupported evidence | blank the value and restore the support status |
| Merging language or access groups | evades the predeclared support rule | restore groups and request better test evidence |
| Ranking or targeting groups | turns a support audit into an action rule | stop and refer to equity and governance reviewers |
| Allowing an agent to choose the design | removes human accountability | require a named human decision owner |
| Beginning FHIR or CDS Hooks prototyping in Module 04 | skips the workflow decision and starts Module 05 early | finish the 25-point release and protected handoff first |
| Treating a passing validator as clinical approval | confuses package integrity with clinical evidence | restate the authority boundary |

## 17. Accessibility, equity, privacy, and responsible-claim checks

### Accessibility

The learner must review semantic order, headings, labels, equivalent text, contrast, zoom, keyboard operation, target size, timing independence, error recovery, and plain language. The passive panel must not rely on color or force an interaction.

### Language and patient communication

English-language support in the synthetic release does not prove usability. Spanish and other-language candidate-card rates at `0.03` are suppressed. The sandbox must create explicit qualified-language test cases. Machine translation alone is not accepted as the clinical communication route.

Patients must be able to ask questions, decline discussion, request language or disability access, and report a concern without penalty. No record authorizes outreach, testing, diagnosis, treatment, or follow-up.

### Disability access

Screen-reader, low-vision, motor-access, and cognitive-support slices remain unsupported at `0.03`. These labels are test prompts, not diagnoses. Module 05 must test the interface behaviors directly.

### Equity

The predeclared support rule requires at least 30 ready encounters and 10 candidate cards. Unsupported rates are blank. Groups remain separate. No result proves a disparity, fairness, equal reach, equal harm, or safe group-specific action.

### Privacy and minimization

The released patient IDs are Commons synthetic IDs. Source synthetic identifiers are represented by SHA-256 fingerprints. Names, addresses, contacts, and direct identifiers are not released in the Module 04 frame. Synthetic status does not remove privacy, access-control, retention, or misuse review.

### Responsible claims

- A synthetic dismissal is not evidence of fatigue.
- Scripted task minutes are not measured labor or cost.
- A passive panel is not burden free.
- No alert is not proven safe or preferred.
- A threshold is not a clinical action.
- Historical calibration does not prove local utility.
- A passing sandbox will not prove interoperability or safety.
- Curriculum acceptance does not authorize real-patient scoring, clinical use, implementation, or deployment.

## 18. AI and agent policy, required disclosure, and verification

An agent may help with code, deterministic generation, file inventory, comparison tables, prose drafting, consistency checks, and validator execution.

An agent may not:

- change accepted Week 3 evidence;
- refit or retune the model;
- select or accept a clinical threshold;
- choose the final progression decision;
- infer clinician motive, fatigue, trust, misuse, or care quality;
- fill or predict a suppressed equity result;
- combine groups to create support;
- recommend diagnosis, testing, treatment, ordering, outreach, or targeting;
- score a real patient;
- approve silent mode, implementation, production connection, or deployment; or
- sign for a human reviewer.

The AI-use record names tools, human-owned decisions, protected evidence, prohibited agent actions, verification, and remaining human review. Agent-generated code must pass source hashes, deterministic builds, manifests, invariants, learner and reference validation, copied validation, and deliberate failure routes.

The final decision remains human-owned even when every automated check passes.

## 19. Answer key and instructor notes

### Exact release facts

- Synthetic people: 1,000.
- Candidate-frame people: 238.
- Encounter opportunities: 1,200.
- Repeat opportunities: 200.
- Candidate-frame encounters: 288.
- Unavailable inputs: 39.
- Ready candidate-frame encounters: 249.
- Sessions: 120.
- Fictional clinicians: 12.
- Candidate events: 7,200.
- Equity slices: 108.
- Candidate cards: 116, 12, 3, 3, 0, and 0.
- Workflow invariants: 20 of 20 pass.

### Candidate interpretation

At `0.02`, the synthetic script produces 116 cards across 74 sessions, including 16 repeats. At `0.03`, it produces 12 cards across 10 sessions, including one repeat. At `0.04` and `0.05`, it produces three cards. At `0.075` and `0.10`, it produces none.

The `0.03` cards contain 10 scripted views, three acknowledgments, three dismissals, three deferments, one view-only state, two unresolved states, a median scripted response of 87 seconds, and 20.00 task minutes. These are scripted teaching values, not observed behavior or workload.

### Access interpretation

At `0.03`, English-language access has 228 ready encounters and 12 candidate cards, which meets the teaching support rule. Spanish has 13 ready encounters and no cards. Other language has 8 and no cards. Every disability-access, age, source-recorded gender, and BMI candidate-card rate is suppressed. The supported English slice does not resolve any other access question.

### Reference decision

The reference is `continue with conditions`. It advances `panel-t003` for Module 05 mechanics only. The design uses `0.03` as an unaccepted sandbox fixture because it supplies 12 positive synthetic cases without scripted banner interruption. The recommendation retains unavailable states, repeat exposure, access testing, human nonaction, override, stop rights, and all authority limits.

Module 05 receives the complete Module 04 release manifest, exact Checkpoint 01 identity, workflow evidence release, candidate design review, automation-bias controls, access and equity review, stop conditions, 25-point score, and 20 gates.

## 20. Runnable acceptance checks for data, code, links, and expected findings

### Workflow builder

```powershell
python courses/clinical-decision-support/modules/04-alert-burden-human-factors-equity/build_workflow.py --self-check
```

Expected result: 1,000 people, 1,200 opportunities, 7,200 candidate rows, 13 designs, byte-identical builds, and existing-target refusal.

### Workspace builder

```powershell
python courses/clinical-decision-support/modules/04-alert-burden-human-factors-equity/build_workspace.py --self-check
```

Expected result: 285 immutable rows, 204 nested immutable rows, 16 editable records, and 302 assembled files. Learner and reference immutable manifests must match.

### Validator

```powershell
python courses/clinical-decision-support/modules/04-alert-burden-human-factors-equity/validate_workspace.py --self-check
```

Expected result: 2,400 reference checks, 2,284 learner checks, copied validation, and 20 rejected failure routes.

The validator checks:

- all 285 own-manifest rows by path, bytes, and SHA-256;
- all 245 checkpoint candidate rows by path, bytes, and SHA-256;
- all 204 nested immutable rows by path, bytes, and SHA-256;
- the 40-point Week 3 identity and authority boundary;
- the deterministic workflow release and output-manifest digest;
- every threshold, candidate count, design, no-alert row, and `0.20` exclusion;
- every unavailable-state and synthetic flag;
- all 108 equity rows and support suppression;
- all 16 records;
- the exact 25-point score;
- all 20 gates;
- the human recommendation, stop rules, Module 05 handoff, and authority limits; and
- copied validator behavior.

The failure routes reject missing records, immutable mutations, checkpoint-manifest mutations, nested-manifest mutations, missing checkpoint files, task-boundary changes, missing candidates, banner substitution, score changes, failed gates, removed pause rights, failed timing reviews, expanded burden claims, missing usability, automation, or access rows, removed stop conditions, expanded agent authority, expanded Module 05 permission, and deployment permission.

The complete curriculum checker must also verify the exact 21 sections, package file count, workflow counts, score, gates, validation counts, release version, and Module 05 handoff.

## 21. Release status, reviewers, version, and known issues

- Module version: `0.1.0`.
- Commons release: `0.81.0`.
- Status: runnable release candidate for curriculum construction.
- Reference score: 25.00 of 25.00.
- Reference gates: 20 of 20 pass.
- Reference progression: `continue with conditions`.
- Module 05 permission: nonproduction sandbox construction only.
- Accepted clinical threshold: none.
- External Python dependencies: none.

### Reviews required before alpha

- APP-4 faculty owner;
- primary-care or endocrinology clinician;
- clinical informatics reviewer;
- workflow and human-factors reviewer;
- patient and patient-communication reviewer;
- Spanish-language and broader language-access reviewer;
- disability-access and accessibility reviewer;
- equity reviewer;
- privacy and data-stewardship reviewer;
- patient-safety reviewer;
- responsible-AI reviewer; and
- independent reproduction instructor.

### Known issues

- The official section and exact half-term dates remain to be assigned from the published academic calendar.
- The scripted workflow does not estimate local prevalence, burden, staffing, capacity, behavior, utility, safety, or fairness.
- Most `0.03` access and equity rates remain unsupported.
- Named human reviews remain pending before alpha.
- The sandbox design and threshold role are curriculum fixtures, not clinical approvals.

### Module 05 handoff

Module 05 must freeze the complete 302-file Module 04 reference workspace and its release manifest. It must preserve the exact Checkpoint 01 identity, all six unaccepted candidates, the rejected `0.20` fixture, the 25-point score, all 20 gates, `panel-t003`, the unaccepted `0.03` sandbox role, every suppressed equity result, and every authority prohibition.

Module 05 may construct only nonproduction FHIR R4 and CDS Hooks-shaped normal and failure cases for the passive panel. It may not connect to a live system, score a real patient, accept a clinical threshold, display a real alert, start silent-mode evaluation, implement, or deploy.
