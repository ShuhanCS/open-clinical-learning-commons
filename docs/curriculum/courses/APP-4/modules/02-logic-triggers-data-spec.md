# APP-4 Module 02: Decision support logic, triggers, and data

## 1. Module identity, duration, prerequisites, and place in the course

- Module ID: `oclc-app4-02`.
- Module version: `0.1.0`.
- Commons release: `0.78.0`.
- Course: APP-4, Data for Clinical Decision Support.
- Course week: 2 of the seven-module, 7.5-week course.
- Learner time: 16 hours.
- Course points: 20 of the 40-point Week 3 checkpoint.
- Status: runnable release candidate.
- Continuing case: fictional adult general internal medicine and primary care service `CGH-GIM-01`.
- Continuing decision: whether a nonbinding advisory concept may eventually advance from offline sandbox review to a proposal for a locally governed, time-limited silent-mode evaluation.

Module 02 turns the accepted Module 01 purpose into a testable candidate logic and data contract. Learners specify who invokes the service, at what workflow moment, with which event-time information, under which terminology and unit rules, in what branch order, with which suppressions, reason codes, nonactions, stop rights, and failure signals.

The module does not fit a model or accept a clinical threshold. It uses supplied mock scores and an arbitrary `0.20` branch value so learners can test comparisons, equality, suppressions, and delivery failures before historical evidence exists.

### Prerequisites

Learners must have:

1. completed APP-4 Module 01;
2. a passing Module 01 workspace with all 29 immutable source and control files;
3. accepted the difference between public NHANES evidence and fictional synthetic workflow truth;
4. basic ability to inspect CSV, JSON, gzip, and FHIR-shaped records;
5. basic understanding of classification scores, thresholds, missingness, time ordering, joins, and version control from FND-1 and FND-2; and
6. no unresolved use-case problem that would make logic construction premature.

### Course handoff

Module 01 permits logic and input construction only. Module 02 may hand a complete candidate contract to Module 03. Module 03 owns the historical cohort, target, predictors, model, calibration, threshold analysis, temporal validation, later-cycle stress test, and subgroup support.

## 2. Healthcare decision and named audience

### Healthcare decision

The module decision is:

> Is the candidate logic, trigger, input, terminology, trace, and synthetic-test contract complete enough to hand to Module 03 for historical evidence and threshold analysis?

This is a curriculum progression decision. It is not a clinical approval, implementation decision, or deployment decision.

### Named audiences

| Audience | Decision supported |
| --- | --- |
| APP-4 learner team | whether its logic and data contract is complete and internally consistent |
| APP-4 faculty owner | whether the 20-point Module 02 release passes and Module 03 construction may begin |
| Primary-care or endocrinology reviewer | whether candidate eligibility, suppression, lookback, wording, and patient consequences are clinically reviewable |
| Clinical informatics reviewer | whether hook, workflow context, branch order, reason codes, and event-time rules are coherent |
| Interoperability and terminology reviewers | whether FHIR, CDS Hooks, code, unit, value-state, and version contracts are explicit |
| Patient-safety and human-factors reviewers | whether nonaction, silent failure, burden, and stop rights are visible |
| Clinical governance council | whether later evidence may be reviewed without implying authority to use the concept clinically |

The fictional point-of-care user is the clinician responsible for the current adult encounter. The user retains judgment and may take no action.

## 3. Foundation skill being revisited or extended

### FND-1 extension

Module 02 revisits technical foundations through a clinical workflow problem:

- Boolean logic becomes an ordered clinical branch table with explicit exits.
- Sets and uniqueness become request idempotency and duplicate-resource checks.
- Time arithmetic becomes effective time, recorded time, availability time, decision time, lookback, and delivery time.
- Missingness becomes a named no-card state rather than automatic imputation.
- Joins become patient, encounter, condition, observation, organization, and practitioner cardinality tests.
- Type and range checks become code-system, unit, version, enumerated-state, and timestamp contracts.
- Reproducibility becomes a complete generator, runtime, configuration, seed, date, population, encoding, file, row, byte, and hash record.

### FND-2 extension

Module 02 revisits classification foundations without performing model analysis:

- a score and a decision threshold remain distinct objects;
- equality at a threshold must be specified rather than assumed;
- a negative output can result from a score branch, a suppression, invalid context, missing input, or transport failure;
- information available after the decision time cannot enter a score or rule retrospectively;
- a threshold cannot be accepted from code behavior alone; and
- branch tests establish software mechanics, not discrimination, calibration, net benefit, subgroup safety, or clinical usefulness.

### DA-730 use

Learners use visual hierarchy and honest annotation to communicate the branch order, input availability timeline, and upstream duplicate-resource pattern. The visual must separate facts from assumptions and mechanics from clinical evidence.

