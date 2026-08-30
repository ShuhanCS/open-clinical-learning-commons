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
data_path <- option_value("--data", file.path(script_dir, "data", "nc_county_health_profiles_2024.csv"))
output_dir <- option_value("--output", file.path(script_dir, "output"))

if (!file.exists(data_path)) stop("Data file not found: ", data_path)
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

data <- read.csv(data_path, stringsAsFactors = FALSE, check.names = FALSE)
required <- c(
  "county_fips", "county_name", "measure_id", "measure_label", "measure_year",
  "adult_population", "crude_prevalence_pct", "age_adjusted_prevalence_pct",
  "age_adjusted_low_ci_pct", "age_adjusted_high_ci_pct", "national_age_adjusted_pct",
  "difference_from_national_pct_points", "point_estimate_above_national",
  "measures_above_national", "profile_order"
)
missing <- setdiff(required, names(data))
if (length(missing)) stop("Missing required columns: ", paste(missing, collapse = ", "))
if (nrow(data) != 500 || length(unique(data$county_fips)) != 100 || length(unique(data$measure_id)) != 5) {
  stop("Expected 500 rows, 100 counties, and five measures.")
}
if (any(table(data$county_fips) != 5) || any(table(data$measure_id) != 100)) {
  stop("Every county must have five measures and every measure must have 100 counties.")
}

measure_order <- c("CSMOKING", "DIABETES", "GHLTH", "LPA", "OBESITY")
label_order <- data$measure_label[match(measure_order, data$measure_id)]
data$measure_label <- factor(data$measure_label, levels = label_order)
profile_names <- unique(data[order(data$profile_order), c("county_name", "profile_order")])$county_name
data$county_profile <- factor(data$county_name, levels = rev(profile_names))
data$shortlist <- data$profile_order <= 12
data$shortlist_label <- ifelse(data$shortlist, "Profile shortlist", "Other county")
data$direction_shape <- ifelse(data$point_estimate_above_national == "yes", "Above national point estimate", "At or below national point estimate")
data$gap_low_pct_points <- data$age_adjusted_low_ci_pct - data$national_age_adjusted_pct
data$gap_high_pct_points <- data$age_adjusted_high_ci_pct - data$national_age_adjusted_pct
data$interval_width_pct_points <- data$age_adjusted_high_ci_pct - data$age_adjusted_low_ci_pct

shortlist <- data[data$shortlist, ]
shortlist_names <- unique(shortlist[order(shortlist$profile_order), c("county_name", "profile_order")])$county_name
shortlist$county_shortlist <- factor(shortlist$county_name, levels = rev(shortlist_names))

theme_compare <- ggplot2::theme_minimal(base_size = 11) +
  ggplot2::theme(
    panel.grid.minor = ggplot2::element_blank(),
    plot.title.position = "plot",
    plot.caption.position = "plot",
    strip.text = ggplot2::element_text(face = "bold")
  )

reference <- unique(data[c("measure_label", "national_age_adjusted_pct")])
reference$measure_label <- factor(reference$measure_label, levels = label_order)

all_counties <- ggplot2::ggplot(
  data,
  ggplot2::aes(x = age_adjusted_prevalence_pct, y = county_profile)
) +
  ggplot2::geom_vline(
    data = reference,
    ggplot2::aes(xintercept = national_age_adjusted_pct),
    color = "#4D4D4D",
    linetype = "dashed",
    linewidth = 0.65
  ) +
  ggplot2::geom_errorbar(
    ggplot2::aes(xmin = age_adjusted_low_ci_pct, xmax = age_adjusted_high_ci_pct),
    width = 0,
    orientation = "y",
    color = "#777777",
    linewidth = 0.3
  ) +
  ggplot2::geom_point(
    ggplot2::aes(shape = shortlist_label, color = shortlist_label),
    size = 1.8
  ) +
  ggplot2::facet_grid(. ~ measure_label, scales = "fixed") +
  ggplot2::scale_x_continuous(limits = c(0, 46), breaks = c(0, 10, 20, 30, 40)) +
  ggplot2::scale_y_discrete(labels = function(values) ifelse(values %in% shortlist_names, values, "")) +
  ggplot2::scale_shape_manual(values = c("Profile shortlist" = 17, "Other county" = 16)) +
  ggplot2::scale_color_manual(values = c("Profile shortlist" = "#B2182B", "Other county" = "#2166AC")) +
  ggplot2::labs(
    title = "One county order and one scale make five panels comparable",
    subtitle = "All 100 North Carolina counties; shortlist order is reused in every panel",
    x = "Age-adjusted prevalence (%)",
    y = "Counties; only the 12 profile-shortlist names are printed",
    shape = NULL,
    color = NULL,
    caption = paste(
      "Dashed lines are measure-specific U.S. age-adjusted point estimates.",
      "Intervals are CDC PLACES 95% confidence limits; overlap is not a pairwise test."
    )
  ) +
  theme_compare +
  ggplot2::theme(legend.position = "top", axis.text.y = ggplot2::element_text(size = 7))

