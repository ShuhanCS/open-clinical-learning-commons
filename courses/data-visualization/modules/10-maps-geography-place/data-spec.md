# Module 10 data specification

## Release inventory

| Release | Rows | Columns | Grain |
|---|---:|---:|---|
| `hpsa_primary_care_nc_2026_08_29.csv` | 1,546 | 28 | One selected HRSA HPSA component record mapped to a North Carolina county FIPS. |
| `nc_place_access_2026.csv` | 100 | 29 | One North Carolina county. |
| `nc_county_boundaries_2024.csv` | 7,121 | 6 | One ordered point in a generalized county polygon ring. |

None of the releases contains patient-level records.

## Source A: CDC PLACES

The module reuses the pinned Module 09 North Carolina release:

```text
courses/data-visualization/modules/09-comparison-small-multiples/data/nc_county_health_profiles_2024.csv
```

- Upstream rows: 500
- Upstream columns: 27
- Upstream checksum: `33b7cfc1c2459f1bde29cee7c05141aa116da2e6f79faf82646961e5162a75a9`
- Selected measure: `GHLTH`
- Measure: fair or poor self-rated health status among adults
- Measure year: 2022
- Estimate used for comparison: age-adjusted prevalence
- Crude estimate retained upstream: yes
- Source intervals retained: yes
- Source adult population retained: yes

The module selects exactly one `GHLTH` row for each of 100 counties. It does not refit the PLACES model or change the published estimates.

## Source B: HRSA primary-care HPSAs

- Publisher: Health Resources and Services Administration
- Discipline: Primary Care
- Full source URL:
  https://data.hrsa.gov/DataDownload/DD_Files/BCD_HPSA_FCT_DET_PC.csv
- Metadata URL:
  https://data.hrsa.gov/DataDownload/DD_Files/HPSA_DATAMART_METADATA.XLSX
- Usage page:
  https://data.hrsa.gov/data/download?data=HPSA
- Retrieval date: 2026-08-29
- Full source rows: 79,358
- Full source bytes: 48,280,174
- Full source SHA-256: `4552ebf09bc5a40d79d71df8ea84aea165de2205953615e03571ad84f1d6b132`
- Metadata bytes: 27,433
- Metadata SHA-256: `56767d21a9d86acfae8ac17ad0eac82c3a5720280a252afdd8bef7f43ab52c8e`

The HRSA metadata marks the selected attributes public. The usage page reports no usage limitation for the HPSA release.

### Selection

The build retains every primary-care source row whose state-and-county FIPS:

1. is exactly five characters;
2. begins with North Carolina state FIPS `37`; and
3. is available for a county join.

The result has 1,546 rows covering all 100 counties.

The source selection keeps current and historical status values:

| HPSA status | Rows |
|---|---:|
| Designated | 740 |
| Proposed For Withdrawal | 104 |
| Withdrawn | 702 |

Only rows with exact status `Designated` contribute to the teaching table. Proposed-withdrawal and withdrawn records remain available for provenance and status exercises.

### HPSA grain

An HPSA row is not a county workforce observation. It can represent a component of a geographic, population, or facility designation. One HPSA identifier can have several component rows, and one county can contain parts of several HPSAs.

The teaching table therefore distinguishes:

- source component rows;
- unique HPSA identifiers;
- designation type;
- component type;
- status; and
- the highest score among currently designated components touching the county.

It never sums HPSA scores.

### HPSA score screen

The reference rule marks a county when its highest current component score is at least 20.

This is a declared teaching screen. It is not an HRSA funding threshold, a county shortage rate, a validated priority score, or proof that the whole county is designated.

## Source C: Census generalized county boundaries

The module reuses the exact Module 05 boundary release:

```text
courses/data-visualization/modules/05-rates-denominators-adjustment/data/nc_county_boundaries_2024.csv
```

- Service:
  https://tigerweb.geo.census.gov/arcgis/rest/services/Generalized_ACS2024/State_County/MapServer
- Layer query:
  https://tigerweb.geo.census.gov/arcgis/rest/services/Generalized_ACS2024/State_County/MapServer/12/query?where=STATE%3D%2737%27&outFields=GEOID%2CNAME%2CSTATE%2CCOUNTY&returnGeometry=true&outSR=4326&f=geojson
