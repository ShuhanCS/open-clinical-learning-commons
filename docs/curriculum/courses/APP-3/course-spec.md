# APP-3: Data for Clinical Performance and Improvement

## 1. Course identity and catalog role

- Course ID: APP-3.
- Title: Data for Clinical Performance and Improvement.
- Credits: 3.
- Delivery: online half-term.
- Planning rhythm: seven instructional weeks plus the official half-term end date.
- Total learner work: 112.5 hours.
- Prerequisites: accepted FND-1 and FND-2 technical releases.
- Primary graded tools: SQL and Python.
- R role: read, run, and interpret statistical process control and forecasting code; writing R from scratch is not graded.
- Final deliverable: clinical performance improvement package with reproducible evidence and a defense.
- Course version target: 0.1.0.
- Current Commons release: 0.65.0 through course specification and source architecture.
- Specification status: construction candidate.

APP-3 is where learners turn harm, delay, unreliable care, poor access, or a capacity constraint into a measurable clinical performance decision. Learners define the unit moving through a service, validate the measures that describe its performance, distinguish a signal from routine variation, locate bottlenecks, forecast demand, and test a bounded redesign before recommending action.

The academic calendar controls each due date:

https://www.mghihp.edu/sites/default/files/2026-06/ihp-calendar-2026-2027-with-winter-term-current.pdf

The 7.5-week phrase is a planning model. Week 3 and Week 6 are instructional checkpoints. The final package is due on the published last day of the assigned half-term.

| Half-term | Published dates | Inclusive calendar days | Approximate weeks |
|---|---|---:|---:|
| Fall 2026 half-term 1 | September 8 through October 27 | 50 | 7.14 |
| Fall 2026 half-term 2 | October 28 through December 18 | 52 | 7.43 |
| Spring 2027 half-term 1 | January 11 through March 2 | 51 | 7.29 |
| Spring 2027 half-term 2 | March 3 through April 24 | 53 | 7.57 |
| Summer 2027 half-term 1 | May 10 through June 29 | 51 | 7.29 |
| Summer 2027 half-term 2 | June 30 through August 20 | 52 | 7.43 |

## 2. Source authority and normalization

The source course is `07-APP-3-Clinical-Performance-and-Improvement.docx`, 26,907 bytes, SHA-256 `084a412054c77169ea065cf15ed3cc7097e412a6017fbb58a260e909d17717e3`. Byte-identical copies appear in both supplied curriculum archives.

The source record is `docs/source/app-3-clinical-performance-improvement-source-record.md`.

The source defines seven modules totaling 112.5 hours and assessments weighted 20, 20, 25, and 35 percent. The Commons preserves every point once:

- Week 3: 40 points;
- Week 6: 25 points; and
- official half-term end date: 35 points.

The Week 3 release combines the measure and operational metric build with the performance diagnostic. The Week 6 release combines the accepted forecast, scenario, evaluation, feasibility, monitoring, and embedded-ML evidence. The final package adds clinician leadership, communication, stewardship, accountability, and defense without rescoring earlier work.

APP-3 does not inherit another applied course's checkpoint weights. Its source assessment plan is authoritative, so APP-3 uses `40 / 25 / 35`.

## 3. Place in the program and prerequisite handoffs

### FND-1 handoff

Learners arrive able to maintain a reproducible repository, retrieve and join public data, define cohorts and denominators, clean and profile data, create time-indexed summaries, record provenance, and verify agent-assisted work.

APP-3 does not reteach generic SQL, project setup, data cleaning, or chart mechanics. It applies those skills to event logic, units of flow, queues, staffing, safety signals, operational rates, and measure stewardship.

### FND-2 handoff

Learners arrive able to classify an analytic aim, define a target and information cutoff, fit transparent models, preserve temporal order, compare a forecast with declared benchmarks, evaluate errors, state validity threats, and document model limits.

APP-3 extends those skills through operational forecasting, statistical process control, queue and capacity reasoning, scenario testing, implementation measures, and the cost of over- and under-forecasting. FND-2 proves that a forecast is technically evaluated. APP-3 asks whether the forecast is useful enough for a specific service decision.

### DA-730 handoff

Learners use accessible charts, exact tables, uncertainty displays, dashboard composition, and audience adaptation from DA-730. APP-3 does not repeat the visualization course as a chart catalog. A run chart, control chart, forecast display, or dashboard is graded here for its clinical performance meaning and decision use.

### Downstream handoff

- APP-4 may rely on operational workflow, alert burden, escalation, and human-factors evidence.
- APP-7 may rely on demand, capacity, utilization, quality, safety, and service-performance evidence before adding finance and value.
- CAP-1 may rely on measure stewardship, improvement evaluation, monitoring, and fallback rules.

