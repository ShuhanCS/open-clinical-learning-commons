# FND-1: Healthcare Data Foundations

- Status: course specification complete; Modules 01 through 05 and Checkpoint 1 are runnable release candidates
- Course specification version: 0.1.0
- Commons release: 0.33.0
- Credits: 3
- Delivery: asynchronous online half-term with scheduled technical clinics and review
- Planning model: seven instructional weeks mapped to official half-term dates
- Total learner workload: 112.5 hours
- Prerequisites: none
- Position: first technical foundation in the 30-credit program
- Final deliverable: reproducible healthcare data toolkit and technical handoff defense
- Source record: `docs/source/fnd-1-healthcare-data-foundations-source-record.md`
- Course package: `courses/healthcare-data-foundations/`

## Course purpose

FND-1 teaches learners to work inside healthcare data before modeling begins. The course starts with the systems that produce records and the technical work required to make those records usable. Learners set up a reproducible workspace, retrieve data with SQL, define a cohort, build an analytic table, inspect defects, describe the data honestly, and release a toolkit another analyst can rerun and audit.

The final course question is practical:

> Can a downstream analyst trust this cohort and analytic table enough to begin modeling or applied analysis?

The course is deliberately technical. It does not distribute basic data preparation across later domain courses. Applied courses may reuse the released data layer, but they do not send learners back through an identical FND-1 lesson.

## Audience and final decision

### Primary learner

The primary learner is a clinician, researcher, analyst, quality professional, or health-system staff member entering graduate healthcare analytics with uneven prior experience in programming, databases, version control, and reproducible work.

### Final decision owner

The final decision owner is a health-system analytics engineering lead or senior clinical data analyst responsible for accepting data into a downstream analytic workflow.

### Secondary readers

- a modeling analyst entering FND-2;
- a clinical informatician checking meaning and provenance;
- a data steward checking rights, fields, and permitted use;
- an instructor checking technical competency; and
- an accessibility reviewer checking documents, diagrams, tables, and charts.

### Final decision

Decide whether the released cohort, analytic table, source records, quality findings, descriptive evidence, and reproduction path are trustworthy enough for downstream work.

### Available dispositions

| Disposition | Meaning | Handoff result |
|---|---|---|
| `accept` | Every release gate passes and no material condition remains. | The toolkit may enter FND-2 or approved applied work. |
| `accept with conditions` | Every noncompensable gate passes and one bounded condition has an owner, date, and closure test. | Downstream use is limited to the recorded condition. |
| `revise` | One or more recoverable data, code, documentation, accessibility, or reproduction defects remain. | The toolkit returns to the learner. |
| `refer` | A privacy, rights, integrity, security, or governance concern needs program review. | The toolkit is held outside the public workflow. |

### Supported action

The reviewer may accept the toolkit, require a bounded repair, narrow its permitted use, or refer it for governance review.

### Unsupported action

Course acceptance does not establish that:

- the synthetic cohort represents a real health-system population;
- a descriptive difference is causal;
- the data support a clinical intervention;
- a downstream model will be valid;
- a public aggregate source can be joined to person-level records without a defined linkage; or
- a learner may place protected or restricted data into the public repository or an external AI service.

## Place in the curriculum

FND-1 and FND-2 are separate technical foundations.

### FND-1 owns

- healthcare data sources and generation processes;
- relational databases and SQL retrieval;
- schemas, keys, grain, and normalization;
- cohort definitions, index dates, windows, inclusion, exclusion, attrition, and denominators;
- analytic-table construction;
- cleaning, reshaping, types, units, duplicates, coding drift, and outliers;
- missingness and data-quality profiling;
- descriptive summaries, cross-tabs, rates, and stratification;
- basic accessible charting and time-indexed inspection;
- Git, environments, semantic versions, releases, and handoff;
- provenance, data dictionaries, validation records, and source rights; and
- responsible AI and agent use in data work.

### FND-2 owns

- analytic aims and estimands;
- regression and general model interpretation;
- prediction workflows and evaluation;
- model-based adjustment and confounding strategy;
- missing-data modeling strategy;
- longitudinal models and survival methods;
- forecasting and temporal validation;
- model testing and failure analysis; and
- model cards, monitoring, drift, retraining, rollback, and governance.

### Boundary with DA-730

FND-1 uses charts to inspect data and communicate descriptive quality findings. DA-730 owns the full concept-first visualization curriculum, including detailed encoding, perception, chart selection, comparison, uncertainty, maps, flows, dashboards, accessibility, annotation, and decision storytelling.

FND-1 learners must create accessible charts, but FND-1 does not reteach the complete DA-730 concept sequence.

### Boundary with applied courses

Applied courses may assume learners can:

- inspect source records;
- state table grain;
- query relational data;
- define a cohort and denominator;
- build and validate an analytic table;
- profile defects and missingness;
- create descriptive tables;
- maintain a versioned repository;
- reproduce a release; and
- disclose and verify AI assistance.

An applied course must state which FND-1 asset it reuses and what domain-specific skill it adds.

## Source fidelity and approved normalization

The canonical course source is `03-FND-1-Healthcare-Data-Foundations.docx`, verified with SHA-256:

`70a78f38824066770b724aca907211ce6df94b3232cbeb8dbfa8389a24556692`

The same exact file appears in both supplied curriculum ZIP packages.

### Preserved source decisions

- seven straight-through technical modules;
- 112.5 total hours;
- no prerequisites;
- SQL and Python as graded core tools;
- R as a read-run-interpret competency;
- Git, versions, environments, provenance, and AI accountability throughout;
- four source assessment components weighted 15, 25, 25, and 35 percent; and
- a reproducible data toolkit as the signature deliverable.

### Checkpoint normalization

The Commons makes the requested Week 3, Week 6, and final checkpoint cadence explicit without changing the source weights:

- the source Week 1 setup component, 15 percent, is the first gated part of the cumulative Week 3 checkpoint;
- the source Week 3 SQL cohort component remains 25 percent;
- together, Checkpoint 1 is 40 percent;
- the source Week 5 cleaning, profiling, and descriptive component remains 25 percent and is submitted at Week 6 with the accessible-chart work;
- Checkpoint 2 is 25 percent; and
- the final toolkit remains 35 percent and is due on the official last day of the half-term.

Week 1 and Week 5 remain required feedback milestones. They do not add assessment weight.

## Course learning outcomes

By the end of FND-1, a learner can:

1. explain how EHR, claims, registry, survey, operational, FHIR, and public data differ in origin, structure, purpose, and claim boundary;
2. state the unit of observation, grain, primary key, foreign keys, time fields, and important denominators for a healthcare table;
3. build and maintain a reproducible analytics repository with a documented environment, Git history, semantic version, and release notes;
4. retrieve relational healthcare records using filters, joins, aggregation, and common table expressions;
5. define an index event, lookback, follow-up, inclusion, exclusion, attrition, and final cohort denominator;
6. create and validate a one-row-per-person analytic table;
7. clean and reshape data while preserving original values and documenting each transformation;
8. detect and assess missingness, duplicates, invalid values, inconsistent units, coding drift, orphan keys, and small cells;
9. issue and defend a stop, fix, proceed, or proceed-with-conditions data-quality recommendation;
10. produce single-variable and two-variable summaries, cross-tabs, rates, and stratified tables with correct denominators;
11. state uncertainty, small-sample, synthetic-data, and descriptive-claim limits;
12. create accessible descriptive and time-indexed charts without implying cause;
13. connect every released value to a source, query or transformation, exact table, and validation check;
14. package a complete toolkit another analyst can reproduce from a clean checkout;
15. read, run, and interpret a supplied R or Quarto analysis without being graded on authoring R from scratch;
16. use AI or agent tools for explanation, testing, debugging, and documentation while preserving a material prompt and verification record; and
17. defend the toolkit's source, cohort, data quality, denominators, limits, permitted use, and release decision.

## Program-outcome mapping

| Course outcome | Program outcomes | Primary evidence |
|---|---|---|
| Healthcare data origins, structures, and governance | PLO-1, PLO-6 | source-system comparison, schema notes, source record |
| Reproducible environment and release | PLO-4 | repository, environment, versions, clean-run record |
| SQL retrieval and analytic-table construction | PLO-1, PLO-4 | tested SQL, cohort flow, analytic table |
| Cleaning and quality reasoning | PLO-1, PLO-3 | profiling notebook, risk log, stop/fix/proceed decision |
| Descriptive evidence and access | PLO-1, PLO-5 | exact tables, memo, accessible charts and text |
| Responsible AI use | PLO-4, PLO-6 | AI-use log, verification, oral defense |

## Academic calendar rule

MGH Institute calls these offerings half-terms. The curriculum may use a 7.5-week instructional design model, but published dates use the official first and last day.

Official calendar:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

| Half-term | First day | Last day | Elapsed span |
|---|---|---|---:|
| Fall 2026 half-term 1 | September 8, 2026 | October 27, 2026 | 49 days |
| Fall 2026 half-term 2 | October 28, 2026 | December 18, 2026 | 51 days |
| Spring 2027 half-term 1 | January 11, 2027 | March 2, 2027 | 50 days |
| Spring 2027 half-term 2 | March 3, 2027 | April 24, 2027 | 52 days |
| Summer 2027 half-term 1 | May 10, 2027 | June 29, 2027 | 50 days |
| Summer 2027 half-term 2 | June 30, 2027 | August 20, 2027 | 51 days |

The final FND-1 toolkit is due on the official last day of the assigned half-term. Do not derive a generic final date by adding 52 or 53 days.

## Schedule and workload

| Week | Module | Hours | Cumulative hours | Required event |
|---:|---|---:|---:|---|
| 1 | 01. Setting up a reproducible workspace | 15.5 | 15.5 | Setup component submitted for feedback and later Checkpoint 1 inclusion. |
| 2 | 02. Databases and retrieving healthcare data | 16.0 | 31.5 | Database, schema, source, and first SQL evidence complete. |
| 3 | 03. Cohorts and analytic tables | 16.5 | 48.0 | Checkpoint 1: validated cohort and analytic-table release. |
| 4 | 04. Cleaning and profiling | 16.5 | 64.5 | Quality profile and stop/fix/proceed draft complete. |
| 5 | 05. Descriptive results | 16.0 | 80.5 | Descriptive notebook and memo submitted for feedback. |
| 6 | 06. Accessible charts and time-indexed data | 16.0 | 96.5 | Checkpoint 2: quality, descriptive, and accessible evidence release. |
| 7 | 07. Reproducible handoff and AI audit | 16.0 | 112.5 | Final checkpoint: toolkit release and technical handoff defense. |
| Total |  | 112.5 |  |  |

### Workload categories

| Work type | Hours |
|---|---:|
| Direct instruction, studios, clinics, and feedback | 18.0 |
| Readings, videos, and guided preparation | 18.0 |
| Labs, coding practice, and data exercises | 28.0 |
| Drafting, revision, peer review, and reflection | 18.5 |
| Signature toolkit project | 30.0 |
| Total | 112.5 |

## Instructional tools

### SQL

SQL is a core graded language. Learners write and check their own queries for:

- filters;
- joins;
- aggregation;
- common table expressions;
- cohort logic;
- analytic-table construction; and
- validation queries.

### SQLite

SQLite is the default course database because it provides a real relational engine without a server install. Python's standard `sqlite3` library can create and query the database. The SQL concepts must remain portable enough for a learner to recognize how PostgreSQL, SQL Server, BigQuery, Snowflake, or another approved platform differs.

The default does not imply that production health systems use SQLite for enterprise clinical data.

### Python

Python is the primary graded language for:

- importing source files;
- building the SQLite release;
- cleaning and reshaping;
- profiling quality;
- descriptive summaries;
- exact table exports;
- basic accessible charts;
- validation; and
- release automation.

The default analysis stack is Python, pandas, Jupyter, and standard-library tools wherever practical.

### R and Quarto

Learners read, run, and interpret a supplied R or Quarto document. They compare its data grain, values, and conclusions with the Python release. They are not graded on writing R from scratch.

### Git and semantic versions

Every graded release has:

- a clean Git history;
- a documented branch and merge exercise;
- a `MAJOR.MINOR.PATCH` version;
- a release note;
- a source and transformation record; and
- a clean reproduction result.

### AI and coding agents

Learners may use GitHub Copilot, Codex, Claude Code, Cursor, Gemini, or another approved tool on the synthetic course data. Every material use is logged and verified. No protected or identifiable patient data enter an outside service.

### Containers

Containers are optional. The course must remain runnable without Docker. A container may be offered as an advanced reproduction path after the ordinary environment path works.

## Continuing healthcare data system

### Core source

The core patient-level source is the pinned Synthea April 2020 CSV sample already used and registered in the Commons.

- Downloads: https://synthea.mitre.org/downloads
- Direct archive: https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip
- CSV data dictionary: https://github.com/synthetichealth/synthea/wiki/CSV-File-Data-Dictionary
- Archive bytes: 8,982,431
- Archive SHA-256: `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a`

Synthea records are simulated. They are suitable for education, software testing, and reproducible pipeline work. They do not estimate real quality, access, utilization, safety, treatment effect, or population burden.

### Core relational tables

The planned SQLite teaching database uses only fields required by the course decision from:

- patients;
- encounters;
- conditions;
- observations;
- medications;
- procedures;
- claims or payer-related records available in the pinned archive; and
- a deterministic synthetic registry extension when the source does not contain a needed registry concept.

The exact table list, row counts, fields, and fingerprints become immutable in the Module 02 release.

### FHIR and JSON examples

The course uses small synthetic examples to recognize nested healthcare exchange structures.

- Patient: https://hl7.org/fhir/R4/patient.html
- Encounter: https://hl7.org/fhir/R4/encounter.html
- Observation: https://hl7.org/fhir/R4/observation.html

Learners identify resource type, identifier, subject reference, encounter reference, coded concept, value, unit, and period. The course does not require implementation of a FHIR server.

