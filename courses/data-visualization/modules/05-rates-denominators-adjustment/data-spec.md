# Data specification

## Purpose

This package uses public county estimates to teach counts, denominators, crude prevalence, age adjustment, model-based uncertainty, low-denominator warnings, and the ecological fallacy.

The decision case is North Carolina adult diabetes prevention. It is not a clinical registry, claims analysis, direct county survey, or funding formula.

## Released files

| File | Rows | Unit | Purpose |
|---|---:|---|---|
| `data/places_diabetes_county_2024.csv` | 6,290 | Geography and value type | Complete national `DIABETES` source extract, including 6,288 county rows and two source national-summary rows. |
| `data/acs_adult_population_county_2024.csv` | 3,222 | ACS county geography | National county adult and older-population context derived from B01001. |
| `data/nc_county_boundaries_2024.csv` | 7,121 | Ordered polygon point | Generalized North Carolina county geometry for teaching maps. |
| `data/nc_diabetes_rates_2024.csv` | 100 | North Carolina county | Joined learner table for the module decision. |

Every file is rebuilt by `build_county_rates.py`. Raw download sizes and hashes are in `source-record.yml`.

## Source A: CDC PLACES

The CDC extract contains every row whose source `MeasureId` is `DIABETES` in dataset `fu4u-a9bh`.

Full landing page:

https://data.cdc.gov/d/fu4u-a9bh

The source reports two rows per county:

- `CrdPrv`: crude prevalence; and
- `AgeAdjPrv`: age-adjusted prevalence.

The source uses 2022 measure data and carries Census 2022 total and adult population fields. The source title calls the dataset the 2024 release. Those dates describe different parts of the release and must not be collapsed into one date.

### CDC fields

| Field | Type | Meaning |
|---|---|---|
| `year` | character | Source measure year. |
| `stateabbr` | character | State abbreviation. |
| `statedesc` | character | State name. |
| `locationname` | character | County name, blank for the source national summary. |
| `locationid` | character | Five-character county FIPS or source national-summary identifier. |
| `measureid` | character | `DIABETES`. |
| `measure` | character | `Diagnosed diabetes among adults`. |
| `data_value_type` | character | Crude or age-adjusted prevalence. |
| `datavaluetypeid` | character | `CrdPrv` or `AgeAdjPrv`. |
| `data_value` | numeric | Modeled prevalence percentage. |
| `low_confidence_limit` | numeric | Lower source 95% confidence limit. |
| `high_confidence_limit` | numeric | Upper source 95% confidence limit. |
| `totalpopulation` | integer | Census 2022 total population carried by PLACES. |
| `totalpop18plus` | integer | Census 2022 adult population carried by PLACES. |
| `data_value_footnote_symbol` | character | Source footnote symbol. |
| `data_value_footnote` | character | Source footnote text. |

### CDC transformation

The build:

1. requests only `DIABETES` rows from the public Socrata endpoint;
2. keeps all 16 requested fields;
3. sorts by source location ID and value-type ID;
4. confirms 6,290 rows and the two expected value types;
5. confirms 3,144 county FIPS values and one row of each type per county;
6. preserves the source national summary rows; and
7. writes a normalized UTF-8 CSV.

The build does not impute, smooth, relabel, or recalculate a CDC prevalence estimate.

## Source B: ACS B01001

The 2024 ACS 5-year table-based Summary File provides the public age and sex table without requiring a private API key.

Full source file:

https://www2.census.gov/programs-surveys/acs/summary_file/2024/table-based-SF/data/5YRData/acsdt5y2024-b01001.dat

### County selection

The build keeps every `GEO_ID` beginning with `0500000US`. The last five characters become `county_fips`.

Names are not required for the national ACS extract because the stable FIPS key joins to PLACES. The module never joins on county name.

### Adult population derivation

The adult estimate is the sum of the B01001 estimate cells representing ages 18 and older:

```text
Male:   B01001_E007 through B01001_E025
Female: B01001_E031 through B01001_E049
```

### Age-65-plus derivation

The older-population estimate is the sum of:

```text
Male:   B01001_E020 through B01001_E025
Female: B01001_E044 through B01001_E049
```

### Approximate margin of error for a sum

For component 90% margins of error `m1` through `mk`, the build uses:

```text
derived_moe90 = round(sqrt(m1^2 + m2^2 + ... + mk^2))
```

This is the standard approximation for a sum when covariance is not available. It is not an exact replicate-weight estimate.

The Census sentinel `-555555555` means the margin is not available or not applicable. When any required component uses that sentinel, the derived margin remains blank and `acs_moe_status` records the reason. All 100 North Carolina teaching rows have reported component margins.

### ACS output fields

| Field | Type | Meaning |
|---|---|---|
| `geo_id` | character | Full ACS county geography ID. |
| `county_fips` | character | Five-character FIPS. |
| `acs_adult_population` | integer | Derived population age 18 and older. |
| `acs_adult_moe90` | integer or blank | Approximate 90% margin of error for the adult sum. |
| `acs_65plus_population` | integer | Derived population age 65 and older. |
| `acs_65plus_moe90` | integer or blank | Approximate 90% margin of error for the older sum. |
| `acs_65plus_share_adult_pct` | numeric | Older population divided by adult population. |
| `acs_moe_status` | character | `reported` or explicit component-unavailability text. |
| `acs_period` | character | `2020-2024`. |
| `acs_table` | character | `B01001`. |

The older-adult share is context. It may help generate a question about crude and adjusted differences, but it does not reconstruct the PLACES age adjustment.

## Source C: TIGERweb boundaries

