source("courses/data-visualization/checkpoints/02-applied-visualization-portfolio/render_portfolio_artifact.R")
render_portfolio_artifact(commandArgs(trailingOnly = TRUE)[1], "10-maps-geography-place", "03-bivariate-screen-map.png", "place_decision_table.csv", "place-display")