### Claims extension

The optional claims-schema extension uses CMS Synthetic Medicare Claims PUF documentation and an instructor-selected teaching subset.

- Collection: https://data.cms.gov/collection/synthetic-medicare-enrollment-fee-for-service-claims-and-prescription-drug-event
- User guide: https://data.cms.gov/sites/default/files/2023-05/d51e1218-68c3-4c7c-9598-0b81f22fe903/User%20Guide%20-%20CMS%20Synthetic%20RIF%20Files%20May%202023_AM508_v2.pdf

The CMS source is synthetic and publicly accessible. It has limited inferential research value and is not used for conclusions about Medicare beneficiaries.

### Public aggregate contrasts

Public aggregate sources demonstrate that a source can be open yet still differ radically from person-level clinical data.

| Source | Teaching role | Full URL |
|---|---|---|
| CMS Timely and Effective Care | Compare one hospital-measure-period rows with longitudinal person-level data. | https://data.cms.gov/provider-data/dataset/yv7e-xc69 |
| CMS HCAHPS | Compare survey reporting, completed-survey counts, response rates, dates, and footnotes. | https://data.cms.gov/provider-data/dataset/dgck-syfz |
| CDC PLACES | Compare model-based county estimates with source observations and person-level records. | https://data.cdc.gov/d/fu4u-a9bh |

These sources are not joined to the synthetic person-level cohort unless a later specification defines a valid, non-personal linkage and reason.

## Data layers and provenance

The course uses four layers.

### Layer 1: immutable source

The exact source archive is retained or reproducibly retrieved when redistribution permits. Its filename, URL, date, size, checksum, and terms are recorded.

### Layer 2: source-preserving relational release

A deterministic build creates the SQLite database from selected source fields. Each table records:

- source filename;
- source row count;
- selected field list;
- destination table;
- destination row count;
- primary key or uniqueness rule;
- foreign-key expectation;
- date and type conversion; and
- SHA-256 fingerprint.

### Layer 3: seeded teaching-defect release

A separate deterministic build adds named defects for Module 04. It never modifies the immutable source or source-preserving database.

Planned defect families:

- exact duplicate records;
- conflicting duplicate records;
- missing required and optional fields;
- impossible dates;
- inconsistent units;
- orphan foreign keys;
- code-label drift across time;
- extreme but possible clinical values;
- impossible values; and
- small cells.

Each defect has an ID, injection rule, expected detection, repair or deferral rule, and answer-key status.

### Layer 4: learner analytic release

The learner creates:

- one validated cohort;
- one one-row-per-person analytic table;
- exact quality profiles;
- descriptive tables;
- accessible figures;
- a data brief; and
- a final toolkit release.

Every output links back to the source-preserving or defect release.

## Continuing cohort and handoff question

### Reference cohort

The reference build targets synthetic adults with a first qualifying emergency or inpatient encounter in an instructor-locked index period.

The planned rules are:

- age 18 or older at index;
- emergency or inpatient encounter class;
- one earliest qualifying index encounter per person;
- 365-day lookback when source history permits;
- 90-day follow-up;
- explicit handling when source history does not cover the full window;
- one row per person in the final analytic table; and
- no inference about real patients or facilities.

The exact index dates and resulting counts are locked only after Module 03 validates the pinned source. The course spec does not invent counts before the query is run.

### Reference analytic table

The planned table contains only fields needed for descriptive and downstream teaching work:

- synthetic person ID;
- index encounter ID;
- index date and class;
- age at index;
- source-recorded demographic fields used by the course;
- selected lookback condition indicators;
- selected prior-use counts;
- selected index observations with units and status;
- follow-up encounter counts;
- 30-day and 90-day acute-return indicators;
- data-completeness flags;
- source-window eligibility flags; and
- cohort-rule version.

The Module 03 specification owns the exact schema and denominator definitions.

### Final handoff question

The learner must answer:

> Should the downstream analyst accept, condition, revise, or refer this released dataset, and what exact limits travel with it?

## Module sequence

| ID | Module | Week | Hours | Primary technical decision |
|---|---|---:|---:|---|
| 01 | Setting up a reproducible workspace | 1 | 15.5 | Can another learner clone, run, inspect, and version the workspace? |
| 02 | Databases and retrieving healthcare data | 2 | 16.0 | Does the relational schema preserve source grain, keys, types, and provenance? |
| 03 | Cohorts and analytic tables | 3 | 16.5 | Does the tested SQL implement the cohort definition and preserve transparent denominators? |
| 04 | Cleaning and profiling | 4 | 16.5 | Should work stop, fix, proceed, or proceed with conditions? |
| 05 | Descriptive results | 5 | 16.0 | Do the summaries preserve clinical meaning, denominators, and descriptive limits? |
| 06 | Accessible charts and time-indexed data | 6 | 16.0 | Can every reviewer inspect the quality and descriptive evidence without a false causal claim? |
| 07 | Reproducible handoff and AI audit | 7 | 16.0 | Can the analytics lead accept and reuse the complete versioned toolkit? |
| Total |  |  | 112.5 |  |

## Module 01 brief: Setting up a reproducible workspace

- Week: 1.
- Hours: 15.5.
- Prerequisites: none.
- Decision owner: course instructor acting as repository maintainer.
- Decision: whether the workspace is ready for source data and graded SQL/Python work.
- Competency: create a versioned environment that another learner can clone and run.
- Core concepts: analytic environments, repository structure, Git commits, branches, merges, semantic versions, README contracts, environment capture, reproduction, and AI-use disclosure.
- Source input: a tiny synthetic smoke-test table that contains no patient or source claim.
- Lab: clone the starter, create the environment, run Python and SQL smoke tests, make clean commits, create and merge a branch, and tag the setup component.
- R path: run and interpret a supplied one-cell R or Quarto smoke test.
- AI task: ask an approved agent to explain one environment or Git failure, then verify and document the advice.
- Submission milestone: working repository, versioned setup check, environment note, and AI-use statement.
- Checkpoint role: the 15-percent setup component is frozen for inclusion in Checkpoint 1.
- Out of scope: database modeling, cohort logic, data cleaning, statistical modeling, Docker administration, and production deployment.

Released module package:

```text
module-01/
  README.md
  VERSION
  requirements.txt
  notebooks/
    01-smoke-test.ipynb
  sql/
    00-smoke-test.sql
  environment-note.md
  version-policy.md
  reproducibility-check.md
  ai-use.md
```

Full specification:

`docs/curriculum/courses/FND-1/modules/01-reproducible-workspace-spec.md`

Runnable package:

`courses/healthcare-data-foundations/modules/01-reproducible-workspace/`

Handoff: Module 02 uses the accepted workspace to build the relational teaching database.

## Module 02 brief: Databases and retrieving healthcare data

