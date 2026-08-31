# Missingness and representation audit

The field-completeness release contains 283,614 generated event records at the tract-age aggregate grain.

| Field | Missing count | Missing percent | Interpretation |
|---|---:|---:|---|
| Race | 6,000 | 2.1156% | Generated missingness is present. |
| Ethnicity | 7,578 | 2.6719% | Generated missingness is present. |
| Primary language | 5,314 | 1.8737% | Generated missingness is present. |
| Disability status | 8,376 | 2.9533% | Generated missingness is present. |
| Tract geography | 0 | 0.0000% | The analytic universe already requires a tract link. Zero does not measure records excluded before linkage. |

Because the universe is conditioned on tract linkage, zero missing geography cannot establish complete capture.

All 19 group rows remain visible in `representation-audit.csv`, including the three missing groups. No small reported group is merged into a larger category to improve support. Population shares and event shares sum to one within each separate dimension.

The three dimensions are independent generated margins. A population share in one table cannot be joined to a share in another table, and the release cannot describe intersectional identities, within-group diversity, self-identification quality, lived experience, or real representation in Massachusetts.
