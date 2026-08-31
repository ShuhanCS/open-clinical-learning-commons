# CDS use-case charter

- Service ID: `CGH-GIM-01`.
- Service status: explicitly fictional adult general internal medicine and primary care service.
- Decision owner: `CGH-GIM-01 clinical decision support governance council`.
- Module decision: `Are the intended use, user, workflow moment, action boundary, source evidence roles, synthetic-data plan, and accountable owners defined well enough to begin logic and input specification?`
- Primary user: `clinician responsible for the current adult encounter`.
- Workflow moment: `after required encounter information is available and before the encounter closes`.
- Intended support: `a nonbinding advisory asking the clinician to consider whether confirmatory HbA1c testing is appropriate`.
- Intended action: `human review of the patient's current record and clinical context; the clinician may consider testing, defer, dismiss, or take no action`.
- Nonaction: `the card may not appear, may be dismissed, or may lead to no order without being treated automatically as an error`.
- Prohibited action: `diagnosis, automatic order, blocked workflow, treatment change, denial, nonclinical targeting, or any action without clinician review`.
- Patient consequence to examine later: `unnecessary testing, missed testing opportunity, confusion, access burden, privacy concern, or inequitable exclusion`.
- Clinician consequence to examine later: `interruption, repeated work, cognitive load, loss of trust, or hidden follow-up work`.
- Public evidence role: `historical survey source feasibility and later model evaluation only`.
- Synthetic evidence role: `future event-time input availability, trigger, interaction, burden, latency, drift, and silent-failure truth`.
- Allowed next step: `construct and test the nonproduction logic and input contract in Module 02`.
- Course points: `0`.

The exact clinical target, eligibility, exclusions, predictor list, units, terminology, threshold candidates, and card wording remain open for named human review. No model or threshold is accepted in Module 01.

The charter does not authorize real-patient scoring, clinical use, implementation, or deployment.
