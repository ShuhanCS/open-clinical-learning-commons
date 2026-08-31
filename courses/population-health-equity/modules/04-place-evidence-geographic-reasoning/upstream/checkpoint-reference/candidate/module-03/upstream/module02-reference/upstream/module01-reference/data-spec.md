# APP-5 Module 01 data specification

## Public source layer

The immutable module release contains three complete Massachusetts census-tract extracts built from accepted public releases.

| File | Rows | Fields | Grain |
|---|---:|---:|---|
| `data/places-diabetes-ma-tract-2025.csv` | 1,597 | 24 | One PLACES modeled adult-diabetes estimate per Massachusetts tract |
| `data/acs-b01001-ma-tract-2024.csv` | 1,620 | 100 | One ACS B01001 age-by-sex estimate and margin row per Massachusetts tract |
| `data/svi2022-ma-tract.csv` | 1,613 | 158 | One SVI context row per Massachusetts tract |

## Source A: CDC PLACES

The accepted query selects every Massachusetts `DIABETES` row from dataset `cwsq-ngmh`, the PLACES census-tract 2025 release. All released rows have measure year 2023 and value type `CrdPrv`.

`data_value` is modeled crude prevalence among adults age 18 and older. `low_confidence_limit` and `high_confidence_limit` are its published 95% limits. `totalpop18plus` is the population field carried with the PLACES model release and remains the matching population context for that estimate.

The file is not an observed case registry. A prevalence multiplied by a population would remain a modeled quantity, not a case count.

## Source B: ACS B01001

The accepted acquisition fingerprints the complete 616,690-row, 200,356,282-byte national 2020-2024 B01001 table-based Summary File before selecting all 1,620 Massachusetts census-tract rows.

`tract_fips` is derived from the source `GEO_ID`. `B01001_E001` through `B01001_E049` are published estimates. `B01001_M001` through `B01001_M049` are their published 90% margins of error. Sex- and age-specific cells support later denominator and standardization work after Module 02 fixes the age bands, sums, and margin method.

ACS values are survey estimates. They do not replace the PLACES adult population silently, and they do not provide diabetes events or intervention outcomes.

## Source C: CDC/ATSDR SVI

The accepted file is the complete 2022 Massachusetts tract CSV. It preserves all 158 published fields, including estimates, margins, percentages, percentile components, theme sums, relative ranks, quality flags, daytime population, and adjunct variables.

Negative sentinel-like values and quality flags remain visible. Module 01 does not recode them. SVI rankings are relative to the accepted release and comparison group; they are not longitudinal measurements and cannot be compared mechanically across versions.

SVI is area context. It cannot be assigned to an individual, used as a trait of a community, or used alone to determine targeting, eligibility, or funding.

## Tract-key feasibility

All keys use the 11-character state, county, and tract FIPS identity.

| Comparison | Intersection | Left only | Right only |
|---|---:|---:|---:|
| PLACES versus SVI | 1,597 | 0 | 16 |
| PLACES versus ACS | 1,597 | 0 | 23 |
| SVI versus ACS | 1,613 | 0 | 7 |

The three-source intersection is 1,597 tracts. The union is 1,620 tracts. A later analytic table may begin from a declared population, but no source row may disappear without an unmatched-state record and reason.

## File contracts

`data/source-inventory.csv` records publisher, release, URL, retrieval date, raw scope, bytes, hash, rows, fields, released identity, geography, population, period, uncertainty, teaching role, and claim limit for each source.

`data/field-inventory.csv` records every released field, order, source or derived status, row count, missingness, distinct support, negative sentinel-like count, and teaching role. It has 282 rows.

`data/join-feasibility.csv` records the three pairwise tract comparisons without choosing an analytic population.

`data/reading-inventory.csv` records the official PLACES, ACS, SVI, and TIGER pages required to interpret the files and their limits.

## Raw and refresh policy

The committed state extracts are immutable inside Module version `0.1.0`. The complete national ACS raw file is not committed, but its URL, bytes, SHA-256, full row and field counts, acquisition code, filter, released extract, and validation are preserved.

A source refresh requires review of the upstream release, a new source record, new hashes, a semantic-version decision, regenerated profiles, unmatched-tract review, and revalidation of every downstream module and checkpoint.

## Data-role boundary

These sources may support source feasibility, later denominator construction, modeled surveillance description, uncertainty, area context, and geographic questions. They cannot supply observed diabetes events, individual risk, causal effects, program capacity, community preference, resource entitlement, intervention reach, program outcomes, or real-world authority.

Later synthetic event and program layers remain separate. No public tract may be presented as having a synthetic real-world outcome.
