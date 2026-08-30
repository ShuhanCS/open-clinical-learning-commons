# Instructor notes

## Purpose

Week 4 revisits database joins, analytic tables, weighted estimates, and uncertainty through a patient-experience problem. The technical work is applied to linkage meaning: one person can have many events, related emergency and inpatient rows are not unrelated encounters, and each patient-reported field has its own valid denominator.

## 16.5-hour plan

| Activity | Hours |
|---|---:|
| Source, checkpoint, and decision briefing | 1.0 |
| Person and event grain lesson | 2.0 |
| Fixed-width source and key lab | 2.0 |
| Governed linkage and reconciliation lab | 2.5 |
| Denominator and survey-domain lesson | 2.0 |
| Access and communication estimation lab | 2.0 |
| Service-use and digital-channel lab | 2.0 |
| Interpretation, reproduction, and claim review | 1.5 |
| Submission defense and feedback | 1.5 |
| Total | 16.5 |

## Teaching sequence

Start with the 1,255-person Week 3 target, not with a join command. Ask learners to predict how four event files change the row count and why summing person weights after a one-to-many join cannot estimate unique people.

Use the 855 linked emergency-inpatient pairs to show why technical equality of keys does not settle analytic meaning. Then show the 12 inpatient stays that begin in 2023. Learners must defend the documented annual-file rule before calculating rates.

The provider-language measure has only 45 valid target records. It remains in the output with `limited_support`; it is not silently dropped or promoted to a confident equity conclusion.

Telehealth is the digital-service example. The accepted source has no portal-preference field. Any learner who calls telehealth use patient preference or engagement must revise the claim.

## Feedback points

Give feedback after the linkage audit and before learners draft their interpretation. A correct table with a wrong denominator does not pass. Ask learners to state the grain, eligible population, weight, uncertainty method, data class, and claim limit for one result selected at random.

Module 5 may begin only after every linkage gate passes. Machine learning remains prohibited until Module 6.
