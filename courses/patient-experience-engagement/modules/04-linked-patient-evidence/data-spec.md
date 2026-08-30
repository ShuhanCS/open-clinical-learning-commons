# Data specification

## Official source layer

The module retains 25 official AHRQ files: the ASCII data archive, documentation PDF, codebook PDF, SAS statements, and R statements for HC-256 and HC-254D through HC-254G. The source inventory pins every URL, byte count, SHA-256 digest, page count, and role. The files total 18,206,634 bytes and the ten PDFs total 1,101 pages.

HC-256 has one row per public-use person. HC-254D, HC-254E, HC-254F, and HC-254G contain inpatient, emergency, outpatient, and office-based events. The build parses the fixed-width files from the official R layouts and links them with `DUPERSID`.

## Accepted upstream layer

The three upstream files freeze the Week 3 release identity, the 1,255-person adult inpatient frame, and its 1,255-row synthetic response study. Their combined size is 570,340 bytes. The build checks the checkpoint candidate manifest hash before using them.

Invitation, response, mode, Q21, Q22, Q23, and item missingness remain synthetic procedural fields. They are never relabeled as real patient responses.

## Released teaching layer

`data/public/linked-persons.csv` has one row for each accepted target person. It preserves grouped public characteristics, person weights, design variables, person-reported service totals, linked event totals, access and communication fields, and the accepted synthetic response handoff.

`data/public/linked-events.csv` has 28,455 rows. It contains 1,692 inpatient stays, 1,601 emergency visits, 4,651 outpatient visits, and 20,511 office-based visits. Sequential teaching IDs replace direct public-use person and event identifiers. Related emergency and inpatient events point to one another with released teaching event IDs.

Twelve inpatient stays begin in 2023 and continue into the 2024 file. Learners retain them under the documented annual-file rule.

## Denominator and weighting rules

Person estimates use `PERWT24F`, `VARSTR`, and `VARPSU`. Each measure has its own valid-response denominator. Survey-domain variance retains every sampled PSU with a zero contribution outside the analytic domain.

Event distributions may use the person weight repeated across events, but they remain event-grain descriptions. A person denominator cannot be replaced by an event denominator, and event weights cannot be summed to claim a count of unique people.

## Evidence gaps

The source contains telehealth event flags for outpatient and office-based visits. It does not measure portal access, portal preference, or whether a patient preferred a digital channel. Telehealth use is therefore a service channel, not proof of engagement or preference.
