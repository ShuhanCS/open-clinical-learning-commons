args <- commandArgs(trailingOnly = TRUE)
data_path <- if (length(args) >= 1) args[[1]] else file.path("data", "nc_diabetes_rates_2024.csv")
boundary_path <- if (length(args) >= 2) args[[2]] else file.path("data", "nc_county_boundaries_2024.csv")
output_dir <- if (length(args) >= 3) args[[3]] else file.path("outputs", "critique")

if (!requireNamespace("ggplot2", quietly = TRUE)) {
  stop("Package 'ggplot2' is required. Install it with: install.packages('ggplot2')", call. = FALSE)
}
if (!file.exists(data_path) || !file.exists(boundary_path)) {
  stop("The teaching table and county boundary file are required.", call. = FALSE)
}

data <- utils::read.csv(data_path, stringsAsFactors = FALSE, colClasses = c(county_fips = "character"))
boundaries <- utils::read.csv(boundary_path, stringsAsFactors = FALSE, colClasses = c(county_fips = "character"))
if (nrow(data) != 100 || length(unique(boundaries$county_fips)) != 100) {
  stop("Expected 100 North Carolina counties in both inputs.", call. = FALSE)
}

match_index <- match(boundaries$county_fips, data$county_fips)
if (anyNA(match_index)) {
  stop("Boundary and teaching FIPS values do not match.", call. = FALSE)
}
boundaries$modeled_adult_count <- data$modeled_adult_count[match_index]

dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

theme_module <- ggplot2::theme_minimal(base_size = 14) +
  ggplot2::theme(
    plot.title.position = "plot",
    plot.title = ggplot2::element_text(face = "bold", size = 17),
    panel.grid = ggplot2::element_blank(),
    axis.text = ggplot2::element_blank(),
    axis.title = ggplot2::element_blank(),
    legend.position = "right"
  )

plot_count_map <- ggplot2::ggplot(
  boundaries,
  ggplot2::aes(x = longitude, y = latitude, group = polygon_group, fill = modeled_adult_count)
) +
  ggplot2::geom_polygon(color = "white", linewidth = 0.15) +
  ggplot2::coord_quickmap() +
  ggplot2::scale_fill_gradient(low = "#deebf7", high = "#08519c", name = "Adults") +
  ggplot2::labs(title = "Adults with diabetes by county") +
  theme_module

top <- data[order(-data$age_adjusted_prevalence_pct, data$county_fips), , drop = FALSE][1:12, ]
top <- top[order(top$age_adjusted_prevalence_pct), , drop = FALSE]
top$county_label <- factor(top$county_name, levels = top$county_name)
plot_rate <- ggplot2::ggplot(top, ggplot2::aes(x = age_adjusted_prevalence_pct, y = county_label)) +
  ggplot2::geom_col(fill = "#2b50b8", width = 0.72) +
  ggplot2::scale_x_continuous(limits = c(0, 17)) +
  ggplot2::labs(
    title = "County diabetes rates",
    x = "Percent",
    y = NULL
  ) +
  ggplot2::theme_minimal(base_size = 14) +
  ggplot2::theme(
    plot.title.position = "plot",
    plot.title = ggplot2::element_text(face = "bold", size = 17),
    panel.grid.minor = ggplot2::element_blank()
  )

ggplot2::ggsave(file.path(output_dir, "C1-raw-count-choropleth.png"), plot_count_map, width = 12.8, height = 8, dpi = 125, bg = "white")
ggplot2::ggsave(file.path(output_dir, "C2-rate-without-denominator.png"), plot_rate, width = 12.8, height = 8, dpi = 125, bg = "white")

cat("Created the Module 05 critique charts in:", normalizePath(output_dir, winslash = "/", mustWork = TRUE), "\n")
cat("C1 hides that the fill is a modeled count driven by adult population.\n")
cat("C2 hides the adult denominator, adjustment status, source interval, period, and modeled nature of the estimate.\n")
