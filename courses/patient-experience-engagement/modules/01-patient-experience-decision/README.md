# APP-2 Module 01: Framing a patient-experience and engagement decision

- Module ID: `oclc-app2-01`.
- Version: `0.1.0`.
- Commons release: `0.56.0`.
- Learner work: 15.5 hours.
- Course points awarded here: 0.
- Week 3 component carried forward: 20 points.

This module asks whether the recovery-at-home patient-reported construct is defined well enough to enter instrument selection. It uses the complete CMS HCAHPS hospital file: 325,720 rows, 4,790 facilities, and 68 measures for the 2024-10-01 through 2025-09-30 reporting period.

The source is hospital level, not patient level. The module does not rank hospitals or authorize a discharge workflow change.

## Verify the full public source

```powershell
python profile_source.py --verify-committed
python profile_source.py --self-check
```

## Build a learner workspace

```powershell
python build_workspace.py --target .work/module01
python validate_workspace.py .work/module01 --starter
```

## Build and validate the reference

```powershell
python build_workspace.py --target .work/module01-reference --reference
python validate_workspace.py .work/module01-reference
```

## Durable specification

The complete teaching and release contract is [the Module 01 specification](../../../../docs/curriculum/courses/APP-2/modules/01-patient-experience-decision-spec.md).
