# APP-1 Module 04: Risk adjustment and fair comparison

## 1. Module identity, duration, prerequisites, and place in the course

- Module ID: `oclc-app1-04`.
- Course: APP-1, Data for Clinical Care.
- Instructional week: 4.
- Hours: 16.5.
- Module version target: 0.1.0.
- Commons release target: 0.52.0.
- Submission: risk-adjusted comparison and interpretation memo.
- Decision: whether adjusted outcome differences are sufficiently credible to compare care groups and synthetic teaching sites.
- Prerequisites: accepted APP-1 Checkpoint 1 at Commons 0.51.0.

The module extends foundation regression and validity skills into a care-specific expected-outcome workflow. Learners define case mix before fitting, use a transparent fixed-horizon model, assess calibration and support, calculate observed-to-expected and standardized results, and state why no adjusted comparison is a causal effect or real-site grade.

## 2. Decision, readers, and intended use

The continuing care decision is whether a hospital medicine council should keep developing a prospective pathway to increase recorded scheduled follow-up after acute-care discharge.

Module 04 asks:

> After accounting for a small prespecified set of baseline prognostic fields, what outcome variation remains across scheduled-follow-up groups and six synthetic teaching sites, and is that comparison stable enough to enter clinical-variation analysis?

Primary readers are a clinical care analytics lead, hospital medicine council, APP-1 faculty owner, methods reviewer, and learner. The intended use is curriculum progression and prospective improvement planning. The analysis is not for deployment, payment, accountability, public reporting, or real-facility ranking.

## 3. Accepted upstream identity and immutable handoff

Module 04 accepts only:

- APP-1 Checkpoint 1 ID `oclc-app1-cp01`;
- checkpoint version `0.1.0`;
- Commons release `0.51.0`;
- 78-row checkpoint candidate manifest SHA-256 `ef5ace3d6b450473f5b7ab8c1b53bf24f63aa42910b1fdab5d72c617f4f57860`;
- Module 03 manifest SHA-256 `067e1953d7fe7bcfaf878880bef2edf44788b846f71c478282ebe34f1a5d4d52`;
- Module 02 analysis-cohort SHA-256 `558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5`; and
- extension ID and seed `app1-six-site-v1`.

The frozen 476-person risk set contains 87 events and 389 administrative censors. It has no pre-event competing-death censor. Module 04 may add baseline transformations, predicted probabilities, expected counts, and comparison outputs. It may not change membership, exposure, outcome, observed time, censoring, event order, or teaching-site assignment.

## 4. Why the model uses a fixed 335-day outcome

Module 03 found a failed proportional-hazards screen, so Module 04 does not use one constant Cox hazard ratio to repair or replace that result.

Every no-event person in this release is observed to the common day-335 administrative boundary after the landmark. No death censors a person before event. Therefore the reference expected-outcome model uses the binary indicator for first later acute return by day 335.

This fixed-horizon route is valid only for this frozen release structure. Unequal censoring, meaningful loss to follow-up, or a pre-event competing outcome would require a censoring-aware or competing-risk method and survival-methods review.

## 5. Learning outcomes

By the end of the module, a learner can:

- state the fixed-horizon outcome and why it is permitted here;
- classify every input field by timing, provenance, role, and prohibited use;
- distinguish baseline prognostic fields from exposure, post-exposure, outcome, identifier, and synthetic extension fields;
- prespecify a transparent expected-outcome model before fitting;
- interpret logistic coefficients, probabilities, expected counts, and model uncertainty;
- report apparent discrimination and calibration without making deployment claims;
- assess case-mix support for exposure groups and teaching sites;
- calculate observed-to-expected ratios and indirectly standardized rates;
- attach count-based uncertainty to standardized site estimates;
- apply a prespecified suppression rule;
- compare unadjusted and adjusted descriptive evidence;
- interpret an adjusted exposure association without causal language;
- detect sparse-coefficient bootstrap instability;
- explain residual confounding and synthetic-site zero-effect provenance; and
- decide whether Module 05 may begin.

## 6. Foundation skill revisited and ownership boundary

FND-2 owns regression fitting, validity threats, calibration recognition, missingness, and adjustment boundaries. APP-1 Module 04 makes those skills operational for one clinical-care comparison.

Module 04 owns:

- the case-mix field-role contract;
- fixed-horizon expected-outcome model;
- apparent model performance and calibration;
- bootstrap coefficient stability;
- person-level expected outcomes;
- exposure-group and teaching-site observed-to-expected comparisons;
- indirect standardization;
- support and suppression rules;
- adjusted exposure association as a bounded secondary analysis; and
- Module 05 progression conditions.

