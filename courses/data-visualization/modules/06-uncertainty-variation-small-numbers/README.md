# Module 06: Uncertainty, variation, and small numbers

This module asks a Massachusetts clinical quality committee whether a ranked list of heart failure readmission estimates identifies hospitals that are meaningfully different. Learners compare the rank with CMS source intervals, denominators, national comparison categories, and reporting footnotes.

## Decision

Which hospitals warrant focused review, which should be monitored, and which lack enough public evidence for a comparison?

The pinned Massachusetts case has 65 hospital rows. Fifty-three have reported estimates. A point-only chart assigns all 53 a unique position, but CMS classifies 52 as no different from the national rate and one as worse. The remaining 12 rows are unavailable or have too few cases.

## Learning outcomes

After this module, a learner can:

- preserve a point estimate, source interval, denominator, period, status, and footnote;
- explain why rank can overstate separation;
- distinguish comparison with a national benchmark from pairwise hospital comparison;
- keep suppressed results visible without imputing zero;
- use a caterpillar plot and exact-value table for a review decision;
- state why denominator alone cannot recreate a risk-standardized interval.

## Source release

- Hospital data: https://data.cms.gov/provider-data/dataset/632h-zaca
- National data: https://data.cms.gov/provider-data/dataset/cvcs-xecj
- Footnote crosswalk: https://data.cms.gov/provider-data/dataset/y9us-9xdf
- Data dictionary: https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/hospital/HOSPITAL_Data_Dictionary.pdf
- Measure: `READM_30_HF`, Heart failure (HF) 30-Day Readmission Rate
- Period: 2023-07-01 through 2025-06-30
- Catalog release date: 2026-08-13
- National rate: 21.3

The repository keeps every national hospital row for the selected measure, all national summary rows, and the full CMS footnote crosswalk. The build validates the complete 67,060-row raw hospital download before filtering.

## Files

```text
06-uncertainty-variation-small-numbers/
  README.md
  assessment.md
  build_hf_uncertainty.py
  critique_charts.R
  data-spec.md
  instructor-notes.md
  lab.R
  release.json
  source-record.yml
  validate_hf_uncertainty.py
  data/
    cms_footnote_crosswalk_2026.csv
    cms_hf_readmission_hospitals_2026.csv
    cms_unplanned_national_2026.csv
    ma_hf_readmission_uncertainty_2026.csv
```

## Rebuild the data

Python's standard library is enough:

```powershell
python build_hf_uncertainty.py
```

The script downloads three pinned CMS files, checks their byte counts and SHA-256 hashes, and writes four deterministic CSV files. To use already downloaded files:

```powershell
python build_hf_uncertainty.py `
  --hospital-input C:\path\Unplanned_Hospital_Visits-Hospital.csv `
  --national-input C:\path\Unplanned_Hospital_Visits-National.csv `
  --footnote-input C:\path\Footnote_Crosswalk.csv
```

The build stops if CMS replaces any pinned file. Update the source record and release metadata before accepting a newer release.

## Validate the data

```powershell
python validate_hf_uncertainty.py
```

The validator checks 42 release, source, missingness, interval, benchmark, ranking, and teaching-case conditions.

## Run the lab

Requirements:

- R 4.x
- ggplot2

```powershell
Rscript lab.R
```

Optional paths:

```powershell
Rscript lab.R --data data/ma_hf_readmission_uncertainty_2026.csv --output output
```

The lab creates:

```text
output/
  01-point-rank.png
  02-interval-caterpillar.png
  03-denominator-and-width.png
  04-reporting-status.png
  ma_hf_uncertainty_decision_table.csv
```

## Run the critique set

```powershell
Rscript critique_charts.R
```

The critique creates two deliberately flawed figures:

```text
critique-output/
  C1-point-only-league-table.png
  C2-hidden-small-n.png
```

Learners repair both. The first labels the highest ten point estimates as the ten worst hospitals while hiding intervals and comparison categories. The second presents small and large denominators with equal visual certainty.

## Measured teaching facts

| Quantity | Result |
|---|---:|
| National selected rows | 4,790 |
| National reported estimates | 3,253 |
| Massachusetts rows | 65 |
| Massachusetts reported estimates | 53 |
| Massachusetts no different from national | 52 |
| Massachusetts worse than national | 1 |
| Massachusetts too few | 2 |
| Massachusetts not available | 10 |
| Reported denominator range | 30 to 2,088 |
| Reported point range | 19.7 to 25.2 |
| Source interval-width range | 6.9 to 9.2 |
| Top-ten ranks classified worse | 1 of 10 |

All 1,378 pairs of displayed Massachusetts source intervals overlap descriptively. That does not test a pairwise hospital difference and does not prove equivalence.

## Learner submission

```text
module-06/
  uncertainty-brief.md
  analysis.R
  figure.png
  source-record.yml
  alt-text.md
  decision-note.md
  ai-use.md
```

See [assessment.md](assessment.md) for the exact prompt and rubric. See [instructor-notes.md](instructor-notes.md) for the answer key and facilitation notes.

## Interpretation boundary

The CMS measure is a risk-standardized hospital estimate. Do not calculate a replacement binomial interval from its denominator. Do not read interval overlap as a formal pairwise test. Do not translate a CMS comparison category into a causal claim about hospital care.

## Week-3 checkpoint

This module closes the visualization judgment dossier from Modules 01 through 06. The exact checkpoint package is defined in the full module specification and the DA-730 course specification.

## Status

This package is a runnable release candidate. Technical checks are complete when `release.json` says so. Statistical, clinical quality, accessibility, source-fidelity, and independent-teachability reviews remain human gates.
