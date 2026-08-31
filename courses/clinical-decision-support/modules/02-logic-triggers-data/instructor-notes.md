# APP-4 Module 02 instructor notes

## Central teaching move

Keep asking one question: what happens when an otherwise plausible rule meets a real workflow state? Learners should be able to name why a card does not appear, not just why one appears.

The strongest work distinguishes five things that are often collapsed: an effective clinical time, a recorded time, an availability time, a rule-evaluation time, and a response-delivery time. The delayed and silent-failure cases make those differences visible.

## Fixture boundary

The `score_fixture` column is supplied, not modeled. The `0.20` value is intentionally arbitrary. It tests equality and ordering only. Stop and repair any submission that interprets it as an estimated risk, recommended cutoff, accepted threshold, or evidence of benefit.

## Duplicate-resource finding

The full Synthea release contains 11,109 repeated IDs across `Location`, `Organization`, `Practitioner`, and `PractitionerRole`. Do not describe the release as dirty or useless. Use the finding to teach explicit entity-resolution policy, cardinality checks, and the danger of a join that multiplies rows.

## Discussion prompts

1. Why does a missing card not prove the patient was below a threshold?
2. Which failures should remain quiet, and which require an operational signal?
3. Who owns terminology drift, stale values, duplicate requests, and response transport?
4. What evidence would be needed before replacing the mock score?
5. What evidence would be needed before accepting any threshold?

## Reference interpretation

All 16 fixtures pass their expected mechanics. This supports Module 03 curriculum construction with conditions. It does not validate the clinical concept, input list, lookback, model, threshold, local burden, patient consequence, safety, implementation, or deployment.
