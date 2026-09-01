# Nutrition Data Rounds

- Status: canonical working specification
- Specification version: `NDR-0.1`
- Date: 2026-09-01
- Commons release: `0.106.1`
- Challenge: NIH Integration of Nutrition Training into Health Care Education Challenge
- Track: Developing
- Program type: Residency Program
- Proposed educational setting: Harvard-Affiliated Emergency Medicine Residency (HAEMR)
- Submission deadline: September 15, 2026, 11:59 PM Eastern Time

## How to use this specification

This is the source of truth for the proposed curriculum and submission strategy. It defines what the product is, what it is not, what must be built before submission, and which questions remain open. The writing team should cite the decision or question ID when proposing a change.

The status words have fixed meanings:

- `Locked` is a project design decision that remains in force until the decision log changes it.
- `Proposed` is the current default, but the named owner must confirm it.
- `Open` needs a decision but does not stop work under the documented default.
- `Blocking` must be resolved before submission.

Locked design decisions do not imply institutional approval. Every institutional role, commitment, resource, purchase, implementation statement, and use of the MGB name remains conditional on the rules and approvals of Mass General Brigham, Mass General Brigham University, Graduate Medical Education, HAEMR, and the Department of Emergency Medicine. The official challenge rules control if this specification conflicts with them.

This document supersedes the earlier food-centered and teaching-kitchen concept for curriculum design. Existing administrative materials that describe food purchases or in-person food sessions must be reconciled before they are circulated as a description of the curriculum.

## Product definition

### Working title

**Nutrition Data Rounds: An Open Computational Curriculum for Emergency Medicine Residency**

### North Star

> Give emergency medicine residents repeated practice recognizing nutrition risk, interpreting nutrition-related data, choosing a safe clinical action or referral, and detecting unreliable AI-generated nutrition advice through self-directed browser cases that provide immediate, transparent feedback.

### The product

Nutrition Data Rounds is a proposed 40-hour longitudinal curriculum made of ten four-hour, browser-based data rounds. Each round begins with a synthetic emergency medicine case and ends with an observable nutrition decision. Residents inspect structured clinical information and public nutrition data, make choices, explain the evidence behind those choices through structured responses, and complete a scored transfer case.

Residents do not need to write code. The curriculum is computational because the cases, data views, decision paths, scoring, feedback, and progress records are computed. Nutrition and clinical reasoning remain the learner-facing subject.

### What success looks like

The project succeeds when all three conditions are met:

1. A resident can complete the pathway and demonstrate the selected HHS nutrition competencies through scored case decisions.
2. A residency outside MGB can inspect the package, run it without MGB credentials or protected health information, and adopt a round with limited local setup.
3. An NIH reviewer can trace every claimed hour and competency to a teaching activity, learner artifact, and evaluation method.

### The problem it solves

Residency programs have limited room for another lecture series and limited access to nutrition faculty for repeated delivery and grading. Nutrition Data Rounds turns the core delivery and assessment into a reusable browser course. Qualified faculty still own the content and curriculum, but they do not need to lecture or manually grade every resident interaction.

The local gap claim remains provisional until HAEMR completes a baseline inventory. The submission must not state that HAEMR lacks specific nutrition competencies without that evidence.

## Locked design decisions

| ID | Decision | Reason |
|---|---|---|
| D-001 | Enter the Developing Track in the Residency Program category. | The challenge permits proposed and early-stage curricula in this track. |
| D-002 | Design for HAEMR residents as the key learners. | The curriculum needs a real graduate medical education setting. |
| D-003 | Use a 40-hour longitudinal design composed of ten four-hour rounds. | Clock hours are easier for reviewers and adopters to verify than an equivalency argument. |
| D-004 | Make the core curriculum computational and self-directed. | The course should not depend on recurring lectures, kitchens, food purchases, or manual grading. |
| D-005 | Do not require residents to program. | Computation is the delivery method, not the learning objective. |
| D-006 | Use synthetic patients and public or openly usable source data only. | This avoids protected health information and makes national reuse possible. |
| D-007 | Use deterministic scoring for the required assessments. | Learners and reviewers must be able to see why an answer passed or failed. |
| D-008 | Use AI-generated advice as an object of critique, not as the final grader or clinical authority. | This supports responsible AI education without making the course depend on unstable model output. |
| D-009 | Build one polished vertical-slice case before submission, not all 40 hours. | The Developing Track permits a proposed curriculum. One working case can establish feasibility. |
| D-010 | Publish through the Open Clinical Learning Commons without requiring MGB Azure, an EHR connection, or proprietary software for adoption. | The national adoption path must be credible. |

