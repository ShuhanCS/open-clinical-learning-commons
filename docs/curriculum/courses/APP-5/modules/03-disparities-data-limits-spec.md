# APP-5 Module 03 specification: Disparities and data limits

## 1. Module identity, decision, and release boundary

- Course: APP-5, Data for Population Health and Equity.
- Module ID: `oclc-app5-03`.
- Module title: Disparities and data limits.
- Module version: `0.1.0`.
- Commons release: `0.89.0`.
- Workload: 16.5 hours.
- Course points: 20.
- Week 3 point role: Module 02 contributes 20 points once and Module 03 contributes 20 points once. Module 01 remains a required zero-point gate.
- Package: `courses/population-health-equity/modules/03-disparities-data-limits/`.
- Build plan: `docs/plans/2026-08-31-app5-module03-plan.md`.
- Status: runnable release candidate.

The module decision is:

> Does the accepted fictional evidence support a bounded synthetic disparity statement strong enough to enter the cumulative Week 3 review under explicit reference, uncertainty, missingness, representation, bias, support, and suppression limits?

The reference answer is `continue with conditions`. It supports a synthetic disparity question inside `fma-dp-01-equity-v1` and permits construction of the Week 3 checkpoint. It does not permit Module 04 until that checkpoint accepts the frozen 40-point package.

This module does not make a real Massachusetts disparity claim. It cannot describe a group as biologically different, characterize a real community, map or rank tracts, determine eligibility, target outreach, allocate resources, choose an intervention, implement a program, or deploy a system.

## 2. Place in the course and prerequisite handoff

Module 01 fixed the population, geography, source, denominator, period, audience, community role, claim boundary, and authority limits. Module 02 built the linked population measures and accepted five-band standardization release. Module 03 accepts those decisions without repair.

The frozen handoff contains:

- the complete 72-file Module 02 reference workspace;
- the 57-row Module 02 nested manifest;
- the accepted Module 02 release record;
- a 73-row, 12,048-byte outer handoff manifest;
- handoff manifest SHA-256 `f5e84b251143edeb65b68d816a57492755083d8bc57c73e6bdaede381b933ef1`;
- 1,620 public-source union tracts and 1,597 measure tracts;
- 7,985 age-band denominator rows and 7,985 generated numerator rows;
- 5,679,768 adult denominator units and 283,614 generated events;
- all crude, age-specific, directly standardized, and guided indirectly standardized results;
- every unavailable state, score, gate, condition, and progression limit; and
- the separation between public PLACES prevalence and the synthetic numerator.

`freeze_upstream.py` builds and validates Module 02 before creating a new handoff. It compares every frozen file by path, byte count, and SHA-256. Module 03 must fail if an upstream file is changed, removed, added, or renamed.

The frozen handoff is evidence, not a cache to repair. A Module 03 learner cannot recalculate an accepted Module 02 rate to make a disparity easier to interpret.

## 3. Learning outcomes

By the end of the module, learners can:

1. state why a disparity measure requires a population, outcome direction, denominator, age standard, reference, interval, support rule, and data-generation boundary;
2. reconcile separate synthetic group margins to an accepted population and numerator without turning them into joint person records;
3. calculate age-specific and directly standardized group rates with intervals and availability states;
4. calculate and interpret rate differences and rate ratios on absolute and relative scales;
5. calculate a summary disparity measure while retaining the pairwise results it can hide;
6. defend a predeclared reference and show how an overall reported reference changes magnitude or direction;
7. profile missing race, ethnicity, primary language, disability status, and tract geography fields;
8. distinguish selection, linkage, measurement, uncertainty, and suppression limits;
9. apply primary and complementary suppression without publishing a blank as zero or exposing it through totals;
10. write one bounded synthetic disparity statement with the evidence, limits, owner, permitted next step, and prohibited uses; and
11. reproduce the release with SQL, Python, manifests, hashes, and an AI-use record.

These outcomes apply FND-1 and FND-2 skills to a population-health decision. The module does not reteach generic SQL, missing-value handling, descriptive statistics, inference, or chart design.

## 4. Concept ownership and protected boundaries

Module 03 owns:

