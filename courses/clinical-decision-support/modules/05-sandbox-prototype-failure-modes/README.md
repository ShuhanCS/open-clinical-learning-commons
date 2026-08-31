# APP-4 Module 05: Sandbox prototype and failure modes

This package is a local, nonnetworked teaching sandbox. It freezes the full Module 04 reference release, creates FHIR R4 and CDS Hooks-shaped fixtures, runs 31 declared normal and failure cases, and protects the Module 06 handoff.

## Run the checks

```powershell
python build_sandbox.py --self-check
python build_workspace.py --self-check
python validate_workspace.py --self-check
```

To assemble a learner workspace:

```powershell
python build_workspace.py --target C:\path\to\new-workspace
```

To assemble the complete reference:

```powershell
python build_workspace.py --target C:\path\to\new-reference --reference
```

Each command refuses an existing target. The sandbox uses local files only. It does not run a listener, call a FHIR server, process real patient data, or claim conformance.

## Release facts

- Module version: `0.1.0`.
- Commons release: `0.82.0`.
- Module points: `0`.
- Module 04 score carried forward: `25.00 of 25.00`, once.
- Cases: `31`.
- FHIR-shaped prefetch resources: `184`.
- Responses: `31`.
- Trace events: `61`.
- Silent failures detected: `1`.
- Accessibility defects blocked: `1`.
- Accepted clinical threshold: `none`.

FHIR R4 teaching source: https://hl7.org/fhir/R4/

CDS Hooks teaching source: https://cds-hooks.hl7.org/

ONC SAFER Guides: https://www.healthit.gov/topic/safety/safer-guides

The resources and messages are teaching shapes. Passing the package does not prove interoperability, safety, clinical utility, or production readiness.
