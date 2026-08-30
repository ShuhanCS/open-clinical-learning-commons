# FND-1 Module 03: Cohorts and analytic tables

## 1. Module identity and place in the course

- Course: FND-1 Healthcare Data Foundations.
- Module: 03 of 07.
- Instructional week: 3.
- Learner workload: 16.5 hours.
- Prerequisites: accepted or conditionally accepted Modules 01 and 02.
- Module version: 0.1.0.
- Commons release: 0.30.0.
- Status: runnable release candidate.
- Decision owner: senior clinical data analyst.
- Core source: accepted Module 02 SQLite release.
- Source archive: pinned Synthea April 2020 CSV sample.
- Assessment role: 25-percent SQL cohort component of the cumulative 40-percent Week 3 checkpoint.
- Handoff: frozen cohort definition and one-row-per-person analytic-table contract for Module 04.

Module 03 turns an explicit clinical-data question into tested SQL. The learner selects one index acute-care encounter for each eligible adult synthetic patient, preserves the complete source-to-cohort flow, builds one analytic row per person, and proves that every count and denominator reconciles.

The module asks:

> Does the tested SQL implement the declared adult acute-care cohort and preserve one transparent denominator at every step?

The answer is a versioned data contract, not a clinical conclusion.

### Starting condition

The Module 02 source is immutable:

- archive SHA-256 `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a`;
- 16 source tables;
- 471,836 source rows;
- 1,171 patients;
- 53,346 encounters;
- 299,697 observations;
- zero foreign-key failures; and
- SQLite integrity `ok`.

### Ending condition

The learner releases:

- written cohort specification;
- written analytic-table specification;
- four readable SQL files;
- 1,048 eligible-event rows;
- 374 selected index rows;
- 374 analytic-table rows;
- four-step cohort flow;
- exact data dictionary;
- machine-readable query checks;
- source and transformation records;
- clean reproduction result;
- AI-use record;
- assessment evidence; and
- `accept`, `accept with conditions`, `revise`, or `refer` disposition.

## 2. Technical decision and named audience

### Decision owner

The senior clinical data analyst owns the release decision. The instructor may serve in this role for the teaching release.

### Decision

The owner decides whether the SQL cohort and analytic table match the declared population, index event, time windows, grain, and denominators closely enough to freeze them for Checkpoint 1 and pass them to Module 04.

### Dispositions

| Disposition | Meaning | Next action |
|---|---|---|
| `accept` | Definition, SQL, flow, table, and checks agree without a material condition. | Freeze version 0.1.0 and assemble Checkpoint 1. |
| `accept with conditions` | Blocking technical gates pass, but a bounded documentation or accessibility condition remains. | Record condition, owner, and due date before Module 04 uses the table. |
| `revise` | Eligibility, index selection, window, grain, field, denominator, or query evidence is incorrect or incomplete. | Correct SQL and regenerate every dependent artifact. |
| `refer` | Source integrity, privacy, rights, security, or academic-integrity concern needs another authority. | Stop release and preserve evidence for review. |

### Primary audience

The primary learner is a clinician, researcher, analyst, or quality professional learning how a written population definition becomes reproducible SQL rather than an informal filter.

### Secondary audiences

- Module 04 data-quality lead;
- clinical informatician checking meaning;
- data engineer checking joins and grain;
- instructor checking SQL competency;
- reviewer checking denominators;
- accessibility reviewer;
- privacy and AI reviewer; and
- second analyst reproducing the cohort.

### Decision evidence

The decision uses:

1. immutable Module 02 source identity;
2. explicit population and index rules;
3. ordered inclusion and exclusion flow;
4. readable common table expressions;
5. deterministic tie-breaking;
6. one-row-per-person proof;
7. lookback and follow-up calculations;
8. query checks;
9. exact expected counts;
10. field-level dictionary;
11. transformation record;
12. independent reproduction; and
13. AI verification.

## 3. Foundation skill and handoff

### Foundation skill

The learner converts a narrative cohort definition into an executable, tested, versioned data transformation with conserved counts.

### Skills revisited

- Module 01 repository, version, reproduction, and AI-accountability practices;
- Module 02 table grain, keys, joins, optionality, provenance, and read-only SQL; and
- source minimization through selected output fields.

### New skills

