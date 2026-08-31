# APP-4 Module 02: Decision support logic, triggers, and data

- Module version: `0.1.0`
- Commons release: `0.78.0`
- Status: runnable release candidate
- Learner time: 16 hours
Course points: 20 of the 40-point Week 3 checkpoint

This module asks whether the fictional `CGH-GIM-01` advisory concept has a complete, testable, nonproduction logic and event-time input contract. Learners specify the `patient-view` hook, context, ordered branches, suppressions, terminology, units, staleness, missingness, duplicate handling, delivery failure, human ownership, and change control.

The module contains a complete Synthea 4.0.0 FHIR R4 teaching release with 1,000 synthetic adults and 811,803 resource rows. It also contains 16 deterministic Commons rule fixtures linked to synthetic patient IDs. No real patient or workplace data are used.

The fixture score and `0.20` threshold exist only to test branch mechanics. They are not predictions, performance estimates, recommendations, selected thresholds, or clinical evidence. Module 03 owns historical model, calibration, decision-threshold, and human-acceptance work.

## Build and validate

From this directory:

```powershell
python generate_synthetic_release.py --verify
python build_logic_fixtures.py --verify
python evaluate_rules.py --self-check
python build_workspace.py --self-check
python validate_workspace.py --self-check
```

Build a learner workspace:

```powershell
python build_workspace.py --target C:\path\to\app4-module02-learner
python validate_workspace.py --workspace C:\path\to\app4-module02-learner --mode starter
```

Build the reference workspace:

```powershell
python build_workspace.py --target C:\path\to\app4-module02-reference --reference
python validate_workspace.py --workspace C:\path\to\app4-module02-reference --mode complete
```

Rebuild rule results after completing the logic records:

```powershell
python evaluate_rules.py --cases data\commons\rule-test-cases.csv --output rule-test-results.csv --replace
```

Rebuilding the 1,000-patient upstream release requires the two pinned build inputs named in `data/synthetic-release/build-inputs.csv`. The generator can acquire them into a local cache and never commits those runtime binaries:

```powershell
python generate_synthetic_release.py --acquire --cache C:\path\to\synthea-cache
python generate_synthetic_release.py --generate --cache C:\path\to\synthea-cache --target C:\path\to\new-release
```

## Reference decision

The reference package is `continue with conditions`. Module 03 historical evidence and threshold analysis may begin for curriculum construction. Model fitting inside Module 02, clinical-threshold acceptance, real-patient scoring, clinical alerting, implementation, and deployment remain prohibited.
