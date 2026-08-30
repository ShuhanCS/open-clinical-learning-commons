# Module 12: Dashboards and multi-view composition

Module 12 asks what minimum set of coordinated views helps one decision owner notice an exception, understand its limits, and take the next defensible action.

## Decision

An emergency department quality director at a low-volume Massachusetts hospital must decide whether a public CMS signal is sufficient to open a local definition and current-data review.

The reference dashboard focuses on Anna Jaques Hospital because the released OP-22 value is 23 percent, the highest observed value among 53 reporting Massachusetts hospitals and above the mock 10-percent review trigger. The public period ended 590 days before CMS released the file. The dashboard therefore recommends validation and current local data review, not a current performance judgment.

## Five views

1. One decision alert with the value, peer reference, mock trigger, and immediate action.
2. One freshness card showing source windows and release lag.
3. One OP-22 peer distribution with the selected hospital, state median, and mock trigger.
4. One OP-18b peer distribution kept separate because it uses minutes and a later reporting window.
5. One ordered action path with a named owner.

Any view without a decision purpose is removed.

## Learning outcomes

By the end of the module, learners can:

1. name one dashboard audience, decision, and action;
2. distinguish public reporting review from operational monitoring;
3. limit a dashboard to three through five necessary views;
4. define every measure, denominator, unit, direction, window, and owner;
5. keep different units and periods visually separate;
6. distinguish a descriptive peer median from a benchmark;
7. distinguish a scenario trigger from an official threshold;
8. connect every alert to an ordered response;
9. state refresh cadence and stale-data behavior;
10. preserve footnotes, unavailable values, samples, and exact tables;
11. write an equivalent text alternative; and
12. remove KPI walls, decorative widgets, and filters without a task.

## Public sources

- CMS dataset: https://data.cms.gov/provider-data/dataset/yv7e-xc69
- Complete pinned CSV: https://data.cms.gov/provider-data/sites/default/files/resources/0437b5494ac61507ad90f2af6b8085a7_1785189967/Timely_and_Effective_Care-Hospital.csv
- Hospital data dictionary: https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/hospital/HOSPITAL_Data_Dictionary.pdf
- Current measure periods: https://data.cms.gov/provider-data/topics/hospitals/measures-and-current-data-collection-periods
- AHRQ dashboard guidance page: https://www.ahrq.gov/evidencenow/tools/dashboard-best-practice.html
- AHRQ display guidance: https://www.ahrq.gov/talkingquality/translate/display/index.html

The package links to and paraphrases the AHRQ guidance. It does not redistribute the third-party copyrighted PDF linked from the AHRQ dashboard page.

## Released data

| File | Grain | Rows | Purpose |
|---|---|---:|---|
| `data/cms_ma_ed_dashboard_source_2026.csv` | One hospital-measure-period row | 186 | Every Massachusetts row for EDV, OP_18b, and OP_22 from the pinned CMS release. |
| `data/ma_ed_public_reporting_dashboard_2026.csv` | One hospital-measure-period row | 186 | Numeric status, peer references, ranks, mock triggers, lag, and actions. |
| `data/ed_dashboard_measure_dictionary_2026.csv` | One measure | 3 | Definition, population, sample meaning, window, trigger, owner, action, cadence, and limit. |

Street address, ZIP code, and telephone number are omitted because the decision does not need them.

## Reference facts

| Item | Value |
|---|---:|
| Massachusetts facilities | 62 |
| Anna Jaques ED volume category | Low |
| Anna Jaques OP-18b | 188 minutes, sample 422 |
| Massachusetts OP-18b median | 211.5 minutes across 54 reported hospitals |
| Mock OP-18b trigger | 240 minutes, not crossed |
| Anna Jaques OP-22 | 23%, denominator 19,211 |
| Massachusetts OP-22 median | 3% across 53 reported hospitals |
| Mock OP-22 trigger | 10%, crossed |
| OP-18b period lag at release | 317 days |
| OP-22 period lag at release | 590 days |

The medians are descriptive peer references. The triggers are mock QI charter assumptions. Neither is a CMS benchmark.

## Files

| File | Purpose |
|---|---|
| `build_ed_dashboard_case.py` | Standard-library source selection, peer context, screen, source-lag, and dictionary build. |
| `validate_ed_dashboard_case.py` | One hundred seventy-nine source, definition, period, calculation, action, and release checks. |
| `lab.R` | Five-view dashboard, exact decision table, and text alternative using ggplot2 and base R grid. |
| `critique_charts.R` | Three deliberately flawed dashboard examples. |
| `assessment.md` | Exact learner package, rubric, and pass conditions. |
| `instructor-notes.md` | Measured answers, facilitation plan, and critique key. |
| `data-spec.md` | Data lineage, definitions, formulas, source rights, and limits. |
| `source-record.yml` | URLs, checksums, reporting periods, trigger contract, and rights. |
| `release.json` | Machine-readable release and review state. |

## Rebuild

From the repository root:

```powershell
python courses/data-visualization/modules/12-dashboards-multi-view-composition/build_ed_dashboard_case.py
```

The default build uses the committed 186-row source selection.

To refresh from the complete pinned CMS CSV:

```powershell
Invoke-WebRequest -Uri "https://data.cms.gov/provider-data/sites/default/files/resources/0437b5494ac61507ad90f2af6b8085a7_1785189967/Timely_and_Effective_Care-Hospital.csv" -OutFile "$env:TEMP\Timely_and_Effective_Care-Hospital.csv" -UseBasicParsing
python courses/data-visualization/modules/12-dashboards-multi-view-composition/build_ed_dashboard_case.py --source-csv "$env:TEMP\Timely_and_Effective_Care-Hospital.csv"
```

The complete source checksum is pinned. A changed source fails instead of silently changing the dashboard.

## Validate

```powershell
python courses/data-visualization/modules/12-dashboards-multi-view-composition/validate_ed_dashboard_case.py
```

Expected result:

```text
Module 12 ED dashboard data passed 179 checks.
```

## Run the reference lab

R and ggplot2 are required. No dashboard-specific package is used.

```powershell
Rscript courses/data-visualization/modules/12-dashboards-multi-view-composition/lab.R --output "$env:TEMP\oclc-da730-m12-lab"
```

## Run the critique lab

```powershell
Rscript courses/data-visualization/modules/12-dashboards-multi-view-composition/critique_charts.R --output "$env:TEMP\oclc-da730-m12-critiques"
```

## Learner package

```text
module-12/
  dashboard-brief.md
  analysis.R
  dashboard.png
  dashboard-decision-table.csv
  measure-dictionary.csv
  source-record.yml
  alt-text.md
  decision-note.md
  ai-use.md
```

## Interpretation boundary

The released dashboard supports a public-reporting validation decision. It does not support real-time staffing, current performance rating, causal attribution, or an intervention-effect claim. Those actions require current, governed local data and clinical review.

## Handoff

Checkpoint 2 packages Modules 07 through 12. Module 13 then turns one sourced, reproducible, accessible analysis into a final decision story for two audiences.