- index-event logic;
- eligibility at an event date;
- one index per person;
- deterministic row ranking;
- lookback and follow-up windows;
- inner and left join choice;
- event-to-person aggregation;
- cohort-flow conservation;
- numerator-denominator checks;
- leakage awareness;
- analytic-table grain; and
- query tests as release evidence.

### Handoff to Checkpoint 1

Checkpoint 1 receives the accepted Module 01 setup state, Module 02 relational release, and Module 03 cohort release. The 15-percent setup and 25-percent cohort components remain separately scored inside one cumulative 40-percent package.

### Handoff to Module 04

Module 04 receives the 374-row analytic table unchanged as its accepted clean baseline. Module 04 creates a separate, deterministic defect release. It does not silently edit the accepted Module 03 artifact.

## 4. Assessable outcomes

The learner can:

1. state the source population and its grain;
2. define the acute encounter classes;
3. define an inclusive index period;
4. calculate completed age at event date;
5. distinguish event-level eligibility from person-level inclusion;
6. identify patients with no qualifying event;
7. identify patients with only minor qualifying events;
8. preserve all eligible event rows before index selection;
9. rank eligible events within person;
10. select one deterministic first index event;
11. explain tie-breaking by start timestamp and encounter ID;
12. define a 365-day pre-index lookback;
13. exclude the index event from history counts;
14. define a 30-day next-encounter window from index stop;
15. define a 90-day acute-return window from index stop;
16. define death within 90 days with endpoint precedence;
17. prove source coverage through the 90-day window;
18. distinguish no recorded encounter from no care;
19. use left joins without dropping patients with no follow-up row;
20. detect join multiplication;
21. build one analytic row per patient;
22. preserve exact person denominators;
23. reconcile cohort-flow exclusions and remaining counts;
24. validate null keys, index dates, ages, windows, and outcome flags;
25. create a data dictionary for every analytic field;
26. state which fields are pre-index, index, post-index, or metadata;
27. identify post-index fields that must not become baseline predictors;
28. reproduce all outputs from the Module 02 database;
29. record transformations and AI assistance; and
30. make a bounded readiness disposition.

## 5. Concept ownership and out-of-scope boundaries

### Module 03 owns

- adult acute-care cohort definition;
- index-period eligibility;
- age-at-index rule;
- first eligible index event;
- deterministic tie-breaking;
- source-to-cohort flow;
- 365-day history counts;
- 30-day next state;
- 90-day acute return and death flags;
- follow-up coverage flag;
- one-row-per-person analytic table;
- field dictionary;
- query checks;
- provenance and transformation records; and
- cohort release decision.

### Out of scope

- correcting source defects;
- deleting extreme or inconvenient values;
- missing-data imputation;
- data-quality severity scoring;
- descriptive clinical estimates;
- inferential statistics;
- regression;
- prediction;
- machine learning;
- causal adjustment;
- risk adjustment;
- visual storytelling;
- intervention recommendation;
- real patient inference; and
- production cohort deployment.

### Deliberate boundary

The analytic table includes post-index outcome fields for later descriptive teaching. Those fields are explicitly classified as post-index and cannot be used as baseline predictors. FND-2 owns formal modeling and leakage evaluation.

## 6. Lesson sequence and learner time

| Block | Activity | Hours | Evidence |
|---:|---|---:|---|
| 1 | Question, population, index, and time-zero contract | 1.50 | Written cohort specification. |
| 2 | Eligible-event SQL and completed-age calculation | 2.00 | 1,048 eligible rows and checks. |
| 3 | Deterministic first index event | 2.00 | 374 one-person index rows. |
| 4 | Cohort-flow construction and conservation | 1.50 | Four-step flow. |
| 5 | Lookback features and join-multiplication controls | 2.25 | Pre-index counts and grain checks. |
| 6 | Thirty-day and ninety-day follow-up | 2.25 | Next state, return, death, endpoint, coverage. |
| 7 | Analytic-table specification and dictionary | 2.00 | 29-field contract and dictionary. |
| 8 | Validation, reproduction, AI verification, and handoff | 3.00 | Query checks, records, disposition. |
| Total |  | 16.50 |  |

### Pacing rule

Index selection is frozen before follow-up fields are built. Learners may not look at the outcome to choose the index event.

## 7. Readings and authoritative sources

### Required project sources

