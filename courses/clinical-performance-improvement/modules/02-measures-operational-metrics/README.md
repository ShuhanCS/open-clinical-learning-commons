# APP-3 Module 02: Measures and operational metrics

This 16-hour module turns the `CGH-ED-01` decision boundary into a reproducible operational measure release. Learners clean nine linked synthetic tables with SQL, validate their logic independently with Python, specify 17 measures, and defend every denominator, unavailable state, and claim limit.

The raw release contains 318,732 rows across encounters, process events, staffing, queue snapshots, safety candidates, calendar demand, scenarios, generated truth, and a defect register. Raw defects are never overwritten. The accepted clean layer contains 43,628 adult encounters and passes 30 exact query checks.

## Build the accepted measures

```powershell
python build_measures.py --self-check
```

## Build and validate workspaces

```powershell
python build_workspace.py --target "$env:TEMP\app3-module02-learner"
python validate_workspace.py "$env:TEMP\app3-module02-learner" --starter

python build_workspace.py --target "$env:TEMP\app3-module02-reference" --reference
python validate_workspace.py "$env:TEMP\app3-module02-reference"
```

Builders refuse to overwrite an existing target. Module 02 releases measures only. Bottleneck diagnosis, staffing proposals, clinical action, causal claims, and implementation decisions remain prohibited.

The full teaching specification is at `docs/curriculum/courses/APP-3/modules/02-measures-operational-metrics-spec.md`.
