source("courses/data-visualization/checkpoints/02-applied-visualization-portfolio/render_portfolio_artifact.R")
render_portfolio_artifact(commandArgs(trailingOnly = TRUE)[1], "09-comparison-small-multiples", "01-all-counties-ordered-small-multiples.png", "comparison_decision_table.csv", "comparison-display")
