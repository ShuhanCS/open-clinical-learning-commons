# Override and stop conditions

- Human override: the clinician may ignore, close, dismiss, defer, or report the passive panel without an automatic consequence.
- Patient recourse: a patient may decline discussion, request language or disability access, ask how the concept works, or report harm.
- Pause owners: receiving clinician, workflow lead, patient-safety lead, clinical informatics lead, data steward, language-access reviewer, disability-access reviewer, and governance council.
- Restart owner: the governance council after the named defect owner supplies evidence and every affected reviewer accepts the change.
- Default fallback: no panel and no automated action.

| Stop ID | Trigger | Immediate action | Evidence required before restart | Owner |
|---|---|---|---|---|
| S01 | real or restricted data enter the package | stop and isolate the package | documented removal, privacy review, and clean rebuild | privacy and data stewards |
| S02 | panel text implies diagnosis, ordering, treatment, or accepted threshold status | stop the sandbox build | corrected content and clinical review | clinical content reviewer |
| S03 | missing, stale, or inconsistent input is treated as negative | stop evaluation | reason-code and unavailable-state tests | data steward |
| S04 | `0.20` enters evidence or `0.03` is called clinically accepted | stop progression | restored threshold contract and governance review | methods and governance owners |
| S05 | suppressed access or equity rate is filled, merged, ranked, or targeted | stop analysis | restored suppression and equity review | equity reviewer |
| S06 | dismissal, deferment, or response time is called observed behavior, fatigue, misuse, or care quality | stop interpretation | corrected language and patient-safety review | patient-safety lead |
| S07 | automated order, suggestion, escalation, penalty, or compliance pressure appears | stop the sandbox build | removal and automation-bias retest | clinical informatics lead |
| S08 | live connection, real-patient scoring, silent-mode evaluation, implementation, or deployment is proposed | stop the course route | governance referral outside course authority | governance council |

Passing Module 04 does not satisfy any restart condition for clinical use. It permits only bounded Module 05 sandbox construction.
