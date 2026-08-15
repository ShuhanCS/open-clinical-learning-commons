# ED length-of-stay synthetic data specification

## Purpose

This dataset teaches one question: when does a correct summary hide a change that matters for a healthcare decision?

The reference case combines two synthetic emergency department processes. Discharged encounters improve after a fast-track pathway. Admitted encounters develop a longer-stay group as boarding becomes more common. The pooled mean changes little, while the upper tail gets much worse.

Every row is synthetic. The generator was designed from Ali Goff's teaching requirements and was not fitted to, sampled from, or derived from a hospital or patient dataset.

## Generate and validate

From this module directory:

```powershell
Rscript generate_ed_los.R real 730 data/ed_los_2026.csv
Rscript validate_ed_los.R data/ed_los_2026.csv real
```

The generator accepts `real`, `null`, or `trivial` as its first argument. The seed and output path are the second and third arguments. Omitting all arguments generates the committed reference dataset.

## Schema

| Column | Type | Rule |
|---|---|---|
| `encounter_id` | character | Unique synthetic identifier in the form `ED26-00001`. |
| `arrival_date` | date | Date from 2026-01-01 through 2026-12-31. |
| `esi` | integer | Emergency Severity Index level 1 through 5. |
| `age_group` | character | `18-39`, `40-64`, `65-79`, or `80+`. |
| `disposition` | character | `admitted` or `discharged`. |
| `boarded` | integer | 0 or 1. Boarded encounters are always admitted. |
| `los_min` | integer | Positive arrival-to-departure length of stay in minutes. |

The reference release contains 8,392 encounters: 6,462 discharged and 1,930 admitted. ESI 1 contains 66 encounters so learners must confront a small denominator.

## Generation assumptions

The generator uses documented log-normal pathway distributions because emergency department length of stay is positive and right-skewed.

| Pathway | Reference median | Log-scale spread |
|---|---:|---:|
| Discharged | Falls from 164 minutes in January to 102 in December for the `real` variant | 0.35 |
| Admitted, not boarded | 252 minutes | 0.18 |
| Admitted, boarded | 782 minutes | 0.23 |

For the `real` variant, boarding rises from about 10 percent to about 46 percent of admitted encounters. The generator creates each pathway from evenly spaced quantiles and then shuffles the values. This makes the file reproducible and keeps the intended distribution stable across seeds.

These are pedagogical assumptions. They do not estimate performance at any hospital.

## Variant contract

| Variant | Learner task | Expected pattern |
|---|---|---|
| `real` | Find the consequential process hidden by the pooled summary. | Stable mean, improving discharged pathway, worsening upper tail, and growing boarding. |
| `null` | Report that the expected deterioration is absent. | January and December summaries remain within the validation limits. |
| `trivial` | Separate statistical detection from operational importance. | The distribution shifts enough for a small p-value but remains inside the stated operational limits. |

The variant label is not stored in a generated CSV. Instructors should record the seed and variant separately.

## Release checks

The validator checks the schema, row counts, allowed values, positive whole-minute length of stay, and the relevant variant contract. The `real` variant must also pass the six teaching checks:

1. overall mean divided by median is at least 1.20;
2. the larger disposition group is at least 2.5 times the smaller group;
3. boarding produces a second admitted process with a median at least 300 minutes longer than non-boarded admissions;
4. the pooled mean changes by less than 6 percent while the 90th percentile rises by more than 40 percent;
5. at least one meaningful subgroup contains fewer than 100 encounters;
6. the unweighted average of disposition means differs from the pooled mean by at least 30 minutes.

A reviewer must also confirm from the density charts that the admitted distribution has a visible second mode and that pooling makes it much less prominent.

## Known limits

- The file models teaching conditions, not a specific emergency department.
- Acuity and age group are assigned independently of disposition and length of stay in this first release.
- Missingness, return visits, diagnoses, timestamps within the visit, staffing, and hospital capacity are outside this module.
- Do not use the data for clinical, operational, or policy estimates.
