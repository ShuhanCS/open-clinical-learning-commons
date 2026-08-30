# FND-2 modeling, inference, and reproducible analytics source record

- Source course ID: FND-2
- Source title: Modeling, Inference, and Reproducible Analytics
- Source filename: `04-FND-2-Modeling-Inference-Reproducible-Analytics.docx`
- Source bytes: 21,850
- Source SHA-256: `eef6fbb36cb27917f8b48b61e705895a5cb5eaad64bd0f0d38bf153525528c03`
- Verified: 2026-08-30
- Commons course specification: `docs/curriculum/courses/FND-2/course-spec.md`

## Package comparison

The source document was verified in both supplied curriculum packages:

- `Curriculum-30-Credits-2026-08-29.zip`; and
- `OneDrive_2026-08-29 (1).zip`.

The FND-2 DOCX files are byte-for-byte identical and have the same SHA-256 fingerprint above.

## Source course identity

- Credits: 3.
- Source format: seven-week online block.
- Prerequisite: FND-1.
- Total learner work: 112.5 hours.
- Primary graded language: Python with pandas and notebooks.
- Database language: SQL, reused from FND-1 to produce model-ready tables.
- R role: read, run, and interpret R Markdown or Quarto; writing R from scratch is not graded.
- Supporting practices: Git, semantic versioning, environment files, model cards, prompt and trace logs, tests, monitoring, and human sign-off.

## Source course purpose

FND-2 starts from a clean, checked FND-1 dataset and asks what analytic evidence a decision needs. Learners classify the aim, identify the target quantity, choose a method family, check assumptions, evaluate validity and performance, state what the result can support, and govern the released analysis.

FND-1 and FND-2 are separate straight-through technical foundations. FND-1 owns the data pipeline, cohort, quality, descriptive evidence, and technical handoff. FND-2 owns the analytic aim, estimand, model, assumptions, evaluation, validity, monitoring, and model decision. Applied courses extend these skills through distinct clinical and health-system decisions.

## Source module sequence

| Week | Source module | Hours | Source submission |
|---:|---|---:|---|
| 1 | Analytic aims and a reproducible modeling workspace | 15.5 | Aim-and-method plan, reproducible modeling repository, baseline model. |
| 2 | Regression models and interpretation | 16.0 | Regression interpretation and assumption lab. |
| 3 | Prediction workflows and evaluation | 16.5 | Prediction evaluation report. |
| 4 | Adjustment, missing data, and longitudinal structure | 16.5 | Validity, adjustment, and longitudinal-method memo. |
| 5 | Forecasting and temporal validation | 16.0 | Forecasting and temporal validation checkpoint. |
| 6 | Agent-assisted modeling and testing | 16.0 | Agent-assisted model review log and test suite. |
| 7 | Model cards, governance, and defense | 16.0 | Final model or agent-assisted analytics package with a model card. |
| Total |  | 112.5 |  |

## Source mastery levels

The source uses three explicit depth levels:

- Core: the learner performs the work independently.
- Guided: the learner performs the work with a bounded template.
- Recognize: the learner identifies the question, reads an example, and knows when a later applied course or specialist must take it further.

Core work includes analytic-aim classification, target quantities, method-family selection, leakage control, reproducible environments, assumption checks, uncertainty communication, threshold reasoning, subgroup performance, validity threats, missingness diagnosis, forecast aims, agent task boundaries, prompt logs, model cards, monitoring, and stop rules.

Guided work includes SQL-to-model preparation, regression fitting, nonlinear and interaction terms, prediction resampling, discrimination and calibration, class-imbalance evaluation, propensity examples, missing-data sensitivity, repeated-measures templates, forecast backtesting, decomposition, smoothing, error metrics, tests, and agent-assisted critique.

Recognition work includes advanced regularization and machine learning, mixed models, survival modeling, stationarity, ARIMA-family fitting, and deeper causal identification.

## Source learning objectives

The source defines six course objectives:

1. classify a healthcare analytic aim as descriptive, associational, predictive, causal, longitudinal, or forecasting and define the target quantity or success criterion;
2. establish a reproducible Python modeling workflow with documented splits, feature preparation, package environments, a baseline model, and reviewable output;
3. fit, interpret, and compare linear and logistic regression models, check assumptions, and evaluate risk prediction for discrimination, calibration, and threshold behavior;
4. diagnose confounding, selection, leakage, missing data, repeated measures, and small-sample threats and choose a remedy or stated caveat;
5. build an introductory forecasting workflow with a temporal split, benchmark, error metrics, and a clear boundary for specialist ARIMA-family work; and
6. produce a model or agent-assisted analytics package with tests, a model card, a prompt and trace log, human review, and a monitoring plan.

