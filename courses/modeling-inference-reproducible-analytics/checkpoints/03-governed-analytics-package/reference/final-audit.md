# Final source, rights, access, and accountability audit

## Source and rights

- Synthetic modeling source fingerprint and rights: The frozen provenance identifies the public synthetic FND-1 handoff and contains no real patient records. Its use remains technical education and method development.
- Public CDC source fingerprint and rights: Both complete registered CDC NHSN data files remain frozen under `evidence/checkpoint2/public-data/`; the source page is https://data.cdc.gov/Public-Health-Surveillance/Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/rhwp-grxi.
- Transformation trace to final evidence: The 168-row candidate manifest reaches every candidate record. Nested manifests and source records connect cohort, model, validity, forecast, testing, and governance artifacts to their owning unit.
- Prohibited-data and secret scan: Candidate validation and final validation reject personal absolute paths and do not permit patient, workplace, restricted, credential, key, secret, or hidden local files.

## Accessibility

- Exact tables for numeric displays: Model evaluation, subgroup, validity, forecast, test, and monitoring evidence is available as CSV or Markdown tables.
- Structured alternatives for displays and DAGs: The validity DAG has node and edge tables plus narrative; forecast displays have exact predictions and text alternatives.
- Non-color status routes: Every status is written as text in tables or records. Color is never the only signal.
- Equivalent handoff and defense route: `handoff-brief.md`, `technical-defense.md`, and this final written defense provide structured alternatives. Assistive-technology review remains C03.

## Agent and human accountability

- Complete trace location: Module 06 prompt constraints, prompt trace, accepted tests, seeded failures, adjudications, and human sign-off remain under `evidence/checkpoint2/modules/06-agent-assisted-modeling-testing/`.
- Material independent checks: Three results were recalculated from accepted evidence and four claims were adjudicated. Repeating a prompt was not counted as verification.
- Human sign-off scope: The reference sign-off covers curriculum construction only. Named live review remains C01, C02, C04, and C05.
- Unsupported agent claims: Agent output is not evidence. Deployment, efficacy, causal, fairness-certification, stable-process, and real-population claims are prohibited.

## Evidence coverage

- Modeling and evaluation: Cohort, split, feature roles, model contract, baseline, threshold, predictions, calibration, confusion, subgroup rows, and intervals are frozen.
- Validity and longitudinal: Structured DAG, selection profile, overlap, missingness, repeated-measures, survival, threat register, and referrals are frozen.
- Forecast: Full public files, target, folds, benchmarks, predictions, errors, residuals, coverage, and failure analysis are frozen.
- Testing and failures: Eighteen accepted tests, ten intended failure rejections, trace, independent checks, and adjudications are frozen.
- Governance and lifecycle: Model card, intended and prohibited use, ten monitoring signals, drift, retraining, versioning, rollback, stop, retirement, and conditions are frozen.
- Reviewer conclusion: The evidence is complete enough for a governed teaching reference. It is not evidence for deployment or real-population performance.
