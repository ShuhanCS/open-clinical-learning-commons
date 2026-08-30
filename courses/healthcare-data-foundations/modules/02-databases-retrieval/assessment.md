# Module 02 assessment: Relational database and first retrievals

## Decision

The clinical data architect decides whether the database preserves source meaning well enough to begin cohort definition in Module 03.

Allowed dispositions are `accept`, `accept with conditions`, `revise`, and `refer`.

## Exact submission

Submit the tagged Module 02 repository state containing:

1. `VERSION` equal to `0.1.0`;
2. exact `source-manifest.csv`;
3. completed `source-record.yml`;
4. exact `schema.sql`;
5. generated `build-report.json`;
6. generated `data-dictionary.csv`;
7. completed `data-model.mmd`;
8. completed accessible `schema-description.md`;
9. generated `fhir/patient.json`, `fhir/encounter.json`, and `fhir/observation.json`;
10. completed `fhir-json-reading.md`;
11. completed `sql/01-first-extracts.sql`;
12. five exact CSV files in `outputs/`;
13. generated `validation-report.json`;
14. completed `validation-notes.md`;
15. completed `ai-use.md`; and
16. the full commit hash identified by annotated tag `fnd1-database-v0.1.0`.

Do not commit the 8.98 MB source ZIP or 141 MB generated SQLite file. They are recreated from the pinned source and build code.

## Five required extracts

| Name | Required result |
|---|---|
| `table-inventory` | 16 tables with registered row and column counts. |
| `encounter-class-counts` | 6 encounter classes in deterministic count order. |
| `observation-linkage` | Numeric/text by linked or missing encounter reference, 3 rows. |
| `selected-patient-timeline` | First 25 encounters for the deterministic highest-encounter patient. |
| `numeric-observation-sample` | First 25 numeric observations with units in deterministic order. |

## Rubric

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Provenance and source fidelity | 15 | Archive and member fingerprints, rights, retrieval, synthetic status, and source age are correct. |
| Relational model and grain | 25 | All 16 grains, keys, optionality, relationships, surrogate choices, and minimized views are correct in diagram and text. |
| SQL retrieval | 25 | Five read-only queries are correct, deterministic, readable, and reproduce exact reference outputs. |
| Validation and technical recommendation | 20 | 126 checks pass; learner interprets integrity, foreign keys, missing links, types, and limits; stop/fix/proceed advice fits evidence. |
| FHIR and JSON reading | 10 | Patient, Encounter, and Observation references resolve; relational and nested shapes are compared; mapping limits are stated. |
| Accessibility, minimization, and AI accountability | 5 | Diagram has a full text alternative; identity-like/cost fields are minimized; material AI use is verified and disclosed. |
| Total | 100 |  |

## Pass conditions

Pass requires:

- at least 80 points;
- source-fingerprint gate passed;
- database-integrity gate passed;
- zero-foreign-key-failure gate passed;
- exact-retrieval gate passed;
- accessible-schema gate passed;
- FHIR-reference gate passed;
- privacy, minimization, and AI-disclosure gates passed; and
- `accept` or `accept with conditions` disposition.

A score cannot compensate for a failed gate.

## Scope gate

The submission fails the scope gate if it defines the graded Module 03 cohort, selects an index event for analysis, calculates cohort attrition, or builds a one-row-per-person analytic table. Module 02 prepares the relational source; Module 03 owns cohort logic.
