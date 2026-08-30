# FND-2 Module 04: Validity, adjustment, and longitudinal structure

This 16.5-hour module asks one practical question: which model claims survive checks of timing, causal structure, missingness, selection, repeated observations, and censoring?

The release combines four bounded teaching cases:

- the accepted 374-person public Synthea cohort and its 111-person recorded-next-encounter subset;
- a deterministic 600-person treatment fixture with known potential outcomes;
- 2,400 repeated observations from 600 generated people; and
- a 600-person time-to-event fixture with 449 events and 151 censored records.

The synthetic fixtures teach method behavior. They do not estimate a real treatment effect, clinical longitudinal effect, or clinical survival effect.

## Start here

1. Read `source-record.yml`, `data-spec.md`, and `assessment.md`.
2. Inspect `outputs/analytic-aim-validity-map.csv`, then answer `causal-claim-screen.md`.
3. Reconcile `dag.mmd`, `outputs/dag-nodes.csv`, and `outputs/dag-edges.csv`.
4. Compare overlap, balance, adjustment, selection, and missingness evidence.
5. Read the repeated-measures and survival results without changing their quantities.
6. Complete the memo, specialist referrals, and progression decision.
7. Rebuild into a new directory and validate the completed submission.

```text
python build_validity_evidence.py reproduced-outputs --outputs-only
python validate_validity_evidence.py . --mode submission
```

The validator never grades clinical judgment by keyword alone. It verifies the release contract and rejects unfinished decision records; an accountable reviewer owns the score and progression decision.

## Reference result

The reference disposition is `continue with conditions`. Module 05 may begin, while every causal, selection, missingness, repeated-measures, censoring, and synthetic-transport condition remains visible.

Repository: https://github.com/ShuhanCS/open-clinical-learning-commons
