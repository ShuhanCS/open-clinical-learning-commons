# APP-5 Module 01: Framing a population-health decision

## 1. Module identity, duration, prerequisites, and place in the course

- Course: APP-5, Data for Population Health and Equity.
- Module: 01 of 07.
- Module ID: `oclc-app5-01`.
- Title: Framing a population-health decision.
- Instructional timing: Week 1.
- Learner time: 15.5 hours.
- Course points: 0.
- Assessment role: required gate for the 40-point Week 3 checkpoint.
- Module version: `0.1.0`.
- Commons release: `0.87.0`.
- Package path: `courses/population-health-equity/modules/01-population-health-decision/`.
- Build status: runnable release candidate.

Module 01 fixes the decision before the course begins calculating. Learners must define who and what the population represents, which denominator belongs to each possible measure, what tract geography and source period can support, who may experience benefit or harm, who can question the work, and what evidence would permit the next technical step.

The continuing case is `FMA-DP-01`, an explicitly fictional Massachusetts adult diabetes-prevention planning review. Public tract identifiers and source values are real. The council, program, resources, intervention, community-response records, implementation stream, and outcomes are fictional or synthetic.

### Prerequisites

Learners must have accepted FND-1 and FND-2 releases. They arrive able to:

- inspect complete public releases and record provenance;
- preserve raw values, missingness, identifiers, and unmatched states;
- write and check SQL joins and aggregations;
- define a population, numerator, denominator, period, and unit;
- interpret estimates, uncertainty, regression, validation, and subgroup support;
- distinguish prediction, description, and causation;
- publish accessible exact tables; and
- disclose and verify agent assistance.

The module applies these skills to population and geography contracts. It does not reteach generic SQL, cleaning, statistics, Git, or visualization.

### Course handoff

Module 01 may permit Module 02 to construct population, denominator, rate, and standardization measures. It cannot accept those measures itself. Module 02 begins only from the exact source release, decision charter, denominator roles, geography and time contract, accountability map, claim boundaries, and open conditions frozen here.

## 2. Population-health decision and named audiences

### Decision

The learner answers:

> Are the population, denominator roles, geography, time frame, source roles, community-review rights, accountable audience, and claim limits defined well enough to begin population-measure construction?

Allowed progression decisions are `continue`, `continue with conditions`, `revise`, and `refer`. The reference decision is `continue with conditions` for curriculum construction.

The permitted next action is narrow: construct and validate the Module 02 population, denominator, rate, and standardization measures. The decision does not permit a real local rate, disparity claim, map, tract ranking, targeting rule, allocation, model, intervention, outreach, implementation, evaluation, or policy.

### Named audiences

| Audience | Module 01 question |
|---|---|
| Affected residents | What is being said about the area, what could happen next, what is uncertain, and how can residents question or stop the process? |
| Community organizations | Which source claims require local knowledge, what is missing, and what revision or alternative is possible? |
| Population-health clinician | Does the condition framing preserve the population-to-patient boundary and avoid implying individual diagnosis or treatment? |
| Epidemiologist | Are the population, numerator concept, denominator roles, period, surveillance cadence, and source limitations coherent? |
| Biostatistician | Is the later rate and standardization plan technically possible without accepting formulas prematurely? |
| GIS and geography reviewer | Are tract identity, vintage, future geometry, aggregation, unmatched rows, and ecological limits explicit? |
| Equity, language, and disability reviewers | Do terms, participation rights, access, possible burden, exclusion, and stigma receive accountable review? |
| Public-health program and resource owners | Is the fictional decision separated from targeting, capacity, allocation, implementation, and real authority? |
| Data, privacy, and governance reviewers | Are complete public identities, public-versus-synthetic roles, minimization, linkage, and audit boundaries explicit? |
| APP-5 faculty | Do all 12 gates support Module 02 curriculum construction without expanding authority? |

## 3. Foundation skill being revisited or extended

### FND-1 extension

FND-1 cohort and denominator work becomes a multi-source population contract. Learners must keep four identities separate:

1. the adult population carried by the PLACES modeled estimate;
2. the ACS 2020-2024 total and age-by-sex population estimates with margins;
3. the SVI 2022 area-context population and ranking fields; and
4. the future deterministic synthetic event and program populations.

A shared tract FIPS supports a join. It does not prove that periods, populations, denominators, methods, or claims are compatible. Unmatched rows remain data, not nuisances.

### FND-2 extension

FND-2 uncertainty and subgroup reasoning becomes a pre-analysis claim contract. Learners inspect what an estimate, margin, modeled interval, relative rank, missing value, quality flag, and small denominator could mean before calculating a disparity or fitting any model.

The module also requires a normative boundary: a numerical difference may later support a disparity statement, but inequity requires evidence and an explicit judgment about unfairness or injustice. The agent cannot make that judgment.

### DA-730 use

Learners use exact tables, annotations, structured text, source labeling, and audience adaptation from DA-730. They do not make a choropleth map in Module 01. Module 04 owns mapping after geometry, support, aggregation, ecological, accessibility, and stigma gates are accepted.

## 4. Learning outcomes that can be assessed

By the end of Module 01, learners can:

1. state a bounded population-health decision with a decision owner, affected communities, intended next action, alternative, nonaction, possible benefit, possible harm, and stop route;
2. define the adult population, provisional numerator concept, source-specific denominator roles, geography, period, and surveillance cadence without inventing a final analytic measure;
3. distinguish modeled prevalence, survey population estimates, area context, relative ranks, synthetic evidence, and observed events;
4. verify the accepted raw and released PLACES, ACS, and SVI identities, including bytes, hashes, rows, fields, releases, periods, geography, and uncertainty;
5. reconcile unique tract keys and all pairwise intersections while preserving every unmatched state;
6. explain why a technically successful tract join does not establish analytic compatibility;
7. distinguish difference, disparity, and inequity and repair stigmatizing, ecological, individualizing, or automatic-targeting language;
8. assign community, clinical, methods, data, access, equity, program, resource, privacy, and faculty decision rights;
9. separate curriculum progression from real-world authority; and
10. disclose agent assistance and verify every source and decision claim independently.

Each outcome is visible in a named submitted record and a deterministic validation or human-review gate.

## 5. Concept ownership and explicit out-of-scope boundaries

### Module 01 owns

- the `FMA-DP-01` fictional case identity;
- population-health versus individual-care framing;
- the initial population and provisional numerator concept;
- source-specific denominator roles without final formulas;
- primary tract geography and later county-comparison route;
- PLACES, ACS, SVI, TIGER, synthetic, and agent evidence roles;
- source release, period, grain, uncertainty, key, and claim-limit records;
- tract-key feasibility and unmatched-state accounting;
- surveillance refresh and compatibility rules;
- difference, disparity, inequity, area-context, individual, and synthetic-result language;
- affected-community question, revision, and stop rights;
- accountable owners and open reviewer conditions;
- the early-analysis and real-world authority boundary; and
- the Module 02 progression decision.

### Module 02 owns later

- exact analytic populations and exclusions;
- synthetic event generator and numerator facts;
- adult and age-specific ACS denominator formulas;
- margin handling for sums;
- crude and specific rate formulas;
- direct-standardization age bands and standard population;
- guided indirect-standardization reference rates and expected counts;
- SQL linkage and reconciliation tables; and
- the 20-point population measure and denominator component.

### Module 03 owns later

- rate differences, rate ratios, and summary disparity measures;
- reference-group choice and sensitivity;
- disparity uncertainty;
- missing equity-field analysis;
- selection, linkage, and measurement bias;
- small-number and suppression rules; and
- the accepted 40-point Week 3 technical release.

### Later modules own

- Module 04: geometry, spatial joins, maps, geographic aggregation, ecological claims, small-area stability, and non-stigmatizing place evidence;
- Module 05: transparent targeting rules, allocation, fairness definitions, differential impact, benefit, harm, burden, and balancing measures;
- Module 06: intervention design, implementation, monitoring, feedback, governance, and the bounded area-profile ML challenger; and
- Module 07: clinician leadership, community-facing communication, final recommendation, accountability, and defense.

### Explicitly out of scope

- calculating or accepting a rate or standardized measure;
- calculating or accepting a disparity;
- choosing a reference group or suppression threshold;
- making a map or spatial inference;
- ranking, labeling, selecting, excluding, or targeting a tract;
- allocating resources or assigning eligibility;
- fitting a model or clustering areas;
- estimating an intervention effect;
- representing synthetic events, capacity, feedback, or outcomes as real;
- assigning an area value to an individual;
- contacting, enrolling, or acting on a real community;
- representing a real Massachusetts agency, program, organization, or funding decision; and
- implementation, evaluation, policy, clinical, or deployment authority.

## 6. Lesson sequence with estimated learner time

| Sequence | Learning work | Hours | Evidence produced |
|---:|---|---:|---|
| 1 | Enter the `FMA-DP-01` case; separate the curriculum decision from a funding or outreach question | 1.0 | Draft decision, owner, next action, alternative, and nonaction |
| 2 | Define population, provisional numerator, denominator roles, and the population-to-individual boundary | 2.0 | Population and denominator draft |
| 3 | Fix tract keys, source periods, boundary vintage, surveillance cadence, and incompatible-trend rules | 1.75 | Geography and time draft |
| 4 | Distinguish difference, disparity, inequity, area context, vulnerability language, and synthetic evidence | 1.5 | Equity-language repair set |
| 5 | Verify and profile the complete accepted PLACES, ACS, and SVI releases; inspect official readings and TIGER route | 3.0 | Reproduced source profile and source-role notes |
| 6 | Reconcile tract identities, all pairwise intersections, the three-source intersection, and unmatched states | 1.5 | Join-feasibility interpretation |
| 7 | Assign community, clinical, methods, access, data, program, resource, privacy, and faculty rights | 1.5 | Accountability map and stop routes |
| 8 | Guided case repair: reject observed-case, ecological, stigmatizing, automatic-targeting, and cross-vintage claims | 1.0 | Claim-boundary draft |
| 9 | Complete the independent population decision and source-feasibility package | 1.75 | Ten assessed learner records |
| 10 | Run validation, repair the package, disclose AI use, and record progression | 0.5 | Passing workspace and progression decision |
| Total |  | 15.5 |  |

The 15.5 hours include instruction, readings, public-data inspection, guided practice, independent work, validation, revision, and reflection.

## 7. Authoritative readings and public clinical sources

### Required public sources

