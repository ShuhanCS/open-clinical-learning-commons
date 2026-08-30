#!/usr/bin/env Rscript

suppressPackageStartupMessages(library(ggplot2))

args <- commandArgs(trailingOnly = TRUE)
output_dir <- if (length(args) >= 2 && args[1] == "--output") args[2] else file.path(tempdir(), "oclc-da730-m11-lab")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

script_arg <- grep("^--file=", commandArgs(), value = TRUE)
script_path <- if (length(script_arg)) sub("^--file=", "", script_arg[1]) else "lab.R"
module_root <- dirname(normalizePath(script_path, mustWork = TRUE))
cohort <- read.csv(file.path(module_root, "data", "synthea_acute_transition_cohort_2020.csv"), check.names = FALSE)

index_order <- c("Emergency", "Inpatient")
next_order <- c("No encounter recorded", "Scheduled care", "Urgent care", "Acute return")
endpoint_order <- c("No acute return within 90 days", "Acute return within 90 days", "Death within 90 days")
palette <- c("Emergency" = "#1f49b6", "Inpatient" = "#d97706")
endpoint_palette <- c(
  "No acute return within 90 days" = "#3a7d44",
  "Acute return within 90 days" = "#b54708",
  "Death within 90 days" = "#5b6472"
)
theme_module <- theme_minimal(base_size = 12) +
  theme(
    plot.title = element_text(face = "bold", size = 16),
    plot.subtitle = element_text(color = "#334155"),
    plot.caption = element_text(color = "#475569", hjust = 0),
    panel.grid.minor = element_blank(),
    legend.position = "bottom"
  )

flow <- aggregate(
  patient_id ~ index_class + next_30d_state + endpoint_90d,
  data = cohort,
  FUN = length
)
names(flow)[4] <- "n"
flow$flow_id <- seq_len(nrow(flow))

allocate_stage <- function(data, node_field, node_order, sort_fields, stage, gap = 9) {
  stage_total <- nrow(cohort) + gap * (length(node_order) - 1)
  max_total <- nrow(cohort) + gap * (length(next_order) - 1)
  cursor <- (max_total - stage_total) / 2
  ymin <- ymax <- numeric(nrow(data))
  nodes <- data.frame(stage = numeric(), node = character(), ymin = numeric(), ymax = numeric(), n = numeric())
  for (node in node_order) {
    idx <- which(data[[node_field]] == node)
    ordering <- do.call(order, lapply(sort_fields, function(field) data[[field]][idx]))
    idx <- idx[ordering]
    node_start <- cursor
    for (i in idx) {
      ymin[i] <- cursor
      ymax[i] <- cursor + data$n[i]
      cursor <- ymax[i]
    }
    nodes <- rbind(nodes, data.frame(stage = stage, node = node, ymin = node_start, ymax = cursor, n = sum(data$n[idx])))
    cursor <- cursor + gap
  }
  list(ymin = ymin, ymax = ymax, nodes = nodes)
}

stage0 <- allocate_stage(flow, "index_class", index_order, c("next_30d_state", "endpoint_90d"), 0)
stage1 <- allocate_stage(flow, "next_30d_state", next_order, c("index_class", "endpoint_90d"), 1)
stage2 <- allocate_stage(flow, "endpoint_90d", endpoint_order, c("next_30d_state", "index_class"), 2)
flow$ymin0 <- stage0$ymin; flow$ymax0 <- stage0$ymax
flow$ymin1 <- stage1$ymin; flow$ymax1 <- stage1$ymax
flow$ymin2 <- stage2$ymin; flow$ymax2 <- stage2$ymax
nodes <- rbind(stage0$nodes, stage1$nodes, stage2$nodes)

ribbon_between <- function(row, left, right) {
  x <- seq(left, right, length.out = 31)
  t <- (x - left) / (right - left)
  smooth <- 3 * t^2 - 2 * t^3
  lower <- (1 - smooth) * row[[paste0("ymin", left)]] + smooth * row[[paste0("ymin", right)]]
  upper <- (1 - smooth) * row[[paste0("ymax", left)]] + smooth * row[[paste0("ymax", right)]]
  data.frame(
    flow_id = row$flow_id,
    index_class = row$index_class,
    x = c(x, rev(x)),
    y = c(lower, rev(upper)),
    segment = paste0(left, "-", right)
  )
}

ribbons <- do.call(rbind, lapply(seq_len(nrow(flow)), function(i) {
  rbind(ribbon_between(flow[i, ], 0, 1), ribbon_between(flow[i, ], 1, 2))
}))
stage_labels <- c("Index acute encounter", "First encounter within 30 days", "Ninety-day endpoint")
nodes$label <- paste0(nodes$node, "\nn=", nodes$n)
nodes$label_x <- c(0.03, 0.03, rep(1.03, 4), rep(1.97, 3))
nodes$label_hjust <- c(0, 0, rep(0, 4), rep(1, 3))

p_flow <- ggplot() +
  geom_polygon(
    data = ribbons,
    aes(x = x, y = y, group = interaction(flow_id, segment), fill = index_class),
    alpha = 0.55,
    color = NA
  ) +
  geom_rect(
    data = nodes,
    aes(xmin = stage - 0.025, xmax = stage + 0.025, ymin = ymin, ymax = ymax),
    fill = "#172033"
  ) +
  geom_label(
    data = nodes,
    aes(x = label_x, y = (ymin + ymax) / 2, label = label, hjust = label_hjust),
    color = "#172033",
    fill = "white",
    linewidth = 0,
    label.padding = grid::unit(0.08, "lines"),
    size = 2.8,
    lineheight = 0.88
  ) +
  scale_fill_manual(values = palette, name = "Index class") +
  scale_x_continuous(breaks = 0:2, labels = stage_labels, limits = c(-0.20, 2.20), expand = expansion(mult = 0)) +
  labs(
    title = "Most synthetic acute episodes had no encounter recorded within 30 days",
    subtitle = "Each ribbon retains one adult synthetic patient from one index event through one mutually exclusive endpoint",
    x = NULL,
    y = "Synthetic patients",
    caption = "Cohort: first emergency or inpatient encounter per adult, 2015-2019. Synthea sample data are simulated and do not estimate real care quality."
  ) +
  theme_module +
  theme(panel.grid = element_blank(), axis.text.y = element_blank(), axis.ticks.y = element_blank())
