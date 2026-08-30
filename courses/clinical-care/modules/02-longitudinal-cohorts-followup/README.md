# APP-1 Module 02: Longitudinal cohorts and follow-up

This module turns the accepted APP-1 care-pathway decision into a complete longitudinal cohort and a reproducible day-30 survival risk set.

The full pinned source produces 518 initial synthetic adults, 9 index deaths, 8 early post-discharge deaths, 25 early acute returns, and 476 landmark-eligible people. Among eligible people, 129 have scheduled follow-up and 87 later acute returns occur. The primary follow-up has 87 event and 389 administrative-end dispositions.

Module 02 also creates six neutral teaching sites with overlapping baseline-risk tiers. The extension changes no source exposure, outcome, date, or event time and has a known direct site effect of zero.

## Build the reference outputs

First build the accepted FND-1 Synthea SQLite database. Then run:

```powershell
python build_longitudinal.py --database <accepted-synthea-sqlite> --target <new-output-directory>
```

The builder opens the database read-only, verifies its exact fingerprint, executes four read-only SQL files, assigns the six teaching sites, writes ten outputs, and refuses an existing target.

## Build a learner workspace

```powershell
python build_workspace.py --target <new-workspace>
```

Complete the records and SQL. Build the workspace outputs with:

```powershell
python <new-workspace>/build_longitudinal.py --database <accepted-synthea-sqlite> --sql-dir <new-workspace>/sql --target <new-workspace>/outputs
```

## Validate

```powershell
python validate_longitudinal.py . --database <accepted-synthea-sqlite>
python <new-workspace>/validate_longitudinal.py <new-workspace> --database <accepted-synthea-sqlite> --submission
```

## Boundaries

- All people and events are synthetic.
- Death is date-granular and is not clinically adjudicated.
- Scheduled encounter occurrence does not prove access, completion, quality, need, or benefit.
- SITE-A through SITE-F are synthetic teaching labels and are not real facilities.
- No real-population, causal, efficacy, fairness, site-ranking, or implementation claim is supported.

Module version: 0.1.0. Commons release: 0.50.0.

Durable specification: `docs/curriculum/courses/APP-1/modules/02-longitudinal-cohorts-followup-spec.md`.
