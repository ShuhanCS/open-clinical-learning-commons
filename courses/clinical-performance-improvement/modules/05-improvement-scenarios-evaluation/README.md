# APP-3 Module 05: Improvement scenarios and evaluation

This 16-hour module uses the accepted Module 04 forecast to compare no change, flex clinician coverage, fast-track activation, and a combined bounded rule for the fictional `CGH-ED-01` service. Learners validate a guided discrete-event model, run five uncertainty conditions with 200 paired replications each, preserve failed results, examine access and workforce consequences, and design a prospective evaluation.

The reference result selects no option for feasibility review. S01 improves P90 wait by 21.244986 minutes but misses the 10-minute median-wait rule. S02 improves completion while worsening median and P90 waits. S03 also misses the point-demand gates. This is a correct no-selection result, not a failed assignment. The full 25-point submission is counted once at the cumulative Week 6 checkpoint.

## Verify the accepted evidence

```powershell
python freeze_upstream.py --self-check
python build_scenarios.py --self-check
python build_workspace.py --self-check
python validate_workspace.py --self-check
```

## Build learner and reference workspaces

```powershell
python build_workspace.py --target "$env:TEMP\app3-module05-learner"
python validate_workspace.py "$env:TEMP\app3-module05-learner" --starter

python build_workspace.py --target "$env:TEMP\app3-module05-reference" --reference
python validate_workspace.py "$env:TEMP\app3-module05-reference"
```

The builder refuses to overwrite an existing target. Module 06 receives the exact no-selection result, failed sensitivities, evaluation plan, and claim limits. It may plan feasibility, monitoring, and the embedded ML comparison, but it may not authorize implementation.

The durable teaching specification is `docs/curriculum/courses/APP-3/modules/05-improvement-scenarios-evaluation-spec.md`.