- Week: 2.
- Hours: 16.0.
- Prerequisites: Module 01 accepted or conditionally accepted.
- Decision owner: clinical data architect.
- Decision: whether the relational teaching release preserves source meaning well enough for cohort work.
- Competency: explain table grain and retrieve checked healthcare records from a relational database.
- Core concepts: rows and columns, schemas, primary and foreign keys, grain, normalization, source systems, provenance, FHIR and JSON recognition, SELECT, WHERE, ORDER BY, and safe extracts.
- Core source: pinned Synthea CSV archive transformed into SQLite.
- Public contrast: selected CMS or CDC aggregate records with source, time, and denominator notes.
- Lab: inspect source files, create tables, declare keys and expected relationships, run first extracts, and compare flat relational rows with nested FHIR R4 examples.
- Validation: row counts, field counts, key uniqueness, expected foreign-key coverage, type checks, date ranges, and source fingerprints.
- Submission: data model diagram, accessible schema description, data dictionary, schema notes, first SQL extracts, FHIR/JSON reading note, source record, and validation output.
- Out of scope: production database administration, query optimization at enterprise scale, HL7 interface implementation, FHIR server configuration, and cohort selection.

Released module package:

```text
module-02/
  README.md
  data-spec.md
  source-record.yml
  schema.sql
  build_database.py
  validate_database.py
  data/
    fnd1-healthcare.sqlite
    data-dictionary.csv
  schema-diagram.svg
  schema-description.md
  source-system-comparison.md
  fhir-json-reading.md
  sql/
    01-first-extracts.sql
  outputs/
    first-extracts.csv
  assessment.md
  instructor-notes.md
  release.json
```

Full specification:

`docs/curriculum/courses/FND-1/modules/02-databases-retrieval-spec.md`

Runnable package:

`courses/healthcare-data-foundations/modules/02-databases-retrieval/`

Handoff: Module 03 treats the validated database, schema, and dictionary as immutable upstream inputs.

## Module 03 brief: Cohorts and analytic tables

- Week: 3.
- Hours: 16.5.
- Prerequisites: Modules 01 and 02.
- Decision owner: senior clinical data analyst.
- Decision: whether the cohort and one-row-per-person analytic table match the declared definition and denominators.
- Competency: turn a written cohort definition into tested SQL and a versioned analytic-table release.
- Core concepts: inner and outer joins, aggregation, common table expressions, index events, lookback, follow-up, inclusion, exclusion, attrition, denominators, table grain, and query tests.
- Core source: Module 02 SQLite release.
- Lab: define the reference adult acute-care cohort, implement it in readable CTEs, select one index event per person, build flow counts, construct the analytic table, and reconcile all counts.
- Required validation: duplicate person rows, unexpected null keys, impossible index dates, window coverage, join multiplication, cohort-flow conservation, numerator-denominator relations, and table-field rules.
- Submission: tested SQL cohort, analytic-table build, cohort specification, cohort-flow table, data dictionary, query checks, provenance, reproduction record, and AI-use record.
- Checkpoint role: completes the cumulative Week 3 checkpoint.
- Out of scope: data cleaning beyond blocking source defects, descriptive inference, regression, prediction, causal adjustment, and intervention decisions.

Released module package:

```text
module-03/
  README.md
  cohort-spec.md
  table-spec.md
  sql/
    01-eligible-events.sql
    02-index-cohort.sql
    03-analytic-table.sql
    04-validation.sql
  outputs/
    cohort-flow.csv
    analytic-table.csv
    query-checks.csv
  data-dictionary.csv
  source-record.yml
  transformation-record.md
  reproducibility-check.md
  ai-use.md
  assessment.md
  instructor-notes.md
  release.json
```

Full specification:

`docs/curriculum/courses/FND-1/modules/03-cohorts-analytic-tables-spec.md`

Runnable package:

`courses/healthcare-data-foundations/modules/03-cohorts-analytic-tables/`

Handoff: the Week 3 checkpoint freezes the cohort definition and analytic-table contract before Module 04 introduces quality defects.

## Module 04 brief: Cleaning and profiling

- Week: 4.
- Hours: 16.5.
- Prerequisites: accepted Week 3 checkpoint.
- Decision owner: data-quality lead.
- Decision: whether to stop, fix, proceed, or proceed with conditions.
- Competency: detect, classify, document, and respond to consequential healthcare data defects.
- Core concepts: tidy data, types, dates, units, duplicates, coding drift, outliers, missingness, completeness, validity, consistency, uniqueness, timeliness, small cells, and decision consequences.
- Core source: a separate deterministic defect release derived from the accepted analytic table and selected relational tables.
- Lab: profile every required field, find seeded and naturally occurring issues, distinguish impossible from extreme, assess missingness patterns, trace coding changes, and make a bounded recommendation.
- Required defect log fields: issue ID, table, field, rule, observed count, affected denominator, severity, likely cause, analytic consequence, proposed response, owner, and status.
- Submission: data-quality notebook, machine-readable profile, quality-risk log, stop/fix/proceed recommendation, transformation record, reproduction check, and AI-use record.
- Out of scope: statistical imputation models, causal missing-data assumptions, production master-data management, and deleting inconvenient observations without a documented rule.

Released module package:

```text
module-04/
  README.md
  data-spec.md
  build_defect_release.py
  validate_defect_release.py
  data/
    fnd1-quality-defects.sqlite
    defect-manifest.csv
  notebooks/
    04-data-quality.ipynb
  outputs/
    quality-profile.csv
    missingness-profile.csv
    quality-risk-log.csv
  stop-fix-proceed.md
  transformation-record.md
  reproducibility-check.md
  ai-use.md
  assessment.md
  instructor-notes.md
  release.json
```

Full specification:

`docs/curriculum/courses/FND-1/modules/04-cleaning-profiling-spec.md`

Runnable package:

`courses/healthcare-data-foundations/modules/04-cleaning-profiling/`

Handoff: Module 05 receives the resolved analytic-table version plus unresolved quality flags that must remain visible.

## Module 05 brief: Descriptive results

- Week: 5.
- Hours: 16.0.
- Prerequisites: Module 04 recommendation permits continued descriptive work.
- Decision owner: clinical analytics reviewer.
- Decision: whether the descriptive evidence preserves the cohort, denominators, status, uncertainty, and source limits.
- Competency: produce exact descriptive summaries that retain their healthcare meaning.
- Core concepts: counts, proportions, central tendency, spread, two-variable summaries, cross-tabs, rates, denominator choice, stratification, table-one structure, uncertainty, limits, and standardization readiness.
- Core source: accepted analytic-table version from Module 04.
- Lab: create a one-variable profile, two cross-tabs with correct row or column denominators, selected rates, stratified descriptive table, and interpretation memo.
- Required denominator record: result ID, numerator definition, denominator definition, exclusions, missing handling, time window, unit, and interpretation limit.
- Submission milestone: descriptive notebook, exact descriptive tables, denominator registry, interpretation memo, source and transformation records, reproduction result, and AI-use record.
- Checkpoint role: the 25-percent source assessment component is drafted for inclusion in Checkpoint 2.
- Out of scope: hypothesis testing as a substitute for description, standardized or risk-adjusted estimates, regression, prediction, causal claims, and real population inference from synthetic data.

Released module package:

```text
module-05/
  README.md
  notebooks/
    05-descriptive-results.ipynb
  outputs/
    variable-profile.csv
    cross-tabs.csv
    rates.csv
    stratified-table.csv
    denominator-registry.csv
  interpretation-memo.md
  source-record.yml
  transformation-record.md
  reproducibility-check.md
  ai-use.md
  assessment.md
  instructor-notes.md
  release.json
```

Full specification:

`docs/curriculum/courses/FND-1/modules/05-descriptive-results-spec.md`

Runnable package:

`courses/healthcare-data-foundations/modules/05-descriptive-results/`

Handoff: Module 06 turns exact quality and descriptive tables into accessible inspection views without changing claims.

## Module 06 brief: Accessible charts and time-indexed data

- Week: 6.
- Hours: 16.0.
- Prerequisites: Modules 04 and 05.
- Decision owner: data-quality review panel.
- Decision: whether the quality and descriptive evidence can be inspected by all reviewers without hiding exact values or implying cause.
- Competency: create accessible descriptive and time-indexed inspection views linked to exact tables.
- Core concepts: chart mapping, chart choice, labels, contrast, non-color cues, alt text, accessible tables, subgroup and uncertainty display, time stamps, intervals, reporting context, and false-cause avoidance.
- Core source: Module 04 quality outputs and Module 05 descriptive outputs.
- Lab: create a missingness or quality view, a descriptive cohort view, and a time-indexed operational view; write exact text alternatives; compare against exact tables; and caption the supported claim.
- Required access paths: PNG, exact CSV, alt text, direct units, non-color status, readable hierarchy, and documented remaining barriers.
- Submission: cleaned analytic table, quality profile, exact descriptive tables, three figures, three alt-text records, data-quality decision, interpretation memo, source and transformation records, reproduction check, and AI-use record.
- Checkpoint role: completes the cumulative Week 6 checkpoint.
- Out of scope: the full DA-730 visualization curriculum, formal process-control claims, forecasting, causal trends, dashboards, maps, and intervention recommendations.

Planned module package:

```text
module-06/
  README.md
  notebooks/
    06-accessible-inspection.ipynb
  figures/
    quality-display.png
    descriptive-display.png
    time-display.png
  evidence-tables/
    quality-display.csv
    descriptive-display.csv
    time-display.csv
  alt-text/
    quality-display.md
    descriptive-display.md
    time-display.md
  accessibility-report.md
  interpretation-memo.md
  source-record.yml
  transformation-record.md
  reproducibility-check.md
  ai-use.md
  assessment.md
  instructor-notes.md
  release.json
```

Full future specification:

`docs/curriculum/courses/FND-1/modules/06-accessible-time-data-spec.md`

Runnable future package:

`courses/healthcare-data-foundations/modules/06-accessible-time-data/`

Handoff: the Week 6 checkpoint freezes the complete evidence set before final packaging and independent reproduction.

## Module 07 brief: Reproducible handoff and AI audit

- Week: 7.
- Hours: 16.0.
- Prerequisites: accepted or conditionally accepted Week 6 checkpoint.
- Decision owner: health-system analytics engineering lead.
- Decision: whether to accept, condition, revise, or refer the complete toolkit for downstream analysis.
- Competency: release, reproduce, audit, explain, and defend the full healthcare data workflow.
- Core concepts: reproducible handoff, release notes, semantic versions, code review, validation queries, provenance, data briefs, AI-output review, prompt logs, limits, and technical defense.
- Core source: all accepted FND-1 releases.
- Lab: assemble the toolkit, remove hidden dependencies, run from a clean checkout, compare outputs, audit one AI-assisted step, write the data brief, tag the release, and defend the handoff.
- Required reviewer roles: course faculty, SQL or data engineering, clinical informatics or healthcare data meaning, accessibility, and independent reproduction.
- Submission: exact final toolkit contract below.
- Checkpoint role: final checkpoint due on the official last day of the half-term.
- Out of scope: fitting or selecting a production model, causal inference, real clinical approval, production deployment, and unreviewed use of restricted data.

Planned module package:

```text
module-07/
  README.md
  release-checklist.md
  data-brief.md
  ai-audit.md
  defense-questions.md
  assessment.md
  instructor-notes.md
  release.json
```

Full future specification:

`docs/curriculum/courses/FND-1/modules/07-reproducible-handoff-ai-audit-spec.md`

Runnable future package:

`courses/healthcare-data-foundations/modules/07-reproducible-handoff-ai-audit/`

Handoff: an accepted final toolkit becomes the required data foundation for FND-2.

## Checkpoint 1: Validated cohort and analytic-table release

- Due: end of instructional Week 3.
- Weight: 40 percent.
- Source components preserved: 15-percent setup component plus 25-percent SQL cohort component.
- Decision owner: senior clinical data analyst and course instructor.
- Decision: whether the workspace, database, cohort, and analytic table are technically ready for quality and descriptive work.

### Exact folder

```text
checkpoint-1/
  README.md
  VERSION
  requirements.txt
  environment-note.md
  version-policy.md
  schema/
    schema-diagram.svg
    schema-description.md
    data-dictionary.csv
    source-system-comparison.md
    fhir-json-reading.md
  sql/
    01-first-extracts.sql
    02-index-cohort.sql
    03-analytic-table.sql
    04-validation.sql
  outputs/
    first-extracts.csv
    cohort-flow.csv
    analytic-table.csv
    query-checks.csv
  cohort-spec.md
  table-spec.md
  source-record.yml
  transformation-record.md
  reproducibility-check.md
  ai-use.md
  review-disposition.md
```

### Required evidence

The release must show:

- reproducible environment setup;
- meaningful Git and semantic-version history;
- declared source and rights;
- relational grain and key definitions;
- accessible schema representation;
- checked first extracts;
- readable cohort SQL;
- one index event per eligible person;
- explicit inclusion and exclusion rules;
- transparent attrition;
- one-row-per-person analytic-table grain;
- query checks;
- denominator reconciliation;
- clean reproduction; and
- verified AI-use disclosure.

### Passing dispositions

- `accept`;
- `accept with conditions`;
- `revise`; or
- `refer`.

Only `accept` and `accept with conditions` permit Module 04 to begin.

### Automatic return

Return without scoring when:

- the source is missing or unidentified;
- a private or restricted file appears;
- the environment cannot run;
- keys or grain are unstated;
- joins multiply rows without explanation;
- cohort counts do not reconcile;
- the analytic table has duplicate person rows;
- a required query or validation output is missing;
- a source value was manually changed;
- AI-generated code is unverified; or
- the learner cannot explain the SQL.

Full checkpoint specification:

`docs/curriculum/courses/FND-1/checkpoints/01-validated-cohort-release-spec.md`

Runnable checkpoint package:

`courses/healthcare-data-foundations/checkpoints/01-validated-cohort-release/`

## Checkpoint 2: Quality, descriptive, and accessible evidence release

- Due: end of instructional Week 6.
- Weight: 25 percent.
- Source component preserved: cleaning, profiling, and descriptive labs, expanded to include the Week 6 access contract.
- Decision owner: data-quality and clinical analytics review panel.
- Decision: whether the cleaned analytic table and descriptive evidence may enter final handoff packaging.

