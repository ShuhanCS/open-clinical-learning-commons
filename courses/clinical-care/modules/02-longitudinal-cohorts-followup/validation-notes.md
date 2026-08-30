# Validation notes

## Cohort and timing

- Source people: 1,171.
- Source encounters: 53,346.
- Initial cohort: 518 unique people.
- Index class: 451 emergency and 67 inpatient.
- Index deaths: 9.
- Early post-discharge deaths: 8.
- Early acute-return people: 25 from 27 retained event rows.
- Branch overlaps: 0.
- Landmark eligible: 476.
- Scheduled follow-up: 129 exposed and 347 unexposed.
- Later acute returns: 87 with a 25/62 exposure split.
- Later deaths recognized: 3. Each follows the first later acute return in this release.
- Censoring: 87 event and 389 administrative-end dispositions. No later death precedes the primary event.
- Observed time among eligible people ranges from 1.00000000 to 335.00000000 days after landmark.

## Event audit

| Role | Rows | Selected first events | People |
|---|---:|---:|---:|
| index encounter | 518 | 518 | 518 |
| index death | 9 | 9 | 9 |
| early death | 8 | 8 | 8 |
| scheduled follow-up | 212 | 138 | 138 |
| early acute return | 27 | 25 | 25 |
| later acute return | 241 | 99 | 99 |
| later death | 3 | 3 | 3 |
| Total | 1,018 | 800 |  |

The selected scheduled and later-event counts include people outside the landmark risk set. The analysis cohort correctly limits them to 129 exposed people and 87 later events among 476 eligible people.

## Six-site support

| Site | People | Exposed | Unexposed | Events | Low | Medium | High | Raw event percent |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SITE-A | 76 | 19 | 57 | 21 | 39 | 22 | 15 | 27.63157895 |
| SITE-B | 75 | 19 | 56 | 10 | 35 | 22 | 18 | 13.33333333 |
| SITE-C | 68 | 19 | 49 | 10 | 21 | 26 | 21 | 14.70588235 |
| SITE-D | 88 | 21 | 67 | 13 | 26 | 32 | 30 | 14.77272727 |
| SITE-E | 87 | 20 | 67 | 18 | 25 | 36 | 26 | 20.68965517 |
| SITE-F | 82 | 31 | 51 | 15 | 13 | 21 | 48 | 18.29268293 |

All six sites have both exposure groups, at least ten later events, and all three risk tiers. Raw percentages are descriptive teaching values. The known direct site effect is zero because assignment changes no source exposure or outcome.

## Disposition

The reference passes the technical gates and may continue to Module 03 with conditions. Named clinical, methods, patient or community, accessibility, governance, responsible-AI, and independent reproduction reviews remain pending before alpha.
