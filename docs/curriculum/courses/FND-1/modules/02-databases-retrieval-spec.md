# FND-1 Module 02: Databases and retrieving healthcare data

## 1. Module identity and place in the course

- Course: FND-1 Healthcare Data Foundations.
- Module: 02 of 07.
- Instructional week: 2.
- Learner workload: 16.0 hours.
- Prerequisite: Module 01 accepted or accepted with conditions.
- Module version: 0.1.0.
- Commons release: 0.29.0.
- Status: runnable release candidate; human review pending.
- Decision owner: clinical data architect.
- Package: `courses/healthcare-data-foundations/modules/02-databases-retrieval/`.
- Primary tools: Python standard library, SQLite, SQL, Git, Mermaid or an accessible equivalent, JSON, and supplied FHIR R4 reading examples.
- Source: complete pinned Synthea April 2020 CSV sample.
- Handoff: validated relational release for Module 03 cohort and analytic-table work.

Module 02 begins the continuing FND-1 healthcare data system. Learners take one exact public synthetic archive, inspect its members, preserve every source row and field in a relational database, define table grain and keys, check relationships, retrieve bounded records, compare flat tables with nested FHIR JSON, and decide whether the database is ready for cohort definition.

The module asks:

> Does this relational release preserve source meaning well enough for Module 03 cohort work?

It does not ask learners to define that cohort yet.

### Starting condition

The learner enters with the accepted Module 01 repository structure, environment, version, reproduction, and AI-accountability practices. The learner can run Python, inspect Git state, execute supplied code, and preserve a tagged release.

### Ending condition

The learner leaves with:

- the verified 16-member source manifest;
- a reproducible 16-table SQLite database;
- exact source and build records;
- an explicit schema;
- a 177-row database dictionary;
- a visual data model and full text equivalent;
- three minimized retrieval views;
- five checked SQL extracts;
- linked FHIR R4 Patient, Encounter, and Observation reading examples;
- a database validation report;
- a technical readiness recommendation;
- an AI-use record; and
- a versioned Module 02 handoff.

### Checkpoint relationship

Module 02 is not independently weighted in the source assessment. Its accepted database, schema, provenance, and validation evidence are required inputs to the 25-percent Module 03 SQL cohort component and the cumulative 40-percent Week 3 checkpoint.

## 2. Technical decision and named audience

### Decision owner

The clinical data architect owns the readiness decision. In a live course, the instructor may act in this role or appoint a qualified reviewer.

### Decision

The owner decides whether the relational database can be used as the immutable upstream source for Module 03.

### Dispositions

| Disposition | Meaning | Module 03 action |
|---|---|---|
| `accept` | Source, schema, keys, relationships, types, retrievals, and records pass with no material condition. | Freeze the database contract and begin cohort work. |
| `accept with conditions` | Core integrity passes, but a bounded documentation, access, or accessibility condition remains. | Begin only with the condition, owner, and due date recorded. |
| `revise` | A source, build, schema, query, FHIR, documentation, or validation defect is correctable. | Correct, rebuild, revalidate, and resubmit. |
| `refer` | Rights, privacy, credential, source-integrity, or academic-integrity concern needs another authority. | Stop reuse until that authority resolves the issue. |

### Primary learner

The learner is a clinician, researcher, analyst, quality professional, or health-system staff member who may recognize healthcare records but may not yet understand relational grain, primary and foreign keys, source provenance, or nested exchange formats.

### Review audiences

- clinical data architect;
- SQL and data engineer;
- clinical informatician;
- source and rights reviewer;
- FHIR instructor;
- accessibility reviewer;
- privacy and governance reviewer;
- Module 03 instructor; and
- another analyst reproducing the build.

### Decision evidence

The decision uses:

1. archive and member fingerprints;
2. source table, row, column, and byte inventory;
3. explicit SQL schema;
4. primary-key and foreign-key checks;
5. type and missing-value handling;
6. SQLite integrity;
7. minimized views;
8. five exact retrieval results;
9. FHIR reference resolution;
10. accessible diagram and text description;
11. learner validation interpretation; and
12. AI-use verification.

