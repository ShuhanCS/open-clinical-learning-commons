# Assessment: tested cohort and analytic table

## Submission

Submit a folder tagged `fnd1-cohort-v0.1.0` containing:

```text
module-03-submission/
  VERSION
  README.md
  cohort-spec.md
  table-spec.md
  data-dictionary.csv
  source-record.yml
  transformation-record.md
  reproducibility-check.md
  ai-use.md
  sql/
    01-eligible-events.sql
    02-index-cohort.sql
    03-analytic-table.sql
    04-validation.sql
  outputs/
    eligible-events.csv
    index-cohort.csv
    analytic-table.csv
    cohort-flow.csv
    query-checks.csv
```

`VERSION` must contain `0.1.0`. Run your SQL against the accepted Module 02 database. Do not edit generated CSV files by hand. End the README with `accept`, `accept with conditions`, `revise`, or `refer`, plus the evidence for that disposition.

## Required explanation

Explain in your own words:

1. the source population and decision;
2. why event count differs from person count;
3. completed-age logic;
4. index-event ordering and tie-breaking;
5. time zero and each window boundary;
6. why history tables are aggregated separately;
7. what `No encounter recorded` does and does not mean;
8. which fields occur after index; and
9. how you reproduced and verified the package.

## Scoring

| Criterion | Points |
|---|---:|
| Written cohort definition and time zero | 20 |
| Eligible-event and deterministic index SQL | 20 |
| Analytic-table grain, windows, and fields | 25 |
| Flow, denominators, and query checks | 20 |
| Reproduction, provenance, and transformation record | 10 |
| Accessibility and AI accountability | 5 |
| Total | 100 |

Passing requires at least 80 points and every gate below.

## Noncompensable gates

- exact upstream source;
- eligibility definition;
- one index per patient;
- one analytic row per patient;
- cohort-flow conservation;
- correct window boundaries;
- no history join multiplication;
- follow-up coverage stated;
- post-index fields labeled;
- reproducible output;
- material AI use disclosed; and
- an allowed release disposition.

The Module 03 work contributes 25 percentage points to the cumulative 40-percent Week 3 checkpoint.

Start from `learner-template`, replace every prompt, run your four SQL files through `build_cohort.py --sql-dir`, and validate the completed folder with `validate_cohort.py --submission`.