## Non-goals for the submission build

The submission build will not include:

- a physical teaching kitchen or required food purchase;
- a new learning management system;
- production EHR integration;
- real patient data;
- patient-facing clinical decision support;
- live generative AI at runtime;
- a research protocol or a claim of curriculum effectiveness;
- compensation or inducement for resident labor;
- ten completed rounds before the deadline; or
- a separate data science course for residents.

Later implementation may add institutionally approved activities, systems, or evaluation methods. Those additions require their own review and do not belong in the current minimum submission.

## Standard four-hour data round

Every round uses the same learner flow so residents and instructors only learn the interface once.

| Step | Resident activity | Minutes | Required output |
|---|---|---:|---|
| 1 | Complete a short pre-check and review a source-grounded evidence brief. | 30 | Baseline responses |
| 2 | Work through a synthetic emergency medicine case. | 60 | Structured nutrition risk and evidence selections |
| 3 | Investigate a prepared public or synthetic dataset through tables and interactive views. | 60 | Data interpretation record |
| 4 | Make and justify a bounded clinical, counseling, or referral decision. | 45 | Structured decision and source citations |
| 5 | Complete an isomorphic transfer case without answer cues. | 30 | Scored assessment record |
| 6 | Review transparent feedback and retry failed items. | 15 | Final attempt record |
| **Total** |  | **240** |  |

An isomorphic case tests the same skill with different patient details and values. It is not the same question repeated.

## Forty-hour curriculum architecture

The hour allocations below add to 40.0 and use the hour equivalents assigned in the HHS Medical Education Nutrition Competency Framework. The [competency crosswalk](2026-09-01-haemr-nutrition-competency-crosswalk.md) is the detailed source for learning activities and assessment evidence.

| Round | Working title | HHS competency allocation | Hours | Main resident decision |
|---:|---|---|---:|---|
| 1 | Food data and nutrient content | 1 (3.0), 8 (1.0 of 2.0) | 4.0 | Decide whether a food comparison and nutrient claim are supported by the source data. |
| 2 | Labels, processing, and national guidance | 8 (1.0 of 2.0), 7 (2.0), 11 (1.0 of 2.0) | 4.0 | Interpret labels and place food choices within national guidance without reducing quality to one nutrient. |
| 3 | Dietary patterns, beverages, and bioavailability | 11 (1.0 of 2.0), 12 (1.5), 20 (1.0), 3 (0.5 of 3.0) | 4.0 | Select feasible food and beverage guidance and explain a case-relevant absorption issue. |
| 4 | Deficiency and drug-nutrient safety | 3 (2.5 of 3.0), 6 (1.5 of 2.5) | 4.0 | Recognize a likely deficiency pattern and identify a drug-nutrient safety concern. |
| 5 | Nutrition risk in the synthetic chart | 22 (4.0) | 4.0 | Integrate history, measurements, and laboratory findings into a bounded nutrition risk assessment. |
| 6 | Biomarkers and medication synthesis | 24 (3.0), 6 (1.0 of 2.5) | 4.0 | Interpret malnutrition risk evidence and choose the safe next step without treating one value as diagnostic. |
| 7 | Continuous glucose monitoring as nutrition data | 26 (4.0) | 4.0 | Interpret a synthetic CGM pattern and identify what the data can and cannot support. |
| 8 | Evidence to care and referral | 30 (2.5), 40 (1.5 of 2.0) | 4.0 | Turn nutrition evidence into an in-scope plan and choose an appropriate referral. |
| 9 | Interprofessional digital nutrition care | 39 (2.5), 40 (0.5 of 2.0), 42 (1.0 of 3.0) | 4.0 | Coordinate roles and select an evidence-based digital support option for a synthetic case. |
| 10 | Responsible digital nutrition capstone | 42 (2.0 of 3.0), 56 (2.0) | 4.0 | Audit AI-generated nutrition advice, reject unsafe claims, and produce an accountable final plan. |
| **Total** | **Ten data rounds** | **16 competencies across five domains** | **40.0** |  |

### Proposed placement across residency

The working schedule is 12 hours in PGY1, 12 hours in PGY2, 8 hours in PGY3, and 8 hours in PGY4. HAEMR leadership must confirm the residency years, required or elective status, and placement within existing education. The curriculum architecture does not depend on this exact distribution.

## Flagship prototype

### Working case

