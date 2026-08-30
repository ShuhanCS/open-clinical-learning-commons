# FND-2 Checkpoint 2 release

This package assembles the accepted Week 6 validity, forecast, testing, and agent-accountability evidence into one immutable release. It is due at the end of instructional Week 6 after 96.5 cumulative course hours and carries 25 course points.

## Build a reference

```powershell
python assemble_checkpoint.py assembled/reference --reference
python assembled/reference/validate_checkpoint.py assembled/reference
```

## Build a learner starter

```powershell
python assemble_checkpoint.py assembled/starter --checkpoint1 <accepted-checkpoint1-root> --module04 <accepted-module04-root> --module05 <accepted-module05-root> --module06 <accepted-module06-root> --public-data <public-data-root>
python assembled/starter/validate_checkpoint.py assembled/starter --starter
```

The public-data root must contain `nhsn_hospital_capacity_jurisdiction_2024_2026.csv` and `ma_hospital_capacity_time_2024_2026.csv` with the fixed release fingerprints.

## Accept

Complete the 12 editable records, earn at least 20.00 points, pass all 25 gates, complete an adequate defense and human sign-off, then run the validator without `--starter`. Only `accept` or `accept with conditions` permits Module 07.

The evidence supports instruction only. It authorizes no clinical, causal, staffing, capacity, operational, fairness, safety, or deployment use.
