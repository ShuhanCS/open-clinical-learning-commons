# FND-1 Module 03: Cohorts and analytic tables

This module turns the accepted Module 02 SQLite release into a tested adult acute-care cohort and a one-row-per-person analytic table. It is a technical cohort-definition exercise using synthetic data. It does not estimate real clinical outcomes.

## Decision

A senior clinical data analyst decides whether the cohort definition, denominators, temporal windows, and analytic-table grain are ready for cleaning and profiling in Module 04.

The allowed dispositions are `accept`, `accept with conditions`, `revise`, and `refer`.

## Released result

- Source population: 1,171 synthetic patients.
- Acute event rows in the 2015 through 2019 index period: 1,243.
- Adult eligible event rows: 1,048.
- Included adults after deterministic first-event selection: 374.
- Analytic table: 374 rows and 29 fields.
- Thirty-day next state: 263 no encounter recorded, 92 scheduled care, 4 urgent care, and 15 acute return.
- Ninety-day flags: 36 acute returns and 8 deaths.

`No encounter recorded` describes the source data only. It does not mean that no care occurred.

## Build

First build the pinned Module 02 database. Then run:

```powershell
python build_cohort.py --database <module-02-workspace>\data\fnd1_synthea_apr2020.sqlite --target <new-output-directory>
```

The target must not already exist. The builder executes the four released read-only SQL files and writes five LF-terminated CSV files. It uses only the Python standard library.

Start a learner submission and run the learner's SQL with:

```powershell
Copy-Item learner-template module-03-submission -Recurse
python build_cohort.py --database <module-02-workspace>\data\fnd1_synthea_apr2020.sqlite --sql-dir module-03-submission\sql --target module-03-submission\outputs
```

Replace every `[REPLACE: ...]` prompt before validation. The output directory is intentionally absent from the starter so the builder can create it safely.

## Validate

Validate the committed release and reproduce every output from the upstream database:

```powershell
python validate_cohort.py . --database <module-02-workspace>\data\fnd1_synthea_apr2020.sqlite
```

Validate a completed learner submission with placeholder and evidence checks:

```powershell
python validate_cohort.py <module-03-submission> --database <module-02-workspace>\data\fnd1_synthea_apr2020.sqlite --submission
```

## Learning route

1. Read `cohort-spec.md` and identify the population, time zero, eligibility, exclusion order, and follow-up limits.
2. Run `sql/01-eligible-events.sql` and reconcile event rows with distinct people.
3. Run `sql/02-index-cohort.sql` and prove one deterministic index per patient.
4. Read `table-spec.md` and `data-dictionary.csv` before running `sql/03-analytic-table.sql`.
5. Run `sql/04-validation.sql`, then reconcile `outputs/cohort-flow.csv`.
6. Complete the transformation, reproducibility, and AI-use records.
7. Submit the exact package in `assessment.md` with a release disposition.

## Boundaries

- The source is the pinned Synthea April 2020 CSV sample rebuilt through Module 02.
- The source is synthetic and older. No population, quality, effectiveness, or causal claim is supported.
- This module owns cohort construction, time zero, windows, denominators, and table grain.
- Module 04 owns cleaning and profiling. Later modules own description and visualization.
- The generated Module 02 SQLite database is not copied into this module or Git.

Module version: 0.1.0. Commons release: 0.30.0.
