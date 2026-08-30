# Source-feasibility interpretation

## SP01 through SP05

SP01 records 325,720 source rows. SP02 records 22 fields. SP03 identifies 4,790 public facilities, SP04 identifies 68 HCAHPS measures, and SP05 identifies 56 state or territory codes. These facts establish the scope of the accepted file. They do not create a patient-level cohort.

## SP06 through SP10

SP06 confirms 4,790 rows for every measure ID. SP07 and SP08 fix the reporting period from 2024-10-01 through 2025-09-30. SP09 records 105,461,119 decompressed bytes. SP10 records the decompressed SHA-256. Together they show that the profile uses the full pinned file rather than a convenience sample.

## SP11 through SP15

SP11 and SP12 fingerprint the deterministic 2,195,547-byte gzip. SP13 finds numeric response rates for 3,949 facilities, while SP14 records 841 facilities without a numeric response rate. SP15 places the first quartile at 18 percent. Missing public values are part of the measurement case and cannot be silently dropped.

## SP16 through SP20

SP16 places the facility-level response-rate median at 22 percent and SP17 places the third quartile at 28 percent. SP18 sums reported completed survey counts to 2,411,406 across supported facilities; this is a reported survey-count total, not proof of distinct patients. SP19 confirms zero patient-level response rows. SP20 confirms 4,790 public facility identities and therefore requires a no-ranking rule.

The primary recovery-at-home anchor has reported percentages for 3,949 facilities and unavailable values for 841. The supporting help and warning-sign items each have reported percentages for 3,610 facilities and unavailable values for 1,180. These patterns show public reporting support, not local representation.

## Decision consequence

The full source supports a patient-experience construct and instrument-selection question. It is not patient-level evidence and does not support hospital ranking, local subgroup interpretation, causal inference, or an intervention decision. Module 02 may proceed with conditions to choose a fit-for-purpose instrument and collection plan.