## 4. Learning outcomes that can be assessed

By the end of Module 02, a learner can:

1. preserve the accepted Module 01 purpose, user, workflow, nonaction, source roles, and authority limits;
2. name one versioned CDS Hooks trigger and the exact required context;
3. express candidate logic as a deterministic ordered table with stable branch and reason identifiers;
4. distinguish a trigger, eligibility check, suppression, score comparison, candidate result, and response-delivery state;
5. specify an event-time input contract for patient, encounter, condition, observation, score, threshold, and response fields;
6. keep effective, recorded, availability, decision, and delivery times separate;
7. document terminology system, version, code, display, unit, value states, missing behavior, and human owner;
8. reproduce a complete 1,000-patient Synthea FHIR release from pinned build inputs;
9. explain why Windows-1252 source normalization to UTF-8 is a portability step rather than evidence cleaning;
10. measure and interpret 11,109 duplicate resource IDs without silently removing them;
11. run and interpret 16 normal, boundary, missing, stale, inconsistent, duplicate, delayed, semantic, version, suppression, unit, context, silent-failure, and missing-score fixtures;
12. locate the first divergent branch from an ordered trace;
13. explain why a missing card is not equivalent to a below-threshold result;
14. label the supplied score and `0.20` value as mechanics-only fixtures;
15. identify the named human owner and stop right for each material failure;
16. write version, invalidation, rollback, and full-rerun rules; and
17. make a bounded `continue`, `continue with conditions`, `revise`, or `refer` progression decision.

## 5. Concept ownership and explicit out-of-scope boundaries

### Module 02 owns

- inheritance of the accepted Module 01 use-case and source boundary;
- candidate `patient-view` hook and version;
- fictional invocation timing and required request context;
- service, user, patient, encounter, and request identity rules;
- ordered candidate branches and reason codes;
- nonaction and clinician-control statements;
- candidate suppression mechanics;
- event-time input availability;
- terminology, units, value states, staleness, missingness, inconsistency, duplicate, and delay behavior;
- complete Synthea synthetic-source provenance and release integrity;
- deterministic Commons workflow and failure fixtures;
- mock score and mock threshold comparison mechanics;
- response delivery and silent-failure detection;
- patient and clinician consequence ownership;
- change control, invalidation, rollback, AI disclosure, and Module 03 handoff; and
- the 20-point use-case and logic component of the Week 3 checkpoint.

### Module 03 owns later

- final historical target definition;
- accepted eligibility and exclusions for model evidence;
- accepted predictor list and information cutoff;
- survey design and weight treatment;
- missing-input treatment for historical evidence;
- transparent model fitting;
- discrimination and calibration;
- candidate clinical threshold analysis;
- decision benefit, alert budget, and missed-case tradeoffs;
- temporal holdout and later-cycle stress testing;
- subgroup support; and
- human threshold acceptance or rejection for later sandbox work.

### Later modules own

- Module 04: alert burden, human factors, workflow, and equity evidence;
- Module 05: nonproduction prototype and failure-mode evaluation;
- Module 06: safety case, monitoring, governance, and embedded ML challenger;
- Module 07: clinician leadership, product brief, and defense.

### Explicitly out of scope

Module 02 must not:

- use real patient, protected, workplace, or local EHR data;
- copy a public NHANES participant row into a synthetic patient;
- fit or tune a model;
- describe a mock score as a prediction;
- estimate, optimize, recommend, select, or accept a clinical threshold;
- call the candidate result a validated clinical alert or recommendation;
- infer clinical correctness from passing fixtures;
- infer local prevalence, workflow fit, reliability, burden, safety, or fairness from Synthea;
- silently deduplicate repeated upstream resources;
- turn missing, stale, delayed, inconsistent, or uninterpretable data into a negative score result;
- diagnose, order, treat, message, or act automatically;
- connect to a live clinical system; or
- authorize implementation or deployment.

## 6. Lesson sequence with estimated learner time

| Lesson | Focus | Hours | Evidence produced |
| ---: | --- | ---: | --- |
| 1 | Reopen the Module 01 decision and immutable chain of custody | 1.0 | inherited-boundary notes in the release brief |
| 2 | Map the fictional workflow to `patient-view` context and nonaction | 1.5 | hook, user, service, patient, encounter, and timing contract |
| 3 | Build ordered branches, exits, suppressions, and reason codes | 2.0 | `logic-specification.csv` |
| 4 | Specify effective, recorded, availability, decision, and delivery time | 2.0 | `input-contract.csv` |
| 5 | Specify terminology, unit, value-state, and version behavior | 1.5 | `terminology-map.csv` and semantic branches |
| 6 | Inspect the complete Synthea release, encoding, hashes, and duplicates | 2.0 | `synthetic-release-interpretation.md` |
| 7 | Design normal, boundary, and failure cases | 2.0 | `trigger-suppression-matrix.csv` |
| 8 | Run the evaluator, compare expected and observed traces, and locate divergence | 2.0 | `rule-test-results.csv` |
| 9 | Map consequences, ownership, change control, invalidation, and rollback | 1.0 | consequence map and change-control record |
| 10 | Assemble, audit, defend, and release the 20-point package | 1.0 | release brief, claims, AI record, and progression decision |
|  | Total | 16.0 | 12 assessed records |

