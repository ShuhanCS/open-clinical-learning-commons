# Open Clinical Learning Commons course and module site

- Status: implemented and verified locally
- Date: 2026-08-29
- Curriculum source: `C:\Users\Shuha\Downloads\OneDrive_2026-08-29 (1).zip`
- Release decision: minor version `0.8.0` to `0.9.0`

## Goal

Give learners one home page where they can see all 11 courses, open any course, and reach a dedicated page for each of its seven modules. Preserve the existing clinical visualization lesson as the first runnable learning asset.

## Site structure

| Page | Purpose | Route |
|---|---|---|
| Home | Show the complete foundation, applied, and capstone path | `/index.html` |
| Course | Show one course, its prerequisites, purpose, and seven modules | `/course.html?id=FND-1` |
| Module | Show one module's outcome, topics, submission, and workload | `/module.html?course=FND-1&week=1` |
| Working lesson | Preserve the current visualization atlas and guided case | `/courses/data-visualization/atlas.html#atlas` |

One shared curriculum data file will hold the 11 courses and 77 modules. The course and module pages will validate query parameters and render from that source, avoiding 77 copied pages that would drift apart.

## Content contract

Every course includes:

- course code, title, stage, credits, format, and prerequisites;
- a plain-language description;
- seven module links;
- the final course deliverable.

Every module includes:

- course and week identity;
- module title and learning outcome;
- main topics;
- required submission;
- estimated workload;
- previous and next module navigation;
- an honest roadmap or working-release status.

## Design direction

Use an editorial clinical field-guide style: warm white paper, deep ink, ConductScience blue, cyan data accents, a serif display face, compact technical labels, and a visible route line through the curriculum. The interface must remain readable, keyboard accessible, and useful without decorative images.

## Release checks

- The home page shows 11 unique courses in 2 foundation, 7 applied, and 2 capstone groups.
- Every course route renders exactly seven modules.
- All 77 course/week combinations render a module page.
- Invalid course or week parameters show a useful recovery link.
- Previous and next navigation stays inside the selected course.
- The visualization atlas and all of its downloads still resolve.
- Mobile, tablet, and desktop layouts have no horizontal overflow.
- Repository and visible site versions read `0.9.0`.
