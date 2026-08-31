# APP-3 Module 05 build plan

## Objective

Build the 16-hour APP-3 Module 05 package, `Improvement scenarios and evaluation`, from the accepted Week 3 diagnosis and Module 04 forecast release. Learners will configure a provided discrete-event model, compare no change with three bounded options, retain failed conditions, and propose an evaluation design without treating simulated results as real intervention effects.

Module 05 owns the complete 25-point `Forecast, scenario, and evaluation` source assessment. The accepted Module 04 forecast is a required input and receives no duplicate points.

## Fixed upstream handoff

- Accepted Module 04: `oclc-app3-04` version `0.1.0` at Commons release `0.70.0`.
- Accepted forecast: seasonal exponential smoothing.
- Week 53 point demand: 876.924084 arrivals.
- Empirical demand range: 805.136639 to 970.733035 arrivals.
- Point planning conversion: 841.847121 historical clinician-hour equivalents.
- Planning range: 772.931174 to 931.903714 historical clinician-hour equivalents.
- Mean absolute weekly error: 64.678197 arrivals.
- Difficult folds: F03, F09, F15, and F16.
- Unsupported slice: nine holiday shifts.
- Accepted Week 3 diagnosis: roomed-to-clinician constraint on evening shifts in Weeks 35 through 44.
- Staffing, clinical, automated, causal, scenario-effect, and implementation authority: not authorized.

Module 05 will freeze the exact Module 04 release, contract, outputs, decision records, accepted encounter measures, source scenario register, known truth, and staffing evidence needed to reproduce the scenario inputs. A file-level manifest will protect the handoff.

## Predeclared scenario contract

### Decision

Decide which option, if any, deserves feasibility and monitoring review in Module 06:

1. S00, no change;
2. S01, flex clinician coverage;
3. S02, fast-track activation; and
4. S03, combined bounded rule.

This is a curriculum progression decision. It is not permission to change staffing, open a real fast track, alter patient routing, or run a clinical test.

### Time and demand

- Warm-up: seven days using the same 21-shift demand shape.
- Measurement: the following seven days.
- Replications: 200 paired replications per scenario and condition.
- Common random numbers: each scenario receives the same arrival and patient-profile realization within a condition and replication.
- Base seed: 7300500, with deterministic condition and replication offsets.
- Arrivals: nonhomogeneous Poisson arrivals within each eight-hour shift.
- Shift demand shape: the accepted Week 53 forecast.
- Measurement population: all synthetic arrivals during the measurement week.

### Patient and service inputs

- Acuity and access-support profiles come from the accepted 43,628-encounter measure release.
- Pre-clinician preparation and clinician-to-departure donors come from accepted completed encounters matched by shift, acuity, and access-support group.
- Priority is nonpreemptive and acuity ordered, with acuity 1 highest.
- Base clinician capacity uses a transparent guided-model schedule: 2 night, 6 day, and 4 evening slots. The first full run at 3, 7, and 5 produced a 55-minute no-change median and too little queue response to distinguish the options. The lower schedule was predeclared before release, keeps no-change abandonment within the broad 4 to 15 percent calibration range, and is a teaching assumption rather than an observed staffing count.
- Effective clinician service time is 20 percent of observed clinician-to-departure elapsed time. This is a transparent teaching proxy for intermittent clinician work, not a productivity estimate.
- Low-acuity abandonment follows the declared synthetic delay mechanism used by the accepted source generator.

### Scenario rules

- S00 changes nothing.
- S01 adds one synthetic clinician slot for a shift when its accepted forecast meets the historical shift-specific 75th-percentile arrival threshold: 32 night, 55 day, or 48 evening arrivals.
- S02 activates a bounded low-acuity fast-track lane after at least four patients wait for 15 minutes. It adds no staff. Eligible acuity 4 and 5 service time is multiplied by 0.70 while active.
- S03 requires both a forecast-threshold-eligible shift and the same sustained queue threshold. Once active, it adds one synthetic clinician slot and applies the bounded fast-track rule for the rest of the shift.
- Every support group remains eligible. The model does not use support need to deny routing.

### Sensitivity conditions

1. C01, lower demand: 805.136639 expected weekly arrivals.
2. C02, point demand: 876.924084 expected weekly arrivals.
3. C03, upper demand: 970.733035 expected weekly arrivals.
4. C04, stress: upper demand and service times 15 percent longer.
5. C05, weak workflow effect: point demand and fast-track service multiplier 0.90.

The release must retain a null or failed improvement condition. It may not delete a condition because an option performs poorly.

## Required outcomes and limits

Every scenario-condition result will report:

- arrivals;
- arrival-to-clinician median and 90th percentile;
- arrival-to-departure median;
- completed throughput;
- left-before-seen count and percent;
- clinician utilization;
- modeled overtime hours;
- flex clinician-hours;
- trigger count and activation delay;
- standard, language-support, and mobility-support wait;
- language and mobility gaps relative to standard;
- queue maximum;
- safety outcome status;
- 72-hour return status; and
- conservation status.

The model does not contain a validated causal mechanism for safety events or 72-hour returns. Both must appear as `not simulated; prospective measurement required`. A missing outcome is not allowed, and an unmodeled outcome cannot be presented as improved.

## Option qualification and selection

At point demand, an option qualifies for feasibility review only if paired median effects meet all of these rules:

- median arrival-to-clinician improves by at least 10 minutes;
- 90th-percentile arrival-to-clinician improves by at least 15 minutes;
- left-before-seen improves by at least 1.0 percentage point;
- throughput does not fall by more than 1 percent;
- the language-support wait gap does not worsen by more than 5 minutes;
- median arrival-to-clinician remains better than no change under C04 stress;
- all conservation and model-validation checks pass; and
- safety and returns remain explicitly unmodeled.

If multiple options qualify and their point-demand median wait improvements differ by no more than 5 minutes, prefer fewer flex clinician-hours. Otherwise prefer the largest point-demand median wait improvement. The decision may be `none` if no option qualifies.

## Evaluation design contract

The proposed real-world evaluation remains future and unauthorized. Learners will specify:

- the existing Week 3 chart and baseline as the process-monitoring foundation;
- a prospective start date only after authority and readiness review;
- a stabilization period rather than an unexamined before-and-after mean;
- primary process, outcome, safety, access, workforce, and balancing measures;
- subgroup support rules and unavailable states;
- secular trend, regression to the mean, measurement change, concurrent intervention, case mix, and gaming checks;
- human escalation, pause, fallback, and restart ownership; and
- the evidence needed before any causal statement.

The module can propose a monitored evaluation. It cannot claim that a simulated option caused a real improvement.

## Deterministic outputs

`build_scenarios.py` will create:

1. `input-profile.csv`;
2. `condition-register.csv`;
3. `validation-checks.csv`;
4. `replication-results.csv`;
5. `scenario-summary.csv`;
6. `paired-effects.csv`;
7. `sensitivity-review.csv`;
8. `evaluation-measures.csv`;
9. `evaluation-threats.csv`;
10. `scenario-findings.json`;
11. `point-demand-tradeoffs.svg`; and
12. `sensitivity-wait-effects.svg`.

The builder will use the Python standard library, produce stable bytes, refuse an existing target, verify exact source identities, and reproduce committed outputs byte for byte.

## Learner and reference records

1. `scenario-assumption-register.csv`;
2. `scenario-validation.md`;
3. `scenario-comparison.md`;
4. `sensitivity-interpretation.md`;
5. `access-workforce-safety-review.md`;
6. `evaluation-design.md`;
7. `evaluation-threat-audit.csv`;
8. `gaming-unintended-effects.md`;
9. `week6-score.csv`;
10. `gate-results.csv`;
11. `module06-handoff.md`;
12. `ai-use.md`;
13. `progression-decision.md`; and
14. `reproducibility-check.md`.

## Assessment

The 25 points are counted once:

- frozen forecast and scenario contract: 3 points;
- model validation and conservation: 5 points;
- scenario comparison: 5 points;
- sensitivity and tradeoffs: 4 points;
- evaluation design and threats: 5 points; and
- reproducibility, communication, and responsible AI: 3 points.

All noncompensable gates must pass. A strong numeric result cannot compensate for altered upstream evidence, failed conservation, hidden null results, missing access or workforce evidence, unmodeled safety claims, or implementation language.

## Release handoff

The deterministic reference build produced 4,000 runs, 20 scenario-condition summaries, 15 paired-effect rows, and 6 retained null or failed comparisons. No option cleared every point-demand and stress gate. S01 improved P90 wait by 21.244986 minutes but missed the median-wait rule. S02 improved completion while worsening median and P90 waits. S03 missed both point-demand wait rules. The accepted handoff is therefore no selected option, with progression to Module 06 under conditions and without implementation authority.

- Module version: 0.1.0.
- Commons release target: 0.71.0.
- Next unit: APP-3 Module 06, `Feasibility, monitoring, and embedded machine learning`.
- Module 06 permission requires the exact 25-point score, passing gates, retained sensitivity conditions, bounded scenario decision, and explicit absence of implementation authority.
