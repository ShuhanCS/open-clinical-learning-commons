# Instructor notes

## Teaching purpose

Module 02 asks whether the class can build population measures that are correct enough to support later disparity analysis. Keep attention on the population, denominator, age band, multiplier, uncertainty, source period, geography, unavailable state, and interpretation limit behind every number.

The continuing case is fictional. The public tract sources are real aggregate estimates. The event numerator is generated and carries no real clinical or allocation meaning.

## Suggested 16-hour sequence

| Block | Hours | Work |
|---|---:|---|
| Handoff and source reconciliation | 1.5 | Verify Module 01, inspect the 1,620-row union, and explain why 23 ACS tracts lack a PLACES diabetes row |
| ACS age-band construction | 2.5 | Trace all 38 B01001 cells, calculate five adult bands, preserve paired margins, and reconcile adult totals |
| Numerator and denominator linkage | 2.0 | Inspect the generated numerator, verify 7,985 one-to-one joins, and test invalid-count conditions |
| Crude and age-specific rates | 2.5 | Build counts, rates per 100,000, Wilson intervals, and unavailable states |
| Direct standardization | 2.5 | Build the five-row standard, verify weights, calculate direct rates, and explain the relative-index limit |
| Guided indirect standardization | 2.0 | Apply statewide synthetic age rates to local age structures and interpret the standardized event ratio |
| Public-synthetic separation and support review | 1.0 | Contrast PLACES modeled prevalence with generated event rates without merging them |
| Validation, assessment, and handoff | 2.0 | Run Python reproduction, score 20 points, resolve gates, document conditions, and issue progression |
| Total | 16.0 |  |

## Facts the reference must reproduce

- 1,620 union tracts and 1,597 measure-eligible tracts.
- Sixteen ACS and SVI tracts without a PLACES diabetes row.
- Seven ACS-only tracts.
- Five adult age bands built from 38 B01001 source cells.
- 7,985 denominator rows and 7,985 synthetic event rows.
- 5,679,768 adult denominator units.
- 283,614 generated events.
- Forty-one zero age-band denominators.
- 7,944 available age-specific rates.
- 1,576 available direct rates and 21 unavailable direct rates.
- Eighty tracts requiring the guided indirect exercise.
- Five standard weights totaling one.
- Thirty passing SQL checks and eight passing source-reconciliation checks.

## Method notes

The ACS 90 percent margin approximation uses the root-sum-of-squares rule for nonzero component estimates and includes only the largest margin among zero-estimate components. The Census Bureau notes that this approximation omits covariance. Do not present it as a published ACS margin for the derived band.

The direct rate applies local synthetic age-specific rates to one common standard distribution. It is a relative index, not an actual local risk. The indirect ratio applies standard synthetic age rates to each tract's own population. It is not directly comparable across tracts as though it used common weights.

The interval methods are deliberately transparent and bounded. Module 03 owns the deeper uncertainty, support, suppression, and disparity analysis.

## Language checks

Accept language such as:

- "The PLACES value is modeled crude prevalence."
- "The synthetic rate is a generated teaching measure."
- "The direct result is unavailable because one age-band denominator is zero."
- "The indirect ratio compares synthetic events with a synthetic expectation."

Reject language such as:

- "observed diabetes cases";
- "the highest-need tract";
- "the disparity is";
- "fund this tract";
- "target this community"; or
- "the intervention will work."

## Grading

Score the five four-point criteria only after all 15 gates pass. An incorrect denominator, hidden unmatched tract, failed source identity, zero-filled unavailable rate, public-synthetic blend, unsupported observed-case claim, or expanded authority blocks progression regardless of the point total.

The reference progression is `continue with conditions`. This permits Module 03 curriculum construction only. It does not approve a disparity statement, map, rank, target, allocation, intervention, community action, implementation, or deployment.

## Human review before alpha

Require faculty, population-health clinical, epidemiology, biostatistics, ACS, PLACES, SVI, community, equity, accessibility, privacy, responsible-AI, and independent-reproduction review. Confirm the age bands, synthetic numerator, ACS margin method, direct standard, interval methods, sparse-support rule, indirect comparison limit, and Module 03 suppression design.
