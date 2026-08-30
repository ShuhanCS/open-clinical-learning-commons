# Assessment: Distributions versus summaries

Module version: `0.4.0`

## Exact submission package

```text
module-04/
  distribution-audit.md
  analysis.R
  figures/
    distribution.png
    monthly-metrics.png
  source-record.yml
  alt-text.md
  decision-note.md
```

`distribution-audit.md` contains A1 through A8 plus the statistic, display, subgroup, tail, and failure reasoning used for A9. `analysis.R` must read the assigned file through a relative path, check required fields, reproduce both figures, and print the declared metrics. The copied source record adds the assigned variant, seed, analysis date, row counts, transformations, outputs, and checksums.

## Directions

Answer in plain language. When a prompt asks for a chart, submit the R script, the exported chart, one or two sentences of alt text, and the requested interpretation. Name the healthcare audience and the patient group or care process represented. A chart is not complete until you explain what clinical or operational decision it supports.

Use synthetic data only. Generate an assessment variant from this module folder with:

```powershell
Rscript generate_ed_los.R trivial 730 outputs/assessment-trivial.csv
Rscript generate_ed_los.R null 730 outputs/assessment-null.csv
```

## Recognition

### A1. Same department-wide mean, different patient experiences

Competency: C4.1 Diagnose

An emergency-department director sees an unchanged annual mean length of stay. Describe one situation in which patient mix and care processes are genuinely stable. Then describe a second situation in which discharged patients move faster while admitted patients wait longer for inpatient beds. State which additional visualization would distinguish the two situations and what decision it would inform.

### A2. When a box plot hides a care process

Competency: C4.1 Diagnose

Emergency-department length of stay may contain one pattern for discharged patients and another for boarded admitted patients. Which feature can a standard box plot fail to reveal: median, skew, multiple modes, or outliers? Explain why missing that feature matters to an emergency-department medical director or patient-flow team.

### A3. What mean length of stay by acuity omits

Competency: C4.1 Diagnose

An emergency-department dashboard shows one bar for mean length of stay in each Emergency Severity Index group. Name three facts the bars do not provide. For each omission, explain how it could change a staffing, fast-track, or bed-flow decision.

## Application

### A4. A detectable but small change

Competencies: C4.2 Select and justify; C4.3 Connect to consequence

Use the `trivial` emergency-department variant. Choose a display and summary that accurately communicate the January-to-December change. Justify them against one reasonable alternative, then tell the chief operating officer whether the result supports a staffing, fast-track, boarding, or monitoring change.

### A5. Four thousand encounters

Competency: C4.2 Select and justify

You have 4,000 encounters across six hospital service lines. Choose a display that lets a system operations director compare typical length of stay, variation, and unusual waits without plotting an unreadable mass of points. Explain how the display handles overplotting, communicates group size, and prevents a small service from appearing as certain as a large one.

### A6. Similar medians, different tails

Competencies: C4.1 Diagnose; C4.2 Select and justify

An empirical cumulative distribution display for two clinics gives these reference points:

| Measure | Clinic North | Clinic South |
|---|---:|---:|
| Median wait | 120 minutes | 150 minutes |
| 75th percentile | 180 minutes | 190 minutes |
| 90th percentile | 520 minutes | 250 minutes |
| Share over 8 hours | 12% | 1% |

Explain why a comparison based only on the medians is misleading. State what the empirical cumulative distribution adds and name one operational question it can answer.

## Judgment and transfer

### A7. Expected deterioration is absent

Competencies: C4.1 Diagnose; C4.3 Connect to consequence

Use the `null` emergency-department variant. A patient-flow director expects boarding deterioration and asks you to find evidence for it. Report what the synthetic data show without manufacturing an effect. Recommend a monitoring or follow-up step that does not waste clinical or operational resources on an unsupported finding.

### A8. A better median and more complaints

Competencies: C4.1 Diagnose; C4.2 Select and justify; C4.3 Connect to consequence

Explain how median door-to-clinician time could improve while complaints about long waits increase. Specify what you would add to the dashboard and what action the fuller view could trigger.

### A9. Board decision brief

Competencies: C4.1 Diagnose; C4.2 Select and justify; C4.3 Connect to consequence

Use the reference `real` dataset or another dataset assigned by the instructor.

The chief operating officer has five minutes at the board meeting. Submit:

1. one reproducible R script;
2. one chart that accurately represents performance in 2026;
3. one or two sentences of alt text;
4. a two-sentence board note stating the finding and recommended decision;
5. a short justification comparing your display with one reasonable alternative.

Your chart must name the measure and unit, use an honest scale, label relevant groups, and avoid relying on color alone.

## Module grading rubric

| Criterion | Points | Full-credit evidence |
|---|---:|---|
| Distribution audit | 25 | A1 through A8 and A9 reasoning identify the center, shape, tail, groups, hidden or absent process, and decision consequence. |
| Reproducible analysis | 20 | Relative paths, field checks, declared variant and seed, exact summaries, and both required figures. |
| Display and statistical fit | 20 | Statistic and display match the decision, reveal consequential structure, and are justified against an alternative. |
| Decision note and claim boundary | 15 | Named owner, supported action, patient or process consequence, and explicit limit. |
| Source and provenance | 10 | CMS calibration, synthetic assumptions, transformations, outputs, rights, and checksums are accurate. |
| Accessibility and alternatives | 10 | Honest scales, units, non-color cues, readable labels, and complete alt text. |
| **Total** | **100** |

A passing submission earns at least 75 points and meets all five conditions:

1. the analysis runs and writes both required figures;
2. the learner states whether the pattern is real, null, or trivial without assuming deterioration;
3. the selected statistic and display expose or honestly dismiss the decision-relevant structure;
4. the source record separates the public hospital-level anchor from synthetic encounter assumptions; and
5. the decision note does not claim a real hospital effect, patient harm, or causal intervention result.

## AI policy

AI may help debug code, compare display candidates, or edit prose. It may not invent observations, source values, patient-level provenance, or an operational effect. The learner records tool, purpose, adopted change, and verification in the decision note.
