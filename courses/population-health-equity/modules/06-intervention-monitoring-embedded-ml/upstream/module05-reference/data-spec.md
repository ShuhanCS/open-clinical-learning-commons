# Data specification

## Accepted public evidence

The upstream handoff is the complete 287-file Module 04 reference workspace. Module 05 reads the accepted 1,597-row PLACES teaching table and the accepted synthetic marginal group release. It does not change source identity, estimate, interval, population field, support state, suppression, geography, score, gate, or claim limit.

## Fictional planning source

`data/raw/fictional-planning-layer.csv.gz` contains one row per accepted measure tract. It adds fictional capacity, travel, staff, language-access readiness, disability-access readiness, community-review state, unresolved questions, objection state, burden, and accountable owner. The generator uses seed `73055` and stable tract-key hashes. It does not use a public prevalence value to generate those fields.

The public and synthetic layers share tract and county keys for teaching linkage. Their meanings remain separate. Public evidence provides modeled area context. Synthetic rows provide fictional planning conditions.

## Resource and rule inputs

`data/rule-definitions.csv` declares exactly four rules. `data/sensitivity-variants.csv` declares 20 variants before analysis. Every base rule receives 280 fictional places in 28 equal ten-place awards. No partial award or automatic action is permitted.

## Released outputs

- `candidate-source-profile.csv`: one-row source, resource, and readiness profile.
- `linked-candidate-table.csv.gz`: 1,597 complete public-plus-synthetic teaching rows.
- `rule-assignments.csv.gz`: 6,388 complete rule-tract results.
- `rule-summary.csv`: four rule consequence summaries.
- `county-concentration.csv`: 56 rule-county rows.
- `group-consequences.csv`: 76 rule-group rows that preserve suppression.
- `rule-overlap.csv`: six pairwise rule comparisons.
- `sensitivity-results.csv`: 20 predeclared variants.
- `query-checks.csv`: 40 release checks.
- `build-report.json`: identities, findings, fingerprints, and authority limit.

## Suppression and missingness

Published synthetic group counts may be summed only where the accepted upstream row is publishable. Suppressed values remain unavailable. They may not be changed to zero, reconstructed from other rows, or joined across marginal dimensions into person-level combinations.

## Claim limit

The release supports a reproducible classroom comparison. It does not establish real need, benefit, harm, capacity, access, preference, consent, fairness, eligibility, outreach, funding, allocation, community action, service delivery, intervention effect, implementation, production readiness, or deployment authority.
