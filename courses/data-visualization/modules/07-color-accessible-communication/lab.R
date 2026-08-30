args <- commandArgs(trailingOnly = TRUE)

option_value <- function(flag, default) {
  match <- which(args == flag)
  if (length(match) == 0) return(default)
  if (match[1] == length(args)) stop(flag, " requires a value")
  args[match[1] + 1]
}

if (!requireNamespace("ggplot2", quietly = TRUE)) {
  stop("Install ggplot2 before running this lab.")
}

script_arg <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
script_dir <- if (length(script_arg)) dirname(normalizePath(sub("^--file=", "", script_arg[1]))) else getwd()
data_path <- option_value("--data", file.path(script_dir, "data", "accessibility_hf_readmission_2026.csv"))
output_dir <- option_value("--output", file.path(script_dir, "output"))

if (!file.exists(data_path)) stop("Data file not found: ", data_path)
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

data <- read.csv(data_path, stringsAsFactors = FALSE, colClasses = c(facility_id = "character"), check.names = FALSE)
required <- c(
  "facility_name", "measure_id", "denominator", "score", "lower_estimate",
  "higher_estimate", "estimate_status", "display_status", "display_label",
  "display_symbol", "display_shape_code", "display_color_hex", "contrast_on_white",
  "reading_order", "short_alt_row", "start_date", "end_date"
)
missing <- setdiff(required, names(data))
if (length(missing)) stop("Missing required columns: ", paste(missing, collapse = ", "))
if (nrow(data) != 65) stop("Expected 65 Massachusetts rows; received ", nrow(data))

reported <- data[data$estimate_status == "reported", ]
if (nrow(reported) != 53) stop("Expected 53 reported estimates.")
reported <- reported[order(reported$score, reported$facility_name), ]
reported$facility_order <- factor(reported$facility_name, levels = reported$facility_name)
reported$status_order <- factor(reported$display_status, levels = c("no different", "worse"))

status_colors <- c("no different" = "#2166AC", "worse" = "#B2182B")
status_shapes <- c("no different" = 16, "worse" = 17)
theme_accessible <- ggplot2::theme_minimal(base_size = 11) +
  ggplot2::theme(
    panel.grid.major.y = ggplot2::element_blank(),
    panel.grid.minor = ggplot2::element_blank(),
    axis.title.y = ggplot2::element_blank(),
    plot.title.position = "plot",
    plot.caption.position = "plot",
    legend.position = "top"
  )

color_shape <- ggplot2::ggplot(reported, ggplot2::aes(y = facility_order)) +
  ggplot2::geom_segment(
    ggplot2::aes(x = lower_estimate, xend = higher_estimate, yend = facility_order),
    color = "#3C3C3C",
    linewidth = 0.55
  ) +
  ggplot2::geom_vline(xintercept = 21.3, color = "#111111", linewidth = 0.7, linetype = "dashed") +
  ggplot2::geom_point(
    ggplot2::aes(x = score, color = status_order, shape = status_order),
    size = 2.8,
    stroke = 0.8
  ) +
  ggplot2::scale_color_manual(
    values = status_colors,
    breaks = c("no different", "worse"),
    labels = c("No different from national", "Worse than national"),
    name = "CMS comparison"
  ) +
  ggplot2::scale_shape_manual(
    values = status_shapes,
    breaks = c("no different", "worse"),
    labels = c("No different from national", "Worse than national"),
    name = "CMS comparison"
  ) +
  ggplot2::labs(
    title = "Color and shape carry the CMS comparison together",
    subtitle = "Massachusetts heart failure readmission estimates, 2023-07-01 to 2025-06-30",
    x = "CMS risk-standardized readmission estimate",
    caption = paste(
      "Points show CMS scores; horizontal lines show source lower and higher estimates.",
      "Dashed reference = national rate of 21.3. Pairwise hospital difference is not tested."
    )
  ) +
  theme_accessible

reported$grayscale_label <- paste0(reported$display_symbol, "  ", reported$facility_name)
reported$grayscale_order <- factor(reported$grayscale_label, levels = reported$grayscale_label)
grayscale <- ggplot2::ggplot(reported, ggplot2::aes(y = grayscale_order)) +
  ggplot2::geom_segment(
    ggplot2::aes(x = lower_estimate, xend = higher_estimate, yend = grayscale_order),
    color = "#4D4D4D",
    linewidth = 0.6
  ) +
  ggplot2::geom_vline(xintercept = 21.3, color = "#000000", linewidth = 0.75, linetype = "dashed") +
  ggplot2::geom_point(ggplot2::aes(x = score, shape = status_order), color = "#111111", size = 2.8, stroke = 0.9) +
  ggplot2::scale_shape_manual(
    values = status_shapes,
    breaks = c("no different", "worse"),
    labels = c("N = no different", "W = worse"),
    name = "CMS comparison"
  ) +
  ggplot2::labs(
    title = "The same finding survives grayscale",
    subtitle = "Shape and the W or N row prefix preserve status without hue",
    x = "CMS risk-standardized readmission estimate",
    caption = "Dashed reference = national rate of 21.3. Source intervals are preserved."
  ) +
  theme_accessible

status_counts <- as.data.frame(table(factor(
  data$display_status,
  levels = c("worse", "no different", "too few", "not available")
)), stringsAsFactors = FALSE)
names(status_counts) <- c("display_status", "count")
status_counts$label <- c("Worse than national", "No different from national", "Too few cases", "Not available")
status_counts$label <- factor(status_counts$label, levels = rev(status_counts$label))