Module 05 owns treatment, procedure, adherence, utilization, time, and pathway variation. Module 06 owns formal subgroup and equity review plus the bounded machine-learning extension.

## 7. Explicitly out of scope

- causal effect of scheduled follow-up;
- propensity-score or inverse-probability treatment weighting;
- target-trial emulation;
- model selection by p-value, AIC search, or automated feature search;
- changing the Module 03 time-to-event conclusion;
- using site or outcome to predict expected outcome;
- using post-landmark information as baseline case mix;
- machine-learning comparison;
- fairness certification;
- ranking clinicians, facilities, demographic groups, or communities;
- real-world transport or prevalence claims; and
- operational deployment.

## 8. Lesson sequence and learner time

| Block | Hours | Work |
|---|---:|---|
| Handoff and fixed-horizon justification | 1.5 | Verify Checkpoint 1 and preserve Module 03 limits |
| Field roles and case-mix contract | 2.5 | Classify all 49 upstream fields; freeze four baseline predictors |
| Expected-outcome model | 3.0 | Fit transparent logistic model; interpret terms and probabilities |
| Calibration, discrimination, and stability | 2.5 | Build quintile table; calculate Brier and AUC; run fixed bootstrap |
| Exposure-group comparison | 1.5 | Compare observed, expected, standardized, and adjusted-association evidence |
| Teaching-site comparison | 2.5 | Calculate support, O/E, standardized rates, intervals, and suppression |
| Fair-comparison interpretation | 1.5 | Explain zero-effect extension, residual confounding, and prohibited ranking |
| Reproduction and progression | 1.0 | Validate package and write Module 05 disposition |
| Total | 16.5 |  |

## 9. Required readings and methods sources

- CMS Measure Management System risk-adjustment guidance: https://mmshub.cms.gov/measure-lifecycle/measure-specification/risk-adjustment
- CMS Measure Management System measure lifecycle overview: https://mmshub.cms.gov/blueprint-measure-lifecycle-overview
- PCORI Methodology Standards: https://www.pcori.org/research-related-projects/about-our-research/research-methodology/pcori-methodology-standards
- statsmodels generalized linear model documentation: https://www.statsmodels.org/stable/glm.html
- scikit-learn calibration guidance for conceptual comparison: https://scikit-learn.org/stable/modules/calibration.html
- Synthea documentation: https://synthetichealth.github.io/synthea/

Learners must distinguish method guidance from validation of this synthetic clinical comparison. No reading converts the teaching extension into real quality evidence.

## 10. Field-role and timing contract

Every one of the 49 Module 02 analysis-cohort fields receives:

- field name;
- provenance class;
- earliest availability;
- analytic role;
- transformation, if any;
- permitted use; and
- prohibited interpretation.

Reference expected-outcome predictors are fixed before fitting:

| Source field | Model field | Transformation | Reason |
|---|---|---|---|
| `age_at_index` | `age_decade_from_40` | `(age - 40) / 10` | baseline age on interpretable scale |
| `prior_365d_acute_count` | `any_prior_acute` | one if count is above zero | preserve sparse prior-use signal without leverage from the maximum of 11 |
| `prior_365d_condition_count` | unchanged | integer count from 0 through 5 | baseline documented condition burden |
| `index_encounter_class` | `index_inpatient` | one for inpatient, zero for emergency | baseline index acuity proxy |

No interaction, spline, nonlinear term, or variable selection is introduced after seeing results.

## 11. Excluded field classes

The expected-outcome model excludes:

- patient and encounter identifiers;
- exact dates and timestamps;
- scheduled-follow-up exposure and its component fields;
- later return, death, observed-time, and censoring fields;
- landmark exclusion fields that are structurally fixed in the eligible cohort;
- source organization, because 64 sparse real-looking identifiers are not stable comparison units;
- teaching-site ID, because it is the comparison group;
- baseline risk score, rank, tier, assignment hash, and assignment uniform, because they belong to the synthetic extension and partly determine teaching-site assignment;
- gender, race, and ethnicity from the expected model because this small synthetic release lacks an approved clinical and equity rationale for using them in expected outcomes; and
- prior total encounter count because it overlaps the prespecified acute-use and condition-burden representation and was not selected prospectively.

Gender, race, and ethnicity remain available for the later prespecified equity audit. Exclusion from this model does not establish that they are irrelevant or that the model is fair.

## 12. Expected-outcome model contract

