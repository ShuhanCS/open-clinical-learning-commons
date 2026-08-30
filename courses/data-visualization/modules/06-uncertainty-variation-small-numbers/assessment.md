# Module 06 assessment

## Decision prompt

A Massachusetts clinical quality committee has received a list of hospitals sorted by the CMS heart failure 30-day readmission point estimate. The chair calls the ten highest values the ten worst hospitals and proposes an immediate focused review at all ten.

Use the pinned `READM_30_HF` release to decide whether that recommendation is supported. Preserve the source interval, denominator, comparison category, reporting status, footnote, and dates.

## Required submission

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

An approved editable analysis file may replace `analysis.R`. Screenshots and exported images do not replace editable analysis.

## Required analysis

Your analysis must:

1. Load `data/ma_hf_readmission_uncertainty_2026.csv`.
2. Confirm 65 Massachusetts rows.
3. Confirm 53 reported estimates, 2 too-few rows, and 10 not-available rows.
4. Reproduce the 52 no-different and 1 worse comparison counts among reported rows.
5. Reproduce the ten highest point estimates.
6. Keep the national rate of 21.3 visible.
7. Keep the 2023-07-01 through 2025-06-30 period visible.
8. Show each selected point with the CMS lower and higher estimates.
9. Keep the denominator available in the figure or exact-value table.
10. Explain what evidence the committee should request next.

## Required `uncertainty-brief.md`

Use these headings:

```text
# Uncertainty brief
## Decision and audience
## Measure and population
## Point-rank finding
## Interval finding
## Reporting-status audit
## Recommendation
## Evidence needed next
## Limits
```

The brief must answer:

- What does the point-only rank make easy to see?
- What does it hide?
- How many top-ten hospitals does CMS classify as worse than the national rate?
- What can the source intervals support?
- What can visual interval overlap not establish?
- How are suppressed results handled?
- What decision follows from this release?

## Required figure

`figure.png` must contain:

- hospital point estimates;
- CMS source intervals;
- a directly labeled 21.3 national reference;
- comparison status shown with color and shape or another redundant pair;
- measure ID and reporting period;
- a note that pairwise difference is not tested;
- readable labels or a clear link to the exact-value table.

A point-only rank chart cannot serve as the final figure unless it appears beside an uncertainty-aware correction and is explicitly labeled as inadequate for the decision.

## Required source record

Use the keys in the full specification. At minimum, record the publisher, dataset ID, exact landing and download URLs, retrieval date, release date, measure, period, geography, raw byte count, raw hash, selected rows, teaching extract hash, build script, data dictionary, footnote crosswalk, rights, and known limits.

## Required alt text

State:

- that the figure shows Massachusetts hospital heart failure readmission estimates;
- how many reported estimates appear;
- the national rate;
- that one hospital is source-classified worse and 52 are no different;
- that 12 other hospital rows lack a public estimate;
- that ranks imply more separation than the source comparison supports.

Do not list every hospital in alt text. Use the table for exact lookup.

## Required decision note

Maximum 350 words.

```text
# Decision note
## Finding
## Action
## Uncertainty
## Evidence needed next
```

The action must separate:

- focused review supported by the CMS comparison category;
- monitoring or local validation prompted by a high point estimate;
- no public estimate available.

## Critique and repair

Run `critique_charts.R`. For each flawed chart, submit:

1. the implied decision;
2. at least four missing or misleading elements;
3. the repair you made;
4. one sentence that states the corrected claim boundary.

### C1: point-only league table

Identify why the title, selection, baseline, color, and missing intervals turn a source comparison into a verdict.

### C2: hidden small numbers

Identify why equal point size does not communicate equal precision and why denominator alone still does not recreate the CMS model.

## Short-answer checks

1. Why does a list of 53 different point estimates always produce ranks?
2. How many top-ten Massachusetts hospitals are CMS-classified worse than the national rate?
3. Does overlap between two displayed source intervals prove the hospitals are equivalent?
4. Why should `Not Available` remain blank rather than zero?
5. Why is a homemade binomial interval inappropriate here?
6. What additional evidence should a focused hospital review request?
7. What is the difference between a benchmark comparison and a pairwise hospital comparison?
8. What information is needed before drawing funnel or control limits?

## Rubric

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Source and measure integrity | 15 | Correct release, measure, dates, geography, hashes, and provenance. |
| Missingness and footnotes | 15 | All rows reconcile and no unavailable result becomes zero. |
| Interval display | 20 | Accurate point, endpoints, benchmark, status, and labels. |
| Rank critique | 15 | Explains why ordering exceeds evidence of separation. |
| Statistical interpretation | 15 | Keeps benchmark, descriptive overlap, and pairwise testing distinct. |
| Decision consequence | 10 | Gives a bounded action and names evidence needed next. |
| Accessibility | 5 | Redundant encoding, readable type, exact values, and useful alt text. |
| Reproducibility and AI record | 5 | Clean run, editable source, provenance, and checked AI use. |
| Total | 100 | 80 required to pass. |

## Automatic failure until corrected

- a suppressed value is zero-filled;
- the final figure omits intervals;
- the top ten are called statistically worse;
- visual overlap is called a pairwise test;
- the national comparator is missing;
- a patient-level or causal quality claim is made;
- analysis cannot be reproduced;
- provenance is incomplete.

## Week-3 checkpoint contribution

Copy the final uncertainty figure to:

```text
checkpoint-1/figures/uncertainty.png
```

Add the editable analysis and source record to their checkpoint folders. Update `selection-matrix.md`, `critique-and-repair.md`, `accessibility-check.md`, and `decision-brief.md` so the dossier contains one coherent decision argument rather than six disconnected module submissions.
