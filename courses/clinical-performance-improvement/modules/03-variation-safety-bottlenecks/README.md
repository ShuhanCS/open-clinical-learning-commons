# APP-3 Module 03: Variation, safety signals, and bottlenecks

This 16.5-hour module turns the accepted Module 02 measures into a bounded performance diagnostic for the fictional `CGH-ED-01` service. Learners choose chart families, calculate exact limits, apply three predeclared signal rules, audit safety undercapture, compare process stages, and defend one human escalation rule.

The reference uses Weeks 1 through 24 as a provisional baseline and Weeks 25 through 52 for evaluation. It produces nine signal records. Stage, queue, throughput, balancing, control, and recovery evidence support a roomed-to-clinician constraint during evening shifts in Weeks 35 through 44. Root cause and staffing adequacy remain unestablished.

## Verify the accepted evidence

```powershell
python freeze_upstream.py --self-check
python build_diagnostic.py --self-check
python build_workspace.py --self-check
python validate_workspace.py --self-check
```

## Build learner and reference workspaces

```powershell
python build_workspace.py --target "$env:TEMP\app3-module03-learner"
python validate_workspace.py "$env:TEMP\app3-module03-learner" --starter

python build_workspace.py --target "$env:TEMP\app3-module03-reference" --reference
python validate_workspace.py "$env:TEMP\app3-module03-reference"
```

The builder refuses to overwrite an existing target. Module 03 permits construction of the 40-point Week 3 checkpoint. It does not authorize Module 04, staffing change, clinical action, automated action, or implementation.

The durable teaching specification is `docs/curriculum/courses/APP-3/modules/03-variation-safety-bottlenecks-spec.md`.
