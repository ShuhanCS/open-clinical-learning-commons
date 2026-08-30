# Module 09 data specification

## Purpose

The releases support one comparison decision: which North Carolina counties should enter a twelve-county partnership-readiness review when five modeled adult health measures, uncertainty, age adjustment, population scale, and comparison rules remain visible?

## Authoritative source

- Publisher: Centers for Disease Control and Prevention
- Dataset: PLACES, Local Data for Better Health, County Data 2024 release
- Dataset ID: `fu4u-a9bh`
- Landing page: https://data.cdc.gov/d/fu4u-a9bh
- Metadata API: https://data.cdc.gov/api/views/fu4u-a9bh
- Methodology: https://www.cdc.gov/places/methodology/index.html
- Retrieval date: 2026-08-29
- Selected measure year: 2022
- Raw selected-query rows: 31,450
- Raw selected-query bytes: 5,095,209
- Raw selected-query SHA-256: `897064d10703b870afe6d55f4cf0bc7e08d1c91f5d3490584952894df3f6de4b`

CDC PLACES uses multilevel regression and poststratification with BRFSS, Census, and ACS inputs to produce small-area estimates. The released point estimates are means over simulated draws, and the reported 95 percent confidence limits use the 2.5th and 97.5th percentiles.

## Selected measures

| ID | Measure | Population | Type |
|---|---|---|---|
| `CSMOKING` | Current cigarette smoking among adults | adults age 18 and older | health risk behavior |
| `DIABETES` | Diagnosed diabetes among adults | adults age 18 and older | health outcome |
| `GHLTH` | Fair or poor self-rated health status among adults | adults age 18 and older | health status |
| `LPA` | No leisure-time physical activity among adults | adults age 18 and older | health risk behavior |
| `OBESITY` | Obesity among adults | adults age 18 and older | health outcome |

All selected rows use measure year 2022. Each measure has crude and age-adjusted prevalence estimates.

## Released files

| File | Rows | Columns | SHA-256 |
|---|---:|---:|---|
| `data/places_county_comparison_2024.csv` | 31,450 | 16 | `2af5ce99fc7d66a18e95451084afc397e0f7392e9f1a2b5476377fd8811658d2` |
| `data/nc_county_health_profiles_2024.csv` | 500 | 27 | `33b7cfc1c2459f1bde29cee7c05141aa116da2e6f79faf82646961e5162a75a9` |

## Selected national release fields

| Field | Type | Rule |
|---|---|---|
| `year` | integer text | Preserve the measure year. |
| `stateabbr` | text or blank | Preserve the source state abbreviation. National rows remain blank. |
| `statedesc` | text or blank | Preserve the source state name. |
| `locationname` | text | Preserve county or national source name. |
| `locationid` | text | Preserve five-character county FIPS or national summary ID `59`. |
| `measureid` | text | One of the five selected measure IDs. |
| `measure` | text | Preserve the source measure label. |
| `data_value_type` | text | Preserve crude or age-adjusted prevalence label. |
| `datavaluetypeid` | text | Preserve `CrdPrv` or `AgeAdjPrv`. |
| `data_value` | decimal | Preserve the point estimate to one decimal place. |
| `low_confidence_limit` | decimal | Preserve the source lower 95 percent confidence limit. |
| `high_confidence_limit` | decimal | Preserve the source upper 95 percent confidence limit. |
| `totalpopulation` | integer | Preserve total source population. |
| `totalpop18plus` | integer | Preserve adult source population. |
| `data_value_footnote_symbol` | text or blank | Preserve source footnote symbol. |
| `data_value_footnote` | text or blank | Preserve source footnote text. |

## North Carolina teaching fields