## 4. Course decision and named audiences

The continuing teaching decision is:

> Should the adult emergency service at the explicitly fictional Commons General Hospital propose a bounded 12-week test of a predeclared flex-staffing and fast-track activation rule to reduce delay without increasing left-before-seen events, 72-hour unplanned returns, escalation delays, staff overtime, or supported subgroup gaps?

The synthetic service ID is `CGH-ED-01`. It is not a real facility and must never be linked to a public hospital identity.

### Primary decision owner

The primary owner is a fictional emergency service quality and operations council led jointly by the medical director, nurse leader, and operations director. The council may accept, condition, revise, refer, or stop a proposed prospective test. A curriculum package does not authorize implementation.

### Required audiences

| Audience | What they need |
|---|---|
| Medical and nursing leaders | measure validity, clinical and safety meaning, service constraints, escalation, and stop rules |
| Frontline staff | process definition, workload, role changes, feedback, fallback, and a blame-free explanation |
| Operations leader | demand, capacity, queues, utilization, staffing assumptions, sensitivity, and feasibility |
| Quality and safety team | event logic, process reliability, control-chart rules, incident limitations, and balancing measures |
| Patient and access representatives | delay, abandonment, language and disability access, subgroup support, burden, and consequences |
| Analytics and data stewards | source identity, measure code, time cutoffs, forecast folds, scenario inputs, tests, and reproduction |
| Governance reviewers | permitted use, synthetic boundaries, agent use, conditions, monitoring, and decision ownership |

## 5. Course learning outcomes

By the end of APP-3, learners can:

| ID | Assessable course outcome | Program connection |
|---|---|---|
| CLO-1 | Frame a clinical performance problem with an accountable aim, unit of flow, eligible population, stakeholders, constraints, and success measures. | PLO-1, PLO-5 |
| CLO-2 | Construct and validate quality, safety, access, flow, capacity, and balancing measures with correct numerator, denominator, exclusion, event, and time logic. | PLO-1, PLO-4 |
| CLO-3 | Diagnose variation, safety signals, delay, and bottlenecks using process maps, run and control charts, operational metrics, and bounded incident evidence. | PLO-2, PLO-3 |
| CLO-4 | Build and validate a bounded demand forecast and connect its error to capacity, staffing, access, and safety consequences. | PLO-2, PLO-3 |
| CLO-5 | Configure and test a guided improvement scenario while accounting for trend, confounding, sensitivity, equity, workforce burden, gaming, and unintended harm. | PLO-3, PLO-6 |
| CLO-6 | Produce and defend a clinical performance improvement package with measure and model stewardship, monitoring, escalation, fallback, and accountable ownership. | PLO-4, PLO-5, PLO-6 |
| CLO-7 | Compare the accepted transparent demand approach with one bounded ML forecast under identical temporal conditions and state whether ML changes the decision. | PLO-2, PLO-3, PLO-6 |

## 6. Concept ownership and boundaries

### APP-3 owns

- clinical performance aims and accountable improvement questions;
- units of flow, process boundaries, demand, capacity, constraints, and ownership;
- structure, process, outcome, access, safety, workforce, and balancing measures;
- numerator, denominator, exclusion, event, attribution, time-window, and refresh logic;
- cycle time, wait time, queue length, throughput, utilization, census, and capacity;
- process mapping, failure points, rework, handoffs, and bottleneck diagnosis;
- common and special cause variation, run charts, control charts, signal rules, and small-number limits;
- incident reports, near misses, trigger evidence, underreporting, and surveillance bias;
- demand forecasting tied to a declared operational horizon and cost of error;
- Little's Law as a bounded consistency check;
- queue, staffing, scheduling, and workflow scenarios;
- sensitivity, secular trend, regression to the mean, confounding, case mix, gaming, and unintended effects;
- implementation feasibility, access, equity, workforce burden, monitoring, escalation, fallback, and stewardship;
- a transparent operational forecast versus a bounded ML extension; and
- clinician leadership, frontline communication, accountability, and defense.

### APP-3 extends rather than repeats

- FND-1 data work gains event clocks, queue states, staffing capacity, process transitions, safety records, and maintained measure definitions.
- FND-2 forecasting gains operational horizons, capacity implications, service-level error costs, scenario use, and decision-change criteria.
- DA-730 concepts are used to make time, signal, uncertainty, exact values, and monitoring accessible. General visual-encoding instruction stays in DA-730.

### Out of scope

