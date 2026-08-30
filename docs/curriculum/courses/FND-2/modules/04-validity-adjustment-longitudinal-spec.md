# FND-2 Module 04: Adjustment, missing data, and longitudinal structure

## 1. Module identity and place in the course

### Release identity

- Course: FND-2, Modeling, Inference, and Reproducible Analytics.
- Module: 04 of 07.
- Module ID: `oclc-fnd2-04`.
- Module version: 0.1.0.
- Commons release target: 0.43.0.
- Source week: 4.
- Learner work: 16.5 hours.
- Week 6 share: 15 of 25 points.
- Package: `courses/modeling-inference-reproducible-analytics/modules/04-validity-adjustment-longitudinal/`.
- Data boundary: accepted Synthea evidence plus deterministic synthetic fixtures.
- Clinical use: prohibited.

### Purpose

Module 04 shows why clean data and correctly executed code are not enough. A model can still answer the wrong question because the design conditions on a selected group, adjusts for the wrong variables, handles missing values under an unsupported assumption, treats repeated observations as independent, or ignores censoring.

The learner moves from "did the code run?" to "what claim can this design support?"

### Relationship to Checkpoint 1

Checkpoint 1 version 0.1.0 is immutable input. Module 04 preserves:

- the 374-row cohort;
- 224/75/75 split;
- 25/7/4 outcomes;
- training-prevalence baseline;
- regression formulas and conditions;
- `ML01` selection;
- threshold 0.08513264;
- 48/23/2/2 test confusion counts;
- sparse subgroup evidence; and
- teaching-only use.

Module 04 adds validity evidence. It does not rewrite the checkpoint result.

### Relationship to Module 05

Module 05 receives the accepted validity-threat register, claim limits, specialist referrals, and testing implications. Its public time-series forecast is a distinct analytic case and must not reuse the row-level prediction split as a forecast split.

### Required starting state

- Checkpoint 1 disposition permits Module 04.
- Checkpoint release and contract match exact fingerprints.
- Module 01 modeling cohort is unchanged.
- Module 02 111-row conditional timing subset is unchanged.
- Module 03 model and test evidence are unchanged.
- No learner has converted structural blanks to zero.

### Required ending state

The learner releases:

- an analytic-aim validity map;
- editable and accessible DAG evidence;
- role and adjustment registers;
- a causal-claim screen;
- overlap and balance evidence;
- missingness and sensitivity evidence;
- selection evidence;
- repeated-measures and mixed-model reading;
- survival and censoring reading;
- 12-threat register;
- specialist referral and stop decisions;
- a validity memo;
- reproducibility, accessibility, and AI-use records; and
- an explicit Module 05 disposition.

## 2. Decision, owner, audience, and dispositions

### Decision owner

The decision owner is a biostatistical validity reviewer with clinical-informatics support. A causal-inference specialist, missing-data specialist, longitudinal-methods specialist, survival analyst, clinician, accessibility reviewer, privacy reviewer, responsible-AI reviewer, and instructor may be consulted.

### Decision

> Which validity threats change the claim, method, uncertainty, or model-use recommendation, and which require specialist referral or a stop decision?

### Allowed dispositions

| Disposition | Meaning | Module 05 |
|---|---|---|
| `continue` | Gates pass and limits are fully carried forward. | permitted |
| `continue with conditions` | Gates pass with explicit referrals or limits. | permitted |
| `revise` | Correctable design or explanation defect remains. | blocked |
| `refer` | Specialist review is needed before progression. | blocked unless referral resolved |
| `stop` | Requested claim or method is unsupported. | blocked for the affected claim |

### Reference disposition

The expected reference is `continue with conditions`. The prediction teaching workflow may continue as a prediction case, but no causal treatment effect, full-cohort time-to-event conclusion from the selected 111 rows, stable mixed-model claim, or clinical survival claim is permitted.

### Audiences