**CGM, poor intake, and the unsafe discharge plan**

The prototype is a 60 to 90 minute vertical slice of the Round 10 experience. A fictional adult with diabetes presents after reduced intake. The learner reviews a synthetic emergency chart, medication list, laboratory results, and CGM trace; inspects prepared nutrition data; selects an in-scope action and referral; and audits a versioned AI-generated discharge recommendation for unsupported or unsafe claims.

The final clinical details and answer key require review by emergency medicine and nutrition professionals. The prototype will not state or imply that it provides patient-specific clinical guidance.

### Scored evidence

The prototype records whether the learner can:

- identify the relevant nutrition risk signals and missing information;
- interpret the CGM pattern within the limits of the synthetic data;
- identify a drug-nutrient or poor-intake safety issue when supported by the case;
- choose an appropriate escalation, consultation, or referral;
- identify unsupported, unsafe, or irrelevant AI-generated statements;
- cite the source that supports the final answer; and
- improve after transparent feedback.

### Definition of done

The prototype is submission-ready when it:

1. runs in a current browser without authentication;
2. uses only versioned synthetic and public source files;
3. exposes scoring rules and answer rationales;
4. produces a downloadable or printable learner result;
5. works by keyboard and includes text alternatives for essential visuals;
6. includes source provenance, known limits, and prohibited-use language;
7. includes a short instructor and reviewer guide;
8. passes one automated content and route check; and
9. has documented emergency medicine and nutrition review status.

## Delivery and technical model

The Open Clinical Learning Commons supplies the existing course package, public site, synthetic-data patterns, and validation approach. The prototype should use the smallest extension of those patterns.

| Layer | Submission design |
|---|---|
| Learner interface | Static browser pages with accessible tables, charts, structured choices, feedback, and retry. |
| Case data | Versioned synthetic chart, laboratory, medication, and CGM files. |
| Public nutrition data | Prepared, versioned extracts with source URL, retrieval date, field definitions, terms, and known limits. |
| AI activity | Fixed, versioned model responses that residents audit. No model call is required during the lesson. |
| Scoring | Deterministic rules for calculations, source selection, safety flags, referrals, and error detection. |
| Results | Local printable result for the prototype. Institutional learner tracking is an implementation decision. |
| Hosting | Public Commons deployment. MGB Azure may support approved internal development but is not an adoption requirement. |

Candidate public sources include:

- USDA FoodData Central API guide: https://fdc.nal.usda.gov/api-guide
- CDC National Health and Nutrition Examination Survey: https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/
- USDA Food Access Research Atlas downloads: https://www.ers.usda.gov/data-products/food-access-research-atlas/download-the-data
- HHS Medical Education Nutrition Competency Framework: https://www.hhs.gov/sites/default/files/nutrition-competencies-framework.pdf

A source is not approved merely because it is public. The submission needs a rights, terms, provenance, and fitness review for every included extract.

## Assessment and evaluation plan

The planned primary learner outcome is change in performance between blueprint-matched pre-course and post-course cases. The evaluation does not depend on self-reported confidence alone.

| Evaluation level | Planned measure | Use |
|---|---|---|
| Learner baseline | Pre-course isomorphic case set | Establish starting performance by competency. |
| Learning | Post-round transfer cases and post-course case set | Measure accurate risk recognition, data interpretation, source use, safe action, referral, and AI error detection. |
| Feedback | Error category, attempt count, and successful retry | Identify where the instruction or feedback fails. |
| Implementation | Completion, time on task, abandonment, technical errors, and faculty support time | Test whether the low-touch model is feasible. |
| Adoption | Time and resources needed for a second program to run one round | Test the national portability claim. |

Required assessment rules:

- Use the same competency blueprint, not the same patient, for pre and post cases.
- Publish the scoring rule for every required item.
- Do not allow a high total score to compensate for a dangerous clinical or referral choice.
- Keep generative AI out of final pass or fail decisions.
- Separate curriculum evaluation from any later human-subjects research determination.

## Human work that remains necessary

The computational model reduces recurring delivery work. It does not remove accountable educational ownership.

| Work | Minimum owner | Expected burden |
|---|---|---|
| Course and platform design | Healthcare Data Analytics curriculum team, subject to institutional confirmation | Concentrated during development and revision |
| Clinical case approval | Emergency medicine clinician educator | Review before release and after material clinical changes |
| Nutrition content approval | Named qualified nutrition professional | Review before release and after material nutrition changes |
| Curriculum placement | HAEMR program leadership | Initial approval and periodic program review |
| Routine learner delivery | Browser course | No live lecturer or manual grading required for the core pathway |
| Cohort monitoring | Named course director or faculty coordinator | Review aggregate completion and flagged safety items once per cohort |