## 3. Foundation skill and handoff

### Foundation skill

The learner translates a set of healthcare-like source files into a documented relational release without changing source grain or silently repairing missingness.

### Technical habits extended from Module 01

- work from a pinned source;
- preserve exact fingerprints;
- keep downloaded and generated large files out of Git when they are reproducible;
- keep source records, build code, schema, small outputs, and validation in Git;
- run from a clean target;
- use semantic versions;
- record actual environment facts; and
- verify material AI suggestions.

### Handoff to Module 03

Module 03 receives:

- archive identity and source manifest;
- immutable database schema;
- exact table counts;
- source field dictionary;
- patient, encounter, condition, observation, medication, procedure, and related tables;
- optionality rules;
- core retrieval views;
- first checked SQL patterns;
- known source limitations; and
- accepted or conditional readiness disposition.

Module 03 then owns:

- analytic question;
- index event;
- observation window;
- inclusion and exclusion rules;
- join direction;
- attrition counts;
- one-row-per-person analytic grain;
- denominators; and
- cohort query tests.

### Separation from FND-2

No statistical model, inferential assumption, performance measure, calibration, prediction, causal claim, or model-governance decision belongs here.

### Separation from DA-730

The schema diagram communicates relationships accessibly. It is not an exercise in visual encoding, perceptual accuracy, dashboard design, or decision storytelling.

## 4. Assessable outcomes

The learner can:

1. verify an archive by size and SHA-256;
2. verify every archive member by path, bytes, rows, columns, and SHA-256;
3. explain why a source manifest is different from a data dictionary;
4. state the grain of all 16 source tables;
5. identify source IDs and tables without source IDs;
6. justify a transparent source-row surrogate without calling it a source identifier;
7. distinguish primary, foreign, optional foreign, and non-key fields;
8. explain one-to-many and optional relationships;
9. preserve all 471,836 source rows;
10. preserve the zero-row supplies table;
11. preserve 30,363 missing observation encounter references as `NULL`;
12. load identifiers and codes as text;
13. load declared count and year fields as integers;
14. load declared cost, coordinate, and quantitative summary fields as real values;
15. explain why source dates remain text at this stage;
16. run SQLite integrity and foreign-key checks;
17. interpret a 177-row database dictionary;
18. identify identity-like and cost fields;
19. use minimized views when broader fields are unnecessary;
20. write deterministic `SELECT` and `WITH` queries;
21. use `WHERE`, `ORDER BY`, `GROUP BY`, `COUNT`, and `CASE` correctly;
22. produce five exact retrieval extracts;
23. explain why a retrieval is not a cohort;
24. trace FHIR Patient, Encounter, and Observation references;
25. compare relational columns with nested JSON paths;
26. state the limits of the teaching FHIR mapping;
27. create an accessible relationship diagram and text equivalent;
28. recommend stop, fix, proceed, or proceed with conditions from validation evidence;
29. disclose and verify material AI use; and
30. hand the database contract to Module 03 without adding cohort logic.

### Evidence map

| Skill | Direct evidence |
|---|---|
| Provenance | Source record and exact manifest. |
| Grain and keys | Data model and schema description. |
| Build | Build report and generated database. |
| Integrity | 96-check validation report. |
| SQL | Five query blocks and five exact CSV outputs. |
| FHIR reading | Completed linked-resource comparison. |
| Accessibility | Mermaid or equivalent plus full text description. |
| Recommendation | Validation notes and disposition. |
| AI accountability | Complete use and verification record. |

## 5. Concept ownership and out-of-scope boundaries

### Module 02 owns

- source-system orientation;
- archive provenance and rights;
- table and row grain;
- fields and storage types;
- source and surrogate keys;
- relational relationships and optionality;
- SQLite schema and database build;
- member and database validation;
- first read-only SQL retrievals;
- minimized views;
- identity-like and cost-field awareness;
- FHIR R4 JSON shape recognition;
- schema diagram and text description; and
- readiness handoff.

