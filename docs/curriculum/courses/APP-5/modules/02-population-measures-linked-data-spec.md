# APP-5 Module 02: Population measures from linked data

## 1. Module identity, decision, and release boundary

- Module ID: `oclc-app5-02`.
- Course: APP-5, Data for Population Health and Equity.
- Instructional week: 2.
- Student effort: 16.0 hours.
- Submission: 20-point population measure and denominator build.
- Module version: `0.1.0`.
- Commons release: `0.88.0`.
- Package: `courses/population-health-equity/modules/02-population-measures-linked-data/`.
- Continuing case: `FMA-DP-01`.
- Decision: are the linked population, age groups, numerator, denominators, crude rates, age-specific rates, and standardization results correct and supported enough to begin disparity analysis?
- Primary decision owner: fictional `FMA-DP-01 population-health planning team`.
- Progression options: `continue`, `continue with conditions`, `revise`, or `refer`.

Module 02 turns the accepted Module 01 population and source contract into executable measures. It preserves the complete public-source union, builds five adult age-band denominators from ACS B01001, links one deterministic synthetic numerator, calculates rates, and makes every unavailable or small-support state visible.

This is a population-measure release. It does not decide whether a disparity exists, interpret geographic pattern, rank a tract, select a target, allocate resources, fit a model, estimate an intervention effect, or authorize action.

## 2. Place in the course and prerequisite handoff

Module 01 accepted a fictional Massachusetts adult diabetes-prevention planning review and permitted Module 02 curriculum construction with conditions. Module 02 must not reopen the population, geography, public-source identities, community rights, or claim boundary simply to obtain cleaner results.

### Required Module 01 identity

- Module ID: `oclc-app5-01`.
- Module version: `0.1.0`.
- Commons release: `0.87.0`.
- Reference workspace files: `27`.
- Immutable manifest rows: `16`.
- Public field inventory rows: `282`.
- PLACES rows: `1,597`.
- ACS rows: `1,620`.
- SVI rows: `1,613`.
- Three-source intersection: `1,597` tracts.
- Three-source union: `1,620` tracts.
- Progression: `continue with conditions`.
- Module 02 permission: `permitted for curriculum construction`.

### Frozen handoff

`freeze_upstream.py` builds and validates the complete Module 01 reference workspace before copying it to `upstream/module01-reference/`. It also copies the accepted Module 01 release record and writes a manifest over all 28 payload files.

The Module 02 upstream package has:

- 27 reference-workspace files;
- one Module 01 release record;
- one 28-row handoff manifest;
- 29 total upstream files;
- a 4,262-byte handoff manifest; and
- handoff manifest SHA-256 `beda2254d019c0969c952773b31fb23db30e2be99798aa8af66d5cb1fbd87a2e`.

A changed, missing, added, renamed, or reordered handoff file fails validation. Module 02 may extend the evidence chain, but it may not repair accepted Module 01 work silently.

## 3. Learning outcomes

By the end of the module, learners can:

1. reconcile a complete public-source union without silently dropping unmatched geographic units;
2. construct mutually exclusive adult age-band denominators from a declared ACS table crosswalk;
3. keep each ACS estimate paired with its published margin of error;
4. approximate margins for sums while explaining the covariance limit;
5. distinguish the PLACES adult population field from an ACS-derived adult denominator;
6. define a synthetic numerator with an exact period, population, geography, and claim limit;
7. link one numerator row to one compatible denominator row;
8. calculate crude and age-specific rates with an explicit multiplier;
9. calculate and interpret Wilson intervals for generated proportions;
10. declare one common standard age distribution;
11. calculate a directly standardized rate as a weighted average of age-specific rates;
12. preserve an unavailable direct rate when any required age-specific rate is unavailable;
13. calculate expected synthetic events with the indirect method;
14. calculate a standardized event ratio and explain why it is not a directly comparable rate;
15. identify small-support results without ranking, suppressing, or targeting early;
16. keep public modeled prevalence separate from synthetic event measures;
17. execute the accepted SQL and reproduce it independently with Python;
18. document source, formula, interval, support, and interpretation limits for each measure; and
19. issue a bounded progression decision for Module 03.

## 4. Concept ownership and protected boundaries

### Module 02 owns

