# Reference transformation record

## Inputs

- Accepted Module 02 SQLite database, SHA-256 `1116dda22c4297fcfeab6bf2c99bb3dbfaf9f9b5e04041b96be90719c76e704a`.
- Tables: patients, encounters, conditions, and medications.

## Ordered transformations

1. Retained emergency and inpatient encounters starting from 2015-01-01 through 2019-12-31.
2. Calculated completed age at each event and retained ages 18 or older.
3. Ranked events within patient by start and encounter ID.
4. Selected rank 1 as the index event.
5. Aggregated encounters, conditions, and medications separately across the 365 days before index start.
6. Selected the first different encounter starting after index stop and within 30 days.
7. Flagged any acute return and synthetic death after index stop and within 90 days.
8. Applied death precedence to the mutually exclusive endpoint.
9. Added source and cohort-definition versions.
10. Sorted output by patient ID and wrote UTF-8 CSV with LF line endings.

## Checks

- 1,048 eligible events become 374 unique patients and index encounters.
- 690 + 107 + 374 = 1,171 source patients.
- Analytic output contains 374 rows and 29 fields.
- All 16 SQL query checks pass.
- A clean SQL rerun reproduces all five output files byte for byte.

## Disposition

Reference disposition: `accept with conditions` for teaching use. Named faculty and human technical review remain pending before alpha promotion.