- protected, identifiable, workplace, or restricted patient and staff data;
- representing synthetic records as real operations, safety events, staff experience, or patient outcomes;
- using public aggregate data as a current local operations dashboard;
- ranking hospitals, clinicians, units, staff, patients, or demographic groups;
- treating a control-chart signal as proof of cause or a single incident report as prevalence;
- treating Little's Law as sufficient when steady-state assumptions do not hold;
- using a forecast or scenario result as an implementation order;
- optimizing flow while hiding safety, access, equity, or workforce harm;
- automated staffing, scheduling, patient routing, or clinical decision making;
- machine learning as a replacement for measure validation, process diagnosis, simpler benchmarks, or human ownership; and
- clinical implementation or model deployment.

## 7. Continuing source and analytic thread

### Public measurement anchor

The course begins with the complete accepted CMS Timely and Effective Care - Hospital release:

https://data.cms.gov/provider-data/dataset/yv7e-xc69

| Item | Accepted fact |
|---|---|
| CMS release date | 2026-08-13 |
| Full rows | 138,084 |
| Full columns | 16 |
| Full bytes | 34,150,899 |
| Full SHA-256 | `1e5a1ca803c2b09468fe3ae3fe60fef3e910f5f5300630a24791c88a1abff516` |
| Accepted Massachusetts EDV, OP_18b, and OP_22 source rows | 186 |
| Source-selection SHA-256 | `f28f5d56e5e0e29001c7a275b01306762e673c9a21459dc7a68ff1aea782943b` |

APP-3 reuses this release identity without reusing DA-730's dashboard assignment. It asks how public measures are defined, what they omit, and why local operational analysis requires different grain and freshness.

### Public safety context

The full CMS Complications and Deaths - Hospital dataset supplies aggregate safety-measure context:

https://data.cms.gov/provider-data/dataset/ynj2-r877

Module 01 must pin the accepted full release before use. Public PSI evidence cannot detect a current local event, identify a bottleneck, or establish the cause of harm.

### Historical capacity context

The HHS COVID-19 Reported Patient Impact and Hospital Capacity by Facility source supplies historical weekly utilization, capacity, occupancy, coverage, and staffing-shortage fields:

https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/anag-cw7u

Required reporting ended after 2024-05-03. The source is useful for teaching coverage, definitions, reporting changes, and historical context. It cannot support a current staffing decision.

### Synthetic operational release

The course's linked operational evidence is a versioned synthetic release for `CGH-ED-01`. It contains encounters, process events, staffing, queue snapshots, safety events, calendar demand, scenarios, and known truth. Each table has a generator version, seed, dictionary, row count, checksum, relationship checks, synthetic flag, and known-truth record.

The generator must seed:

1. measure defects that can be found and repaired;
2. routine and special-cause conditions that remain distinct from causal truth;
3. one process bottleneck with known timing and capacity constraints;
4. incident-report undercapture and reviewed non-events;
5. demand seasonality and calendar effects;
6. at least two redesign options plus a no-change baseline;
7. heterogeneous access or burden that requires supported subgroup review; and
8. one null or failed improvement condition so the course cannot guarantee a positive answer.

No synthetic value may be attached to a public facility. Public releases supply measurement and reporting context, not local truth.

## 8. Workload and module sequence

| Module | Title | Instructional week | Hours | Main submission |
|---:|---|---:|---:|---|
| 01 | Framing a clinical performance and improvement decision | 1 | 15.5 | Clinical performance charter |
| 02 | Measures and operational metrics | 2 | 16.0 | 20-point measure and operational metric build |
| 03 | Variation, safety signals, and bottlenecks | 3 | 16.5 | 20-point performance diagnostic and Week 3 release |
| 04 | Demand forecasting and capacity | 4 | 16.5 | Forecasting and capacity evidence |
| 05 | Improvement scenarios and evaluation | 5 | 16.0 | 25-point forecast, scenario, and evaluation component |
| 06 | Feasibility, monitoring, and embedded machine learning | 6 | 16.0 | Week 6 release with simple-versus-ML comparison |
| 07 | Clinician leadership, recommendation, and defense | 7 | 16.0 | Final clinical performance improvement package |
| Total |  |  | 112.5 |  |

Module 06 contains eight hours of application, feasibility, and monitoring work plus an eight-hour ML extension. The extension compares one bounded gradient-boosted arrival-demand forecast with the accepted transparent approach. It cannot change the target, eligible information, cutoffs, folds, horizons, or evaluation rows.

## 9. Module 01 brief: Framing a clinical performance and improvement decision