## Proposed institutional model

| Role | Proposed assignment | Evidence required before the role can be claimed as confirmed |
|---|---|---|
| Eligible Lead Entity | Mass General Brigham, exact legal entity pending | Research Management and GME confirmation of legal name, eligibility, accreditation basis, and one-entry clearance |
| Educational setting | Harvard-Affiliated Emergency Medicine Residency | Program leadership support, learner population, curriculum placement, and implementation commitment |
| Institutional sponsor and implementation coordinator | MGB Department of Emergency Medicine | Department leadership authorization and confirmed submission role |
| Curriculum creator and analytics lead | MGB University Healthcare Data Analytics Program | Program confirmation of curriculum, data, assessment, and evaluation responsibilities |
| Point of Contact | Shuhan He, if authorized by the eligible Lead Entity | Written institutional authority to register, communicate, and submit on its behalf |
| Nutrition content reviewer | To be named | Qualifications and written content review responsibility |
| Public delivery layer | Open Clinical Learning Commons | Public route, rights review, demonstrable case, and maintenance owner |

A department, program, laboratory, or individual is not automatically a separate eligible institution. The official Lead Entity and Point of Contact must satisfy the challenge rules.

## NIH scoring strategy

The Developing Track Curriculum Overview receives a global score from 0 to 5 on each of eight criteria, for a maximum of 40 points. Scalability has a required narrative section and is a cross-cutting expectation, but it is not a ninth 5-point Developing Track criterion.

| Criterion | Claim to earn a 5 | Evidence that must exist |
|---|---|---|
| Framework | The 40 hours are fully traceable to selected HHS competencies. | Hour map, detailed crosswalk, learner work, assessment evidence, and nutrition review. |
| Innovation | Computation makes repeated case practice and immediate feedback possible without turning nutrition into a programming course. | Working prototype, comparison with ordinary delivery, and a clear reason for each technology choice. |
| Clarity of Teaching Methods | Another educator can see exactly what the resident does and how long it takes. | Standard round flow, module table, sample case, outputs, scoring rules, and instructor guide. |
| Means to Address Identified Competency Gaps | Every documented local gap has a curriculum response. | HAEMR baseline inventory, gap matrix, and selected competency rationale. |
| Evaluation Methods | The plan measures observable performance and implementation feasibility. | Isomorphic pre and post blueprint, scoring rules, safety gates, and implementation measures. |
| Integration of Innovative Approaches | Open data, synthetic cases, interactive views, and AI audit each serve a nutrition learning outcome. | Prototype artifacts and method-to-outcome map. |
| Context within Medical Education | The curriculum has a credible place across residency. | Required or elective status, PGY placement, governance, course owner, and HAEMR support. |
| Interdisciplinary Approach | Each discipline owns necessary work rather than appearing only in a letter. | Role table, named contributors, review records, and support letters. |

The internal go standard is at least 34 of 40 points, no criterion below 4, no administrative triage failure, and no unsupported institutional or effectiveness claim. This is a project quality bar, not an NIH cutoff.

## Required submission package

The challenge requires three separate PDFs:

| PDF | Limit | Role |
|---|---:|---|
| Curriculum Overview | 15 pages maximum, excluding optional appendices | Primary scored narrative |
| Nutrition Education Toolkit | 3 pages maximum | Public dissemination document, reviewed pass or fail |
| Participant Agreement | Official form length | Eligibility, institutional agreement, and rights terms |

Curriculum Overview pages must be 8.5 by 11 inches with at least 1-inch margins, at least 11-point Arial, and line spacing of at least 1.0. The Title and Executive Summary must be the first page and cannot exceed one page. The document must use the exact required section headings. It must not use HHS or NIH logos or imply federal endorsement.

The required Developing Track headings are:

1. Curriculum Overview Section 1: Title and Executive Summary
2. Curriculum Overview Section 2: Description of the curriculum and how it is designed to serve key learners
3. Curriculum Overview Section 3: Nutrition focus and alignment with the HHS Medical Education Nutrition Competency Framework
4. Curriculum Overview Section 4: Education or training approaches and modalities
5. Curriculum Overview Section 5: Means to address identified competency gaps
6. Curriculum Overview Section 6: Assessment methods
7. Curriculum Overview Section 8: Potential for broader dissemination and scalability
8. Curriculum Overview Section 9: Context within medical or nursing education
9. Curriculum Overview Section 10: Interdisciplinary approach