- a predeclared synthetic group contract;
- separate marginal group tables;
- age-specific and directly standardized group rates;
- absolute rate differences and relative rate ratios;
- one summary absolute disparity measure and one summary relative measure;
- reference-group choice and sensitivity;
- missing equity-field measurement;
- representation shares and unsupported group states;
- selection, linkage, measurement, and uncertainty bias analysis;
- primary small-number suppression;
- complementary suppression and non-reconstruction; and
- a responsible disparity claim boundary.

The module extends prior courses:

- FND-1 owns generic joins, aggregation, data profiling, missingness, provenance, and reproducibility.
- FND-2 owns generic inference, uncertainty, subgroup support, and interpretation of model limits.
- DA-730 owns comparison and uncertainty display concepts. Module 03 applies them to a population-health claim but does not grade a visualization.
- APP-2 owns patient-experience representation and response bias. APP-5 owns population-level group margins and an allocation-facing claim boundary.
- APP-4 owns subgroup evaluation for a clinical decision support tool. APP-5 owns population disparity measures and their later place and targeting consequences.

Module 03 cannot:

- change the accepted population, numerator, denominator, geography, period, or standard population;
- relabel public PLACES modeled prevalence as observed cases;
- relabel generated events or rates as observed Massachusetts evidence;
- join separate margins into a joint identity table;
- establish an intersectional disparity;
- treat race or ethnicity as biological exposure;
- treat a reference group as a norm, ideal, or policy target;
- merge a small group only to avoid suppression;
- impute or reconstruct a suppressed value;
- map or rank real tracts;
- select a target, eligibility rule, resource allocation, intervention, or implementation action; or
- authorize a real decision.

## 5. Continuing evidence thread and source authority

The continuing case remains `FMA-DP-01`, a fictional adult diabetes-prevention planning review. Real Massachusetts tract identities and frozen public aggregate releases remain in the upstream package. The group layer is synthetic because those public sources do not provide an accepted joint numerator, denominator, identity, access, disability, or program record for this teaching decision.

The source roles remain separate:

| Evidence | Role in Module 03 | Prohibited interpretation |
|---|---|---|
| ACS B01001 | Frozen adult age denominators and common standard population | Individual identity, diabetes event, or actual equity-group denominator |
| CDC PLACES | Frozen modeled crude diabetes prevalence for source context | Observed diagnosis count, intervention outcome, or generated numerator |
| CDC/ATSDR SVI | Frozen area-level context for later work | Individual trait, group identity, automatic target, or funding rule |
| Module 02 synthetic events | Frozen generated planning-need numerator | Observed case, diagnosis, eligibility result, or outcome |
| Module 03 synthetic margins | Group-rate and data-limit teaching source | Massachusetts group estimate, joint record, biological effect, or action authority |

Module 03 downloads no replacement public source. It carries the complete accepted public releases through the Module 02 reference handoff. This prevents a new source vintage from changing the Week 3 evidence halfway through the course.

## 6. Synthetic equity source release contract

Release `fma-dp-01-equity-v1` uses:

- generator version `0.1.0`;
- seed `73053`;
- fictional period `2024`;
- three separate marginal dimensions;
- 19 group definitions;
- 151,715 tract-age-dimension-group rows;
- 7,985 tract-age field-completeness rows;
- 5,679,768 generated population units per dimension;
- 283,614 generated events per dimension; and
- source-manifest SHA-256 `c3f7549f6fcc25e0bfd5f074a7f936e519a0bd7f9459452da903c653aee28384`.

The source files are:

| File | Rows | Bytes | SHA-256 |
|---|---:|---:|---|
| `data/raw/synthetic-equity-margins.csv.gz` | 151,715 | 1,708,745 | `aaacdd529cf3ab563db5ad4ebd4509496db544ebb63896b8c4dfaed44c89793d` |
| `data/raw/synthetic-field-completeness.csv.gz` | 7,985 | 71,316 | `9093020f885deaa71b9f1a1f47682343c17a401910c298b9f72fd661768c9edf` |
| `data/equity-group-contract.csv` | 19 | 5,366 | `56530a6063dd614eab498396ca9cfaca68fd37c70888be375a003d21fe468e70` |
| `data/data-dictionary.csv` | 39 | 8,148 | `1ae498e5a8f084bacb5e34a65d716b70747116c73d03fc3e25c7326712e0fdab` |
| `data/synthetic-source-manifest.csv` | 4 | 1,606 | `c3f7549f6fcc25e0bfd5f074a7f936e519a0bd7f9459452da903c653aee28384` |

