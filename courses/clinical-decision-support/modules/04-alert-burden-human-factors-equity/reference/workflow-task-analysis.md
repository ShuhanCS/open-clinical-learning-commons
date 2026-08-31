# Workflow task analysis

- Decision: whether one candidate design may enter a nonproduction Module 05 sandbox.
- Primary user: a fictional `CGH-GIM-01` primary-care clinician.
- Workflow moment: after required encounter inputs are available and before the fictional encounter closes.
- Expected action: review a passive informational panel and decide whether any follow-up discussion belongs in the encounter.
- Nonaction: close, dismiss, defer, or ignore the panel without an automatic order, diagnosis, treatment change, penalty, or escalation.
- Alternative: continue existing work without decision support.
- Patient consequence: the concept may prompt a clinician-patient discussion, add hidden work, create confusion, or exclude people whose inputs or access needs are unsupported.
- Hidden work: input review, uncertainty review, patient explanation, language and accessibility support, documentation, repeat handling, defect reporting, and unresolved follow-up.
- Human owner: the fictional clinical decision support governance council.
- Stop authority: the receiving clinician, workflow lead, patient-safety lead, clinical informatics lead, and governance council may pause the sandbox concept.
- Evidence boundary: public NHANES evidence and scripted synthetic workflow evidence do not establish local utility, burden, behavior, safety, or patient benefit.

| Step | Actor | Task | Information available | Candidate design | Failure or burden question | Required control |
|---:|---|---|---|---|---|---|
| 1 | clinician | begin a scheduled session | fictional schedule and competing-work script | no card | does preparation add another queue? | no extra session-start task in the reference design |
| 2 | clinician | open the patient-view context | patient and encounter identifiers | passive panel may be eligible | can the panel appear before inputs are ready? | evaluate only after the input-readiness check |
| 3 | CDS logic owner | evaluate candidate frame and input state | age, BMI, diabetes state, prior HbA1c, and offline synthetic score | no card when unavailable | can missing, stale, or inconsistent data look negative? | preserve unavailable states and show no clinical conclusion |
| 4 | clinician | notice or ignore the passive panel | bounded informational text | `panel-t003` sandbox fixture | does a passive panel still compete for attention? | count every card and session concentration |
| 5 | clinician | acknowledge, dismiss, defer, view, or leave unresolved | scripted interaction state | no automated consequence | is an interaction being mistaken for motive or quality? | label all interactions scripted and avoid motive claims |
| 6 | clinician and patient | decide whether discussion is appropriate | uncertainty, limits, and access needs | clinician-owned conversation only | can language, disability, or privacy needs be missed? | require qualified language and accessible-format routes |
| 7 | clinician | close the fictional encounter | no automated order or escalation | panel ends with the encounter | does hidden work carry beyond the encounter? | document unresolved work and permit pause or redesign |

The task analysis supports sandbox construction only. It does not approve the panel, threshold, workflow, or clinical action.