### Introduced for later use

- encounter chronology;
- conditions, observations, medications, procedures, and care plans;
- payer and organization relationships;
- missing encounter links; and
- code and description pairs.

These are inspected, not analyzed.

### Out of scope

- cohort definition;
- index-event selection;
- eligibility windows;
- attrition;
- analytic-table construction;
- duplicate correction;
- missing-data imputation;
- data-quality severity scoring;
- descriptive clinical results;
- visualization;
- statistical inference;
- machine learning;
- real patient access;
- FHIR server operation;
- terminology-server validation;
- full FHIR conformance testing;
- database-server administration;
- query-performance engineering beyond useful indexes;
- claims adjudication; and
- production deployment.

### Deliberate implementation ceiling

SQLite is the default because it is portable, requires no server, and supports keys, views, indexes, read-only connections, and integrity checks. The module does not add PostgreSQL, cloud infrastructure, an ORM, migration framework, container, or workflow engine.

## 6. Lesson sequence and learner time

| Block | Work | Hours | Evidence |
|---:|---|---:|---|
| 1 | Source systems, provenance, archive, and rights | 1.50 | Verified source record and manifest. |
| 2 | Relational grain, keys, types, and optionality | 2.50 | Table-grain and relationship notes. |
| 3 | Complete database build and manifest audit | 2.00 | Passing build report. |
| 4 | Schema diagram and accessible text description | 2.00 | Completed `.mmd` and Markdown description. |
| 5 | SQL retrieval and deterministic extracts | 3.00 | Five SQL blocks and outputs. |
| 6 | FHIR R4 Patient, Encounter, and Observation reading | 1.50 | Completed FHIR comparison. |
| 7 | Validation, minimization, and flagged fields | 1.50 | Validation report and notes. |
| 8 | Independent extracts, AI verification, and handoff | 2.00 | Complete submission and disposition. |
| Total |  | 16.00 |  |

### Block 1

Learners distinguish EHR-like clinical event tables, organization/provider tables, payer tables, and a synthetic generator output. They verify the archive before opening any CSV.

### Block 2

Learners inspect headers and ask for each table:

- what does one row represent;
- what identifies it;
- which table owns each referenced ID;
- which reference is optional;
- which field is a code versus description;
- which field looks numeric but is an identifier; and
- which missing value is preserved.

### Block 3

The builder creates all tables in dependency order, inserts in batches, records source metadata, creates indexes and views, checks integrity, and produces linked JSON examples.

### Block 4

The learner completes every relationship, including payers, payer transitions, organizations, providers, care plans, allergies, imaging, immunizations, devices, and the empty supplies table. The text alternative must stand alone.

### Block 5

Learners write five named, read-only query blocks. Query names become filenames, and deterministic ordering is required.

### Block 6

Learners trace the same synthetic person, encounter, and observation through relational and JSON forms. The lesson focuses on shape and references, not FHIR implementation.

### Block 7

Learners interpret source and database facts, including identity-like fields, financial fields, empty tables, missing encounter links, and logical versus byte-level reproducibility.

### Block 8

Learners verify one material claim, run the 126-check submission validator, record the readiness decision, version the work, and hand it to Module 03.

## 7. Readings and authoritative sources

### Required sources

- Synthea downloads: https://synthea.mitre.org/downloads
- Synthea project: https://synthetichealth.github.io/synthea/
- Pinned archive: https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip
- CSV dictionary: https://github.com/synthetichealth/synthea/wiki/CSV-File-Data-Dictionary
- Synthea repository: https://github.com/synthetichealth/synthea
- Synthea license: https://github.com/synthetichealth/synthea/blob/master/LICENSE
- SQLite foreign keys: https://www.sqlite.org/foreignkeys.html
- SQLite language: https://www.sqlite.org/lang.html
- Python SQLite: https://docs.python.org/3/library/sqlite3.html
- FHIR R4 Patient: https://hl7.org/fhir/R4/patient.html
- FHIR R4 Encounter: https://hl7.org/fhir/R4/encounter.html
- FHIR R4 Observation: https://hl7.org/fhir/R4/observation.html

