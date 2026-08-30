# APP-1 Module 03: Survival and time-to-event outcomes

## 1. Module identity, duration, prerequisites, and place in the course

- Module ID: `oclc-app1-03`.
- Course: APP-1, Data for Clinical Care.
- Instructional week: 3.
- Hours: 16.5.
- Module version target: 0.1.0.
- Commons release target: 0.51.0.
- Submission: survival analysis package and cumulative Week 3 release.
- Decision: what the time-to-event evidence says and whether the accepted cohort may enter adjusted comparison.
- Prerequisites: accepted APP-1 Modules 01 and 02, including the corrected 476-person day-30 landmark cohort.

The module moves survival analysis from foundation recognition to working use. Learners preserve the accepted risk set, produce count-first Kaplan-Meier evidence, compare scheduled-follow-up groups, inspect the proportional-hazards assumption, and explain what a synthetic observational comparison can and cannot support.

The cumulative Week 3 checkpoint freezes Modules 01 through 03. It awards the 20 phenotype-and-cohort points exactly once. Module 03 survival evidence is a required progression gate, not a second score.

## 2. Decision, audience, and claim boundary

The continuing decision is:

> Should a hospital medicine care-improvement council continue developing a prospective pathway to increase scheduled follow-up within 30 days after an adult's first qualifying acute-care discharge?

The analytic question for this module is narrower:

> Among the accepted day-30 landmark cohort, how does time to first later acute return differ between people with and without a recorded scheduled follow-up encounter, and is the evidence adequate to begin risk adjustment?

Primary readers are the hospital medicine clinical care-improvement council, the APP-1 faculty owner, and a survival-methods reviewer. They need exact counts, uncertainty, assumption checks, and a bounded progression recommendation.

The source is synthetic. Scheduled encounter occurrence does not prove access, completion, quality, clinical need, or benefit. Group differences are observational associations. No output may be described as a treatment effect, efficacy estimate, causal effect, real-facility result, or population prevalence.

## 3. Accepted upstream identity and frozen risk set

Module 03 accepts only the following upstream package:

- APP-1 Module 02 ID `oclc-app1-02`;
- Module 02 version `0.1.0`;
- Commons release `0.50.0`;
- 476-row, 49-field `analysis-cohort.csv`;
- analysis-cohort bytes `200699`;
- analysis-cohort SHA-256 `558c31b8aa5031c12baadeaa2f8cbb788289842b08aae79f38ecfe0d68fe9bd5`;
- 1,018-row event audit SHA-256 `8491e4c02d33771a904bcc095982cccd6265c3d301c10fc79ac259ceede6fe9c`;
- extension ID and seed `app1-six-site-v1`;
- source database SHA-256 `1116dda22c4297fcfeab6bf2c99bb3dbfaf9f9b5e04041b96be90719c76e704a`; and
- Module 02 workspace-manifest SHA-256 `9d78f888753b39797ad421d2576eef377ba0bc01fcca02d9ef3c9da388057c10`.

The accepted risk set contains 476 unique people, 129 with scheduled follow-up and 347 without it. It contains 87 first later acute returns, divided into 25 exposed and 62 unexposed events. The other 389 people are administratively censored at the end of the fixed follow-up window.

Module 03 may add analytic outputs. It may not add or remove people, change exposure, move time zero, change an event, replace an observed time, alter a censoring reason, or regenerate a teaching-site assignment.

## 4. Foundation skill revisited at working level

FND-2 owns recognition of time zero, event, censoring, observed time, risk sets, Kaplan-Meier probabilities, hazard ratios, and specialist referral triggers. APP-1 Module 03 requires learners to use those ideas on the clinical-care cohort.

Learners must:

1. reconcile all people, events, and censors before modeling;
2. construct event-time risk sets by scheduled-follow-up group;
3. compute and interpret Kaplan-Meier estimates with uncertainty;
4. compare groups with a log-rank test;
5. fit and read a guided unadjusted Cox model;
6. check proportional hazards and respond to a failed screen;
7. reconcile Python evidence with supplied R code; and
8. translate the evidence into a clinical progression decision without causal overreach.