### Exact folder

```text
checkpoint-2/
  README.md
  data/
    analytic-table.csv
    data-dictionary.csv
  notebooks/
    data-quality.ipynb
    descriptive-results.ipynb
    accessible-inspection.ipynb
  quality/
    quality-profile.csv
    missingness-profile.csv
    quality-risk-log.csv
    defect-resolution.csv
  evidence-tables/
    variable-profile.csv
    cross-tabs.csv
    rates.csv
    stratified-table.csv
    denominator-registry.csv
    time-display.csv
  figures/
    quality-display.png
    descriptive-display.png
    time-display.png
  alt-text/
    quality-display.md
    descriptive-display.md
    time-display.md
  stop-fix-proceed.md
  interpretation-memo.md
  accessibility-report.md
  source-record.yml
  transformation-record.md
  reproducibility-check.md
  ai-use.md
  review-disposition.md
```

### Required evidence

- exact analytic-table version from the accepted cohort contract;
- every seeded or observed quality issue in a machine-readable risk log;
- explicit defect resolution or deferral;
- stop, fix, proceed, or proceed-with-conditions recommendation;
- exact descriptive outputs with denominator registry;
- correct missing-value handling;
- no real-population claim from synthetic data;
- three accessible figures with distinct inspection purposes;
- exact CSV alternatives;
- equivalent alt text;
- no color-only status;
- no false causal or process-control claim;
- clean notebook execution; and
- verified AI-use record.

### Automatic return

Return without scoring when:

- the analytic table differs from the accepted cohort without a versioned change record;
- a blocking defect is hidden or silently dropped;
- a denominator is absent or changes across outputs;
- missingness is treated as zero without source support;
- synthetic evidence is described as real performance;
- a figure changes an exact table value;
- accessibility depends only on color or hover;
- a time plot implies cause from descriptive chronology;
- notebooks depend on local absolute paths; or
- the learner cannot explain a cleaning or summary decision.

Future full checkpoint specification:

`docs/curriculum/courses/FND-1/checkpoints/02-quality-descriptive-accessible-release-spec.md`

Future runnable package:

`courses/healthcare-data-foundations/checkpoints/02-quality-descriptive-accessible-release/`

## Final checkpoint: Reproducible healthcare data toolkit

- Due: official last day of the assigned half-term.
- Weight: 35 percent.
- Decision owner: health-system analytics engineering lead.
- Decision: whether the toolkit may be accepted for downstream modeling or applied analysis.

### Exact folder

```text
fnd1-toolkit/
  README.md
  VERSION
  CHANGELOG.md
  requirements.txt
  release-notes.md
  sql/
    01-first-extracts.sql
    02-index-cohort.sql
    03-analytic-table.sql
    04-validation.sql
  notebooks/
    data-quality.ipynb
    descriptive-results.ipynb
    accessible-inspection.ipynb
  data/
    analytic-table.csv
    data-dictionary.csv
    cohort-flow.csv
    query-checks.csv
    quality-profile.csv
    quality-risk-log.csv
    denominator-registry.csv
  figures/
    quality-display.png
    descriptive-display.png
    time-display.png
  alt-text/
    quality-display.md
    descriptive-display.md
    time-display.md
  docs/
    cohort-spec.md
    table-spec.md
    schema-description.md
    source-record.yml
    transformation-record.md
    data-brief.md
    accessibility-report.md
    limitations.md
  validation/
    validate_release.py
    validation-results.txt
  reproducibility-check.md
  ai-use.md
  ai-audit.md
  review-disposition.md
  defense/
    handoff-brief.md
    questions-and-responses.md
```

### Final release gates

The toolkit must:

- use the accepted cohort and analytic-table version;
- preserve the exact source, rights, and fingerprints;
- regenerate the analytic table, tables, and figures;
- pass query and data validation;
- contain no hidden or local-only dependency;
- preserve all unresolved quality flags;
- state permitted and prohibited uses;
- contain an accessible schema, figures, exact tables, and text alternatives;
- include complete release notes and semantic version;
- include complete AI disclosure and one audited AI-assisted step;
- pass independent reproduction;
- pass a technical handoff defense; and
- receive `accept` or `accept with conditions`.

### Technical defense

The learner gives an eight-minute handoff and answers questions for approximately seven minutes.

Required topics:

1. source and permitted use;
2. relational schema and grain;
3. cohort definition and denominator;
4. analytic-table construction;
5. most consequential quality issue;
6. descriptive evidence and limit;
7. accessibility path;
8. reproduction and validation;
9. AI-assisted step and human checks; and
10. recommended disposition and conditions.

### Handoff questions

The learner must answer:

1. What does one row in every released table represent?
2. Which query creates the cohort and how do the counts reconcile?
3. What is the numerator and denominator for each released rate?
4. Which defect most threatens downstream use and why?
5. What was fixed, what was left unresolved, and how is that visible?
6. Why can the synthetic source support pipeline education but not real clinical inference?
7. How can another analyst reproduce the toolkit?
8. What did an AI tool contribute and how was it checked?
9. What use is permitted now?
10. What evidence would require the release to stop or be revised?

Future full checkpoint specification:

`docs/curriculum/courses/FND-1/checkpoints/03-reproducible-toolkit-spec.md`

Future runnable package:

`courses/healthcare-data-foundations/checkpoints/03-reproducible-toolkit/`

## Assessment weights

| Cumulative checkpoint | Source components | Weight |
|---|---|---:|
| Checkpoint 1, Week 3 | Environment, Git, version, and database setup, 15%; SQL cohort and analytic-table workflow, 25% | 40% |
| Checkpoint 2, Week 6 | Cleaning, profiling, descriptive analysis, and accessible inspection | 25% |
| Final checkpoint, official half-term end | Reproducible toolkit, AI audit, and technical handoff defense | 35% |
| Total |  | 100% |

### Feedback milestones

- End of Week 1: setup component receives targeted feedback before database work expands.
- End of Week 5: descriptive draft receives targeted feedback before Checkpoint 2 closes.

Milestones are required but do not add weight beyond their cumulative checkpoint.

## Shared grading criteria

| Criterion | Meaning | Primary outcomes |
|---|---|---|
| Correct | Queries, transformations, checks, and summaries are accurate and reconcile. | SQL, cohort, cleaning, description |
| Reproducible | Work reruns from the repository with environment, versions, and clear structure. | workspace, release, handoff |
| Sound data reasoning | Provenance, grain, missingness, denominators, quality, and limits are explicit. | source, cohort, quality |
| Clear and accessible | Outputs, diagrams, tables, charts, and prose work for the intended readers. | description, access, defense |
| Responsible AI use | Assistance is disclosed, traced, checked, corrected, and owned by the learner. | all modules |

### Criterion emphasis

- Checkpoint 1 emphasizes correctness, reproducibility, and sound data reasoning.
- Checkpoint 2 emphasizes correctness, sound data reasoning, and accessible communication.
- The final checkpoint weights all five criteria and includes defense performance.

