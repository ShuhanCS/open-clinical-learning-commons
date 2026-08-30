# Visualization chart atlas plan

## Goal

Expand the public visualization lesson into a chart atlas that helps a new learner choose among the main visualization families used in the course and reproduce each example in R.

## Learner experience

1. Scan ten chart families: comparison, distribution, time, relationship, uncertainty, flow, network, composition, place, and dashboard.
2. Choose a family to see the healthcare question it answers, a labeled example, common alternatives, and a warning about misuse.
3. Read the matching R and ggplot2 example without leaving the page.
4. Download one script that generates all ten example charts.
5. Continue into the existing emergency-department case to practice choosing and interpreting a chart.

## Implementation

- Keep the site as one dependency-free static page.
- Add the atlas to `index.html` and reuse the current color, typography, accessibility, and responsive patterns.
- Render examples with the page's existing SVG helper instead of adding a charting library.
- Add `courses/data-visualization/chart_gallery.R` with small synthetic datasets and ten runnable examples.
- Use `ggplot2` for every example. Use `ggalluvial` only for the Sankey-style patient-flow chart because that is the clearest learner-facing R implementation.
- Bump the preview from `0.6.0` to `0.7.0`.

## Checks

- The atlas lists exactly ten families and every family has a chart renderer, explanation, alternatives, and R snippet.
- The downloadable R script writes ten PNG files and stops if an expected output is missing.
- Keyboard controls, visible focus, text alternatives, exact labels, narrow-screen layout, and reduced-motion behavior remain available.
- The existing emergency-department data checks continue to pass.

## Deliberate limit

The atlas covers the ten families in the course, not every named chart variant. Each family lists common variants so learners can see where histograms, Sankey diagrams, forest plots, treemaps, maps, heatmaps, and related forms belong.