- tract-key source reconciliation;
- adult age-band construction from B01001;
- estimate and margin pairing;
- approximate margin calculation for sums;
- synthetic numerator generation and identity;
- numerator-denominator linkage;
- crude and age-specific synthetic rates;
- Wilson intervals for generated proportions;
- one declared direct-standardization population;
- standard weights and weight reconciliation;
- directly standardized synthetic rates;
- indirect expected synthetic events;
- standardized event ratios;
- zero-denominator and small-support states;
- public-synthetic evidence separation;
- 20-point measure scoring;
- noncompensable measure gates; and
- permission for Module 03 curriculum construction.

### Module 02 extends rather than repeats

- FND-1 joins and descriptive summaries by applying them to population denominators and geographic source coverage;
- FND-2 rate and uncertainty work by binding each formula to a population-health claim limit;
- DA-730 comparison and uncertainty principles by producing accessible, auditable tables rather than teaching chart selection again; and
- Module 01 source roles by turning the accepted feasibility record into executable measures.

### Out of scope

- disparity measures;
- reference-group selection;
- disparity conclusions;
- missing equity-field analysis;
- small-number suppression;
- residual disclosure analysis;
- maps or spatial joins;
- ecological interpretation;
- tract ranking;
- targeting or allocation rules;
- intervention choice;
- model fitting;
- causal or intervention-effect estimation;
- real community claims;
- implementation; and
- deployment.

Module 03 owns disparity measures, reference sensitivity, missing equity fields, support rules, suppression, bias analysis, and the Week 3 checkpoint. Later modules own place, targeting, intervention, machine learning, and clinician leadership.

## 5. Continuing evidence thread and source authority

The module uses three frozen public tabular releases and one generated source.

### CDC PLACES

The accepted PLACES extract contains every Massachusetts 2025 release row with `measureid=DIABETES`: 1,597 rows and 24 fields. It preserves the 2023 modeled crude prevalence value, modeled 95 percent interval, tract identity, county identity, total population field, and adult population field.

Official metadata:

https://data.cdc.gov/api/views/cwsq-ngmh

Official methodology:

https://www.cdc.gov/places/methodology/index.html

PLACES remains a modeled small-area prevalence source. It is not an observed diagnosis file, event count, intervention evaluation, or local validation source.

### American Community Survey

The accepted 2020-2024 ACS five-year B01001 tract release contains 1,620 Massachusetts rows and 100 fields. B01001 has the universe `total population`. Module 02 uses the adult male estimate cells 007 through 025 and adult female estimate cells 031 through 049 with their paired margin fields.

Official B01001 table:

https://data.census.gov/table/ACSDT5Y2024.B01001

Official 2024 ACS five-year variable definitions:

https://api.census.gov/data/2024/acs/acs5/groups/B01001.json

ACS supplies survey-derived area denominator estimates. It does not supply diabetes cases, synthetic planning events, individual records, intervention outcomes, or allocation authority.

### CDC/ATSDR SVI

The accepted SVI 2022 Massachusetts tract release contains 1,613 rows and 158 fields.

Official documentation:

https://atsdr.cdc.gov/place-health/php/svi/svi-data-documentation-download.html

Module 02 verifies SVI source presence and preserves it in the handoff. SVI values do not generate the synthetic numerator and do not determine a rate, priority, target, eligibility rule, or funding decision in this module.

### Synthetic planning-need events

The generated release contains one row per accepted tract, adult age band, and fictional period. The numerator exists only to teach rate construction. It is not a diabetes diagnosis, PLACES case, patient record, eligibility result, local program observation, intervention outcome, or community preference.

## 6. Synthetic source release contract

| Item | Accepted value |
|---|---|
| Release | `fma-dp-01-measures-v1` |
| Generator | `generate_synthetic_events.py` |
| Generator version | `0.1.0` |
| Seed | `73052` |
| Case | `FMA-DP-01` |
| Period | fictional calendar year 2024 |
| Tracts | 1,597 |
| Age bands | 5 |
| Rows | 7,985 |
| Adult denominator total | 5,679,768 |
| Synthetic event total | 283,614 |
| Zero age-band denominators | 41 |
| Synthetic flag | 1 on every event row |