## 7. Authoritative readings and public clinical sources

### Required standards and source readings

Synthea 4.0.0 release:

https://github.com/synthetichealth/synthea/releases/tag/v4.0.0

Pinned Synthea tag commit:

https://github.com/synthetichealth/synthea/commit/0185c09ea9d10a822c6f5f3ef9bdcbcbe960c813

Synthea source and license:

https://github.com/synthetichealth/synthea

CDS Hooks 2.0.1:

https://cds-hooks.hl7.org/

CDS Hooks `patient-view` 1.0:

https://cds-hooks.org/hooks/patient-view/

HL7 FHIR R4:

https://hl7.org/fhir/R4/

FHIR R4 Observation:

https://hl7.org/fhir/R4/observation.html

FHIR R4 Condition:

https://hl7.org/fhir/R4/condition.html

US Core 7.0.0:

https://hl7.org/fhir/us/core/STU7/

ONC SAFER Guide to the Safety of Computerized Clinical Decision Support:

https://www.healthit.gov/topic/safety/safer-guides

LOINC candidate HbA1c concept:

https://loinc.org/4548-4/

LOINC candidate BMI concept:

https://loinc.org/39156-5/

SNOMED CT candidate Type 2 diabetes mellitus concept:

http://snomed.info/id/44054006

UCUM:

https://ucum.org/ucum

### Reading purpose

Learners use Synthea documentation to understand the generator, output, configuration, limits, and license. They use CDS Hooks to define a request and response boundary. They use FHIR R4 and US Core to inspect resource shape and references. They use LOINC, SNOMED CT, and UCUM to identify terminology and unit decisions that require human review. They use SAFER to ask what happens when a rule, input, or response fails.

No reading endorses the use case, clinical input list, 365-day fixture, mock score, `0.20` value, candidate card, or deployment.

## 8. Dataset inventory, provenance, license, and teaching purpose

### Inherited Module 01 evidence

The assembled workspace contains 29 immutable Module 01 files under `inherited/module01/`:

- 9 module control files;
- 4 public-source profile files; and
- 16 complete NHANES XPT releases, deterministically compressed.

These files preserve 34,221,200 raw bytes, 3,149,043 committed gzip bytes, 145,563 component rows, 442 field inventory rows, and zero duplicate `SEQN` rows within file. Their role in Module 02 is chain of custody and source-boundary inheritance. Learners do not fit a model with them here.

### Synthetic build inputs

| Input | Version | Bytes | SHA-256 | Committed? |
| --- | --- | ---: | --- | --- |
| Synthea runnable JAR | 4.0.0 | 201,164,144 | `ed43c20ad40ba5c3bc724503a5af032715fe3c491620b766148e7c2361e6ecc1` | no |
| Eclipse Temurin portable JRE | 17.0.20.1+1 | 43,780,109 | `bc21a93923103cdaac93ee337b0ae4365e739fde36df823dd456bc67c8a9d352` | no |

The JAR is Apache-2.0 licensed. The runtime uses its published Temurin license terms. They are local build inputs and are not added to the Commons repository.

### Generation contract

| Setting | Accepted value |
| --- | --- |
| Release ID | `CGH-GIM-01-SYNTHETIC-2026-08-31-v1` |
| Synthea version | `4.0.0` |
| Random seed | `7400202` |
| Clinician seed | `7400203` |
| Reference date | `20260831` |
| End date | `20260831` |
| Population | `1000` |
| Age range | `18-89` |
| Geography | `Massachusetts` |
| Only alive at reference date | `true` |
| History | `5 years` |
| Generator threads | `1` |
| Output | `FHIR R4 Bulk Data NDJSON` |
| US Core exporter setting | `7.0.0` |
| Source encoding read on Windows | `Windows-1252` |
| Committed encoding | `UTF-8` |
| Gzip timestamp | `0` |

### Complete committed release

| Measure | Value |
| --- | ---: |
| FHIR files | 25 |
| NDJSON resource files | 24 |
| Bulk Data Parameters files | 1 |
| Resource rows | 811,803 |
| Canonical uncompressed bytes | 1,549,494,665 |
| Committed gzip bytes | 100,178,478 |
| Parse failures | 0 |
| Duplicate IDs within file | 11,109 |