- Module ID: `oclc-app3-01`.
- Hours: 15.5.
- Package path: `courses/clinical-performance-improvement/modules/01-clinical-performance-decision/`.
- Specification: `docs/curriculum/courses/APP-3/modules/01-clinical-performance-decision-spec.md`.
- Decision: whether the service problem, unit of flow, source evidence, measure family, and accountable action are defined well enough to begin measure construction.
- Submission: clinical performance charter.

Learners distinguish quality improvement from performance reporting, define error, near miss, adverse event, and harm, name the encounter as the primary unit of flow, map demand and capacity, write a bounded aim, identify owners and affected groups, and separate public aggregate context from the synthetic local case.

The source audit must inspect every accepted full release, preserve unavailable and inconvenient values, state data freshness, and record what public data cannot answer. Progression requires a synthetic-service declaration, source feasibility record, process boundary, measure family, stakeholder and accountability map, claim boundary, AI-use record, and decision to begin measure construction.

No operational diagnosis or staffing proposal is allowed in Module 01.

## 10. Module 02 brief: Measures and operational metrics

- Module ID: `oclc-app3-02`.
- Hours: 16.0.
- Package path: `courses/clinical-performance-improvement/modules/02-measures-operational-metrics/`.
- Specification: `docs/curriculum/courses/APP-3/modules/02-measures-operational-metrics-spec.md`.
- Decision: whether the measure logic and linked operational tables are valid enough to diagnose performance over time.
- Submission: 20-point measure and operational metric build.

Learners specify quality, safety, access, flow, capacity, workforce, and balancing measures. Every measure records the numerator or summary, denominator or population, exclusions, unit, direction, event clock, attribution, reporting window, refresh cadence, owner, threshold origin, unavailable state, and interpretation limit.

SQL owns the linked event and denominator logic. Python independently checks event order, duplicate inclusion, impossible time, missing transitions, queue conservation, staff-capacity intervals, known-event sensitivity and specificity, cycle and wait time, throughput, utilization, queue length, and stratification support.

The build must preserve seeded defects in a raw layer, repair them through declared rules, and show how each defect changes at least one measure. A good score cannot compensate for a wrong denominator, event clock, unit, or source identity.

## 11. Module 03 brief: Variation, safety signals, and bottlenecks

- Module ID: `oclc-app3-03`.
- Hours: 16.5.
- Package path: `courses/clinical-performance-improvement/modules/03-variation-safety-bottlenecks/`.
- Specification: `docs/curriculum/courses/APP-3/modules/03-variation-safety-bottlenecks-spec.md`.
- Decision: whether the evidence supports one bounded process diagnosis and immediate escalation rule.
- Submission: 20-point performance diagnostic and 40-point Week 3 release.

Learners map the service, locate rework and handoffs, distinguish common from special cause, choose a chart that matches the measure distribution and denominator, calculate centerlines and limits, apply predeclared signal rules, preserve low-count limits, and compare prespecified shifts or acuity segments.

Safety evidence combines known synthetic events, incident reports, near misses, triggers, and reviewed non-events. Learners report undercapture, false positives, review status, and surveillance bias. A chart signal prompts investigation; it does not prove cause. An incident count is not a prevalence estimate.

The bottleneck claim must reconcile process transitions, queue states, wait, service time, throughput, utilization, staffing, and capacity. Checkpoint 01 freezes Modules 01 through 03 before forecasting begins.

## 12. Module 04 brief: Demand forecasting and capacity

- Module ID: `oclc-app3-04`.
- Hours: 16.5.
- Package path: `courses/clinical-performance-improvement/modules/04-demand-forecasting-capacity/`.
- Specification: `docs/curriculum/courses/APP-3/modules/04-demand-forecasting-capacity-spec.md`.
- Decision: what demand and capacity implication is supportable for the declared staffing horizon.
- Submission: forecasting and capacity evidence for the Week 6 assessment.

Learners define the target, issue time, horizon, unit, decision, eligible history, calendar effects, and cost of error before fitting. They compare last-value and seasonal-naive benchmarks with one bounded exponential-smoothing model on identical rolling-origin folds.

The release reports errors in arrivals and staffing consequences, not only unitless scores. Under-forecast and over-forecast costs remain separate. Forecast eligibility, missing shifts, reporting coverage, structural changes, residuals, and failure periods stay visible.

Learners apply Little's Law only as a bounded consistency check and state when nonstationarity, priority classes, abandonment, blocking, or changing capacity weaken it. The accepted forecast becomes an input to Module 05; it does not order staffing.

## 13. Module 05 brief: Improvement scenarios and evaluation