### Minimum course standard

Recommended passing score: at least 80 of 100, with every noncompensable gate satisfied.

### Noncompensable gates

A high average cannot compensate for:

- protected or restricted data in the public workflow;
- missing source or rights record;
- irreconcilable cohort counts;
- duplicate final person rows;
- undocumented denominator changes;
- materially altered source values;
- hidden blocking quality defects;
- irreproducible outputs;
- inaccessible required evidence;
- undisclosed material AI use;
- inability to explain submitted SQL or Python; or
- failed technical handoff defense.

## Reproducibility policy

Every checkpoint states:

- repository URL;
- full commit hash;
- semantic version;
- operating system;
- Python version;
- SQLite version;
- pandas and notebook versions;
- R or Quarto version when used;
- exact commands;
- input fingerprints;
- output names, row counts, and fingerprints;
- validation results;
- visual and accessibility inspection;
- tester; and
- date.

A clean run begins from a fresh checkout or isolated folder. The submission may not rely on an uncommitted file, hidden extract, private notebook, manual spreadsheet change, or machine-specific absolute path.

## Data validation policy

Each data release checks, when applicable:

- file and table presence;
- row and column counts;
- header and schema;
- type conversion;
- key uniqueness;
- foreign-key coverage;
- allowed values;
- date ranges and ordering;
- missingness by field and subgroup;
- duplicate and conflict counts;
- unit consistency;
- cohort-flow conservation;
- analytic-table grain;
- numerator not exceeding denominator;
- exact-table equality with source-derived results;
- fingerprints; and
- known defect detection.

The validator reports failures. It does not silently repair source data.

## Accessibility policy

All graded evidence must be usable without relying on one sensory channel or proprietary interaction.

### Diagrams

A schema diagram includes:

- readable labels;
- non-color key relationships;
- sufficient contrast;
- SVG or another zoomable form when practical; and
- a structured text description of tables, grain, keys, and relationships.

### Tables

Tables include:

- descriptive headers;
- preserved leading zeros where identifiers require them;
- units;
- denominator fields when relevant;
- status or missingness fields;
- machine-readable CSV; and
- prose that states the main interpretation.

### Charts

Charts include:

- direct title and unit;
- non-color cues;
- sufficient contrast;
- readable labels;
- exact table;
- alt text;
- a longer description when the relationships require it;
- stated time and denominator; and
- no causal language beyond the design.

### Notebooks

Notebooks include:

- descriptive headings;
- meaningful link text;
- output descriptions;
- no information conveyed only by color;
- logical execution order; and
- an exported accessible alternative when the learning platform cannot render the notebook accessibly.

Reference standards:

- https://www.w3.org/TR/WCAG22/
- https://www.w3.org/WAI/tutorials/images/complex/

## Privacy, security, and data governance

### Public course boundary

Only approved open or synthetic data enter the repository.

No real patient record, protected health information, MGB patient data, partner-restricted file, credential, access token, or private URL enters:

- the public repository;
- a learner submission intended for public release;
- an external AI service; or
- an instructor example distributed outside its approved environment.

### Synthetic does not mean true

Learners must distinguish:

- synthetic from deidentified;
- realistic structure from real population validity;
- pipeline testing from clinical discovery;
- a seeded defect from source-observed quality; and
- a simulated person identifier from a real patient identifier.

### Small-cell rule

The synthetic core can be used to teach small-cell instability and disclosure thinking. It cannot be used to imply that a particular synthetic subgroup experiences a real disparity.

### Refer conditions

Use `refer` when:

- data rights are unclear;
- a learner introduces real or restricted data;
- identifiers or secrets are exposed;
- a source fingerprint cannot be reconciled;
- material evidence may be fabricated; or
- another governance concern exceeds the instructor's authority.

## Responsible AI and agent policy

### Permitted uses

- explain code or error messages;
- suggest tests;
- review code;
- draft documentation;
- compare SQL alternatives;
- diagnose environment failures;
- suggest accessibility checks; and
- rehearse handoff questions.

### Required disclosure

Every graded release records:

- tool and model;
- date;
- task delegated;
- material prompt or instruction;
- output used;
- learner revision;
- number and definition checks;
- source and rights checks;
- code and test checks;
- accessibility checks;
- rejected suggestions; and
- final responsibility.

### Prohibited uses

- placing protected or identifiable data into an outside tool;
- submitting unverified generated output;
- inventing source records, URLs, checksums, or test results;
- using an agent to bypass the assessed SQL, cleaning, or reasoning work;
- hiding material assistance; and
- claiming that an agent owns the final decision.

### AI audit

The final toolkit audits one material AI-assisted step from prompt through output, correction, tests, retained changes, rejected changes, and human sign-off.

## Healthcare interpretation and claim policy

The course teaches data handling, not clinical inference.

Learners may claim:

- what the synthetic source contains;
- how the source is structured;
- how many source or cohort records meet a declared rule;
- what defects were detected;
- what descriptive summaries were calculated;
- whether the release passed technical checks; and
- what limits or conditions downstream users must preserve.

Learners may not claim:

- real prevalence, quality, safety, access, utilization, cost, or treatment effect;
- causal explanations for descriptive differences;
- clinical benefit or harm from a synthetic pattern;
- representativeness of a real health system; or
- readiness of a model that has not been built and evaluated in FND-2.

## Instructor interaction and feedback

The course includes:

- one concept walkthrough each week;
- one live or recorded SQL and Python technical lab each week;
- a weekly question clinic;
- a monitored help channel with published response expectations;
- code review and targeted setup feedback in Week 1;
- cohort and SQL feedback at Checkpoint 1;
- data-quality and descriptive feedback in Week 5;
- accessible evidence review at Checkpoint 2;
- an independent reproduction clinic in Week 7; and
- a final technical handoff defense.

### Instructor roles

The teaching team needs coverage for:

- SQL and relational data;
- Python and notebooks;
- healthcare data meaning and provenance;
- reproducibility and version control;
- accessibility; and
- responsible AI use.

A clinical data architect or informatician may provide domain context. FND-1 does not require the applied-course clinician leadership block.

## Instructor package contract

Every module package contains:

```text
courses/healthcare-data-foundations/modules/<module-id>/
  README.md
  data-spec.md
  source-record.yml
  build-data.*
  validate-data.*
  lab.*
  assessment.md
  instructor-notes.md
  release.json
```

The exact files may expand when the module needs schema, SQL, notebooks, diagrams, figures, tables, or templates. A runnable module always provides:

- learner instructions;
- tiered support or a worked starting path;
- exact submission names;
- rubric and pass gates;
- answer key;
- common errors;
- timing and cut options;
- source and rights record;
- accessibility notes;
- AI verification requirements;
- automated checks;
- human review fields;
- release version; and
- known issues.

## Module specification contract

Every FND-1 module specification uses the 21-section contract:

1. identity, duration, prerequisites, and course position;
2. technical decision and named audience;
3. foundation skill and handoff;
4. assessable outcomes;
5. concept ownership and out-of-scope boundaries;
6. lesson sequence and time;
7. readings and sources;
8. dataset inventory, provenance, rights, and teaching purpose;
9. data dictionary and expected structure;
10. worked example;
11. guided practice;
12. independent exercise;
13. visualization or communication requirements;
14. exact submission package;
15. rubric and pass conditions;
16. common failures and instructor interventions;
17. accessibility, equity, privacy, and claim checks;
18. AI policy, disclosure, and verification;
19. answer key and instructor notes;
20. runnable acceptance checks; and
21. release status, reviewers, version, and known issues.

## Release maturity

| Stage | Evidence required |
|---|---|
| Specified | Course or module specification defines outcomes, sources, work, assessment, checks, and handoff. |
| Runnable candidate | Data, code, lab, assessment, instructor notes, and automated checks run from a clean checkout. |
| Alpha | Faculty, data engineering, healthcare data, accessibility, and independent-instructor reviews are recorded. |
| Beta | The course or module has been taught once and timing, defects, and revisions are recorded without learner identifiers. |
| Stable | A second instructor or program has taught it successfully and no release-blocking issue remains. |

The course specification is currently specified. No FND-1 module is yet a runnable release candidate.

## Required human review roles

Before alpha promotion, record named decisions for:

- FND-1 faculty owner;
- SQL and data engineering;
- clinical informatics or healthcare data meaning;
- source rights and provenance;
- Python and notebook teachability;
- accessibility;
- privacy and data governance;
- responsible AI use; and
- independent reproduction and teachability.

## Release and version policy

### Course version

- Patch: wording, typo, link, or noncontractual clarification.
- Minor: compatible module, source, checkpoint, scaffold, validation, or review expansion.
- Major: incompatible outcome, module ownership, data system, checkpoint, assessment weight, or final handoff change.

### Module version

Each module has its own semantic version inside the current Commons release.

### Source change

A source change requires:

- new source URL and date;
- new terms review;
- new size and fingerprint;
- new table and field inventory;
- new row counts;
- rebuilt relational data;
- rerun validation;
- new cohort and analytic-table facts when affected;
- regenerated learner outputs;
- updated answer keys;
- new version decisions; and
- human review.

Silent source refresh is prohibited.

## Build order

1. Module 01: Setting up a reproducible workspace.
2. Module 02: Databases and retrieving healthcare data.
3. Module 03: Cohorts and analytic tables.
4. Checkpoint 1: Validated cohort and analytic-table release.
5. Module 04: Cleaning and profiling.
6. Module 05: Descriptive results.
7. Module 06: Accessible charts and time-indexed data.
8. Checkpoint 2: Quality, descriptive, and accessible evidence release.
9. Module 07: Reproducible handoff and AI audit.
10. Final checkpoint: Reproducible healthcare data toolkit.
11. Complete course-level human review and release wrapper.

Each completed unit updates `docs/curriculum/BUILD-LEDGER.md`, records source and validation facts, makes a semantic-version decision, runs its checks, commits, and pushes before the next unit begins.

## Runnable acceptance plan

The course-level checker will verify:

- seven module briefs;
- exact module hours totaling 112.5;
- three checkpoint sections;
- exact assessment weights totaling 100;
- separate FND-1 and FND-2 ownership language;
- complete source DOCX fingerprint;
- official calendar URL and final-date rule;
- course package and source-record links;
- module and checkpoint paths;
- no Unicode em dash or en dash in contract files;
- no local absolute path in learner-facing documentation; and
- release metadata once module packages exist.

Each module adds its own source, data, code, output, and release checks.

## Course acceptance checklist

- [x] FND-1 is a separate straight-through technical foundation course.
- [x] FND-1 and FND-2 ownership is explicit.
- [x] The source DOCX is fingerprinted and verified across both supplied packages.
- [x] The seven source modules and hours are preserved.
- [x] The course totals 112.5 hours.
- [x] SQL and Python are graded core tools.
- [x] R remains read-run-interpret rather than a from-scratch coding requirement.
- [x] The continuing synthetic healthcare data system is defined.
- [x] Public EHR, claims, FHIR, survey, operational, and aggregate-source contrasts are defined.
- [x] The Week 3 checkpoint has exact deliverables.
- [x] The Week 6 checkpoint has exact deliverables.
- [x] The final official-date checkpoint has exact deliverables and defense questions.
- [x] Source assessment weights are preserved through cumulative checkpoint packaging.
- [x] Git, environments, semantic versions, provenance, reproducibility, and AI accountability run through the course.
- [x] Accessibility is a pass gate for diagrams, notebooks, tables, charts, and final handoff.
- [x] No real patient or restricted data enter the public course.
- [x] The module specification and package paths are defined.
- [x] Module 01 has a complete specification and runnable package.
- [x] Module 02 has a complete specification and runnable package.
- [x] Module 03 has a complete specification and runnable package.
- [x] Checkpoint 1 has a runnable assembler, templates, validator, and instructor notes.
- [x] Module 04 has a complete specification and runnable package.
- [x] Module 05 has a complete specification and runnable package.
- [ ] Module 06 has a complete specification and runnable package.
- [ ] Checkpoint 2 has a runnable assembler, templates, validator, and instructor notes.
- [ ] Module 07 has a complete specification and runnable package.
- [ ] The final checkpoint has a runnable assembler, templates, validator, and instructor notes.
- [ ] Named human reviews are recorded.
- [ ] The course has reached beta after a taught pilot.

## Unresolved implementation decisions

These decisions do not block Module 01 specification and build:

1. Lock the exact Python, pandas, Jupyter, and SQLite versions during Module 01.
2. Lock the exact Synthea table and field subset after inspecting the pinned archive in Module 02.
3. Confirm whether the pinned Synthea archive contains sufficient claims fields or whether the CMS Synthetic Medicare Claims extension is needed for the default path.
4. The deterministic defect manifest and severity rules are locked in Module 04 version 0.1.0.
5. Lock the reference cohort's exact index-period dates and counts only after Module 03 runs against the pinned database.
6. Name the faculty, data engineering, clinical informatics, accessibility, privacy, AI, and independent-instructor reviewers.
7. Confirm whether the first live cohort permits an approved SQL platform alternative while retaining SQLite as the reproducible default.

## Context-safe continuation

After this specification release, resume at Module 01.

Read:

- this course specification;
- `docs/source/fnd-1-healthcare-data-foundations-source-record.md`;
- `docs/specs/2026-08-29-curriculum-master-architecture-spec.md`; and
- `docs/curriculum/BUILD-LEDGER.md`.

Then:

1. write the 21-section Module 01 specification;
2. create the minimal cross-platform starter workspace;
3. build one Python and one SQLite smoke test;
4. create the version, environment, reproduction, and AI-use learner templates;
5. create the assessment and instructor answer key;
6. create a standard-library validator with a self-check;
7. run the workspace from a clean target;
8. update versions, checker, source status, and ledger;
9. commit and push Module 01; and
10. proceed to Module 02 without merging FND-2 content into FND-1.
