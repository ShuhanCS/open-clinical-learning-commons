args <- commandArgs(trailingOnly = TRUE)

option_value <- function(flag, default) {
  match <- which(args == flag)
  if (length(match) == 0) return(default)
  if (match[1] == length(args)) stop(flag, " requires a value")
  args[match[1] + 1]
}

if (!requireNamespace("ggplot2", quietly = TRUE)) stop("Install ggplot2 before running this lab.")

script_arg <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
script_dir <- if (length(script_arg)) dirname(normalizePath(sub("^--file=", "", script_arg[1]))) else getwd()
data_path <- option_value("--data", file.path(script_dir, "data", "nc_place_access_2026.csv"))
boundary_path <- option_value("--boundaries", file.path(script_dir, "data", "nc_county_boundaries_2024.csv"))
output_dir <- option_value("--output", file.path(script_dir, "output"))

if (!file.exists(data_path) || !file.exists(boundary_path)) stop("The teaching table and boundary file are required.")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

data <- read.csv(data_path, stringsAsFactors = FALSE, colClasses = c(county_fips = "character"), check.names = FALSE)
boundaries <- read.csv(boundary_path, stringsAsFactors = FALSE, colClasses = c(county_fips = "character"), check.names = FALSE)
required <- c(
  "county_fips", "county_name", "adult_population", "age_adjusted_fair_poor_health_pct",
  "age_adjusted_low_ci_pct", "age_adjusted_high_ci_pct", "national_age_adjusted_pct",
  "max_active_hpsa_score", "higher_hpsa_score_screen", "bivariate_screen_class",
  "reference_review_eligible", "reference_review_order", "reference_shortlist"
)
missing <- setdiff(required, names(data))
if (length(missing)) stop("Missing teaching fields: ", paste(missing, collapse = ", "))
if (nrow(data) != 100 || nrow(boundaries) != 7121 || length(unique(boundaries$county_fips)) != 100) {
  stop("Expected 100 teaching counties and 7,121 boundary points.")
}

map_index <- match(boundaries$county_fips, data$county_fips)
if (any(is.na(map_index))) stop("Every boundary county must match the teaching table.")
map_data <- cbind(boundaries, data[map_index, setdiff(names(data), c("county_fips", "county_name")), drop = FALSE])

albers_equal_area <- function(longitude, latitude) {
  radians <- pi / 180
  phi1 <- 29.5 * radians
  phi2 <- 45.5 * radians
  phi0 <- 23 * radians
  lambda0 <- -96 * radians
  phi <- latitude * radians
  theta <- 0.5 * (sin(phi1) + sin(phi2)) * (longitude * radians - lambda0)
  n <- 0.5 * (sin(phi1) + sin(phi2))
  c_value <- cos(phi1)^2 + 2 * n * sin(phi1)
  rho <- sqrt(c_value - 2 * n * sin(phi)) / n
  rho0 <- sqrt(c_value - 2 * n * sin(phi0)) / n
  data.frame(projected_x = rho * sin(theta), projected_y = rho0 - rho * cos(theta))
}
map_data <- cbind(map_data, albers_equal_area(map_data$longitude, map_data$latitude))

class_order <- c(
  "Neither screen condition",
  "Higher health estimate only",
  "Higher HPSA score only",
  "Higher health estimate + higher HPSA score"
)
class_colors <- c(
  "Neither screen condition" = "#d9dde3",
  "Higher health estimate only" = "#3573a8",
  "Higher HPSA score only" = "#d8a328",
  "Higher health estimate + higher HPSA score" = "#713e91"
)
map_data$bivariate_screen_class <- factor(map_data$bivariate_screen_class, levels = class_order)

health_map <- ggplot2::ggplot(
  map_data,
  ggplot2::aes(x = projected_x, y = projected_y, group = polygon_group, fill = age_adjusted_fair_poor_health_pct)
) +
  ggplot2::geom_polygon(color = "white", linewidth = 0.18) +
  ggplot2::coord_equal() +
  ggplot2::scale_fill_gradient(
    low = "#f7fbff",
    high = "#084594",
    limits = c(12, 28),
    breaks = c(12, 16, 20, 24, 28),
    name = "Age-adjusted\npercent"
  ) +
  ggplot2::labs(
    title = "Fair or poor self-rated health varies across North Carolina",
    subtitle = "Model-based age-adjusted percentage among adults, PLACES measure year 2022",
    caption = "The map shows spatial context, not a causal pattern. Generalized 2024 Census boundaries in an Albers equal-area projection."
  ) +
  ggplot2::theme_void(base_size = 12) +
  ggplot2::theme(
    plot.title = ggplot2::element_text(face = "bold"),
    plot.caption = ggplot2::element_text(hjust = 0),
    legend.position = "right"
  )