- Module ID: `oclc-app3-05`.
- Hours: 16.0.
- Package path: `courses/clinical-performance-improvement/modules/05-improvement-scenarios-evaluation/`.
- Specification: `docs/curriculum/courses/APP-3/modules/05-improvement-scenarios-evaluation-spec.md`.
- Decision: which baseline, flex-staffing, or fast-track option, if any, deserves feasibility review.
- Submission: 25-point forecast, scenario, and evaluation component.

Learners configure a provided discrete-event scenario rather than build a production simulation system. They validate arrival, service, routing, priority, staffing, capacity, warm-up, replication, and conservation assumptions against the accepted evidence.

Every scenario reports wait, cycle time, throughput, abandonment, utilization, overtime, escalation delay, safety, access, and subgroup consequences. Learners vary uncertain inputs, compare at least two redesign options with no change, identify fragile conclusions, and preserve runs that do not improve performance.

The proposed evaluation separates process-control monitoring from causal claims. Learners audit secular trend, regression to the mean, measurement changes, concurrent interventions, case mix, gaming, and unintended effects. A scenario is evidence about assumptions, not proof of a real intervention effect.

## 14. Module 06 brief: Feasibility, monitoring, and embedded machine learning

- Module ID: `oclc-app3-06`.
- Hours: 16.0.
- Application and monitoring block: 8.0 hours.
- Embedded ML extension: 8.0 hours.
- Package path: `courses/clinical-performance-improvement/modules/06-feasibility-monitoring-embedded-ml/`.
- Specification: `docs/curriculum/courses/APP-3/modules/06-feasibility-monitoring-embedded-ml-spec.md`.
- Decision: whether the proposal is feasible enough for clinician leadership review and whether ML changes the operational recommendation.
- Submission: cumulative Week 6 release.

The application block tests staffing, scheduling, governance, access, equity, disability and language needs, quality and safety interactions, workforce burden, implementation measures, dashboard purpose, refresh cadence, escalation, fallback, and stewardship. It names who gains, who carries work, who may be excluded, and who can pause the proposal.

The ML extension fits one bounded gradient-boosted regression forecast using only eligible calendar and lag features. It must use the accepted target, cutoffs, folds, horizons, and evaluation rows. Learners compare it with the transparent approach on forecast error, under- and over-forecast cost, capacity decisions, shift support, failure periods, reproducibility, and leakage tests.

ML changes the recommendation only if a prespecified decision rule is met and the operational implication remains safe under sensitivity analysis. Better average error alone is insufficient. The ML result cannot replace the process diagnosis, scenario, balancing measures, or human decision.

The Week 6 package carries the 25 Module 05 course points once. Module 06 gates are required but add no points.

## 15. Module 07 brief: Clinician leadership, recommendation, and defense

- Module ID: `oclc-app3-07`.
- Hours: 16.0.
- Clinician of record: Joe Joseph, MD, SFHM. Dated public identity is confirmed; participation and final wording require direct confirmation before alpha.
- Package path: `courses/clinical-performance-improvement/modules/07-clinician-leadership-defense/`.
- Specification: `docs/curriculum/courses/APP-3/modules/07-clinician-leadership-defense-spec.md`.
- Decision: whether to propose a bounded prospective test, revise the evidence or design, refer the question, or stop.
- Submission: final clinical performance improvement package and defense.

Module 07 freezes the accepted Week 3 and Week 6 evidence before adding leadership records. Learners cannot repair a weak measure, change a forecast fold, tune a scenario, or reinterpret a failed gate inside the leadership package.

The final package includes an evidence synthesis, frontline brief, leadership summary, recommendation, alternative considered, resource and feasibility record, measure and model stewardship, monitoring plan, escalation and fallback thresholds, ownership map, disagreement record, reproducibility audit, responsible-claims audit, AI-use record, and defense.

Leadership must address blame, staff voice, patient access, uncertainty, operational burden, safety, and who has authority to pause or restart. Package acceptance and permission to run a real test remain separate decisions.

## 16. Three cumulative checkpoint contracts

### Checkpoint 1: Measures, variation, and bottleneck readiness

- Timing: end of instructional Week 3.
- Course points: 40.
- Future package path: `courses/clinical-performance-improvement/checkpoints/01-measures-variation-readiness/`.
- Future specification: `docs/curriculum/courses/APP-3/checkpoints/01-measures-variation-readiness-spec.md`.
- Decision: may the accepted service definition, measures, diagnostic, and escalation logic enter forecasting and scenario work?