Section 7 is for Exemplar Track entries and is omitted from the Developing Track narrative.

## Minimum build before submission

| Deliverable | Completion test |
|---|---|
| Canonical specification | Decisions, questions, boundaries, architecture, and change log are current. |
| Forty-hour map | Exactly 40.0 hours with no duplicated competency hours. |
| Flagship prototype | One public, accessible, scored vertical slice passes its automated check. |
| Curriculum Overview | Complete 15-page-or-less narrative using every required heading. |
| Public Toolkit | Complete three-page-or-less PDF plus prepared portal form responses. |
| Evaluation package | Pre and post blueprint, scoring logic, safety gates, and implementation measures. |
| Proposal figure | One readable diagram of the learner loop, curriculum, and portability model. |
| Institutional package | Eligible entity, one-entry clearance, Point of Contact, signer, roles, and Participant Agreement confirmed. |
| Review package | Emergency medicine review, nutrition review, rights review, and simulated score completed. |

The final submission will include at least one clear schematic. The figure should explain the learner loop and national adoption model. It should not be decorative.

## Fifteen-day working schedule

| Date | Exit condition |
|---|---|
| September 1 | Product specification and computational direction locked. |
| September 2 to 4 | Institutional route, Point of Contact, one-entry status, HAEMR role, and content reviewers identified. |
| September 2 to 8 | Flagship prototype built and checked. |
| September 3 to 9 | Curriculum narrative, competency map, evaluation plan, and figure drafted. |
| September 7 to 10 | Emergency medicine, nutrition, and program reviews completed or accurately described as pending. |
| September 10 to 12 | Curriculum Overview and Toolkit assembled within page limits. |
| September 13 | Simulated panel review and correction. |
| September 14 | Institutional signature and target submission. |
| September 15 | Contingency only. Official deadline is 11:59 PM Eastern Time. |

## Question register

Questions should be resolved in this table so the specification stays stable while the team discusses them.

| ID | Question | Current default | Decision owner | Status |
|---|---|---|---|---|
| Q-ADM-01 | What is the exact legal Lead Entity and eligibility basis? | Mass General Brigham is the working entity. | MGB Research Management and GME | Blocking |
| Q-ADM-02 | May Shuhan He act as the institutional Point of Contact and submitter? | Yes only if the Lead Entity gives written authority. | Eligible Lead Entity | Blocking |
| Q-ADM-03 | Does the Lead Entity have one-entry clearance? | No clearance is assumed. | Eligible Lead Entity | Blocking |
| Q-ADM-04 | Who may sign the Participant Agreement? | Use the signer designated by the Lead Entity. | MGB Research Management or legal office | Blocking |
| Q-ADM-05 | Can the institution grant the required rights for the proposed package? | Use only cleared original, public, or permitted assets. | MGB legal or designated rights reviewer | Blocking |
| Q-CUR-01 | Will the submission claim 40 clock hours or a competency equivalent? | Claim the ten-round, 40-clock-hour design. | HAEMR curriculum leadership | Proposed |
| Q-CUR-02 | Is the curriculum required, elective, or mixed? | Required longitudinal pathway. | HAEMR curriculum leadership | Open |
| Q-CUR-03 | Where do the ten rounds fit across residency? | PGY1 12 hours, PGY2 12, PGY3 8, PGY4 8. | HAEMR curriculum leadership | Open |
| Q-CUR-04 | Which current HAEMR nutrition gaps support the selected competencies? | Do not claim local gaps until a baseline inventory exists. | HAEMR curriculum leadership | Blocking for Section 5 |
| Q-CUR-05 | Is Nutrition Data Rounds the final public title? | Use the working title. | Project and institutional communications owners | Open |
| Q-CLN-01 | Who is the qualified nutrition reviewer? | Name one reviewer with authority over nutrition accuracy and scope. | Project leadership | Blocking |
| Q-CLN-02 | Who approves emergency medicine case accuracy? | Name one EM clinician educator. | Department of Emergency Medicine | Blocking |
| Q-CLN-03 | Is the proposed CGM and poor-intake case the prototype? | Build this case unless clinical review identifies a better scenario. | EM and nutrition reviewers | Proposed |
| Q-CLN-04 | Which choices are noncompensable safety failures? | Unsafe disposition, missed escalation, and unsupported AI advice accepted as fact are candidate gates. | EM and nutrition reviewers | Open |
| Q-TECH-01 | Where will the public prototype run? | Existing Open Clinical Learning Commons public deployment. | Commons maintainer | Proposed |
| Q-TECH-02 | How will institutional completion be recorded? | Prototype provides a printable local result; LMS integration is deferred. | HAEMR and institutional IT | Open |
| Q-TECH-03 | Which public datasets pass rights and fitness review? | Start with FoodData Central and synthetic clinical or CGM data. | Data lead and rights reviewer | Open |
| Q-EVAL-01 | What is the primary learner outcome? | Change in blueprint-matched case performance. | Curriculum and assessment leads | Proposed |
| Q-EVAL-02 | Will implementation evaluation be educational quality improvement or research? | Treat submission-stage work as curriculum development; obtain an institutional determination before later learner research. | Institutional review office | Open |
| Q-TEAM-01 | How may the Healthcare Data Analytics Program role be described? | Proposed curriculum creator and analytics lead. | Program and institutional leadership | Blocking |
| Q-TEAM-02 | How may the Department of Emergency Medicine role be described? | Proposed sponsor and implementation coordinator. | Department leadership | Blocking |
| Q-SUB-01 | Which letters are necessary? | Prioritize HAEMR, Department of Emergency Medicine, Healthcare Data Analytics, and nutrition review support. | Submission lead | Open |

