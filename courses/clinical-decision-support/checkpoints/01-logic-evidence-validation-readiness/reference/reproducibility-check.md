# Reproducibility check

- Candidate files: `245`.
- Nested immutable rows: `204`.
- Checkpoint files: `263`.
- Module 01 has 0 points.
- Module 02 has 20 points once.
- Module 03 has 20 points once.
- The sum is 40.
- Two independent reference builds match byte for byte at the candidate manifest and candidate-file level.
- The learner and reference candidates have the same manifest.
- All three nested release manifests match their accepted SHA-256 values.
- Module 01 source profiler and workspace validator: `pass`.
- Module 02 synthetic release, fixture, rule, workspace, and validator checks: `pass`.
- Module 03 evidence release, workspace, and validator checks: `pass`.

## Rejected mutation routes

- Candidate mutation: `rejected`.
- Missing-candidate mutation: `rejected`.
- Nested-manifest mutation: `rejected`.
- Module 01 point mutation: `rejected`.
- Duplicate Module 02 point mutation: `rejected`.
- Duplicate Module 03 point mutation: `rejected`.
- Wrong-total mutation: `rejected`.
- Failed inherited gate: `rejected`.
- Failed checkpoint gate: `rejected`.
- Promoted `0.20` fixture: `rejected`.
- Accepted-threshold mutation: `rejected`.
- Diagnosis mutation: `rejected`.
- Holdout-retuning mutation: `rejected`.
- Transport-pooling mutation: `rejected`.
- Unsupported-subgroup mutation: `rejected`.
- Incomplete-defense mutation: `rejected`.
- Missing-AI-field mutation: `rejected`.
- Invalid-progression mutation: `rejected`.
- Real-patient scoring mutation: `rejected`.
- Deployment mutation: `rejected`.

Named clinical, survey-methods, calibration, clinical-informatics, patient, workflow, equity, accessibility, responsible-AI, and independent-reproduction review remains pending before alpha.