The largest committed file is `Observation.ndjson.gz` at 21,845,732 bytes. No single file approaches GitHub's 100 MB file limit.

### Resource inventory

The release includes AllergyIntolerance, CarePlan, CareTeam, Claim, Condition, Device, DiagnosticReport, DocumentReference, Encounter, ExplanationOfBenefit, ImagingStudy, Immunization, Location, Medication, MedicationAdministration, MedicationRequest, Observation, Organization, Patient, Practitioner, PractitionerRole, Procedure, Provenance, SupplyDelivery, and Parameters.

### Duplicate distribution

| Resource | Rows | Unique IDs | Duplicate IDs |
| --- | ---: | ---: | ---: |
| Location | 3,534 | 705 | 2,829 |
| Organization | 3,464 | 704 | 2,760 |
| Practitioner | 3,464 | 704 | 2,760 |
| PractitionerRole | 3,464 | 704 | 2,760 |
| All other files | 797,877 | 797,877 or no ID for Parameters | 0 |

### Teaching purpose and rights boundary

Synthea supplies synthetic, realistic-looking patient records for teaching. The Commons supplies deterministic fictional workflow truth and failure cases. Neither supplies real local evidence. No protected data, public participant identity, or workplace data enter the release.

## 9. Data dictionary and expected analytic structure

### Synthetic source manifest

`data/synthetic-release/source-manifest.csv` has one row per committed file:

| Field | Meaning |
| --- | --- |
| `relative_path` | path below the synthetic release root |
| `resource_type` | one FHIR resource type or `Parameters` |
| `rows` | parsed JSON resources |
| `unique_ids` | unique nonmissing resource IDs within file |
| `duplicate_ids` | rows beyond the unique ID count |
| `parse_failures` | JSON rows that failed parsing |
| `uncompressed_bytes` | canonical UTF-8 bytes |
| `compressed_bytes` | deterministic gzip bytes |
| `sha256` | SHA-256 of the committed gzip file |

### Commons patient linkage

`data/commons/patient-linkage.csv` links 16 case IDs to 16 stable patient IDs from the full synthetic release. It includes birth date for fixture inspection, release ID, and an explicit synthetic-data label. It contains no NHANES identifiers or values.

### Rule test cases

`data/commons/rule-test-cases.csv` contains:

| Field | Meaning | Allowed reference values |
| --- | --- | --- |
| `case_id` | stable test identifier | `C01` through `C16` |
| `patient_id` | linked synthetic FHIR Patient ID | one accepted ID |
| `encounter_id` | fictional encounter | `CGH-ENC-*` |
| `request_id` | fictional idempotency key | `CGH-REQ-*` |
| `service_id` | service context | `CGH-GIM-01` or deliberate mismatch |
| `hook` | workflow hook | `patient-view` |
| `hook_version` | hook contract version | `1.0` or deliberate `0.9` mismatch |
| `user_id` | synthetic user reference | `PractitionerRole/CGH-GIM-01-PCP` |
| `decision_time` | event-time information cutoff | `2026-08-31T15:00:00Z` |
| `input_state` | bundle readiness | ready, missing, stale, inconsistent, delayed |
| `diabetes_state` | candidate condition state | absent, present, unknown |
| `prior_hba1c_days` | fixture days before decision | 365 or 366 |
| `terminology_state` | semantic state | valid or mismatch |
| `unit_state` | unit state | valid or mismatch |
| `score_fixture` | supplied mechanics value | blank, 0.19, 0.20, or 0.42 |
| `threshold_fixture` | supplied comparison value | 0.20 |
| `duplicate_of` | earlier request if duplicate | blank or `C03` |
| `response_transport` | delivery state | delivered or suppressed |
| `expected_result` | expected top-level mechanics result | no_card, candidate_card, silent_failure |
| `expected_reason` | expected terminal reason | stable reason code |
| `condition_class` | teaching category | 16 distinct classes |

### Expected analytic grain

The rule test grain is one offline request evaluation per case. A branch trace contains one ordered path and one terminal result. Resource-level FHIR rows must not be joined directly into this grain without a documented normalization, time, and cardinality policy.

### Missingness and negative results

Blank, unknown, stale, delayed, inconsistent, or uninterpretable values are not equivalent to absence. A `no_card` result must retain its terminal reason. Only `below_mock_threshold` represents the fixture comparison's negative branch.

## 10. Worked example and instructor walkthrough

### Starting prompt

> If the risk is at least 20 percent, show the diabetes alert.

This prompt is not implementable or clinically defensible. It omits the service, user, hook, encounter, information cutoff, score source, threshold evidence, eligibility, suppressions, missing behavior, terminology, units, idempotency, reason codes, nonaction, delivery monitoring, and human owners. It also calls an arbitrary fixture a risk and an alert.

