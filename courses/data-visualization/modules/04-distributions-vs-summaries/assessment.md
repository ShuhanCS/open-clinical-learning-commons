# Assessment: Distributions versus summaries

Module version: `0.3.1`

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

## A9 grading rubric

| Criterion | Points |
|---|---:|
| Diagnoses the hidden or absent distributional pattern | 25 |
| Selects an appropriate statistic and display | 20 |
| Justifies the choice against a reasonable alternative | 15 |
| Connects the evidence to a defensible healthcare decision | 30 |
| Produces reproducible, readable, and accessible work | 10 |
| **Total** | **100** |

A passing submission needs at least 70 points and at least 18 of the 30 decision points.
