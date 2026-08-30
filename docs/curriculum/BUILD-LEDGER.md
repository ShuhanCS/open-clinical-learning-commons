# Curriculum build ledger

- Current release: 0.17.1
- Last updated: 2026-08-29
- Active phase: DA-730 module specification and build
- Last completed unit: DA-730 Week 3 visualization judgment checkpoint
- Next unit: DA-730 Module 07, Color and accessible visual communication

## Confirmed decisions

- FND-1 and FND-2 are separate straight-through technical foundation courses.
- APP-1 through APP-7 revisit foundations through different domain methods and decisions.
- Applied courses use seven distinct modules. Module 6 contains the week-6 application checkpoint and an embedded half-week machine-learning extension.
- Module 7 is the final clinician-led leadership block.
- Every applied course has cumulative checkpoints at instructional weeks 3 and 6 and on the official last day of the half-term.
- Three-credit courses retain 112.5 total learner hours.
- CAP-0 remains zero credits unless approved program documents change it.
- DA-730 remains separate and moves from a Tableau-centered source course to a concept-first, software-flexible visualization course.
- Public clinical sources, open datasets, and documented synthetic teaching data are core course materials.
- Every module requires exact learner, instructor, data, assessment, rubric, accessibility, and release deliverables.

## Source status

- `Curriculum-30-Credits-2026-08-29.zip` inspected: 11 DOCX course files.
- `OneDrive_2026-08-29 (1).zip` inspected: same 11 DOCX course files and file sizes.
- MGH Institute 2026-2027 academic calendar checked: offerings are labeled half-terms and span 49 to 52 elapsed days.
- Master architecture: `docs/specs/2026-08-29-curriculum-master-architecture-spec.md`.
- DA-730 Module 01 uses the CMS HCAHPS 2026-08-13 release, filtered to all 65 Massachusetts `H_RECMND_DY` rows. The file contains 56 reported and 9 unavailable results for 2024-10-01 through 2025-09-30.
- Module 01 teaching extract SHA-256: `56fa078a15ffd456f2fa8eee441e46d37462715346effb774d606b65e2300b74`.
- Module 01 build, 15-check validator, tiered lab, two critique charts, assessment, instructor key, and release record are complete as a runnable release candidate.
- DA-730 Module 02 reuses the Module 01 HCAHPS extract through a 10-row perception-task release with two dot, bar, table, pie, and bubble trials.
- Module 02 task SHA-256: `b792637411a00c67baa30d70688e5a9b8353cee8a2758251419e84c0c4c1cbe6`.
- Module 02 build, 12-check validator, 10 stimuli, scorer, two critique charts, assessment, instructor key, and release record are complete as a runnable release candidate.
- DA-730 Module 03 reuses the Module 01 HCAHPS extract and adds a 10-case chart-selection table covering comparison, lookup, relationship, distribution, time, composition, flow, geography, monitoring, and evidence verification.
- Module 03 case SHA-256: `0f295bd9bf94e9f5800e4fdaebea303d8cc0b28ccd3afcb01603d8e1c0a2eff8`.
- Module 03 build, 13-check validator, two HCAHPS charts, one exact-value table, two selection matrices, one flawed-dashboard critique, assessment, instructor key, and release record are complete as a runnable release candidate.
- DA-730 Module 04 preserves every national CMS OP_18b row from the 2026-08-13 Timely and Effective Care release: 4,658 hospital rows, including 4,081 reported and 577 unavailable values. The reported hospital median is 148 minutes.
- Module 04 CMS extract SHA-256: `c9603109d4ea251b8096a655c27ad42cd6313bdb1309999bee3eb37ce79ec67d`.
- Module 04 synthetic encounter release 0.2.0 contains 8,392 rows and SHA-256 `27c1c0feed8beb4ab0ac6dc77eaa3d1ed95c07b89f52f4881c25954ba43fbc55`.
- Module 04 real, null, and trivial variants pass 26, 23, and 23 checks. The lab creates four figures and a monthly table; the critique creates three intentionally flawed figures.
- DA-730 Module 05 preserves 6,290 CDC PLACES `DIABETES` rows, including crude and age-adjusted prevalence for all 3,144 counties and the source national summary.
- Module 05 CDC extract SHA-256: `764b46c63508a5a6a2510ee2766866ab91abdeeaf7d633f50ae70a3aff561de6`.
- Module 05 also preserves all 3,222 ACS county rows derived from B01001 and 100 generalized North Carolina Census county features.
- Module 05 teaching table contains 100 North Carolina counties and SHA-256 `1528b204830966dff88e00f57fc4f77b8dcf5db135daa122e8aff3679fdf32c7`.
- Module 05 passes 32 data checks. Its lab creates four figures and a decision table; its critique creates two deliberately flawed figures.
- In the pinned release, the top 12 modeled-count and top 12 age-adjusted-prevalence lists have zero counties in common. The largest count-to-adjusted rank change is 93 places.
- DA-730 Module 06 validates the complete 67,060-row CMS Unplanned Hospital Visits hospital download before preserving all 4,790 `READM_30_HF` rows, all 14 national summary rows, and all 32 official footnotes.
- Module 06 national hospital extract SHA-256: `e69fcee79711ef8496cb32205b492e6e3a788c4e63009bc1330a84216b0edeba`.
- Module 06 Massachusetts teaching table contains 65 hospital rows and SHA-256 `33e6284a1064bb12600903526e4e65c009f875d9e6f6a3f25783d3a9a4b00727`.
- Module 06 passes 42 data checks. Its lab creates four figures and a decision table; its critique creates two deliberately flawed figures.
- The Massachusetts case has 53 reported estimates, 52 CMS-classified no different from the national rate, 1 worse, 2 too few, and 10 not available. Only 1 of the ten highest point estimates is source-classified worse.
- All 1,378 displayed Massachusetts interval pairs overlap descriptively. The module states that this is not a pairwise hypothesis test and does not prove equivalence.
- DA-730 Checkpoint 1 maps Modules 03 through 06 to exact comparison, distribution, rate, and uncertainty figure names while carrying Module 01 encoding choices and Module 02 perception evidence into the selection matrix.
- The checkpoint package assembles four figures and four editable R files from the released module data, supplies four complete source records and six writing templates, and validates the completed folder contract with a Python standard-library check.

## Pending confirmation

- Confirm that the intended Joe Joseph, MD, is the Sound Physicians hospital medicine leader publicly listed with FHM/SFHM and Regional Chief Medical Officer experience.
- Confirm publishable biography and current title directly before release.

## Next resume instructions

1. Read the DA-730 Module 07 brief and the Module 06 accessibility handoff.
2. Write `docs/curriculum/courses/DA-730/modules/07-color-accessible-communication-spec.md` using the 21-section contract.
3. Reuse the Module 06 interval and status case so color changes do not change the statistical claim.
4. Build screen, print, grayscale, redundant-encoding, and text-alternative exercises.
5. Verify and release Module 07, then continue to Module 08.