1. CDC PLACES 2025 census-tract dataset metadata: https://data.cdc.gov/api/views/cwsq-ngmh
2. CDC PLACES methodology: https://www.cdc.gov/places/methodology/index.html
3. CDC PLACES frequently asked questions, including intervention-effect limits: https://www.cdc.gov/places/faqs/index.html
4. 2020-2024 ACS five-year data and API guidance: https://www.census.gov/data/developers/data-sets/acs-5year.html?lv=true
5. ACS B01001 table landing page: https://data.census.gov/table/ACSDT5Y2024.B01001
6. CDC/ATSDR SVI data and documentation: https://atsdr.cdc.gov/place-health/php/svi/svi-data-documentation-download.html
7. Census TIGER/Line 2024 release page: https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2024.html
8. CDC health-equity definition and context: https://www.cdc.gov/health-disparities-hiv-std-tb-hepatitis/about/index.html

### Reading purpose

Learners use the PLACES metadata, methodology, and FAQ to identify the adult population, small-area model, estimate type, interval, release, and program-effect boundary. They use ACS materials to identify the B01001 universe, estimate and margin fields, geography, and five-year period. They use SVI documentation to identify area-level variables, margins, flags, relative ranks, corrections, and cross-release limits. They use TIGER materials to reserve a compatible geometry route without mapping early.

The health-equity reading supports precise language. It does not determine by itself whether a measured difference in this teaching case is an inequity. That judgment requires additional evidence and accountable human reasoning.

Instructor and learner materials must link to complete visible URLs. A secondary summary cannot replace an official source identity or methods page.

## 8. Dataset inventory, provenance, license, and teaching purpose

### Accepted released files

| Source | Raw accepted scope | Released artifact | Rows | Fields | Released bytes | Released SHA-256 |
|---|---|---|---:|---:|---:|---|
| CDC PLACES | Every Massachusetts `DIABETES` row returned by the accepted 2025-release query | `data/places-diabetes-ma-tract-2025.csv` | 1,597 | 24 | 356,204 | `3d55a099be438999fd52b1e34f13589dcf3e260162c56967fa01fb0a80135846` |
| ACS B01001 | Complete 616,690-row national table file before extraction of every Massachusetts tract | `data/acs-b01001-ma-tract-2024.csv` | 1,620 | 100 | 576,420 | `bca33aebaa0a9e418d6a5343818aebc1e8b1dc2d355156419e5693d1907fa419` |
| CDC/ATSDR SVI | Complete Massachusetts 2022 tract CSV | `data/svi2022-ma-tract.csv` | 1,613 | 158 | 1,188,187 | `fac1aabd51880624ce728f4a63f01ba6b50959c203c6975400c02daf21329de0` |

### Raw identities

- PLACES accepted query: 426,520 bytes; SHA-256 `55125d80183968c4aaef419ed6171ee0d897254a95c472a8e4b346aa19a35ba3`.
- ACS complete national B01001 file: 200,356,282 bytes; SHA-256 `1637b18a96881b81e050df1cd3d5ac38a33208b9b69b40e1dbeb3c4e13718f0e`; 616,690 rows; 99 fields.
- SVI complete Massachusetts CSV: 1,189,804 bytes; SHA-256 `9e38e15b91041909fc58bdd56db677d9073598f9f8080048b71d16dd38f8b81e`.

### Profile artifacts

| Artifact | Rows | SHA-256 | Purpose |
|---|---:|---|---|
| `data/source-inventory.csv` | 3 | `1392a8a84047cf9725daf4053dbc0ac6efdbbe1b93eb6e9ed1e0c8074b6e89dd` | Complete source and release identities, roles, and limits |
| `data/field-inventory.csv` | 282 | `d65fb0bbde925e17e2b94ee362e43c1320d4f10467241f77cd260f50329854f7` | Every released field, support, missingness, and sentinel-like count |
| `data/join-feasibility.csv` | 3 | `2fc7811fc1f6350fb65581a5d946d073039b05a72006a9dd30ad829005cde1e6` | Pairwise tract intersections and unmatched states |
| `data/reading-inventory.csv` | 9 | `081f5d85da1657d838e51df31cb746d32f4ac6f716a3e24e4c28e33235148292` | Official interpretation and future geography routes |

### Rights and teaching purpose

PLACES is marked Public Domain in the official dataset metadata. ACS is U.S. government public data. SVI is an official public CDC/ATSDR release with a required suggested citation. The Commons preserves attribution and direct source routes for all three.

Open access does not remove ethical responsibility. Tract-level public data can still cause harm through careless linkage, misleading comparison, ecological inference, small-number reconstruction, stigma, or operational targeting. The release is for reproducible instruction and bounded public-data analysis only.

## 9. Data dictionary and expected analytic structure

### PLACES release

The 24 fields preserve:

- source and release facts: `year`, `datasource`, `category`, `measure`, `measureid`, `categoryid`, and `short_question_text`;
- geography: `stateabbr`, `statedesc`, `countyname`, `countyfips`, `locationname`, `locationid`, and `geolocation`;
- value definition: `data_value_unit`, `data_value_type`, and `datavaluetypeid`;
- modeled estimate and uncertainty: `data_value`, `low_confidence_limit`, `high_confidence_limit`, and footnote fields; and
- population context: `totalpopulation` and `totalpop18plus`.

All 1,597 rows are Massachusetts `DIABETES`, measure year 2023, and crude prevalence. Every tract key is unique. Every row has a point estimate, lower limit, upper limit, and adult population.

### ACS release

The 100 fields contain:

- `tract_fips`, derived deterministically from the source geography ID;
- `GEO_ID`, the complete source geography identity;
- `B01001_E001` through `B01001_E049`, the published estimates; and
- `B01001_M001` through `B01001_M049`, the published 90% margins.

Module 01 does not derive an adult denominator or combine margins. Those formulas and their tests belong to Module 02.