- FND-1 course specification.
- Module 02 specification, schema, manifest, dictionary, and release record.
- Synthea CSV dictionary: https://github.com/synthetichealth/synthea/wiki/CSV-File-Data-Dictionary
- Pinned archive: https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip
- SQLite window functions: https://www.sqlite.org/windowfunctions.html
- SQLite date/time functions: https://www.sqlite.org/lang_datefunc.html
- SQLite WITH clause: https://www.sqlite.org/lang_with.html
- SQLite SELECT: https://www.sqlite.org/lang_select.html

### Reading questions

- What is the difference between an eligible event and an included patient?
- Why is age calculated at the event rather than from calendar year alone?
- What happens when one patient has multiple eligible events?
- Why does `ROW_NUMBER` need a tie-break field?
- Why do history joins multiply rows?
- Why is index stop, not index start, used for follow-up?
- Why must no recorded follow-up remain an explicit state?
- Which analytic fields occur after time zero?

## 8. Dataset inventory, provenance, rights, and teaching purpose

### Upstream release

Module 03 uses the Module 02 SQLite database and does not download or transform another source release.

### Required upstream tables

| Table | Upstream rows | Module 03 use |
|---|---:|---|
| patients | 1,171 | birth, death, gender, race, ethnicity, person denominator |
| encounters | 53,346 | eligibility, index, history, next encounter, acute return |
| conditions | 8,376 | pre-index condition count |
| medications | 42,989 | pre-index medication count |

Other Module 02 tables remain available but are not joined into the version 0.1.0 analytic table because the declared decision does not need them.

### Rights

Upstream Synthea source and generator: Apache-2.0.

Commons code: MIT.

Commons documentation: CC-BY-4.0.

### Synthetic-data boundary

All people, encounters, conditions, medications, deaths, and outcomes are synthetic. The cohort demonstrates technical definition and reproducibility only.

## 9. Cohort and analytic-table structure

### Source population

All 1,171 synthetic patients in Module 02.

### Qualifying acute event

An encounter qualifies when:

- `encounterclass` is `emergency` or `inpatient`;
- encounter start is from 2015-01-01 00:00:00 UTC through 2019-12-31 23:59:59 UTC; and
- the patient is at least 18 completed years old at encounter start.

### Index selection

For each patient, order eligible events by:

1. encounter start ascending; and
2. encounter ID ascending.

The first row is the index event.

### Exact flow

| Step | Starting | Excluded | Remaining | Rule |
|---:|---:|---:|---:|---|
| 1 | 1,171 | 0 | 1,171 | All source patients. |
| 2 | 1,171 | 690 | 481 | Has emergency or inpatient encounter in index period. |
| 3 | 481 | 107 | 374 | Has at least one qualifying event at age 18 or older. |
| 4 | 374 | 0 | 374 | Select first eligible event per patient. |

Supporting event facts:

- 1,243 emergency or inpatient event rows in the index period;
- 687 emergency rows;
- 556 inpatient rows;
- 1,048 adult-eligible event rows; and
- 674 eligible non-index event rows after one index is selected per person.

### Lookback

The 365-day lookback begins exactly 365 elapsed days before index start and ends immediately before index start.

Count:

- all encounters;
- emergency or inpatient encounters;
- condition rows with start in the window; and
- medication rows with start in the window.

The index encounter is excluded.

### Thirty-day next state

Find the first different encounter starting after index stop and no more than 30 elapsed days later.

Map:

| Source class | State |
|---|---|
| ambulatory, outpatient, wellness | Scheduled care |
| urgentcare | Urgent care |
| emergency, inpatient | Acute return |
| no qualifying row | No encounter recorded |

### Ninety-day fields

- `acute_return_90d`: any emergency or inpatient encounter starting after index stop and no more than 90 days later.
- `death_90d`: synthetic death date after index stop date and no more than 90 days later.
- `endpoint_90d`: death first, otherwise acute return, otherwise no acute return.
- `followup_90d_complete`: source encounter coverage extends through index stop plus 90 days.

### Analytic-table grain

Exactly one row per included synthetic patient and selected index event.

### Analytic fields

