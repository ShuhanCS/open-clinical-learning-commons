# Measurement and representation readiness review

## Decision chain

The accepted decision is to continue developing an accessible local process for adult inpatient reports about information that supports recovery at home. The selected measure is the updated HCAHPS Discharge Information Q22 and Q23 pair under the QAG V19.0 instrument effective January 1, 2025, with the April 2026 addendum checked.

Q21 another health facility makes Q22 and Q23 not applicable. Q22 and Q23 each use their own answered yes-plus-no denominator. The local teaching composite is the mean of the two question-level yes proportions. It remains public-domain HCAHPS-derived, local, unadjusted unless explicitly labeled, and unofficial. It is not an official adjusted HCAHPS score and has no established local meaningful-change threshold.

## Measurement readiness

Module 02 scores 20.00 of 20.00 with all 18 measurement gates passing. The package covers construct and content fit, score reproduction, reliability distinctions, meaningful-interpretation limits, language and mode routes, proxy and disability access, literacy, non-digital access, burden, stop rules, rights, naming, source provenance, and accountable agent use.

Any changed item, wording, order, response choice, skip rule, score, translation, construct, naming decision, or intended use returns to Module 02.

## Response and representation readiness

The public MEPS HC-256 source has 19,140 rows, including 18,683 with a positive person weight. The analytic target is 1,255 adults with positive `PERWT24F` and at least one reported 2024 inpatient discharge. Their base-weighted population is 18,879,474.284615. The teaching frame and invitation set each contain all 1,255 records, so coverage is 100 percent only by construction.

The deterministic synthetic response layer produces 782 respondents, or 62.31075697 percent unweighted and 62.69744128 percent under `PERWT24F`. Among respondents, 642 have synthetic Q21 home eligibility. Q22 has 585 answered and 57 missing records. Q23 has 589 answered and 53 missing records. Total nonresponse, Q21 not-applicable states, and item missingness remain separate.

The subgroup audit retains small support, including a one-record missing-language cell. The adjustment uses 13 observed age, language, and income cells. The age 18 to 44, other-language, lower-income cell has a raw factor of 3.13328156 and hits the 3.0 bound. Kish effective sample size falls from 548.95483815 under respondent base weights to 527.00399458 under adjusted weights.

`PERWT24F` is the official MEPS final person weight. The added factor is teaching-only and adjusts only the synthetic local response layer. It is not an official MEPS or HCAHPS weight.

## Known-truth result

The bounded adjustment improves all three synthetic comparisons relative to base weighting alone. Adjusted absolute bias remains 3.14500108 percentage points for Q22, 5.26048779 for Q23, and 4.20274444 for the teaching composite. The adjustment helps in this simulation and does not remove bias.

## Protection and claim boundary

Before real fielding, the council still needs named patient or caregiver, survey-methods, accessibility, language-access, privacy, responsible-AI, clinical, faculty, and independent reproduction reviews. Plain-language notice, refusal and stop-contact routes, accessible modes, minimum necessary use, role-based access, retention, deletion, incident response, and urgent safety-content handling remain required.

The CMS and AHRQ source files are public. The patient-level Q21, Q22, Q23, response, mode, and missingness fields are synthetic procedural teaching data. This checkpoint does not establish a real patient, hospital, HCAHPS, access, equity, prevalence, mode, benefit, or clinical result.

## Readiness decision

The package may enter Module 04 linked analysis with conditions. Clinical action, hospital ranking, real fielding, and patient targeting remain prohibited. Machine learning remains reserved for Module 06.