The primary model is a binomial generalized linear model with logit link:

`event_indicator ~ age_decade_from_40 + any_prior_acute + prior_365d_condition_count + index_inpatient`

Contract:

- population: all 476 accepted people;
- outcome: first later acute return by day 335;
- complete rows: 476;
- events: 87;
- intercept included;
- no weights;
- no regularization;
- no site effect;
- no exposure effect;
- no automated feature selection;
- coefficient covariance: model-based for the teaching reference;
- expected events: sum of person-level predicted probabilities; and
- intended use: descriptive indirect standardization in this synthetic cohort.

The model is fit on the full cohort because it estimates expected outcomes for the same bounded teaching population. Apparent performance is not an external-validation claim.

## 13. Apparent performance and calibration

Required apparent metrics:

- people and events;
- event prevalence;
- Brier score;
- rank-based area under the ROC curve;
- log likelihood and deviance;
- parameter count and events per non-intercept parameter; and
- expected-event conservation.

Calibration uses five deterministic groups formed by sorting predicted probability and patient ID, then assigning nearly equal-sized quintiles. Each row reports people, observed events, expected events, observed rate, mean predicted probability, observed minus expected, and support status.

The intercept ensures overall expected events reconcile with observed events in-sample. That identity is a fitting property, not proof of calibration, transportability, or clinical validity.

## 14. Bootstrap stability

The release uses 300 person-level bootstrap samples with seed `20260830`. Each sample has 476 draws with replacement and refits the exact expected-outcome formula.

For every coefficient, the stability table reports:

- reference estimate;
- bootstrap median;
- 2.5th and 97.5th percentiles;
- share of successful fits with the same sign as the reference;
- successful fits; and
- failed fits.

The bootstrap is a stability screen, not corrected inference. A very wide interval or low sign stability becomes an explicit condition. It cannot be removed by dropping the field after seeing the result.

## 15. Exposure-group comparison

For scheduled-follow-up and no-recorded-follow-up groups, report:

- people;
- observed events and crude event rate;
- expected events and mean expected probability;
- observed-to-expected ratio;
- indirectly standardized event rate, defined as O/E multiplied by the cohort event rate;
- count-based 95 percent interval for the standardized rate; and
- support and claim boundary.

A secondary logistic model adds `landmark_exposure` to the same four baseline fields. It reports an adjusted odds ratio and interval as an observational association. It is not the expected-outcome model, causal effect, hazard ratio, risk ratio, or proof of pathway benefit.

## 16. Teaching-site fair comparison

For each of `SITE-A` through `SITE-F`, report:

- people and events;
- crude event rate;
- expected events and expected rate;
- O/E ratio;
- indirectly standardized event rate;
- exact Poisson count interval transformed to the standardized-rate scale;
- scheduled-follow-up support;
- low, medium, and high synthetic risk-tier support;
- suppression status; and
- zero-effect and synthetic provenance.

The prespecified reporting rule suppresses a site if any condition holds:

- fewer than 50 people;
- fewer than 10 observed events;
- fewer than 10 expected events;
- either exposure group is absent; or
- any synthetic baseline-risk tier is absent.

Passing the rule means `report with caution`, never rank. Borderline support remains visible.

## 17. Uncertainty and interpretation rules

Site and exposure O/E intervals treat expected events as fixed and use exact Poisson limits for observed counts. This is a bounded teaching approximation. It does not propagate model-estimation uncertainty, account for site construction, or validate inferential coverage.

Required quantity distinctions:

- predicted probability is a fixed-horizon expected event probability;
- O/E compares observed event count with model-expected count;
- standardized rate rescales O/E to the cohort event rate;
- odds ratio is not a risk ratio or hazard ratio;
- adjusted association is not a causal effect; and
- interval overlap is not an equivalence test.

## 18. Exact learner deliverables and assessment

Required learner workspace:

- immutable source, checkpoint, field-role, environment, assessment, builder, validator, and R-reading controls;
- `risk-adjustment-memo.md`;
- `model-assessment.md`;
- `support-suppression-review.md`;
- `fair-comparison-interpretation.md`;
- `reproducibility-check.md`;
- `ai-use.md`;
- `progression-decision.md`; and
- released output files.

Twenty-five course points are awarded at the Week 6 checkpoint for the combined survival and risk-adjusted component:

| Criterion | Points |
|---|---:|
| Survival evidence, uncertainty, and PH response from Module 03 | 6.00 |
| Field roles, fixed horizon, and case-mix contract | 4.00 |
| Expected-outcome model, calibration, and stability | 6.00 |
| Exposure and teaching-site adjustment, support, and uncertainty | 6.00 |
| Interpretation, reproducibility, accessibility, and accountable AI use | 3.00 |
| Total | 25.00 |

