# Assessment: Distributions versus summaries

Module version: `0.2.0`

## Directions

Answer in plain language. When a prompt asks for a chart, submit the R script, the exported chart, one or two sentences of alt text, and the requested interpretation. A chart is not complete until you explain what decision it supports.

Use synthetic data only. Generate an assessment variant from this module folder with:

```powershell
Rscript generate_ed_los.R trivial 730 outputs/assessment-trivial.csv
Rscript generate_ed_los.R null 730 outputs/assessment-null.csv
```

## Recognition

### A1. Same mean, different systems

Competency: C4.1 Diagnose

Give two different situations that could produce an unchanged annual mean. Only one situation should represent a system that is genuinely unchanged. State what additional view would distinguish them.

### A2. Limits of a box plot

Competency: C4.1 Diagnose

Which feature can a standard box plot fail to reveal: median, skew, multiple modes, or outliers? Explain your choice.

### A3. What a bar of means omits

Competency: C4.1 Diagnose

Name three facts that a bar of mean cost by service line does not provide. For each fact, say why it could matter to an operational decision.

## Application

### A4. A detectable but small change

Competencies: C4.2 Select and justify; C4.3 Connect to consequence

Use the `trivial` variant. Choose a display and a summary that accurately communicate the change from January to December. Justify them against one reasonable alternative, then state whether the result supports an operational change.

### A5. Four thousand encounters

Competency: C4.2 Select and justify

You have 4,000 encounters across six service lines. Choose a display that lets a director compare typical values, spread, and unusual values without plotting an unreadable mass of points. Explain how your design avoids overplotting and how it communicates group size.

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

Use the `null` variant. A director expects deterioration and asks you to find evidence for it. Report what the data show without manufacturing an effect. Recommend a next step.

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
| Connects the evidence to a defensible operational decision | 30 |
| Produces reproducible, readable, and accessible work | 10 |
| **Total** | **100** |

A passing submission needs at least 70 points and at least 18 of the 30 decision points.