- Coordinate reference system in the release: longitude and latitude, EPSG:4326
- Boundary points: 7,121
- County features: 100
- Polygon parts: 104
- SHA-256: `6eb085f49b400d4ecf6f88646f51dd01fdd4154533262e66ade02b1d1d8f666f`

The lab converts longitude and latitude to an Albers equal-area teaching projection before drawing the maps. The released coordinate table remains unchanged.

The generalized boundaries support state-scale teaching maps. They are not suitable for addresses, parcels, routing, travel time, service areas, or operational boundary decisions.

## Selected HPSA source dictionary

| Field | Meaning | Use |
|---|---|---|
| `HPSA Name` | Source designation name. | Audit the highest-score context. |
| `HPSA ID` | Source HPSA identifier. | Count unique designations. |
| `Designation Type` | Geographic, population, facility, or related type. | Avoid treating unlike designations as one grain. |
| `HPSA Discipline Class` | Health discipline. | Must equal Primary Care. |
| `HPSA Score` | Source primary-care HPSA score. | Highest active component screen only. |
| `Primary State Abbreviation` | Primary source state. | Source context. |
| `HPSA Status` | Designated, proposed for withdrawal, or withdrawn. | Select current designated rows. |
| `HPSA Designation Date` | Initial designation date. | Recency and history. |
| `HPSA Designation Last Update Date` | Last designation update date. | Recency and history. |
| `HPSA Degree of Shortage` | Source shortage category. | Source interpretation. |
| `Withdrawn Date` | Withdrawal date when applicable. | Status audit. |
| `HPSA FTE` | Source provider FTE field. | Source context, not summed by the module. |
| `HPSA Designation Population` | Population associated with the designation. | Source context, not a county denominator. |
| `% of Population Below 100% Poverty` | Source designation context. | Equity context. |
| `HPSA Formal Ratio` | Source provider-to-population ratio text. | Source context. |
| `HPSA Population Type` | Population designation type. | Interpret scope. |
| `Rural Status` | Source rural classification. | Context only. |
| `Common County Name` | Source county label. | Audit the FIPS join. |
| `Common State Abbreviation` | Source state label. | Audit the FIPS join. |
| `State and County Federal Information Processing Standard Code` | Five-character county FIPS. | Join key. |
| `HPSA Component Name` | Source component label. | Audit component grain. |
| `HPSA Component Source Identification Number` | Component source identifier. | Stable row context. |
| `HPSA Component Type Description` | Census tract, county subdivision, single county, or unknown. | Define scope. |
| `HPSA Estimated Served Population` | Source component estimate. | Context only. |
| `HPSA Estimated Underserved Population` | Source component estimate. | Context only. |
| `HPSA Provider Ratio Goal` | Source goal ratio. | Context only. |
| `HPSA Shortage` | Source shortage field. | Context only. |
| `Data Warehouse Record Create Date` | HRSA source snapshot date. | Version the selection. |

## Teaching table dictionary

### Identity and health fields

| Field | Type | Meaning |
|---|---|---|
| `county_fips` | character | Five-character county FIPS with leading zero preserved. |
| `county_name` | character | Short county name. |
| `state_abbr` | character | `NC`. |
| `health_measure_id` | character | `GHLTH`. |
| `health_measure_label` | character | Short display label. |
| `health_measure_year` | integer | 2022. |
| `adult_population` | integer | PLACES adult population context. |
| `age_adjusted_fair_poor_health_pct` | decimal | Published age-adjusted point estimate. |
| `age_adjusted_low_ci_pct` | decimal | Published lower confidence limit. |
| `age_adjusted_high_ci_pct` | decimal | Published upper confidence limit. |
| `national_age_adjusted_pct` | decimal | Published national point estimate, 17.0%. |
| `difference_from_national_pct_points` | decimal | County point estimate minus national point estimate. |
| `health_rank_descending` | integer | Competition-free teaching order by point estimate, then FIPS. |
| `health_point_above_national` | character | Descriptive point direction, yes or no. |

Rank is an ordering device. It is not evidence of meaningful county separation.

### HPSA context fields

