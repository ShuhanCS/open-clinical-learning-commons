# FND-2 Final checkpoint: Governed analytics package

This checkpoint freezes the complete Module 07 governed candidate and records two separate decisions: whether the package is acceptable and what use the fitted model may support.

The reference package preserves 168 candidate files in a final candidate manifest, adds exact Checkpoint 2 and Module 07 release identities, the 35-point score, 27 gates, 15-question defense, reviewer and reproduction records, audit, conditions, final decision, and release acceptance. It contains 182 files in total.

## Assemble the reference package

```powershell
python assemble_final.py --reference --target <new-target-folder>
python validate_final.py <new-target-folder>
```

## Assemble learner work

```powershell
python assemble_final.py --candidate <module-07-candidate-folder> --target <new-target-folder>
python validate_final.py <new-target-folder> --starter
```

Complete the records under `final-review/`, then run validation without `--starter`.

The assembler refuses an existing target and never refits the model. The proposed tag remains uncreated until named human acceptance of the exact reviewed commit.

## Decisions

- Package disposition: `accept`, `accept with conditions`, `revise`, or `refer`.
- Model-use recommendation: a separate controlled value.
- Reference result: `accept with conditions` and `teaching use only`.

An accepted package is not deployment permission.

## Durable specification

`docs/curriculum/courses/FND-2/checkpoints/03-governed-analytics-package-spec.md`