reporting_status <- ggplot2::ggplot(status_counts, ggplot2::aes(x = count, y = label)) +
  ggplot2::geom_col(fill = "#595959", width = 0.65) +
  ggplot2::geom_text(ggplot2::aes(label = count), hjust = -0.25, color = "#111111", size = 4) +
  ggplot2::coord_cartesian(xlim = c(0, 57), clip = "off") +
  ggplot2::labs(
    title = "Twelve of 65 hospitals have no displayed estimate",
    subtitle = "Direct labels and counts communicate status without a color legend",
    x = "Massachusetts hospital rows",
    y = NULL,
    caption = "Source: CMS Unplanned Hospital Visits, READM_30_HF, release 2026-08-13."
  ) +
  theme_accessible +
  ggplot2::theme(legend.position = "none")

cue_key <- data.frame(
  status = factor(
    c("Better than national", "No different from national", "Worse than national", "Too few cases", "Not available"),
    levels = rev(c("Better than national", "No different from national", "Worse than national", "Too few cases", "Not available"))
  ),
  color = c("#1B7837", "#2166AC", "#B2182B", "#4D4D4D", "#111111"),
  shape = c(15, 16, 17, 4, 3),
  symbol = c("B", "N", "W", "T", "NA"),
  contrast = c(5.54, 5.90, 6.87, 8.45, 18.88),
  stringsAsFactors = FALSE
)
cue_key$description <- sprintf("%s  |  %s  |  %.2f:1 on white", cue_key$symbol, cue_key$status, cue_key$contrast)

cue_plot <- ggplot2::ggplot(cue_key, ggplot2::aes(y = status)) +
  ggplot2::geom_point(ggplot2::aes(x = 0, color = color, shape = factor(shape)), size = 5, stroke = 1.1) +
  ggplot2::geom_text(ggplot2::aes(x = 0.12, label = description), hjust = 0, color = "#111111", size = 4) +
  ggplot2::scale_color_identity() +
  ggplot2::scale_shape_manual(values = setNames(cue_key$shape, cue_key$shape)) +
  ggplot2::coord_cartesian(xlim = c(-0.08, 1.25), clip = "off") +
  ggplot2::labs(
    title = "A status cue needs text and shape as well as color",
    subtitle = "Every foreground color exceeds 4.5:1 contrast on white",
    x = NULL,
    y = NULL,
    caption = "Contrast uses the WCAG relative-luminance formula. Verify again in the final delivery context."
  ) +
  theme_accessible +
  ggplot2::theme(
    axis.text = ggplot2::element_blank(),
    axis.ticks = ggplot2::element_blank(),
    panel.grid = ggplot2::element_blank(),
    legend.position = "none"
  )

ggplot2::ggsave(file.path(output_dir, "01-color-plus-shape.png"), color_shape, width = 12, height = 14, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "02-grayscale-redundant.png"), grayscale, width = 12, height = 14, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "03-reporting-status-with-counts.png"), reporting_status, width = 10, height = 5.5, dpi = 150, bg = "white")
ggplot2::ggsave(file.path(output_dir, "04-contrast-and-cue-key.png"), cue_plot, width = 10, height = 6, dpi = 150, bg = "white")

table_fields <- c(
  "reading_order", "facility_id", "facility_name", "score", "lower_estimate",
  "higher_estimate", "denominator", "display_label", "display_symbol",
  "start_date", "end_date", "footnote_text", "short_alt_row"
)
utils::write.csv(data[table_fields], file.path(output_dir, "accessible_hf_readmission_table.csv"), row.names = FALSE, na = "")

status_count <- function(value) sum(data$display_status == value)
alt_text <- c(
  "# Reference text alternative",
  "",
  "## Short alternative",
  "",
  paste(
    "Caterpillar plot of 53 reported Massachusetts hospital heart failure readmission estimates with CMS source intervals and a national reference at 21.3.",
    "One hospital is classified worse than national and 52 are classified no different; 12 additional hospitals have too few cases or no available estimate."
  ),
  "",
  "## Long description",
  "",
  paste(
    "The display contains all 65 Massachusetts hospital rows in the CMS READM_30_HF release for 2023-07-01 through 2025-06-30.",
    "Fifty-three rows have a reported score and source interval."
  ),
  "",
  sprintf(
    "The reported scores range from %.1f to %.1f. CMS classifies %d as worse than the national rate and %d as no different.",
    min(reported$score), max(reported$score), status_count("worse"), status_count("no different")
  ),
  "",
  sprintf(
    "%d rows are marked too few cases and %d are not available. They remain in the accompanying table with blank score and interval cells.",
    status_count("too few"), status_count("not available")
  ),
  "",
  paste(
    "Horizontal lines are the lower and higher estimates published by CMS, not intervals recalculated from the denominator.",
    "The chart compares each hospital with the source national benchmark. It does not test every hospital pair or establish a causal quality difference."
  ),
  "",
  "See accessible_hf_readmission_table.csv for every facility, exact value, interval, denominator, status, period, footnote, and row-level text alternative."
)
writeLines(alt_text, file.path(output_dir, "alt-text-reference.md"), useBytes = TRUE)

cat("Created four figures, one accessible table, and one text alternative in:", normalizePath(output_dir, winslash = "/"), "\n")