### Walkthrough

1. Restore the Module 01 purpose: a nonbinding candidate card, not diagnosis or automation.
2. Name the fictional service: `CGH-GIM-01`.
3. Choose one versioned candidate hook: `patient-view` 1.0.
4. Require the clinician user, patient, encounter, request, and decision time.
5. Check whether the service and context are supported before touching clinical inputs.
6. enforce request idempotency.
7. reject missing, stale, delayed, or inconsistent required input without imputation.
8. reject unknown terminology and unit states without coercion.
9. apply candidate suppressions before the score comparison.
10. label the supplied score as a fixture, not a prediction.
11. compare the fixture against the arbitrary mock threshold with an explicit inclusive boundary.
12. separate the candidate decision result from response delivery.
13. preserve a terminal reason and ordered trace for every result.
14. name a human owner and stop right for every material failure.

### Case C02: equality boundary

Case C02 has a mock score of `0.20` and a mock threshold of `0.20`. The branch condition is `score >= threshold`, so the expected mechanics result is `candidate_card`. This establishes the chosen comparison operator in the test harness. It does not establish that `0.20` is clinically meaningful.

### Case C15: silent failure

Case C15 passes service, context, idempotency, input, semantics, suppression, and mock threshold branches. The response transport is then suppressed. The expected result is `silent_failure`, not `no_card` and not a delivered candidate card.

This distinction is central: the clinician sees nothing in both a below-threshold result and a delivery failure, but the system state, patient consequence, operational response, and responsible owner are different.

### Correct reference decision

`continue with conditions` for Module 03 curriculum construction. The complete contract and passing traces permit the next evidence-building module. They do not establish clinical correctness or threshold acceptance.

## 11. Guided practice

### Practice A: classify ten no-card statements

Given ten statements such as “the code was unknown,” “the score was below the fixture,” and “the response was lost,” classify each as context, idempotency, readiness, semantics, suppression, score, or delivery. Require a stable reason code and owner.

### Practice B: draw the event-time line

Place effective, recorded, availability, decision, and delivery times on one line. Move one observation's availability time to five minutes after the decision and explain why the value becomes delayed even if its effective time is earlier.

### Practice C: inspect duplicate-resource cardinality

Use `source-manifest.csv` to calculate duplicate proportions for Location, Organization, Practitioner, and PractitionerRole. Predict what happens to an encounter count if a many-to-many join uses the repeated resources without normalization.

### Practice D: repair an unsafe input contract

Repair this entry: “Use latest HbA1c.” Add code system, code, status, unit, subject, encounter relation, effective time, availability time, lookback, duplicates, missing, inconsistency, owner, and current review status.

### Practice E: reverse one branch

Change the equality comparison from `>=` to `>`. Predict the C02 result, run the evaluator after making the change in a disposable copy, and identify the first divergent branch.

### Practice F: trace absence

Compare C01, C04, C07, C09, C11, C14, C15, and C16. All except C15 end in no card. Explain why their reasons cannot be collapsed into one negative category.

### Practice G: separate mechanics from evidence

For each of the following, label what Module 02 can show and what later evidence is required: branch determinism, model discrimination, calibration, net benefit, local alert burden, subgroup safety, transport reliability, and deployment readiness.

## 12. Independent exercise

### Assignment

Complete the twelve-record Module 02 release for the fictional `CGH-GIM-01` service. Use the immutable source, configuration, linkage, and cases supplied in the learner workspace. Do not replace them, add real data, fit a model, or reinterpret the mock threshold as clinical evidence.

### Required decisions

1. State the progression decision and permitted next action.
2. Preserve or explicitly refer any Module 01 boundary.
3. Define the candidate hook and required context.
4. Define ordered branches, candidate actions, reason codes, nonactions, and owners.
5. Define every input's source, code or field, timing, states, unit, missing behavior, duplicate or delay behavior, owner, and status.
6. Explain the full synthetic release and encoding normalization.
7. Calculate and interpret duplicate-resource counts.
8. Map all 16 cases to expected results and reasons.
9. Run the rule evaluator and interpret every unexpected result.
10. Map patient, clinician, operational, and governance consequences.
11. Define versioning, invalidation, rollback, and full-rerun rules.
12. Bound claims, disclose AI use, and preserve prohibited authority.

### Independent defense questions