- learner conducting validity review;
- biostatistical reviewer;
- clinical informatician checking timing and selection;
- later forecasting learner;
- instructor reviewing referrals; and
- maintainer verifying immutable handoff evidence.

### What this decision does not approve

- treatment recommendations;
- real comparative effectiveness;
- transport to a clinical population;
- production imputation;
- patient-specific survival prediction;
- causal attribution;
- fairness; or
- deployment.

## 3. Foundation skill and claim hierarchy

### Foundation skill

The durable skill is to identify the design structure required by a claim, then either use a bounded appropriate method, narrow the claim, refer to a specialist, or stop.

### Claim hierarchy

| Claim | Minimum design question |
|---|---|
| Description | Who and what was observed? |
| Association | What variables and selected population condition the relationship? |
| Prediction | What is known at prediction time and how is future performance evaluated? |
| Causal effect | What intervention contrast, exchangeability assumptions, time ordering, and adjustment set apply? |
| Longitudinal change | What repeats within whom and how is dependence represented? |
| Survival | What is time zero, event, censoring, risk set, and competing structure? |

### Stop principle

When the requested claim requires information or assumptions absent from the design, the correct output may be a narrower claim or `stop`, not a more complex model.

### Prediction versus causation

The Module 03 feature set was chosen for prediction. It is not a causal adjustment set. A predictor can be a mediator, collider, proxy, or post-exposure variable and still improve prediction while biasing a causal contrast.

### Specialist boundary

This module teaches recognition and bounded reading. It does not certify independent causal inference, multiple imputation, mixed-model design, or survival modeling practice.

## 4. Assessable outcomes and evidence map

### Outcomes

The learner can:

1. classify 12 validity threats by design stage;
2. distinguish descriptive, predictive, and causal aims;
3. define a bounded causal contrast;
4. draw and narrate a DAG;
5. label exposure, outcome, confounder, mediator, collider, and selection roles;
6. choose an adjustment set from the DAG rather than prediction importance;
7. inspect propensity overlap;
8. read pre- and post-weighting balance;
9. state positivity limits;
10. identify selection in the 111-row timing subset;
11. profile observed missingness;
12. state MCAR, MAR, and MNAR as assumptions;
13. compare complete-case and bounded imputation sensitivity;
14. identify repeated units and clusters;
15. explain why independent-row uncertainty can be wrong;
16. read a random-intercept mixed-model output;
17. define time zero, event, and censoring;
18. read Kaplan-Meier and Cox teaching outputs;
19. distinguish censoring from ordinary missingness;
20. record a remedy, caveat, referral, or stop action; and
21. issue a Module 05 progression disposition.

### Evidence map

| Outcome group | Evidence |
|---|---|
| Aim and claim | analytic-aim map and causal screen |
| DAG | Mermaid source, SVG, nodes, edges, narrative |
| Adjustment | role register, propensity scores, overlap, balance, effect sensitivity |
| Selection | 111-versus-374 profile and selection memo |
| Missingness | field profile, mechanism assumptions, sensitivity table |
| Repeated structure | person-visit fixture, cluster register, naive and mixed outputs |
| Survival | person-level fixture, censoring record, KM and Cox reading outputs |
| Decision | threat register, memo, referrals, progression |
| Accountability | source, build, reproduction, access, and AI-use records |

### Minimum explanation

Every material threat explanation names:

- claim affected;
- design stage;
- observed evidence;
- untestable assumption;
- likely direction or nature of concern when defensible;
- remedy or boundary;
- specialist trigger; and
- progression effect.

## 5. Concept ownership and out-of-scope boundaries

### Module 04 owns

- causal-claim screening;
- basic DAG role reasoning;
- selection diagnosis;
- prediction versus causal adjustment distinction;
- propensity overlap and balance reading;
- missingness mechanism assumptions;
- bounded missing-data sensitivity;
- repeated-unit recognition;
- mixed-model output reading;
- censoring recognition;
- Kaplan-Meier and Cox output reading;
- validity-threat classification;
- specialist referral; and
- claim-narrowing decisions.