| Field | Type | Derivation and use |
|---|---|---|
| `county_fips` | text | Five-character county identifier. |
| `county_name` | text | Public county name. |
| `state_abbr` | text | Always `NC`. |
| `state_name` | text | Always `North Carolina`. |
| `measure_id` | text | Selected source measure ID. |
| `measure_name` | text | Complete source measure name. |
| `measure_label` | text | Short display label. |
| `measure_year` | integer text | Always 2022 in this release. |
| `adult_population` | integer | Source population age 18 and older. |
| `crude_prevalence_pct` | decimal | Source crude point estimate. |
| `crude_low_ci_pct` | decimal | Source crude lower confidence limit. |
| `crude_high_ci_pct` | decimal | Source crude upper confidence limit. |
| `age_adjusted_prevalence_pct` | decimal | Source age-adjusted point estimate. |
| `age_adjusted_low_ci_pct` | decimal | Source adjusted lower confidence limit. |
| `age_adjusted_high_ci_pct` | decimal | Source adjusted upper confidence limit. |
| `national_age_adjusted_pct` | decimal | Matching national age-adjusted point estimate. |
| `national_age_adjusted_low_ci_pct` | decimal | National lower confidence limit. |
| `national_age_adjusted_high_ci_pct` | decimal | National upper confidence limit. |
| `difference_from_national_pct_points` | decimal | County adjusted estimate minus matching national point estimate. |
| `rank_descending_point_estimate` | integer | Competition rank within one measure across 100 counties. |
| `counties_compared` | integer | Always 100; makes the comparison denominator explicit. |
| `point_estimate_above_national` | yes or no | Descriptive point-estimate direction. |
| `measures_above_national` | integer | Count from 0 through 5 for the county. |
| `largest_gap_measure_id` | text | Measure with the county's largest point-estimate difference from national. |
| `largest_gap_pct_points` | decimal | That largest difference. |
| `profile_order` | integer | Transparent teaching order from 1 through 100. |
| `source_footnote` | text or blank | Joined crude and adjusted source footnotes. Blank for this case. |

## Profile-order contract

The reference order is calculated once per county and reused in all five panels:

1. descending `measures_above_national`;
2. descending `largest_gap_pct_points`;
3. ascending `county_name`.

The order is a visualization device and screening example. It does not establish equal clinical importance of the measures, program readiness, causal need, funding priority, or community preference.

## National reference contract

Each panel uses the matching U.S. age-adjusted point estimate:

| Measure | National point estimate |
|---|---:|
| Current smoking | 13.2% |
| Diagnosed diabetes | 10.4% |
| Fair or poor health | 17.0% |
| No leisure activity | 23.0% |
| Obesity | 33.4% |

The reference definition stays constant even though the numeric value differs by measure. A local state median may be shown as additional context, but it may not silently replace the national comparator from panel to panel.

## Completeness contract

- The selected national release contains 3,144 counties and ten national summary rows.
- Every measure has 6,290 rows: one crude and one age-adjusted row for each county and national summary.
- Every North Carolina county has all five crude and all five age-adjusted estimates.
- All point estimates and confidence limits are present.
- Every source interval contains its point estimate.
- The teaching release has no source footnotes.
- Adult population is consistent across the five measure rows for a county.

## Build and validation

`build_places_comparison.py` uses Python's standard library. It downloads or reads the pinned query, verifies the checksum and 16-field schema, normalizes numeric text, preserves all selected source rows, pairs crude and adjusted county estimates, adds national references, calculates transparent comparison fields, and writes deterministic CSV files.

`validate_places_comparison.py` runs 58 checks across source identity, checksums, keys, measures, years, geographies, value types, intervals, exact source reconciliation, population consistency, ranks, reference differences, profile counts, order, ranges, and the reference shortlist.

## Interpretation limits

- PLACES estimates are model-based, not direct county survey estimates or observed case counts.
- The source measures include self-reported behaviors, diagnoses, height, weight, and general health.
- County values do not reveal within-county distributions or inequity.
- Age adjustment supports comparison and does not represent a county's outreach volume.
- Crude and adjusted estimates answer different questions; their difference is not change over time.
- Point-estimate direction and interval overlap do not provide a formal pairwise significance test.
- The five-measure count gives every selected measure equal weight and omits readiness, cost, community priorities, and intervention fit.