Generic programming, data cleaning, SQL, chart selection, and Cox derivation from first principles are not retaught.

## 5. Learning outcomes

By the end of the module, a learner can:

- define the unit, landmark time zero, event, censoring event, follow-up horizon, exposure, and target contrast;
- prove that group-specific people equal events plus censors;
- explain why a censored person remains in the risk set until censoring;
- calculate a Kaplan-Meier product-limit estimate from a risk table;
- report group-specific event-free probabilities and 95 percent intervals at fixed times;
- distinguish survival probability, cumulative event risk, hazard, hazard ratio, and risk difference;
- run and interpret a log-rank comparison without treating a large p-value as proof of equivalence;
- fit and interpret a one-predictor Cox model as an unadjusted associational model;
- inspect Schoenfeld residual evidence and reject a constant-hazard-ratio summary when the screen fails;
- explain the later-death pattern and the limits of cause-specific censoring;
- read and reconcile supplied R survival code without being graded on writing R from scratch;
- create an accessible curve plus an exact structured alternative; and
- decide whether Module 04 may begin, with explicit conditions.

## 6. Concept ownership and out-of-scope boundaries

Module 03 owns:

- event-free survival after the day-30 landmark;
- risk-set construction;
- Kaplan-Meier estimates and Greenwood uncertainty;
- prespecified fixed-time comparisons;
- log-rank comparison;
- an unadjusted Cox exposure model;
- proportional-hazards screening;
- later-death and censoring interpretation;
- survival-focused R reading; and
- the survival-readiness gate in the Week 3 package.

Module 04 owns baseline covariate selection, prognostic modeling, case-mix support, adjusted Cox or alternative outcome models, calibration, expected outcomes, standardized comparisons, and residual-confounding interpretation.

Out of scope:

- changing the Module 02 phenotype or landmark;
- selecting an adjusted model based on this module's p-values;
- causal treatment-effect estimation;
- recurrent-event modeling;
- Fine-Gray or other competing-risk regression;
- time-varying exposure analysis;
- automated model selection;
- real-site ranking;
- subgroup or fairness claims; and
- clinical deployment.

## 7. Lesson sequence and learner time

| Block | Hours | Work |
|---|---:|---|
| Risk-set and censoring reconciliation | 2.0 | Freeze upstream identity; reconcile 476 people, 87 events, and 389 censors |
| Kaplan-Meier construction | 3.0 | Build event-time and fixed-time tables; inspect product-limit calculations |
| Uncertainty and accessible display | 2.0 | Read Greenwood intervals; create curve and structured alternative |
| Fixed-time and log-rank comparison | 2.0 | Compare prespecified event-free probabilities; run log-rank test |
| Guided Cox model | 2.0 | Fit exposure-only model; interpret hazard ratio and interval |
| Proportional-hazards assessment | 2.0 | Inspect Schoenfeld residual time screen; identify changing-hazard evidence |
| R read-run-interpret exercise | 1.5 | Run supplied script when a named R environment is available; reconcile output |
| Clinical interpretation and checkpoint release | 2.0 | Explain deaths and censoring; assemble Week 3 progression package |
| Total | 16.5 |  |

## 8. Required readings and source documentation

Required method references:

- NIST/SEMATECH e-Handbook survival analysis overview: https://www.itl.nist.gov/div898/handbook/apr/section1/apr15.htm
- R `survival` package documentation: https://cran.r-project.org/package=survival
- statsmodels proportional-hazards regression documentation: https://www.statsmodels.org/stable/generated/statsmodels.duration.hazard_regression.PHReg.html
- statsmodels survival-function documentation: https://www.statsmodels.org/stable/generated/statsmodels.duration.survfunc.SurvfuncRight.html
- PCORI Methodology Standards: https://www.pcori.org/research-related-projects/about-our-research/research-methodology/pcori-methodology-standards

Required source documentation:

- Synthea overview: https://synthetichealth.github.io/synthea/
- Synthea source repository: https://github.com/synthetichealth/synthea
- accepted APP-1 Module 02 source and extension records in the repository.

The learner must distinguish a methods reference from evidence about the clinical pathway. None of these sources validates a clinical effect in the synthetic cohort.

## 9. Analysis contract

| Element | Frozen definition |
|---|---|
| Unit | one accepted landmark-eligible synthetic person |
| Time zero | day-30 landmark after index discharge |
| Exposure | recorded scheduled follow-up encounter within 30 days, frozen by Module 02 |
| Comparator | no recorded scheduled follow-up encounter within 30 days |
| Event | first emergency or inpatient acute return after the landmark through day 365 after discharge |
| Observed time | days from landmark to first later acute return, competing death before event, or administrative end |
| Administrative censor | end of the fixed day-365-after-discharge window |
| Competing event | recorded death after the landmark and before first later acute return |
| Primary descriptive quantity | Kaplan-Meier event-free probability by exposure group |
| Prespecified times | 0, 30, 90, 180, 270, and 335 days after landmark |
| Primary group test | two-sided log-rank test |
| Guided model | unadjusted Cox model with scheduled-follow-up indicator only, Efron ties |
| PH screen | event-level Schoenfeld residual association with log event time |
| Interpretation | synthetic observational association; no causal effect |

The log-rank test and Cox model answer related but not identical questions. Neither replaces the count-first survival table. A p-value above 0.05 does not establish equivalence, benefit, safety, or absence of clinically relevant difference.

## 10. Kaplan-Meier construction and count-first risk tables

For each group and distinct event time, the released event table must contain:

- number at risk immediately before the time;
- number of events at the time;
- number censored at the time;
- conditional event-free factor;
- cumulative Kaplan-Meier event-free probability;
- Greenwood cumulative term;
- standard error; and
- log-log 95 percent confidence limits.

At each prespecified time, the risk table must contain the original group size, number at risk immediately before the time, cumulative events, cumulative censors, event-free probability, cumulative event risk, and interval.

At time zero, event-free probability is 1. At day 335, people administratively censored at the boundary remain at risk immediately before censoring. The table must not relabel them as events or drop them from earlier risk sets.

## 11. Fixed-time comparisons and uncertainty

The fixed-time comparison table uses the same prespecified times for both groups. It reports:

- event-free probability in the scheduled-follow-up group;
- event-free probability in the no-follow-up group;
- event-free probability difference, exposed minus unexposed;
- cumulative event risk in each group;
- cumulative event-risk difference, exposed minus unexposed;
- both group intervals; and
- an interpretation boundary.

The reference release must foreground estimates and support counts. It may report p-values, but may not reduce the decision to statistical significance. No multiplicity-adjusted discovery claim is attempted because these times are descriptive checkpoints.

## 12. Log-rank comparison

The log-rank output must record:

- two groups;
- 476 people;
- 87 events;
- observed and expected events in the scheduled-follow-up group;
- variance;
- one-degree-of-freedom chi-square statistic;
- two-sided p-value; and
- the non-equivalence boundary.

The learner must explain that the log-rank test is most naturally read under broadly proportional separation. Crossing or changing hazards can weaken its summary value even when its calculation is correct.

## 13. Guided Cox model and quantity discipline

The reference Cox model contains one predictor: the frozen scheduled-follow-up indicator. It uses Efron handling for event-time ties. The output reports coefficient, standard error, hazard ratio, 95 percent interval, z statistic, p-value, people, events, and censors.

The hazard ratio is an instantaneous rate comparison conditional only on membership in the current risk set. In this unadjusted model it is not:

- a probability;
- a cumulative event risk;
- a risk ratio;
- a survival difference;
- an adjusted care comparison; or
- a causal effect.

Case-mix adjustment is prohibited in Module 03 because Module 04 owns the adjustment contract.

## 14. Proportional-hazards assessment and response

The Python release includes a reproducible Schoenfeld residual time-correlation screen for the scheduled-follow-up coefficient. The output records the transform, coefficient, event rows, correlation, p-value, threshold, and disposition.