### Reading questions

For Synthea:

- What is generated?
- What source limitations travel with the archive?
- How are CSV fields described?
- Why can synthetic identity-like fields still support minimization practice?

For SQLite:

- When are foreign keys enforced?
- What does `PRAGMA foreign_key_check` test?
- What does integrity `ok` mean and not mean?
- Why use a read-only connection for extraction?

For FHIR:

- Which resource owns the patient ID?
- How does Encounter reference Patient?
- How does Observation reference Patient and Encounter?
- Where do value and unit appear?
- What does a three-resource example leave untested?

## 8. Dataset inventory, provenance, rights, and teaching purpose

### Archive contract

- Label: April 2020 CSV sample.
- Compressed bytes: 8,982,431.
- Uncompressed CSV bytes: 82,293,440.
- SHA-256: `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a`.
- Members: 16 files under `csv/`.
- Total rows: 471,836.
- Total source columns: 168.

### Table inventory

| Table | Rows | Columns | Source ID |
|---|---:|---:|---|
| allergies | 597 | 6 | none |
| careplans | 3,483 | 9 | `Id` |
| conditions | 8,376 | 6 | none |
| devices | 78 | 7 | none |
| encounters | 53,346 | 15 | `Id` |
| imaging_studies | 855 | 10 | `Id` |
| immunizations | 15,478 | 6 | none |
| medications | 42,989 | 13 | none |
| observations | 299,697 | 8 | none |
| organizations | 1,119 | 11 | `Id` |
| patients | 1,171 | 25 | `Id` |
| payer_transitions | 3,801 | 5 | none |
| payers | 10 | 21 | `Id` |
| procedures | 34,981 | 8 | none |
| providers | 5,855 | 12 | `Id` |
| supplies | 0 | 6 | none |

Every member's exact byte count and SHA-256 appears in `source-manifest.csv` and is machine checked before loading.

### Rights and privacy

Synthea is distributed under Apache-2.0. The records are synthetic. The module uses no real patient data.

Synthetic status permits open teaching use but does not make every field necessary. Identity-like and cost fields are flagged, and first extracts use minimized views where possible.

### Teaching purpose

The archive provides realistic relational complexity without protected records:

- patient-to-encounter history;
- clinical event tables;
- organization/provider relationships;
- payer relationships;
- optional encounter linkage;
- code/description pairs;
- numeric and text observations;
- start/stop dates; and
- source tables with and without IDs.

### Interpretation boundary

The database cannot estimate or evaluate a real population, hospital, clinician, payer, treatment, utilization pattern, cost, outcome, or disparity.

## 9. Data dictionary and expected structure

### Key strategy

Source `Id` is the primary key for patients, organizations, providers, payers, encounters, care plans, and imaging studies.

The other nine tables receive `source_row_number`, a 1-based ordinal in original CSV order. It provides stable technical row identity while clearly recording that the source did not provide an `Id` field.

### Foreign keys

- providers.organization -> organizations.id;
- encounters.patient -> patients.id;
- encounters.organization -> organizations.id;
- encounters.provider -> providers.id;
- encounters.payer -> payers.id;
- clinical event patient -> patients.id;
- clinical event encounter -> encounters.id;
- medications.payer -> payers.id; and
- payer_transitions.payer -> payers.id.

Observation encounter is nullable. Other declared references in the pinned release are nonblank and resolve.

### Types

- IDs and codes: `TEXT`.
- source dates and timestamps: `TEXT`.
- counts and years: `INTEGER`.
- costs, coverage amounts, coordinates, and summary quantities: `REAL`.
- observation value: `TEXT` because the source contains numeric and text types.
- missing source strings: SQL `NULL`.

### Dictionary fields

The generated dictionary includes:

- table;
- database position;
- source field;
- database field;
- SQLite type;
- required flag;
- identity-like flag;
- cost/coverage flag;
- core-view inclusion flag; and
- description route.

### Core views

`v_patients_minimal` contains nine fields.