The generator uses the accepted ACS age-band denominator structure, fixed teaching probabilities by age, and one seeded fictional tract effect between minus 0.0125 and plus 0.0125. It then generates a deterministic binomial count for each tract-age row.

The fixed age probabilities are:

| Age band | Base probability |
|---|---:|
| 18-34 | 0.018 |
| 35-49 | 0.035 |
| 50-64 | 0.065 |
| 65-74 | 0.085 |
| 75+ | 0.100 |

PLACES prevalence and SVI values are excluded generation inputs. Public data inform the accepted population structure and source identity, not a fictional tract's event probability.

### Pinned generated files

| File | Bytes | SHA-256 |
|---|---:|---|
| `data/raw/synthetic-events.csv.gz` | 113,029 | `56f04f4e660e40292351cc0ed630b8cbb2f2c0d9cf9c39fbc8420b2113d813cb` |
| `data/age-band-crosswalk.csv` | 2,456 | `16cf59b15747375088bdd7f77e380a0b17b5d6f8f4dbb5ee1fe3e2d234646e20` |
| `data/data-dictionary.csv` | 5,053 | `66a42e357d190f85e69b3774d7b50cecb6131573398ea6615bed15f33cd93e59` |
| `data/synthetic-source-manifest.csv` | 778 | `9915aeb15f62d88a52cfa6304d211a4fd092d33c11e73cd5d63a14d64946823d` |

A refresh requires a new source release, review of every downstream result, and a semantic-version decision.

## 7. Authoritative readings and methods

Learners use official sources for field definitions and method limits.

1. ACS B01001, Sex by Age: https://data.census.gov/table/ACSDT5Y2024.B01001
2. ACS 2024 five-year B01001 variables: https://api.census.gov/data/2024/acs/acs5/groups/B01001.json
3. Census Bureau training on ACS estimates and margins of error: https://www.census.gov/content/dam/Census/programs-surveys/acs/guidance/training-presentations/20180418_MOE_Webinar_Transcript.pdf
4. CDC/NCHS age-adjustment definition and direct formula: https://www.cdc.gov/nchs/hus/sources-definitions/age-adjustment.htm
5. CDC discussion of crude, direct, and indirect small-area rates: https://www.cdc.gov/pcd/issues/2010/jan/09_0054.htm
6. CDC PLACES methodology: https://www.cdc.gov/places/methodology/index.html
7. CDC/ATSDR SVI documentation: https://atsdr.cdc.gov/place-health/php/svi/svi-data-documentation-download.html

The Census guidance explains that the root-sum-of-squares method approximates a margin for a sum and does not include covariance. It also recommends special handling when several component estimates equal zero.

CDC defines a directly adjusted rate as a weighted sum of population-specific age rates under a declared standard distribution. CDC also notes that adjusted rates are relative indexes rather than actual risk measures. The indirect method applies stable standard age-specific rates to a local age distribution to calculate expected cases or events. Indirect results do not support direct cross-area comparisons in the same way as a common-standard direct rate.

The course applies these methods to a synthetic numerator. Clinical or policy authority does not transfer from a method page to the teaching output.

## 8. Workload and learning sequence

| Sequence | Activity | Hours | Required evidence |
|---:|---|---:|---|
| 1 | Verify the Module 01 handoff | 1.0 | Passing 29-file upstream verification |
| 2 | Reconcile the complete tract union | 0.5 | 1,620-row linkage audit |
| 3 | Trace the B01001 adult age cells | 1.5 | 38-row crosswalk and five age bands |
| 4 | Construct age-band denominators and margins | 1.5 | 7,985 denominator rows and total reconciliation |
| 5 | Inspect the generated numerator and claim boundary | 1.0 | Pinned source identity and public-synthetic separation |
| 6 | Link numerator and denominator | 1.0 | 7,985 one-to-one linked rows and zero mismatches |
| 7 | Calculate crude and age-specific rates | 2.0 | Rate table, multiplier, intervals, and unavailable states |
| 8 | Build the common standard population | 1.0 | Five weights totaling one |
| 9 | Calculate direct standardized rates | 1.5 | 1,576 results and 21 unavailable states |
| 10 | Complete guided indirect standardization | 1.5 | 1,597 expected-count and ratio rows |
| 11 | Interpret support and evidence limits | 1.0 | Standardization and source-separation memos |
| 12 | Run independent checks and repair work | 1.5 | Thirty passing SQL checks and Python reproduction |
| 13 | Score, resolve gates, disclose AI use, and record progression | 1.0 | 20-point score, 15 gates, and Module 03 handoff |
| Total |  | 16.0 |  |

