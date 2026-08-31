# APP-5 Module 03 build plan

## Purpose

Build `oclc-app5-03`, Disparities and data limits, as a deterministic 16.5-hour, 20-point release at Module version `0.1.0` and Commons release `0.89.0`.

The module turns the accepted Module 02 population measures into a bounded disparity analysis. It adds a separate synthetic equity-group layer, calculates age-specific and directly standardized group rates, compares absolute and relative disparities under two reference choices, audits missing equity fields and representation, and applies primary and complementary suppression. It cannot make a real disparity, place, targeting, allocation, intervention, or community claim.

## Frozen Module 02 handoff

`freeze_upstream.py` must build and validate the complete Module 02 reference workspace, then copy it without editing into `upstream/module02-reference/`. The handoff also includes the accepted Module 02 `release.json` and a deterministic manifest for every frozen file.

The handoff must preserve:

- the complete 72-file Module 02 reference workspace and 57 immutable manifest rows;
- all 1,620 public-source union tracts and 1,597 measure tracts;
- all 7,985 accepted age-band denominators and generated numerator rows;
- the 5,679,768 adult denominator and 283,614 generated-event totals;
- all accepted crude, age-specific, direct, and guided indirect results;
- all unavailable states, query checks, score, gates, conditions, and the progression decision; and
- every prohibition on disparity claims, mapping, ranking, targeting, real community action, implementation, and deployment.

Any changed, missing, added, or renamed upstream file must fail validation.

## Synthetic equity release

`generate_equity_layer.py` must create release `fma-dp-01-equity-v1` with generator version `0.1.0` and seed `73053`.

The release has two linked teaching tables:

1. `synthetic-equity-margins.csv.gz` allocates every accepted tract-age denominator and generated event total across three separate marginal dimensions: combined race and ethnicity, primary language, and disability status.
2. `synthetic-field-completeness.csv.gz` records generated missing-field counts for race, ethnicity, primary language, disability status, and tract geography at the accepted tract-age grain.

The equity dimensions are separate margins, not joint records. They cannot be crossed to infer intersectional groups or individual identities. Names follow current federal data concepts where practical, but the values are fictional and are not Massachusetts demographic estimates.

Every dimension must reconcile independently to the accepted Module 02 denominator and numerator for each tract-age row. Group assignment uses fixed probabilities, fixed risk multipliers, deterministic tract variation, and largest-remainder integer allocation. The generator must publish its group contract, field dictionary, manifest, bytes, hashes, and reconciliation findings.

## Measurement contract

The reference SQL must:

1. link and reconcile the synthetic margins to the frozen Module 02 measure release;
2. aggregate age-specific group rates and Wilson intervals;
3. directly standardize every group to the accepted five-band Module 02 standard population;
4. calculate rate differences and rate ratios against both a predeclared group reference and the overall reported population;
5. calculate a summary rate difference and summary rate ratio for each dimension and reference choice;
6. profile missingness and representation without treating a zero missing count as proof of complete capture;
7. publish tract-group rates only when the generated event count is at least 16 and the denominator is at least 100; and
8. apply complementary suppression whenever a tract-dimension table has a primary suppressed cell.

Suppressed outputs must retain the tract, dimension, group, support state, and reason while leaving protected counts, rates, and intervals blank. Totals that would reveal a suppressed cell must not appear in the published tract-group table. The threshold is a fixed teaching rule informed by CDC presentation practice, not a universal legal or clinical standard.

Python must independently reproduce the SQL totals, rates, reference comparisons, summary measures, missingness, representation shares, primary suppression, and complementary suppression.

## Learner records

The learner workspace must provide blank but structurally valid copies of:

- `disparity-measure-specifications.csv`;
- `reference-group-sensitivity.csv`;
- `missingness-and-representation-audit.md`;
- `selection-linkage-measurement-bias.md`;
- `suppression-policy.md`;
- `responsible-disparity-claim.md`;
- `week3-component-score.csv`;
- `gate-results.csv`;
- `progression-decision.md`;
- `reproducibility-check.md`;
- `ai-use.md`; and
- four SQL files.

The reference workspace must contain the completed answer set. The workspace builder must refuse to overwrite a nonempty target and produce deterministic manifests.

## Assessment and authority

Module 03 contributes 20 course points once. Together with the accepted Module 02 score, the eventual Week 3 checkpoint totals 40 points. Module 01 remains a required zero-point gate.

Noncompensable gates must reject at least:

- changed upstream evidence;
- changed synthetic source or generated outputs;
- missing learner records;
- placeholder or copied reference answers;
- SQL that differs from the submitted learner SQL;
- a score below 16 of 20;
- a failed required gate;
- a disparity measure with the wrong direction, denominator, scale, or reference;
- a missing or unsupported interval;
- hidden missingness, exclusion, or linkage loss;
- a suppressed value published as zero;
- a single-cell suppression that can be reconstructed from totals;
- an intersectional claim from separate margins;
- a real observed-case or community claim;
- tract ranking, targeting, or allocation authority; and
- implementation or deployment authority.

The reference may conclude that a synthetic disparity statement is supported for the fictional teaching release, subject to named limits and conditions. It may permit construction of the cumulative Week 3 checkpoint. It may not permit Module 04 until that checkpoint accepts the frozen 40-point package.

## Verification and release sequence

1. Run the handoff, generator, disparity builder, workspace builder, and validator self-checks.
2. Run complete and starter validation, copied-answer rejection, complete-mode starter rejection, and protected failure routes.
3. Parse and execute the focused APP-5 section of `scripts/check-curriculum-specs.ps1`.
4. Check JavaScript syntax and APP-5 catalog hours.
5. Check plain ASCII, personal-path exclusion, package shape, hashes, and `git diff --check`.
6. Advance the Commons from `0.88.0` to `0.89.0`.
7. Commit, push, and verify the remote feature branch before building the Week 3 checkpoint.

## Human review before alpha

Faculty, population-health clinical, epidemiology, biostatistics, equity, community, privacy, race and ethnicity standards, language access, disability, accessibility, responsible-AI, and independent-reproduction reviewers must confirm the group contract, reference choices, interval method, missingness design, bias analysis, suppression rules, non-reconstruction behavior, claims, and progression conditions before alpha promotion.