`v_encounters_core` contains nine fields.

`v_observations_core` contains nine fields.

Together, 27 dictionary rows are marked as core-view fields.

## 10. Worked example

### Step 1: Verify source

Confirm archive byte count and SHA-256, then verify all 16 member paths, bytes, and fingerprints. Stop before extraction if any differs.

### Step 2: Read grains

Compare:

- one patient row;
- one encounter row;
- one observation row;
- one payer transition; and
- the zero-row supplies file.

State why these grains cannot be joined and counted without a declared question.

### Step 3: Build

```text
python build_database.py --source-zip PATH_TO_ZIP --target learner-database-workspace
```

Expected result:

```text
FND-1 Module 02 database build passed: 471836 rows across 16 source tables.
```

### Step 4: Inspect build report

Reference facts:

- status `pass`;
- 16 exact table counts;
- 471,836 total rows;
- zero foreign-key failures;
- integrity `ok`;
- 177 dictionary rows; and
- three FHIR IDs.

### Step 5: Trace one relationship

Take one encounter. Confirm that its patient, organization, provider, and payer IDs resolve. Then take one linked observation and resolve its patient and encounter.

### Step 6: Run first retrieval

List the 16 registered tables and source row/column counts. This query reads database metadata and does not touch a clinical question.

### Step 7: Group encounter classes

Expected counts:

- wellness 19,106;
- ambulatory 18,936;
- outpatient 9,003;
- urgentcare 2,373;
- emergency 2,090; and
- inpatient 1,838.

This is a source inventory, not a utilization estimate.

### Step 8: Inspect optional linkage

Observation grouping returns three rows because numeric observations include linked and missing encounter references, while text observations in this release form the third combination.

### Step 9: Read FHIR examples

Trace Patient `00185faa-2760-4218-9bf5-db301acf8274`, Encounter `6b5bfe89-1c58-42e8-87c4-847b542d5f0b`, and Observation `synthea-observation-191026`.

### Step 10: Decide

A supported recommendation is:

> Proceed to cohort definition because the pinned archive, complete table loads, declared keys, optional observation linkage, zero foreign-key failures, integrity check, minimized views, and reference retrievals pass. Carry the synthetic, source-age, identity-like-field, and FHIR-mapping limits into Module 03.

## 11. Guided practice

### Practice 1: Grain sorting

Learners match each table to its grain and reject ambiguous phrases such as "one clinical record."

### Practice 2: Identifier typing

Learners classify patient IDs, encounter IDs, ZIP values, codes, counts, years, costs, and observation values. They explain why identifiers that contain digits remain text.

### Practice 3: Relationship audit

Learners use left joins and null checks to confirm parent coverage without changing the database.

### Practice 4: Empty table

Learners explain why keeping `supplies` with zero rows is more faithful than omitting it.

### Practice 5: Optional observation encounter

Learners compare null encounter reference with an orphan reference and explain why only the latter would violate the foreign key.

### Practice 6: Minimized view

Learners compare `patients` and `v_patients_minimal`, then state which fields are unnecessary for first retrieval.

### Practice 7: Deterministic order

Learners run a `LIMIT` query with and without `ORDER BY`, then explain why only the ordered result is a stable release artifact.

### Practice 8: FHIR references

Learners locate `subject.reference`, `encounter.reference`, `valueQuantity.value`, and `valueQuantity.unit` and connect them to relational columns.

### Practice 9: AI verification

Learners verify one suggested join or FHIR claim with the schema, database, validator, or official HL7 page.

### Tiered support

- Tier 1: exact build and validation commands.
- Tier 2: partially completed relationship table and query purpose prompts.
- Tier 3: guided technical clinic with read-only database browser.

All tiers produce the same final evidence.

## 12. Independent exercise

The learner independently:

1. verifies source and members;
2. builds the database;
3. checks the report;
4. completes all table grains;
5. completes all relationships and optionality;
6. completes the accessible schema description;
7. writes five query blocks;
8. generates five outputs;
9. completes the FHIR comparison;
10. runs database and submission validation;
11. records one verified AI or manual troubleshooting claim;
12. recommends stop, fix, proceed, or proceed with conditions; and
13. versions and tags the release.