The sequence keeps calculation and interpretation together. Learners do not generate dozens of rates first and add denominator or claim limits afterward.

## 9. SQL and Python execution contract

SQL is the primary measure-construction language. Four ordered files create the accepted tables:

1. `01-link-sources-and-build-denominators.sql` creates the complete union audit and five adult age-band denominators.
2. `02-link-events-and-separate-public-measure.sql` links the generated numerator and creates a separate PLACES modeled-prevalence table.
3. `03-calculate-rates-and-direct-standardization.sql` creates the standard population, age-specific rates, crude rates, and direct rates.
4. `04-indirect-standardization-and-validation.sql` creates expected synthetic events, standardized event ratios, source reconciliation, and exact checks.

`build_measures.py` loads the frozen releases into a temporary SQLite database. It normalizes the 38 B01001 crosswalk cells into 61,560 tract-cell rows, executes the four SQL files, exports ten tables, and independently recalculates all 7,985 age-specific results and all 1,597 tract summaries in Python.

The build fails when:

- a SQL file is missing or contains `REPLACE`;
- a source row width changes;
- a B01001 crosswalk field is missing;
- a generated count is negative or exceeds its denominator;
- any exact SQL check fails;
- Python disagrees with SQL outside the declared tolerance;
- a public and synthetic measure schema is blended; or
- the output target is already nonempty.

No database file is committed. The build uses a temporary SQLite database and writes only the declared outputs.

## 10. Population, age-band, and denominator contract

The measure population is adults age 18 and older in the 1,597 tracts present in PLACES, ACS, and SVI. The 1,620-row source union remains visible even though only the complete intersection enters the measure build.

### Five adult age bands

| Age band | Male B01001 cells | Female B01001 cells | Total source cells |
|---|---|---|---:|
| 18-34 | E007-E012 | E031-E036 | 12 |
| 35-49 | E013-E015 | E037-E039 | 6 |
| 50-64 | E016-E019 | E040-E043 | 8 |
| 65-74 | E020-E022 | E044-E046 | 6 |
| 75+ | E023-E025 | E047-E049 | 6 |
| Total | 19 cells | 19 cells | 38 |

Every estimate cell has a paired `M` margin field. The crosswalk includes source labels, sex branches, field names, age-band IDs, and calculation order.

### Denominator invariants

- Every eligible tract has five denominator rows.
- The denominator table has 7,985 rows.
- The five age bands are mutually exclusive.
- The band total equals the derived adult total for each tract.
- The complete adult denominator total is 5,679,768.
- Negative estimates are prohibited.
- Forty-one tract-age denominators equal zero.
- A zero denominator produces an unavailable rate, not a zero rate.
- The ACS denominator is not replaced with PLACES `totalpop18plus`.

## 11. ACS margin and interval contract

For an age-band sum with component estimates `E_i` and margins `M_i`, the accepted approximate 90 percent margin is:

```text
sqrt(sum(M_i^2 for E_i != 0) + max(M_i^2 for E_i == 0))
```

The maximum zero-estimate term is zero when no component estimate equals zero. This prevents several zero-estimate margins from being counted together in the approximation.

The output records:

- denominator estimate;
- approximate 90 percent margin;
- source-cell count;
- zero-source-cell count;
- denominator source;
- source period;
- geography;
- margin method; and
- the covariance limit.

The ACS margin does not measure uncertainty in the generated event count. The generated rate uses a Wilson 95 percent interval for the synthetic event proportion:

```text
p = x / n
center = (p + z^2 / (2n)) / (1 + z^2 / n)
half = z * sqrt((p(1-p) + z^2 / (4n)) / n) / (1 + z^2 / n)
```

with `z=1.959963984540054`. The bounds are multiplied by 100,000. The two uncertainty records stay separate because they describe different constructions.

## 12. Crude and age-specific rate contract

The rate multiplier is 100,000 throughout Module 02.

### Age-specific rate

```text
age-specific rate = synthetic event count / ACS age-band denominator * 100,000
```

Each row preserves:

- tract;
- age-band ID and label;
- period;
- synthetic event count;
- denominator estimate and approximate margin;
- multiplier;
- rate and Wilson interval;
- availability state;
- support state;
- measure definition; and
- claim limit.

Of 7,985 rows, 7,944 have a positive denominator and an available rate. Forty-one remain unavailable because the denominator is zero.

### Crude rate

```text
crude rate = sum of five synthetic event counts / sum of five ACS age-band denominators * 100,000
```

The crude rate preserves the tract's age composition. It may differ from the direct rate because the direct result applies one common age distribution.

Neither rate is an observed diabetes rate. Both use the generated planning-need numerator.

## 13. Direct standardization contract

The direct standard is the complete ACS adult population across all 1,597 matched tracts.

| Age band | Standard population | Weight | Statewide synthetic events | Synthetic rate per 100,000 |
|---|---:|---:|---:|---:|
| 18-34 | 1,681,962 | 0.2961321660 | 30,524 | 1,814.78535187 |
| 35-49 | 1,330,444 | 0.2342426662 | 46,481 | 3,493.64573030 |
| 50-64 | 1,409,112 | 0.2480932320 | 91,534 | 6,495.86406191 |
| 65-74 | 739,218 | 0.1301493300 | 62,984 | 8,520.35529438 |
| 75+ | 519,032 | 0.0913826058 | 52,091 | 10,036.18274018 |

The five weights total `1.0000000000`.

For tract `j`:

```text
direct rate_j = sum(age-specific rate_ij * standard weight_i)
```

The interval uses the weighted binomial variance:

```text
variance_j = sum(weight_i^2 * p_ij * (1 - p_ij) / n_ij)
bound = direct proportion_j +/- 1.96 * sqrt(variance_j)
```

The output clips bounds to zero and 100,000 after applying the multiplier.

Direct results are available for 1,576 tracts. Twenty-one tracts have at least one zero age-band denominator and keep an unavailable direct result. A partial weighted sum is not accepted as a complete direct rate.

The direct result is a relative teaching index under the declared standard age distribution. It is not the tract's actual risk, event burden, need, or priority.

## 14. Guided indirect standardization contract

The indirect method uses the five complete statewide synthetic age-specific rates in the standard-population table.

For tract `j` and age band `i`:

```text
expected synthetic events_ij = tract denominator_ij * statewide synthetic rate_i / 100,000
```

The tract expectation sums the five age-specific expectations:

```text
expected synthetic events_j = sum(expected synthetic events_ij)
standardized event ratio_j = synthetic event count_j / expected synthetic events_j
```

All 1,597 expected values are positive, so all 1,597 standardized event ratios are available. The interval uses a transparent log approximation for positive counts. A zero-count row would use zero as the lower bound and `-log(0.05) / expected` as the upper bound.

Eighty tracts have at least one age-band denominator below 50 and must complete the guided indirect exercise. Other tracts may use it as a secondary method check.

The indirect ratio uses each tract's own age distribution in its expected count. It therefore is not directly comparable across tracts as though it were a rate under common standard weights. It is not a real excess-case statement, disparity measure, ranking variable, targeting score, or allocation rule.

## 15. Required learner deliverables

The learner workspace contains 61 files. It includes all immutable controls, the generated source, the complete frozen handoff, four SQL templates, ten assessed records, and a 46-row manifest. It contains no accepted answer outputs.

Learners complete:

1. `sql/01-link-sources-and-build-denominators.sql`;
2. `sql/02-link-events-and-separate-public-measure.sql`;
3. `sql/03-calculate-rates-and-direct-standardization.sql`;
4. `sql/04-indirect-standardization-and-validation.sql`;
5. `population-measure-specifications.csv` with nine ordered measure definitions;
6. `age-band-and-moe-method.md`;
7. `linkage-and-denominator-audit.md`;
8. `standardization-interpretation.md`;
9. `public-synthetic-separation.md`;
10. `measure-score.csv`;
11. `gate-results.csv`;
12. `progression-decision.md`;
13. `reproducibility-check.md`; and
14. `ai-use.md`.

The ten assessed records are editable. The four SQL files are also assessed. Source files, controls, and upstream files are immutable.