Module 04 records this cumulative component score. It is not awarded again in Module 05 or 06.

## 19. Noncompensable gates and common failures

Required gates:

1. exact Checkpoint 1 and cohort identity;
2. unchanged 476-person risk set and 87 outcomes;
3. common day-335 fixed horizon justified;
4. all 49 fields classified;
5. four predictors frozen before fitting;
6. no exposure, site, outcome, post-exposure, or extension leakage into expected outcomes;
7. expected events conserve to 87 within tolerance;
8. apparent performance labeled apparent;
9. five calibration groups complete;
10. 300 bootstrap fits accounted for;
11. sparse-coefficient instability reported;
12. exposure comparison and adjusted association kept distinct;
13. six site comparisons include support and suppression;
14. Poisson interval approximation disclosed;
15. synthetic site zero-effect provenance explicit;
16. no causal, efficacy, fairness, real-site ranking, or deployment claim;
17. Module 03 PH failure remains visible; and
18. explicit Module 05 progression decision.

Common failures include selecting fields after viewing p-values, using the synthetic risk score as an observed clinical predictor, adjusting for follow-up in expected outcomes, reporting a site league table, treating no suppression as strong evidence, calling odds a risk, or claiming that adjustment removes confounding. Any such failure returns the package.

## 20. Reproducibility, validation, and mutation rejection

The release must:

- verify exact Checkpoint 1, Module 03, and cohort fingerprints;
- build into a new target and reject overwrite;
- create identical outputs on two builds;
- verify rows, fields, bytes, and SHA-256 for every output;
- reproduce coefficients, predictions, calibration, bootstrap, O/E, standardized rates, intervals, and suppression;
- conserve 476 people and 87 events through all comparisons;
- verify expected-event reconciliation;
- assemble separate learner and reference workspaces;
- verify the copied validator command and immutable manifest;
- reject changed cohort, field role, output, score, gate, progression, or zero-effect provenance;
- scan for personal paths, placeholders, credentials, and unsupported claims; and
- pass the whole-curriculum checker.

The release record freezes final evidence, output measurements, package manifest, validation counts, and progression conditions after construction.

Release evidence:

- 13 deterministic outputs contain 128,209 bytes; `release.json` records exact rows, fields, bytes, and SHA-256 for every file;
- the learner workspace contains 19 files and the reference workspace contains 32 files;
- the immutable manifest contains 10 rows, 1,666 bytes, and SHA-256 `5eaf8ba19e965b437cd4c586a1811b6d4aeb0f5cc82ea585dae2405432c9a8bb`;
- complete reference validation passes 155 checks, starter validation passes 85 checks, and the module source package passes 122 checks; and
- copied-validator, duplicate-build, overwrite, changed-upstream, changed-field-role, incomplete-starter, changed-output, invalid-score, invalid-progression, and visual-inspection routes pass.

## 21. Progression, reviewers, version, and known issues

Allowed dispositions are `continue`, `continue with conditions`, `revise`, and `refer`.

Module 05 may begin only when all 18 gates pass. Expected conditions include sparse prior-acute bootstrap instability, apparent-only performance, count-based intervals that omit model uncertainty, residual confounding, unreviewed demographic-field policy, synthetic-site provenance, the Module 03 PH failure, and pending named reviews.

Required reviewers before alpha:

- APP-1 faculty owner;
- hospital medicine clinician;
- clinical informatician;
- biostatistician with risk-adjustment expertise;
- survival-methods reviewer;
- equity reviewer;
- accessibility reviewer;
- privacy and responsible-AI reviewers; and
- independent instructor reproducer.

Known limits:

- only 87 events support four expected-outcome predictors;
- any-prior-acute is sparse and may have unstable bootstrap upper estimates;
- performance and calibration are apparent in the fitting cohort;
- no external, temporal, or geographic validation exists;
- Poisson intervals treat expected counts as fixed;
- the six sites are deterministic synthetic labels with known direct effect zero;
- adjustment cannot remove unmeasured confounding or prove fairness;
- the source is synthetic and dated April 2020; and
- no real-population, causal, efficacy, facility-ranking, or deployment claim is supported.

Module 04 is complete only when this 21-section specification, deterministic risk-adjustment outputs, learner and reference packages, validators, full curriculum gate, Commons 0.52.0 update, commit, and push all pass.
