# Progression decision

- Decision: `continue with conditions`.
- Module 03 curriculum construction: `permitted`.
- Model fitting inside Module 02: `prohibited`.
- Clinical-threshold selection or acceptance: `prohibited`.
- Real-patient scoring: `prohibited`.
- Clinical alerting or action: `prohibited`.
- Implementation: `prohibited`.
- Deployment: `prohibited`.
- Decision owner: `APP-4 faculty owner`, subject to the named clinical and governance reviewers.

## Basis

All inherited Module 01 files preserve their accepted identities. The full 25-file synthetic FHIR release has 811,803 resource rows and zero parse failures. The 11,109 duplicate IDs are measured and bounded. The 16 linked rule fixtures cover normal, boundary, missing, stale, inconsistent, duplicate, delayed, terminology, version, suppression, unit, context, silent-failure, and missing-score conditions. Every expected result and ordered trace passes.

## Conditions

Clinical, interoperability, terminology, human-factors, patient-safety, patient-access, privacy, accessibility, responsible-AI, and independent-reproduction review remain open. Module 03 must define and defend the historical target, eligibility, exclusions, predictors, missing-input rules, calibration approach, candidate thresholds, burden, missed-case consequences, temporal validation, later-cycle stress test, and subgroup support.

The mock score and `0.20` branch value cannot be carried forward as evidence. This decision authorizes Module 03 curriculum construction only. It does not authorize clinical use.
