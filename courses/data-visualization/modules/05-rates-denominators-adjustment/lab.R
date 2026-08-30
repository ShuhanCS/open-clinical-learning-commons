args <- commandArgs(trailingOnly = TRUE)
input_path <- if (length(args) >= 1) args[[1]] else file.path("data", "nc_diabetes_rates_2024.csv")
output_dir <- if (length(args) >= 2) args[[2]] else file.path("outputs", "lab")

if (!requireNamespace("ggplot2", quietly = TRUE)) {
  stop("Package 'ggplot2' is required. Install it with: install.packages('ggplot2')", call. = FALSE)
}
if (!file.exists(input_path)) {
  stop(sprintf("Data file not found: %s", input_path), call. = FALSE)
}

data <- utils::read.csv(input_path, stringsAsFactors = FALSE, colClasses = c(county_fips = "character"))
required <- c(
  "county_fips", "county_name", "places_adult_population", "crude_prevalence_pct",
  "crude_low_95_pct", "crude_high_95_pct", "age_adjusted_prevalence_pct",
  "age_adjusted_low_95_pct", "age_adjusted_high_95_pct", "modeled_adult_count",
  "teaching_low_denominator_flag"
)
missing <- setdiff(required, names(data))
if (length(missing) > 0) {
  stop(sprintf("Input is missing required columns: %s", paste(missing, collapse = ", ")), call. = FALSE)
}
if (nrow(data) != 100 || anyNA(data[required])) {
  stop("Input must contain 100 complete North Carolina county rows.", call. = FALSE)
}

rank_desc <- function(values, fips) {
  order_index <- order(-values, fips)
  result <- integer(length(values))
  result[order_index] <- seq_along(values)
  result
}

data$count_rank <- rank_desc(data$modeled_adult_count, data$county_fips)
data$crude_rank <- rank_desc(data$crude_prevalence_pct, data$county_fips)
data$adjusted_rank <- rank_desc(data$age_adjusted_prevalence_pct, data$county_fips)
data$count_adjusted_rank_change <- data$count_rank - data$adjusted_rank
data$crude_adjusted_rank_change <- data$crude_rank - data$adjusted_rank

comparison_fips <- union(
  data$county_fips[data$count_rank <= 12],
  data$county_fips[data$adjusted_rank <= 12]
)
comparison <- data[data$county_fips %in% comparison_fips, , drop = FALSE]
decision <- data[data$adjusted_rank <= 12, , drop = FALSE]
decision <- decision[order(decision$adjusted_rank), , drop = FALSE]

dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

theme_module <- ggplot2::theme_minimal(base_size = 14) +
  ggplot2::theme(
    plot.title.position = "plot",
    plot.title = ggplot2::element_text(face = "bold", size = 17),
    plot.subtitle = ggplot2::element_text(size = 12, margin = ggplot2::margin(b = 9)),
    panel.grid.minor = ggplot2::element_blank(),
    axis.title.y = ggplot2::element_blank(),
    legend.position = "bottom"
  )

count_view <- comparison[order(comparison$modeled_adult_count), , drop = FALSE]
count_view$county_label <- factor(count_view$county_name, levels = count_view$county_name)
plot_count <- ggplot2::ggplot(count_view, ggplot2::aes(x = modeled_adult_count, y = county_label)) +
  ggplot2::geom_col(fill = "#2b50b8", width = 0.72) +
  ggplot2::geom_text(
    ggplot2::aes(label = format(modeled_adult_count, big.mark = ",", scientific = FALSE)),
    hjust = -0.08,
    size = 3.4
  ) +
  ggplot2::scale_x_continuous(expand = ggplot2::expansion(mult = c(0, 0.18))) +
  ggplot2::labs(
    title = "Modeled adult count prioritizes population scale",
    subtitle = "Derived from crude PLACES prevalence and the matching adult population; these are not observed cases.",
    x = "Modeled adults with diagnosed diabetes"
  ) +
  theme_module

crude_view <- comparison[order(comparison$crude_prevalence_pct), , drop = FALSE]
crude_view$county_label <- factor(crude_view$county_name, levels = crude_view$county_name)
plot_crude <- ggplot2::ggplot(crude_view, ggplot2::aes(x = crude_prevalence_pct, y = county_label)) +
  ggplot2::geom_segment(
    ggplot2::aes(x = 0, xend = crude_prevalence_pct, yend = county_label),
    color = "#b8c2d8",
    linewidth = 0.8
  ) +
  ggplot2::geom_point(color = "#0f766e", size = 3.1) +
  ggplot2::geom_text(
    ggplot2::aes(label = sprintf("%.1f%%", crude_prevalence_pct)),
    hjust = -0.35,
    size = 3.3
  ) +
  ggplot2::scale_x_continuous(limits = c(0, max(crude_view$crude_prevalence_pct) + 3)) +
  ggplot2::labs(
    title = "Crude prevalence changes the county order",
    subtitle = "The denominator is the modeled county adult population age 18 and older.",
    x = "Modeled crude prevalence (percent)"
  ) +
  theme_module

