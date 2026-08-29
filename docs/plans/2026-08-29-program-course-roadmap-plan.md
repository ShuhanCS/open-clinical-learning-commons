# Open Clinical Learning Commons program course roadmap

- Status: implemented and verified locally
- Date: 2026-08-29
- Source: `C:\Users\Shuha\Downloads\OneDrive_2026-08-29 (1).zip`
- Release decision: minor version `0.7.0` to `0.8.0`

## Goal

Make the public Learning Commons page show the complete program path described by the supplied curriculum documents. Keep the clinical visualization atlas and Module 04 lesson as the first working example rather than presenting the remaining courses as finished releases.

## Course inventory

| Stage | Course | Prerequisite | Final deliverable |
|---|---|---|---|
| Foundation | FND-1: Healthcare Data Foundations | None | Reproducible data toolkit |
| Foundation | FND-2: Modeling, Inference, and Reproducible Analytics | FND-1 | Analytics package and model card |
| Applied | APP-1: Data for Clinical Care | FND-1 and FND-2 | Clinical care improvement brief |
| Applied | APP-2: Data for Patient Experience and Engagement | FND-1 and FND-2 | Patient experience and engagement package |
| Applied | APP-3: Data for Clinical Performance and Improvement | FND-1 and FND-2 | Clinical performance improvement package |
| Applied | APP-4: Data for Clinical Decision Support | FND-1 and FND-2 | Clinical decision support package and safety case |
| Applied | APP-5: Data for Population Health and Equity | FND-1 and FND-2 | Population intervention analytics plan |
| Applied | APP-6: Data for Health Research and Innovation | FND-1 and FND-2 | Research and innovation package |
| Applied | APP-7: Data for Health Systems Strategy, Finance, and Value | FND-1 and FND-2 | Strategic investment decision package |
| Capstone | CAP-0: Capstone Preparation | FND-1, FND-2, and at least five applied courses | Approved capstone proposal |
| Capstone | CAP-1: Capstone: Learning Health System Analytics | FND-1, FND-2, six applied courses, and CAP-0 | Final package, oral defense, and reflection |

## Public page changes

- Broaden the page title and introduction from one visualization course to the Learning Commons program.
- Add a curriculum path with foundation, applied, and capstone stages.
- Give every course its credits, prerequisites, plain-language purpose, seven weekly topics, and final deliverable.
- Mark the visualization atlas as the current working example and keep all existing lab links and interactions intact.
- Add a direct curriculum link to the page navigation.

## Release checks

- All 11 supplied course documents appear exactly once.
- Every course shows seven weekly topics and the correct prerequisites.
- Existing chart-atlas and Module 04 self-checks continue to pass.
- The page remains usable at mobile, tablet, and desktop widths.
- Keyboard focus, native disclosure controls, headings, and labels remain accessible.
- Repository version and visible page version both read `0.8.0`.