For each tract-age row, the generator:

1. reads the accepted Module 02 denominator and event total;
2. perturbs fixed group shares with a stable hash-derived tract-age value;
3. allocates integer populations by largest remainder;
4. allocates events through deterministic constrained weighted sampling, never assigning more events than population units;
5. verifies that every dimension returns exactly to the accepted denominator and numerator; and
6. writes explicit synthetic and margin-only flags.

The constrained event allocation avoids a rounding artifact that would systematically remove events from very small generated groups when each tract-age row is processed separately.

## 7. Authoritative readings and methods

Learners use the following public methods:

Healthy People 2030 methods:

https://www.cdc.gov/nchs/healthy-people/hp2030/methods.html

The NCHS page distinguishes absolute and relative, between-group and overall, and maximal and summary disparity measures. It also makes reference choice part of the method rather than a hidden default.

NCHS, Methodological Issues in Measuring Health Disparities:

https://stacks.cdc.gov/view/cdc/6654/cdc_6654_DS1.pdf

The report frames six choices that matter here: reference point, absolute or relative scale, favorable or adverse event orientation, pairwise or summary form, group weighting, and group ordering.

U.S. Cancer Statistics suppression guidance:

https://www.cdc.gov/united-states-cancer-statistics/technical-notes/suppression.html

The current CDC presentation rule withholds rates and counts based on fewer than 16 cases. Module 03 uses 16 as its event threshold and adds a denominator threshold of 100 as an explicit teaching rule.

U.S. Cancer Statistics data dictionary and complementary suppression guidance:

https://www.cdc.gov/rdc/media/pdfs/2026/01/uscs-rdc-datadictionary-cdc-nov2024.pdf

The guidance explains why another cell must be withheld when a single suppressed cell could be recovered from a total.

2024 revision to OMB Statistical Policy Directive No. 15:

https://www.govinfo.gov/content/pkg/FR-2024-03-29/pdf/2024-06469.pdf

HHS implementation guidance on race, ethnicity, primary language, and disability status:

https://aspe.hhs.gov/sites/default/files/documents/20f1e2b607af3f3b46d7668f337b679b/dhhs-implementation-guidance-data-collection-standards.pdf

The synthetic labels borrow current collection concepts where practical. The teaching release is not a compliant survey instrument, and named standards, community, language-access, and disability reviewers must approve it before alpha.

## 8. Workload and learning sequence

The 16.5-hour workload is fixed:

| Work | Hours | Evidence |
|---|---:|---|
| Verify the frozen Module 02 handoff and source identities | 1.5 | Handoff and source checks |
| Read the group, margin, field-completeness, and claim contracts | 2.0 | Measure specifications |
| Link margins and build age-specific group rates in SQL | 3.0 | SQL files 01 and 02 |
| Standardize rates and calculate pairwise and summary disparities | 2.5 | SQL file 03 and disparity tables |
| Defend both reference choices and compare interpretations | 2.0 | Reference-sensitivity record |
| Audit missingness, representation, selection, linkage, and measurement bias | 2.0 | Missingness and bias records |
| Apply primary and complementary suppression | 2.0 | SQL file 04 and suppression policy |
| Write the responsible claim, score, gates, progression, AI, and reproduction records | 1.5 | Completed submission |
| Total | 16.5 | 20-point component |

An instructor may divide the work across shorter sessions. The evidence order must remain intact: source contract before calculation, calculation before claim, and support before publication.

## 9. SQL and Python execution contract

The learner submits four SQL files:

1. `01-link-equity-margins-and-reconcile.sql`;
2. `02-build-group-age-rates.sql`;
3. `03-standardize-and-compare-references.sql`; and
4. `04-audit-missingness-bias-and-suppression.sql`.

SQL owns:

- typed source loading;
- tract, age, dimension, and group keys;
- marginal reconciliation;
- age-specific group aggregation;
- rate and interval calls;
- direct standardization;
- reference joins;
- rate differences and ratios;
- summary measures;
- missingness and representation tables;
- tract-group support;
- primary and complementary suppression;
- the bias register; and
- 36 query checks.