The submission is incomplete when any `REPLACE`, `TODO`, or `TBD` marker remains, an expected record is missing, a schema changes, an ID is reordered, a formula cannot run, or the manifest identity changes.

## 16. Assessment, score, and noncompensable gates

### Twenty-point rubric

| Criterion | Points |
|---|---:|
| Population, age-band, numerator, denominator, and linkage logic | 4 |
| Crude and age-specific rates | 4 |
| Direct and indirect standardization | 4 |
| Uncertainty, support, and evidence separation | 4 |
| Reproducibility, interpretation, and handoff | 4 |
| Total | 20 |

### Fifteen gates

1. The complete Module 01 handoff reproduces.
2. The public-source union and intersection remain complete.
3. All 38 B01001 source cells and five age bands are declared.
4. Every ACS estimate remains paired with its margin.
5. The synthetic release and all 7,985 rows reproduce.
6. Every synthetic row matches one derived denominator.
7. Counts and denominators conserve without hidden drops.
8. Crude and age-specific rates use the declared multiplier and unavailable states.
9. Direct standard weights are complete and total one.
10. Direct rates never convert a zero denominator to a zero rate.
11. Indirect expected counts and ratios reproduce.
12. PLACES modeled prevalence remains separate from synthetic events.
13. SQL and independent Python results match.
14. No observed-case, disparity, ranking, targeting, or allocation claim appears.
15. Progression and real-world authority remain bounded.

All gates are noncompensable. A 20-point arithmetic score does not pass the module when one gate fails.

The reference scores 20 of 20 and passes all 15 gates.

## 17. Reference package and instructor key

The reference workspace contains 72 files:

- 57 immutable manifest rows;
- 29 frozen upstream files;
- four generated-source files;
- 13 module control files;
- 11 accepted output files, including the build report;
- four accepted SQL files;
- ten completed assessed records; and
- one release manifest.

### Exact reference findings

- 1,620 union tracts.
- 1,597 measure tracts.
- Sixteen ACS and SVI tracts without PLACES.
- Seven ACS-only tracts.
- 61,560 normalized ACS tract-cell rows.
- 7,985 denominator rows.
- 7,985 generated event rows.
- 5,679,768 denominator units.
- 283,614 generated events.
- Forty-one zero age-band denominators.
- 7,944 available age-specific rates.
- 1,576 available direct rates.
- Twenty-one unavailable direct rates.
- Eighty guided indirect cases.
- Five standard rows.
- Thirty passing query checks.
- Eight passing source-reconciliation checks.
- Zero failed checks.

The instructor key must distinguish a technically valid calculation from an authorized interpretation. A result can reproduce and still be too weak or too synthetic for a real claim.

## 18. Validation and protected failure routes

The package leaves four runnable checks:

```powershell
python .\freeze_upstream.py --self-check
python .\generate_synthetic_events.py --self-check
python .\build_measures.py --self-check
python .\build_workspace.py --self-check
python .\validate_workspace.py --self-check
```

The checks verify:

- two handoff freezes match;
- two synthetic source builds match;
- two measure builds match;
- two reference workspace manifests match;
- every committed generated file has the pinned identity;
- every committed output has the build-report identity;
- SQL and Python agree;
- complete reference validation passes 266 checks;
- starter validation passes 187 checks;
- a copied answer fails starter mode;
- an incomplete starter fails complete mode; and
- twelve protected failure routes are rejected.

The twelve failure routes are:

1. upstream source mutation;
2. generated source mutation;
3. missing assessed file;
4. placeholder in complete work;
5. changed SQL expectation;
6. incorrect score;
7. invalid progression;
8. public-synthetic blending;
9. unsupported observed-case claim;
10. tract-ranking authority;
11. targeting or allocation authority; and
12. personal local path disclosure.

The validator rejects the first failing boundary. It does not repair work or infer an intended answer.

## 19. Accessibility, equity, privacy, and AI requirements

### Accessibility

- Every output is a machine-readable CSV, deterministic gzip CSV, JSON, Markdown, Python, SQL, or YAML file.
- Tables keep explicit headers and exact-value alternatives.
- Availability and support states use words rather than color.
- Age bands use readable labels and stable IDs.
- Instructions expose complete file paths and commands.
- The learner can inspect all formulas without proprietary software.

### Equity and community accountability

