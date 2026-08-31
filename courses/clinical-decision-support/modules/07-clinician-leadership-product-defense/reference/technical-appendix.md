# Technical appendix

## Checkpoint identity

| Checkpoint | Files | Candidate rows | Candidate manifest bytes | Candidate manifest SHA-256 | Points |
|---|---:|---:|---:|---|---:|
| `oclc-app4-cp01@0.1.0` | 263 | 245 | 45,897 | `4e78d2313ce324fd372e6fc187afee333b27ed0cc0270c6ab8c08354dd5c3151` | 40 |
| `oclc-app4-cp02@0.1.0` | 1,047 | 1,030 | 236,732 | `14ac12dd890045dce21cdc44a9b614770b8b2428bd71a1d4f5eb9cc9de63d642` | 25 |

## Model partitions

| Partition | Rows | Outcomes | Weight | Role |
|---|---:|---:|---|---|
| Development | 3,652 | 156 | `WTMEC2YR / 2` | fit transparent and fixed challenger models |
| Temporal holdout | 1,806 | 97 | `WTMEC2YR` | untouched temporal evaluation |
| Transport stress | 2,086 | 75 | `WTPH2YR` | separate later-cycle stress test |

## Transparent model performance

| Partition | Prevalence | Mean probability | Brier | ROC AUC | Calibration intercept | Calibration slope |
|---|---:|---:|---:|---:|---:|---:|
| Temporal holdout | 0.02904272 | 0.03015261 | 0.02811126 | 0.68783144 | -0.03946013 | 0.88441129 |
| Transport stress | 0.03274014 | 0.03041245 | 0.03175435 | 0.68422573 | 0.07788522 | 0.81620710 |

## Challenger decision

| Item | Exact value |
|---|---:|
| Common rows | 7,544 |
| Predictors | 3 |
| Replacement rules | 11 |
| Passing rules | 8 |
| Failed rules | R03, R04, R08 |
| Temporal-holdout AUC difference | -0.00743486 |
| Transport-stress AUC difference | -0.01928938 |
| Worst supported subgroup AUC degradation | 0.10385240 |
| Decision | retain transparent model |

## Prototype and safety

| Item | Exact value |
|---|---:|
| Sandbox cases | 31 |
| Prefetch resources | 184 |
| Trace events | 61 |
| Inherited failures | 17 |
| Silent failures detected | 1 |
| Accessibility blockers | 1 |
| Hazards | 22 |
| Monitoring measures | 20 |
| Monitoring scenarios | 8 |
| Escalation routes | 12 |
| Automatic actions | 0 |

All probabilities, thresholds, burden counts, subgroup results, and monitoring triggers remain historical or synthetic teaching evidence. No clinical threshold is accepted.