### Module 04 introduces but does not own

- formal causal identification;
- target-trial emulation;
- doubly robust estimation;
- multiple imputation pooling;
- generalized estimating equations;
- random-slope design;
- competing risks;
- time-dependent exposure;
- informative censoring adjustment;
- transportability; and
- sensitivity-analysis theory.

### Module 04 does not own

- new prediction model selection;
- new test evaluation;
- forecast methods;
- model monitoring;
- production data pipelines;
- real treatment comparisons;
- clinical recommendations; or
- deployment.

### No complexity theater

The module uses one bounded propensity example, one bounded missingness comparison, one random-intercept reading, one Kaplan-Meier summary, and one Cox reading. Additional methods are not added unless they change a teaching decision.

## 6. Lesson sequence and learner time

| Sequence | Activity | Hours | Evidence |
|---:|---|---:|---|
| 1 | Checkpoint handoff and claim screen | 1.0 | accepted-input audit |
| 2 | DAG roles and adjustment sets | 2.0 | nodes, edges, narrative |
| 3 | Confounded treatment fixture | 2.0 | unadjusted comparison |
| 4 | Propensity overlap and balance | 2.0 | overlap and SMD tables |
| 5 | Selection in the timing subset | 1.5 | 111-versus-374 evidence |
| 6 | Missingness mechanisms | 1.5 | profile and assumption record |
| 7 | Bounded imputation sensitivity | 1.5 | sensitivity table |
| 8 | Repeated measures and mixed model | 2.0 | naive and mixed reading |
| 9 | Survival and censoring | 1.5 | KM and Cox reading |
| 10 | Threat register, referrals, and memo | 1.5 | final decision package |
| Total |  | 16.5 | complete module |

### Within-module gates

- No causal model before the causal contrast and DAG are stated.
- No propensity estimate before field timing and roles are checked.
- No weighted result before overlap and balance are shown.
- No imputed result before a mechanism assumption is stated.
- No row-level regression on repeated data without naming the cluster.
- No survival summary before time zero, event, and censoring are defined.

## 7. Source and fixture architecture

### Accepted source evidence

The module fingerprints:

- Checkpoint 1 release and contract;
- Module 01 modeling cohort and split registry;
- Module 02 linear subset and assumption register;
- Module 03 model contract and progression decision.

### Fixture classes

| Fixture | Rows | Grain | Purpose |
|---|---:|---|---|
| Selection | 374 plus 111 selected rows | person | show conditioning on recorded next encounter |
| Treatment | 600 | synthetic person | confounding, overlap, balance, adjustment |
| Repeated | 2400 | synthetic person-visit | within-person dependence and mixed model |
| Survival | 600 | synthetic person | event, censoring, KM, Cox reading |

The executed reference freezes 255 treated people, 91 missing observed baseline-severity values, four visits for each of 600 people, 449 survival events, and 151 censored records. The treatment fixture fingerprint is `ea82788315dafab0921fd797623741d4ea850e92c3a65b634db32941833dd1c7`; the DAG SVG fingerprint is `47533b8d784ac8ef9cc2e2fa54ba587ef0af7a2e8e8feb4b701e027bb0f9bd74`.

### Synthetic treatment design

The treatment fixture exposes its data-generating process. Baseline age, severity, comorbidity count, and site affect treatment assignment. Baseline severity and comorbidity affect outcome. Treatment has a fixed beneficial potential-outcome shift. Shared noise creates paired potential outcomes available only for teaching audit.

### Why known potential outcomes are included

Real observational data never reveal both potential outcomes for one person. A synthetic fixture may retain them in an instructor audit table so learners can compare estimators with known truth without confusing estimated and observed effects.

### Missingness design

Observed severity is masked by a fixed rule depending on observed baseline characteristics. The reference treats MAR as a design assumption for the bounded primary exercise and adds low and high delta shifts as MNAR sensitivity. The true complete severity remains in an instructor-only audit field or protected reference output.

### Repeated design

