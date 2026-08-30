# Module 02 instructor notes and answer key

## Teaching purpose

Learners should finish the week able to explain what one row means, how tables connect, what the source actually contains, and whether the database can safely support the next technical step. Do not let the week become an early cohort assignment.

## 16-hour plan

| Activity | Hours |
|---|---:|
| Source systems, provenance, archive, and rights | 1.50 |
| Relational grain, keys, types, and optionality | 2.50 |
| Complete database build and source-manifest audit | 2.00 |
| Schema diagram and accessible text description | 2.00 |
| SQL SELECT, WHERE, ORDER BY, GROUP BY, and safe extracts | 3.00 |
| FHIR R4 Patient, Encounter, and Observation reading | 1.50 |
| Validation, minimization, and identity-like/cost fields | 1.50 |
| Independent extracts, AI verification, and handoff | 2.00 |
| Total | 16.00 |

## Reference build facts

- Archive: 8,982,431 bytes.
- Archive SHA-256: `4194b18c11eaedcf0d5d5dd448d8ac9661f14381e2ef9f109215dc42266cd38a`.
- Uncompressed CSV bytes: 82,293,440.
- Source tables: 16.
- Source rows: 471,836.
- Database dictionary rows: 177.
- Tested database bytes: 141,234,176.
- Tested database SHA-256: `1116dda22c4297fcfeab6bf2c99bb3dbfaf9f9b5e04041b96be90719c76e704a`.
- Foreign-key failures: 0.
- Integrity: `ok`.
- Base validator: 96 checks.
- Complete submission validator: 126 checks.

The SQLite byte fingerprint may change after a supported SQLite-version update even when logical contents match. The release gates logical table, relationship, dictionary, FHIR, and query facts. The tested fingerprint remains an audit record.

## Table and relationship answer key

- `patients.id` is the parent for every patient reference.
- `organizations.id` parents providers and encounters.
- `providers.id` parents encounter provider references.
- `payers.id` parents encounters, medications, and payer transitions.
- `encounters.id` parents clinical event tables.
- Observation encounter is optional; 30,363 rows have no encounter reference.
- Other nonblank registered references have zero orphans.
- Nine tables lack a source `Id` and receive stable `source_row_number` values.
- The zero-row supplies table remains present because absence is a source fact.

## Reference extract row counts

- table inventory: 16;
- encounter class counts: 6;
- observation linkage: 3;
- selected timeline: 25; and
- numeric observation sample: 25.

## FHIR example answer key

- Patient ID: `00185faa-2760-4218-9bf5-db301acf8274`.
- Encounter ID: `6b5bfe89-1c58-42e8-87c4-847b542d5f0b`.
- Observation ID: `synthea-observation-191026`.
- Encounter subject resolves to the Patient.
- Observation subject resolves to the Patient.
- Observation encounter resolves to the Encounter.
- Observation has a numeric value and nonempty unit.

These examples illustrate shape and references only.

## Common errors

| Error | Correction |
|---|---|
| Counts ZIP or codes as numeric measures | Keep identifiers and codes as text. |
| Drops the zero-row supplies table | Preserve it and explain that zero rows are a source fact. |
| Makes every observation encounter required | Preserve 30,363 null encounter references. |
| Calls generated row numbers source IDs | Label them transparent technical surrogates. |
| Uses synthetic names or costs in every extract | Start with minimized views and justify any broader field. |
| Treats FHIR JSON as another flat table | Trace nested fields and references explicitly. |
| Claims full FHIR conformance | State that the examples are teaching mappings. |
| Builds a cohort early | Return to table retrieval; move index and eligibility logic to Module 03. |
| Commits the database | Remove it from tracking; preserve source and build records. |
| Copies a plausible AI join | Verify keys, row counts, and duplication against schema and database. |

## Review sequence

1. Revalidate the source archive.
2. Build to a new target.
3. Run the 96-check database validation.
4. Inspect diagram and text alternative.
5. Run the learner's five SQL blocks and compare exact outputs.
6. Read the FHIR mapping record.
7. Review validation and AI-use notes.
8. Run the 126-check submission validation.
9. Record score, gates, disposition, conditions, owner, and date.

## Human review still required

Faculty, data engineering, healthcare-data meaning, FHIR, accessibility, source rights, privacy, responsible-AI, and independent-instructor reviews gate alpha promotion.