## Administrative triage gates

The entry does not proceed to scoring if the institution cannot establish eligibility, authority, completeness, rights, or timely submission. Before final packaging, confirm:

- exact eligible Lead Entity and accreditation basis;
- authorized Point of Contact and Participant Agreement signer;
- one-entry clearance;
- HAEMR participation and curriculum placement;
- all three separate PDFs;
- exact required headings and page rules;
- ownership and permission for every submitted work; and
- portal submission before the deadline.

## Simulated review panel

NIH has published the review structure but not the names of individual judges. Administrative triage precedes technical scoring. A technical Evaluation Panel scores eligible entries, a federal Judging Panel selects proposed winners, and the Award Approving Official makes the final decision.

This fictional panel tests the published criteria:

| Reviewer lens | Question the reviewer must answer |
|---|---|
| Nutrition science and dietetics | Are the selected competencies accurate, adequately taught, and reviewed by a qualified professional? |
| Emergency medicine residency | Does each round change a decision relevant to emergency medicine, and can the pathway fit residency? |
| Graduate medical education | Are placement, supervision, faculty ownership, progression, and approval credible? |
| Learning science and assessment | Does the assessment demonstrate competence rather than exposure or confidence? |
| Clinical AI and data | Do computation and AI audit improve nutrition learning, and are scoring and safety boundaries transparent? |
| Open education and implementation | Can another residency adopt a round without MGB accounts, protected data, or specialist engineers? |

Each simulated reviewer scores all eight criteria independently from 0 to 5, cites one piece of evidence for each score, and identifies one unresolved concern for every score below 5. A score range of 2 or more on any criterion triggers discussion and revision.

## Change log

| Specification version | Date | Change |
|---|---|---|
| `NDR-0.1` | 2026-09-01 | Replaced the broad food-centered concept with Nutrition Data Rounds, a ten-round computational curriculum, and defined the prototype, automation boundary, evaluation plan, decision IDs, and question register. |

## Official sources

- Official challenge announcement and rules: https://www.nih.gov/challenges/integration-nutrition-training-into-health-care-education-challenge
- Submission guide: https://nutritioneducationchallenge.org/wp-content/uploads/2026/05/FINAL_5.21.26_Submission-Guide_NIH-Nutrition-Challenge.pdf
- Participant Agreement: https://nutritioneducationchallenge.org/wp-content/uploads/2026/05/NIH-Nutrition-Education-Challenge-Team-Agreement_5.26.26-1.pdf
- HHS Medical Education Nutrition Competency Framework: https://www.hhs.gov/sites/default/files/nutrition-competencies-framework.pdf
- Challenge portal: https://nutritioneducationchallenge.org/
- Challenge FAQ: https://nutritioneducationchallenge.org/faq/
- Harvard-Affiliated Emergency Medicine Residency: https://haemr.org/
- Mass General Brigham University Health Data Analytics Program: https://www.mgbu.edu/health-rehabilitation-sciences/departments-programs/health-sciences/master-science-healthcare-data-analytics/
- Open Clinical Learning Commons: https://github.com/ShuhanCS/open-clinical-learning-commons
