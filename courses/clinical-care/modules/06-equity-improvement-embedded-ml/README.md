# APP-1 Module 06: Equity, feasible improvement, and embedded machine learning

## Decision

Decide whether the accepted clinical-care evidence justifies a bounded prospective pathway test and whether one random-forest extension changes that decision compared with the transparent benchmark.

## Reference conclusion

Continue to clinical leadership review with conditions. The source retains an equity question because it does not observe offer, preference, access, completion, barriers, or burden. A capacity-aware scheduling workflow is feasible enough to review prospectively. The bounded random forest does not improve the overall held-out evidence and does not change the decision. Clinical implementation and model deployment are prohibited.

## Run

```powershell
python build_equity_improvement.py --self-check
python validate_equity_improvement.py .
python build_workspace.py --self-check
```

The builder reads the accepted Module 02 cohort, Module 04 expected outcomes, and Module 05 care-pattern output. It creates 15 deterministic outputs. `pathway-figure.svg` has exact CSV alternatives and a structured explanation in `pathway-display.md`.

## Learner release

Use `python build_workspace.py --target <new-folder>` for a starter or add `--reference` for the completed teaching package. The builder refuses to overwrite an existing target.

The 24 Module 06 requirements are gates, not extra grade points. The cumulative Week 6 package carries 25 points from Module 04 and 20 points from Module 05 exactly once.
