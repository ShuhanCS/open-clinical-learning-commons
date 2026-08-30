# APP-1 Module 05 learner workspace

Build the eleven outputs from the accepted source, then complete every record without changing an immutable file.

```powershell
python build_variation.py --database <accepted-synthea-sqlite> --cohort <analysis-cohort.csv> --expected <expected-outcomes.csv> --target outputs
python validate_variation.py . --submission
```

Replace every `REPLACE` prompt. Preserve exact numerators, denominators, time windows, source meaning, support decisions, and claim limits.