### SVI release

The 158 source fields preserve state, county, tract, location, area, population and housing estimates, margins, percentages, percentile components, theme sums, relative ranks, quality flags, daytime population, internet, and racial and ethnic adjunct variables.

The accepted Massachusetts file contains 1,385 negative sentinel-like values across its fields. These remain source values in Module 01. Later recoding requires the official documentation, a field-specific rule, an unavailable state, and validation. A negative source sentinel never becomes a real negative population or a zero by default.

### Expected grains and joins

| Layer | Grain | Unique key | Module 01 join rule |
|---|---|---|---|
| PLACES | one modeled diabetes estimate per tract | `locationid` | retain all 1,597 accepted rows |
| ACS | one B01001 population row per tract | `tract_fips` | preserve all 1,620 rows and all estimates and margins |
| SVI | one context row per tract | `FIPS` | preserve all 1,613 rows and sentinel-like values |

The three-source intersection is 1,597 tracts. The union is 1,620. Module 01 reports feasibility only; it does not publish a merged analytic table.

## 10. Worked example and instructor walkthrough

### Starting prompt

> Use the public data to identify the Massachusetts tracts with the greatest diabetes need and recommend which should receive the first fictional outreach resources.

The prompt is intentionally too broad. It hides the population, denominator, source role, uncertainty, period, geography, community authority, capacity, resource constraint, intervention, and possible harm. It also turns modeled prevalence into an allocation rule.

### Walkthrough

1. **Repair the action.** Replace “identify tracts for resources” with “decide whether the evidence is defined well enough to build measures and later ask structured community-review questions.”
2. **Name the population.** State adults age 18 and older represented by the accepted PLACES tract release, while requiring each later measure to preserve its own source-specific population.
3. **Separate numerator concepts.** PLACES is modeled prevalence. A later synthetic numerator is fictional. Neither is an observed local case count.
4. **Separate denominator roles.** The PLACES adult population travels with the PLACES estimate. ACS B01001 supplies separate age-by-sex estimates and margins. SVI population fields remain context.
5. **Fix geography and time.** Use 11-character tract FIPS, retain PLACES 2023/2025, ACS 2020-2024, and SVI 2022 labels, and reserve TIGER 2024 geometry for Module 04.
6. **Inspect complete sources.** Verify all accepted raw and released bytes, hashes, rows, fields, and official interpretation pages.
7. **Reconcile keys.** Confirm that all 1,597 PLACES tracts have ACS and SVI rows while preserving the 16 extra SVI and seven extra ACS-beyond-SVI tract states.
8. **Repair language.** Say modeled prevalence, area context, and relative rank. Do not say observed cases, high-risk residents, vulnerable tracts, causal effect, or automatic need.
9. **Assign rights.** Residents and community organizations can question the framing, add evidence, require revision, and stop progression to real action.
10. **Bound progression.** Permit Module 02 curriculum construction with conditions. Prohibit early analysis and every real-world action.

### Correct reference decision

`Continue with conditions` is supportable because the sources and roles reproduce, the 1,597-tract teaching population has complete tabular source coverage, unmatched rows remain visible, and the decision boundary is explicit.

The conditions are material: methods reviewers must approve age bands, denominator formulas, standard population, margin handling, synthetic numerators, standardization, disparity measures, and suppression. Community, equity, language, disability, privacy, source, clinical, accessibility, and independent-reproduction review remain required.

The decision does not identify or rank a tract.

## 11. Guided practice

### Practice A: repair the population

Convert “Massachusetts adults” into a population statement with source, age, tract inclusion, period, exclusions, and source-specific denominator roles.

### Practice B: keep denominators attached

Given PLACES `totalpop18plus`, ACS B01001, and SVI `E_TOTPOP`, explain which can accompany the PLACES modeled prevalence and which require a different measure contract.

### Practice C: inspect source identity

Use `source-inventory.csv` to trace one source from official URL through raw bytes and hash to the released artifact and claim limit.

### Practice D: reconcile tract sets

Reproduce the three pairwise intersections. Explain why all PLACES tracts having ACS and SVI rows does not justify silently discarding the source-only rows.

### Practice E: repair an observed-case claim

Rewrite “Tract X has 400 adults with diagnosed diabetes” so it correctly describes modeled prevalence, population context, uncertainty, and what cannot be inferred.

### Practice F: repair an ecological claim

Rewrite “Residents of high-SVI tracts are high risk” at the area level and state what person-level evidence would be needed.

### Practice G: separate disparity and inequity

Draft one supported numerical-difference statement and list the additional evidence and judgment required before calling it an inequity.

### Practice H: test community rights

Given a plan that allows community comment but not revision or stopping, identify the accountability failure and repair the decision-right record.

### Practice I: stop automatic targeting

Challenge a rule that selects tracts by PLACES prevalence or SVI rank alone. Name the missing local, capacity, access, burden, fairness, and community evidence.

## 12. Independent exercise

### Assignment

Build a complete Module 01 decision and source-feasibility package for `FMA-DP-01`. Use the immutable public release. Do not change a source file, calculate a rate, publish a map, rank a tract, or create a targeting score.

### Required decisions

