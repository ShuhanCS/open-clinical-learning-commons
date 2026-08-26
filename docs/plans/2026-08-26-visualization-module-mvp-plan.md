# Visualization module MVP plan

## Goal

Deploy a public, no-login preview of Module 04 that lets a newcomer experience the central lesson without installing R or navigating GitHub.

## First release

- One static page deployed as a Vercel preview.
- A short emergency-department case using the measured Module 04 dataset results.
- Interactive views of the median, mean, 90th percentile, long waits, and January versus December distributions.
- One decision question with immediate feedback.
- Direct downloads for the dataset, lab, assessment, and instructor notes.

## Deliberate limits

The preview has no accounts, learner tracking, grading database, content management system, or hosted R environment. GitHub remains the source for teaching materials.

## Release checks

- Works on narrow and wide screens.
- Keyboard controls and chart descriptions are present.
- Displayed values match the committed synthetic dataset and release record.
- Static page passes its built-in data checks before deployment.

