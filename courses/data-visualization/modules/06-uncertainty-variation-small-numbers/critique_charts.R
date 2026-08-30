args <- commandArgs(trailingOnly = TRUE)

option_value <- function(flag, default) {
  match <- which(args == flag)
  if (length(match) == 0) return(default)
  if (match[1] == length(args)) stop(flag, " requires a value")
  args[match[1] + 1]
}

if (!requireNamespace("ggplot2", quietly = TRUE)) stop("Install ggplot2 before running this critique.")

script_arg <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
script_dir <- if (length(script_arg)) dirname(normalizePath(sub("^--file=", "", script_arg[1]))) else getwd()
data_path <- option_value("--data", file.path(script_dir, "data", "ma_hf_readmission_uncertainty_2026.csv"))
output_dir <- option_value("--output", file.path(script_dir, "critique-output"))

data <- read.csv(data_path, stringsAsFactors = FALSE, colClasses = c(facility_id = "character"), check.names = FALSE)
required <- c("facility_name", "score", "denominator", "estimate_status", "reported_rank_worst_first")
missing <- setdiff(required, names(data))
if (length(missing)) stop("Missing required columns: ", paste(missing, collapse = ", "))
if (nrow(data) != 65) stop("Expected 65 rows; received ", nrow(data))
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

reported <- data[data$estimate_status == "reported", ]
reported$score <- as.numeric(reported$score)
reported$denominator <- as.numeric(reported$denominator)
reported$reported_rank_worst_first <- as.integer(reported$reported_rank_worst_first)

top_ten <- reported[reported$reported_rank_worst_first <= 10, ]
top_ten$facility_name <- factor(top_ten$facility_name, levels = rev(top_ten$facility_name[order(top_ten$score, decreasing = TRUE)]))
league <- ggplot2::ggplot(top_ten, ggplot2::aes(x = score, y = facility_name)) +
  ggplot2::geom_col(fill = "#b42318", width = 0.72) +
  ggplot2::geom_text(ggplot2::aes(label = sprintf("%.1f", score)), hjust = -0.2, size = 3.5) +
  ggplot2::coord_cartesian(xlim = c(0, 31), clip = "off") +
  ggplot2::labs(
    title = "Ten worst Massachusetts hospitals",
    subtitle = "Highest heart failure readmission rates",
    x = "Rate",
    y = NULL,
    caption = "Intentionally flawed: intervals, national comparison, denominator, period, and 55 other rows are hidden."
  ) +
  ggplot2::theme_minimal(base_size = 12) +
  ggplot2::theme(panel.grid = ggplot2::element_blank(), plot.title.position = "plot")

small_set <- reported[reported$denominator < 100 | reported$reported_rank_worst_first %in% c(1, 2, 53), ]
small_set$facility_name <- factor(small_set$facility_name, levels = small_set$facility_name[order(small_set$score)])
hidden_n <- ggplot2::ggplot(small_set, ggplot2::aes(x = score, y = facility_name)) +
  ggplot2::geom_point(size = 5, color = "#1f49b6") +
  ggplot2::labs(
    title = "Hospital readmission performance",
    subtitle = "Every point is presented with equal certainty",
    x = "Rate",
    y = NULL,
    caption = "Intentionally flawed: sample size, interval, source status, and benchmark are omitted."
  ) +
  ggplot2::theme_minimal(base_size = 12) +
  ggplot2::theme(panel.grid.minor = ggplot2::element_blank(), plot.title.position = "plot")

ggplot2::ggsave(file.path(output_dir, "C1-point-only-league-table.png"), league, width = 11, height = 7, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "C2-hidden-small-n.png"), hidden_n, width = 10, height = 6.5, dpi = 150, bg = "white")
cat("Created two intentionally flawed critique charts in:", normalizePath(output_dir, winslash = "/"), "\n")