Python owns independent reproduction. It recalculates each rate, interval, standardization, pairwise comparison, summary measure, missingness total, representation share, primary suppression, complementary suppression, source total, output hash, and workspace manifest.

SQLite receives only three registered math helpers: square root, Wilson lower bound, and Wilson upper bound. No external Python dependency is required. Reference SQL cannot contain a learner placeholder.

## 10. Group, margin, and field-completeness contract

The three dimensions are:

| Dimension | Reported groups | Missing group | Primary reference |
|---|---:|---:|---|
| Combined race and ethnicity | 8 | 1 | White |
| Primary language | 6 | 1 | English |
| Disability status | 2 | 1 | No reported disability |

The combined race and ethnicity dimension includes American Indian or Alaska Native, Asian, Black or African American, Hispanic or Latino, Middle Eastern or North African, Native Hawaiian or Pacific Islander, White, Multiple identities, and Missing.

The primary-language dimension includes English, Spanish, Portuguese, Haitian Creole, Chinese, Another language, and Missing. The disability dimension includes Reported disability, No reported disability, and Missing.

These are generated marginal categories. A row in the race and ethnicity margin is not the same person or record as a row in the language or disability margin. The release cannot answer questions about Black Spanish-speaking adults with a disability, or any other intersection. It also cannot establish self-identification quality or real population composition.

The field-completeness table separately records generated missing counts for race, ethnicity, primary language, disability status, and tract geography. This permits distinct race and ethnicity missingness review even though the disparity margin uses a combined race and ethnicity dimension.

## 11. Group rate, interval, and standardization contract

For group (g) and age band (a):

```text
rate_g,a = generated_events_g,a / generated_population_g,a * 100000
```

Age-specific intervals use the Wilson score interval for the generated event proportion. The module uses the interval to teach support and uncertainty, not to claim random sampling from a real Massachusetts population.

For direct standardization:

```text
direct_rate_g = sum over age bands (standard_weight_a * rate_g,a)
```

The five weights are the accepted Module 02 standard population and total one. The approximate variance is:

```text
sum over age bands (
  standard_weight_a^2
  * p_g,a * (1 - p_g,a)
  / generated_population_g,a
) * 100000^2
```

The 95 percent interval uses the normal critical value 1.959963984540054. A reported group comparison requires all five positive age denominators and at least 16 generated statewide events. Missing groups remain in the audit but do not enter disparity comparisons.

The accepted outputs contain 110 group-age rates and 22 standardized rows: 19 groups plus an overall reported reference for each of three dimensions.

## 12. Absolute, relative, and summary disparity contract

For group (g) and reference (r):

```text
rate_difference_g,r = standardized_rate_g - standardized_rate_r
rate_ratio_g,r = standardized_rate_g / standardized_rate_r
```

The rate difference is per 100,000 and retains direction. The ratio is unitless. A ratio above one means the generated adverse-event rate is higher than the selected reference; a ratio below one means it is lower. Neither result explains why.

Conservative comparison intervals use group and reference endpoints:

```text
difference_low = group_low - reference_high
difference_high = group_high - reference_low
ratio_low = group_low / reference_high
ratio_high = group_high / reference_low
```

The release has 32 pairwise rows: 16 reported groups under a predeclared group reference and the same 16 under the overall reported reference.

For each dimension and reference choice, the module calculates:

- the mean absolute pairwise rate difference;
- the mean ratio oriented above one;
- the maximal rate difference; and
- the maximal rate ratio.

There are six summary rows. These are unweighted teaching summaries. They cannot replace the pairwise results, group sizes, missing groups, or support states.

## 13. Reference-group sensitivity contract

The predeclared group references are White, English, and No reported disability. They were chosen before calculation because they are large generated reported groups that make a familiar reference-choice critique possible. They are not biological baselines, norms, ideals, or targets.

The alternative reference is the directly standardized overall reported population for the same dimension. Missing groups are excluded from that reference but remain in the missingness and representation audit.

The accepted summary sensitivity is:

| Dimension | Primary reference | Primary absolute summary | Primary ratio summary | Overall absolute summary | Overall ratio summary |
|---|---|---:|---:|---:|---:|
| Disability status | No reported disability | 2,172.8508 | 1.471738 | 1,086.4254 | 1.220960 |
| Primary language | English | 778.3285 | 1.162898 | 584.3474 | 1.118987 |
| Combined race and ethnicity | White | 974.8181 | 1.212924 | 718.9415 | 1.147838 |

Changing the reference does not change a source count or group rate. It changes the comparison question, and therefore the magnitude and sometimes the direction of the result. Learners must name that consequence.

## 14. Missingness, representation, and bias contract

The accepted field audit uses 283,614 generated event records:

| Field | Missing | Percent |
|---|---:|---:|
| Race | 6,000 | 2.1156% |
| Ethnicity | 7,578 | 2.6719% |
| Primary language | 5,314 | 1.8737% |
| Disability status | 8,376 | 2.9533% |
| Tract geography | 0 | 0.0000% |

Zero tract-geography missingness is a property of the conditioned analytic layer. It does not count records that could not enter the layer because geography was absent or unusable.

The 19-row representation audit reports each group's generated population count, event count, population share, event share, support, and missing-group status. Groups cannot be merged after results are seen.

The eight-row bias register covers:

1. selection into the tract-linked analytic universe;
2. selection created by a generated numerator;
3. exclusion of 23 ACS-only tracts from the measure intersection;
4. generated combined race and ethnicity categories;
5. generated language and disability categories;
6. inability to cross separate margins;
7. interval uncertainty omitted from the teaching calculation; and
8. loss of local detail through suppression.

Each row has a mechanism, evidence, likely direction, mitigation or limit, owner, and open status. A correct join does not close a selection or measurement problem.

## 15. Primary and complementary suppression contract

A tract-group row is primarily suppressed when:

```text
generated_event_count < 16
or generated_population_count < 100
```

When exactly one group in a tract-dimension table is primarily suppressed, the smallest remaining supported cell is also withheld. Selection uses generated event count, then denominator, then fixed group order. If two or more cells are already primarily suppressed, no additional cell is needed for this teaching rule.

The accepted 30,343-row publication table contains:

- 19,742 primary suppressed cells;
- 1,488 complementary suppressed cells; and
- 9,113 publishable cells.

All 4,791 tract-dimension audits pass. The 21,230 suppressed rows retain keys, state, and reason. Their population count, event count, rate, and interval are blank. Blank means unavailable, not zero.

The publication table has no tract-dimension total. The module also prohibits reconstructing a cell from another output, filling a blank from the open synthetic source, or merging categories to avoid the rule in a submitted publication.

The raw source is openly available and synthetic. The rule teaches publication behavior; it is not a claim that the repository provides confidentiality protection for real records.

## 16. Required learner deliverables

The learner submits 15 editable files:

| File | Required evidence |
|---|---|
| `sql/01-link-equity-margins-and-reconcile.sql` | Typed links, margin totals, frozen-source reconciliation, and separate-margin flags |
| `sql/02-build-group-age-rates.sql` | Group-age aggregation, rates, Wilson intervals, and availability states |
| `sql/03-standardize-and-compare-references.sql` | Direct standardization, pairwise measures, intervals, two references, and summary measures |
| `sql/04-audit-missingness-bias-and-suppression.sql` | Missingness, representation, bias, primary suppression, complementary suppression, and checks |
| `disparity-measure-specifications.csv` | Nine complete measure definitions |
| `reference-group-sensitivity.csv` | Three primary-versus-overall comparisons |
| `missingness-and-representation-audit.md` | Five fields, 19 groups, conditioned universe, and margin limits |
| `selection-linkage-measurement-bias.md` | Separate bias mechanisms, evidence, direction, mitigation, and limits |
| `suppression-policy.md` | Thresholds, counts, complementary rule, blanks, and non-reconstruction |
| `responsible-disparity-claim.md` | One bounded synthetic claim and prohibited uses |
| `week3-component-score.csv` | Five criteria and a 20-point total |
| `gate-results.csv` | 18 passing gates with evidence and owners |
| `progression-decision.md` | Checkpoint permission, Module 04 hold, authority limits, and ten conditions |
| `reproducibility-check.md` | Commands, deterministic findings, checks, hashes, and limits |
| `ai-use.md` | Agent role, data shared, human owner, verification, and zero action authority |

