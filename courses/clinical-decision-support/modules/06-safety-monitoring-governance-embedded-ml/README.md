# APP-4 Module 06: Safety, monitoring, governance, and embedded machine learning

This 16-hour module completes the Week 6 application block. Learners review 22 hazards, turn every Module 05 failure into a governed safety control, specify 20 monitoring measures and 12 escalation routes, and compare one fixed gradient-boosted challenger with the accepted transparent model.

The reference challenger passes 8 of 11 replacement rules. It improves Brier score on the untouched evaluation sets, but its weighted ROC AUC is 0.00743486 lower on the temporal holdout and 0.01928938 lower on the later stress set. Its worst supported subgroup AUC degradation is 0.10385240. The transparent model remains accepted for the teaching comparison. No threshold is selected, and no clinical or production action is authorized.

## Package map

- `outputs/`: deterministic safety, monitoring, and model-comparison evidence.
- `upstream/module05/`: the complete immutable 341-file Module 05 reference workspace, assembled into each learner or reference release.
- `reference/`: complete instructor records.
- `template/`: learner records with explicit placeholders.
- `ml-contract.json`: the fixed split, features, model settings, and replacement rules.
- `build_evidence.py`: the deterministic evidence builder.
- `build_workspace.py`: the protected learner or reference assembler.
- `validate_workspace.py`: the release and deliberate-failure validator.

## Run the checks

From this directory:

```powershell
python build_evidence.py --self-check
python build_workspace.py --self-check
python validate_workspace.py --self-check
```

Build a learner workspace:

```powershell
python build_workspace.py --target C:\path\to\new\app4-module06-workspace
```

Build the complete reference:

```powershell
python build_workspace.py --target C:\path\to\new\app4-module06-reference --reference
```

The builders refuse an existing destination. The supported environment is Python 3.12, NumPy 2.0.2, and scikit-learn 1.9.0.
