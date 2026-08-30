# Stop, fix, or proceed decision

## Initial decision: fix

Do not use the defective table for description. It contains duplicate people, missing keys, impossible eligibility values, malformed and inconsistent time fields, vocabulary drift, unsupported missingness, invalid flags, and provenance/version drift. These problems can change denominators, break follow-up, or disconnect the result from its source.

## Evidence

- 379 rows represent 374 people because five rows are exact duplicates.
- All 20 seeded rule families are present at their registered counts.
- The 56 seeded issue cases reconcile to 68 manifest changes.
- The accepted 374-row source remains unchanged.

## After resolution: proceed with conditions

The resolved table is byte-for-byte identical to the accepted source, contains one row per person, and passes the seeded rules. Module 05 may proceed with these conditions:

1. retain structurally allowed missingness and state the available denominator;
2. keep N04 through N06 extreme-value review notes visible;
3. carry N07 and N08 small-cell cautions into any display or interpretation;
4. call `No encounter recorded` a statement about this source, not about all care;
5. make no real clinical, quality, safety, utilization, or population claim from synthetic data; and
6. use the exact resolved fingerprint and quality records in the descriptive handoff.

Decision owner: data-quality lead. Module 04 reference disposition: `proceed with conditions`.