ggsave(file.path(output_dir, "01-defined-cohort-flow.png"), p_flow, width = 14, height = 8, dpi = 180)

matrix <- aggregate(patient_id ~ index_class + next_30d_state, cohort, length)
names(matrix)[3] <- "n"
denoms <- aggregate(patient_id ~ index_class, cohort, length)
names(denoms)[2] <- "denominator"
matrix <- merge(matrix, denoms, by = "index_class")
matrix$row_pct <- 100 * matrix$n / matrix$denominator
matrix$label <- sprintf("%d\n%.1f%%", matrix$n, matrix$row_pct)
matrix$index_class <- factor(matrix$index_class, levels = rev(index_order))
matrix$next_30d_state <- factor(matrix$next_30d_state, levels = next_order)

p_matrix <- ggplot(matrix, aes(next_30d_state, index_class, fill = row_pct)) +
  geom_tile(color = "white", linewidth = 1.5) +
  geom_text(aes(label = label), fontface = "bold", size = 4) +
  scale_fill_gradient(low = "#eef4ff", high = "#1f49b6", name = "Within-index\npercentage") +
  labs(
    title = "The matrix makes each index denominator explicit",
    subtitle = "Cell labels show count and percentage within the index encounter class",
    x = "First encounter within 30 days",
    y = "Index encounter class",
    caption = "No encounter recorded means none appears in this Synthea extract during the defined window. It is not evidence of failed follow-up."
  ) +
  theme_module +
  theme(axis.text.x = element_text(angle = 18, hjust = 1))
ggsave(file.path(output_dir, "02-transition-matrix.png"), p_matrix, width = 11.5, height = 6.5, dpi = 180)

composition <- aggregate(patient_id ~ index_class + endpoint_90d, cohort, length)
names(composition)[3] <- "n"
composition <- merge(composition, denoms, by = "index_class")
composition$pct <- 100 * composition$n / composition$denominator
composition$endpoint_90d <- factor(composition$endpoint_90d, levels = endpoint_order)
composition$index_class <- factor(composition$index_class, levels = index_order)

p_composition <- ggplot(composition, aes(index_class, pct, fill = endpoint_90d)) +
  geom_col(width = 0.62, color = "white") +
  geom_text(aes(label = ifelse(pct >= 3, sprintf("%.1f%%\n(n=%d)", pct, n), "")), position = position_stack(vjust = 0.5), color = "white", fontface = "bold", size = 3.4) +
  scale_fill_manual(values = endpoint_palette, name = "Ninety-day endpoint") +
  scale_y_continuous(labels = function(x) paste0(x, "%"), expand = expansion(mult = c(0, 0.05))) +
  labs(
    title = "Composition answers a different question than the flow",
    subtitle = "The denominator resets within each index encounter class and remains visible",
    x = "Index encounter class",
    y = "Percentage of synthetic patients",
    caption = "Death is shown as a mutually exclusive endpoint and takes precedence over the acute-return label."
  ) +
  theme_module
ggsave(file.path(output_dir, "03-endpoint-composition.png"), p_composition, width = 10.5, height = 7, dpi = 180)

paths <- unique(cohort[c("transition_path", "path_count", "path_denominator", "path_acute_return_count", "path_acute_return_pct", "cohort_acute_return_pct", "priority_screen")])
paths <- paths[order(-paths$path_count, paths$transition_path), ]
write.csv(paths, file.path(output_dir, "transition-path-decision-table.csv"), row.names = FALSE, quote = TRUE)

alt_text <- c(
  "# Module 11 reference figure alternatives",
  "",
  "## Defined cohort flow",
  "",
  "The alluvial display follows 374 adult synthetic patients. Each person contributes one first emergency or inpatient encounter from 2015 through 2019. There are 314 emergency index encounters and 60 inpatient index encounters. Within 30 days, 263 people have no encounter recorded, 92 have scheduled care, 15 have an acute return, and 4 have urgent care. By 90 days, 330 have no acute return recorded, 36 have an acute return, and 8 die. Ribbon widths encode patient counts and conserve the same 374 people at every stage.",
  "",
  "## Transition matrix",
  "",
  "The matrix crosses index class with the first encounter state within 30 days. Emergency episodes include 225 people with no encounter recorded, 73 with scheduled care, 12 with an acute return, and 4 with urgent care. Inpatient episodes include 38 with no encounter recorded, 19 with scheduled care, and 3 with an acute return. Each cell states both its count and its percentage within the index class.",
  "",
  "## Endpoint composition",
  "",
  "The 100 percent stacked bars compare mutually exclusive 90-day endpoints within emergency and inpatient index groups. The chart uses a separate denominator for each bar and labels sufficiently large segments with a percentage and count.",
  "",
  "## Interpretation boundary",
  "",
  "These are simulated Synthea records. No encounter recorded means no qualifying row appears in the extract during the declared interval. It does not prove that follow-up failed, that care occurred outside a network, or that the pattern exists in a real population."
)
writeLines(alt_text, file.path(output_dir, "alt-text-reference.md"), useBytes = TRUE)

cat(sprintf("Module 11 lab wrote 3 figures, 1 table, and 1 text alternative to %s\n", output_dir))
