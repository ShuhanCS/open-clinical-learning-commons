# Reviewer record

| Required role | Reviewer | Independence | Date | Evidence reviewed | Decision | Acknowledgment |
|---|---|---|---|---|---|---|
| FND-1 faculty owner | Unassigned before alpha under C01 | Not yet assessed | 2026-08-30 | Technical reference fixture | Pass with condition | C01 recorded |
| Health-system analytics engineering lead | Unassigned before alpha under C01 | Must be independent of learner | 2026-08-30 | Score, gates, defense, and disposition | Pass with condition | C01 recorded |
| SQL and data engineering | Unassigned before alpha under C01 | Not yet assessed | 2026-08-30 | Source, SQL, manifest, and reproduction | Pass with condition | C01 recorded |
| Clinical informatics | Unassigned before alpha under C01 | Not yet assessed | 2026-08-30 | Grain, time, quality, denominators, and claims | Pass with condition | C01 recorded |
| Accessibility | Unassigned before alpha under C01 | Not yet assessed | 2026-08-30 | Figure routes and defense access | Pass with condition | C01 recorded |
| Privacy and data governance | Unassigned before alpha under C01 | Not yet assessed | 2026-08-30 | Rights, exclusions, prompt boundary, and permitted use | Pass with condition | C01 recorded |
| Responsible AI | Unassigned before alpha under C01 | Not yet assessed | 2026-08-30 | Disclosure, audit, evidence, and ownership | Pass with condition | C01 recorded |
| Independent reproducer | Unassigned before alpha under C01 | Cannot be learner or final decision owner | 2026-08-30 | Clean assembly and exact comparisons | Pass with condition | C01 recorded |

The automated reference is a complete technical fixture, not a substitute for named human approval. The learner is not the final decision owner or independent reproducer.

## Conditions

| Condition ID | Owner | Due point | Evidence required | Verifier | Closure status | Escalation trigger |
|---|---|---|---|---|---|---|
| C01 | FND-1 faculty owner | Before alpha promotion | Named decisions for all eight required roles and a recorded learner defense | Health-system analytics engineering lead | Open | Any required reviewer rejects evidence or the defense is inadequate |
| C02 | Independent reproduction owner | Before stable promotion | Named macOS and Linux clean reproduction with exact comparisons | FND-1 faculty owner | Open | A platform needs an undeclared dependency or changes an accepted output |
| C03 | Release author | At learner acceptance | Final 100-file commit and annotated `fnd1-toolkit-v0.1.0` tag identify the same state | Health-system analytics engineering lead | Open | The tag is missing, lightweight, early, or points to another commit |
