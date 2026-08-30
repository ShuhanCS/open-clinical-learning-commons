# APP-1 Module 01: Framing a care-pathway decision

This module turns a broad post-acute follow-up idea into a complete clinical decision contract before any new cohort or model is built.

The reference case uses the full pinned 16-table, 471,836-row Synthea release to decide whether a 30-day scheduled follow-up pathway is measurable. The fixed feasibility profile has 518 initial synthetic adults, 8 early deaths, 25 early acute returns, 485 day-30 landmark-eligible people, 129 with scheduled follow-up, and 87 later acute returns. Sixty-four sparse source organizations make raw site ranking inappropriate.

No real patient data are used. The package supports technical education and prospective-test design only.

## Build a learner workspace

```powershell
python build_workspace.py --target <new-target-folder>
python validate_workspace.py <new-target-folder> --starter
```

Complete the nine learner records, then run validation without `--starter`.

## Build the reference

```powershell
python build_workspace.py --reference --target <new-target-folder>
python validate_workspace.py <new-target-folder>
```

## Reproduce the feasibility profile

First build the full pinned database with the accepted FND-1 Module 02 builder. Then run:

```powershell
python profile_source.py <synthea-sqlite-path> --output <new-output.csv>
```

The profiler reads the database and writes only the aggregate eleven-row feasibility record. It never changes the database.

## Durable specification

`docs/curriculum/courses/APP-1/modules/01-care-pathway-decision-spec.md`
