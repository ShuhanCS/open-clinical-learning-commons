# ED length-of-stay synthetic data specification

## Purpose

This dataset teaches one question: when does a correct summary hide a change that matters for a healthcare decision?

The reference case combines two synthetic emergency department processes. Discharged encounters improve after a fast-track pathway. Admitted encounters develop a longer-stay group as boarding becomes more common. The pooled mean changes little, while the upper tail gets much worse.

Every encounter row is synthetic. The generator anchors the center of its discharged pathway to the median of all reported hospital OP_18b values in the CMS Timely and Effective Care release dated 2026-08-13. It is not fitted to, sampled from, or derived from patient records. All patient-level shapes, monthly trends, dispositions, boarding patterns, acuity values, and age groups remain teaching assumptions.

## Generate and validate

From this module directory:

```powershell
Rscript build_cms_ed_calibration.R data/cms_ed_op18b_2026.csv
Rscript generate_ed_los.R real 730 data/ed_los_2026.csv
Rscript validate_ed_los.R data/ed_los_2026.csv real
```

The calibration builder downloads the pinned 34,150,899-byte CMS national file and retains every OP_18b hospital row. The generator accepts `real`, `null`, or `trivial` as its first argument. The seed, output path, and optional calibration path are the next arguments. Omitting all arguments generates the committed reference dataset from the committed calibration extract.

## Public calibration release

| Field | Contract |
|---|---|
| Publisher | Centers for Medicare & Medicaid Services |
| Dataset | Timely and Effective Care - Hospital |
| Dataset ID | `yv7e-xc69` |
| Measure | `OP_18b` |
| Release | 2026-08-13 |
| Coverage | 2024-10-01 through 2025-09-30 |
| Extract | `data/cms_ed_op18b_2026.csv` |
| Hospital rows | 4,658 |
| Reported | 4,081 |
| Unavailable | 577 |
| Reported median | 148 minutes |
| Reported range | 42 to 413 minutes |
| Extract SHA-256 | `c9603109d4ea251b8096a655c27ad42cd6313bdb1309999bee3eb37ce79ec67d` |

The extract preserves every national OP_18b row, including unavailable results and footnotes. CMS reports hospital-level medians. The 148-minute value anchors a plausible time scale. It does not define a patient-level distribution and is not a target or benchmark for the synthetic hospital.

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
| Discharged | Falls from 179 minutes in January to 117 in December for the `real` variant, centered on the 148-minute CMS anchor | 0.35 |
| Admitted, not boarded | 252 minutes | 0.18 |
| Admitted, boarded | 782 minutes | 0.23 |

For the `real` variant, boarding rises from about 10 percent to about 46 percent of admitted encounters. The generator creates each pathway from evenly spaced quantiles and then shuffles the values. This makes the file reproducible and keeps the intended distribution stable across seeds.

The monthly change and every admitted or boarding parameter are pedagogical assumptions. They do not estimate performance at any hospital.

## Variant contract

| Variant | Learner task | Expected pattern |
|---|---|---|
| `real` | Find the consequential process hidden by the pooled summary. | Stable mean, improving discharged pathway, worsening upper tail, and growing boarding. |
| `null` | Report that the expected deterioration is absent. | January and December summaries remain within the validation limits. |
| `trivial` | Separate statistical detection from operational importance. | The distribution shifts enough for a small p-value but remains inside the stated operational limits. |

The variant label is not stored in a generated CSV. Instructors should record the seed and variant separately.

## Release checks

The validator first checks the 4,658-row CMS calibration contract, including 4,081 reported values, 577 unavailable values, the 148-minute median, release, period, and source URL. It then checks the synthetic schema, row counts, allowed values, positive whole-minute length of stay, and the relevant variant contract. The `real` variant must also pass the six teaching checks:

1. overall mean divided by median is at least 1.20;
2. the larger disposition group is at least 2.5 times the smaller group;
3. boarding produces a second admitted process with a median at least 300 minutes longer than non-boarded admissions;
4. the pooled mean changes by less than 6 percent while the 90th percentile rises by more than 40 percent;
5. at least one meaningful subgroup contains fewer than 100 encounters;
6. the unweighted average of disposition means differs from the pooled mean by at least 30 minutes.

A reviewer must also confirm from the density charts that the admitted distribution has a visible second mode and that pooling makes it much less prominent.

## Known limits

- The file models teaching conditions, not a specific emergency department.
- CMS OP_18b is a hospital-level median and does not supply a patient-level distribution.
- Only the discharged median center is calibrated to the public source.
- Acuity and age group are assigned independently of disposition and length of stay in this first release.
- Missingness, return visits, diagnoses, timestamps within the visit, staffing, and hospital capacity are outside this module.
- Do not use the data for clinical, operational, or policy estimates.
