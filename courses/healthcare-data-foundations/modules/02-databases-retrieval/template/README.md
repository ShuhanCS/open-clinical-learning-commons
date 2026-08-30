# FND-1 Module 02 learner database workspace

This workspace contains the complete 16-table Synthea April 2020 CSV sample transformed into SQLite. The source records are synthetic, not real patients. They cannot estimate clinical prevalence, utilization, quality, cost, access, or outcomes.

## Build contract

- Source archive: https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip
- Archive bytes: 8,982,431
- Archive SHA-256: `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a`
- Source tables: 16
- Source rows: 471,836
- Database: `data/fnd1_synthea_apr2020.sqlite`

The database and downloaded ZIP are ignored by Git. The manifest, schema, data dictionary, build report, FHIR examples, SQL, outputs, and learner records are committed.

## Inspect before querying

1. Read `source-record.yml` and `source-manifest.csv`.
2. Read `schema.sql` and `schema-description.md`.
3. Confirm that `build-report.json` says `pass`.
4. Compare source-table row counts with database row counts.
5. Inspect `data-dictionary.csv`, including identity-like and cost flags.
6. Read the three `fhir/*.json` examples beside `fhir-json-reading.md`.

## Run the first extracts

Complete every block in `sql/01-first-extracts.sql`, then run:

```text
python run_queries.py --database data/fnd1_synthea_apr2020.sqlite --sql sql/01-first-extracts.sql --output-dir outputs
```

The runner accepts named read-only `SELECT` or `WITH` blocks and refuses a nonempty output directory.

## Required submission

Submit every tracked file plus the exact source archive and database fingerprints in your records. Do not commit the ZIP or SQLite database. Submit:

- complete source and build records;
- `data-model.mmd` and accessible `schema-description.md`;
- completed `fhir-json-reading.md`;
- five SQL blocks and five CSV extracts;
- `validation-notes.md`;
- `ai-use.md`; and
- a clean tagged Module 02 repository state.

Do not define the adult acute-care cohort or a one-row-per-person analytic table. Those belong to Module 03.
