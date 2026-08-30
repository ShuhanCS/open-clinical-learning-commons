# Transformation record

| Step | Input | Transformation | Output | Conservation or check |
|---|---|---|---|---|
| T01 | accepted 16-table SQLite database | verify 141234176 bytes and accepted SHA-256 | read-only source connection | source identity passes |
| T02 | patients and encounters | select first qualifying adult emergency or inpatient encounter | 518-row index cohort | one row per person and 451/67 class split |
| T03 | patient death date and index stop | classify date-granular index and early death | 9 index deaths and 8 early deaths | branches retained |
| T04 | post-discharge acute encounters | select first acute return through day 30 and retain all audit events | 25 early-return people and 27 event rows | first-event and audit counts reconcile |
| T05 | scheduled encounters | select first scheduled encounter through day 30 and retain all audit events | 129 exposed eligible people and 212 audit rows | exposure assigned at landmark only |
| T06 | index and early branches | apply day-30 landmark | 476 eligible people | 9 + 8 + 25 + 476 = 518 |
| T07 | later acute encounters and death | select first event and apply censoring order through day 365 | 87 events and 389 administrative censors | 87 + 0 + 389 = 476 |
| T08 | baseline source fields | calculate fixed risk score and ranked thirds | low medium and high risk tiers | score uses only index-available fields |
| T09 | fixed extension contract | assign SITE-A through SITE-F with SHA-256 draw | 476 site assignments | one site per person and all tiers at all sites |
| T10 | longitudinal plus extension | merge by synthetic patient ID | 476-row analysis cohort | source exposure and outcome unchanged |
| T11 | all outputs | write LF-terminated CSV and sorted JSON metadata | ten output files | rows bytes and SHA-256 frozen |

No source date, exposure, outcome, event indicator, or observed time is changed by the site extension.
