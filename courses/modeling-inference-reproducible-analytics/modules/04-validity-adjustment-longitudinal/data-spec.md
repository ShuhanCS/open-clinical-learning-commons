# Data specification

## Accepted inputs

Nine fingerprinted inputs come from the accepted Week 3 checkpoint and Modules 01 through 03. The builder stops if any byte count or SHA-256 fingerprint changes. The learner copy stores them in `data/`.

The 374-row modeling cohort is public-safe Synthea teaching data. The 111-row linear subset contains only people with a recorded next encounter; the other 263 timing values are structural blanks and must never become zero.

## Deterministic fixtures

All generated cases use seed `20260830` and contain no real patient records.

| File | Unit | Rows | Purpose |
|---|---|---:|---|
| `treatment-fixture.csv` | generated person | 600 | confounding, propensity, overlap, balance, missingness, sensitivity |
| `repeated-measures-fixture.csv` | generated person-visit | 2,400 | dependence, clustered uncertainty, random intercept |
| `survival-fixture.csv` | generated person | 600 | risk sets, censoring, Kaplan-Meier, Cox quantities |

The treatment generator contains a known individual effect of -6 symptom-score points. `outcome_30d` is lower-is-better. Treatment is more likely with greater baseline severity, age, comorbidity, and site. `early_response` is post-treatment and is a mediator, not a baseline adjustment variable.

`baseline_severity_observed` is missing for 91 of 600 people. Missingness depends on observed age and site. The generator makes that mechanism known for audit, but a real observed analysis could only defend it as an assumption. The protected generator retains complete severity so the exercise can compare methods with known truth.

The repeated fixture has four visits per person at weeks 0, 4, 8, and 12. `fixture_id` defines the cluster. The survival fixture preserves each generated event or censoring time and an event indicator; censored records remain in risk sets until censoring.

## Structured outputs

Every visual has a nonvisual equivalent. `dag.svg` is paired with `dag.mmd`, `dag-nodes.csv`, `dag-edges.csv`, and `dag-narrative.md`. Model readings are CSV tables, not screenshots.

## Boundaries

- Do not join the four cases at row level.
- Do not treat synthetic identifiers as people.
- Do not infer a real treatment effect from known synthetic truth.
- Do not convert structural blanks or censoring to zero outcomes.
- Do not replace the accepted Week 3 inputs.
- Do not use the fixture for clinical care, external validation, or deployment.
