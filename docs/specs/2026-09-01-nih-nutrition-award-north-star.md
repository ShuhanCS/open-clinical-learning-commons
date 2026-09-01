# Open Nutrition Data Commons for Nursing Education

- Status: working North Star for discussion
- Date: 2026-09-01
- Commons release: `0.97.0`
- Challenge: NIH Integration of Nutrition Training into Health Care Education Challenge
- Working track: Developing
- Working program type: Nursing
- Submission deadline: September 15, 2026, 11:59 PM Eastern Time

## Purpose

This specification defines the submission we are trying to create before the team writes the 15-page Curriculum Overview or builds nutrition modules. It keeps the learner outcome, prize criteria, team roles, technical boundary, and evidence requirements stable while details are refined.

This is a prize submission, not a request for NIH to finance speculative infrastructure. The application must show that the team, development environment, educational partnership, and national distribution path are credible now.

## North Star

> Build a 53-hour, competency-mapped nutrition data and responsible AI pathway for nursing education that is engineered by the Mass General Brigham Department of Emergency Medicine Division of Artificial Intelligence, academically co-designed by the Mass General Brigham University Health Data Analytics Program, reviewed with nursing educators and nutrition experts, and released as a portable national teaching package through the Open Clinical Learning Commons.

The learner outcome comes before the platform. A nursing learner completing the pathway should be able to recognize nutrition risk, reason from clinical and population data, evaluate evidence, communicate within nursing scope, make an appropriate referral, and identify when an AI-supported nutrition recommendation is unsupported, unsafe, biased, or irrelevant to the patient.

The adoption test is equally important:

> A nursing educator outside MGB should be able to understand the full pathway in 30 minutes, inspect the competency and hour map, select a module for local use, and run it without MGB credentials, protected health information, or proprietary software.

## Prize thesis

The proposed entry is stronger than a collection of nutrition lectures because it joins four capabilities in one reusable model:

1. Division AI builds and maintains the analytic learning environment, reproducible assets, and responsible AI activities.
2. The Health Data Analytics Program turns nutrition questions into applied work with data, visualization, interpretation, and evaluation.
3. Nursing educators connect the work to nursing learners, clinical practice, curriculum placement, and an adoption pathway.
4. Nutrition experts validate the evidence, content boundaries, referrals, and scope of practice.

The public value is a portable curriculum package, not access to MGB infrastructure. Microsoft Azure supports development and validation, while the public release must remain platform-independent.

## Working submission structure

| Role | Working assignment | Evidence needed before submission |
|---|---|---|
| Lead Entity | Mass General Brigham | Authorized representative, confirmation of eligibility basis, and confirmation that this is its only entry. |
| Submitting unit and builder | Department of Emergency Medicine, Division of Artificial Intelligence | Division leadership approval and a precise, supportable description of the Azure environment and engineering capacity. |
| Lead Point of Contact | Shuhan He, acting in an authorized Division AI capacity | Written confirmation that the Lead Entity authorizes registration and submission. |
| Academic collaborator | Mass General Brigham University Health Data Analytics Program | Collaboration letter or other institutional confirmation of the program's role. |
| Health Data Analytics lead | Shuhan He, Program Director | Description of curriculum, assessment, and analytics contributions. |
| Nursing education collaborator | To be confirmed | Letter describing faculty review, nursing learner context, and a realistic pilot or adoption pathway. |
| Nutrition content reviewer | To be confirmed | Named RDN or other qualified nutrition professional with a specific review commitment. |
| Public delivery layer | Open Clinical Learning Commons | Public repository, licensing, module structure, and a demonstrable sample. |
| Development environment | MGB-procured Microsoft Azure environment | Approved wording about procurement, governance, capabilities, and limits. |

The Lead Entity and Partner Entity treatment must be resolved against the Participation and Team Agreement. If Mass General Brigham University is a formal Partner Entity, its authorized representative must sign. If its programs participate only as collaborators, the application must still have permission to use their institutional names and describe their commitments.

## Submission boundary

### In scope

- A 53-hour modular nutrition pathway designed for nursing education.
- Evidence-based nutrition content mapped to selected HHS competencies.
- Synthetic and legally reusable open data.
- Applied analytics, visualization, communication, referral, and responsible AI activities.
- Online, case-based, simulation, and experiential learning formats.
- Reusable faculty guidance, learner materials, datasets, code, rubrics, and evaluation tools.
- An implementation and sustainability plan for nursing programs with different resources.

### Out of scope for this submission

- Real patient records or protected health information.
- Patient-facing AI or autonomous clinical recommendations.
- Claims that the curriculum is approved, required, implemented, or effective unless documented.
- A new learning management system.
- A requirement that adopters purchase Azure or use MGB infrastructure.
- A complete rebuild of the existing Commons curriculum.
- Clinical nutrition practice beyond the learner's professional scope.

## Draft 53-hour pathway

