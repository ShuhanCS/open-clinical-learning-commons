# Data specification

## Upstream evidence

The workspace contains the complete 263-file Checkpoint 01 reference release. Its 245-row candidate manifest has SHA-256 `4e78d2313ce324fd372e6fc187afee333b27ed0cc0270c6ab8c08354dd5c3151`. The nested Module 01, Module 02, and Module 03 immutable manifests contain 29, 73, and 102 rows. Module 04 does not edit or recompute that evidence.

The workflow builder reads only accepted package files:

- the complete Synthea Patient, Observation, and Condition files from Module 02;
- the Module 02 synthetic-release record;
- the Module 03 fixed coefficients, temporal-holdout performance, and threshold audit; and
- the Checkpoint 01 contract and release.

Every source is checked by bytes and SHA-256 before calculation.

## Generated workflow evidence

| File | Grain | Role |
|---|---|---|
| `data/workflow/patient-frame.csv.gz` | one synthetic person | candidate-frame, language, access, and offline-score inputs |
| `data/workflow/encounter-opportunities.csv.gz` | one scripted encounter opportunity | session, timing, input state, competing work, and interaction script |
| `data/workflow/candidate-events.csv.gz` | one encounter-threshold comparison | rule result, repeat-card state, scripted interaction, and claim boundary |
| `outputs/workflow-profile.csv` | one release measure | core row and design counts |
| `outputs/candidate-burden.csv` | one unaccepted threshold | cards, sessions, repeats, unavailable inputs, interactions, and task minutes |
| `outputs/design-comparison.csv` | one candidate design | banner, passive panel, or no-alert comparison with separate NHANES consequences |
| `outputs/session-burden.csv.gz` | one threshold-session | card concentration, competing alerts, repeats, and scripted task time |
| `outputs/equity-slices.csv` | one threshold-dimension-group | ready inputs, candidate cards, support rule, and suppression |
| `outputs/invariant-checks.csv` | one build invariant | release integrity result |
| `build-report.json` | one release | source identities, output identities, counts, and authority boundary |

## Synthetic workflow rules

The release contains 1,000 synthetic people, 1,200 encounter opportunities, 200 repeat opportunities, 120 sessions, and 12 fictional clinicians. Every session contains 10 opportunities. Input states are scripted as ready, missing, stale, or inconsistent. The builder never imputes or scores an unavailable encounter input.

Offline teaching scores use the fixed Module 03 coefficients without refitting. The six evidence candidates remain unselected and unaccepted. The `0.20` mechanics fixture is checked in the source audit and excluded from candidate-event data.

Interaction states and task minutes are deterministic scripts. They are not measurements of clinician behavior. Language values come from the synthetic Patient release. Disability access needs are a Commons teaching overlay, not diagnoses. Equity rates require at least 30 ready encounters and 10 candidate cards; unsupported rates remain blank.

## Claim boundary

No generated row is a real patient, clinical encounter, alert, user observation, burden estimate, staffing estimate, behavior measure, prevalence estimate, fairness result, utility estimate, safety result, or implementation record.
