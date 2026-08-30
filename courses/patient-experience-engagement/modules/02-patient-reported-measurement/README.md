# APP-2 Module 02: Patient-reported measurement and scale construction

This 16-hour lab asks one decision: are the exact patient-reported items, scoring rules, access plan, and naming boundary ready for a response and representation study?

The current teaching choice is the updated HCAHPS Q22/Q23 Discharge Information pair. Q20 remains a separate individual item, and Q21 controls whether Q22/Q23 apply. The package includes the full current official instrument suite, QAG V19.0 guidance, the full public CMS HCAHPS file, and a visibly synthetic 240-row response fixture.

Run from this directory:

```powershell
python build_measurement.py --verify-committed
python build_measurement.py --self-check
python build_workspace.py --self-check
python validate_workspace.py --self-check
```

Build a learner or reference workspace into a new path:

```powershell
python build_workspace.py --target ..\app2-module02-learner
python build_workspace.py --target ..\app2-module02-reference --reference
python validate_workspace.py ..\app2-module02-reference
```

The public CMS file is hospital-level reporting, not patient-level evidence. The synthetic file is procedural teaching data, not observed experience. This package does not authorize survey fielding, clinical action, hospital ranking, or comparison of a partial local item set with official adjusted HCAHPS scores.
