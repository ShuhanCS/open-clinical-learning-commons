# Nutrition Data Rounds 40-hour HHS competency crosswalk

- Status: working appendix to the canonical specification
- Date: 2026-09-01
- Specification version: `NDR-0.1`
- Proposed learners: Harvard-Affiliated Emergency Medicine Residency residents
- Total: 16 competencies, five HHS domains, 40.0 hours

## Purpose

This crosswalk allocates every proposed curriculum hour to a competency in the HHS Medical Education Nutrition Competency Framework. It also connects each competency to computational resident work and observable assessment evidence.

The final selection depends on a baseline inventory of the existing HAEMR curriculum and review by a qualified nutrition professional. Until those reviews occur, this is a proposed design rather than a claim about HAEMR's current gaps or an approved residency curriculum.

The HHS framework is the source of record for the complete competency wording and hour equivalents:

https://www.hhs.gov/sites/default/files/nutrition-competencies-framework.pdf

## Selection rules

Each selected competency must:

1. change an emergency physician's nutrition assessment, evidence use, communication, consultation, referral, or safety judgment;
2. fit a browser-based case without requiring residents to write code;
3. produce structured work that can be scored with transparent rules;
4. preserve the roles of registered dietitians and other nutrition professionals;
5. work with synthetic patients and public or openly usable source data; and
6. contribute once, and only once, to the 40-hour total.

Analytics, visualization, simulation, and AI audit are teaching methods. They do not create extra nutrition hours.

## Domain arithmetic

| HHS domain | Selected competencies | Hours |
|---|---|---:|
| Domain 1: Foundational Nutrition Knowledge | 1, 3, 6, 7, 8, 11, 12, 20 | 17.0 |
| Domain 2: Nutrition Assessment and Diagnosis | 22, 24, 26 | 11.0 |
| Domain 3: Food and Nutrition-Related Communication Skills | 30 | 2.5 |
| Domain 4: Collaborative, Interprofessional Referral and Patient Management | 39, 40, 42 | 7.5 |
| Domain 7: Medical Interventions in Combination with Lifestyle Practices | 56 | 2.0 |
| **Total** | **16 competencies across five domains** | **40.0** |

## Competency-to-evidence map

The labels below are concise references to the official framework. The linked framework controls the full wording.

| HHS number | Domain | Hours | Allocation | Working label | Computational learning activity | Observable assessment evidence |
|---:|---|---:|---|---|---|---|
| 1 | Foundational Nutrition Knowledge | 3.0 | Round 1 | Nutritional content of foods, macronutrients, and micronutrients | Compare versioned food records and identify which nutrients support or contradict a claim. | Correct field selection, unit handling, comparison, and source citation. |
| 3 | Foundational Nutrition Knowledge | 3.0 | 0.5 in Round 3; 2.5 in Round 4 | Identify nutrient deficiencies and recommend foods or supplements | Interpret a synthetic presentation, distinguish a plausible deficiency from unsupported inference, and choose a bounded next step. | Pattern recognition, urgency, contraindication, food or supplement option, and referral gate. |
| 6 | Foundational Nutrition Knowledge | 2.5 | 1.5 in Round 4; 1.0 in Round 6 | Drug-nutrient interactions | Reconcile a synthetic medication list with nutrition history and laboratory context. | Correct interaction flag, evidence source, mitigation, and escalation choice. |
| 7 | Foundational Nutrition Knowledge | 2.0 | Round 2 | Minimally processed and highly processed foods | Compare foods using ingredients, nutrient data, and stated processing context without relying on one proxy. | Correct classification evidence, uncertainty statement, and defensible comparison. |
| 8 | Foundational Nutrition Knowledge | 2.0 | 1.0 in Round 1; 1.0 in Round 2 | Interpret nutrition labels and menu labeling | Resolve serving sizes, units, daily values, and menu claims in structured examples. | Calculation accuracy, label interpretation, and misleading-claim detection. |
| 11 | Foundational Nutrition Knowledge | 2.0 | 1.0 in Round 2; 1.0 in Round 3 | Healthy balanced diet under national guidance | Apply national guidance to a constrained synthetic discharge scenario. | Guideline selection, feasible option, scope, and source citation. |
| 12 | Foundational Nutrition Knowledge | 1.5 | Round 3 | Evidence-based beverage guidance | Choose case-specific beverage guidance when hydration or metabolic risk makes it relevant. | Appropriate recommendation, contraindication check, and concise rationale. |
| 20 | Foundational Nutrition Knowledge | 1.0 | Round 3 | Food bioavailability and preparation | Evaluate a case-relevant preparation or food-pairing claim against a fixed evidence source. | Correct mechanism, limit, and supported recommendation. |
| 22 | Nutrition Assessment and Diagnosis | 4.0 | Round 5 | Integrate history, measurements, and laboratory findings | Build a nutrition risk assessment from a synthetic chart and identify missing information. | Data selection, calculation, interpretation, uncertainty, and next action. |
| 24 | Nutrition Assessment and Diagnosis | 3.0 | Round 6 | Interpret examination data and biomarkers for malnutrition risk | Interpret synthetic examination and laboratory patterns without treating one measure as diagnostic. | Pattern interpretation, false-certainty rejection, severity, and escalation gate. |
| 26 | Nutrition Assessment and Diagnosis | 4.0 | Round 7 | Continuous glucose monitoring interpretation | Explore a synthetic CGM trace, identify supported patterns, and test whether a proposed dietary explanation fits the data. | Pattern identification, uncertainty, confounding, and safe next step. |
| 30 | Food and Nutrition-Related Communication Skills | 2.5 | Round 8 | Integrate evidence-based nutrition information into care | Turn a source-grounded evidence packet into a bounded emergency care or discharge recommendation. | Evidence fit, clinical scope, patient constraint, and recommendation accuracy. |
| 39 | Collaborative, Interprofessional Referral and Patient Management | 2.5 | Round 9 | Work with other health professionals for multidisciplinary nutrition care | Complete a branching case that requires correct sequencing of emergency medicine, dietetics, pharmacy, and follow-up roles. | Role selection, handoff content, escalation, and closed-loop plan. |
| 40 | Collaborative, Interprofessional Referral and Patient Management | 2.0 | 1.5 in Round 8; 0.5 in Round 9 | Make appropriate referrals | Select the appropriate discipline, urgency, information transfer, and contingency for synthetic cases. | Indication, destination, urgency, handoff content, and contingency. |
| 42 | Collaborative, Interprofessional Referral and Patient Management | 3.0 | 1.0 in Round 9; 2.0 in Round 10 | Integrate evidence-based digital health technology | Compare a versioned set of digital nutrition tools and determine whether one is appropriate for the case. | Evidence threshold, accessibility, privacy and burden check, and recommendation limit. |
| 56 | Medical Interventions in Combination with Lifestyle Practices | 2.0 | Round 10 | Responsible use of AI for nutrition advice | Audit a fixed AI-generated response against named sources and the synthetic patient record. | Unsupported-claim detection, safety error detection, source verification, rejection or revision, and human accountability. |