| Field | Timing | Meaning |
|---|---|---|
| patient_id | key | Synthetic patient ID. |
| birth_date | source | Synthetic birth date. |
| death_date | source | Synthetic death date or null. |
| age_at_index | index | Completed age. |
| gender | source | Synthea source gender value. |
| race | source | Synthea race value. |
| ethnicity | source | Synthea ethnicity value. |
| index_encounter_id | key | Selected encounter ID. |
| index_start | index | Source timestamp. |
| index_stop | index | Source timestamp. |
| index_class | index | `emergency` or `inpatient`. |
| index_code | index | Source encounter code. |
| index_description | index | Source description. |
| index_reason_code | index | Optional source reason code. |
| index_reason_description | index | Optional reason description. |
| prior_365d_encounter_count | pre-index | All prior encounters in lookback. |
| prior_365d_acute_count | pre-index | Prior emergency/inpatient encounters. |
| prior_365d_condition_count | pre-index | Condition rows in lookback. |
| prior_365d_medication_count | pre-index | Medication rows in lookback. |
| next_30d_state | post-index | First next-state group or explicit absence. |
| next_30d_encounter_id | post-index | Source encounter ID or null. |
| next_30d_start | post-index | Source timestamp or null. |
| next_30d_days_after_index_stop | post-index | Elapsed days or null. |
| acute_return_90d | post-index | 0/1 flag. |
| death_90d | post-index | 0/1 flag. |
| endpoint_90d | post-index | Mutually exclusive outcome label. |
| followup_90d_complete | metadata | 0/1 source-coverage flag. |
| source_release | metadata | `synthea-csv-apr2020`. |
| cohort_definition_version | metadata | `0.1.0`. |

## 10. Worked example and instructor walkthrough

### Worked sequence

1. Count all patients: 1,171.
2. Identify 1,243 acute event rows in the index window.
3. Count 481 patients represented by those rows.
4. Calculate completed age at each event.
5. Retain 1,048 adult event rows for 374 patients.
6. Rank within patient and retain rank 1.
7. Verify 374 distinct patients and 374 distinct index encounters.
8. Calculate pre-index counts without joining all event tables at once.
9. Find the first post-index encounter within 30 days.
10. Calculate any acute return within 90 days.
11. calculate death within 90 days with precedence.
12. Check that source coverage reaches every 90-day endpoint.
13. Produce one analytic row per person.
14. Reconcile all counts.

### Join-multiplication example

Joining encounters, conditions, and medications directly before aggregation can create encounter-by-condition-by-medication products. The reference SQL aggregates each history table to one row per index patient first, then joins those summaries.

### Worked interpretation

Supported:

> The SQL reproducibly selects 374 adult synthetic patients with one first emergency or inpatient encounter in the declared period.

Unsupported:

> The cohort estimates acute-care use or outcomes in a real population.

## 11. Guided practice

### Practice 1: Age edge cases

Compare a birthday before, on, and after the index month/day. Explain the subtraction used for completed years.

### Practice 2: Event versus patient count

Explain why 1,048 eligible rows become 374 patients and why `COUNT(*)` cannot replace `COUNT(DISTINCT patient)`.

### Practice 3: Tie-breaking

Create two safe mock events at the same timestamp. Show why encounter ID produces deterministic selection.

### Practice 4: Inner versus left join

Show how an inner join to follow-up encounters would drop people with no recorded next encounter.

### Practice 5: Lookback multiplication

Compare a direct multi-table join with separately aggregated history CTEs.

### Practice 6: Window boundaries

Test events exactly at index stop, just after stop, at 30 days, after 30 days, at 90 days, and after 90 days.

### Practice 7: Conservation

Confirm 690 + 107 + 374 = 1,171 and 374 index rows = 374 analytic rows.

### Practice 8: Leakage labels

Classify every analytic field as source, pre-index, index, post-index, or metadata.

### Practice 9: AI verification

Verify one suggested age, window, join, ranking, or denominator rule against SQL output and authoritative SQLite behavior.

## 12. Independent exercise

The learner independently completes and explains:

- eligible-event SQL;
- index-cohort SQL;
- analytic-table SQL;
- validation SQL;
- cohort flow;
- data dictionary;
- transformation record;
- reproduction record;
- AI-use record; and
- release disposition.

The learner may not copy the reference cohort CSV as a substitute for running SQL.

## 13. Visualization or communication requirements

### Required communication

- cohort specification;
- four-step accessible cohort-flow table;
- analytic-table specification;
- field dictionary;
- query-check registry;
- transformation record;
- reproduction record; and
- technical handoff recommendation.

### Visualization

No chart is required. Cohort flow is represented as an exact table because conservation and exclusion reasons matter more than visual decoration.

If an optional flow diagram is added, the exact table remains required and the diagram cannot encode widths that fail conservation.

## 14. Exact submission package

