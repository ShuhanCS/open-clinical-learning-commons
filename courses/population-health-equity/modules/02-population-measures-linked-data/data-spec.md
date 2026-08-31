# Data specification

## Frozen public handoff

`upstream/module01-reference/` is the complete accepted 27-file Module 01 reference workspace. `upstream/module01-release.json` carries the accepted release decision. `upstream/module01-handoff-manifest.csv` fingerprints all 28 payload files.

The handoff includes:

- 1,597 CDC PLACES 2025 Massachusetts `DIABETES` tract rows;
- 1,620 ACS 2020-2024 B01001 Massachusetts tract rows;
- 1,613 CDC/ATSDR SVI 2022 Massachusetts tract rows;
- 282 public-source field inventory rows; and
- the complete Module 01 population, denominator, geography, time, community, claim, AI, and progression records.

## Synthetic source

`data/raw/synthetic-events.csv.gz` has 7,985 rows, one for each of five adult age bands in each of 1,597 matched tracts. Every row has `synthetic_flag=1`, generator version `0.1.0`, seed `73052`, fictional period `2024`, and case ID `FMA-DP-01`.

The generated numerator is an adult planning-need event used only to teach rate construction. It is not a diagnosis, PLACES case, patient record, individual eligibility result, local observation, intervention outcome, or allocation signal.

`data/age-band-crosswalk.csv` names all 38 ACS B01001 estimate and margin fields used to construct the adult age bands. `data/data-dictionary.csv` defines all 22 source fields. `data/synthetic-source-manifest.csv` records the source identities.

## Adult age bands

| ID | Age band | B01001 source cells |
|---|---|---:|
| A01 | 18-34 | 12 |
| A02 | 35-49 | 6 |
| A03 | 50-64 | 8 |
| A04 | 65-74 | 6 |
| A05 | 75+ | 6 |

The accepted matched population totals 5,679,768 adult denominator units. Forty-one tract-age rows have a zero denominator. Those rates remain unavailable.

## ACS margin method

For each age-band sum, the approximate 90 percent margin of error is the square root of the sum of squared margins for nonzero estimates plus the largest squared margin among zero-estimate cells, when any are present. The result is an approximation because the method does not include component covariance.

The paired ACS estimate and margin stay together. A missing or unavailable value cannot become zero.

## Measure outputs

| Output | Rows | Role |
|---|---:|---|
| `tract-linkage-audit.csv` | 1,620 | Complete union and source-presence states |
| `age-band-denominators.csv.gz` | 7,985 | ACS adult age-band estimates and approximate margins |
| `synthetic-event-linkage.csv.gz` | 7,985 | Generated numerator linked to the independently derived denominator |
| `age-specific-rates.csv.gz` | 7,985 | Synthetic age-specific rates and Wilson intervals |
| `standard-population.csv` | 5 | One common matched-population age standard |
| `tract-rate-summary.csv` | 1,597 | Crude and directly standardized synthetic rates |
| `indirect-standardization.csv` | 1,597 | Expected synthetic events and standardized event ratios |
| `public-modeled-prevalence.csv` | 1,597 | Separate PLACES modeled prevalence evidence |
| `source-reconciliation.csv` | 8 | Source and measure conservation checks |
| `query-checks.csv` | 30 | Exact SQL invariants |

`outputs/build-report.json` records every source, SQL, output, and finding identity.

## Standardization rules

The direct method applies each tract's five synthetic age-specific rates to one common standard age distribution built from the 5,679,768 matched ACS adult denominator units. The five weights total one. A direct rate is unavailable for 21 tracts with at least one zero age-band denominator. Eighty tracts have at least one age-band denominator below 50 and must complete the guided indirect exercise.

The indirect method applies the complete statewide synthetic age-specific rates to each tract's own age distribution. The standardized event ratio compares a synthetic count with an expected synthetic count. It is not a directly standardized rate, a real excess-case measure, or an allocation rule.

## Protected boundaries

Public modeled prevalence and synthetic event measures remain in separate tables. The release contains no disparity claim, map, tract ranking, targeting or allocation rule, model fit, intervention-effect estimate, real community result, implementation instruction, or deployment authority.
