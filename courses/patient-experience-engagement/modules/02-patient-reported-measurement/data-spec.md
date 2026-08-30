# Module 02 data specification

## Source suite

`data/source-inventory.csv` is the trust anchor for 28 immutable public files: 22 current instrument PDFs, five guidance PDFs, and the full deterministic CMS HCAHPS gzip. Every byte count and SHA-256 fingerprint is checked before an output is built.

The CMS file has 325,720 hospital-measure rows, 4,790 facilities, 68 measure IDs, and no patient-level responses. Its reporting period is 2024-10-01 through 2025-09-30 and crosses the January 2025 instrument transition without a patient-level version marker.

## Synthetic fixture

`data/synthetic/patient-measurement-responses.csv` has 240 visibly synthetic records. It contains no names, facilities, dates, demographics, outcomes, or patient text.

- 200 records are eligible for Q22/Q23.
- 20 report discharge to another health facility, making Q22/Q23 not applicable.
- 20 have missing Q21, so Q22/Q23 remain missing.
- Q22 has 176 answered records: 148 yes and 28 no.
- Q23 has 184 answered records: 144 yes and 40 no.

## Scoring

Question-level top-box percentages use question-specific answered denominators. The unadjusted teaching composite is the mean of the Q22 and Q23 top-box proportions. The person-weighted teaching mean first averages available Q22/Q23 responses within a synthetic person and then averages those person means. The calculations answer different questions.

The public concordance output compares the simple mean of rounded published item percentages with the official adjusted CMS composite. It measures reproduction mismatch only and must not be used to rank facilities.

## Missing states

`missing`, `not_applicable`, and `no` are distinct. Only `yes` and `no` enter the Q22/Q23 item denominators. Another-facility discharge is never recoded as no.
