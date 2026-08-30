# Module 01 data specification

## Purpose

`template/data/workspace_smoke_test.csv` exists only to prove that the workspace can read a table, preserve types, load rows into SQLite, run a fixed aggregation, and return the same checked facts in Python, pandas, and R.

It is synthetic software-test data. It is not a patient table, simulated EHR extract, quality measure, outcome, utilization record, or clinical dataset. Module 02 introduces the continuing synthetic healthcare source.

## Release identity

- Data ID: `fnd1-workspace-smoke-test`
- Version: 0.1.0
- File: `template/data/workspace_smoke_test.csv`
- Format: UTF-8 CSV with header and LF line endings in Git
- Rows excluding header: 3
- Columns: 3
- SHA-256: `330da80c517c912fccd9bca3963aded84898dbb51e8b7271aa3bc53b0439c3ab`
- Synthetic: yes
- Direct identifiers: none
- Clinical meaning: none
- Redistribution: included with the Commons under CC0-1.0

## Dictionary

| Field | Type | Required | Grain role | Allowed values or rule |
|---|---|---|---|---|
| `record_id` | text | yes | primary key | Exactly `demo-001`, `demo-002`, and `demo-003` in version 0.1.0. |
| `source_label` | text | yes | display label | Exactly `synthetic-workspace-a`, `synthetic-workspace-b`, and `synthetic-workspace-c`. |
| `event_count` | integer | yes | test value | Nonnegative; version 0.1.0 contains 3, 5, and 7. |

## Immutable release checks

The validator stops if any of these facts change:

1. the file fingerprint is not the registered SHA-256;
2. the ordered header is not `record_id,source_label,event_count`;
3. row count is not 3;
4. `record_id` is not unique;
5. an `event_count` is not an integer;
6. an `event_count` is negative;
7. the total is not 15;
8. the minimum is not 3; or
9. the maximum is not 7.

## SQL structure

The supplied SQL declares:

- `record_id TEXT PRIMARY KEY`;
- `source_label TEXT NOT NULL`; and
- `event_count INTEGER NOT NULL CHECK (event_count >= 0)`.

The Python smoke test creates an in-memory SQLite database, executes the supplied schema, inserts the three CSV rows with parameterized values, and queries the fixed result. No database file persists.

## Change control

Changing a value, field, file encoding, label, or order creates a new data version and requires updated fingerprints, expected results, notebook output, R output, validator assertions, answer key, and release metadata. An instructor must not silently replace the file while keeping version 0.1.0.
