# Care-pathway decision charter

- Decision owner: `hospital medicine care-improvement council`
- Decision: `Should the council design and prospectively evaluate a pathway that increases scheduled follow-up within 30 days after an adult's first qualifying acute-care discharge?`
- Proposed next action: `build and validate the longitudinal cohort before deciding whether to design a bounded prospective improvement test`
- Target population: `synthetic adults at their first qualifying emergency or inpatient encounter from 2010-01-01 through 2019-03-31`
- Pathway entry: `first qualifying emergency or inpatient encounter at age 18 or older`
- Discharge origin: `qualifying index encounter stop`
- Exposure: `at least one ambulatory, outpatient, or wellness encounter after discharge and through day 30`
- Comparator: `no scheduled encounter in the exposure window`
- Exposure window: `open after discharge and closed at day 30`
- Landmark: `day 30 after discharge among people with no index death, early post-discharge death, or early acute return`
- Landmark exclusions: `recorded death date on or before index discharge, death after discharge through day 30, or emergency/inpatient return after discharge through day 30`
- Primary outcome: `time from day-30 landmark to first emergency or inpatient return`
- Outcome window: `open after day 30 and closed at day 365 after discharge`
- Analysis aim: `describe and compare time-to-event evidence to judge feasibility for a prospective improvement test`
- Evidence standard: `validated cohort, defensible landmark, sufficient support, transparent adjustment, uncertainty, patient and access review, and no unsupported causal claim`
- Feasibility conclusion: `longitudinal and survival teaching case is feasible with conditions`
- Raw site comparison: `not ready because 476 landmark-eligible people span 64 sparse source organizations`
- Patient-important evidence gap: `the source does not directly capture follow-up burden, experience, trust, or whether the appointment met patient needs`
- Claim boundary: `synthetic observational evidence supports method instruction and prospective-test design only, not efficacy, causation, or real performance; it does not authorize implementation`
- Stop or referral trigger: `changed source identity, wrong time zero, early-event deletion, restricted data, inadequate support, inaccessible evidence, or proposed clinical action`

## Why this decision matters

Scheduled follow-up after acute care is a measurable process that could connect discharge to ongoing care. A care team needs more than a crude return rate: it needs a clear population, visible early events, a patient-relevant outcome set, a feasible workflow, access and burden review, and evidence that can support a prospective test without claiming effectiveness from synthetic retrospective data.

## What Module 02 must build

Module 02 must reproduce the complete source, validate the phenotype and first qualifying index, retain early death and acute return, create the day-30 landmark cohort, define follow-up and time-to-event fields, publish the cohort flow and event audit, and build a documented deterministic six-site teaching extension. Every field must be marked source, derived, or extension.