```text
module-03-submission/
  VERSION
  README.md
  cohort-spec.md
  table-spec.md
  data-dictionary.csv
  source-record.yml
  transformation-record.md
  reproducibility-check.md
  ai-use.md
  sql/
    01-eligible-events.sql
    02-index-cohort.sql
    03-analytic-table.sql
    04-validation.sql
  outputs/
    eligible-events.csv
    index-cohort.csv
    analytic-table.csv
    cohort-flow.csv
    query-checks.csv
```

Required tag: `fnd1-cohort-v0.1.0`.

The upstream SQLite database is rebuilt from Module 02 and is not duplicated in the Module 03 submission.

The runnable package includes `learner-template/` with the exact document and SQL skeleton. The output directory is absent until the learner runs the protected builder against their own four SQL files.

## 15. Rubric and pass conditions

| Criterion | Points |
|---|---:|
| Written cohort definition and time zero | 20 |
| Eligible-event and deterministic index SQL | 20 |
| Analytic-table grain, windows, and fields | 25 |
| Flow, denominators, and query checks | 20 |
| Reproduction, provenance, and transformation record | 10 |
| Accessibility and AI accountability | 5 |
| Total | 100 |

### Pass threshold

At least 80 points.

### Noncompensable gates

- exact upstream source;
- eligibility definition;
- one index per person;
- one analytic row per person;
- cohort-flow conservation;
- window boundaries;
- no join multiplication;
- follow-up coverage;
- post-index leakage labeling;
- reproducibility;
- AI disclosure; and
- accept or accept with conditions disposition.

## 16. Common failures and instructor interventions

| Failure | Intervention | Required evidence |
|---|---|---|
| Counts events as people | Compare `COUNT(*)` with distinct patient count. | 1,048 events and 374 people. |
| Uses year difference for age | Apply month/day correction. | Completed age tests pass. |
| Selects first acute event before adult filter | Filter eligible adult events before ranking. | 374 correct index rows. |
| Ranking lacks tie-breaker | Add encounter ID after start. | Deterministic rerun. |
| Includes index in lookback | Use start strictly before index start. | History boundary checks pass. |
| Uses inner follow-up join | Restore left join or correlated summary. | No-follow-up people retained. |
| Directly joins multiple event tables | Aggregate each to person-index grain first. | No row multiplication. |
| Treats no recorded encounter as no care | Correct label and limit. | Explicit absence wording. |
| Counts death and acute return as mutually exclusive flags | Keep separate flags; apply precedence only to endpoint. | Flags and endpoint reconcile. |
| Uses post-index field as baseline feature | Label timing and remove from baseline set. | Leakage gate passes. |
| Edits output CSV manually | Rebuild from SQL. | Byte-for-byte reproduction. |
| Defines a clinical benchmark | Remove unsupported interpretation. | Synthetic boundary passes. |

## 17. Accessibility, equity, privacy, and claim checks

### Accessibility

- SQL uses named CTEs and one purpose per block;
- flow is an exact text table;
- field dictionary is machine readable;
- all status values are text;
- commands are copyable;
- no evidence relies on color; and
- an accessible SQL client is permitted.

### Equity

Learners receive the same upstream database build and expected source facts. Technical clinics support SQL syntax and environment access without changing the final evidence standard.

### Privacy

The source is synthetic. Direct-like identity fields not needed for cohort logic are excluded from outputs. No workplace or real patient data may replace the source.

### Claims

- Counts describe this synthetic archive only.
- No encounter recorded is not no care.
- Death and return flags are generator-derived.
- The cohort is not representative.
- No rate, quality, effectiveness, or causal claim is supported.
- Cohort acceptance is a technical data decision.

## 18. AI policy, disclosure, and verification

Permitted uses include SQL explanation, test suggestions, join diagnosis, and documentation editing.

Prohibited uses include fabricated output, hidden source sharing, changed expected values, copied SQL without understanding, protected data, credentials, and unsupported clinical interpretation.

For each material use, record:

- date;
- tool and model;
- purpose;
- data shared;
- advice used;
- human verification;
- accepted, changed, or rejected decision; and
- affected file or query.

At least one material SQL or cohort claim is verified against source rows, independent SQL, validator evidence, or official SQLite documentation.

## 19. Answer key and instructor materials

### Reference counts

