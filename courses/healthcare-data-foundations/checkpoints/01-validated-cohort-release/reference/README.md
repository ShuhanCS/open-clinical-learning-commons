# FND-1 Checkpoint 1: Validated cohort and analytic-table release

## Audience and decision

This reference release is for a data-quality lead. A senior clinical data analyst and course instructor decide whether the technical foundation is ready for Module 04.

## Released evidence

The tested environment leads to the pinned 16-table Synthea database, five checked first extracts, 1,048 adult eligible acute events, 374 deterministic index encounters, and a 374-row by 29-field analytic table. All 16 cohort query checks pass and the four-step flow conserves all 1,171 source patients.

## Folder map

`schema/` contains source, relationship, dictionary, FHIR, and source-system evidence. `sql/` contains retrieval and cohort logic. `outputs/` contains exact extracts and cohort data. The root records provenance, transformation, reproduction, AI use, scoring, and review disposition.

## Reproduce this release

Build Module 02 from the pinned archive, run its reference extracts, run Module 03 against that database into a new output target, then run `python validate_checkpoint.py <checkpoint-folder>`. Every released CSV must reproduce byte for byte.

## Known limits

All records are synthetic and the source is older. The outputs do not estimate real utilization, quality, access, mortality, or treatment effects. Named human review and non-Windows reproduction remain conditions before alpha promotion.

## Next use

The technical reference supports `accept with conditions`. Module 04 may use analytic-table version 0.1.0 only after the course decision owners confirm the human-review conditions.
