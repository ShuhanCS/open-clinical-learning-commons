# FND-1 Module 04: Cleaning and profiling

This module asks a data-quality lead to decide whether a healthcare analytic table should stop, be fixed, proceed, or proceed with conditions. It uses synthetic records and supports no real clinical or population claim.

## Decision

The initial 379-row defect layer must be fixed. After deterministic restoration, the reference decision is `proceed with conditions`: keep optional missingness, extreme-value review notes, and small-cell cautions visible in Module 05.

## Released facts

- Accepted analytic table: 374 people, 29 fields, SHA-256 `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a`.
- Defect layer: 379 rows and 374 distinct people.
- Seeded defects: 20 families, 56 cases, and 68 manifest changes.
- Natural conditions: 8 rules that require interpretation rather than automatic correction.
- Resolved table: byte-for-byte identical to the accepted analytic table.

## Build and profile

Both scripts use the Python standard library. Targets must not already exist.

```powershell
python build_defect_release.py --source ..\03-cohorts-analytic-tables\outputs\analytic-table.csv --target <new-data-directory>
python profile_quality.py --data-dir <new-data-directory> --dictionary ..\03-cohorts-analytic-tables\data-dictionary.csv --target <new-output-directory>
```

The checked reference data and outputs are included so learners can inspect exact evidence before reproducing it.

## Notebook

Open `notebooks/04-data-quality.ipynb` from this module folder. It verifies grain, missingness, all 28 rules, the resolution record, and the final source fingerprint. `profile_quality.py` is the accessible non-notebook route to the same evidence.

## Validate

```powershell
python validate_defect_release.py .
python validate_defect_release.py <module-04-submission> --submission
```

## Learning route

1. Verify the accepted source before inspecting defects.
2. Compare accepted and defective grain.
3. Profile every field and distinguish required from structurally allowed missingness.
4. Reconcile all seeded rules to the manifest.
5. Separate impossible values from extreme but supported values.
6. Complete the risk and resolution logs.
7. Rebuild the resolved table and make a bounded readiness decision.
8. Record reproduction and any material AI use.

## Boundaries

- The accepted Checkpoint 1 table is immutable.
- The defect layer is a separately versioned teaching transformation.
- Blank does not mean zero, negative, or clinically absent.
- Extreme does not mean wrong.
- Resolved means technically restored, not clinically validated.
- Small-cell rules here are teaching cautions, not universal publication policy.

Module version: 0.1.0. Commons release: 0.32.0.