Required evidence includes the Module 01 charter and source audit; exact public and synthetic release identities; unit of flow; measure family; accountability and claim boundaries; SQL measure build; event validation; defects and repairs; operational metrics; process map; chart-selection record; exact control-chart calculations; signal-rule audit; safety-source limitations; bottleneck reconciliation; subgroup support; 40-point score; gates; AI record; defense; and progression decision.

The checkpoint counts the 20-point Module 02 and 20-point Module 03 components once. Module 01 adds no points but is a required gate.

### Checkpoint 2: Forecast, scenario, evaluation, and monitoring release

- Timing: end of instructional Week 6.
- Course points: 25.
- Future package path: `courses/clinical-performance-improvement/checkpoints/02-forecast-scenario-monitoring-release/`.
- Future specification: `docs/curriculum/courses/APP-3/checkpoints/02-forecast-scenario-monitoring-release-spec.md`.
- Decision: is the analytic case strong enough for clinician leadership review?

Required evidence includes accepted Week 3 identity; forecast contract; temporal folds; benchmark and smoothing predictions; exact errors and cost of error; residual and failure evidence; Little's Law limit; capacity implication; scenario contract; seeds and replications; scenario validation; baseline and redesign results; sensitivity; evaluation threats; gaming and unintended effects; feasibility; access and equity; workforce burden; implementation, process, outcome, safety, and balancing measures; dashboard and exact table; escalation and fallback rules; transparent-versus-ML comparison; leakage tests; 25-point score; gates; AI record; defense; and progression decision.

The checkpoint counts the 25-point Module 05 component once. Module 04 supplies required forecast evidence and Module 06 supplies required application and ML gates without adding points.

### Final checkpoint: Clinical performance improvement package

- Timing: official last day of the assigned half-term.
- Course points: 35.
- Future package path: `courses/clinical-performance-improvement/checkpoints/03-clinical-performance-improvement-package/`.
- Future specification: `docs/curriculum/courses/APP-3/checkpoints/03-clinical-performance-improvement-package-spec.md`.
- Decision: should the fictional service propose a bounded prospective test, revise, refer, or stop?

Required evidence includes both accepted checkpoints; immutable candidate manifest; final reproducible repository; evidence synthesis; frontline brief; leadership summary; recommendation and alternatives; feasibility and resource record; measure, forecast, scenario, and ML stewardship; monitoring schedule; implementation, process, outcome, safety, access, workforce, and balancing measures; escalation, stop, fallback, and restart rules; accountability and disagreement records; accessible exact evidence; technical appendix; AI and claims audit; 35-point score; gates; defense; reviewer record; reproduction; conditions; and separate package and test recommendations.

The final checkpoint adds 35 points once, giving a course total of `40 + 25 + 35 = 100` with no duplication.

## 17. Assessment map and grading rules

| Source assessment | Feedback milestone | Cumulative checkpoint | Course points |
|---|---|---|---:|
| Measure and operational metric build | End of Week 2 | Week 3 | 20 |
| Performance diagnostic | End of Week 3 | Week 3 | 20 |
| Forecast, scenario, and evaluation | End of Week 5 | Week 6 | 25 |
| Clinical performance improvement package | End of Week 7 | Official half-term end date | 35 |
| Total |  |  | 100 |

Every component uses five recurring criteria: correct, reproducible, sound clinical performance reasoning, clear and action-guiding, and responsible agent use.

A numeric threshold cannot compensate for a wrong source, unit of flow, numerator, denominator, event clock, chart family, control limit, information cutoff, forecast fold, scenario assumption, synthetic label, balancing measure, inaccessible output, unsupported causal claim, or missing owner.

## 18. Software, reproducibility, and data policy

SQL owns linked event, state, measure, denominator, and time-window logic. Python owns source checks, operational metrics, control charts, forecasts, scenarios, ML, accessible exact exports, and validation. R output is read and interpreted when a supported runtime is available. Git records reviewed versions and immutable handoffs.

Every public source is pinned by landing page, resource URL, release date, retrieval date, bytes, hash, rows, fields, rights, grain, reporting period, and completeness. A build must inspect the full accepted release before deriving a teaching selection. When a full binary is too large for Git, the source record retains the complete identity and acquisition procedure, and the deterministic selection code proves what was retained.

Synthetic data require a generator, version, seed, known-truth contract, relationship tests, source-influence record, explicit flag, rows, bytes, hashes, and defect registry. A raw synthetic layer remains immutable. Repairs occur in a derived layer through tested code.

Every module must provide a complete reference, incomplete learner template, instructor material, assessment, rubric, source and data specification, release record, semantic version, deterministic builder, validator, failure self-check, and protected handoff.