ggplot2::ggsave(
  file.path(output_dir, "01-health-choropleth.png"),
  health_map,
  width = 11,
  height = 7.2,
  dpi = 180,
  bg = "white"
)

ordered <- data[order(data$health_rank_descending), ]
ordered$county_order <- factor(ordered$county_name, levels = rev(ordered$county_name))
ordered$score_screen <- ifelse(
  ordered$higher_hpsa_score_screen == "yes",
  "Highest active component HPSA score 20 or higher",
  "Score below 20 or no active designation"
)

comparison <- ggplot2::ggplot(
  ordered,
  ggplot2::aes(x = age_adjusted_fair_poor_health_pct, y = county_order)
) +
  ggplot2::geom_vline(
    xintercept = unique(ordered$national_age_adjusted_pct),
    color = "#525252",
    linetype = "dashed",
    linewidth = 0.55
  ) +
  ggplot2::geom_errorbar(
    ggplot2::aes(xmin = age_adjusted_low_ci_pct, xmax = age_adjusted_high_ci_pct),
    orientation = "y",
    width = 0,
    color = "#a4a9b0",
    linewidth = 0.45
  ) +
  ggplot2::geom_point(
    ggplot2::aes(shape = score_screen, fill = score_screen),
    color = "#172033",
    size = 2.8,
    stroke = 0.7
  ) +
  ggplot2::scale_shape_manual(values = c(
    "Highest active component HPSA score 20 or higher" = 24,
    "Score below 20 or no active designation" = 21
  )) +
  ggplot2::scale_fill_manual(values = c(
    "Highest active component HPSA score 20 or higher" = "#d8a328",
    "Score below 20 or no active designation" = "white"
  )) +
  ggplot2::scale_x_continuous(limits = c(10, 30), breaks = seq(10, 30, 5)) +
  ggplot2::labs(
    title = "The non-map view preserves order, intervals, and exact comparison",
    subtitle = "Dashed line: national age-adjusted point estimate, 17.0%. Shape and fill repeat the declared HPSA screen.",
    x = "Adults reporting fair or poor health, age-adjusted percent",
    y = NULL,
    shape = NULL,
    fill = NULL,
    caption = "HPSA score is the highest active component score touching the county, not a county workforce rate."
  ) +
  ggplot2::theme_minimal(base_size = 11) +
  ggplot2::theme(
    panel.grid.major.y = ggplot2::element_blank(),
    panel.grid.minor = ggplot2::element_blank(),
    legend.position = "top",
    plot.title = ggplot2::element_text(face = "bold"),
    plot.caption = ggplot2::element_text(hjust = 0)
  )

ggplot2::ggsave(
  file.path(output_dir, "02-health-ordered-comparison.png"),
  comparison,
  width = 12,
  height = 24,
  dpi = 150,
  bg = "white",
  limitsize = FALSE
)

bivariate_map <- ggplot2::ggplot(
  map_data,
  ggplot2::aes(x = projected_x, y = projected_y, group = polygon_group, fill = bivariate_screen_class)
) +
  ggplot2::geom_polygon(color = "white", linewidth = 0.18) +
  ggplot2::coord_equal() +
  ggplot2::scale_fill_manual(values = class_colors, drop = FALSE) +
  ggplot2::labs(
    title = "A four-class screen makes both comparison rules visible",
    subtitle = "Health point estimate above 17.0% and highest active component HPSA score of 20 or higher",
    fill = "Teaching screen",
    caption = "19 counties meet both conditions. Score 20 is a declared teaching rule, not an official funding threshold."
  ) +
  ggplot2::theme_void(base_size = 12) +
  ggplot2::theme(
    plot.title = ggplot2::element_text(face = "bold"),
    plot.caption = ggplot2::element_text(hjust = 0),
    legend.position = "right"
  )

ggplot2::ggsave(
  file.path(output_dir, "03-bivariate-screen-map.png"),
  bivariate_map,
  width = 12,
  height = 7.2,
  dpi = 180,
  bg = "white"
)

review <- data[data$reference_review_eligible == "yes", ]
review <- review[order(as.integer(review$reference_review_order)), ]
review$county_order <- factor(review$county_name, levels = rev(review$county_name))
review$shortlist_label <- ifelse(review$reference_shortlist == "yes", "Reference twelve", "Other eligible county")
review$detail <- sprintf(
  "HPSA %s | adults %s",
  review$max_active_hpsa_score,
  format(review$adult_population, big.mark = ",", scientific = FALSE)
)

