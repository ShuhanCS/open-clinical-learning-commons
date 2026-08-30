# Causal claim screen

## Decision

The selected Synthea cases support conditional description and prediction teaching only. The generated treatment case supports method recovery against known synthetic truth. None supports a real clinical causal claim.

## Teaching contrast

- Unit: one generated fixture person.
- Time zero: synthetic treatment assignment.
- Exposure: treatment versus no treatment.
- Outcome: 30-day symptom score; lower is better.
- Target: average treatment effect among the 600 generated people.
- Known generator effect: -6.00000000 points for every generated person.

## Screen

| Question | Finding | Action |
|---|---|---|
| Is time zero defined before the outcome? | Yes in the generated case | continue |
| Are adjustment variables pre-treatment? | Age, severity, comorbidity, and site are pre-treatment | eligible for teaching adjustment |
| Is early response pre-treatment? | No, it is a mediator | exclude from total-effect adjustment |
| Is clinical preference measured? | No | keep unmeasured-confounding boundary visible |
| Is complete severity a neutral filter? | No, record completeness depends on age and site | inspect selection; do not call complete cases representative |
| Is positivity established for real care? | No; only fixture overlap is inspected | no transport claim |
| Is consistency or no interference established? | Only by the generator convention | synthetic teaching boundary |

Disposition: `continue with conditions`. The case teaches what evidence a causal analysis would need; it does not establish those conditions in clinical practice.