gap_profile <- ggplot2::ggplot(
  shortlist,
  ggplot2::aes(x = difference_from_national_pct_points, y = county_shortlist)
) +
  ggplot2::geom_vline(xintercept = 0, color = "#333333", linewidth = 0.7) +
  ggplot2::geom_errorbar(
    ggplot2::aes(xmin = gap_low_pct_points, xmax = gap_high_pct_points),
    width = 0,
    orientation = "y",
    color = "#777777",
    linewidth = 0.45
  ) +
  ggplot2::geom_point(
    ggplot2::aes(shape = direction_shape, color = direction_shape),
    size = 2.2
  ) +
  ggplot2::facet_grid(. ~ measure_label, scales = "fixed") +
  ggplot2::scale_x_continuous(limits = c(-10, 14), breaks = c(-10, -5, 0, 5, 10)) +
  ggplot2::scale_shape_manual(values = c("Above national point estimate" = 17, "At or below national point estimate" = 16)) +
  ggplot2::scale_color_manual(values = c("Above national point estimate" = "#B2182B", "At or below national point estimate" = "#2166AC")) +
  ggplot2::labs(
    title = "A consistent zero means the same thing in every panel",
    subtitle = "Twelve profile-shortlist counties; difference from each measure's U.S. age-adjusted point estimate",
    x = "Percentage-point difference from national estimate",
    y = NULL,
    shape = NULL,
    color = NULL,
    caption = "A county interval crossing zero after subtracting the national point is descriptive. It is not a formal county-versus-national test."
  ) +
  theme_compare +
  ggplot2::theme(legend.position = "top", axis.text.y = ggplot2::element_text(size = 8))

dumbbell <- rbind(
  data.frame(
    county_shortlist = shortlist$county_shortlist,
    measure_label = shortlist$measure_label,
    estimate_type = "Crude",
    prevalence = shortlist$crude_prevalence_pct
  ),
  data.frame(
    county_shortlist = shortlist$county_shortlist,
    measure_label = shortlist$measure_label,
    estimate_type = "Age-adjusted",
    prevalence = shortlist$age_adjusted_prevalence_pct
  )
)
dumbbell$estimate_type <- factor(dumbbell$estimate_type, levels = c("Crude", "Age-adjusted"))

adjustment <- ggplot2::ggplot() +
  ggplot2::geom_segment(
    data = shortlist,
    ggplot2::aes(
      x = crude_prevalence_pct,
      xend = age_adjusted_prevalence_pct,
      y = county_shortlist,
      yend = county_shortlist
    ),
    color = "#777777",
    linewidth = 0.55
  ) +
  ggplot2::geom_point(
    data = dumbbell,
    ggplot2::aes(x = prevalence, y = county_shortlist, shape = estimate_type, color = estimate_type),
    size = 2.1
  ) +
  ggplot2::facet_grid(measure_label ~ ., scales = "fixed") +
  ggplot2::scale_x_continuous(limits = c(0, 46), breaks = seq(0, 40, 10)) +
  ggplot2::scale_shape_manual(values = c("Crude" = 16, "Age-adjusted" = 17)) +
  ggplot2::scale_color_manual(values = c("Crude" = "#4D4D4D", "Age-adjusted" = "#2166AC")) +
  ggplot2::labs(
    title = "Crude and age-adjusted estimates answer different comparison questions",
    subtitle = "Twelve profile-shortlist counties, fixed 0 to 46 percent scale in every panel",
    x = "Prevalence (%)",
    y = NULL,
    shape = NULL,
    color = NULL,
    caption = "The dumbbell direction reflects age adjustment, not improvement, change over time, or statistical significance."
  ) +
  theme_compare +
  ggplot2::theme(legend.position = "top", axis.text.y = ggplot2::element_text(size = 7))