adjusted_view <- comparison[order(comparison$age_adjusted_prevalence_pct), , drop = FALSE]
adjusted_view$county_label <- factor(adjusted_view$county_name, levels = adjusted_view$county_name)
adjusted_view$context <- sprintf(
  "adults %s | modeled count %s%s",
  format(adjusted_view$places_adult_population, big.mark = ",", scientific = FALSE),
  format(adjusted_view$modeled_adult_count, big.mark = ",", scientific = FALSE),
  ifelse(adjusted_view$teaching_low_denominator_flag == 1, " | LOW DENOMINATOR", "")
)
plot_adjusted <- ggplot2::ggplot(
  adjusted_view,
  ggplot2::aes(x = age_adjusted_prevalence_pct, y = county_label)
) +
  ggplot2::geom_errorbar(
    ggplot2::aes(xmin = age_adjusted_low_95_pct, xmax = age_adjusted_high_95_pct),
    orientation = "y",
    width = 0,
    color = "#64748b",
    linewidth = 0.7
  ) +
  ggplot2::geom_point(
    ggplot2::aes(shape = factor(teaching_low_denominator_flag)),
    color = "#b45309",
    fill = "white",
    size = 3.2,
    stroke = 1.1
  ) +
  ggplot2::geom_text(
    ggplot2::aes(label = context),
    hjust = -0.04,
    size = 3.0
  ) +
  ggplot2::scale_shape_manual(
    values = c("0" = 16, "1" = 17),
    labels = c("0" = "Adult population at least 10,000", "1" = "Training low-denominator warning"),
    name = NULL
  ) +
  ggplot2::scale_x_continuous(
    limits = c(min(adjusted_view$age_adjusted_low_95_pct) - 0.5, max(adjusted_view$age_adjusted_high_95_pct) + 12)
  ) +
  ggplot2::labs(
    title = "Age adjustment supports comparison; population still travels with the result",
    subtitle = "Diagnosed diabetes among adults, 2022 measure data, PLACES 2024 release. Lines are source 95% intervals.",
    x = "Modeled age-adjusted prevalence (percent)"
  ) +
  theme_module

shift_view <- data[order(-abs(data$count_adjusted_rank_change), data$county_fips), , drop = FALSE][1:16, ]
shift_view <- shift_view[order(shift_view$adjusted_rank, decreasing = TRUE), , drop = FALSE]
shift_view$county_label <- factor(shift_view$county_name, levels = shift_view$county_name)
plot_shift <- ggplot2::ggplot(shift_view, ggplot2::aes(y = county_label)) +
  ggplot2::geom_segment(
    ggplot2::aes(x = count_rank, xend = adjusted_rank, yend = county_label),
    color = "#94a3b8",
    linewidth = 1
  ) +
  ggplot2::geom_point(ggplot2::aes(x = count_rank, shape = "Modeled count rank"), color = "#2b50b8", size = 3.2) +
  ggplot2::geom_point(ggplot2::aes(x = adjusted_rank, shape = "Age-adjusted rank"), color = "#b45309", size = 3.2) +
  ggplot2::scale_shape_manual(values = c("Modeled count rank" = 15, "Age-adjusted rank" = 16), name = NULL) +
  ggplot2::scale_x_reverse(breaks = c(100, 80, 60, 40, 20, 1)) +
  ggplot2::labs(
    title = "Changing the quantity can reverse apparent priority",
    subtitle = "Sixteen largest rank shifts among 100 North Carolina counties. Rank 1 is highest.",
    x = "County rank"
  ) +
  theme_module

ggplot2::ggsave(file.path(output_dir, "01-modeled-count.png"), plot_count, width = 12.8, height = 8, dpi = 125, bg = "white")
ggplot2::ggsave(file.path(output_dir, "02-crude-prevalence.png"), plot_crude, width = 12.8, height = 8, dpi = 125, bg = "white")
ggplot2::ggsave(file.path(output_dir, "03-adjusted-with-denominator.png"), plot_adjusted, width = 12.8, height = 8, dpi = 125, bg = "white")
ggplot2::ggsave(file.path(output_dir, "04-rank-change.png"), plot_shift, width = 12.8, height = 8, dpi = 125, bg = "white")

decision_output <- decision[c(
  "county_fips", "county_name", "adjusted_rank", "age_adjusted_prevalence_pct",
  "age_adjusted_low_95_pct", "age_adjusted_high_95_pct", "crude_rank",
  "crude_prevalence_pct", "count_rank", "modeled_adult_count", "places_adult_population",
  "teaching_low_denominator_flag"
)]
utils::write.csv(decision_output, file.path(output_dir, "county_decision_table.csv"), row.names = FALSE, na = "")

cat("Created the Module 05 lab outputs in:", normalizePath(output_dir, winslash = "/", mustWork = TRUE), "\n")
print(decision_output, row.names = FALSE)
cat("\nDiscuss:\n")
cat("1. Why do the modeled-count and age-adjusted top-12 lists have no counties in common?\n")
cat("2. Which quantity answers comparative prevalence and which answers outreach scale?\n")
cat("3. Which rank changes are related to population size, and which may be related to age structure?\n")
cat("4. Why can the source intervals not be reduced to a yes-or-no significance rule in this module?\n")
cat("5. Which local evidence could change the first-pass shortlist?\n")