## 19. Accessibility, equity, privacy, and responsible claims

Every display has an exact table and structured text alternative. Control-chart, forecast, scenario, and monitoring cues use text or shape in addition to color. Units, periods, centerlines, limits, forecast origins, intervals when used, denominators, unavailable states, and threshold origins remain available outside the figure.

Every subgroup review begins with eligibility, denominator, event count, missingness, support, uncertainty, and suppression. Learners may identify a supported access or burden concern. They may not turn a synthetic difference into a claim about a real group or treat one outcome as a group trait.

No protected or identifiable patient or workforce data enter the repository or an external agent. Public facility data remain public but are not used for unsupported ranking or local performance claims. Synthetic staff workload is not employee surveillance.

Public aggregate reporting does not establish current local performance. A control-chart signal does not establish cause. Incident reports do not estimate prevalence. A forecast does not guarantee demand. A scenario does not prove intervention effect. Package acceptance does not authorize a test.

## 20. Agent policy and accountability

Agents may explain code, suggest tests, diagnose measure and time-order errors, draft documentation, and help review a bounded forecast or scenario. The learner records the tool, purpose, prompt, data classes, affected files, output used or rejected, material claims, independent check, corrections, retained limits, and human owner.

Required verification includes source fingerprints, denominator logic, event order, queue conservation, control-chart calculations, signal rules, forecast folds, future-row exclusion, forecast errors, scenario assumptions, random seeds, scenario conservation, ML feature eligibility, score totals, and decision language.

Prohibited use includes protected or workplace data, hidden assistance, fabricated execution or review evidence, unverified safety claims, silent change to accepted evidence, synthetic-as-real language, and using repeated agent output as independent confirmation.

The learner remains accountable for every number, safety statement, staffing implication, threshold, and recommendation.

## 21. Instruction, feedback, and clinician leadership

Learners receive a weekly clinical performance case walkthrough, data or methods lab, structured critique, question clinic, and monitored help channel. Targeted feedback follows the Week 2 measure build, Week 3 diagnostic, Week 5 forecast and scenario, and Week 6 draft package.

Joe Joseph, MD, SFHM, is the designated clinician for Module 07 under the dated identity boundary recorded in the master architecture. The course makes no current-employer or current-title claim. Participation, schedule, format, recording permission, and final biography wording require direct confirmation.

The final clinician session addresses how leaders respond to uncertain operational signals, avoid blame, listen to frontline and patient consequences, decide what is feasible, assign ownership, set stop rules, and distinguish a good analytic package from permission to change care or staffing.

## 22. Reviewer roles and release gates

| Role | Main responsibility |
|---|---|
| APP-3 faculty owner | outcomes, workload, scoring, checkpoints, and progression |
| Clinical performance and quality reviewer | measure family, improvement aim, interpretation, and action boundary |
| Emergency care clinician | clinical flow, safety meaning, feasibility, escalation, and defense |
| Nursing and operations reviewer | staffing, handoffs, queue assumptions, workload, and fallback |
| Measure steward | numerator, denominator, exclusions, events, attribution, refresh, and ownership |
| Statistical process control reviewer | chart choice, limits, signal rules, phase changes, and small numbers |
| Patient-safety reviewer | events, near misses, triggers, underreporting, surveillance bias, and harm claims |
| Forecasting reviewer | target, cutoff, folds, benchmarks, error, structural change, and use limit |
| Operations-research reviewer | scenario structure, conservation, seeds, replications, sensitivity, and scope |
| Equity and access reviewer | subgroup support, exclusion, burden, language, disability access, and reporting |
| Workforce reviewer | workload, overtime, interruptions, feasibility, and surveillance boundary |
| Accessibility reviewer | figure, table, text, contrast, keyboard, and equivalent-evidence review |
| Model evaluation reviewer | simple-versus-ML comparability, leakage, errors, failures, and decision change |
| Privacy and governance reviewer | public rights, synthetic boundary, prompts, permitted use, and conditions |
| Responsible-AI reviewer | trace, independent checks, corrections, and human ownership |
| Independent reproducer | clean build, exact outputs, hidden dependencies, and release identity |

Noncompensable release gates include:

1. exact course and data source identities;
2. full-source inspection before teaching selection;
3. explicit synthetic institution and row labels;
4. no public-facility-to-synthetic-service linkage;
5. valid measure definitions and independent recalculation;
6. correct time order, event order, and queue conservation;
7. chart family and control limits matched to the data;
8. signal language kept separate from causal language;
9. incident undercapture and review status retained;
10. forecast benchmarks, cutoffs, folds, errors, and failures retained;
11. scenario assumptions, seeds, replications, and sensitivity retained;
12. access, equity, safety, workforce, and balancing measures retained;
13. ML uses identical target, information, folds, horizons, and evaluation rows;
14. all displays have exact accessible alternatives;
15. all score components counted once;
16. required AI trace and independent checks complete;
17. named conditions retained through handoff; and
18. package acceptance kept separate from test or implementation authority.