The learner workspace has 108 files and 92 immutable manifest rows. It contains no accepted output directory. The reference workspace has 120 files and 104 immutable manifest rows.

## 17. Assessment, score, and noncompensable gates

The five criteria are worth four points each:

| Criterion | Points |
|---|---:|
| Group rates, support, intervals, and standardization | 4 |
| Absolute, relative, summary, and reference-sensitivity measures | 4 |
| Missingness, representation, selection, linkage, and measurement bias | 4 |
| Primary and complementary suppression with non-reconstruction | 4 |
| Responsible claim, reproduction, AI record, and progression | 4 |
| Total | 20 |

A passing score is at least 16 of 20 and all 18 gates. The reference earns 20 of 20.

The gates require:

1. the exact frozen Module 02 identity;
2. the exact synthetic source identity;
3. three complete dimension reconciliations;
4. separate-margin flags on every source row;
5. group support and intervals;
6. direct standardization;
7. absolute disparity calculations;
8. relative disparity calculations;
9. predeclared reference choices;
10. overall reported alternative references;
11. supported summary measures;
12. five-field missingness;
13. all 19 representation rows without merging;
14. eight explicit bias records;
15. deterministic primary suppression;
16. deterministic complementary suppression;
17. non-reconstruction and unavailable-not-zero behavior; and
18. a bounded claim and authority decision.

A point score cannot compensate for a failed gate. A polished sentence cannot compensate for a wrong denominator, hidden missingness, unsupported interval, changed reference, or exposed suppressed cell.

## 18. Reference package and instructor key

The package contains 136 files. Its accepted outputs are:

| Output | Rows | SHA-256 |
|---|---:|---|
| `equity-margin-reconciliation.csv` | 12 | `f50399f9fa23c67d20936fc1be2eea44122ccd6e1cb97510ce3847705a52ec17` |
| `group-age-rates.csv` | 110 | `8cb835a825a123aaaab230cbaee7d47365a0cd081db539b5cbc5792541011844` |
| `standardized-group-rates.csv` | 22 | `1feccf9c75de467e9c3e301a08084e097c62391c3e55c72f986613e0cb15dd1f` |
| `disparity-comparisons.csv` | 32 | `96b9f25c5c768e680636f4f222bdc1c34ca58fcd956caa85a7ec143dcd61ce78` |
| `summary-disparities.csv` | 6 | `1a0d27cc4a145388b0007b2be859daac06c29f9bc43dc367bfc2e7f7bc344289` |
| `missingness-audit.csv` | 5 | `5503bf8bd7e7034b63a07c6a0e7b22ca7acf9988a2d4b67de323d25a942ed63c` |
| `representation-audit.csv` | 19 | `9461154fc0172a4d3bf427a2e1f6818d4b78ef7b010c85e962dc4760d034702a` |
| `published-tract-group-rates.csv.gz` | 30,343 | `1bb68ab0ed13f2f49df41bdc5e84c622c6a4b645ec8611ad54548accb81fe2d0` |
| `complementary-suppression-audit.csv` | 4,791 | `0b47dc885d478d1485ba9a130ba4635b9daba836ff63c94a50ffb39e77a0f3ec` |
| `bias-register.csv` | 8 | `3b06a50c0246d6a4118923d90eb8f70812f2eae81bf59425a86b630450ebf59e` |
| `query-checks.csv` | 36 | `6ce2bbd7980f5ebe1f5222f46625e2ccfbb9ec445a08e44737b5a51bb099e426` |

`outputs/build-report.json` pins every output's rows, columns, bytes, content hash, compressed hash, source findings, SQL hashes, and interpretation boundary.

The reference responsible claim uses the largest predeclared-reference contrast, the generated disability-status margin:

- Reported disability standardized rate: 6,778.90 per 100,000.
- No reported disability standardized rate: 4,606.05 per 100,000.
- Generated rate difference: 2,172.85 per 100,000.
- Generated rate ratio: 1.4717.

