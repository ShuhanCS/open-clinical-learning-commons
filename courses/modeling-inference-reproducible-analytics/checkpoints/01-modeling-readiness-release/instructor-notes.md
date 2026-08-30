# Instructor notes

## Review sequence

1. Verify manifest and module identities.
2. Check the four Module 01 criteria.
3. Check the two Module 02 criteria.
4. Check the three Module 03 criteria.
5. Review cumulative interpretation and H01.
6. Check all 23 gates.
7. conduct the 12-question defense.
8. reconcile score, defense, gates, and disposition.
9. record Module 04 conditions.

## Central teaching move

Ask the learner to trace one claim backward. For example, "This threshold detects half the test outcomes" must lead to 2 true positives, 2 false negatives, 4 outcomes, threshold 0.08513264, validation selection, the frozen `ML01` pipeline, the 224-row training fit, and the Module 01 prediction time.

## Reference facts

- modeling rows: 374;
- split: 224/75/75;
- outcomes: 25/7/4;
- baseline: 0.111607142857;
- linear fit: 69 of 111 timing rows;
- structural blanks: 263;
- `LOG01` prior-acute odds ratio: 2.20423495;
- selected model: `ML01`;
- leaked model: rejected before performance review;
- threshold: 0.08513264;
- test ROC AUC: 0.58802817;
- confusion: 48 TN, 23 FP, 2 FN, 2 TP; and
- reference disposition: `accept with conditions`.

## Common failures

- treating checkpoint assembly as a new analysis;
- scoring 39 points because H01 was not corrected;
- editing module evidence in the assembled folder;
- calling an odds ratio a risk multiplier;
- omitting structural blanks;
- treating the leaked model as a valid benchmark;
- saying `ML01` won on test;
- changing the threshold after test;
- reporting rates without counts;
- treating NPV as safety;
- ranking suppressed subgroups;
- allowing a high score to compensate for a failed gate; and
- permitting Module 04 after `revise` or `refer`.

## Reference status

The automated reference can earn full technical points with conditions. A real learner still requires a live defense and named reviewers. Technical validation does not impersonate those human decisions.