### Constraints

The learner may not:

- change the source fingerprint;
- drop a source table or row;
- coerce codes or identifiers into numbers;
- replace blank optional references with fabricated IDs;
- edit reference expectations to force a pass;
- write mutation SQL in the extract file;
- define the Module 03 cohort;
- commit the ZIP or SQLite database;
- expose credentials or private paths; or
- describe synthetic results as real estimates.

## 13. Visualization or communication requirements

### Diagram

The learner supplies an entity-relationship diagram in Mermaid or an accessible equivalent. It must show every table and relationship needed to understand the source.

### Text alternative

`schema-description.md` must independently state:

- every table grain;
- primary or surrogate key;
- every parent relationship;
- cardinality;
- optionality;
- core views;
- flagged fields; and
- structural limits.

The text is not a caption. A reader must be able to understand the database without rendering the diagram.

### SQL communication

Each query has a stable name, readable layout, explicit selected fields, and deterministic ordering. `SELECT *` is not used in learner extracts.

### No clinical visualization

No chart is required. The work is source structure and retrieval, not a clinical finding.

## 14. Exact submission package

```text
learner-database-workspace/
  .gitattributes
  .gitignore
  README.md
  VERSION
  source-record.yml
  source-manifest.csv
  schema.sql
  build-report.json
  data-dictionary.csv
  data-model.mmd
  schema-description.md
  fhir-json-reading.md
  validation-notes.md
  validation-report.json
  ai-use.md
  run_queries.py
  data/
    fnd1_synthea_apr2020.sqlite  # generated, ignored, not committed
  fhir/
    patient.json
    encounter.json
    observation.json
  sql/
    01-first-extracts.sql
  outputs/
    table-inventory.csv
    encounter-class-counts.csv
    observation-linkage.csv
    selected-patient-timeline.csv
    numeric-observation-sample.csv
```

The source ZIP may appear under ignored `source-cache/`. It is not committed.

### Git release

The tagged submission uses `fnd1-database-v0.1.0` and identifies the complete tracked evidence. The generated database is reproduced from the pinned source rather than distributed through Git.

## 15. Rubric and pass conditions

| Criterion | Points |
|---|---:|
| Provenance and source fidelity | 15 |
| Relational model and grain | 25 |
| SQL retrieval | 25 |
| Validation and technical recommendation | 20 |
| FHIR and JSON reading | 10 |
| Accessibility, minimization, and AI accountability | 5 |
| Total | 100 |

### Threshold

At least 80 points.

### Noncompensable gates

- source fingerprint;
- database integrity;
- zero foreign-key failures;
- exact retrieval;
- accessible schema;
- FHIR references;
- privacy and minimization;
- AI disclosure;
- scope boundary; and
- accept or accept with conditions disposition.

### Revision

Before checkpoint freeze, the learner corrects and rebuilds every affected output. After freeze, a changed accepted interface receives a new semantic version and tag.

## 16. Common failures and instructor interventions

| Failure | Intervention | Resolution evidence |
|---|---|---|
| Archive fingerprint differs | Stop and obtain the pinned archive. | Exact bytes and SHA pass. |
| Member missing or refreshed | Do not mix releases. | All 16 member fingerprints pass. |
| Database target already exists | Choose a new target; inspect rather than overwrite. | Safe clean build. |
| Identifier imported numeric | Restore text schema and rebuild. | Leading/source formatting preserved. |
| Empty strings loaded as empty text inconsistently | Use declared loader rule and rebuild. | Expected null counts. |
| Observation encounter made required | Restore optional foreign key. | 30,363 nulls and zero orphans. |
| Supplies table omitted | Restore table and manifest row. | Zero-row table present. |
| Source row number called clinical ID | Relabel as generated ordinal. | Dictionary and description corrected. |
| `LIMIT` without order | Add deterministic order. | Output matches reference bytes. |
| Mutation SQL used | Replace with read-only query. | Runner accepts block. |
| Output folder silently overwritten | Use a new empty output folder. | Guard passes. |
| Diagram lacks text equivalent | Complete every grain and relationship in prose. | Accessibility review passes. |
| Synthetic values treated as estimates | Correct source interpretation. | Claim boundary explicit. |
| FHIR conformance overstated | Narrow to teaching mapping. | Mapping limit explicit. |
| Cohort built early | Remove eligibility/index logic. | Module 02 remains retrieval only. |
| AI join copied without check | Run key and row-count audit. | Human verification recorded. |