Module 02 treats a denominator as a claim about who is represented. It preserves source mismatches, zero denominators, small supports, and source vintages. It does not turn a technical difference into a disparity or inequity conclusion.

The Module 01 community rights remain frozen. Residents and community organizations retain rights to question framing, add local knowledge, contest burdens, require revision, and stop progression toward real community action. Module 02 does not simulate consent or claim community endorsement.

### Privacy

The public sources are aggregate tract releases. The synthetic source is aggregate and contains no individual record. Protected, identifiable, restricted, or live operational data are prohibited.

Tract-level public data still require responsible use. A public row does not authorize stigmatizing language, individual inference, outreach, eligibility, or funding decisions.

### AI use

Learners disclose AI assistance, the files or text shared, protected-data status, human checks, corrections, and final accountability. An agent has no authority over the numerator, denominator, standard population, formula, result, unavailable state, disparity, ranking, targeting, allocation, intervention, progression, or final decision.

## 20. Release, versioning, and human review

- Module version: `0.1.0`.
- Commons release: `0.88.0`.
- Release status: runnable release candidate.
- Semantic-version decision: Commons advances from `0.87.0` to `0.88.0` because a new runnable module, synthetic source, measure pipeline, assessment, and durable handoff are added without changing the master architecture.

### Package identities

- Upstream handoff manifest SHA-256: `beda2254d019c0969c952773b31fb23db30e2be99798aa8af66d5cb1fbd87a2e`.
- Synthetic source manifest SHA-256: `9915aeb15f62d88a52cfa6304d211a4fd092d33c11e73cd5d63a14d64946823d`.
- Age-band denominator output SHA-256: `6e0c632132b65e9322f098ccba3c2ce70ca8151f4ee8f536862f635ac23eef1f`.
- Age-specific rate output SHA-256: `54523baa1c7ba1a73a8dc5136172f6c8f7b363fd1d91f65bbebd85e1feb70791`.
- Tract summary output SHA-256: `1d557e5de780aa5bb4d5f7928086f012ddfa9a652dcd386e6b42702475b25d47`.
- Indirect output SHA-256: `61d66043d24047d50cc8daad4820ed709666a612c4fdc5d7f888ebe93773b5f8`.

Before alpha, named reviewers must examine:

- faculty scope and assessment;
- population-health clinical meaning;
- epidemiologic rate and standardization methods;
- biostatistical interval and support rules;
- ACS field routing and margin approximation;
- PLACES estimate interpretation;
- SVI source role;
- synthetic numerator wording and generation;
- community and equity consequences;
- privacy and tract-level disclosure;
- accessibility;
- responsible AI; and
- independent reproduction.

The official course section and half-term dates remain a program scheduling decision.

## 21. Progression decision and Module 03 handoff

The reference progression is `continue with conditions`. Module 03 curriculum construction is permitted.

Module 03 must freeze:

- the complete 72-file Module 02 reference workspace;
- the 57-row Module 02 immutable manifest;
- all 29 Module 01 upstream files;
- all four generated-source files;
- all ten measure output tables and the build report;
- the 20-point score;
- all 15 gate results;
- the public-synthetic evidence boundary;
- all unavailable and small-support states; and
- the eight open conditions.

### Eight owned conditions

1. Epidemiology and ACS reviewers must confirm the five age bands and 38-cell routing.
2. A population-health clinical reviewer must confirm the synthetic planning-need numerator wording and age probabilities.
3. A biostatistics reviewer must confirm the ACS margin approximation and covariance disclosure.
4. A biostatistics reviewer must confirm the direct standard and interval method.
5. An epidemiology reviewer must confirm the indirect method and cross-tract comparison limit.
6. Equity, community, and privacy reviewers must define Module 03 group, missingness, and protection rules.
7. Biostatistics and privacy reviewers must define deterministic suppression and non-reconstruction rules.
8. An independent reproducer must verify every source and output identity before alpha.

Module 03 may build rate differences, rate ratios, summary disparity measures, reference sensitivity, missing equity-field audits, bias analysis, uncertainty, support, and suppression. It may not rewrite an accepted Module 02 result silently.

Disparity claims, mapping, tract ranking, targeting or allocation, model fitting, intervention-effect estimation, real community action, implementation, and deployment remain prohibited at the Module 02 handoff.
