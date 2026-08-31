# APP-3 Module 06: Feasibility, monitoring, and embedded machine learning

This 16-hour module completes the Week 6 application block. Learners screen the accepted no-selection scenario result, specify monitoring and escalation, build an accessible static dashboard, and compare one fixed gradient-boosted forecast with the accepted transparent forecast.

The reference challenger passes 7 of 8 replacement rules. Its MAE improvement is 0.731788 arrivals per shift, below the declared 0.750000 requirement. The transparent forecast remains accepted. The result does not authorize a scenario, test, staffing change, clinical action, implementation, production model, or deployment.

## Package map

- `upstream/`: 33 immutable files plus the handoff manifest from Modules 04 and 05.
- `outputs/`: 19 deterministic feasibility, monitoring, dashboard, and ML outputs.
- `reference/`: complete instructor records.
- `template/`: learner records with explicit placeholders.
- `ml-contract.json`: target, folds, features, model, and decision rules.
- `build_evidence.py`: deterministic evidence builder.
- `build_workspace.py`: protected learner or reference assembler.
- `validate_workspace.py`: release, workspace, and failure-route validator.

## Run the checks

From this directory:

```powershell
python freeze_upstream.py --self-check
python build_evidence.py --self-check
python build_workspace.py --self-check
python validate_workspace.py --self-check
```

Build a learner workspace:

```powershell
python build_workspace.py --target C:\path\to\new\app3-module06-workspace
```

Build the complete reference:

```powershell
python build_workspace.py --target C:\path\to\new\app3-module06-reference --reference
```

The builders refuse an existing destination. The supported environment is Python 3.12.10, NumPy 2.0.2, pandas 3.0.3, and scikit-learn 1.9.0.