Curriculum-construction references may proceed with named conditions. Alpha requires program and human review. No release authorizes a real workflow or staffing change.

## 23. Durable paths and build order

- Course specification: `docs/curriculum/courses/APP-3/course-spec.md`.
- Source record: `docs/source/app-3-clinical-performance-improvement-source-record.md`.
- Course package: `courses/clinical-performance-improvement/`.
- Build ledger: `docs/curriculum/BUILD-LEDGER.md`.

Module specification paths:

1. `docs/curriculum/courses/APP-3/modules/01-clinical-performance-decision-spec.md`.
2. `docs/curriculum/courses/APP-3/modules/02-measures-operational-metrics-spec.md`.
3. `docs/curriculum/courses/APP-3/modules/03-variation-safety-bottlenecks-spec.md`.
4. `docs/curriculum/courses/APP-3/modules/04-demand-forecasting-capacity-spec.md`.
5. `docs/curriculum/courses/APP-3/modules/05-improvement-scenarios-evaluation-spec.md`.
6. `docs/curriculum/courses/APP-3/modules/06-feasibility-monitoring-embedded-ml-spec.md`.
7. `docs/curriculum/courses/APP-3/modules/07-clinician-leadership-defense-spec.md`.

Checkpoint specification paths:

1. `docs/curriculum/courses/APP-3/checkpoints/01-measures-variation-readiness-spec.md`.
2. `docs/curriculum/courses/APP-3/checkpoints/02-forecast-scenario-monitoring-release-spec.md`.
3. `docs/curriculum/courses/APP-3/checkpoints/03-clinical-performance-improvement-package-spec.md`.

Build Modules 01 through 07 in order. Build each checkpoint after its upstream modules. Every unit receives a durable specification, learner package, complete reference, instructor materials, exact data or accepted handoff, checks, release record, semantic-version decision, commit, push, and ledger handoff before the next unit.

## 24. Known issues and construction acceptance

Open conditions before alpha:

- Confirm Joe Joseph's participation, schedule, format, recording permission, and final biography wording.
- Assign the official course section and half-term dates before publishing due dates.
- Pin and fingerprint the exact full CMS Complications and Deaths release used by Module 01.
- Pin and fingerprint the exact full HHS historical capacity snapshot or document why its complete binary cannot be retained in Git.
- Complete human review of the synthetic operational generator, known truth, subgroup design, safety events, staffing assumptions, and workload language.
- Declare the exact control-chart families and signal rules after the generated measure distributions are accepted.
- Declare the exact forecast horizon, rolling-origin folds, benchmark eligibility, and error-cost assumptions after the synthetic calendar-demand release is accepted.
- Declare the scenario warm-up, replications, seeds, conservation checks, and decision thresholds after the baseline model is validated.
- Declare the ML decision-change threshold before fitting the ML candidate.
- Confirm SimPy, statsmodels, R, qcc, and a supported forecasting package in one teaching environment, or document a tested course-supported alternative.
- Name the faculty, clinical, nursing, operations, measurement, process-control, safety, forecasting, operations-research, workforce, equity, accessibility, governance, model, responsible-AI, and independent-reproduction reviewers.

Construction acceptance for this course-level unit:

- [x] The exact DOCX source is fingerprinted in both archives.
- [x] Seven distinct modules total 112.5 hours.
- [x] The source assessment weights are preserved as 40, 25, and 35 checkpoint points.
- [x] Modules 01 through 03 form the technical block.
- [x] Modules 04 through 06 form the application block.
- [x] Module 06 contains an eight-hour embedded ML extension.
- [x] Module 07 is clinician led.
- [x] The continuing decision uses an explicitly fictional service.
- [x] Full public quality, safety, and capacity sources have declared roles and boundaries.
- [x] Synthetic operational data have a required table, truth, provenance, and validation contract.
- [x] Every checkpoint has a decision, points, evidence, and protected handoff.
- [x] APP-3 remains distinct from FND-1, FND-2, APP-1, APP-2, and DA-730.
- [ ] Module 01 is not yet built.

Resume with Module 01 only: pin the remaining full public releases, build the source-feasibility and decision-framing workspace, validate it, update semver and the ledger, commit, and push before Module 02 begins.