| Field | Type | Meaning |
|---|---|---|
| `active_hpsa_component_rows` | integer | Count of designated source component rows touching the county. |
| `active_hpsa_designations` | integer | Count of unique designated HPSA identifiers touching the county. |
| `max_active_hpsa_score` | integer or blank | Highest score among designated component rows touching the county. |
| `max_score_hpsa_ids` | character | Source identifiers tied at the county maximum. |
| `max_score_hpsa_names` | character | Source names tied at the county maximum. |
| `active_designation_types` | character | Sorted distinct active designation types. |
| `active_rural_statuses` | character | Sorted distinct active rural statuses. |
| `whole_county_geographic_hpsa` | character | Yes only when an active geographic or high-needs geographic HPSA has component type Single County. |
| `higher_hpsa_score_screen` | character | Yes when the highest active component score is at least 20. |

Component-row and designation counts should not be compared as if they were workforce rates. Large urban counties can contain many census-tract components.

### Decision fields

| Field | Type | Meaning |
|---|---|---|
| `bivariate_screen_class` | character | One of four combinations of the health and HPSA screen conditions. |
| `reference_review_eligible` | character | Yes when health is above the national point and HPSA score is at least 20. |
| `reference_review_order` | integer or blank | Order among the 19 eligible counties. |
| `reference_shortlist` | character | Yes for the first 12 eligible counties. |
| `time_alignment_status` | character | Declares the 2022 health measure and 2026 HPSA snapshot. |
| `interpretation_boundary` | character | States that the selected HPSA value is not a county workforce rate. |

## Four-class map rule

The class combines two declared binary questions:

1. Is the county health point estimate above the 17.0% national point estimate?
2. Is the highest active primary-care HPSA component score touching the county at least 20?

The release contains:

| Class | Counties |
|---|---:|
| Higher health estimate + higher HPSA score | 19 |
| Higher health estimate only | 54 |
| Higher HPSA score only | 4 |
| Neither screen condition | 23 |

The map legend must state the two rules. Labels such as high risk, critical, underserved county, or problem county are not acceptable substitutes.

## Reference review order

Nineteen counties meet both conditions. They are ordered by:

1. age-adjusted fair or poor health point estimate, descending;
2. highest active component HPSA score, descending;
3. county name, ascending; and
4. county FIPS, ascending.

The first twelve form the reference discussion list. This limit is a planning capacity assumption for the exercise, not a scientific threshold.

## Projection

The boundary release is stored in longitude and latitude. The lab applies an Albers equal-area formula with:

- first standard parallel: 29.5 degrees north;
- second standard parallel: 45.5 degrees north;
- latitude of origin: 23 degrees north; and
- central meridian: 96 degrees west.

The teaching formula supports a state-scale comparison without a new dependency. It is not a substitute for a verified production geographic workflow.

## Missingness and completeness

- Every one of the 100 counties has a PLACES estimate and boundary.
- Ninety-eight counties have at least one current designated HPSA record touching them.
- Two counties have no current designated record in the selected source.
- Blank maximum scores remain blank and are assigned to the lower HPSA screen condition.
- Historical and proposed-withdrawal records do not become current records.
- No missing source value is imputed.

## Time alignment

The health measure and shortage designations are not contemporaneous:

- PLACES measure year: 2022
- PLACES release: 2024
- HPSA source snapshot: 2026-08-29
- Census boundaries: generalized ACS 2024 service

The module treats them as cross-sectional planning context. It does not claim that a 2026 designation caused a 2022 health estimate.

## Rights decision

The direct HRSA HPSA source is used because its metadata marks the fields public and its usage page reports no usage limitation. Census and CDC government data retain their source notices.

The AHRF 2024-2025 download was inspected but is not redistributed. Its included documentation restricts reproduction and calls out copyrighted source fields. A downloadable file is not automatically an open teaching asset.

## Reproducibility

The builder uses the Python standard library. It pins:

- upstream PLACES checksum;
- upstream boundary checksum;
- full HRSA source checksum; and
- selected HRSA source checksum.

The validator checks 60 source, status, estimate, join, screen, order, and polygon conditions. Any source refresh requires a new release version and answer key.

## Interpretation limits

- PLACES estimates are model-based small-area estimates.
- County results do not describe every resident.
- HPSA score belongs to a designation component, not to the county as a whole.
- A maximum score ignores lower-scoring designations and scope differences.
- County boundaries do not represent travel time, referral networks, service areas, or local identity.
- A map can suggest spatial pattern but does not test clustering or causation.
- The selected sources do not measure local readiness, trust, assets, transportation, broadband, hours, language access, cost, or intervention fit.
- The reference list starts local review and cannot allocate resources by itself.
