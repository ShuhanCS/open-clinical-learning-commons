# APP-5 course and Module 01 build plan

## Purpose

Establish APP-5, Data for Population Health and Equity, as a distinct seven-module applied course, then build `oclc-app5-01`, Framing a population-health decision, as a deterministic runnable release candidate at Module version `0.1.0` and Commons release `0.87.0`.

The course owns population denominators, linked public and contextual data, rate standardization, disparity measurement, small-number protection, geographic reasoning, targeting, fairness, intervention analytics, community accountability, and an equity recommendation. It uses foundation and visualization skills without reteaching them.

Module 01 decides whether a fictional Massachusetts statewide adult diabetes-prevention planning review is defined well enough to begin the population-measure build in Module 02. It does not calculate a disparity, rank or target a tract, make a map, allocate resources, fit a model, evaluate an intervention, or authorize action in a real community.

## Fixed course handoff

- Course: APP-5, Data for Population Health and Equity.
- Credits: 3.
- Delivery: seven instructional modules inside an official half-term; the academic calendar controls the final due date.
- Total learner time: 112.5 hours.
- Prerequisites: accepted FND-1 and FND-2 releases.
- Primary graded tools: SQL and Python; R remains read, run, and interpret.
- Week 3 checkpoint: 40 points.
- Week 6 checkpoint: 25 points.
- Final checkpoint: 35 points on the official last day of the assigned half-term.
- Module 06: eight hours of intervention design, monitoring, and governance plus an eight-hour embedded-ML extension.
- Module 07: clinician-led leadership, communication, accountability, and defense designed for Joe Joseph, MD, SFHM, without claiming participation before direct confirmation.

## Continuing case and decision boundary

A fictional Massachusetts population-health planning team is considering a limited adult diabetes-prevention outreach planning review. The public evidence may identify tract-level patterns and questions for community review. It cannot establish observed disease counts, individual risk, causal effects, intervention effectiveness, community deficit, automatic program eligibility, or a funding decision.

The initial decision is whether the population, denominator, geography, time frame, evidence roles, accountable audience, affected-community role, and claim limits are coherent enough to build measures next.

## Full public-source architecture

Module 01 will acquire, fingerprint, profile, and release the complete Massachusetts tract rows needed for the continuing case while recording the full upstream identities:

- CDC PLACES 2025 census-tract release: every Massachusetts `DIABETES` row, including point estimate, interval, measure year, total population, adult population, county, and tract identity;
- 2020-2024 ACS five-year Detailed Table B01001: every Massachusetts census-tract row and all published age-by-sex estimates and margins needed for later denominator and standardization work, extracted only after the complete national table file is fingerprinted;
- CDC/ATSDR SVI 2022 Massachusetts census-tract CSV: the complete state tract release with estimates, margins, themes, ranks, and source fields preserved; and
- Census TIGER/Line 2024 Massachusetts tract boundaries: source route fixed for Module 04, where geometry is acquired and validated before mapping.

PLACES is modeled small-area prevalence and cannot detect local intervention effects. ACS and SVI are survey-derived area context with vintages and uncertainty that must remain visible. SVI percentile ranks are relative and are not interchangeable across releases. Area values cannot be assigned to individuals.

## Module 01 source-feasibility outputs

- `data/places-diabetes-ma-tract-2025.csv`
- `data/acs-b01001-ma-tract-2024.csv`
- `data/svi2022-ma-tract.csv`
- `data/source-inventory.csv`
- `data/field-inventory.csv`
- `data/join-feasibility.csv`
- `data/reading-inventory.csv`

The source profiler must reject changed, missing, truncated, duplicated, out-of-state, wrong-measure, or schema-inconsistent releases. It must preserve unmatched tract identities as evidence rather than silently dropping them.

## Learner and reference records

- `population-decision-charter.md`
- `population-denominator-contract.csv`
- `geography-time-contract.csv`
- `public-data-role-map.csv`
- `source-feasibility-interpretation.md`
- `equity-language-contract.csv`
- `community-accountability-map.csv`
- `claim-boundary.csv`
- `progression-decision.md`
- `ai-use.md`

The learner template keeps source evidence and controls complete while leaving assessed records incomplete. The reference package contains one bounded construction answer and preserves all open faculty, epidemiology, biostatistics, geography, equity, community, accessibility, privacy, and independent-reproduction conditions.

## Required implementation

- APP-5 source record and course-level specification before the module specification;
- seven distinct module briefs, workload, checkpoint contracts, assessment map, embedded-ML boundary, leadership boundary, and build order;
- durable 21-section Module 01 specification;
- deterministic public-source acquisition, extraction, profiling, and verification;
- deterministic learner/reference workspace builder with an immutable manifest;
- validator with complete, starter, copied-answer, source-mutation, placeholder, progression, and prohibited-authority checks;
- assessment, rubric, instructor notes, data specification, decision contract, source record, release record, requirements, and semantic version;
- course catalog, root README, build ledger, and central curriculum-checker integration.

## Noncompensable Module 01 gates

1. All accepted source identities, fields, rows, bytes, hashes, releases, and vintages reproduce.
2. Massachusetts tract and measure filters are complete and exact.
3. Source grain, population, denominator, time, uncertainty, and geographic identity are explicit.
4. PLACES, ACS, SVI, and future synthetic intervention data have separate evidence roles.
5. Population, denominator, geography, time frame, surveillance cadence, and accountable decision are explicit.
6. Equity, disparity, and inequity are used precisely; a measured difference is not automatically labeled unjust.
7. Affected communities have review, question, revision, and stop routes rather than being passive subjects.
8. Modeled prevalence, area context, and relative ranks are not described as observed cases, individual traits, causal effects, or program impact.
9. No tract is ranked, targeted, funded, excluded, stigmatized, or assigned an intervention in Module 01.
10. No disparity metric, map, targeting score, model, or intervention-effect estimate appears early.
11. AI use is disclosed, protected data are prohibited, and human accountability remains explicit.
12. Progression permits Module 02 measure construction only while every real-world allocation, implementation, and deployment authority remains prohibited.

## Verification and release

1. Rebuild every committed public extract from the accepted upstream identities.
2. Build two reference workspaces and require byte-identical manifests.
3. Build and validate an incomplete learner workspace.
4. Validate the complete reference workspace.
5. Reject source mutations, missing records, copied answers, placeholders in complete work, invalid progression, unsupported claims, and any early targeting or real-world authority.
6. Run focused APP-5 checks and proportionate curriculum regression checks.
7. Advance Commons from `0.86.0` to `0.87.0`.
8. Commit, push, and remote-verify the APP-5 course and Module 01 as one isolated unit.