review_plot <- ggplot2::ggplot(
  review,
  ggplot2::aes(x = age_adjusted_fair_poor_health_pct, y = county_order)
) +
  ggplot2::geom_errorbar(
    ggplot2::aes(xmin = age_adjusted_low_ci_pct, xmax = age_adjusted_high_ci_pct),
    orientation = "y",
    width = 0,
    color = "#a4a9b0",
    linewidth = 0.55
  ) +
  ggplot2::geom_point(
    ggplot2::aes(shape = shortlist_label, fill = shortlist_label),
    color = "#172033",
    size = 3.4,
    stroke = 0.75
  ) +
  ggplot2::geom_text(
    ggplot2::aes(label = detail),
    hjust = 0,
    nudge_x = 0.35,
    size = 3.1,
    color = "#303846"
  ) +
  ggplot2::scale_shape_manual(values = c("Reference twelve" = 24, "Other eligible county" = 21)) +
  ggplot2::scale_fill_manual(values = c("Reference twelve" = "#713e91", "Other eligible county" = "white")) +
  ggplot2::scale_x_continuous(limits = c(10, 35), breaks = seq(10, 30, 5)) +
  ggplot2::labs(
    title = "Nineteen counties meet the screen; twelve enter the reference discussion list",
    subtitle = "Order: health estimate descending, HPSA score descending, county name. Intervals remain visible.",
    x = "Adults reporting fair or poor health, age-adjusted percent",
    y = NULL,
    shape = NULL,
    fill = NULL,
    caption = "The list starts a readiness conversation. It does not allocate funds or label county residents."
  ) +
  ggplot2::theme_minimal(base_size = 11) +
  ggplot2::theme(
    panel.grid.major.y = ggplot2::element_blank(),
    panel.grid.minor = ggplot2::element_blank(),
    legend.position = "top",
    plot.title = ggplot2::element_text(face = "bold"),
    plot.caption = ggplot2::element_text(hjust = 0)
  )

ggplot2::ggsave(
  file.path(output_dir, "04-reference-review-list.png"),
  review_plot,
  width = 12,
  height = 10,
  dpi = 180,
  bg = "white"
)

decision_fields <- c(
  "county_fips", "county_name", "health_measure_year", "adult_population",
  "age_adjusted_fair_poor_health_pct", "age_adjusted_low_ci_pct", "age_adjusted_high_ci_pct",
  "national_age_adjusted_pct", "health_rank_descending", "active_hpsa_designations",
  "max_active_hpsa_score", "whole_county_geographic_hpsa", "bivariate_screen_class",
  "reference_review_eligible", "reference_review_order", "reference_shortlist",
  "time_alignment_status", "interpretation_boundary"
)
write.csv(data[decision_fields], file.path(output_dir, "place_decision_table.csv"), row.names = FALSE, na = "")

shortlist_names <- review$county_name[review$reference_shortlist == "yes"]
alt_text <- c(
  "# Module 10 reference text alternative",
  "",
  "## Short alternative",
  "",
  "North Carolina county map and ordered comparison of modeled fair or poor adult health, paired with a declared primary-care HPSA score screen and an exact table.",
  "",
  "## Long description",
  "",
  "The first map shades 100 counties by model-based age-adjusted fair or poor self-rated health for PLACES measure year 2022. Values range from 12.1% to 27.2%; the national point estimate is 17.0%.",
  "",
  "The ordered non-map view gives every county the same horizontal scale, shows the source interval, and marks whether the highest active primary-care HPSA component score touching the county is at least 20. Seventy-three counties are above the national health point estimate, 23 meet the HPSA score screen, and 19 meet both conditions.",
  "",
  paste0("The reference twelve, in declared review order, are: ", paste(shortlist_names, collapse = ", "), "."),
  "",
  "The map supports regional and neighboring-county discussion. The ordered comparison supports rank, interval, and exact-value review. The two should be used together when both spatial coordination and comparative evidence matter.",
  "",
  "PLACES values are model-based small-area estimates. The HPSA value is the highest active component score touching each county, not a county workforce rate. The health measure is from 2022 and the HPSA snapshot is from 2026-08-29. The screen is not a validated allocation rule.",
  "",
  "Exact values for all 100 counties are in place_decision_table.csv."
)
writeLines(alt_text, file.path(output_dir, "alt-text-reference.md"), useBytes = TRUE)

message("Created four figures, one decision table, and one text alternative in: ", normalizePath(output_dir))
