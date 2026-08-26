# Visualization module MVP plan

## Goal

Deploy a public, no-login preview of Module 04 that lets a newcomer experience the central lesson without installing R or navigating GitHub.

The course teaches data visualization through healthcare decisions. Synthetic healthcare data provides a safe, realistic setting, while chart selection, interpretation, critique, and communication remain the assessed skills.

## First release

- One static page deployed as a Vercel preview.
- A short emergency-department case using the measured Module 04 dataset results.
- Interactive views of the median, mean, 90th percentile, long waits, and January versus December distributions.
- One chart-choice question and one chart-title exercise with immediate feedback.
- Direct downloads for the dataset, lab, assessment, and instructor notes.

## Learning loop

1. Give the learner a healthcare question and an incomplete chart-based claim.
2. Ask which visualization would test the claim before revealing the full evidence.
3. Let the learner compare measures and inspect the distribution.
4. Explain what the first visualization showed and what it hid.
5. Ask the learner to choose a decision-ready chart title that communicates both findings.
6. Offer the dataset and R lab as an optional way to reproduce the visualization.

## Interface direction

- Present the module as a modern learning workspace with a clear top bar, lesson navigation, progress, and one focused activity at a time.
- Use calm white and slate surfaces with ConductScience blue as the primary action color. Reserve coral for the worsening tail of the distribution.
- Keep the page useful without an account, installation, or coding environment.
- Make charts responsive and pair every visual with exact values for assistive technology.

## Deliberate limits

The preview has no accounts, learner tracking, grading database, content management system, or hosted R environment. GitHub remains the source for teaching materials.

## Release checks

- Works on narrow and wide screens.
- Keyboard controls and chart descriptions are present.
- Displayed values match the committed synthetic dataset and release record.
- Static page passes its built-in data checks before deployment.
