# APP-5 Week 3 checkpoint defense

## Q01. Which releases are frozen?

Answer: APP-5 Modules 01, 02, and 03 at versions `0.1.0` and Commons releases `0.87.0`, `0.88.0`, and `0.89.0` are frozen in the candidate.

Evidence: The outer manifest has 219 rows, and the three nested manifests have 16, 57, and 104 rows.

Limit: A correction must return to its owning module and create a reviewed new release.

## Q02. How are the 40 points counted?

Answer: Module 01 contributes zero points, Module 02 contributes 20 once, Module 03 contributes 20 once, and the checkpoint contributes zero.

Evidence: `checkpoint-score.csv` has two 20-point subtotals and one 40-point total.

Limit: A passing score cannot compensate for a failed gate.

## Q03. What population and source roles remain in scope?

Answer: `FMA-DP-01` is a fictional adult Massachusetts teaching review using complete public PLACES, ACS, and SVI tract releases plus separately labeled synthetic evidence.

Evidence: Module 01 inventories 1,597 PLACES, 1,620 ACS, and 1,613 SVI rows.

Limit: Real tract identifiers do not make the fictional council, numerator, or decision real.

## Q04. What denominator and linkage are accepted?

Answer: The five-band adult denominator totals 5,679,768, and 1,597 measure tracts link to 283,614 generated planning-need events.

Evidence: Module 02 source reconciliation and all 30 query checks pass.

Limit: The generated numerator is not an observed case count.

## Q05. What rate and standardization evidence is accepted?

Answer: Crude, age-specific, direct standardized, and guided indirect measures use one declared standard population and explicit support and uncertainty states.

Evidence: There are 1,576 available direct rates, 21 unavailable direct rates, and 80 guided indirect cases.

Limit: An unavailable rate cannot be changed to zero or filled by convenience.

## Q06. How are public and synthetic measures separated?

Answer: PLACES modeled prevalence remains in its own table, while ACS denominators and synthetic events support the teaching rate release.

Evidence: `public-modeled-prevalence.csv` has 1,597 rows and is not joined into the synthetic numerator.

Limit: The two evidence types cannot be combined into a false observed local measure.

## Q07. What does the synthetic equity layer contain?

Answer: It contains three separately reconciling marginal dimensions, 19 groups, 151,715 group-margin rows, and 7,985 completeness rows.

Evidence: Each dimension reconciles to 5,679,768 denominator units and 283,614 synthetic events.

Limit: The margins are not joint person records and do not support intersectional estimates.

## Q08. What disparity and reference evidence is accepted?

Answer: The release has 110 group-age rates, 22 standardized rates, 32 reference comparisons, and six summary disparity records under declared and overall references.

Evidence: All 36 disparity query checks and 12 source reconciliations pass.

Limit: Reference sensitivity supports interpretation, not a real or causal disparity claim.

## Q09. What missingness and representation limits remain?

Answer: Race, ethnicity, language, and disability retain explicit missing counts, and geography has zero missing only after conditioning on the accepted linked frame.

Evidence: The missing counts are 6,000, 7,578, 5,314, 8,376, and zero respectively, with 19 representation records.

Limit: Zero conditioned geography missingness does not prove perfect capture.

## Q10. How are selection, linkage, and measurement bias handled?

Answer: The release keeps an eight-row register that separates the three bias types and assigns an owner and decision consequence.

Evidence: `bias-register.csv` contains eight complete records.

Limit: A register makes a limit visible; it does not remove the bias.

## Q11. How does suppression prevent reconstruction?

Answer: Cells with fewer than 16 events or a denominator below 100 receive primary suppression, and complementary cells are withheld when subtraction could reveal one protected value.

Evidence: The release has 19,742 primary, 1,488 complementary, and 21,230 total suppressed cells; all 4,791 audits pass.

Limit: Suppressed counts, rates, and intervals remain blank, and tract totals are not published.

## Q12. What responsible disparity statement is supported?

Answer: The fictional synthetic release supports a bounded teaching statement under its declared references, missingness, bias, support, uncertainty, and suppression rules.

Evidence: The responsible claim, score, and all 18 Module 03 gates agree.

Limit: No real Massachusetts, intersectional, causal, ranking, targeting, or allocation claim is supported.

## Q13. What cumulative conflict did the checkpoint resolve?

Answer: It preserves modeled public prevalence, synthetic event rates, and synthetic equity margins as distinct evidence layers while keeping one population and denominator chain of custody.

Evidence: The evidence index and readiness review name every source role and prohibit merging them.

Limit: Reconciliation of identities does not make unlike measures interchangeable.

## Q14. What may Module 04 do?

Answer: Module 04 may validate geometry, compare geographic aggregation, study small-area stability and ecological limits, and create one responsible accessible teaching map and context memo.

Evidence: The progression decision grants Module 04 curriculum construction with conditions.

Limit: Module 04 cannot revise accepted measures or begin Module 05 targeting work early.

## Q15. What remains prohibited and unresolved?

Answer: Real or intersectional disparity claims, a map inside this checkpoint, tract ranking, targeting, eligibility, outreach, allocation, funding, model fitting, intervention-effect estimation, real community action, implementation, production connection, and deployment remain prohibited. Twelve human-review conditions remain open before alpha.

Evidence: `responsible-claims-audit.md`, `conditions-register.csv`, and `progression-decision.md` agree.

Limit: Curriculum progression is not real-world authorization.
