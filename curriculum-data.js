(function () {
  "use strict";

  const curriculum = {
  "version": "0.27.0",
  "courseCount": 11,
  "moduleCount": 77,
  "courses": [
    {
      "id": "FND-1",
      "stage": "Foundation",
      "title": "Healthcare Data Foundations",
      "credits": 3,
      "format": "Seven-week online block",
      "prerequisites": "None",
      "summary": "Build, check, describe, and hand off healthcare data another analyst can trust.",
      "finalDeliverable": "Final toolkit package: SQL, notebook, README, version tag, data brief.",
      "modules": [
        {
          "week": 1,
          "title": "Setting up a reproducible workspace",
          "outcome": "Set up a working analytic environment and explain why reproducibility is part of data quality.",
          "topics": "Environments, Git, version numbers, reproducibility, AI-use disclosure.",
          "submission": "Working repository, versioned setup check, environment note, AI-use statement.",
          "hours": 15.5
        },
        {
          "week": 2,
          "title": "Databases and retrieving data",
          "outcome": "Explain what a database is and retrieve healthcare records from one.",
          "topics": "Relational model, schemas, keys, table grain, healthcare source systems, FHIR and JSON basics.",
          "submission": "Data model diagram, schema notes, first SQL extracts.",
          "hours": 16
        },
        {
          "week": 3,
          "title": "Cohorts and analytic tables",
          "outcome": "Build a validated cohort and a derived analytic table.",
          "topics": "Joins, aggregation, common table expressions, index dates, time windows, inclusion and exclusion logic, attrition, denominators.",
          "submission": "Tested SQL cohort, cohort flow counts, table specification.",
          "hours": 16.5
        },
        {
          "week": 4,
          "title": "Cleaning and profiling",
          "outcome": "Clean and profile a dataset and decide whether to stop, fix, or proceed.",
          "topics": "Tidy data, types, missingness, outliers, coding changes, data-quality dimensions, small-cell caution.",
          "submission": "Data-quality notebook, quality-risk log, stop/fix/proceed recommendation.",
          "hours": 16.5
        },
        {
          "week": 5,
          "title": "Descriptive results",
          "outcome": "Produce descriptive results that retain their clinical meaning.",
          "topics": "Single-variable and two-variable summaries, cross-tabs, rates, denominators, stratification, multivariable tables.",
          "submission": "Descriptive analysis notebook and interpretation memo.",
          "hours": 16
        },
        {
          "week": 6,
          "title": "Accessible charts and time-indexed data",
          "outcome": "Build accessible charts and simple exploratory outputs for review.",
          "topics": "Chart choice, accessibility, subgroup and uncertainty display, time-indexed signals, avoiding false cause.",
          "submission": "Accessible chart set, exploratory notebook section.",
          "hours": 16,
          "resource": {
            "title": "Clinical visualization atlas",
            "description": "Choose, read, and rebuild healthcare charts with a synthetic emergency department case.",
            "url": "courses/data-visualization/atlas.html#atlas"
          }
        },
        {
          "week": 7,
          "title": "Reproducible handoff and AI audit",
          "outcome": "Package a reproducible workflow and audit the steps where you used AI.",
          "topics": "Reproducible handoff, release notes, code review, provenance, review of AI output.",
          "submission": "Final toolkit package: SQL, notebook, README, version tag, data brief.",
          "hours": 16
        }
      ]
    },
    {
      "id": "FND-2",
      "stage": "Foundation",
      "title": "Modeling, Inference, and Reproducible Analytics",
      "credits": 3,
      "format": "Seven-week online block",
      "prerequisites": "FND-1",
      "summary": "Turn checked data into analytic evidence and defend the method, assumptions, claims, and monitoring plan.",
      "finalDeliverable": "Final model or agent-assisted analytics package with a model card.",
      "modules": [
        {
          "week": 1,
          "title": "Analytic aims and a reproducible modeling workspace",
          "outcome": "Classify an analytic aim and stand up a reproducible modeling workspace.",
          "topics": "Analytic aim taxonomy, estimands, method families, data leakage, train and test roles, SQL-to-model pipelines, baseline models.",
          "submission": "Aim-and-method plan, reproducible modeling repository, baseline model.",
          "hours": 15.5
        },
        {
          "week": 2,
          "title": "Regression models and interpretation",
          "outcome": "Fit, interpret, and check regression models for healthcare questions.",
          "topics": "Linear regression, logistic regression, assumptions, nonlinear terms, interactions, effect estimates, confidence intervals, odds and risk.",
          "submission": "Regression interpretation and assumption lab.",
          "hours": 16
        },
        {
          "week": 3,
          "title": "Prediction workflows and evaluation",
          "outcome": "Build a prediction workflow and judge whether it is valid enough to use.",
          "topics": "Feature preparation, resampling, temporal split, discrimination, calibration, thresholds, class imbalance, subgroup performance.",
          "submission": "Prediction evaluation report.",
          "hours": 16.5
        },
        {
          "week": 4,
          "title": "Adjustment, missing data, and longitudinal structure",
          "outcome": "Evaluate adjusted and longitudinal situations without overclaiming.",
          "topics": "Causal diagrams, confounding, propensity-score adjustment, missing-data mechanisms, sensitivity analysis, repeated measures, mixed models, survival basics.",
          "submission": "Validity, adjustment, and longitudinal-method memo.",
          "hours": 16.5
        },
        {
          "week": 5,
          "title": "Forecasting and temporal validation",
          "outcome": "Build an introductory forecast and validate it over time.",
          "topics": "Forecast aim and horizon, temporal validation, backtesting, decomposition, smoothing, stationarity, ARIMA-family concepts, error metrics.",
          "submission": "Forecasting and temporal validation checkpoint.",
          "hours": 16
        },
        {
          "week": 6,
          "title": "Agent-assisted modeling and testing",
          "outcome": "Use analytic agents safely for modeling support, testing, and documentation.",
          "topics": "Agent task decomposition, prompt constraints, generation limits, unit and data tests, model critique, hallucination checks, trace logs, human sign-off.",
          "submission": "Agent-assisted model review log and test suite.",
          "hours": 16
        },
        {
          "week": 7,
          "title": "Model cards, governance, and defense",
          "outcome": "Package, defend, and govern a model or agent-assisted workflow.",
          "topics": "Model cards, intended use, subgroup and equity review, monitoring, drift, retraining triggers, rollback and stop rules, reproducibility audit.",
          "submission": "Final model or agent-assisted analytics package with a model card.",
          "hours": 16
        }
      ]
    },
    {
      "id": "APP-1",
      "stage": "Applied",
      "title": "Data for Clinical Care",
      "credits": 3,
      "format": "Seven-week online block",
      "prerequisites": "FND-1 and FND-2",
      "summary": "Follow a clinical cohort over time, compare outcomes fairly, and recommend a feasible care-pathway improvement.",
      "finalDeliverable": "Final clinical care improvement brief.",
      "modules": [
        {
          "week": 1,
          "title": "Framing a care-pathway decision",
          "outcome": "Frame a care-pathway decision around a patient population, treatment or exposure, clinical outcomes, and a feasible improvement.",
          "topics": "Clinical pathways, outcome sets, comparison groups, evidence standards, audience and stakeholder definition.",
          "submission": "Care-pathway decision charter.",
          "hours": 15.5
        },
        {
          "week": 2,
          "title": "Longitudinal cohorts and follow-up",
          "outcome": "Define and validate a longitudinal clinical cohort with follow-up time.",
          "topics": "Clinical phenotyping, index events, lookback and follow-up windows, outcome definitions, censoring setup, event and procedure logic.",
          "submission": "Validated phenotype and cohort with follow-up.",
          "hours": 16
        },
        {
          "week": 3,
          "title": "Survival and time-to-event outcomes",
          "outcome": "Analyze time-to-event outcomes along the pathway with survival methods.",
          "topics": "Censoring, Kaplan-Meier curves, log-rank comparison, Cox proportional hazards, hazard ratios, competing risks.",
          "submission": "Survival analysis notebook.",
          "hours": 16.5
        },
        {
          "week": 4,
          "title": "Risk adjustment and fair comparison",
          "outcome": "Compare outcomes fairly across patients and sites with risk adjustment.",
          "topics": "Case mix, baseline severity, risk-adjustment models, observed-to-expected ratios, standardized rates, model interpretation for clinicians.",
          "submission": "Risk-adjusted comparison and interpretation memo.",
          "hours": 16.5
        },
        {
          "week": 5,
          "title": "Clinical variation and patterns of care",
          "outcome": "Examine variation in treatment, utilization, and clinical outcomes.",
          "topics": "Treatment and practice variation, adherence and exposure, utilization patterns, site comparison, clinical significance, residual confounding.",
          "submission": "Clinical variation memo.",
          "hours": 16
        },
        {
          "week": 6,
          "title": "Equity, variation, and a feasible improvement",
          "outcome": "Identify equity concerns and shape a feasible care-pathway improvement.",
          "topics": "Subgroup analysis, health equity, pathway visualization, driver diagrams, improvement metrics, feasibility, unintended consequences.",
          "submission": "Equity checkpoint and draft improvement brief.",
          "hours": 16
        },
        {
          "week": 7,
          "title": "Integrated recommendation",
          "outcome": "Defend a clinical care recommendation and evaluation plan.",
          "topics": "Evidence synthesis, clinical communication, implementation and evaluation metrics, responsible claims, next-step measurement.",
          "submission": "Final clinical care improvement brief.",
          "hours": 16
        }
      ]
    },
    {
      "id": "APP-2",
      "stage": "Applied",
      "title": "Data for Patient Experience and Engagement",
      "credits": 3,
      "format": "Seven-week online block",
      "prerequisites": "FND-1 and FND-2",
      "summary": "Treat patient reports about health, access, communication, and trust as evidence for improving care.",
      "finalDeliverable": "Final patient-experience and engagement package.",
      "modules": [
        {
          "week": 1,
          "title": "Framing a patient-experience and engagement decision",
          "outcome": "Frame a patient-experience or engagement decision with patient partners and a clear action.",
          "topics": "Patient experience, engagement, partnership, PROMs and PREMs, journey mapping, evidence needs, accountable decisions.",
          "submission": "Patient-experience decision charter.",
          "hours": 15.5
        },
        {
          "week": 2,
          "title": "Patient-reported measurement",
          "outcome": "Select and interpret measures that fit the patient question.",
          "topics": "Instrument selection, validity, reliability, scoring, meaningful change, language and accessibility, measurement burden.",
          "submission": "Patient-measurement lab.",
          "hours": 16
        },
        {
          "week": 3,
          "title": "Response, representation, and bias",
          "outcome": "Determine who the data represent and who is missing.",
          "topics": "Sampling, coverage, response rates, nonresponse, missingness, mode effects, weighting, privacy and consent.",
          "submission": "Response and representation audit.",
          "hours": 16.5
        },
        {
          "week": 4,
          "title": "Linked patient evidence",
          "outcome": "Link experience with access, communication, engagement, and service-use data.",
          "topics": "Data linkage, access measures, portal and digital engagement, communication, navigation, governance, denominator alignment.",
          "submission": "Linked patient-evidence analysis.",
          "hours": 16.5
        },
        {
          "week": 5,
          "title": "Patient voice, group differences, and equity",
          "outcome": "Analyze comments and group differences without overstating the evidence.",
          "topics": "Comment coding, bounded text analysis, qualitative limits, subgroup comparison, uncertainty, equity, non-stigmatizing reporting.",
          "submission": "Equity and patient-voice memo.",
          "hours": 16
        },
        {
          "week": 6,
          "title": "Patient partnership and improvement design",
          "outcome": "Co-design a feasible improvement and its feedback measures.",
          "topics": "Patient partnership, co-design, driver diagrams, implementation, balancing measures, feedback loops, unintended effects.",
          "submission": "Draft improvement package.",
          "hours": 16
        },
        {
          "week": 7,
          "title": "Recommendation, communication, and accountability",
          "outcome": "Defend a patient-experience and engagement recommendation.",
          "topics": "Evidence synthesis, patient-facing reporting, leadership communication, evaluation measures, responsible claims, accountability.",
          "submission": "Final patient-experience and engagement package.",
          "hours": 16
        }
      ]
    },
    {
      "id": "APP-3",
      "stage": "Applied",
      "title": "Data for Clinical Performance and Improvement",
      "credits": 3,
      "format": "Seven-week online block",
      "prerequisites": "FND-1 and FND-2",
      "summary": "Turn harm, delay, unreliable care, access, or capacity problems into measured and tested improvements.",
      "finalDeliverable": "Final clinical performance improvement package.",
      "modules": [
        {
          "week": 1,
          "title": "Framing a clinical performance problem",
          "outcome": "Frame a clinical performance problem around quality, safety, access, flow, and an accountable improvement aim.",
          "topics": "Quality improvement, patient safety, unit of flow, demand and capacity, process and outcome measures, balancing measures, SMART aims.",
          "submission": "Clinical performance charter.",
          "hours": 15.5
        },
        {
          "week": 2,
          "title": "Measures and operational metrics",
          "outcome": "Specify, build, and validate the measures that define the problem.",
          "topics": "Numerators, denominators, exclusions, event detection, cycle time, wait time, utilization, throughput, capacity, measure validation.",
          "submission": "Measure and operational metric build.",
          "hours": 16
        },
        {
          "week": 3,
          "title": "Variation, safety signals, and bottlenecks",
          "outcome": "Diagnose variation, safety signals, delays, and bottlenecks.",
          "topics": "Process mapping, common and special cause, run and control charts, signal rules, incident data, bottleneck analysis, small numbers.",
          "submission": "Performance diagnostic.",
          "hours": 16.5
        },
        {
          "week": 4,
          "title": "Demand forecasting and capacity",
          "outcome": "Forecast demand and connect it to capacity and staffing.",
          "topics": "Forecast aim and horizon, benchmark forecast, seasonality, temporal validation, error metrics, Little's Law, cost of error.",
          "submission": "Forecasting and capacity checkpoint.",
          "hours": 16.5
        },
        {
          "week": 5,
          "title": "Improvement scenarios and evaluation",
          "outcome": "Test an improvement and the assumptions behind it.",
          "topics": "Queueing and capacity logic, guided scenario model, staffing and scheduling options, pre and post traps, trend, confounding, sensitivity.",
          "submission": "Improvement scenario and evaluation.",
          "hours": 16
        },
        {
          "week": 6,
          "title": "Feasibility, equity, and monitoring",
          "outcome": "Judge feasibility, equity, workforce effects, and unintended harm.",
          "topics": "Implementation, safety and quality interactions, access and equity, workforce burden, balancing measures, dashboards, escalation and fallback rules.",
          "submission": "Draft clinical performance package.",
          "hours": 16
        },
        {
          "week": 7,
          "title": "Recommendation and defense",
          "outcome": "Defend a clinical performance recommendation and monitoring plan.",
          "topics": "Evidence synthesis, measure stewardship, leadership and frontline communication, accountability, continuous learning, reproducible handoff.",
          "submission": "Final clinical performance improvement package.",
          "hours": 16
        }
      ]
    },
    {
      "id": "APP-4",
      "stage": "Applied",
      "title": "Data for Clinical Decision Support",
      "credits": 3,
      "format": "Seven-week online block",
      "prerequisites": "FND-1 and FND-2",
      "summary": "Take a prediction into a clinical workflow, test its burden and failure modes, and stop before it does harm.",
      "finalDeliverable": "Final CDS package.",
      "modules": [
        {
          "week": 1,
          "title": "Framing a decision support use case",
          "outcome": "Frame a decision support use case around a user, a workflow moment, an intended action, and a safety boundary.",
          "topics": "Clinical decision support, the five rights, sociotechnical workflow, human-in-the-loop design, intended use, safety constraints.",
          "submission": "CDS use-case charter.",
          "hours": 15.5
        },
        {
          "week": 2,
          "title": "Decision support logic, triggers, and data",
          "outcome": "Specify the logic, triggers, thresholds, and data inputs for a decision support concept.",
          "topics": "Rule and trigger logic, CDS Hooks and FHIR, terminology and value sets, data availability at the decision, threshold selection, alert modality.",
          "submission": "Logic and data-input specification.",
          "hours": 16
        },
        {
          "week": 3,
          "title": "Evidence, calibration, and validation",
          "outcome": "Judge whether the evidence is strong enough for the intended use.",
          "topics": "Threshold confusion measures, calibration, prospective and temporal validation, net benefit, subgroup performance, alert workload.",
          "submission": "CDS evidence and calibration audit.",
          "hours": 16.5
        },
        {
          "week": 4,
          "title": "Alert burden, human factors, and equity",
          "outcome": "Assess workflow fit and the risk of harm.",
          "topics": "Alert fatigue, alert burden, usability, automation bias, equity in deployment, privacy, workflow fit.",
          "submission": "Workflow and alert-burden review.",
          "hours": 16.5
        },
        {
          "week": 5,
          "title": "Sandbox prototype and failure modes",
          "outcome": "Build a sandbox prototype and disclose its limits.",
          "topics": "Nonproduction prototyping, traceable logic, test and edge cases, silent failure, failure modes, disclosure, implementation boundary.",
          "submission": "Sandbox prototype checkpoint.",
          "hours": 16
        },
        {
          "week": 6,
          "title": "Safety case, monitoring, and governance",
          "outcome": "Assemble a safety case with a monitoring and governance plan.",
          "topics": "Safety case, live monitoring signals, calibration drift, silent-failure surveillance, escalation and stop rules, governance, retirement.",
          "submission": "Draft CDS safety and monitoring plan.",
          "hours": 16
        },
        {
          "week": 7,
          "title": "Product brief and defense",
          "outcome": "Defend the product brief and the implementation and evaluation plan.",
          "topics": "Product brief, staged rollout, post-deployment evaluation, implementation risk, human oversight, stakeholder defense.",
          "submission": "Final CDS package.",
          "hours": 16
        }
      ]
    },
    {
      "id": "APP-5",
      "stage": "Applied",
      "title": "Data for Population Health and Equity",
      "credits": 3,
      "format": "Seven-week online block",
      "prerequisites": "FND-1 and FND-2",
      "summary": "Measure how health differs across groups and places, then shape an accountable intervention.",
      "finalDeliverable": "Final population intervention analytics plan.",
      "modules": [
        {
          "week": 1,
          "title": "Framing a population-health decision",
          "outcome": "Frame a population-health decision with its denominator, geography, time frame, and accountable audience.",
          "topics": "Population and community health, denominator logic, geographic levels, surveillance framing, community accountability, equity and disparity definitions.",
          "submission": "Population decision charter.",
          "hours": 15.5
        },
        {
          "week": 2,
          "title": "Population measures from linked data",
          "outcome": "Build and validate population, subgroup, rate, and denominator measures from linked data.",
          "topics": "Data linkage, census and ACS variables, social-determinant indices, crude and specific rates, direct and indirect standardization, provenance.",
          "submission": "Population measure build.",
          "hours": 16
        },
        {
          "week": 3,
          "title": "Disparities and data limits",
          "outcome": "Measure disparities honestly while accounting for data and denominator limits.",
          "topics": "Disparity metrics, reference-group choice, small numbers, cell suppression, missing race and ethnicity data, selection and measurement bias, uncertainty.",
          "submission": "Disparity analysis checkpoint.",
          "hours": 16.5
        },
        {
          "week": 4,
          "title": "Place-based evidence and geographic reasoning",
          "outcome": "Read place-based evidence responsibly with maps and area-level data.",
          "topics": "Choropleth mapping, geographic aggregation, ecological fallacy, contextual and compositional effects, small-area rate stability, non-stigmatizing visualization.",
          "submission": "Responsible map and context memo.",
          "hours": 16.5
        },
        {
          "week": 5,
          "title": "Targeting and fairness",
          "outcome": "Evaluate the targeting and fairness of a proposed intervention.",
          "topics": "Resource allocation, targeting rules, need-based allocation, benefit and harm tradeoffs, fairness across groups, differential impact, monitoring.",
          "submission": "Targeting and fairness audit.",
          "hours": 16
        },
        {
          "week": 6,
          "title": "Designing an accountable intervention plan",
          "outcome": "Design an accountable population intervention analytics plan.",
          "topics": "Intervention analytics design, implementation measures, evaluation design, community communication, feedback loops, accountability.",
          "submission": "Draft population intervention plan.",
          "hours": 16
        },
        {
          "week": 7,
          "title": "Defending the population recommendation",
          "outcome": "Defend the population recommendation and its monitoring plan.",
          "topics": "Evidence synthesis, equity rationale, monitoring measures, community-facing communication, decision accountability, stated limits.",
          "submission": "Final population intervention analytics plan.",
          "hours": 16
        }
      ]
    },
    {
      "id": "APP-6",
      "stage": "Applied",
      "title": "Data for Health Research and Innovation",
      "credits": 3,
      "format": "Seven-week online block",
      "prerequisites": "FND-1 and FND-2",
      "summary": "Design a health study that can answer a causal question and produce evidence another researcher can review.",
      "finalDeliverable": "Final research and innovation package.",
      "modules": [
        {
          "week": 1,
          "title": "From a question to a causal estimand and study design",
          "outcome": "Frame a research or innovation question as a causal or evaluation estimand with a clear target.",
          "topics": "Research and evaluation questions, causal versus descriptive aims, causal estimand, target trial thinking, comparators, outcomes, evidence standards.",
          "submission": "Study and innovation design charter.",
          "hours": 15.5
        },
        {
          "week": 2,
          "title": "Data feasibility and measurement",
          "outcome": "Determine whether the available data can support the proposed study.",
          "topics": "Feasibility counts, event rates, precision, variable definitions, measurement validity, missingness, data provenance, go or no-go.",
          "submission": "Feasibility table and data-risk memo.",
          "hours": 16
        },
        {
          "week": 3,
          "title": "Causal diagrams, confounding, and identification",
          "outcome": "Draw a causal diagram, state the identification assumptions, and choose an adjustment set.",
          "topics": "DAGs, confounders, colliders, mediators, backdoor criterion, adjustment sets, exchangeability, positivity, consistency, selection bias.",
          "submission": "Validity and design memo.",
          "hours": 16.5
        },
        {
          "week": 4,
          "title": "Estimation, adjustment, and sensitivity analysis",
          "outcome": "Estimate a causal or quasi-experimental effect and test how fragile it is.",
          "topics": "Propensity scores, matching, weighting, balance and overlap, quasi-experimental designs, sensitivity analysis, missing data.",
          "submission": "Estimation analysis checkpoint.",
          "hours": 16.5
        },
        {
          "week": 5,
          "title": "Reproducible protocol analytics and preregistration",
          "outcome": "Preregister a protocol and analysis plan and produce a reproducible analytic record.",
          "topics": "Study protocol, statistical analysis plan, preregistration, prespecified versus exploratory analyses, versioned evidence, code review.",
          "submission": "Preregistered protocol and reproducible record.",
          "hours": 16
        },
        {
          "week": 6,
          "title": "Innovation evidence, prototype evaluation, and the dissemination artifact",
          "outcome": "Evaluate an innovation claim and build the prototype or evidence brief that goes with it.",
          "topics": "Digital health evidence, prototype evaluation, benefit and risk, safety, equity, implementation fit, overclaiming.",
          "submission": "Innovation evidence critique and prototype or brief.",
          "hours": 16
        },
        {
          "week": 7,
          "title": "Reporting standards, methodological defense, and next-study logic",
          "outcome": "Meet reporting standards, defend your methodology, and state the next study.",
          "topics": "Observational reporting standards, honest limitations, dissemination artifact, methodological defense, peer review, next-study logic.",
          "submission": "Final research and innovation package.",
          "hours": 16
        }
      ]
    },
    {
      "id": "APP-7",
      "stage": "Applied",
      "title": "Data for Health Systems Strategy, Finance, and Value",
      "credits": 3,
      "format": "Seven-week online block",
      "prerequisites": "FND-1 and FND-2",
      "summary": "Turn service, cost, finance, and value data into a strategic investment recommendation leadership can weigh.",
      "finalDeliverable": "Final strategic investment decision package.",
      "modules": [
        {
          "week": 1,
          "title": "Framing the strategic decision",
          "outcome": "Frame a strategic decision with clear alternatives, constraints, and criteria.",
          "topics": "Mission, value, stakeholders, opportunity cost, strategic fit, decision criteria, risk framing.",
          "submission": "Strategic decision charter.",
          "hours": 15.5
        },
        {
          "week": 2,
          "title": "Reading finance and value data",
          "outcome": "Read finance and value data without category errors.",
          "topics": "Payer mix, reimbursement, cost structure, revenue, contribution margin, value frameworks, volume versus value.",
          "submission": "Finance and value interpretation lab.",
          "hours": 16
        },
        {
          "week": 3,
          "title": "Service-line and access diagnosis",
          "outcome": "Diagnose service-line performance and its access and capacity context.",
          "topics": "Utilization, referrals, leakage, access, capacity, case mix, benchmarks, need versus demand.",
          "submission": "Service-line diagnostic.",
          "hours": 16.5
        },
        {
          "week": 4,
          "title": "Strategic context",
          "outcome": "Read the internal and external context that constrains the decision.",
          "topics": "Market context, partnerships, payment and policy uncertainty, mission, equity, community benefit.",
          "submission": "Strategic context memo.",
          "hours": 16.5
        },
        {
          "week": 5,
          "title": "Financial and value modeling",
          "outcome": "Build and test a transparent financial and value model.",
          "topics": "Baseline, forecast, return on investment, payback, budget impact, cost-effectiveness, sensitivity and scenario analysis.",
          "submission": "Scenario and budget-impact model.",
          "hours": 16
        },
        {
          "week": 6,
          "title": "Comparing and prioritizing options",
          "outcome": "Compare options across financial and nonfinancial value.",
          "topics": "Multi-criteria prioritization, workforce, feasibility, equity, governance, stop rules.",
          "submission": "Draft executive decision package.",
          "hours": 16
        },
        {
          "week": 7,
          "title": "The executive decision package",
          "outcome": "Defend a board-ready recommendation and monitoring plan.",
          "topics": "Executive visualization, assumptions, risk triggers, implementation measures, contingency planning.",
          "submission": "Final strategic investment decision package.",
          "hours": 16
        }
      ]
    },
    {
      "id": "CAP-0",
      "stage": "Capstone",
      "title": "Capstone Preparation",
      "credits": 0,
      "format": "Seven-week preparation block",
      "prerequisites": "FND-1, FND-2, and at least five applied courses",
      "summary": "Prove the capstone problem, data, methods, ethics, and delivery plan are feasible before the project begins.",
      "finalDeliverable": "Approved capstone proposal.",
      "modules": [
        {
          "week": 1,
          "title": "Framing the problem",
          "outcome": "Frame the problem around the decision it serves.",
          "topics": "Decision-first framing, learning-health-system fit, scope control.",
          "submission": "Problem statement draft.",
          "hours": 3
        },
        {
          "week": 2,
          "title": "Stakeholders and aim",
          "outcome": "Map stakeholders and set a measurable aim.",
          "topics": "Stakeholder mapping, aim statements, success and balancing measures.",
          "submission": "Stakeholder map and aim statement.",
          "hours": 3
        },
        {
          "week": 3,
          "title": "Data feasibility",
          "outcome": "Confirm the data exist, are reachable, and are permitted.",
          "topics": "Data source inventory, access and permitted use, feasibility profiling.",
          "submission": "Data-access confirmation.",
          "hours": 4
        },
        {
          "week": 4,
          "title": "Methods plan",
          "outcome": "Choose methods and state their assumptions and risks.",
          "topics": "Analytic aim classification, method selection, validity threats.",
          "submission": "Methods plan.",
          "hours": 4
        },
        {
          "week": 5,
          "title": "Ethics and privacy",
          "outcome": "Clear the ethics, privacy, and IRB requirements.",
          "topics": "Ethics determination, IRB or data-use materials, identifiability and small-cell risk.",
          "submission": "Ethics and privacy determination.",
          "hours": 4
        },
        {
          "week": 6,
          "title": "Reproducible skeleton and timeline",
          "outcome": "Build the reproducible skeleton and the timeline.",
          "topics": "Project skeleton, capstone timeline, risk and contingency.",
          "submission": "Project skeleton and timeline.",
          "hours": 3
        },
        {
          "week": 7,
          "title": "Proposal defense",
          "outcome": "Present and defend an approved proposal.",
          "topics": "Proposal synthesis, defense and critique, revision to approval.",
          "submission": "Approved capstone proposal.",
          "hours": 3
        }
      ]
    },
    {
      "id": "CAP-1",
      "stage": "Capstone",
      "title": "Capstone: Learning Health System Analytics",
      "credits": 3,
      "format": "Seven-week online block",
      "prerequisites": "FND-1, FND-2, six applied courses, and CAP-0",
      "summary": "Run one complete healthcare analytics project from an authentic decision through a defended recommendation.",
      "finalDeliverable": "Final package, oral defense, and reflection.",
      "modules": [
        {
          "week": 1,
          "title": "Scoping and stakeholder framing",
          "outcome": "Confirm a decision-centered project scope and manage its risks before any analysis begins.",
          "topics": "Learning health system cycle, decision charter, stakeholder requirements, milestone and change control, contingency scope, project AI-use plan.",
          "submission": "Approved project charter and analysis plan.",
          "hours": 15.5
        },
        {
          "week": 2,
          "title": "Data acquisition and cohort build",
          "outcome": "Establish governed, reproducible data access and a working thin-slice pipeline.",
          "topics": "Data provenance, governance route, cohort and unit definition, data dictionary, quality checks, privacy and small cells, reproducible pipeline.",
          "submission": "Data and reproducibility checkpoint.",
          "hours": 16
        },
        {
          "week": 3,
          "title": "Methods selection and analysis",
          "outcome": "Produce a first defensible analysis and respond to technical review.",
          "topics": "Analytic aim, method selection and justification, baseline and comparator, assumption checks, error analysis, claim and evidence fit.",
          "submission": "Analytic result and review response.",
          "hours": 16.5
        },
        {
          "week": 4,
          "title": "Evaluation and validity",
          "outcome": "Test whether the conclusion could be wrong or harmful.",
          "topics": "Validation design, sensitivity analysis, confounding and leakage, subgroup performance, equity, ethics, safety, stated limits.",
          "submission": "Validity, equity, and risk review.",
          "hours": 16.5
        },
        {
          "week": 5,
          "title": "Implementation and evaluation planning",
          "outcome": "Translate the evidence into a recommendation, an implementation pathway, and an evaluation plan.",
          "topics": "Implementation planning, workflow effects, resources and feasibility, stakeholder recommendation, measurement and evaluation design.",
          "submission": "Draft report, visual product, and implementation and evaluation plan.",
          "hours": 16
        },
        {
          "week": 6,
          "title": "Communication and review readiness",
          "outcome": "Prepare the work for independent review and stakeholder delivery.",
          "topics": "Reproducibility audit, accessibility, technical and audience editing, limitations, handoff readiness.",
          "submission": "Release candidate and review disposition log.",
          "hours": 16
        },
        {
          "week": 7,
          "title": "Oral defense and next-cycle learning",
          "outcome": "Defend the final recommendation and identify what the system should learn next.",
          "topics": "Oral defense, response to critique, reflective practice, monitoring and maintenance, next-cycle learning.",
          "submission": "Final package, oral defense, and reflection.",
          "hours": 16
        }
      ]
    }
  ]
};

  const courseIds = curriculum.courses.map(course => course.id);
  const moduleTotal = curriculum.courses.reduce((total, course) => total + course.modules.length, 0);
  const valid = curriculum.courseCount === 11
    && curriculum.moduleCount === 77
    && new Set(courseIds).size === 11
    && moduleTotal === 77
    && curriculum.courses.every(course => course.modules.length === 7);

  if (!valid) {
    throw new Error("The curriculum data failed its integrity check.");
  }

  window.Curriculum = curriculum;
})();