Each synthetic person has four scheduled visits. Outcomes contain a person-specific random intercept, time trend, treatment-by-time component, and visit noise. The cluster is the person, not the row.

### Survival design

Each synthetic person has an event time and censoring time generated separately. Observed time is their minimum; event status records which occurred first. Time zero is treatment assignment in the synthetic fixture.

### Real-data boundary

No row represents a real person. Labels such as treatment, severity, symptom score, visit, and event are instructional variables, not clinical findings.

## 8. Analytic aims and causal-claim screen

### Aim map

`analytic-aim-validity-map.csv` includes:

- aim ID;
- question;
- aim class;
- unit;
- time zero;
- exposure or predictor;
- outcome;
- horizon;
- population;
- minimum assumptions;
- supported claim; and
- prohibited claim.

### Required aims

1. conditional linear timing description;
2. 90-day acute-return prediction;
3. synthetic treatment ATE;
4. repeated symptom-score change;
5. synthetic time-to-event comparison.

### Causal contrast

The synthetic treatment target is the average difference in 30-day symptom score under treatment versus no treatment in the 600-person fixture. Lower scores are better. The fixture contains known paired potential outcomes for audit, but learners estimate from the observed treatment and outcome.

### Causal screen questions

- Is exposure manipulable enough for the teaching contrast?
- Does exposure precede outcome?
- Is time zero common?
- Is the population explicit?
- Are confounders measured before exposure?
- Are mediators or post-outcome variables excluded from adjustment?
- Is positivity plausible?
- Is interference excluded by design?
- Is consistency stated?
- What unmeasured confounding remains possible?

### Screen outcome

The synthetic fixture supports a bounded method demonstration because its generator is known. It does not license a real treatment claim.

## 9. DAG and adjustment-set contract

### Required nodes

- age;
- baseline severity;
- comorbidity count;
- site;
- treatment;
- mediator or early response;
- 30-day outcome;
- selection into complete-case analysis; and
- unmeasured clinical preference.

### Required roles

| Role | Teaching examples |
|---|---|
| Exposure | treatment |
| Outcome | 30-day symptom score |
| Confounder | baseline severity, age, comorbidity, site |
| Mediator | early response |
| Collider | complete-case selection when caused by treatment and outcome-related factors |
| Unmeasured | clinician preference |

### Structured route

The DAG is represented by:

- `dag.mmd` editable Mermaid source;
- `dag.svg` accessible visual;
- `dag-nodes.csv`;
- `dag-edges.csv`; and
- `dag-narrative.md`.

### Adjustment set

The primary propensity example adjusts for age, baseline severity, comorbidity count, and site. It excludes the mediator, observed outcome, potential outcomes, missingness indicator caused after exposure, and any post-treatment field.

### Prediction-set comparison

The learner records why the Module 03 prediction set cannot be copied automatically. Fields are compared by timing and causal role, not predictive importance.

### DAG change rule

A changed node, edge, time ordering, exposure, outcome, population, or contrast requires a revised adjustment decision and version record.

## 10. Propensity, overlap, balance, and effect sensitivity

### Propensity model

The provided logistic propensity model estimates treatment probability from the four declared pre-exposure confounder families. It is a teaching nuisance model, not a clinical prediction model.

### Overlap evidence

Outputs include:

- treatment prevalence;
- minimum and maximum propensity by group;
- common support interval;
- counts outside support;
- ten score bins by treatment; and
- weight distribution and truncation.

### Weighting rule

The primary example uses ATE inverse probability weights with percentile truncation declared before outcome comparison. The exact truncation values and affected rows are recorded.

### Balance evidence

`balance-table.csv` reports for every encoded covariate:

- treated and untreated means before weighting;
- unweighted standardized mean difference;
- weighted treated and untreated means;
- weighted standardized mean difference; and
- absolute balance status under a declared 0.10 teaching threshold.

### Effect table

The package compares:

- known synthetic ATE;
- observed unadjusted mean difference;
- complete-case adjusted regression;
- propensity-weighted difference; and
- missingness sensitivity estimates.

### Interpretation boundary

Closer agreement with known synthetic truth demonstrates the fixture mechanics. It does not prove that propensity weighting removes unmeasured confounding in real data.

### Positivity boundary

Poor overlap triggers `refer` or target-population restriction. Weight truncation is reported as a design choice, not hidden cleanup.

## 11. Selection and structural-missingness case

### Selected timing subset

Module 02 contains 111 people with a recorded different encounter in 30 days. Only 69 are training rows. The remaining 263 cohort people have no recorded timing value.

### Selection question

The conditional linear model asks about timing among people with a recorded next encounter. It cannot estimate time to next encounter for all 374 people because most do not have an observed event in that window.

### Selection profile

The module compares selected and nonselected rows on:

- age;
- index class;
- prior encounters;
- prior acute encounters;
- prior conditions;
- prior medications;
- 90-day acute return; and
- follow-up completeness.

### Structural blank rule

Blank timing means no recorded different encounter within the defined window. Zero would mean an event at time zero. Conversion to zero invents an event and fails the module.

### Remedy

Options include:

- retain the conditional descriptive claim;
- use a survival framework with censoring for a broader time-to-event question;
- revise the follow-up window; or
- stop the full-cohort timing claim.

### No inverse-probability shortcut

The module does not automatically weight the 111 selected rows back to the full cohort. That would require a defensible selection model and assumptions outside this bounded case.

## 12. Missingness mechanisms and sensitivity

### Observed profile

`missingness-profile.csv` reports field, rows, missing count, percent, timing, cause in the synthetic generator, and learner-visible interpretation.

### Mechanism vocabulary

- MCAR: missingness independent of observed and unobserved values under the model.
- MAR: missingness independent of the missing value after conditioning on observed information.
- MNAR: missingness still depends on the unobserved value after conditioning.

These are assumptions about a data-generating process, not labels proven by a missingness table.

### Primary teaching assumption

The fixture uses a documented observed-characteristic masking mechanism, making MAR a known generator fact. Learners are still required to state it as an assumption they could not prove from an ordinary observed dataset.

### Methods compared

- full synthetic truth, instructor audit only;
- complete case;
- median imputation with missingness indicator;
- low-delta imputation sensitivity; and
- high-delta imputation sensitivity.

### Same-target rule

Every estimate targets the same 600-person synthetic ATE. A method that silently changes population or outcome fails the sensitivity comparison.

### No truth language for imputation

Imputed values are completed analytic values under a method and assumption. They are not recovered facts.

### Referral triggers

- high missingness in a core confounder;
- incompatible missingness by treatment group;
- sensitivity that changes sign or decision;
- multiple incomplete variables requiring joint modeling;
- post-treatment missingness; or
- likely MNAR mechanism.

## 13. Repeated measures and mixed-model reading

### Repeated unit

The repeated fixture contains four scheduled visits within each synthetic person. The person is the cluster. Visit rows are not independent people.

### Required evidence

- person-visit table;
- visit counts per person;
- within- and between-person variance;
- naive independent-row regression output;
- cluster-robust output;
- random-intercept mixed-model output;
- paired R reading target;
- interpretation record; and
- referral decision.

### Teaching comparison

The learner compares the same fixed effects under:

1. naive ordinary least squares;
2. cluster-robust standard errors; and
3. a random-intercept mixed model.

Differences in standard errors and variance decomposition show why row independence matters.

### Mixed-model interpretation

The learner identifies:

- fixed intercept;
- visit-time effect;
- treatment main effect;
- treatment-by-time effect;
- person random-intercept variance;
- residual variance; and
- intraclass correlation.

### Scope boundary

The module does not teach random-slope selection, covariance-structure optimization, small-sample corrections, nonlinear mixed models, or definitive longitudinal treatment effects.

### R role

The supplied R script uses a named mixed-model implementation and writes a normalized reading table. Learners read and reconcile output; from-scratch R programming is not graded.

