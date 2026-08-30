# Data specification

## Source layer

The module uses the complete pinned Synthea April 2020 CSV release already accepted by FND-1. The source is synthetic and contains no real patient records.

- Archive: https://synthetichealth.github.io/synthea-sample-data/downloads/synthea_sample_data_csv_apr2020.zip
- Bytes: 8,982,431.
- SHA-256: `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a`.
- Tables: 16.
- Rows: 471,836.
- Uncompressed bytes: 82,293,440.

`data/source-table-inventory.csv` freezes every source table's archive path, bytes, rows, columns, and SHA-256.

## Reference pathway

1. Select each synthetic adult's first emergency or inpatient encounter starting on or after 2010-01-01 and before 2019-04-01.
2. Use encounter stop as discharge origin.
3. Count death or an emergency/inpatient return after discharge and through day 30 as an early branch.
4. At day 30, include people alive and without an early acute return.
5. Classify scheduled follow-up when an ambulatory, outpatient, or wellness encounter occurs after discharge and through day 30.
6. Follow landmark-eligible people for the first emergency or inpatient return after day 30 and through day 365.

The fixed profile is 518 initial people, 8 early deaths, 25 early acute returns, 485 landmark-eligible people, 129 with scheduled follow-up, and 87 later acute returns. Later outcomes split 25/62 between exposed and unexposed groups. The landmark population spans 64 index organizations.

## Module boundary

Module 01 carries only the complete source inventory and aggregate feasibility profile. The full archive and 141-MB SQLite database are verified but not duplicated in the learner package. Module 02 owns full source assembly, final phenotype SQL, person-level cohort, censoring, and the deterministic six-site teaching extension.

## Interpretation boundary

The fixed counts show that a longitudinal teaching case is feasible. They do not estimate real care, utilization, access, quality, equity, site performance, treatment effect, or clinical benefit. Raw 64-organization ranking is not ready.
