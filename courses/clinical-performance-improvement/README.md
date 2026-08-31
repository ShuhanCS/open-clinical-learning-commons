# APP-3: Data for Clinical Performance and Improvement

- Course ID: APP-3.
- Credits: 3.
- Prerequisites: FND-1 and FND-2.
- Total learner work: 112.5 hours.
- Current Commons release: 0.71.0.
- Current build: course specification, source architecture, Modules 01 through 05, and Checkpoint 01 complete; later modules and checkpoints not yet built.

APP-3 teaches learners to define and validate clinical performance measures, distinguish process signals from routine variation, diagnose bottlenecks, forecast demand, test capacity and workflow scenarios, and defend a monitored improvement recommendation.

The continuing case is an explicitly fictional adult emergency service, `CGH-ED-01`. Public CMS quality and safety releases and historical HHS capacity data supply measure definitions and external context. A versioned synthetic operational layer supplies the linked process, staffing, queue, safety, demand, and known-truth evidence that public sources do not contain.

## Module sequence

| Module | Title | Hours | Build status |
|---:|---|---:|---|
| 01 | Framing a clinical performance and improvement decision | 15.5 | Runnable release candidate |
| 02 | Measures and operational metrics | 16.0 | Runnable release candidate |
| 03 | Variation, safety signals, and bottlenecks | 16.5 | Runnable release candidate |
| 04 | Demand forecasting and capacity | 16.5 | Runnable release candidate |
| 05 | Improvement scenarios and evaluation | 16.0 | Runnable release candidate |
| 06 | Feasibility, monitoring, and embedded machine learning | 16.0 | Specified in course contract |
| 07 | Clinician leadership, recommendation, and defense | 16.0 | Specified in course contract |
| Total |  | 112.5 |  |

## Checkpoints

- Week 3: [40-point measures, variation, safety, and bottleneck readiness package](checkpoints/01-measures-variation-readiness/reference/README.md).
- Week 6: 25-point forecast, scenario, evaluation, and monitoring package.
- Official half-term end date: 35-point clinical performance improvement package.

The Week 3 checkpoint combines the source course's 20-point measure build and 20-point performance diagnostic. The Week 6 checkpoint carries the source course's 25-point forecast, scenario, and evaluation assessment. Module 06 adds required feasibility, monitoring, and simple-versus-ML gates without adding course points.

## Public and synthetic sources

- CMS Timely and Effective Care - Hospital: https://data.cms.gov/provider-data/dataset/yv7e-xc69
- CMS Complications and Deaths - Hospital: https://data.cms.gov/provider-data/dataset/ynj2-r877
- HHS historical facility capacity: https://healthdata.gov/Hospital/COVID-19-Reported-Patient-Impact-and-Hospital-Capa/anag-cw7u
- Synthetic service: `CGH-ED-01`, generated and labeled as teaching data only.

The full course contract is [the APP-3 course specification](../../docs/curriculum/courses/APP-3/course-spec.md). Source normalization and data routing are recorded in [the APP-3 source record](../../docs/source/app-3-clinical-performance-improvement-source-record.md).

The first runnable package is [Module 01](modules/01-clinical-performance-decision/README.md), governed by its [durable specification](../../docs/curriculum/courses/APP-3/modules/01-clinical-performance-decision-spec.md). It defines the fictional service, unit of flow, process boundary, measure families, source feasibility, accountability, claim limits, and Module 02 progression decision.

The second runnable package is [Module 02](modules/02-measures-operational-metrics/README.md), governed by its [durable specification](../../docs/curriculum/courses/APP-3/modules/02-measures-operational-metrics-spec.md). It generates 318,732 linked synthetic operational rows, preserves 12 raw defects, defines 17 measures, produces eight accepted outputs, awards the 20-point Week 3 measure component, and passes 15 release gates before Module 03 begins.

The third runnable package is [Module 03](modules/03-variation-safety-bottlenecks/README.md), governed by its [durable specification](../../docs/curriculum/courses/APP-3/modules/03-variation-safety-bottlenecks-spec.md). It produces 13 diagnostic outputs, four accessible figures, nine audited signals, exact safety-surveillance evidence, a bounded stage diagnosis, and one human escalation rule. Its 20-point component completes the evidence needed to build the 40-point Week 3 checkpoint.

The cumulative [Week 3 checkpoint](checkpoints/01-measures-variation-readiness/reference/README.md), governed by its [durable specification](../../docs/curriculum/courses/APP-3/checkpoints/01-measures-variation-readiness-spec.md), freezes 137 accepted module files in a 153-file assembly. It counts the Module 02 and Module 03 20-point components once, passes 18 checkpoint integrity gates, and uses a 12-question defense before permitting Module 04 demand forecasting and capacity analysis with conditions.

The fourth runnable package is [Module 04](modules/04-demand-forecasting-capacity/README.md), governed by its [durable specification](../../docs/curriculum/courses/APP-3/modules/04-demand-forecasting-capacity-spec.md). It compares three transparent methods on 28 common rolling origins, selects bounded seasonal exponential smoothing, releases the Week 53 point and empirical range, and passes 18 zero-point gates before permitting Module 05 scenario construction with conditions.

The fifth runnable package is [Module 05](modules/05-improvement-scenarios-evaluation/README.md), governed by its [durable specification](../../docs/curriculum/courses/APP-3/modules/05-improvement-scenarios-evaluation-spec.md). It runs 4,000 paired scenario simulations across five conditions, retains six null or failed comparisons, defines 12 prospective measures and eight evaluation threats, awards the 25-point component once, and passes 20 gates. No option clears the predeclared decision rule, so Module 06 receives a bounded no-selection result without implementation authority.

No package authorizes clinical implementation, current hospital performance judgment, patient or workforce targeting, staffing change, or model deployment.
