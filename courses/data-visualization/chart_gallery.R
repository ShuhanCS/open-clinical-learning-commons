# Clinical visualization chart atlas
#
# This script creates ten small synthetic examples that match the public chart
# atlas. Install the two packages once with:
# install.packages(c("ggplot2", "ggalluvial"))

required_packages <- c("ggplot2", "ggalluvial")
missing_packages <- required_packages[
  !vapply(required_packages, requireNamespace, logical(1), quietly = TRUE)
]

if (length(missing_packages) > 0) {
  stop(
    "Install the missing package(s) first: install.packages(c(",
    paste(sprintf('"%s"', missing_packages), collapse = ", "),
    "))"
  )
}

library(ggplot2)
library(ggalluvial)

script_argument <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
script_directory <- if (length(script_argument) == 1) {
  dirname(normalizePath(sub("^--file=", "", script_argument)))
} else {
  getwd()
}
output_directory <- file.path(script_directory, "outputs", "chart-gallery")
dir.create(output_directory, recursive = TRUE, showWarnings = FALSE)

ink <- "#172033"
muted <- "#5d687b"
blue <- "#1f49b6"
cyan <- "#0d8fa6"
green <- "#147a5a"
amber <- "#d97706"
coral <- "#d4543f"
grid <- "#dce3ee"

atlas_theme <- theme_minimal(base_size = 12) +
  theme(
    plot.title = element_text(face = "bold", size = 16, color = ink),
    plot.subtitle = element_text(color = muted),
    plot.caption = element_text(color = muted, hjust = 0),
    axis.title = element_text(color = muted),
    panel.grid.minor = element_blank(),
    panel.grid.major = element_line(color = grid, linewidth = 0.35),
    legend.position = "bottom",
    legend.title = element_blank()
  )

chart_labs <- function(title, subtitle, x = NULL, y = NULL) {
  labs(
    title = title,
    subtitle = subtitle,
    x = x,
    y = y,
    caption = "Synthetic teaching data"
  )
}

# 01. Comparison: dot plot
comparison <- data.frame(
  unit = c("North", "Central", "South", "West"),
  follow_up_rate = c(78, 71, 64, 59)
)
comparison$unit <- reorder(comparison$unit, comparison$follow_up_rate)

comparison_plot <- ggplot(comparison, aes(follow_up_rate, unit)) +
  geom_segment(
    aes(x = 0, xend = follow_up_rate, yend = unit),
    color = grid,
    linewidth = 1.2
  ) +
  geom_point(size = 4, color = blue) +
  geom_text(aes(label = paste0(follow_up_rate, "%")), hjust = -0.5, color = ink) +
  coord_cartesian(xlim = c(0, 85), clip = "off") +
  chart_labs(
    "North has the highest follow-up rate",
    "Share of patients contacted within 72 hours",
    "Follow-up within 72 hours (%)",
    NULL
  ) +
  atlas_theme

# 02. Distribution: histogram
set.seed(730)
length_of_stay <- c(rgamma(620, shape = 3.2, scale = 38), rgamma(80, shape = 5, scale = 92))
distribution <- data.frame(minutes = pmin(length_of_stay, 720))

distribution_plot <- ggplot(distribution, aes(minutes)) +
  geom_histogram(binwidth = 45, boundary = 0, fill = blue, color = "white") +
  geom_vline(xintercept = median(distribution$minutes), color = coral, linewidth = 1.1) +
  annotate(
    "text",
    x = median(distribution$minutes) + 12,
    y = Inf,
    label = "Median",
    hjust = 0,
    vjust = 1.8,
    color = coral
  ) +
  chart_labs(
    "Most visits are short, but a long tail remains",
    "Emergency department length of stay",
    "Minutes",
    "Visits"
  ) +
  atlas_theme

# 03. Time: line chart
monthly <- data.frame(
  month = factor(month.abb, levels = month.abb),
  on_time = c(61, 63, 65, 64, 68, 70, 73, 74, 72, 76, 79, 82)
)

time_plot <- ggplot(monthly, aes(month, on_time, group = 1)) +
  geom_line(linewidth = 1.2, color = blue) +
  geom_point(size = 2.8, color = blue) +
  geom_text(
    data = monthly[c(1, nrow(monthly)), ],
    aes(label = paste0(on_time, "%")),
    vjust = -0.8,
    color = ink
  ) +
  coord_cartesian(ylim = c(55, 87)) +
  chart_labs(
    "On-time follow-up improved across the year",
    "Monthly share completed within 72 hours",
    NULL,
    "On-time follow-up"
  ) +
  atlas_theme

# 04. Relationship: scatter plot
set.seed(731)
relationship <- data.frame(
  travel_minutes = seq(8, 64, length.out = 36)
)
relationship$missed_visits <- pmax(
  2,
  4 + relationship$travel_minutes * 0.42 + rnorm(nrow(relationship), 0, 3.2)
)