This is a planning map. Nursing educators and the nutrition reviewer must approve the final sequence, learner level, and hour assignments.

| Component | Hours | Primary learner work | HHS connection |
|---|---:|---|---|
| Nutrition foundations and evidence | 7 | Interpret core nutrition concepts and distinguish strong evidence from unsupported claims. | Foundational nutrition knowledge; critical use of evidence. |
| Nutrition assessment and clinical data | 8 | Combine history, measurements, laboratory findings, and context to identify nutrition risk. | Nutrition assessment and diagnosis. |
| Food access, public health, and equity | 6 | Analyze food and nutrition needs, access barriers, population patterns, and referral options. | Public health nutrition. |
| Communication and behavior change | 6 | Practice brief, respectful, evidence-based nutrition communication and shared goals. | Food and nutrition-related communication skills. |
| Interprofessional referral and management | 5 | Identify scope boundaries and coordinate with dietitians and other professionals. | Collaborative, interprofessional referral and patient management. |
| Applied nutrition analytics and visualization | 8 | Build reproducible summaries and visual explanations from synthetic and open nutrition data. | Additive data literacy and evidence interpretation competencies. |
| Responsible AI and digital nutrition tools | 6 | Test AI-generated guidance, document sources, identify bias and unsafe advice, and preserve human accountability. | Digital health technology integration; responsible use of AI for nutrition advice. |
| Integrated nursing case and portfolio | 7 | Complete and defend one evidence chain from assessment through communication, referral, and follow-up. | Integrated demonstration across selected domains. |
| **Total** | **53** |  |  |

## Minimum release package

The Developing Track entry does not need every lesson to be fully implemented, but it needs enough concrete material to make the plan believable.

1. A complete 53-hour curriculum and competency map.
2. One representative module built to runnable release-candidate quality.
3. One synthetic or open dataset with provenance, terms, data dictionary, and known limits.
4. One worked learner case and one independent assessment task.
5. One scoring rubric and one evaluation instrument.
6. A faculty implementation guide and a low-resource adoption path.
7. Letters confirming the Division AI, Health Data Analytics, nursing education, and nutrition-review roles.
8. A public-facing three-page toolkit that is useful without access to the scored application.

## Official award evaluation criteria

The Developing Track Curriculum Overview is scored on eight criteria worth 0 to 5 points each. The maximum is 40 points.

| Criterion | Our 5-point standard | Required evidence |
|---|---|---|
| Framework | Every claimed hour and competency is traceable to a lesson, learner action, and assessment. | 53-hour map, competency crosswalk, module specifications, and nutrition expert review. |
| Innovation | Data and AI change what learners can practice, inspect, and defend. The technology is not ornamental. | Applied cases, auditable AI task, reproducible data exercise, and comparison with ordinary instruction. |
| Clarity of teaching methods | Another educator can tell exactly what the learner and instructor do, in what order, for how long, and with what output. | Module map, sample lesson, faculty guide, learner instructions, and delivery plan. |
| Means to address identified competency gaps | The application documents a specific current gap and maps each gap to a curriculum response. | Baseline curriculum inventory, gap analysis, stakeholder input, and response matrix. |
| Evaluation methods | Measures cover knowledge and performance and can be run during a pilot. | Pre and post measures, performance rubric, AI audit rubric, implementation measures, and feedback loop. |
| Integration of innovative approaches | Cases, simulation, data laboratories, visual explanation, and AI critique are tied to outcomes. | Sample artifacts and a rationale for each modality. |
| Context within medical or nursing education | The pathway has a credible nursing home, learner level, calendar, approval path, and required or elective status. | Nursing letter, integration map, implementation timeline, and governance steps. |
| Interdisciplinary approach | Each discipline owns necessary work, and the collaboration changes the curriculum. | Role table, named contributors, letters, review records, and decision rights. |

Scalability remains a required submission theme and a cross-cutting expectation. It must be demonstrated in the Curriculum Overview and public toolkit even though the Developing Track rubric does not list it as a ninth scored criterion.

## Who evaluates and judges

NIH has published the judging structure but not the names of individual judges.

1. Administrative triage reviews eligibility, completeness, and applicability to scope.
2. A technical Evaluation Panel with relevant subject-matter expertise scores eligible submissions.
3. A Judging Panel made up of federal employees from NIH and potentially other federal agencies considers the technical evaluations and selects winners, pending final approval.
4. The Award Approving Official makes the final award decision.

We will not invent judge identities, affiliations, or preferences. The internal panel below simulates the expertise and questions the published process is likely to require.

## Simulated review panel

