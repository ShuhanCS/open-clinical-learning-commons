# Module 09: Comparison and small multiples

This module asks a state population-health analyst to compare 100 North Carolina counties across five CDC PLACES measures without changing scales, order, reference definitions, or uncertainty from panel to panel.

## Decision

Which twelve counties should enter a partnership-readiness review, and why is the comparison rule suitable only for screening rather than automatic funding or program selection?

The worked case uses five 2022 age-adjusted adult prevalence measures: current smoking, diagnosed diabetes, fair or poor health, no leisure-time physical activity, and obesity. The source release preserves both crude and age-adjusted estimates, 95 percent confidence limits, adult populations, and national summary rows.

## Learning outcomes

After this module, a learner can:

- choose a dot plot, dumbbell, slope display, or small multiple for a stated comparison;
- keep the same scale, order, and reference definition across comparable panels;
- distinguish a shared visual scale from a shared clinical meaning;
- preserve within-group variation instead of showing only group means;
- choose and disclose an ordering rule;
- compare crude and age-adjusted estimates without calling adjustment improvement;
- show uncertainty without treating interval overlap as a pairwise test;
- keep the comparison denominator and adult population visible;
- explain why a count across measures is not automatically a validated risk score;
- produce a shortlist for review without turning it into an allocation decision.

## Public source

- CDC PLACES dataset: https://data.cdc.gov/d/fu4u-a9bh
- CDC metadata API: https://data.cdc.gov/api/views/fu4u-a9bh
- CDC PLACES methodology: https://www.cdc.gov/places/methodology/index.html
- CDC health outcome definitions: https://www.cdc.gov/places/measure-definitions/health-outcomes.html
- CDC health risk behavior definitions: https://www.cdc.gov/places/measure-definitions/health-risk-behaviors.html
- CDC health status definitions: https://www.cdc.gov/places/measure-definitions/health-status.html

The exact Socrata query is pinned in `source-record.yml` and `release.json`. It returns 31,450 rows: crude and age-adjusted estimates for five measures across 3,144 counties plus the national summary.

## Files

```text
09-comparison-small-multiples/
  README.md
  assessment.md
  build_places_comparison.py
  critique_charts.R
  data-spec.md
  instructor-notes.md
  lab.R
  release.json
  source-record.yml
  validate_places_comparison.py
  data/
    nc_county_health_profiles_2024.csv
    places_county_comparison_2024.csv
```

## Rebuild the releases

Python's standard library is enough. The source query is checksum pinned.

```powershell
python build_places_comparison.py
```

For an offline rebuild, save the exact query response and pass it explicitly:

```powershell
python build_places_comparison.py --raw-input places-comparison-pinned-query.csv
```

## Validate the data

```powershell
python validate_places_comparison.py
```

The validator runs 58 checks across query identity, checksums, keys, measure years, geographies, value types, intervals, source reconciliation, ranks, reference differences, profile order, denominators, and measured teaching facts.

## Run the lab

Requirements:

- R 4.x
- ggplot2

```powershell
Rscript lab.R
```

Optional paths:

```powershell
Rscript lab.R --data data/nc_county_health_profiles_2024.csv --output output
```

The lab creates:

```text
output/
  01-all-counties-ordered-small-multiples.png
  02-shortlist-difference-from-national.png
  03-crude-age-adjusted-dumbbells.png
  04-profile-count-denominator.png
  comparison_decision_table.csv
  alt-text-reference.md
```

## Run the critique set

```powershell
Rscript critique_charts.R
```

The critique set creates:

```text
critique-output/
  C1-free-panel-scales.png
  C2-changing-panel-baselines.png
  C3-overloaded-rainbow-profiles.png
```

## Measured teaching facts

| Measure | North Carolina range | U.S. reference | Counties above U.S. point |
|---|---:|---:|---:|
| Current smoking | 9.7% to 25.0% | 13.2% | 89 of 100 |
| Diagnosed diabetes | 8.0% to 15.6% | 10.4% | 62 of 100 |
| Fair or poor health | 12.1% to 27.2% | 17.0% | 73 of 100 |
| No leisure activity | 15.8% to 33.1% | 23.0% | 68 of 100 |
| Obesity | 25.6% to 43.5% | 33.4% | 70 of 100 |

Fifty-four counties are above the matching national point estimate on all five measures. Nine are at or below all five. Adult population ranges from 2,644 to 908,531.

The reference twelve-county order is Robeson, Bertie, Hertford, Anson, Hyde, Nash, Warren, Columbus, Scotland, Halifax, Swain, and Sampson. It first counts point estimates above the national reference, then uses the largest gap and county name. This is a transparent teaching order, not a validated clinical, equity, readiness, or funding score.

## Learner submission

```text
module-09/
  comparison-brief.md
  analysis.R
  all-groups.png
  shortlist-profile.png
  adjustment-comparison.png
  decision-table.csv
  alt-text.md
  decision-note.md
  ai-use.md
```

See `assessment.md` for the exact prompt and rubric. See `instructor-notes.md` for the answer key and facilitation sequence.

## Interpretation boundary

PLACES estimates are model-based small-area prevalence estimates, not direct county survey estimates or observed diagnoses. A higher point estimate does not establish cause, program readiness, or the experience of every community within a county. Interval overlap is descriptive here and is not a formal pairwise test. A five-measure count gives each selected measure equal weight and omits community priorities, capacity, cost, population size, and within-county inequity.

## Status

This package is a runnable release candidate. Technical checks are complete when `release.json` says so. Population-health, epidemiology, equity, visualization, accessibility, and independent-teachability reviews remain human gates.
