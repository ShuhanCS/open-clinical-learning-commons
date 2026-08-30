# Module 02 data specification

## Release identity

- Data release: `fnd1-synthea-relational-apr2020`
- Version: 0.1.0
- Source archive: Synthea April 2020 CSV sample
- Source archive bytes: 8,982,431
- Source archive SHA-256: `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a`
- Source members: 16 CSV files
- Source rows: 471,836
- Source columns across files: 168
- Database dictionary rows: 177, including 9 transparent surrogate row numbers
- Generated database: SQLite, `PRAGMA user_version = 1`
- Synthetic: yes
- Real patient records: none

## Table inventory

| Table | Grain | Rows | Source columns | Database key |
|---|---|---:|---:|---|
| patients | one synthetic patient | 1,171 | 25 | source `id` |
| organizations | one synthetic organization | 1,119 | 11 | source `id` |
| providers | one synthetic provider | 5,855 | 12 | source `id` |
| payers | one synthetic payer | 10 | 21 | source `id` |
| encounters | one synthetic encounter | 53,346 | 15 | source `id` |
| allergies | one allergy row | 597 | 6 | generated `source_row_number` |
| careplans | one care-plan row | 3,483 | 9 | source `id` |
| conditions | one condition row | 8,376 | 6 | generated `source_row_number` |
| devices | one device row | 78 | 7 | generated `source_row_number` |
| imaging_studies | one imaging-study row | 855 | 10 | source `id` |
| immunizations | one immunization row | 15,478 | 6 | generated `source_row_number` |
| medications | one medication row | 42,989 | 13 | generated `source_row_number` |
| observations | one observation row | 299,697 | 8 | generated `source_row_number` |
| payer_transitions | one patient-payer coverage period | 3,801 | 5 | generated `source_row_number` |
| procedures | one procedure row | 34,981 | 8 | generated `source_row_number` |
| supplies | one supply row | 0 | 6 | generated `source_row_number` |

Exact member sizes and SHA-256 values are registered in `source-manifest.csv`.

## Relational integrity

The pinned source has:

- 1,171 unique patient IDs;
- 53,346 unique encounter IDs;
- 1,119 unique organization IDs;
- 5,855 unique provider IDs;
- 10 unique payer IDs;
- zero orphan patient references;
- zero orphan nonblank encounter references;
- zero orphan organization references;
- zero orphan provider references;
- zero orphan payer references; and
- 30,363 observations with an intentionally blank encounter reference.

The blank observation encounter is loaded as `NULL` and preserved as optional. It is not fabricated or dropped.

## Encounter classes

| Class | Rows |
|---|---:|
| ambulatory | 18,936 |
| wellness | 19,106 |
| outpatient | 9,003 |
| urgentcare | 2,373 |
| emergency | 2,090 |
| inpatient | 1,838 |

## Observation types

- Numeric: 278,488.
- Text: 21,209.
- Missing units: 12,719.
- Missing encounter reference: 30,363.

Missing units are not automatically errors because text observations and some coded values do not use numeric units.

## Field handling

- Empty source strings load as SQL `NULL`.
- Identifiers and codes load as text, preserving leading zeros and source formatting.
- Declared count and year fields load as integers.
- Declared monetary, coordinate, and quantitative summary fields load as real numbers.
- Dates and timestamps remain ISO-like source text so learners can inspect the source representation before later analytic transformation.
- Tables without source IDs receive a stable 1-based source-row ordinal.

## Identity-like and cost fields

The full source is synthetic, but the dictionary flags identity-like and financial fields. The three core views exclude fields such as synthetic names, addresses, SSNs, driver identifiers, passports, provider names, payer details, and costs when they are not required for first retrieval.

This teaches minimization without pretending the source columns do not exist.

## Database invariants

A valid release has:

- all archive and member fingerprints unchanged;
- all 16 tables present;
- exact rows and columns;
- exact field order and declared SQLite types;
- zero foreign-key failures;
- SQLite integrity `ok`;
- all three minimized views;
- 177 data-dictionary rows;
- linked FHIR example references; and
- exact reference-extract results.

## Change control

A source refresh requires a new archive fingerprint, complete member inventory, rebuilt database, new table and field facts, rerun FHIR mapping, regenerated extracts, updated answer key, and semantic-version decision. Silent refresh is prohibited.