## 14. Survival and censoring recognition

### Required definitions

- unit: synthetic person;
- time zero: synthetic treatment assignment;
- event: generated symptom-resolution event;
- censoring: generated end of observation before event;
- observed time: minimum of event and censoring time;
- status: event before or at censoring;
- risk set: people still observed and event free immediately before a time.

### Required evidence

- survival fixture;
- censoring summary;
- event and at-risk table;
- Kaplan-Meier table by treatment;
- fixed-time survival reading;
- Cox teaching output;
- proportional-hazards boundary;
- paired R reading target; and
- specialist referral.

### Censoring is not ordinary missingness

A censored person contributes observed event-free time and remains in risk sets until censoring. Dropping the row or setting event time to zero destroys that information.

### Kaplan-Meier reading

The learner reads stepwise survival probabilities and numbers at risk. The curve estimates the generated fixture's event-free function under its censoring assumptions; it is not a clinical prognosis.

### Cox reading

The learner reads a treatment hazard ratio conditional on declared covariates. A hazard ratio is not a risk ratio, probability difference, median difference, or causal effect by itself.

### Referral triggers

- nonproportional hazards;
- competing events;
- interval censoring;
- recurrent events;
- time-varying treatment;
- informative censoring;
- few events; or
- clinical survival claim.

## 15. Exact learner deliverables and package contract

### Required core files

- `README.md`;
- `VERSION`;
- `requirements.txt`;
- `source-record.yml`;
- `data-spec.md`;
- `assessment.md`;
- `instructor-notes.md` in the reference package;
- deterministic builder;
- validator;
- release metadata; and
- learner template.

### Required decision files

- `causal-claim-screen.md`;
- `dag.mmd`;
- `dag-narrative.md`;
- `validity-adjustment-longitudinal-memo.md`;
- `mixed-model-reading.md`;
- `survival-censoring-reading.md`;
- `specialist-referrals.md`;
- `reproducibility-check.md`;
- `accessibility-review.md`;
- `ai-use.md`; and
- `progression-decision.md`.

### Required generated data and evidence

- treatment fixture;
- repeated-measures fixture;
- survival fixture;
- analytic-aim validity map;
- DAG nodes and edges;
- confounder/collider/mediator/selection register;
- propensity predictions;
- overlap table;
- balance table;
- adjustment estimate table;
- selection profile;
- missingness profile;
- mechanism assumptions;
- imputation sensitivity;
- repeated summary;
- naive, cluster-robust, and mixed outputs;
- KM and Cox outputs;
- 12-row threat register;
- invariant checks;
- accessible DAG SVG; and
- build report.

### No screenshot-only evidence

Every visual has structured CSV or text equivalence. The DAG SVG is accompanied by editable Mermaid source, node and edge tables, and narrative.

### Portable build

The learner workspace contains fingerprinted accepted inputs, synthetic fixture rules, code, prompts, and reference outputs. A clean copied workspace rebuilds outputs into a new target and refuses overwrite.

## 16. Assessment, rubric, and noncompensable gates

### Fifteen-point rubric

| Criterion | Points |
|---|---:|
| Aim, estimand, DAG, and causal-claim boundary | 4.00 |
| Confounding, overlap, balance, and adjustment reasoning | 3.00 |
| Missingness assumptions and sensitivity evidence | 3.00 |
| Selection, repeated measures, mixed-model, survival, and specialist boundaries | 3.00 |
| Clear memo, accessible DAG, reproduction, and agent disclosure | 2.00 |
| Total | 15.00 |

The minimum numeric score is 12.00 of 15.00. Every gate must pass.

### Gates

