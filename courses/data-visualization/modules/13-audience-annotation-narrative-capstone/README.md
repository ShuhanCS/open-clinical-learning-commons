# Module 13: Audience, annotation, narrative, and capstone

Module 13 asks what may change when one stable analysis is delivered to two audiences, and what must remain true in both versions.

## Reference decision

Authorize a local definition and current-data review for a historical public CMS OP-22 signal.

The technical version serves an emergency department quality director. The executive version serves a hospital quality committee. Both preserve the same 23-percent public OP-22 value, 2024 reporting period, 2026 CMS release, 590-day source lag, descriptive peer context, mock-trigger boundary, and validation-first action.

## Two audience versions

### Technical quality director

The technical figure shows all 53 reported Massachusetts OP-22 values, directly labels the selected 23-percent value, marks the descriptive 3-percent state median, labels the mock 10-percent review trigger as non-CMS, states the reporting period and lag, and names the validation action.

### Executive quality committee

The executive figure reduces the story to three needs:

1. the public signal;
2. the time boundary; and
3. the authorization request.

It assigns the emergency department quality director and requires current local OP-22 and emergency department time evidence at the next review.

## Invariants

These elements do not change across audiences:

- source release;
- facility;
- values and units;
- samples;
- reporting windows;
- release date and lag;
- peer counts and medians;
- threshold values and origin;
- trigger results;
- historical-use label;
- supported action; and
- unsupported conclusions.

## Public sources

- CMS dataset: https://data.cms.gov/provider-data/dataset/yv7e-xc69
- Complete pinned CSV: https://data.cms.gov/provider-data/sites/default/files/resources/0437b5494ac61507ad90f2af6b8085a7_1785189967/Timely_and_Effective_Care-Hospital.csv
- Hospital data dictionary: https://data.cms.gov/provider-data/sites/default/files/data_dictionaries/hospital/HOSPITAL_Data_Dictionary.pdf
- Current measure periods: https://data.cms.gov/provider-data/topics/hospitals/measures-and-current-data-collection-periods

Module 13 reuses the pinned Module 12 teaching release. It does not silently refresh or duplicate the data.

## Reference facts

| Item | Value |
|---|---:|
| Massachusetts facilities | 62 |
| Selected facility | Anna Jaques Hospital, CMS ID 220029 |
| Selected ED volume category | Low |
| Selected OP-18b | 188 minutes, sample 422 |
| Massachusetts OP-18b median | 211.5 minutes across 54 reported hospitals |
| Mock OP-18b trigger | 240 minutes, not crossed |
| Selected OP-22 | 23 percent, source sample 19,211 |
| Massachusetts OP-22 median | 3 percent across 53 reported hospitals |
| Mock OP-22 trigger | 10 percent, crossed |
| OP-18b source lag | 317 days |
| OP-22 source lag | 590 days |

The medians are descriptive references. The triggers are course assumptions. Neither is a CMS benchmark or target.

## Learning outcomes

By the end of the module, learners can:

1. define two audiences and their authority;
2. separate finding, interpretation, recommendation, and action;
3. write a finding-led title without implying cause;
4. choose one primary figure and no more than one necessary supporting figure;
5. use annotation to expose values, boundaries, and actions;
6. preserve evidence invariants across audience versions;
7. move detail to a table or note without hiding it;
8. produce an accessible exact-value path;
9. document transformations and audience adaptations;
10. reproduce the final package from a clean checkout;
11. document and verify AI assistance; and
12. defend the source, limit, and action without expanding the claim.

## Files

| File | Purpose |
|---|---|
| `validate_decision_story_case.py` | Sixty-six checks of the reused Module 12 sources, selected facts, definitions, and invariants. |
| `lab.R` | Two audience figures, exact table, accessible alternative, adaptation record, and decision brief. |
| `critique_charts.R` | Three deliberately flawed narrative examples. |
| `assessment.md` | Exact learner capstone package, rubric, pass gates, and defense contract. |
| `instructor-notes.md` | Sixteen-and-a-half-hour plan, answer key, critique key, and defense questions. |
| `data-spec.md` | Upstream lineage, stable facts, invariant rules, output fields, and interpretation limits. |
| `source-record.yml` | Full URLs, upstream checksums, rights, and reuse boundary. |
| `release.json` | Machine-readable release, validation, review, and known-limit record. |

## Validate the evidence

From the repository root:

```powershell
python courses/data-visualization/modules/13-audience-annotation-narrative-capstone/validate_decision_story_case.py
```

Expected result:

```text
Module 13 decision story data passed 66 checks.
```

## Run the reference lab

R and ggplot2 are required.

```powershell
Rscript courses/data-visualization/modules/13-audience-annotation-narrative-capstone/lab.R --output "$env:TEMP\oclc-da730-m13-lab"
```

The lab writes:

- `01-technical-decision-story.png`;
- `02-executive-decision-story.png`;
- `decision-story-table.csv`;
- `alt-text-reference.md`;
- `audience-adaptation-reference.md`; and
- `decision-brief-reference.md`.

## Run the critique lab

```powershell
Rscript courses/data-visualization/modules/13-audience-annotation-narrative-capstone/critique_charts.R --output "$env:TEMP\oclc-da730-m13-critiques"
```

The critique lab writes:

- `C1-overstated-causality.png`;
- `C2-hidden-freshness.png`; and
- `C3-annotation-misdirection.png`.

## Learner package

```text
module-13/
  README.md
  decision-brief.md
  figure-primary.png
  figure-supporting.png
  accessible-table.csv
  alt-text.md
  analysis.R
  source-record.yml
  transformation-record.md
  audience-adaptation-record.md
  reproducibility-check.md
  critique-response.md
  ai-use.md
  defense/
    slides.pdf
    questions-and-responses.md
```

An approved alternative tool may replace `analysis.R` with another editable source. The evidence, accessibility, provenance, and defense standards do not change.

## Interpretation boundary

The reference story supports authorization of a local definition and current-data review. It does not support current performance rating, causal attribution, staffing change, care change, or an intervention-effect claim.

## Handoff

The final checkpoint packages the learner's approved Module 13 release on the official last day of the half-term. The finished evidence chain can then travel into the foundation, applied, and capstone courses with its source, definitions, limitations, accessibility, and action boundary intact.
