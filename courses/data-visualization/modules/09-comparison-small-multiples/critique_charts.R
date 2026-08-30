args <- commandArgs(trailingOnly = TRUE)

option_value <- function(flag, default) {
  match <- which(args == flag)
  if (length(match) == 0) return(default)
  if (match[1] == length(args)) stop(flag, " requires a value")
  args[match[1] + 1]
}

if (!requireNamespace("ggplot2", quietly = TRUE)) stop("Install ggplot2 before running this critique set.")

script_arg <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
script_dir <- if (length(script_arg)) dirname(normalizePath(sub("^--file=", "", script_arg[1]))) else getwd()
nc_path <- option_value("--data", file.path(script_dir, "data", "nc_county_health_profiles_2024.csv"))
all_path <- option_value("--all-data", file.path(script_dir, "data", "places_county_comparison_2024.csv"))
output_dir <- option_value("--output", file.path(script_dir, "critique-output"))

if (!file.exists(nc_path) || !file.exists(all_path)) stop("Both released data files are required.")
nc <- read.csv(nc_path, stringsAsFactors = FALSE)
all_data <- read.csv(all_path, stringsAsFactors = FALSE)
if (nrow(nc) != 500 || nrow(all_data) != 31450) stop("Released comparison data do not match the expected row counts.")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

measure_order <- c("CSMOKING", "DIABETES", "GHLTH", "LPA", "OBESITY")
label_order <- nc$measure_label[match(measure_order, nc$measure_id)]
nc$measure_label <- factor(nc$measure_label, levels = label_order)
shortlist_names <- unique(nc[nc$profile_order <= 12, c("county_name", "profile_order")])
shortlist_names <- shortlist_names[order(shortlist_names$profile_order), "county_name"]
shortlist <- nc[nc$profile_order <= 12, ]
shortlist$county_name <- factor(shortlist$county_name, levels = rev(shortlist_names))

free_scales <- ggplot2::ggplot(
  shortlist,
  ggplot2::aes(x = age_adjusted_prevalence_pct, y = county_name)
) +
  ggplot2::geom_point(color = "#2166AC", size = 2) +
  ggplot2::facet_grid(. ~ measure_label, scales = "free_x") +
  ggplot2::labs(
    title = "FLAWED: every panel stretches its range to look equally variable",
    subtitle = "Free x scales erase absolute prevalence differences across measures",
    x = "Age-adjusted prevalence (%)",
    y = NULL
  ) +
  ggplot2::theme_minimal(base_size = 11) +
  ggplot2::theme(panel.grid.minor = ggplot2::element_blank(), strip.text = ggplot2::element_text(face = "bold"))

peer_states <- c("GA", "NC", "SC", "TN", "VA")
diabetes <- all_data[
  all_data$measureid == "DIABETES" &
    all_data$datavaluetypeid == "AgeAdjPrv" &
    all_data$stateabbr %in% peer_states,
]
diabetes$data_value <- as.numeric(diabetes$data_value)
state_medians <- aggregate(data_value ~ stateabbr, data = diabetes, FUN = median)
names(state_medians)[2] <- "state_median"
diabetes <- merge(diabetes, state_medians, by = "stateabbr")
diabetes$local_class <- ifelse(diabetes$data_value > diabetes$state_median, "Above panel median", "At or below panel median")

changing_baseline <- ggplot2::ggplot(
  diabetes,
  ggplot2::aes(x = data_value, y = reorder(locationname, data_value))
) +
  ggplot2::geom_vline(
    data = state_medians,
    ggplot2::aes(xintercept = state_median),
    color = "#B2182B",
    linetype = "dashed"
  ) +
  ggplot2::geom_point(ggplot2::aes(color = local_class), size = 1.25) +
  ggplot2::facet_grid(stateabbr ~ ., scales = "free_y", space = "free_y") +
  ggplot2::scale_color_manual(values = c("Above panel median" = "#B2182B", "At or below panel median" = "#2166AC")) +
  ggplot2::labs(
    title = "FLAWED: each state changes what the red label means",
    subtitle = "The same diabetes value can switch class because every panel uses its own median",
    x = "Age-adjusted diagnosed diabetes prevalence (%)",
    y = NULL,
    color = NULL
  ) +
  ggplot2::theme_minimal(base_size = 10) +
  ggplot2::theme(axis.text.y = ggplot2::element_blank(), panel.grid.minor = ggplot2::element_blank(), legend.position = "top")

rainbow <- nc[nc$profile_order <= 30, ]
rainbow$measure_label <- factor(rainbow$measure_label, levels = label_order)
overloaded <- ggplot2::ggplot(
  rainbow,
  ggplot2::aes(x = measure_label, y = age_adjusted_prevalence_pct, group = county_name, color = county_name)
) +
  ggplot2::geom_line(linewidth = 0.7) +
  ggplot2::geom_point(size = 1.3) +
  ggplot2::labs(
    title = "FLAWED: thirty rainbow lines connect five different constructs",
    subtitle = "County identity is color-only, labels are absent, and crossings dominate the comparison",
    x = NULL,
    y = "Age-adjusted prevalence (%)",
    color = "County"
  ) +
  ggplot2::theme_minimal(base_size = 10) +
  ggplot2::theme(axis.text.x = ggplot2::element_text(angle = 25, hjust = 1), legend.position = "none")

ggplot2::ggsave(file.path(output_dir, "C1-free-panel-scales.png"), free_scales, width = 15, height = 7, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "C2-changing-panel-baselines.png"), changing_baseline, width = 10, height = 12, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "C3-overloaded-rainbow-profiles.png"), overloaded, width = 11, height = 7, dpi = 150, bg = "white")

cat("Created three deliberately flawed comparison figures in:", normalizePath(output_dir, winslash = "/"), "\n")