## 17. Accessibility, equity, privacy, and claim checks

### Accessibility

- commands are text;
- status markers are text;
- diagram has a full prose equivalent;
- tables have headings;
- no result depends on color;
- SQL is formatted and named;
- JSON examples are small and indented; and
- a read-only graphical SQLite browser is permitted when accessible.

### Equity

The 141 MB database is generated locally. Instructors provide an institution-managed build when bandwidth, storage, permissions, or hardware make local work impractical. Learners are not penalized for the provided environment route.

### Privacy

Records are synthetic. Learners still practice minimization. They do not replace the source with workplace data, paste identity-like rows into external AI tools without need, or commit credentials and private paths.

### Claims

Required statements:

- Synthea records are synthetic.
- Counts describe this pinned synthetic archive only.
- Schema integrity is not clinical validity.
- Referential integrity is not data-quality completeness.
- FHIR shape reading is not conformance certification.
- Retrieval is not a cohort.
- Module 03 must define denominators before analysis.

## 18. AI policy, disclosure, and verification

### Permitted

- explain a SQLite error;
- propose a read-only query;
- explain a relationship;
- compare relational and JSON shape;
- improve accessible schema prose; and
- propose a validation check.

### Prohibited

- fabricate source or validation output;
- alter expected counts to force a pass;
- invent key relationships;
- send protected or workplace data;
- send credentials;
- conceal use;
- outsource the full diagram or query set without understanding; or
- make a clinical claim from synthetic counts.

### Required verification

For one material use, record tool/model, prompt purpose, data shared, relevant advice, database or authoritative check, observed result, and accepted/changed/rejected decision.

An AI answer is not evidence.

## 19. Answer key and instructor materials

### Reference technical facts

- 16 source tables.
- 471,836 source rows.
- 168 source fields.
- 177 database dictionary rows.
- 9 generated source-row surrogate fields.
- 3 minimized views.
- 27 fields across minimized views.
- 0 foreign-key failures.
- integrity `ok`.
- 96 base checks.
- 126 submission checks.

### Reference queries

The exact instructor SQL is `reference-first-extracts.sql`. It returns 16, 6, 3, 25, and 25 rows.

### Reference recommendation

Proceed with the pinned database as immutable upstream input, carrying synthetic/source-age limits, optional observation encounter linkage, identity-like and cost-field minimization, and nonconformant teaching-FHIR status into Module 03.

### Grading order

1. verify source;
2. rebuild cleanly;
3. run 96 checks;
4. inspect diagram/text;
5. run learner SQL;
6. compare five outputs;
7. inspect FHIR record;
8. inspect validation and AI notes;
9. run 126 checks;
10. score gates and disposition.

## 20. Runnable acceptance checks

### Builder

The builder verifies:

- manifest has 16 sorted tables;
- manifest rows total 471,836;
- archive bytes and SHA;
- exact archive members;
- exact member bytes and SHA;
- exact headers;
- exact source row counts;
- type conversion;
- dependency-order loading;
- foreign keys;
- integrity;
- dictionary generation;
- FHIR generation;
- existing-target refusal; and
- deterministic logical report.

### Query runner

The runner verifies:

- named blocks exist;
- names are unique and filename safe;
- each block begins with `SELECT` or `WITH`;
- one statement per block;
- database opens read only;
- headers and rows write as LF CSV;
- one output per block; and
- nonempty output refusal.

### Database validator