If the p-value is below 0.05, the gate requires:

1. label the constant-hazard-ratio assumption unsupported by this screen;
2. stop using the single Cox hazard ratio as the main summary;
3. foreground the Kaplan-Meier table and prespecified fixed-time differences;
4. carry a time-varying or alternative survival-model referral into Module 04; and
5. prohibit causal language.

A failed screen does not invalidate the cohort or erase the observed events. It changes which summaries may drive the decision.

The paired R script supplies `cox.zph` as a second reading route. Its result remains pending until run in a named managed R environment. Python and R diagnostics must not be described as byte-identical implementations.

## 15. Death, competing-event, and censoring interpretation

Module 02 found three later deaths among landmark-eligible people. All three occur after a first later acute return. Therefore:

- the three deaths remain visible in a death audit;
- none is a competing-death censor before the event;
- all 389 no-event rows are administratively censored; and
- the cause-specific event analysis has zero observed pre-event death censors in this release.

This pattern does not prove noninformative censoring. It does not show that death is irrelevant in a real population. Date-granular synthetic death records, unmeasured loss to follow-up, recurrent events, and real competing outcomes remain specialist-review concerns.

## 16. Visualization and accessible alternative

The module releases one Kaplan-Meier curve with:

- both exposure groups;
- step geometry;
- labeled axes and units;
- direct group labels or a clear legend;
- a note that the source is synthetic;
- a visible fixed follow-up boundary; and
- alt text or an adjacent structured description.

The exact CSV risk table is the authoritative accessible alternative. It must be understandable without color or the chart. Color is never the only group cue. The chart may not smooth away steps, crop the y-axis to exaggerate differences, or omit the number-at-risk context.

## 17. Exact learner deliverables and Week 3 package

Module 03 learner workspace:

- `README.md`;
- `VERSION`;
- `source-record.yml`;
- `analysis-contract.json`;
- `environment.yml`;
- `assessment.md`;
- `build_survival.py`;
- `validate_survival.py`;
- `paired-survival.R`;
- `survival-interpretation.md`;
- `ph-assessment.md`;
- `competing-events-note.md`;
- `accessibility-review.md`;
- `reproducibility-check.md`;
- `ai-use.md`;
- `progression-decision.md`;
- `workspace-manifest.csv`; and
- released `outputs/` evidence.

The cumulative Week 3 checkpoint path is `courses/clinical-care/checkpoints/01-longitudinal-survival-readiness/`. It must freeze:

- accepted Module 01 release identity and decision records;
- accepted Module 02 package identity, cohort evidence, 20-point assessment, and progression record;
- Module 03 survival outputs and completed interpretation records;
- source, environment, repository, commit, and semantic-version evidence;
- one cumulative 20-point score with no duplicate scoring;
- survival-readiness gates; and
- permission or refusal to enter Module 04.

## 18. Assessment and noncompensable gates

Module 03 adds no course points at Week 3. The checkpoint carries forward the accepted Module 02 score of 20.00 out of 20.00. Module 03 uses survival-readiness gates.

Required gates:

1. exact Module 02 fingerprint;
2. unchanged 476-person risk set;
3. 129 exposed and 347 unexposed people;
4. 87 events and 389 censors conserved;
5. event-time and fixed-time risk tables complete;
6. Kaplan-Meier uncertainty present;
7. accessible structured alternative present;
8. log-rank output reconciled;
9. Cox quantity interpreted correctly;
10. PH screen reported and acted on;
11. three later deaths explained;
12. no claim that zero pre-event deaths proves noninformative censoring;
13. R status recorded honestly;
14. AI use disclosed and independently checked;
15. no causal, clinical-efficacy, real-site, or population claim; and
16. explicit Module 04 progression decision.

Any failed gate returns the survival package for revision even when the cumulative phenotype-and-cohort score is passing.

## 19. Common failure modes and instructor response