## Round arithmetic

| Round | Competency allocation | Hours |
|---|---|---:|
| Round 1 | 1 (3.0), 8 (1.0 of 2.0) | 4.0 |
| Round 2 | 8 (1.0 of 2.0), 7 (2.0), 11 (1.0 of 2.0) | 4.0 |
| Round 3 | 11 (1.0 of 2.0), 12 (1.5), 20 (1.0), 3 (0.5 of 3.0) | 4.0 |
| Round 4 | 3 (2.5 of 3.0), 6 (1.5 of 2.5) | 4.0 |
| Round 5 | 22 (4.0) | 4.0 |
| Round 6 | 24 (3.0), 6 (1.0 of 2.5) | 4.0 |
| Round 7 | 26 (4.0) | 4.0 |
| Round 8 | 30 (2.5), 40 (1.5 of 2.0) | 4.0 |
| Round 9 | 39 (2.5), 40 (0.5 of 2.0), 42 (1.0 of 3.0) | 4.0 |
| Round 10 | 42 (2.0 of 3.0), 56 (2.0) | 4.0 |
| **Total** | **16 competencies** | **40.0** |

## Assessment gates

The automated score cannot compensate for an unsafe required choice. The final case blueprints must identify noncompensable errors, including any case-specific failure to escalate, dangerous recommendation, inappropriate referral, or acceptance of unsupported AI advice as clinical fact.

Automation checks structured evidence. It does not certify that the clinical answer key is correct. Emergency medicine and nutrition reviewers own that judgment before release.

## Approval gates

- HAEMR curriculum leadership confirms the baseline gaps, selected competencies, resident years, schedule, and required or elective status.
- A qualified nutrition professional verifies the competency interpretation, evidence sources, answer keys, and scope boundaries.
- An emergency medicine clinician educator verifies the cases, decisions, safety gates, and residency relevance.
- The Healthcare Data Analytics Program confirms its proposed curriculum design, data, assessment, and evaluation role.
- The Department of Emergency Medicine confirms its proposed sponsorship and implementation role.
- The writing team keeps this crosswalk, the canonical specification, Toolkit, and Curriculum Overview numerically identical.

Competencies outside this map may appear as context. They must not be claimed as taught or counted unless the team adds explicit time, instruction, and assessment and preserves the 40-hour total.
