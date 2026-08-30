-- Complete all five named, read-only query blocks.
-- Do not define a cohort or one-row-per-person analytic table in Module 02.

-- query: table-inventory
[REPLACE: list all source tables with registered rows and columns in table-name order]

-- query: encounter-class-counts
[REPLACE: count encounters by encounter class and use a deterministic order]

-- query: observation-linkage
[REPLACE: count numeric/text observations by linked versus missing encounter reference]

-- query: selected-patient-timeline
[REPLACE: select one deterministic patient with the most encounters, then return the first 25 encounters in time order]

-- query: numeric-observation-sample
[REPLACE: return the first 25 numeric observations with nonmissing units in deterministic order]
