# FND-1 Module 02: Databases and retrieving healthcare data

Module 02 builds the complete pinned Synthea April 2020 CSV sample into a relational SQLite teaching database. Learners decide whether the schema preserves source grain, keys, types, relationships, and provenance well enough for Module 03 cohort work.

- Course: FND-1 Healthcare Data Foundations
- Week: 2
- Learner work: 16 hours
- Module version: 0.1.0
- Commons release: 0.29.0
- Status: runnable release candidate; human review pending
- Decision owner: clinical data architect
- Decision: accept, accept with conditions, revise, or refer the relational release
- Source: 16 synthetic Synthea CSV tables, 471,836 rows, 82,293,440 uncompressed bytes
- Generated SQLite reference: 141,234,176 bytes in the tested environment

No real patient records are used. Synthea values do not estimate real prevalence, utilization, quality, cost, access, or outcomes.

## Source release

- Landing page: https://synthea.mitre.org/downloads
- Archive: https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip
- Archive bytes: 8,982,431
- Archive SHA-256: `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a`
- CSV dictionary: https://github.com/synthetichealth/synthea/wiki/CSV-File-Data-Dictionary
- Repository: https://github.com/synthetichealth/synthea
- License: https://github.com/synthetichealth/synthea/blob/master/LICENSE

## What the build preserves

The database loads all source rows and all source fields from:

- patients;
- organizations;
- providers;
- payers;
- payer transitions;
- encounters;
- allergies;
- care plans;
- conditions;
- devices;
- imaging studies;
- immunizations;
- medications;
- observations;
- procedures; and
- supplies, including its zero-row state.

Source tables without an `Id` field receive `source_row_number`, a stable ordinal surrogate that makes row identity explicit without pretending the source supplied a natural primary key.

Three views support minimized retrieval:

- `v_patients_minimal`;
- `v_encounters_core`; and
- `v_observations_core`.

The full synthetic source fields remain available for schema study. The learner extracts avoid identity-like and cost fields when they are not needed.

## Build a learner workspace

Use an already downloaded archive:

```text
python courses/healthcare-data-foundations/modules/02-databases-retrieval/build_database.py --source-zip PATH_TO_ZIP --target learner-database-workspace
```

Or ask the builder to download the pinned archive:

```text
python courses/healthcare-data-foundations/modules/02-databases-retrieval/build_database.py --download --target learner-database-workspace
```

The target must not exist. The builder does not overwrite another directory.

The ZIP and generated 141 MB SQLite file are ignored by Git. The reproducible build code, exact source manifest, build report, schema, data dictionary, FHIR examples, SQL, and learner records remain portable.

## Validate the database

```text
python courses/healthcare-data-foundations/modules/02-databases-retrieval/validate_database.py learner-database-workspace --source-zip PATH_TO_ZIP
```

The reference database passes 96 grouped checks. A completed submission passes 126:

```text
python courses/healthcare-data-foundations/modules/02-databases-retrieval/validate_database.py learner-database-workspace --source-zip PATH_TO_ZIP --submission
```

## Run reference extracts

```text
python courses/healthcare-data-foundations/modules/02-databases-retrieval/run_queries.py --database learner-database-workspace/data/fnd1_synthea_apr2020.sqlite --sql courses/healthcare-data-foundations/modules/02-databases-retrieval/reference-first-extracts.sql --output-dir reference-outputs
```

Expected output rows:

| Extract | Rows |
|---|---:|
| `table-inventory.csv` | 16 |
| `encounter-class-counts.csv` | 6 |
| `observation-linkage.csv` | 3 |
| `selected-patient-timeline.csv` | 25 |
| `numeric-observation-sample.csv` | 25 |

These are retrieval exercises. They do not define a cohort or analytic table.

## FHIR R4 reading examples

The build derives one linked Patient, Encounter, and numeric Observation JSON example. The examples are transparent teaching mappings from the CSV rows, not a certified FHIR server export or a complete conformance claim.

- Patient: https://hl7.org/fhir/R4/patient.html
- Encounter: https://hl7.org/fhir/R4/encounter.html
- Observation: https://hl7.org/fhir/R4/observation.html

## Maintainer checks

```text
python courses/healthcare-data-foundations/modules/02-databases-retrieval/build_database.py --self-check
python courses/healthcare-data-foundations/modules/02-databases-retrieval/run_queries.py --self-check
python courses/healthcare-data-foundations/modules/02-databases-retrieval/validate_database.py --self-check
```

Durable specification:

`docs/curriculum/courses/FND-1/modules/02-databases-retrieval-spec.md`
