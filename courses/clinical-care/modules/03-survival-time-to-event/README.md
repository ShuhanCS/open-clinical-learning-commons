# APP-1 Module 03: Survival and time-to-event outcomes

This module follows the accepted 476-person day-30 landmark cohort through the first later acute return. It releases count-first Kaplan-Meier evidence, fixed-time comparisons, a log-rank test, an unadjusted Cox model, a proportional-hazards screen, an accessible curve, and a person-level later-death audit.

## Reference result

- 129 people have recorded scheduled follow-up and 347 do not.
- The cohort contains 87 events and 389 administrative censors.
- The two-sided log-rank chi-square is 0.17859356 with p = 0.67258471.
- The unadjusted scheduled-follow-up hazard ratio is 1.10542457 with a 95 percent interval from 0.69479700 to 1.75873453.
- The event-level Schoenfeld residual time screen has p = 0.00636020 and fails the prespecified 0.05 threshold.
- Three later deaths occur after a first later acute return. No death censors a person before the event.

The failed screen means the single Cox hazard ratio is not the main result. Use the Kaplan-Meier risk table and prespecified fixed-time differences. Nothing in this synthetic observational comparison establishes benefit, harm, equivalence, or causation.

## Build

```powershell
python build_survival.py --self-check
python build_survival.py --cohort ../02-longitudinal-cohorts-followup/outputs/analysis-cohort.csv --target <new-output-directory>
python build_workspace.py --target <new-learner-workspace>
python build_workspace.py --target <new-reference-workspace> --reference
python validate_survival.py .
```

Run the supplied R reading route only in a named environment with the `survival` package:

```powershell
Rscript paired-survival.R ../02-longitudinal-cohorts-followup/outputs/analysis-cohort.csv
```

R execution is not required to reproduce the Python reference on this machine. Record its actual status; do not claim an unrun result.