## Source assessment weights

| Source assessment | Source timing | Weight |
|---|---|---:|
| Reproducible modeling setup and aim classification | End of Week 1 | 15% |
| Regression and prediction labs | End of Week 3 | 25% |
| Validity, longitudinal, and forecasting memo | End of Week 5 | 25% |
| Model or agent-assisted analytics package with model card | End of Week 7 | 35% |
| Total |  | 100% |

## Commons checkpoint normalization

The Commons preserves the source weights and straight-through sequence while making the requested three cumulative checkpoints explicit:

- Week 3 checkpoint: the Week 1 setup component remains 15% and the Week 3 regression and prediction component remains 25%, submitted together as a cumulative 40% modeling-readiness release.
- Week 6 checkpoint: the source Week 5 validity, longitudinal, and forecasting component remains 25% and now includes the required Week 6 test, agent-review, trace, and human-sign-off evidence.
- Final checkpoint: the source final analytics package remains 35% and is due on the official last day of the assigned half-term.

Week 1 and Week 5 remain required feedback milestones. Week 6 is an integration and accountability checkpoint, not added course weight.

## Approved wording normalization

The Commons keeps the source scope but narrows several phrases so the teaching claim matches the design:

- A linear or logistic coefficient is called an association unless a defensible causal design supports stronger language.
- Odds, risks, predicted probabilities, and risk differences remain distinct quantities.
- A confidence interval is interpreted under the stated model and design assumptions, not as a general validity certificate.
- A synthetic case is an authentic decision scenario, not evidence about a real patient population.
- A fitted model can be accepted as a technically reproducible teaching artifact while its use recommendation is `do not deploy`.
- A small synthetic test set and sparse subgroup outcomes are treated as validity evidence, not hidden through pooled or optimistic reporting.
- Model monitoring in the public course is a governed plan and simulation. It does not claim that a clinical model has entered production.

## Source materials that must be developed

The source explicitly says these materials do not yet exist:

- a modeling-ready analytic dataset derived from the FND-1 database;
- a time-indexed operational series for forecasting;
- intentionally flawed leakage, overfitting, and confounding examples;
- SQL extraction scripts and environment files;
- feature-preparation templates;
- Python and R worked examples for regression, prediction, propensity adjustment, repeated measures, missing data, and forecasting;
- a model-card template;
- an agent prompt and trace log;
- a testing checklist;
- an evaluation-metric explainer; and
- instructor answer keys and rubrics for validity, forecasting, agent use, communication, and reproducibility.

These are build requirements, not claims that the DOCX includes runnable data or code.

## Source AI and agent policy

The source permits AI and agent tools for explaining and reviewing code, suggesting tests, critiquing a model, drafting documentation, and diagnosing errors. Every graded assignment discloses assistance. Material prompts, outputs, and verification enter a trace log. The learner checks, corrects, and signs off on every result.

The source prohibits unverified output, bypassing the learning, giving an agent final analytic decision authority, and placing protected or identifiable data in an external service. The learner remains accountable regardless of assistance.

## Stable source decisions

- FND-2 stays a separate straight-through technical foundations course.
- The course starts from an accepted FND-1 technical data foundation.
- SQL supports model-ready extraction; Python is the graded modeling language.
- R is read-run-interpret rather than a from-scratch programming requirement.
- Regression, prediction, validity, forecasting, testing, model cards, governance, and defense all remain in the seven-module course.
- Advanced machine learning, mixed models, survival, causal inference, and ARIMA-family fitting remain guided or recognition work until an applied course goes deeper.
- The final deliverable is a reproducible analytics package with a model card, tests, trace log, monitoring plan, and defense.
- No protected or identifiable patient data enter the public Commons or an external AI tool.

## Interpretation rule

The source document defines the curriculum, mastery levels, workload, and assessment weights. The Commons course specification adds exact synthetic and public sources, release identities, split rules, prediction-time boundaries, checkpoint folders, validation gates, accessibility requirements, reviewer roles, model-use decisions, and version controls needed to make the course runnable.