- source patients: 1,171;
- source encounters: 53,346;
- acute rows in index period: 1,243;
- emergency rows in period: 687;
- inpatient rows in period: 556;
- patients with any acute row: 481;
- patients without acute row: 690;
- patients with only minor acute rows: 107;
- adult eligible event rows: 1,048;
- included adults: 374;
- eligible non-index rows: 674;
- index emergency: 314;
- index inpatient: 60;
- next state no encounter: 263;
- next state scheduled care: 92;
- next state urgent care: 4;
- next state acute return: 15;
- any acute return within 90 days: 36;
- death within 90 days: 8;
- no acute-return endpoint: 330.

### Review order

1. verify Module 02 fingerprint and schema;
2. run eligible events;
3. inspect flow;
4. run index selection;
5. prove uniqueness;
6. run analytic build;
7. inspect timing categories;
8. run validation SQL and Python validator;
9. reproduce in a new target;
10. score and record disposition.

## 20. Runnable acceptance checks

The release validator must check:

1. upstream archive fingerprint;
2. upstream logical table facts;
3. four SQL files exist;
4. five output files exist;
5. exact output headers;
6. exact row counts;
7. exact output fingerprints;
8. 1,171 source patients;
9. 1,243 acute-period events;
10. 481 candidate patients;
11. 690 no-acute exclusions;
12. 107 minor-only exclusions;
13. 1,048 adult eligible events;
14. 374 included patients;
15. 674 non-index eligible events;
16. one index per person;
17. unique index encounter;
18. completed age at least 18;
19. index dates within bounds;
20. classes restricted to emergency/inpatient;
21. index stop not before start;
22. no null person/index key;
23. one analytic row per index row;
24. nonnegative history counts;
25. history excludes index and future;
26. next encounter after index stop;
27. next encounter no more than 30 days;
28. acute return no more than 90 days;
29. death no more than 90 days;
30. endpoint precedence;
31. source coverage through follow-up;
32. flow conservation;
33. numerator no greater than denominator;
34. 29 analytic fields;
35. 29 dictionary fields;
36. field timing labels;
37. source and cohort versions;
38. SQL rerun reproduces committed outputs;
39. incomplete submission is rejected;
40. nonempty target is protected; and
41. no Unicode dash or personal absolute path appears in contract files.

### Automated and human boundary

Automation proves structure and exact facts. Human review decides whether the written definition is understandable, the SQL is teachable, the accessibility route works, the AI verification is meaningful, and the disposition fits the evidence.

## 21. Release status, reviewers, version, and known issues

### Release identity

- Module ID: `oclc-fnd1-03`.
- Module version: 0.1.0.
- Commons release: 0.30.0.
- Cohort definition version: 0.1.0.
- Status: runnable release candidate.
- Repository: https://github.com/ShuhanCS/open-clinical-learning-commons

### Measured runnable release

- Four read-only SQL files produce 1,048 eligible-event rows, 374 index rows, 374 analytic rows, and 16 passing query checks.
- The analytic table has 29 fields and exact SHA-256 `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a`.
- The 365-day encounter, acute, condition, and medication count sums are 2,138, 113, 468, and 1,007.
- The standard-library validator passes 600 release checks, 613 checks with upstream database reproduction, and 614 checks for a complete learner submission.
- All five committed outputs reproduce byte for byte from the accepted Module 02 database.

### Semantic-version decision

Module 0.1.0 establishes the first cohort, index, window, flow, analytic-table, and validation contract. Commons 0.30.0 adds this compatible runnable module and does not change Modules 01 or 02.

### Required human reviewers

| Role | Reviewer | Status |
|---|---|---|
| FND-1 faculty owner | unassigned | pending |
| SQL and data engineering | unassigned | pending |
| Clinical informatics and cohort meaning | unassigned | pending |
| Denominator and temporal logic | unassigned | pending |
| Accessibility | unassigned | pending |
| Privacy and data governance | unassigned | pending |
| Responsible AI | unassigned | pending |
| Independent reproduction and teachability | unassigned | pending |

### Known issues after technical validation

1. Named human review is pending.
2. macOS and Linux reproduction remain pending until recorded.
3. The source is synthetic and older.
4. The optional CMS Synthetic Medicare claims extension is not part of this cohort.

### Context-safe handoff

Module 03 implementation and technical reproduction are complete. Assemble the cumulative Week 3 checkpoint from Modules 01 through 03 before beginning Module 04. Preserve the accepted Module 02 database and Module 03 cohort definition as immutable upstream releases.