1. Why is `patient-view` only a candidate hook for this fictional workflow?
2. Why is information availability different from clinical effective time?
3. Why can a missing card not be treated as a negative prediction?
4. What is the first branch that differs between C01 and C15?
5. Why is C02 useful even though `0.20` has no clinical authority?
6. What harm could silent deduplication cause?
7. What join would be most vulnerable to the repeated Organization and Practitioner rows?
8. Who owns a terminology mismatch?
9. Who owns a delivery failure?
10. What evidence must Module 03 produce before any threshold can be reviewed?
11. What would invalidate this release?
12. What exactly does `continue with conditions` permit?

## 13. Visualization and communication requirements

### Required decision flow

The release brief must show the ordered flow in a form that remains understandable without color:

`service -> context -> idempotency -> input readiness -> semantics -> suppressions -> mock score -> mock threshold -> delivery`

Every terminal exit must retain a stable reason code. A text alternative must explain that the path stops at the first failed condition.

### Required input-availability view

Show effective time, availability time, decision time, and delivery time for at least one ready case and one delayed case. Label assumptions directly. Do not use position or color alone to distinguish available from delayed.

### Required duplicate view

Show rows and unique IDs for the four repeated resource types. Begin the axis at zero, label exact values, and state that duplicates are upstream synthetic-source properties rather than real prevalence findings.

### Communication rules

- Use `candidate_card`, not `alert`, unless discussing the prohibited claim.
- Use `mock score fixture`, not `risk prediction`.
- Use `mock threshold fixture`, not `clinical cutoff`.
- Use `synthetic patient`, not `patient`, when the data class could be ambiguous.
- Put “mechanics only” beside any score comparison.
- Put the terminal reason beside every no-card example.
- Put the responsible human owner beside every failure.
- Provide table or prose equivalents for any diagram.

## 14. Exact submission package and filenames

### Immutable files

The builder supplies 73 immutable files:

- 29 inherited Module 01 files;
- 12 Module 02 control and executable files;
- 29 synthetic release files, including 25 FHIR files and 4 release controls; and
- 3 Commons rule-fixture files.

Do not edit immutable files. Their bytes and SHA-256 identities appear in `release-manifest.csv`.

### Editable assessed records

Submit exactly these twelve files at workspace root:

1. `use-case-logic-release.md`
2. `logic-specification.csv`
3. `input-contract.csv`
4. `trigger-suppression-matrix.csv`
5. `rule-test-results.csv`
6. `terminology-map.csv`
7. `synthetic-release-interpretation.md`
8. `logic-change-control.md`
9. `patient-workflow-consequence-map.csv`
10. `claim-boundary.csv`
11. `ai-use.md`
12. `progression-decision.md`

The assembled workspace contains 86 files: 73 immutable files, 12 assessed records, and one release manifest.

### File rules

- UTF-8 text and LF line endings.
- No personal local paths.
- No `REPLACE` placeholders in a complete submission.
- No copied reference record in a learner starter.
- No real patient, protected, or workplace data.
- No additional file that changes the assessed decision without being named in the release brief.

## 15. Rubric and pass conditions

| Criterion | Full-credit evidence | Points |
| --- | --- | ---: |
| Use-case and logic release | preserves Module 01; names decision, hook, nonaction, mechanics, limits, conditions, and next action | 3 |
| Ordered logic | complete stable branch IDs, priorities, conditions, results, reasons, nonactions, owners, status, and claim limits | 5 |
| Event-time input contract | complete source, semantics, unit, state, cutoff, staleness, missing, duplicate, delay, owner, and review status | 4 |
| Synthetic provenance and data quality | exact build inputs, configuration, encoding, files, rows, bytes, hashes, duplicates, rights, and claim limits | 3 |
| Executable traces | all 16 observed results, reasons, ordered traces, pass states, and mechanics-only interpretations reproduce | 3 |
| Governance and communication | consequence owners, change control, rollback, claims, AI disclosure, and bounded progression are complete | 2 |
| Total |  | 20 |

### Passing threshold

A numeric score of at least 16 of 20 and all twelve noncompensable gates are required. Any gate failure results in `revise` or `refer`, even if the numeric score is higher.

### Excellence indicators

Full-credit work does more than reproduce the reference. It makes branch order easy to audit, distinguishes every time concept, explains rather than hides upstream duplicates, assigns ownership at the point of failure, and states exactly what the evidence does not show.

## 16. Common errors, failure modes, and instructor interventions

