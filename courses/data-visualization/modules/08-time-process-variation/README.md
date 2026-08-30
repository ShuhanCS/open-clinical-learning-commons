# Module 08: Time and process variation

This module asks a hospital operations analyst to decide whether a weekly change is a useful signal, ordinary variation, a seasonal pattern, or a reporting artifact. Learners keep the raw series visible, declare every baseline, and read reporting coverage beside the clinical measure.

## Decision

What should an operations leader investigate now, what should remain under routine monitoring, and what cannot be concluded from a changing jurisdiction-level aggregate?

The worked case uses 94 consecutive weeks of public Massachusetts hospital data from the CDC National Healthcare Safety Network. The source contains inpatient and ICU capacity, occupancy, respiratory admissions, and reporting coverage.

## Learning outcomes

After this module, a learner can:

- select a run chart, seasonal comparison, or exploratory process chart for a stated decision;
- distinguish chronological order from a category display;
- define a baseline before calculating a center line or limits;
- show raw weekly values whenever short changes matter;
- explain what a trailing mean reveals and hides;
- place reporting coverage beside a changing aggregate without using a deceptive dual axis;
- treat missing periods and source-schema changes as evidence, not decoration;
- annotate a reporting event without inventing a clinical intervention;
- use exploratory control limits without claiming formal statistical process control;
- provide an exact weekly table and accessible text alternative.

## Public source

- CDC landing page: https://data.cdc.gov/Public-Health-Surveillance/Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/rhwp-grxi
- CDC metadata API: https://data.cdc.gov/api/views/rhwp-grxi
- Pinned Socrata query: https://data.cdc.gov/resource/rhwp-grxi.csv?%24select=weekendingdate%2Cjurisdiction%2Crespseason%2Cnuminptbeds%2Cnuminptbedsocc%2Cpctinptbedsocc%2Cnumicubeds%2Cnumicubedsocc%2Cpcticubedsocc%2Ctotalconfc19newadm%2Ctotalconfflunewadm%2Ctotalconfrsvnewadm%2Cpctinptbedsocchosprep%2Cpctinptbedsoccperchosprep&%24where=weekendingdate+between+%272024-11-09T00%3A00%3A00.000%27+and+%272026-08-22T00%3A00%3A00.000%27&%24order=weekendingdate%2Cjurisdiction&%24limit=10000

The release includes 6,208 jurisdiction-week rows from 67 jurisdictions. The Massachusetts teaching table contains 94 complete weekly rows from 2024-11-09 through 2026-08-22.

## Files

```text
08-time-process-variation/
  README.md
  assessment.md
  build_nhsn_time_series.py
  critique_charts.R
  data-spec.md
  instructor-notes.md
  lab.R
  release.json
  source-record.yml
  validate_nhsn_time_series.py
  data/
    ma_hospital_capacity_time_2024_2026.csv
    nhsn_hospital_capacity_jurisdiction_2024_2026.csv
```

## Rebuild the releases

Python's standard library is enough. The live query is checksum pinned, so a source revision stops the build instead of silently changing the lesson.

```powershell
python build_nhsn_time_series.py
```

For an offline rebuild, save the exact query response and pass it explicitly:

```powershell
python build_nhsn_time_series.py --raw-input nhsn-pinned-query.csv
```

## Validate the data

```powershell
python validate_nhsn_time_series.py
```

The validator runs 47 checks across source identity, checksums, keys, dates, missingness, published anomalies, weekly continuity, derived fields, and measured teaching facts.

## Run the lab

Requirements:

- R 4.x
- ggplot2

```powershell
Rscript lab.R
```

Optional paths:

```powershell
Rscript lab.R --data data/ma_hospital_capacity_time_2024_2026.csv --output output
```

The lab creates:

```text
output/
  01-occupancy-run-chart.png
  02-respiratory-admission-seasonality.png
  03-raw-and-smoothed-occupancy.png
  04-reporting-coverage-context.png
  05-exploratory-control-chart.png
  weekly_time_decision_table.csv
  alt-text-reference.md
```

## Run the critique set

```powershell
Rscript critique_charts.R
```

The critique set creates three deliberately flawed figures:

```text
critique-output/
  C1-arbitrary-dual-axis.png
  C2-smoothed-line-hides-weekly-change.png
  C3-unsupported-control-limits.png
```

## Measured teaching facts

| Quantity | Result |
|---|---:|
| Massachusetts weeks | 94 |
| Date gaps | 0 |
| Occupancy minimum | 77.96% on 2024-12-28 |
| Occupancy maximum | 87.30% on 2025-03-01 |
| Series median | 84.12% |
| Respiratory admission maximum | 1,996 on 2025-02-08 |
| Reporting coverage minimum | 67.05% on 2025-02-15 |
| Largest weekly rise | 6.35 percentage points on 2025-01-04 |
| Largest weekly decline | 7.79 percentage points on 2024-12-28 |
| Source season field unavailable | 61 weeks |
| Data validation checks | 47 |

## Learner submission

```text
module-08/
  time-audit.md
  analysis.R
  run-chart.png
  comparison-chart.png
  process-chart.png
  decision-table.csv
  alt-text.md
  decision-note.md
  ai-use.md
```

See `assessment.md` for the exact prompt and rubric. See `instructor-notes.md` for the answer key and facilitation sequence.

## Interpretation boundary

These are weekly jurisdiction aggregates across reporting hospitals, not one hospital's internal process. Reporting coverage and hospital mix change. Exploratory limits may generate questions, but they do not establish special cause, seasonality, capacity failure, or an intervention effect. Preserve official anomalies and missing values unless a documented source correction is available.

## Status

This package is a runnable release candidate. Technical checks are complete when `release.json` says so. Clinical operations, statistical process control, public-source fidelity, visualization, accessibility, and independent-teachability reviews remain human gates.
