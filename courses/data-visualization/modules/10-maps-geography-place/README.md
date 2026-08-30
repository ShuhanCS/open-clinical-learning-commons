# Module 10: Maps, geography, and place

Module 10 asks a practical question: does a map add decision value, or does it only turn a comparison into geography?

## Decision

A North Carolina population-health access planner must decide where regional listening sessions could help local teams examine fair or poor adult health, primary-care shortage designations, community priorities, and readiness.

The reference analysis uses a map and a non-map comparison together:

- the map shows regional pattern and neighboring counties;
- the ordered comparison shows rank, uncertainty, and the exact reference;
- the table preserves every value and definition;
- the decision note states what must be learned locally before resources are allocated.

## Learning outcomes

By the end of the module, learners can:

1. state why place matters to a named decision;
2. distinguish a rate, count, designation, score, and boundary;
3. join health, shortage, and geometry tables with five-character county FIPS;
4. map an age-adjusted percentage rather than raw population;
5. explain how aggregation and boundaries affect interpretation;
6. declare projection and classification choices;
7. compare a continuous map with a four-class bivariate screen;
8. build an ordered non-map view with intervals and a common reference;
9. decide when the map and non-map should be used together;
10. describe counties and residents without stigma;
11. preserve an exact table and equivalent text alternative; and
12. keep a transparent screen separate from an allocation rule.

## Public sources

The package reuses two pinned Commons releases and adds one direct HRSA source.

- CDC PLACES county data 2024 release:
  https://data.cdc.gov/d/fu4u-a9bh
- HRSA primary-care Health Professional Shortage Areas:
  https://data.hrsa.gov/DataDownload/DD_Files/BCD_HPSA_FCT_DET_PC.csv
- HRSA HPSA metadata:
  https://data.hrsa.gov/DataDownload/DD_Files/HPSA_DATAMART_METADATA.XLSX
- HRSA data download and usage page:
  https://data.hrsa.gov/data/download?data=HPSA
- Census generalized ACS 2024 state and county map service:
  https://tigerweb.geo.census.gov/arcgis/rest/services/Generalized_ACS2024/State_County/MapServer

The PLACES values are model-based small-area estimates. The HPSA table contains designation records and components. Neither is patient-level data.

## Why AHRF was not redistributed

The course brief originally named the Area Health Resources Files. The current AHRF download page says usage limitations are none, but the technical documentation inside the 2024-2025 release restricts reproduction and identifies copyrighted AMA, AHA, and ADA fields.

This open package therefore uses the directly public HRSA HPSA data mart instead of redistributing AHRF clinician fields. The decision is recorded in `source-record.yml`.

## Files

| File | Purpose |
|---|---|
| `data/hpsa_primary_care_nc_2026_08_29.csv` | All 1,546 mappable North Carolina primary-care HPSA source rows, including designated, proposed-withdrawal, and withdrawn records. |
| `data/nc_place_access_2026.csv` | One 100-county teaching table joining the selected health measure with current designated-HPSA context. |
| `data/nc_county_boundaries_2024.csv` | The exact 7,121-point generalized boundary release from Module 05. |
| `build_place_access_case.py` | Standard-library source selection, join, declared screen, and boundary-copy build. |
| `validate_place_access_case.py` | Sixty source, join, formula, ranking, shortlist, and geometry checks. |
| `lab.R` | Four reference figures, a 100-row exact table, and a text alternative. |
| `critique_charts.R` | Three deliberately flawed maps for repair. |
| `assessment.md` | Exact learner task, files, rubric, and pass conditions. |
| `instructor-notes.md` | Reproducible answers, facilitation notes, and critique key. |
| `data-spec.md` | Grain, dictionary, transformations, rights, and interpretation limits. |
| `source-record.yml` | URLs, retrieval dates, checksums, and provenance decisions. |
| `release.json` | Machine-readable release and review status. |

## Rebuild from the committed source selection

From the repository root:

```powershell
python courses/data-visualization/modules/10-maps-geography-place/build_place_access_case.py
```

The default rebuild uses:

- the committed Module 09 North Carolina PLACES table;
- the committed Module 10 HPSA source selection; and
- the committed Module 05 generalized boundaries.

It rewrites the three Module 10 releases deterministically.

## Refresh from the complete HRSA source

Download the complete source without changing its bytes:

```powershell
Invoke-WebRequest -Uri "https://data.hrsa.gov/DataDownload/DD_Files/BCD_HPSA_FCT_DET_PC.csv" -OutFile "$env:TEMP\BCD_HPSA_FCT_DET_PC.csv" -UseBasicParsing
python courses/data-visualization/modules/10-maps-geography-place/build_place_access_case.py --hpsa-input "$env:TEMP\BCD_HPSA_FCT_DET_PC.csv"
```

The released full-source checksum is pinned. A later HRSA update should fail rather than silently change the course. A source refresh requires a new source date, checksums, measured answers, version, and review.

## Validate

```powershell
python courses/data-visualization/modules/10-maps-geography-place/validate_place_access_case.py
```

Expected result:

```text
Module 10 place and access data passed 60 checks.
```

## Run the reference lab

R and ggplot2 are required.

```powershell
Rscript courses/data-visualization/modules/10-maps-geography-place/lab.R --output "$env:TEMP\oclc-da730-m10-lab"
```

The lab writes:

```text
01-health-choropleth.png
02-health-ordered-comparison.png
03-bivariate-screen-map.png
04-reference-review-list.png
place_decision_table.csv
alt-text-reference.md
```

The maps transform the released longitude and latitude points with an Albers equal-area formula. No geospatial package is required.

## Run the critique set

```powershell
Rscript courses/data-visualization/modules/10-maps-geography-place/critique_charts.R --output "$env:TEMP\oclc-da730-m10-critique"
```

The critique set writes:

```text
C1-raw-count-need-map.png
C2-arbitrary-bin-map.png
C3-stigmatizing-place-labels.png
```

## Measured teaching facts

- The PLACES measure year is 2022.
- Age-adjusted fair or poor health ranges from 12.1% to 27.2% across the 100 counties.
- The national age-adjusted point estimate is 17.0%.
- Seventy-three counties are above that national point estimate.
- The selected HRSA source release contains 1,546 mappable North Carolina rows.
- Of those, 740 rows and 210 unique HPSA identifiers are currently designated.
- Ninety-eight counties have at least one current designated record touching them.
- Twenty-three counties have a highest active component HPSA score of 20 or higher.
- Seven counties have a current whole-county geographic designation.
- Nineteen counties meet both declared screen conditions.
- The reference review list contains the first twelve of those nineteen.

The reference twelve are Robeson, Scotland, Hertford, Halifax, Warren, Greene, Washington, Wilson, Anson, Lenoir, Edgecombe, and Swain.

## Learner submission

```text
module-10/
  place-brief.md
  analysis.R
  health-map.png
  bivariate-map.png
  non-map.png
  decision-table.csv
  source-record.yml
  alt-text.md
  decision-note.md
  ai-use.md
```

See `assessment.md` for the exact contract.

## Interpretation boundary

The screen is a reproducible way to begin review, not a validated need score or resource-allocation rule. HPSA score is the highest active component score touching a county, not a county workforce rate. The PLACES measure and HPSA snapshot do not describe the same year. County aggregates conceal within-county communities, travel, care networks, local assets, implementation capacity, and resident priorities.

## Status

Version 0.1.0 is a runnable release candidate in Commons 0.21.0. Named population-health, shortage-designation, geography, equity, accessibility, and independent-instructor reviews remain pending.