The module uses the Census generalized ACS 2024 county layer at 1:5,000,000 scale.

Full service:

https://tigerweb.geo.census.gov/arcgis/rest/services/Generalized_ACS2024/State_County/MapServer

The query returns every North Carolina county feature in GeoJSON. The build flattens Polygon and MultiPolygon rings so base CSV and ggplot2 can render the critique map without a geospatial package.

### Boundary fields

| Field | Type | Meaning |
|---|---|---|
| `county_fips` | character | Five-character Census GEOID. |
| `county_name` | character | Census county label. |
| `polygon_group` | character | County, polygon, and ring identifier. |
| `point_order` | integer | Coordinate order within the ring. |
| `longitude` | numeric | Longitude in EPSG:4326. |
| `latitude` | numeric | Latitude in EPSG:4326. |

Every polygon part is closed by repeating its first point when needed. The generalized boundaries are teaching geometry, not operational geography.

## Joined North Carolina table

The teaching table has 100 rows and 27 columns.

| Field | Type | Meaning and rule |
|---|---|---|
| `county_fips` | character | Five-character join key. |
| `state_abbr` | character | `NC`. |
| `state_name` | character | `North Carolina`. |
| `county_name` | character | PLACES county name. |
| `measure_id` | character | `DIABETES`. |
| `measure_name` | character | Diagnosed diabetes among adults. |
| `measure_year` | integer | `2022`. |
| `release_label` | character | `PLACES 2024 release`. |
| `places_total_population` | integer | Census 2022 total population carried by PLACES. |
| `places_adult_population` | integer | Census 2022 adult population carried by PLACES. |
| `crude_prevalence_pct` | numeric | Modeled crude prevalence percentage. |
| `crude_low_95_pct` | numeric | Lower crude source interval. |
| `crude_high_95_pct` | numeric | Upper crude source interval. |
| `age_adjusted_prevalence_pct` | numeric | Modeled age-adjusted prevalence percentage. |
| `age_adjusted_low_95_pct` | numeric | Lower adjusted source interval. |
| `age_adjusted_high_95_pct` | numeric | Upper adjusted source interval. |
| `modeled_adult_count` | integer | Rounded crude prevalence times PLACES adults. |
| `count_status` | character | `modeled estimate, not observed cases`. |
| `acs_adult_population` | integer | Derived ACS adult context. |
| `acs_adult_moe90` | integer | Approximate ACS adult margin of error. |
| `acs_65plus_population` | integer | Derived ACS older population. |
| `acs_65plus_moe90` | integer | Approximate ACS older-population margin. |
| `acs_65plus_share_adult_pct` | numeric | Older share of ACS adults. |
| `acs_moe_status` | character | Availability status for derived ACS margins. |
| `adult_population_difference_pct` | numeric | ACS adult estimate minus PLACES adults, divided by PLACES adults. |
| `teaching_low_denominator_flag` | integer | One when PLACES adults are below 10,000. |
| `source_footnote` | character | CDC footnote text, blank when none. |

## Derived modeled count

```text
modeled_adult_count = round(crude_prevalence_pct / 100 * places_adult_population)
```

This field is a transformation of a modeled prevalence estimate. It is not an observed number of diagnoses, claims, patients, survey respondents, or program participants.

Never multiply `age_adjusted_prevalence_pct` by population. The adjusted estimate describes a standardized comparison population rather than the county's current age distribution.

## Training low-denominator rule

The CDC source publishes all 100 North Carolina diabetes estimates. The course does not pretend that CDC suppressed nine values.

Instead it declares this teaching warning:

```text
teaching_low_denominator_flag = 1 when places_adult_population < 10000
```

Nine counties trigger the rule: Alleghany, Camden, Clay, Gates, Graham, Hyde, Jones, Tyrrell, and Washington.

The warning means `do not treat this rank as decisive without local validation`. It does not mean the CDC estimate is invalid or formally unstable. Module 06 handles the interval and stability question.

## Measured release properties

- Modeled count range: 428 to 93,326.
- Crude prevalence range: 8.5% to 20.0%.
- Age-adjusted prevalence range: 8.0% to 15.6%.
- PLACES adult population range: 2,644 to 908,531.
- Largest count-to-adjusted rank shift: 93 places.
- Largest crude-to-adjusted rank shift: 57 places.
- Overlap between top 12 modeled counts and top 12 adjusted prevalence values: zero counties.
- Overlap between top 12 crude and top 12 adjusted prevalence values: nine counties.

These are properties of the pinned teaching release, not general facts about county health data.

## Validation

Run:

```powershell
python validate_county_rates.py
```

The validator checks hashes, row counts, fields, county identities, value types, interval containment, the modeled-count formula, ACS margin availability for the teaching case, the training threshold, rank contrasts, boundary coverage, and polygon closure.

## Rebuild

From the module directory:

```powershell
python build_county_rates.py
```

The default build downloads about 201 MB across the three public sources. It fails when a raw source byte count or SHA-256 hash changes. That failure protects provenance; it is not a request to overwrite the released files silently.

For a checked local copy of the raw files:

```powershell
python build_county_rates.py --cdc-input places.csv --acs-input acsdt5y2024-b01001.dat --tiger-input nc-counties.geojson
```

## Claim limits

The released data cannot establish:

- an individual's diabetes diagnosis or risk;
- observed county case counts;
- local incidence or new diagnoses;
- a causal explanation for county differences;
- intervention effectiveness;
- program readiness or community preference;
- need for a particular budget;
- within-county distribution; or
- statistical difference between county pairs without further analysis.