| Error | Why it matters | Instructor intervention |
| --- | --- | --- |
| Calling `0.20` a clinical threshold | imports authority that Module 02 cannot earn | stop scoring; require mechanics-only rewrite and claim audit |
| Calling the supplied value a risk prediction | implies a model and performance evidence that do not exist | trace value provenance and relabel every occurrence |
| Treating all no-card results as negative | conceals missingness, suppressions, context errors, and silent failures | require reason-specific counts and compare C01 with C15 |
| Using effective time as availability time | creates information leakage | redraw the event-time line and rerun delayed cases |
| Silently deduplicating provider resources | changes the complete source and hides a cardinality decision | restore source; define a future normalization policy separately |
| Letting unknown terminology pass | risks semantic misclassification | force no-card, name terminology owner, and document mapping review |
| Imputing missing fixture inputs | changes the teaching contract and may conceal failure | restore explicit no-card behavior |
| Showing a second response for a retry | creates burden and inconsistent audit history | add request idempotency and duplicate reason |
| Checking delivery before the candidate decision | cannot distinguish transport failure from logic result | move transport to the final branch and preserve both states |
| Claiming FHIR conformance from valid JSON | structure is not profile or semantic validation | narrow claim and name required conformance tooling |
| Claiming Synthea proves local workflow fit | synthetic generation is not local evidence | return to source-role map and governance owner |
| Allowing AI to choose clinical content | removes accountable human judgment | mark revise and reconstruct decisions with named reviewers |

## 17. Accessibility, equity, privacy, and responsible-claim checks

### Accessibility

- Every diagram has a text alternative.
- Branch meaning does not depend on color alone.
- Tables have descriptive headers and stable reading order.
- File names and headings identify the decision, not the visual style.
- Exact values accompany graphical marks.
- Candidate-card language is concise and avoids unexplained abbreviations.
- A screen-reader user can determine why each case ended.

### Equity

Module 02 does not estimate subgroup performance. Learners must still identify where harm could enter:

- missing or delayed information may differ by care setting or access;
- terminology and unit mismatches may cluster by source system;
- repeated cards may burden clinicians and patients unevenly;
- prior-testing suppressions may reflect unequal access to testing;
- synthetic demographic realism does not establish representativeness; and
- a future model or threshold must be evaluated with explicit subgroup support and consequence analysis.

Do not calculate a fairness metric from the mock scores. Record the future equity questions and accountable owners instead.

### Privacy

- Only public NHANES files and synthetic FHIR or Commons rows are allowed.
- No real patient, local EHR, employee, or workplace data may enter the workspace.
- No public NHANES row may be copied into a synthetic patient.
- Synthetic identifiers must not be linked to real identities.
- Local cache paths and usernames must not appear in released logs.

### Responsible claims

Every result must be classified as one of:

- exact source fact;
- deterministic fixture behavior;
- candidate clinical assumption pending human review;
- evidence requirement for a later module; or
- prohibited claim.

## 18. AI and agent policy, required disclosure, and verification

### Permitted assistance

AI or agents may help:

- inspect documented schemas and source manifests;
- draft code that is independently run and checked;
- enumerate edge cases;
- compare expected and observed traces;
- improve table structure or prose clarity; and
- identify missing fields or inconsistent labels.

### Human-only decisions

AI or agents may not decide:

- clinical purpose or intended use;
- hook suitability for a real workflow;
- eligibility, exclusions, clinical input meaning, or suppression policy;
- target, predictors, model, calibration, or threshold;
- candidate-card wording or patient consequence;
- progression approval;
- implementation or deployment; or
- clinical action.

### Required disclosure

`ai-use.md` must name:

1. tools used;
2. tasks assisted;
3. human-owned decisions;
4. agent authority limits;
5. exact independent checks;
6. prohibited-data check; and
7. known limitations.

### Verification rule

Generated code or prose is not accepted because it looks complete. The learner must run the release verifier, fixture verifier, rule evaluator, workspace validator, and full curriculum checks. A human must inspect clinical, terminology, accessibility, safety, and progression statements.

## 19. Answer key and instructor notes

### Reference branch order

1. supported service;
2. supported hook, hook version, and user;
3. first request rather than duplicate;
4. ready event-time inputs;
5. valid terminology and units;
6. no known-diabetes candidate suppression;
7. no recent-HbA1c candidate suppression;
8. mock score present;
9. score below or at-or-above mock threshold; and
10. candidate response delivered or silently failed.

### Reference case results

| Case | Result | Reason |
| --- | --- | --- |
| C01 | no_card | below_mock_threshold |
| C02 | candidate_card | at_or_above_mock_threshold |
| C03 | candidate_card | at_or_above_mock_threshold |
| C04 | no_card | required_input_missing |
| C05 | no_card | required_input_stale |
| C06 | no_card | input_inconsistent |
| C07 | no_card | duplicate_request |
| C08 | no_card | required_input_delayed |
| C09 | no_card | terminology_mismatch |
| C10 | no_card | hook_version_mismatch |
| C11 | no_card | recent_hba1c_suppression |
| C12 | no_card | known_diabetes_suppression |
| C13 | no_card | unit_mismatch |
| C14 | no_card | unsupported_service |
| C15 | silent_failure | candidate_response_not_delivered |
| C16 | no_card | score_fixture_missing |