The instructor must lead with the generator boundary. The result is useful because it lets learners practice a complete method, not because it describes Massachusetts.

## 19. Validation and protected failure routes

`validate_workspace.py` performs 431 complete checks and 332 starter checks. It verifies:

- exact file sets and workspace counts;
- semantic versions and release identities;
- every immutable path, byte count, and SHA-256;
- the complete nested Module 02 handoff;
- source rows, flags, dimensions, groups, and totals;
- all learner records and SQL files;
- measure and sensitivity schemas;
- score and gate arithmetic;
- reference choices and exact summary results;
- missingness, conditioned geography, representation, and bias language;
- suppression counts, blank values, and missing totals;
- claim and progression authority;
- all committed output hashes;
- all 36 SQL checks and 12 source reconciliations;
- independent Python reproduction; and
- byte-identical regenerated outputs.

Complete validation passes 431 checks, and starter validation passes 332 checks.

The self-check rejects a copied reference answer in starter mode, rejects a starter in complete mode, and rejects 17 protected failure routes:

1. upstream mutation;
2. synthetic source mutation;
3. missing learner record;
4. unresolved placeholder;
5. changed SQL;
6. bad score;
7. failed gate;
8. changed reference result;
9. missing interval;
10. hidden conditioned missingness;
11. a suppressed blank relabeled as zero;
12. a tract total that makes suppression reconstructable;
13. an intersectional claim from separate margins;
14. a real Massachusetts disparity claim;
15. tract-ranking authority;
16. implementation authority; and
17. a personal absolute path.

The handoff, generator, calculation, and workspace builders each refuse unsafe or nonempty targets and prove deterministic reproduction.

## 20. Accessibility, equity, privacy, AI, versioning, and review

Every table uses explicit words for availability and suppression. Meaning does not depend on color. Exact-value CSV alternatives accompany any later display. Group labels remain in the output when a value is withheld, so absence is not mistaken for a nonexistent group.

Equity requirements include:

- retain missing groups;
- do not merge a group after results are inspected;
- do not treat a reference as a norm;
- state absolute and relative measures together;
- name the outcome direction;
- keep the selected and excluded analytic universes visible;
- prohibit cross-margin and intersectional inference;
- separate category labels from biological claims;
- assign group-contract, language-access, disability, and community review owners; and
- allow a reviewer to narrow, refer, or stop the claim.

Privacy requirements include primary and complementary suppression, blank protected values, no revealing totals, no imputation, and no claim that an open synthetic repository protects confidential real records.

The AI record names the agent, role, public and synthetic data shared, human owner, verification, corrections, and lack of authority. No protected, identifiable, restricted, or live operational data enter the release.

The module begins at version `0.1.0`. The Commons advances from `0.88.0` to `0.89.0` because this adds a complete runnable curriculum unit, new synthetic release, accepted outputs, workspaces, assessment, and validation.

Before alpha, named faculty, population-health clinical, epidemiology, biostatistics, equity, community, privacy, race and ethnicity standards, language-access, disability, accessibility, responsible-AI, and independent-reproduction reviewers must confirm the release.

## 21. Progression decision and Week 3 checkpoint handoff

The reference progression is `continue with conditions`.

Permitted next step:

- construct the cumulative 40-point Week 3 checkpoint from the exact accepted Module 01 through Module 03 packages;
- count the Module 02 20-point score and Module 03 20-point score once;
- preserve every inherited gate, condition, unavailable state, source identity, group contract, reference, missingness result, bias record, suppression state, claim, and AI record; and
- decide whether the frozen technical package can enter place-based evidence work.

Not yet permitted:

- Module 04 curriculum construction before checkpoint acceptance.

Still prohibited:

- a real disparity or intersectional claim;
- mapping or tract ranking;
- eligibility, targeting, or allocation;
- model fitting or intervention-effect estimation;
- real community action;
- implementation; and
- deployment.

Ten open conditions assign review of the group contract, language and disability labels, generator, reference choices, intervals, missingness, bias register, suppression, independent reproduction, and checkpoint assembly.

The Week 3 checkpoint must freeze the complete evidence. It cannot recompute a source, choose a more convenient reference, turn a blank into zero, recover a suppressed cell, or reinterpret a generator output as a real community fact.