1. What exact curriculum decision is being made?
2. Who owns it, who may be affected, and who can require revision or stop progression?
3. What population is represented, and what remains excluded or unknown?
4. What provisional numerator concepts exist, and which are modeled, synthetic, or prohibited?
5. Which denominator travels with each source role?
6. What tract key, periods, vintages, later aggregation, and surveillance cadence apply?
7. What can PLACES, ACS, SVI, TIGER, and future synthetic evidence each support?
8. What do the pairwise intersections and unmatched tract states mean?
9. How will the work distinguish difference, disparity, and inequity?
10. Which observed-case, individual, causal, ecological, stigmatizing, targeting, and real-world claims are prohibited?
11. What agent assistance was used and independently verified?
12. May Module 02 begin, under what conditions, and with what authority still prohibited?

### Independent defense questions

1. Why is the PLACES adult population not silently interchangeable with ACS or SVI population fields?
2. Why does the 1,597-tract intersection establish technical feasibility but not analytic compatibility?
3. What do the 16 SVI-without-PLACES and seven ACS-without-SVI records teach?
4. Why is modeled prevalence not an observed count?
5. What additional evidence turns a disparity claim into an inequity claim?
6. What could harm a community even when every source is public?
7. Why does a community need more than a comment box?
8. What exact work may Module 02 begin, and what remains prohibited?

## 13. Visualization and communication requirements

### Required displays

Module 01 requires no map and no ranked chart. The submission must include, within the named records:

- one exact source-scale table with PLACES, ACS, and SVI rows, fields, periods, geography, and evidence roles;
- one exact tract-feasibility table with all pairwise intersections and unmatched counts;
- one plain-language source-role explanation that distinguishes modeled, survey, contextual, boundary, and synthetic evidence;
- one population and denominator explanation that a nontechnical community reader can follow; and
- one accountable progression statement with permitted, prohibited, revision, and stop routes.

### Communication rules

- Use `modeled prevalence`, not observed cases.
- Use `area-level context`, not individual vulnerability or risk.
- Keep PLACES 2023 measure year and 2025 release distinct.
- Keep ACS 2020-2024 and SVI 2022 labels visible.
- State that SVI ranks are release-relative.
- Report unmatched states as unavailable or unmatched, never zero.
- Do not name a “highest-need,” “worst,” “vulnerable,” or “priority” tract.
- Do not use color, position, or geography as the only carrier of meaning.
- Give exact values and structured text for every comparison.
- State that `FMA-DP-01` is fictional and that no real action is authorized.

## 14. Exact submission package and filenames

### Immutable controls and public evidence, 16 manifest rows

The builder copies these files unchanged and records their bytes, SHA-256, and role in `release-manifest.csv`:

1. `.gitattributes`
2. `VERSION`
3. `requirements.txt`
4. `assessment.md`
5. `data-spec.md`
6. `decision-contract.json`
7. `profile_sources.py`
8. `source-record.yml`
9. `validate_workspace.py`
10. `data/places-diabetes-ma-tract-2025.csv`
11. `data/acs-b01001-ma-tract-2024.csv`
12. `data/svi2022-ma-tract.csv`
13. `data/source-inventory.csv`
14. `data/field-inventory.csv`
15. `data/join-feasibility.csv`
16. `data/reading-inventory.csv`

The learner may read but not edit these files. A changed byte invalidates the workspace.

### Editable assessed records, 10 files

1. `population-decision-charter.md`
2. `population-denominator-contract.csv`
3. `geography-time-contract.csv`
4. `public-data-role-map.csv`
5. `source-feasibility-interpretation.md`
6. `equity-language-contract.csv`
7. `community-accountability-map.csv`
8. `claim-boundary.csv`
9. `progression-decision.md`
10. `ai-use.md`

Filenames, headers, row counts, IDs, Markdown field labels, and safety fields are fixed. Learners complete content rather than changing the schema.

### Generated workspace control

`release-manifest.csv` is generated during assembly. It contains 16 sorted immutable rows with `relative_path`, `bytes`, `sha256`, and `role`.

The assembled learner or reference workspace contains exactly 27 files. Extra files, renamed records, duplicate submissions, embedded local paths, or missing evidence fail validation.

### Build commands

From the module package:

```powershell
python .\profile_sources.py
python .\build_workspace.py --target D:\CodexTemp\app5-m01-learner
python .\validate_workspace.py D:\CodexTemp\app5-m01-learner --starter
```

### Reference commands

```powershell
python .\build_workspace.py --target D:\CodexTemp\app5-m01-reference --reference
python .\validate_workspace.py D:\CodexTemp\app5-m01-reference
```

The builder refuses to overwrite an existing target. A rebuild uses a new empty target or a reviewed, exact cleanup outside the module package.

## 15. Rubric and pass conditions

Module 01 is a zero-point required gate. It is evaluated as `pass`, `revise`, or `refer`; a strong narrative cannot compensate for a failed source, population, community-right, or authority gate.

| Dimension | Passing evidence | Revision trigger |
|---|---|---|
| Decision | One bounded curriculum decision, owner, next action, alternative, nonaction, possible benefit, possible harm, and stop route | The decision is a broad research topic, tract ranking, outreach, allocation, or real program action |
| Population and denominator | Age, tract inclusion, source-specific populations, numerator concepts, denominator roles, periods, and limits are explicit | “Massachusetts adults” or one denominator is used for every source without a contract |
| Source identity | Raw and released bytes, hashes, rows, fields, releases, URLs, uncertainty, and roles reproduce | A convenience sample, changed file, incomplete national ACS inspection, or invented provenance appears |
| Tract feasibility | Unique keys, all pairwise intersections, the 1,597 three-source intersection, and unmatched states are accurate | Rows are dropped, unmatched becomes zero, or a successful join is called analytic compatibility |
| Equity reasoning | Difference, disparity, inequity, area context, individual inference, stigma, and synthetic status are precise | A difference is automatically called inequity or a place is labeled as a fixed problem |
| Community accountability | Residents and organizations can question, add evidence, require revision, and stop progression to real action | Community involvement is passive, decorative, inaccessible, or fabricated |
| Claim boundary | Modeled, survey, contextual, synthetic, ecological, causal, targeting, and authority limits are complete | The package claims observed cases, individual risk, causation, intervention effect, automatic need, or permission |
| Reproducibility and AI | Source, builder, starter, complete, and protected failure checks pass; AI use is disclosed and verified | The release cannot rerun, a protected route passes, an agent made a human decision, or a personal path leaks |