### Reference source findings

- 25 complete committed FHIR files.
- 811,803 parsed resource rows.
- 1,549,494,665 canonical uncompressed bytes.
- 100,178,478 compressed bytes.
- zero parse failures.
- 11,109 duplicate IDs, all in four provider or organization resource files.
- 16 stable linked cases.
- 16 distinct condition classes.
- three top-level result states: `no_card`, `candidate_card`, and `silent_failure`.

### Reference progression

`continue with conditions` is the strongest defensible decision. The package is complete enough for Module 03 construction. Human clinical, interoperability, terminology, human-factors, safety, privacy, accessibility, responsible-AI, and independent-reproduction reviews remain open.

### Instructor stop points

Stop and require revision if a learner:

- treats the mock threshold as evidence;
- collapses failure reasons;
- changes immutable source bytes;
- hides duplicate counts;
- uses real data;
- claims clinical correctness or local validity;
- omits a responsible owner or stop right; or
- permits real-patient scoring, clinical alerting, implementation, or deployment.

## 20. Runnable acceptance checks for data, code, links, and expected findings

### Source release checks

```powershell
python generate_synthetic_release.py --verify
```

Required result:

- 25 resource files;
- 811,803 resource rows;
- 100,178,478 compressed bytes;
- exact file hashes;
- exact within-file duplicate counts; and
- zero parse failures.

### Commons fixture checks

```powershell
python build_logic_fixtures.py --verify
python evaluate_rules.py --self-check
```

Required result:

- 16 linked synthetic patients;
- 16 rule cases;
- 16 distinct condition classes;
- every expected result and reason passes; and
- no score is generated by a model.

### Workspace checks

```powershell
python build_workspace.py --self-check
python validate_workspace.py --self-check
```

Required result:

- 73 immutable manifest rows;
- 12 editable assessed records;
- 86 assembled files;
- byte-identical reference manifests across two builds;
- complete and starter modes pass;
- mutated immutable source fails;
- placeholder in complete package fails;
- copied reference answer in starter fails;
- deployment authority fails;
- clinical-threshold authority fails; and
- missing assessed evidence fails.

### Manual checks

1. Open the FHIR Bulk Data Parameters resource and confirm it names every NDJSON type.
2. Inspect one Unicode provider name after UTF-8 normalization.
3. Confirm the four duplicate-resource counts from the source manifest.
4. Trace C02, C07, C11, and C15 by hand.
5. Compare the manual trace with `rule-test-results.csv`.
6. Confirm all URLs use complete visible paths.
7. Confirm no personal local path or real identifier appears.
8. Confirm every clinical or workflow assumption names a human reviewer.

### Full curriculum regression

Run the repository's complete curriculum checker after Module 02 package checks. A Module 02 pass cannot override a failed course architecture, calendar, checkpoint, source, or earlier-module check.

## 21. Release status, reviewers, version, and known issues

### Release

- Module version: `0.1.0`.
- Commons version: `0.78.0`.
- Status: runnable release candidate.
- Reference progression: `continue with conditions`.
- Next construction unit: APP-4 Module 03, Evidence, calibration, and validation.

### Required reviewers before alpha

- APP-4 faculty owner;
- primary-care or endocrinology clinician;
- clinical informatician;
- CDS Hooks and FHIR interoperability reviewer;
- terminology and unit reviewer;
- NHANES survey-methods reviewer for the Module 03 handoff;
- human-factors reviewer;
- patient-safety reviewer;
- patient-access or patient-partner reviewer;
- privacy reviewer;
- accessibility reviewer;
- responsible-AI reviewer; and
- independent reproducer.

### Known issues and open decisions

1. `patient-view` is a candidate teaching hook; fictional invocation timing does not prove local workflow suitability.
2. The known-diabetes concept, status rule, and concept set require clinical and terminology review.
3. The 365-day prior-HbA1c lookback is a fixture, not accepted clinical policy.
4. BMI and other future predictors remain candidates for Module 03 rather than accepted inputs.
5. The full release preserves 11,109 repeated provider and organization IDs; Module 03 must define a separate normalization policy before joining those resources.
6. Synthea output is synthetic and does not establish local prevalence, reliability, workflow fit, or safety.
7. FHIR JSON parsing does not prove profile, terminology, or semantic conformance.
8. The score fixtures and `0.20` value cannot be carried into Module 03 as evidence.
9. Two clean generations produce manifest SHA-256 `0d3c4c11e5ab29284f312d76413f8e005fb957226039d324912f80af93dcf3c0`; any future generator or environment change requires a new semantic-version decision.
10. Official course dates, named reviewers, and faculty acceptance remain pending.
11. No clinical use, real-patient scoring, implementation, or deployment is authorized.