relationship_plot <- ggplot(relationship, aes(travel_minutes, missed_visits)) +
  geom_point(size = 2.8, alpha = 0.78, color = cyan) +
  geom_smooth(method = "lm", se = TRUE, color = blue, fill = "#dce7ff") +
  chart_labs(
    "Longer travel is associated with more missed visits",
    "The chart shows association, not cause",
    "Travel time to clinic (minutes)",
    "Missed visits per 100 appointments"
  ) +
  atlas_theme

# 05. Uncertainty: forest plot
uncertainty <- data.frame(
  service = factor(c("Ward A", "Ward B", "Ward C", "Ward D"), levels = rev(c("Ward A", "Ward B", "Ward C", "Ward D"))),
  estimate = c(0.82, 0.93, 1.08, 1.19),
  low = c(0.68, 0.84, 0.88, 0.97),
  high = c(0.99, 1.03, 1.31, 1.46)
)

uncertainty_plot <- ggplot(uncertainty, aes(estimate, service)) +
  geom_vline(xintercept = 1, color = muted, linetype = "dashed") +
  geom_errorbar(
    aes(xmin = low, xmax = high),
    orientation = "y",
    width = 0,
    linewidth = 1,
    color = blue
  ) +
  geom_point(size = 3.6, color = coral) +
  chart_labs(
    "The estimates differ in precision",
    "Rate ratio with 95% confidence interval",
    "Rate ratio",
    NULL
  ) +
  atlas_theme

# 06. Flow: Sankey-style alluvial chart
journeys <- data.frame(
  arrival = c("Walk-in", "Walk-in", "Walk-in", "Ambulance", "Ambulance", "Ambulance"),
  decision = c("Discharge", "Observation", "Admit", "Discharge", "Observation", "Admit"),
  outcome = c("Home", "Home", "Ward", "Home", "Ward", "Ward"),
  visits = c(390, 95, 115, 80, 105, 215)
)

flow_plot <- ggplot(
  journeys,
  aes(axis1 = arrival, axis2 = decision, axis3 = outcome, y = visits)
) +
  geom_alluvium(aes(fill = decision), width = 0.12, alpha = 0.78) +
  geom_stratum(width = 0.12, fill = "white", color = ink) +
  geom_text(stat = "stratum", aes(label = after_stat(stratum)), size = 3.2) +
  scale_x_discrete(limits = c("Arrival", "Decision", "Outcome"), expand = c(0.08, 0.05)) +
  scale_fill_manual(values = c("Discharge" = blue, "Observation" = amber, "Admit" = coral)) +
  chart_labs(
    "Patient pathways split after arrival",
    "Ribbon width represents synthetic visit count",
    NULL,
    "Visits"
  ) +
  atlas_theme +
  theme(panel.grid = element_blank())

# 07. Network: node-link diagram
nodes <- data.frame(
  node = c("Primary care", "Cardiology", "Imaging", "Pharmacy", "Home health"),
  x = c(0, 1.1, 1.05, 2.1, 2.1),
  y = c(0.5, 0.9, 0.15, 0.95, 0.15),
  referrals = c(420, 205, 170, 135, 92)
)
edges <- data.frame(
  from = c("Primary care", "Primary care", "Cardiology", "Imaging", "Cardiology"),
  to = c("Cardiology", "Imaging", "Pharmacy", "Home health", "Home health")
)
edges <- merge(edges, nodes[, c("node", "x", "y")], by.x = "from", by.y = "node")
names(edges)[names(edges) %in% c("x", "y")] <- c("x_from", "y_from")
edges <- merge(edges, nodes[, c("node", "x", "y")], by.x = "to", by.y = "node")
names(edges)[names(edges) %in% c("x", "y")] <- c("x_to", "y_to")

network_plot <- ggplot() +
  geom_segment(
    data = edges,
    aes(x_from, y_from, xend = x_to, yend = y_to),
    linewidth = 1.3,
    color = "#a9b8ce"
  ) +
  geom_point(data = nodes, aes(x, y, size = referrals), color = blue) +
  geom_text(data = nodes, aes(x, y, label = node), nudge_y = -0.13, size = 3.2, color = ink) +
  scale_size(range = c(5, 11), guide = "none") +
  coord_equal(xlim = c(-0.3, 2.5), ylim = c(-0.1, 1.2), clip = "off") +
  chart_labs(
    "Referral links cluster around primary care",
    "A link means a recorded referral, not proof of collaboration"
  ) +
  atlas_theme +
  theme(panel.grid = element_blank(), axis.text = element_blank(), axis.ticks = element_blank())