### Noncompensable gates

All 12 gates must pass:

1. The accepted PLACES, ACS, and SVI raw and released identities match.
2. Source rows, fields, tract keys, state and measure filters, releases, periods, and uncertainty reproduce.
3. The 1,597-tract intersection and every unmatched state remain explicit.
4. PLACES, ACS, SVI, TIGER, future synthetic, and agent roles remain separate.
5. Population, numerator concept, denominator roles, geography, time, cadence, and accountable decision are explicit.
6. Difference, disparity, and inequity are distinct.
7. Affected communities have question, evidence, revision, and stop rights.
8. Modeled prevalence, area context, and relative ranks are not observed, individual, causal, or evaluative claims.
9. No tract is ranked, targeted, funded, excluded, stigmatized, or assigned an intervention.
10. No rate, standardization, disparity metric, map, targeting score, model, or intervention effect appears early.
11. Agent use is disclosed, protected data are absent, and humans retain accountability.
12. Progression permits Module 02 construction only while every real-world authority remains prohibited.

### Passing threshold

A complete package passes when all deterministic checks and all 12 human-review gates pass. `Continue with conditions` is allowed only when conditions concern named later review or construction decisions and do not conceal a current gate failure.

## 16. Common errors, failure modes, and instructor interventions

| Error | Why it fails | Instructor response |
|---|---|---|
| “Massachusetts adults” without source or period | The population cannot be reproduced or matched to a denominator | Require age, tract set, source, period, exclusions, and source-specific roles |
| Multiplying PLACES prevalence by a population and calling it observed cases | PLACES is a model-based estimate | Restore modeled wording and prohibit count construction in Module 01 |
| Replacing the PLACES population with ACS without explanation | The measure and denominator no longer share a source contract | Require separate denominator roles and reserve comparison for Module 02 |
| Treating SVI `E_TOTPOP` as the health-rate denominator | SVI population fields serve its area-context release | Return the record to source-role review |
| Treating SVI rank as a longitudinal measure | Ranks are relative to the accepted release and comparison set | Require release-specific language and prohibit cross-version trend claims |
| Dropping the 16 or seven unmatched tract states | Missing source support becomes invisible | Require pairwise reconciliation and an explicit unmatched policy |
| Calling a technical join analytically compatible | Key agreement does not align populations, periods, methods, or meaning | Ask for one compatibility condition for each source role |
| Mapping immediately | Geometry, support, aggregation, ecological, accessibility, and stigma gates have not passed | Remove the map and reserve it for Module 04 |
| Ranking by PLACES or SVI | Public evidence is converted into an unreviewed policy choice | Reframe to source feasibility and later structured community review |
| Calling a difference an inequity | The normative and community evidence is missing | Require separate technical and normative statements |
| Calling tracts vulnerable, high risk, resistant, or underserved | The language can stigmatize and often exceeds the measure | Name the specific measured condition, unit, source, period, and limit |
| Giving community members comment rights only | They cannot change or stop the process | Add revision, evidence, access, recourse, and stop rights |
| Fabricating community input | Synthetic text is misrepresented as real voice | Remove it; reserve clearly fictional community records for later teaching |
| Allowing the agent to decide progression | Accountability is delegated | Require human rationale, independent checks, and signed ownership |
| Calling curriculum progression approval | Course construction is not implementation or policy authority | Repair every progression and final sentence |

An instructor stops progression immediately for a changed immutable source, hidden unmatched state, protected or identifiable data, individual inference, fabricated community endorsement, automatic target, or real-world action claim.

## 17. Accessibility, equity, privacy, and responsible-claim checks

### Accessibility

- All tables have headers, units, periods, geography, source, and structured reading order.
- All source and comparison facts appear as text, not only visual position.
- Links use descriptive text and the complete visible URL.
- Meaning does not depend on color.
- Markdown headings are nested correctly.
- Plain-language explanations define modeled prevalence, denominator, tract, margin, rank, and synthetic evidence.
- Community-review rights include language and disability access.
- A future map requires a nonvisual exact-value alternative before it can pass Module 04.

### Equity and community accountability

- Learners identify who is represented, absent, unmatched, misclassified, or affected by the framing.
- A disparity statement remains separate from an inequity judgment.
- Area context is not assigned to individuals.
- Sources do not stand in for community priorities, consent, endorsement, or lived experience.
- Residents and community organizations can question, add evidence, require revision, and stop progression to real action.
- Potential benefits and harms include stigma, exclusion, surveillance burden, inaccessible delivery, resource diversion, and false precision.
- No group or place receives a lower evidence or safety standard.

### Privacy and data minimization

All accepted source data are public tract-level records. The module contains no address, person, household, patient, employee, clinician, program participant, credential, or restricted record. Learners do not attempt to link public tract fields to individuals or reconstruct suppressed or unavailable values.

