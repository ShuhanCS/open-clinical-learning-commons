# Cumulative transformation record

## Version chain

Module 01, Module 02, Module 03, and checkpoint versions are each 0.1.0. The checkpoint preserves the accepted setup tag and cohort definition without a silent source or interface change.

## Source to database

The build verifies the 8,982,431-byte archive and its SHA-256, creates the declared SQLite schema, loads all 471,836 rows, converts empty strings to null, adds nine transparent source-row ordinals, creates three minimized views, and verifies integrity and relationships.

## Database to cohort

Read-only SQL retains emergency and inpatient encounters in 2015 through 2019, calculates completed age, filters adults before ranking, orders by start and encounter ID, and selects one index per patient. The flow conserves all 1,171 source patients.

## Cohort to analytic table

Separate CTEs aggregate 365-day encounter, acute, condition, and medication history. Follow-up begins after index stop. The table records the first 30-day state, 90-day return and death flags, endpoint precedence, source coverage, and release versions.

## Immutable handoff

Module 04 receives analytic-table version 0.1.0: 374 rows, 29 fields, 121,787 bytes, and SHA-256 `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a`. Module 04 creates a separate defect layer and cannot edit this release in place.