# 08. Composition: 100% stacked bar
service_mix <- data.frame(
  quarter = rep(c("Q1", "Q2", "Q3", "Q4"), each = 4),
  service = rep(c("Emergency", "Inpatient", "Outpatient", "Virtual"), 4),
  visits = c(26, 30, 35, 9, 24, 29, 35, 12, 23, 27, 34, 16, 21, 25, 32, 22)
)

composition_plot <- ggplot(service_mix, aes(quarter, visits, fill = service)) +
  geom_col(position = "fill", width = 0.68) +
  scale_y_continuous(labels = function(value) paste0(round(value * 100), "%")) +
  scale_fill_manual(values = c(blue, coral, green, amber)) +
  chart_labs(
    "Virtual care takes a larger share of visits",
    "Quarterly service mix",
    NULL,
    "Share of visits"
  ) +
  atlas_theme

# 09. Place: proportional-symbol map
clinics <- data.frame(
  clinic = c("North", "Central", "East", "South", "West"),
  x = c(3.2, 2.4, 3.8, 2.7, 1.2),
  y = c(4.1, 2.8, 2.2, 1.0, 2.0),
  patients = c(820, 1290, 610, 430, 710),
  access_gap = c(12, 27, 18, 35, 22)
)

place_plot <- ggplot(clinics, aes(x, y)) +
  annotate("rect", xmin = 0.5, xmax = 4.5, ymin = 0.5, ymax = 4.6, fill = "#eef3f8", color = grid) +
  geom_path(
    data = data.frame(x = c(0.8, 1.6, 2.1, 3.0, 4.2), y = c(3.8, 3.2, 2.4, 2.1, 1.2)),
    aes(x, y),
    linewidth = 6,
    color = "white",
    inherit.aes = FALSE
  ) +
  geom_point(aes(size = patients, color = access_gap), alpha = 0.9) +
  geom_text(aes(label = clinic), nudge_y = -0.32, size = 3.2, color = ink) +
  scale_size(range = c(6, 14), guide = "none") +
  scale_color_gradient(low = blue, high = amber, name = "Access gap") +
  coord_equal(xlim = c(0.4, 4.6), ylim = c(0.4, 4.8), clip = "off") +
  chart_labs(
    "The largest access gap is near South clinic",
    "Circle size shows patients; color shows access gap"
  ) +
  atlas_theme +
  theme(panel.grid = element_blank(), axis.text = element_blank(), axis.ticks = element_blank())

# 10. Dashboard: calendar-style heatmap
dashboard <- expand.grid(
  day = c("Mon", "Tue", "Wed", "Thu", "Fri"),
  hour = c(8, 10, 12, 14, 16, 18)
)
dashboard$wait_minutes <- with(dashboard, 18 + 7 * (hour >= 12) +
  9 * (hour >= 16) + 5 * (day %in% c("Tue", "Wed", "Thu")))
dashboard$day <- factor(dashboard$day, levels = rev(c("Mon", "Tue", "Wed", "Thu", "Fri")))
dashboard$hour <- factor(sprintf("%02d", dashboard$hour), levels = c("08", "10", "12", "14", "16", "18"))

dashboard_plot <- ggplot(dashboard, aes(hour, day, fill = wait_minutes)) +
  geom_tile(color = "white", linewidth = 1) +
  geom_text(
    aes(label = wait_minutes, color = wait_minutes <= 25),
    size = 3.4,
    show.legend = FALSE
  ) +
  scale_color_manual(values = c("FALSE" = ink, "TRUE" = "white")) +
  scale_fill_viridis_c(option = "C", name = "Wait (min)") +
  chart_labs(
    "Afternoon waits need attention",
    "Median check-in wait by weekday and time",
    "Hour",
    NULL
  ) +
  atlas_theme

charts <- list(
  "01-comparison-dot-plot.png" = comparison_plot,
  "02-distribution-histogram.png" = distribution_plot,
  "03-time-line-chart.png" = time_plot,
  "04-relationship-scatter-plot.png" = relationship_plot,
  "05-uncertainty-forest-plot.png" = uncertainty_plot,
  "06-flow-sankey-alluvial.png" = flow_plot,
  "07-network-node-link.png" = network_plot,
  "08-composition-stacked-bar.png" = composition_plot,
  "09-place-proportional-symbol-map.png" = place_plot,
  "10-dashboard-heatmap.png" = dashboard_plot
)

for (filename in names(charts)) {
  ggsave(
    filename = file.path(output_directory, filename),
    plot = charts[[filename]],
    width = 8,
    height = 5.2,
    dpi = 160,
    bg = "white"
  )
}

expected_outputs <- file.path(output_directory, names(charts))
stopifnot(length(charts) == 10, all(file.exists(expected_outputs)))
message("Created 10 chart examples in ", output_directory)