Open data still require minimization. Only fields needed for the course decision are used in a derived release. Source-only rows and sentinel states remain available for audit without being converted into person-level profiles.

### Responsible claims

Every statement identifies whether its evidence is:

- modeled PLACES prevalence;
- ACS survey population estimate or margin;
- SVI area estimate, margin, flag, theme, or relative rank;
- Census boundary metadata;
- deterministic synthetic teaching evidence;
- a derived calculation; or
- a human judgment.

The submission must state that PLACES does not supply observed cases or local intervention effects; ACS and SVI values are not individual traits; a shared key is not analytic compatibility; SVI ranks are not longitudinal; a cluster or score is not a community type or entitlement; and curriculum acceptance is not real-world authority.

## 18. AI and agent policy, required disclosure, and verification

### Permitted assistance

Agents may help:

- retrieve the declared public URLs;
- draft or explain source-checking code;
- inspect schemas, rows, keys, missingness, sentinel-like values, and joins;
- draft alternative decision or claim wording;
- suggest validation tests;
- review accessibility and plain language; and
- diagnose a failed deterministic check.

### Human-only decisions

The learner and named reviewers must decide:

- the population and numerator concept;
- denominator roles;
- geography, period, and cadence;
- whether a source is suitable for a claim;
- difference, disparity, and inequity language;
- community decision rights;
- possible benefit and harm;
- progression and conditions; and
- every real-world authority boundary.

The agent may not choose a tract, rank, threshold, weight, fairness definition, intervention, community position, progression, or final recommendation.

### Required disclosure

`ai-use.md` records:

- tool and task;
- public data shared;
- confirmation that protected or identifiable data shared are `none`;
- instruction or prompt;
- output used;
- independent source, code, and claim checks;
- human revision;
- accountable human; and
- confirmation that agent authority is `none` over the population, denominator, equity language, community role, progression, targeting, allocation, intervention, or final decision.

### Verification rule

Every agent-produced data or source statement must reproduce through the accepted standard-library scripts or direct inspection of the immutable release. Every wording suggestion must be checked against the source role, audience, community consequence, and claim boundary. An agent's confidence is not evidence.

## 19. Answer key and instructor notes

### Exact release facts

- PLACES released rows: 1,597.
- PLACES fields: 24.
- PLACES counties: 14.
- PLACES measure year: 2023.
- PLACES value type: crude prevalence.
- PLACES point-estimate range: 0.7% to 30.5%.
- PLACES adult population field range: 66 to 13,070.
- PLACES rows with both published confidence limits: 1,597.
- ACS released Massachusetts tract rows: 1,620.
- ACS released fields: 100.
- ACS complete national raw rows: 616,690.
- ACS complete national raw fields: 99.
- ACS complete national raw bytes: 200,356,282.
- SVI released Massachusetts tract rows: 1,613.
- SVI fields: 158.
- SVI negative sentinel-like field values preserved: 1,385.
- Field-inventory rows: 282.
- PLACES and SVI intersection: 1,597; PLACES only: 0; SVI only: 16.
- PLACES and ACS intersection: 1,597; PLACES only: 0; ACS only: 23.
- SVI and ACS intersection: 1,613; SVI only: 0; ACS only: 7.
- Three-source intersection: 1,597.
- Three-source union: 1,620.

These are source-feasibility facts. They are not tract rankings, disease counts, disparities, targets, or program results.

### Reference population and denominator conclusion

The initial population is adults age 18 and older represented in the accepted PLACES Massachusetts diabetes-tract release, with each later measure retaining its own source-specific population.

The PLACES adult population remains attached to the modeled PLACES estimate. ACS B01001 supplies separate age-by-sex population estimates and margins for later denominator and standardization work. SVI population fields remain area context. A future synthetic numerator must be labeled, versioned, and matched to a declared denominator without creating a false real local result.

### Reference source conclusion

The three public tabular sources are technically feasible for the next curriculum step because every PLACES tract has ACS and SVI support and the unmatched source rows are fully accounted for. They are not analytically interchangeable. Periods, populations, methods, uncertainties, and meanings remain different.

### Reference language conclusion

Module 01 may describe a modeled difference or area pattern only as a source fact. It does not accept a disparity analysis. It cannot label an inequity without later accepted technical, structural, historical, normative, and community evidence.

### Reference accountability conclusion

Affected residents and community organizations have rights to question the framing, add local evidence, contest interpretations and burdens, require revision, and stop progression to real action. No real community input or endorsement appears in the reference case.

### Reference progression

The correct reference decision is `continue with conditions` for Module 02 curriculum construction. Rate calculation in Module 01, standardization in Module 01, disparity claims, mapping, tract ranking, targeting, allocation, model fitting, intervention-effect estimation, real community action, implementation, and deployment remain prohibited.

### Required open conditions

- population-health clinical review;
- epidemiology and biostatistics review;
- ACS, PLACES, and SVI methods review;
- approval of synthetic events, age bands, standard population, margin handling, and standardization plan;
- community, racial and ethnic equity, language-access, and disability-access review;
- GIS and boundary review before Module 04;
- privacy, data-governance, accessibility, and responsible-AI review; and
- independent reproduction.

## 20. Runnable acceptance checks for data, code, links, and expected findings

### Source checks

```powershell
python .\profile_sources.py
python .\profile_sources.py --self-check
```

The source check must verify:

- all three committed released hashes;
- 1,597 PLACES rows and 24 fields;
- 1,620 ACS rows and 100 fields;
- 1,613 SVI rows and 158 fields;
- 282 field-inventory rows;
- unique 11-character Massachusetts tract keys;
- exact state, measure, year, and value-type filters;
- exact pairwise intersections and unmatched counts;
- a 1,597-tract three-source intersection and 1,620-tract union; and
- exact profile hashes.

The protected source mutation route must fail.

### Builder checks

```powershell
python .\build_workspace.py --self-check
```

The builder must produce two byte-identical reference manifests, one incomplete learner workspace, 16 sorted immutable manifest rows, and exactly 27 files. It must refuse to overwrite an existing target.

### Validator checks

```powershell
python .\validate_workspace.py --self-check
```

The accepted release reports:

- complete reference validation: 176 checks;
- learner starter validation: 112 checks;
- noncompensable gates: 12; and
- protected failures rejected: missing record, changed source, placeholder in complete work, expanded authority, removed community stop right, observed-case claim, copied reference answer in starter mode, and personal local path.

### Independent workspace checks

```powershell
python .\build_workspace.py --target D:\CodexTemp\app5-m01-reference --reference
python .\validate_workspace.py D:\CodexTemp\app5-m01-reference
python .\build_workspace.py --target D:\CodexTemp\app5-m01-starter
python .\validate_workspace.py D:\CodexTemp\app5-m01-starter --starter
```

### Acquisition check

An authorized source refresh may run:

```powershell
python .\profile_sources.py --acquire --temp-root D:\CodexTemp
```

The acquisition must download and verify the complete 200,356,282-byte ACS national B01001 file before extraction. A changed upstream byte or hash blocks replacement and requires review rather than silently refreshing the release.

### Link checks

Before alpha, an independent reviewer must confirm that every URL in `data/reading-inventory.csv` resolves to the intended official resource and that no redirect changes publisher, dataset, release, or method meaning.

### Expected findings

The exact release findings in Section 19 must reproduce. The expected decision is not a tract selection. It is a bounded determination that public-source and decision framing are strong enough to begin Module 02 curriculum construction under named conditions.

## 21. Release status, reviewers, version, and known issues

### Release decision

- Module version: `0.1.0`.
- Commons release: `0.87.0`.
- Status: runnable release candidate.
- Reference progression: `continue with conditions`.
- Module 02 curriculum construction: permitted.
- Course points awarded here: 0.
- Week 3 points owned later: Module 02, 20; Module 03, 20.

The release includes complete public tabular evidence, deterministic acquisition and profiles, learner and reference records, a 16-row immutable manifest, a 27-file workspace, a validator, protected failure routes, instructor notes, an assessment, a source record, a data specification, a decision contract, and a semantic version.

### Required review coverage before alpha

- APP-5 faculty owner;
- population-health physician or clinical reviewer;
- epidemiologist;
- biostatistician with standardization and disparity-methods expertise;
- ACS and Census methods reviewer;
- PLACES small-area-estimation reviewer or qualified equivalent;
- SVI and social-determinants reviewer;
- GIS and Census-geography reviewer;
- community-engagement and community-governance reviewer;
- racial and ethnic equity reviewer;
- language-access reviewer;
- disability-access reviewer;
- public-health program and resource-allocation reviewer;
- privacy and data-governance reviewer;
- responsible-AI reviewer;
- accessibility and communication reviewer; and
- independent reproducer.

One person may cover more than one role only when qualifications and conflicts are recorded. Missing clinical, epidemiology, biostatistics, geographic, community, equity, accessibility, privacy, or independent-reproduction coverage blocks alpha.

### Known issues and open decisions

- The official APP-5 section and half-term dates are not assigned.
- Named human reviewers are not assigned.
- The final synthetic event generator, seed, age groups, period, numerator, and known truth are not accepted.
- The ACS adult denominator cells, margin-of-error combination method, and treatment of annotations or sentinels require Module 02 methods review.
- The direct standard population and guided indirect-standardization reference rates are not accepted.
- The disparity measures, reference groups, missing-equity-field design, support, uncertainty, small-number, aggregation, and suppression rules are reserved for Module 03.
- TIGER 2024 Massachusetts geometry is not acquired or validated until Module 04.
- Local evidence, capacity, access, resource constraints, community-review design, and targeting alternatives are reserved for Modules 04 and 05.
- The intervention, implementation, monitoring, evaluation proposal, feedback, incident, escalation, pause, stop, revision, and retirement design is reserved for Module 06.
- The fixed ML feature set, scaling, cluster count, seed, stability tests, and rejection rule are reserved for Module 06.
- Joe Joseph's participation, schedule, format, recording permission, biography wording, case wording, and assessment role require direct confirmation before Module 07 alpha.

### Protected Module 02 handoff

Module 02 receives:

- the exact `0.1.0` Module 01 release identity;
- all three public-source files and four profile files;
- the 1,597-tract intersection and complete unmatched accounting;
- the accepted population and source-specific denominator roles;
- the tract, period, vintage, and surveillance contract;
- the public, boundary, synthetic, and agent data-role map;
- the equity-language and community-accountability contracts;
- all 14 claim boundaries;
- the reference progression and open conditions; and
- every early-analysis and real-world prohibition.

Module 02 may build deterministic synthetic event aggregates and population measures for curriculum construction. It may not silently change the public source release, case identity, community rights, claim limits, or real-world authority. A change requires a new recorded handoff and semantic-version decision.