profile_count <- unique(data[c("county_fips", "county_name", "measures_above_national")])
count_distribution <- as.data.frame(table(profile_count$measures_above_national), stringsAsFactors = FALSE)
names(count_distribution) <- c("measures_above_national", "counties")
count_distribution$measures_above_national <- as.integer(count_distribution$measures_above_national)

denominator <- ggplot2::ggplot(
  count_distribution,
  ggplot2::aes(x = measures_above_national, y = counties)
) +
  ggplot2::geom_col(fill = "#2166AC", width = 0.72) +
  ggplot2::geom_text(ggplot2::aes(label = counties), vjust = -0.35, size = 3.8) +
  ggplot2::scale_x_continuous(breaks = 0:5) +
  ggplot2::scale_y_continuous(limits = c(0, 60), expand = ggplot2::expansion(mult = c(0, 0.02))) +
  ggplot2::labs(
    title = "A national reference alone does not create a narrow shortlist",
    subtitle = "54 of 100 North Carolina counties are above the national point estimate on all five selected measures",
    x = "Selected measures above the national age-adjusted point estimate",
    y = "Counties",
    caption = "The count is descriptive and gives every measure equal weight. It is not a validated risk score or funding rule."
  ) +
  theme_compare

ggplot2::ggsave(file.path(output_dir, "01-all-counties-ordered-small-multiples.png"), all_counties, width = 15, height = 10, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "02-shortlist-difference-from-national.png"), gap_profile, width = 15, height = 7.5, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "03-crude-age-adjusted-dumbbells.png"), adjustment, width = 10, height = 13, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "04-profile-count-denominator.png"), denominator, width = 10, height = 6.5, dpi = 150, bg = "white")

decision_fields <- c(
  required,
  "age_adjusted_low_ci_pct", "age_adjusted_high_ci_pct", "national_age_adjusted_low_ci_pct",
  "national_age_adjusted_high_ci_pct", "rank_descending_point_estimate", "counties_compared",
  "largest_gap_measure_id", "largest_gap_pct_points", "interval_width_pct_points",
  "gap_low_pct_points", "gap_high_pct_points", "shortlist"
)
decision_fields <- unique(decision_fields)
utils::write.csv(data[decision_fields], file.path(output_dir, "comparison_decision_table.csv"), row.names = FALSE, na = "")

measure_counts <- aggregate(point_estimate_above_national ~ measure_label, data = data, FUN = function(values) sum(values == "yes"))
count_text <- paste(paste0(measure_counts$measure_label, ": ", measure_counts$point_estimate_above_national, " of 100"), collapse = "; ")
alt_text <- c(
  "# Reference text alternative",
  "",
  "## Short alternative",
  "",
  paste(
    "Five aligned panels compare 100 North Carolina counties on age-adjusted smoking, diabetes, fair or poor health, physical inactivity, and obesity estimates.",
    "The same county order and 0 to 46 percent scale are used in every panel; 54 counties exceed the national point estimate on all five measures."
  ),
  "",
  "## Long description",
  "",
  "Each panel contains one point and 95 percent confidence interval for every county. Dashed vertical lines show the measure-specific U.S. age-adjusted point estimate.",
  "",
  paste("Counties above each national point estimate:", count_text, "."),
  "",
  paste("The 12 profile-shortlist counties, in the order used across panels, are", paste(shortlist_names, collapse = ", "), "."),
  "",
  paste(
    "The shortlist order first counts how many of the five county point estimates exceed their matching national point estimate,",
    "then uses the county's largest percentage-point gap and county name."
  ),
  "",
  paste(
    "The count gives each measure equal weight and does not account for program readiness, population size, cost, patient priorities,",
    "within-county inequity, or formal pairwise uncertainty. It is a teaching order, not a validated risk score or allocation rule."
  ),
  "",
  "See comparison_decision_table.csv for all 500 county-measure rows, exact intervals, adult population, ranks, national references, and profile fields."
)
writeLines(alt_text, file.path(output_dir, "alt-text-reference.md"), useBytes = TRUE)

cat("Created four figures, one decision table, and one text alternative in:", normalizePath(output_dir, winslash = "/"), "\n")
