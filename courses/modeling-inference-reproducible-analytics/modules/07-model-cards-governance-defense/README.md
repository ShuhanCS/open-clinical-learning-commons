# FND-2 Module 07: Model cards, governance, and defense

Module 07 assembles accepted Checkpoint 2 evidence into the governed final candidate. It adds a model card, accessible performance appendix, subgroup limits, simulated monitoring contract, drift and retraining rules, rollback and stop rules, clean reproduction audit, technical handoff, defense, and separate package and model-use decisions.

## Build the reference

```powershell
python assemble_candidate.py assembled/reference --reference
python assembled/reference/validate_candidate.py assembled/reference
```

## Build a learner starter

```powershell
python assemble_candidate.py assembled/starter --checkpoint2 <accepted-checkpoint2-directory>
python assembled/starter/validate_candidate.py assembled/starter --starter
```

Complete all 24 records, then validate without `--starter`. The proposed tag is `fnd2-governed-candidate-v0.1.0`; do not create it until the final checkpoint identifies the exact accepted commit.

The reference package disposition is `accept with conditions`. Its model-use recommendation is separately `teaching use only`.
