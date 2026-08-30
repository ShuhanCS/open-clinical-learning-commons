# Instructor notes and answer key

## Review purpose

Decide whether the learner has a defensible quality, descriptive, and accessible evidence package for Module 07. Review the fixed synthetic cohort and exact release chain. Do not turn synthetic counts into clinical findings or ask learners to redesign accepted figures during the checkpoint.

## Weight map

- Module 04 quality evidence: 13.75 of 25 points.
- Module 05 descriptive evidence: 6.25 of 25 points.
- Module 06 access evidence: 5.00 of 25 points.
- Numeric pass threshold: 20.00.
- Gates, defense, and disposition still apply.

## Immutable answer key

- Analytic table: 374 rows, 29 fields, one row per selected synthetic person.
- Analytic SHA-256: `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a`.
- Defect layer: 379 rows, 20 seeded defect families, 56 issue cases, 68 manifest changes.
- Quality rules: 28 passing results.
- Resolution: D01 through D20 resolved; N01 through N08 retained.
- Final quality recommendation: `proceed with conditions`.
- Descriptive outputs: 17 profiles, 12 cross-tab cells, six rates, two strata, 27 denominator records, and 18 passing checks.
- Rate numerators: 111, 92, 4, 15, 36, and 8, each over 374.
- Figures: F01 through F03, each with exact CSV, PNG, SVG, registry row, and structured alternative.
- F03: 20 quarters totaling 374 selected indexes, including 314 emergency and 60 inpatient.

## Interpretation key

- The separate defect layer teaches detection without corrupting the accepted table.
- High missingness may be structurally valid; it is not automatically a defect.
- The 263 rows without a recorded next encounter do not receive elapsed time zero.
- RT01 contains RT02 through RT04, so those rows are not six mutually exclusive outcomes.
- Wilson intervals are descriptive arithmetic for the fixed synthetic cohort, not real-population inference or significance tests.
- The two index-class rows are unadjusted descriptions.
- F03 shows selected synthetic indexes by quarter. It is not hospital volume, a tested trend, a forecast, or a causal result.

## Accessibility key

Every figure has an exact table and structured alternative. F01 uses hatch, F02 uses direct labels, and F03 uses line and marker differences in addition to color. The accepted review records grayscale, 50-percent width, 200-percent zoom, reading order, and exact-table equivalence. Named human accessibility review remains pending.

## Review order

1. Verify the three module releases, 35-row contract, manifest, and 50-file package.
2. Confirm the analytic fingerprint and grain.
3. Trace D01 through D20 and N01 through N08.
4. Reconcile one profile, cross-tab, rate, stratum, and denominator record.
5. Trace one mark in each figure back to its exact table.
6. Read the alternatives without the figures.
7. Review the cumulative quality, interpretation, accessibility, reproduction, and AI records.
8. Run complete validation.
9. Conduct the defense and record the score, gates, disposition, and progression.

## Common interventions

- Structural blank treated as zero: return to field- and state-specific missingness rules.
- Changed immutable evidence: return to the owning module and version the change.
- Rate without denominator or window: require the exact denominator-registry row.
- Interval treated as a hypothesis test: restore descriptive synthetic-cohort wording.
- Figure judged by appearance alone: require exact-table, alternative, grayscale, size, zoom, and reading-order review.
- Quarterly count called a trend or volume: restore selected-cohort wording.
- Plausible AI explanation without evidence: require a source row, rule, arithmetic check, or fingerprint verification.

## Technical reference result

Reference and learner assembly each create 50 files with 35 immutable artifacts. The artifact contract is 5,993 bytes with SHA-256 `ec031d23a50628b07ce15091c90a76f03241e3f4c4a17927211b74b854754a6b`. The release manifest is 8,812 bytes with SHA-256 `d7bb0e561309f4b61353f4485fe1d647d8a15c47e064f93acd816a77e512489d`. Starter validation passes 363 checks; complete reference validation passes 389. Existing targets, incomplete records, and missing immutable artifacts are rejected.

## Human review still required

Faculty, data-quality, clinical analytics, clinical informatics, accessibility, Python reproducibility, privacy, responsible-AI, and independent-instructor review remains pending before alpha promotion.