Base validation passes 96 grouped checks covering:

- 17 required workspace files;
- workspace version;
- exact source manifest;
- optional full source revalidation;
- build-report facts;
- SQLite integrity and foreign keys;
- user version;
- row and column counts for all 16 tables;
- database manifest;
- total source rows;
- three view counts;
- six encounter classes;
- numeric/text observations;
- missing encounter links;
- empty supplies;
- dictionary rows, uniqueness, and flags;
- three FHIR files, types, IDs, references, value, and unit; and
- five reference extract row counts.

Complete submission validation passes 126 checks by adding:

- seven complete learner records;
- no common personal absolute paths;
- learner SQL parse and execution;
- exact query row counts;
- five required output files;
- output agreement with submitted SQL; and
- byte agreement with reference results.

### Self-checks

- builder conversion and overwrite guard;
- query runner valid output and overwrite rejection;
- validator manifest facts;
- valid FHIR links; and
- broken FHIR encounter-reference rejection.

### Full release test

Maintainers build from the exact archive in a new temporary target, validate with the archive, run reference queries, create a completed fixture, prove 126 checks pass, prove incomplete records fail, and protect nonempty targets and outputs.

### Human checks

Automation does not decide whether the diagram is understandable, the prose is accessible, the learner understands grain, the recommendation is justified, the AI verification is meaningful, or the workload is teachable.

## 21. Release status, reviewers, version, and known issues

### Release identity

- Module ID: `oclc-fnd1-02`.
- Module version: 0.1.0.
- Commons release: 0.29.0.
- Data release: `fnd1-synthea-relational-apr2020` 0.1.0.
- Status: runnable release candidate.
- Release date: 2026-08-30.
- Repository: https://github.com/ShuhanCS/open-clinical-learning-commons

### Semantic-version decision

Module 0.1.0 is the first runnable database-and-retrieval contract. Commons 0.29.0 adds a compatible FND-1 module without changing course architecture or Module 01 interfaces.

### Technical completion

- source archive verified;
- every member inventoried;
- schema complete;
- 471,836 rows loaded;
- 177 dictionary rows generated;
- zero foreign-key failures;
- integrity `ok`;
- 141,234,176-byte tested database built;
- linked FHIR examples generated;
- five reference extracts passed;
- 96 base checks passed;
- 126 complete-submission checks passed;
- invalid FHIR reference rejected;
- incomplete learner record rejected;
- existing target protected; and
- nonempty output protected.

### Required human reviewers

| Role | Reviewer | Status |
|---|---|---|
| FND-1 faculty owner | unassigned | pending |
| SQL and data engineering | unassigned | pending |
| Clinical informatics and healthcare-data meaning | unassigned | pending |
| FHIR R4 reading path | unassigned | pending |
| Source rights and provenance | unassigned | pending |
| Accessibility | unassigned | pending |
| Privacy and data governance | unassigned | pending |
| Responsible AI | unassigned | pending |
| Independent reproduction and teachability | unassigned | pending |

### Known issues

1. Named human reviews are pending.
2. The full reference build was tested on Windows with Python 3.12.10 and SQLite 3.49.1; named macOS/Linux reproduction is pending.
3. The 141 MB database is intentionally rebuilt rather than stored in Git.
4. Database byte hash can change with an approved SQLite/build change; logical invariants remain the primary validation contract.
5. FHIR examples do not claim full conformance.
6. The archive is an older synthetic sample.
7. Module 02 does not yet include the optional CMS Synthetic Medicare claims extension.
8. A live course needs a supported large-file build route for learners with limited bandwidth or storage.

### Context-safe handoff

After release, resume at Module 03.

Read this specification, the course specification, Module 01 release, Module 02 release, source record, and build ledger. Then define the adult acute-care cohort and one-row-per-person analytic table against the immutable Module 02 database. Preserve all source and relationship facts. Add index date, lookback, follow-up, inclusion/exclusion, attrition, denominators, query tests, and the 25-percent checkpoint component. Do not begin cleaning, profiling, statistical modeling, or applied-course work.
