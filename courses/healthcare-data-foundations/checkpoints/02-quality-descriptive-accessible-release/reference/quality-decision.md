# Cumulative quality decision

## Accepted input and grain

The released analytic table has 374 rows, 29 fields, one row per selected synthetic person, one unique index encounter per row, source release `synthea-csv-apr2020`, and cohort definition 0.1.0. It is 121,787 bytes with SHA-256 `3c9944edc3806aa3b709a9ca08a9986a2f79978b1074ed098e31f19b533db25a`.

## Seeded defect resolution

The separate 379-row teaching layer contains 20 seeded defect families, D01 through D20, across 56 issue cases and 68 manifest changes. All 28 rule-result rows pass their expected detection counts. D01 through D20 have `resolved` status, and the restored table is byte-identical to the accepted 374-row release.

## Retained conditions

N01 death-date missingness, N02 missing reason pairs, N03 no-next-event companion blanks, N04 age at least 100, N05 prior encounters above 100, N06 prior medications above 100, N07 small race-category rows, and N08 urgent-state or death-endpoint rows remain accepted review conditions. They are not silently corrected, hidden, or converted to zero.

## Recommendation

`proceed with conditions`. Module 07 must preserve the accepted fingerprint, D01 through D20 audit trail, N01 through N08, field-specific missingness, small-result visibility, source version, and synthetic claim boundary. Any changed immutable artifact, new blocking defect, altered denominator, or unsupported patient-data substitution requires revision or referral.