1. Checkpoint 1 accepted input unchanged.
2. Prediction and causal aims remain distinct.
3. DAG roles and adjustment choices explicit.
4. No collider or post-outcome variable added without defensible reason.
5. Overlap and balance shown.
6. Missingness mechanisms labeled assumptions.
7. Structural blanks not converted to zero.
8. Sensitivity comparison uses same target and population.
9. Repeated observations not treated as independent without a limit.
10. Censoring not handled as ordinary missingness.
11. No causal, treatment, survival, or transport claim beyond design.
12. DAG has equivalent structured route.
13. Explicit Module 05 progression disposition.

### Automatic return

- checkpoint fingerprint mismatch;
- restricted or real patient data;
- unresolved prompt;
- changed synthetic generator without versioning;
- outcome-informed propensity model;
- missing overlap or balance evidence;
- imputation presented as truth;
- invented zero event time;
- missing cluster or censoring definition;
- inaccessible DAG;
- unsupported claim; or
- missing progression decision.

## 17. Feedback, revision, recovery, and support

### Feedback order

1. claim and timing;
2. DAG and roles;
3. adjustment and overlap;
4. selection;
5. missingness assumptions;
6. repeated and survival structure;
7. specialist referrals;
8. reproduction and access;
9. prose.

### Revision examples

| Defect | Response |
|---|---|
| Predictive feature called confounder | return to DAG role reasoning |
| Mediator included in total-effect adjustment | revise adjustment set or estimand |
| Poor overlap hidden | restore evidence and refer or restrict target |
| Structural blank set to zero | stop and restore source meaning |
| Imputation changes sign | carry sensitivity and refer |
| Person-visits treated as independent | add dependence-aware reading and revise uncertainty |
| Censored rows dropped | rebuild survival evidence |
| Hazard ratio called probability | correct quantity and defense |

### Supported route

The reference Python environment is pinned. R execution uses a supplied script and normalized reading target; a managed R environment may be provided. Learners are assessed on interpretation and reconciliation.

### Accessibility route

All exact tasks can be completed from CSV and Markdown. Mermaid and SVG are redundant views of the same node-edge structure.

### Extension

Appropriate extensions deepen one existing threat. Adding a new causal estimator or survival family is deferred until the bounded evidence is mastered.

## 18. Responsible AI, privacy, accessibility, and integrity

### AI may assist

- classify draft threats;
- explain method vocabulary;
- check code;
- draft DAG narration;
- compare output tables;
- suggest accessible descriptions; and
- format records.

### AI may not own

- causal contrast;
- DAG truth;
- adjustment set;
- missingness mechanism judgment;
- specialist referral;
- clinical meaning;
- score; or
- progression.

### Required AI-use record

Tool, task, data shared, output retained, independent checks, corrections, and accountable human are recorded.

### Privacy

No real patient record, secret, credential, private URL, local personal path, or restricted source may enter the package. All generated fixtures are explicitly synthetic.

### Accessibility

- DAG title and description;
- structured nodes and edges;
- narrative route;
- labeled tables;
- plain-language quantities;
- no color-only meaning; and
- no screenshot-only assessment.

### Integrity traps

- selecting a DAG because it gives a preferred effect;
- including future information in a propensity model;
- deleting poor-overlap rows without changing the target;
- calling MAR proven;
- hiding sign-changing sensitivity;
- treating repeat rows as more people;
- deleting censored people;
- calling a hazard ratio causal; and
- allowing agent prose to replace reviewer judgment.

## 19. Validation and acceptance tests

### Builder self-check

The builder must:

- verify accepted checkpoint and upstream fingerprints;
- create all three synthetic fixtures deterministically;
- generate every output table and DAG SVG;
- preserve structural blanks;
- prove overlap and balance calculations;
- conserve person and visit counts;
- conserve survival events and censoring;
- pass invariant checks;
- create a copied learner workspace;
- rebuild identical outputs; and
- refuse an existing target.

### Validator self-check

The validator must:

- accept reference release;
- accept prompted starter structurally;
- reject prompted completion;
- compare all generated outputs;
- verify source fingerprints;
- verify DAG equivalence;
- verify rubric and gates;
- reject missing or changed evidence;
- reject structural-zero corruption;
- reject unsupported progression; and
- reject personal paths and secrets.

