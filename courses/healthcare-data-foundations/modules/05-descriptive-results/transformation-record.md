# Reference transformation record

## Inputs

- Exact Module 04 resolved analytic table.
- Exact Module 04 quality-rule results.

## Ordered transformations

1. Verify both fingerprints, source shape, person and index grain, source release, and cohort version.
2. Select the 17 registered fields without changing source rows.
3. Calculate availability, missingness, distinct values, and type-appropriate summaries.
4. Use sample standard deviation and inclusive interpolated quartiles.
5. Build complete gender-by-endpoint and index-class-by-endpoint tables.
6. Calculate row percentages from unrounded counts.
7. Calculate six cohort proportions and Wilson 95-percent intervals.
8. Build two unadjusted index-class stratum rows.
9. Register 27 result families with denominator and interpretation contracts.
10. Attach N01 through N08 to affected results.
11. Run 18 release invariants and write deterministic LF-terminated CSV files.

No cohort row is excluded. No missing value is imputed. No source value is edited. No inferential test is performed.
