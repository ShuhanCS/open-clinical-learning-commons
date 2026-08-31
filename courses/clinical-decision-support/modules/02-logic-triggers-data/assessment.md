# APP-4 Module 02 assessment

## Decision

Is the candidate logic, trigger, input, terminology, trace, and synthetic-test contract complete enough to hand to Module 03 for historical evidence and threshold analysis?

## Course-point role

Module 02 awards 20 course points as the first half of the 40-point Week 3 checkpoint. Module 03 awards the remaining 20 points. Module 01 is a required zero-point gate whose accepted boundaries are inherited here.

## Scoring

| Criterion | Points |
| --- | ---: |
| Use-case and logic release preserves the Module 01 decision and names the permitted next action | 3 |
| Ordered logic, hook, trigger, suppression, nonaction, and branch reasons are complete | 5 |
| Event-time input, terminology, unit, value-state, staleness, and failure contract is complete | 4 |
| Synthetic-source provenance, encoding normalization, duplicates, limits, and reproducibility are correctly interpreted | 3 |
| All 16 rule cases reproduce expected results and traces, including silent failure | 3 |
| Change control, consequence ownership, claims, AI disclosure, and progression are defensible | 2 |
| Total | 20 |

## Required evidence

1. `use-case-logic-release.md`
2. `logic-specification.csv`
3. `input-contract.csv`
4. `trigger-suppression-matrix.csv`
5. `rule-test-results.csv`
6. `terminology-map.csv`
7. `synthetic-release-interpretation.md`
8. `logic-change-control.md`
9. `patient-workflow-consequence-map.csv`
10. `claim-boundary.csv`
11. `ai-use.md`
12. `progression-decision.md`

## Noncompensable gates

1. Every inherited Module 01 source and authority file matches its accepted hash.
2. All 25 synthetic FHIR files match the release manifest and have zero parse failures.
3. The upstream Windows-1252 to committed UTF-8 normalization is disclosed.
4. All 11,109 duplicate resource IDs are preserved, measured, and bounded rather than silently removed.
5. `CGH-GIM-01` and all clinical and workflow rows remain explicitly fictional and synthetic.
6. Hook, user, service, decision time, branch order, nonaction, and reason codes are testable.
7. Every candidate input has terminology, unit, value-state, event-time, staleness, and failure handling.
8. All 16 normal and failure fixtures produce expected results and ordered traces.
9. The score and `0.20` threshold are labeled mechanics-only fixtures in every relevant record.
10. No model is fit and no clinical threshold is selected or accepted.
11. AI use and independent checks are disclosed.
12. Progression permits Module 03 curriculum construction only while live use and deployment remain prohibited.

Any failed gate caps the module at `revise`, regardless of points.

## Progression decisions

- `continue`: complete technical handoff with no unresolved condition that affects Module 03 construction;
- `continue with conditions`: Module 03 construction may begin while named human reviews remain open;
- `revise`: one or more required records, traces, or boundaries need repair; or
- `refer`: the use case or logic requires clinical, interoperability, safety, privacy, or governance escalation before construction continues.

The reference decision is `continue with conditions`. This does not authorize a model, clinical threshold, patient score, clinical card, implementation, or deployment.