### Acceptance commands

```powershell
python courses/modeling-inference-reproducible-analytics/modules/04-validity-adjustment-longitudinal/build_validity_evidence.py --self-check
python courses/modeling-inference-reproducible-analytics/modules/04-validity-adjustment-longitudinal/validate_validity_evidence.py --self-check
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/check-curriculum-specs.ps1
```

### Repository acceptance

- 21 specification sections;
- module 0.1.0;
- Commons 0.43.0;
- exact output fingerprints recorded;
- module checks pass;
- full curriculum gate passes;
- semantic-version trail complete;
- commit and push complete.

## 20. Risks, limitations, and required human review

### Material limitations

1. Fixtures are synthetic and simplified.
2. Known potential outcomes exist only because the treatment case is generated.
3. One propensity specification cannot establish real causal validity.
4. Bounded imputation is not multiple imputation.
5. Random-intercept reading is not full longitudinal-methods training.
6. Cox and Kaplan-Meier outputs are recognition exercises.
7. Checkpoint 1 still has four test outcomes and sparse subgroups.
8. Paired R execution requires a named environment.
9. No real treatment, longitudinal, survival, or clinical claim is supported.

### Required reviewers

- FND-2 faculty;
- biostatistical validity;
- causal inference;
- missing data;
- longitudinal methods;
- survival analysis;
- clinical informatics;
- clinician;
- accessibility;
- privacy and security;
- responsible AI; and
- independent instructor/reproducer.

### Risk controls

| Risk | Control |
|---|---|
| Causal overclaim | synthetic truth and claim screen |
| Wrong adjustment | DAG role register |
| Positivity hidden | overlap and weight tables |
| Missingness certainty | assumption language and deltas |
| Selection ignored | 111-versus-374 profile |
| Dependence ignored | naive versus cluster/mixed comparison |
| Censoring mishandled | risk-set and KM evidence |
| Inaccessible DAG | SVG, Mermaid, nodes, edges, narrative |
| Agent overreach | disclosure and human decisions |

## 21. Release, handoff, and resume contract

### Semantic-version decision

Module 04 begins at 0.1.0 and advances the Commons minor release from 0.42.0 to 0.43.0. Checkpoint 1 and Modules 01 through 03 remain unchanged.

### Completed release record

The 0.1.0 release records every source fingerprint plus rows, fields, bytes, and SHA-256 for all 19 generated CSVs, the accessible DAG SVG, and the build report. The known synthetic ATE is -6.00000000; the unadjusted estimate is -1.27214587; all five weighted absolute standardized differences are below 0.10. Complete-case IPTW uses 509 rows and estimates -6.17942841. The observed fixture has 91 missing severity values.

The repeated case freezes 2,400 observations from 600 people and an ICC of 0.83598751. The survival case freezes 449 events, 151 censored records, and a treatment hazard ratio of 0.67945425. All 16 generated invariants pass. Builder self-check, existing-target refusal, copied-workspace reproduction, incomplete-submission rejection, and broken-output rejection pass. The independent validator executes 36,575 release checks and 36,512 starter checks. The reference disposition is `continue with conditions`.

### Module 05 handoff

Module 05 receives:

- accepted validity map;
- 12-threat register;
- prediction versus causation boundary;
- unresolved referrals;
- missingness and selection limits;
- repeated and survival recognition limits;
- reproduction and AI-use evidence; and
- explicit forecast testing implications.

It begins a distinct 94-week public CDC NHSN forecasting case. It does not reuse the row-level prediction split.

### Resume record

Module 04 is complete when the 21-section spec, deterministic synthetic fixtures, exact validity evidence, learner package, validator, full curriculum gate, Commons 0.43.0 update, commit, and push all pass.

Resume with Module 05 only. Do not alter Checkpoint 1, causal contrast, DAG, generator, adjustment rule, missingness methods, repeated structure, survival definition, or claim boundary without a documented return and semantic-version decision.