| Panel role | Primary criteria | Review posture | Required challenge question |
|---|---|---|---|
| Nutrition science and dietetics reviewer | Framework; competency gaps | Protect content accuracy and professional scope. | Which claimed competency lacks qualified review, enough learner time, or an assessment? |
| Nursing curriculum reviewer | Context; teaching clarity | Test whether this belongs in real nursing education. | Where do the 53 hours fit, who teaches them, and what will nursing learners do differently? |
| Learning science and assessment reviewer | Teaching clarity; evaluation | Look for alignment among outcomes, practice, and measurement. | What learner performance would prove competence rather than exposure? |
| Clinical AI and data reviewer | Innovation; innovative approaches | Separate meaningful analytic learning from technology decoration. | Why is data or AI necessary here, and how will learners catch a wrong answer? |
| Implementation and open education reviewer | Interdisciplinary approach; scalability | Test portability, workload, maintenance, and reuse. | Can a resource-constrained nursing program adopt this without MGB accounts or specialist engineers? |
| Simulated federal adjudicator | Overall public value | Decide whether the entry is in scope, feasible, distinctive, and nationally useful. | Why should NIH recognize and disseminate this model instead of another nutrition curriculum? |

### Simulation procedure

1. Run administrative triage before scoring. A failed eligibility, scope, completeness, hour, signature, or one-entry check stops the review.
2. Give every reviewer the same submission package and require an independent 0 to 5 score for all eight criteria.
3. Require one evidence citation and one unresolved concern for every score below 5.
4. Discuss any criterion with a score range of 2 or more points across reviewers.
5. Revise the submission and repeat the panel after the evidence package changes materially.

### Internal go standard

- Total score of at least 34 of 40.
- No criterion below 4.
- No unresolved administrative triage failure.
- No unsupported claim about eligibility, approval, partnership, Azure, implementation, or effectiveness.
- A one-page executive summary that states the learner, problem, 53-hour approach, team, evidence, and national value.

This is an internal quality bar. NIH has not published a minimum winning score.

## Administrative triage simulation

| Check | Submission evidence | Current status |
|---|---|---|
| Eligible Lead Entity | Lead Entity name and accreditation basis. | Open decision. |
| Authorized Point of Contact | Written institutional authority to register and submit. | Open decision. |
| One entry per institution | Confirmation from each formal participating institution. | Open decision. |
| Correct track | Developing Track selected consistently. | Working decision. |
| Applicable scope | Nursing learners, nursing curriculum context, and 53 hours. | Working design. |
| Complete package | Curriculum Overview, Toolkit, and signed Participant Agreement as separate PDFs. | Not started. |
| Formatting | Page size, margins, font, page limits, language, and prohibited-logo rules. | Not started. |
| Deadline | Complete submission by September 15, 2026, 11:59 PM Eastern Time. | Fixed. |

## Fifteen-day submission package

The final entry requires three separate PDFs:

1. Curriculum Overview, no more than 15 pages excluding appendices.
2. Nutrition Education Toolkit form plus a public-facing toolkit PDF no more than 3 pages.
3. Participation and Team Agreement signed by the Lead Entity and any formal Partner Entities.

The working build should also produce a competency appendix, 53-hour map, representative module, evaluation instruments, implementation timeline, and support letters. These are evidence for the three required PDFs rather than additional portal deliverables unless the final rules or portal request them.

## North Star decisions to make together

- [ ] Confirm the final title and whether `Open Nutrition Data Commons` is the public program name.
- [ ] Confirm whether the submission is a single-entity MGB entry or an MGB and Mass General Brigham University partnership.
- [ ] Confirm the exact eligibility basis and authorized signer for each formal entity.
- [ ] Name the nursing program, learner level, faculty liaison, and planned curriculum placement.
- [ ] Confirm whether the pathway is required, elective, embedded, or a combination.
- [ ] Approve or revise the draft 53-hour module map.
- [ ] Name a credentialed nutrition reviewer and define the review commitment.
- [ ] Approve the exact public description of the Division's Azure procurement and environment.
- [ ] Choose the representative module that will be built before submission.
- [ ] Confirm licensing for curriculum prose, code, synthetic data, and imported sources.

## Official sources

- Official challenge page: https://www.nih.gov/challenges/integration-nutrition-training-into-health-care-education-challenge
- Submission guide: https://nutritioneducationchallenge.org/wp-content/uploads/2026/05/FINAL_5.21.26_Submission-Guide_NIH-Nutrition-Challenge.pdf
- Participation and Team Agreement: https://nutritioneducationchallenge.org/wp-content/uploads/2026/05/NIH-Nutrition-Education-Challenge-Team-Agreement_5.26.26-1.pdf
- HHS Medical Education Nutrition Competency Framework: https://www.hhs.gov/sites/default/files/nutrition-competencies-framework.pdf
- Challenge FAQ: https://nutritioneducationchallenge.org/faq/
- Mass General Brigham University Health Data Analytics Program: https://www.mgbu.edu/health-rehabilitation-sciences/departments-programs/health-sciences/master-science-healthcare-data-analytics/
- Open Clinical Learning Commons: https://github.com/ShuhanCS/open-clinical-learning-commons