| Failure | Required response |
|---|---|
| Censored people are deleted | rebuild all risk sets and explain contributed time |
| Day-30 landmark is moved | restore Module 02 cohort and reject submission |
| Hazard ratio called a risk or probability | correct the estimand before progression |
| Large p-value called proof of no difference | replace with interval, support, and non-equivalence language |
| Failed PH screen hidden | return package and foreground fixed-time evidence |
| Cox model adjusted early | remove adjustment and defer contract to Module 04 |
| Three later deaths called pre-event censors | reconcile person-level death audit |
| Zero competing censors called proof of independent censoring | narrow claim and add referral |
| Curve has no exact alternative | add fixed-time and event-time tables |
| R output claimed without named execution | mark pending and retain Python reference |
| Synthetic site treated as real | stop comparison and correct provenance |

Instructors should intervene at the first changed denominator, unsupported quantity, hidden assumption failure, or causal claim.

## 20. Reproducibility, validation, and release checks

The package must:

- verify every accepted upstream hash before analysis;
- use a new output target and refuse overwrite;
- create all outputs from the frozen Module 02 analysis cohort;
- produce byte-identical outputs on two builds;
- verify every released row count, field count, byte count, and SHA-256;
- validate all fixed-time and event-time conservation rules;
- recompute log-rank, Cox, and PH-screen evidence;
- reject a changed cohort, output, score, gate, or progression value;
- assemble separate learner and reference workspaces;
- validate the copied learner command, including its manifest;
- scan text for personal paths and unsupported placeholders;
- parse JSON, YAML-compatible records, CSV, SVG, Python, and R artifacts; and
- pass the whole-curriculum checker.

The frozen release contains 11 output files totaling 70,204 bytes. The outputs include 84 event-time rows, 12 fixed-time risk rows, six paired fixed-time comparisons, one accessible SVG, and exact log-rank, Cox, PH-screen, death-audit, cohort, and build records.

The two-sided log-rank chi-square is 0.17859356 with p = 0.67258471. The unadjusted Cox hazard ratio is 1.10542457 with a 95 percent interval from 0.69479700 to 1.75873453. The Schoenfeld residual time screen correlation is 0.29040504 with p = 0.00636020 and fails. Event-free differences for scheduled follow-up minus no recorded follow-up are 0.01242097 at day 30, -0.03469383 at day 180, and -0.01512410 at day 335.

The nine-row immutable manifest is 1,385 bytes with SHA-256 `067e1953d7fe7bcfaf878880bef2edf44788b846f71c478282ebe34f1a5d4d52`. Complete reference validation passes 131 checks, learner-starter validation passes 74 checks, and module-root validation passes 101 checks. Two output builds match byte for byte. Copied-validator, existing-target, changed-upstream, incomplete-starter, changed-output, and invalid-progression routes pass.

## 21. Progression, reviewers, version, and known issues

Allowed dispositions are `continue`, `continue with conditions`, `revise`, and `refer`.

Module 04 may begin only when all 16 gates pass. A proportional-hazards concern may be carried as an open condition if the learner stops treating the constant Cox hazard ratio as the main summary and preserves fixed-time evidence for adjustment planning.

Required reviewers before alpha:

- APP-1 faculty owner;
- hospital medicine clinician;
- survival-analysis methodologist;
- clinical informatician;
- accessibility reviewer;
- privacy and data steward;
- responsible-AI reviewer; and
- independent instructor reproducer.

Known release limits:

- the source is synthetic and dated April 2020;
- exposure records do not prove follow-up quality or access;
- all no-event rows share administrative censoring at the fixed boundary;
- only 87 events support the unadjusted comparison;
- the PH screen may make one constant hazard ratio unsuitable as the main summary;
- no pre-event death censor occurs in this release;
- date-granular death is not clinical adjudication;
- R execution depends on a named environment with the `survival` package; and
- no real-population, causal, efficacy, fairness, site-ranking, or implementation claim is supported.

Module 03 is complete only when this 21-section specification, deterministic survival evidence, paired R reading route, learner and reference packages, cumulative Week 3 checkpoint, validators, curriculum gate, Commons 0.51.0 update, commit, and push all pass.
