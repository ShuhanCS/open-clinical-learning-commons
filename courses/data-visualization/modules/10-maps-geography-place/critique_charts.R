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
data_path <- option_value("--data", file.path(script_dir, "data", "nc_place_access_2026.csv"))
boundary_path <- option_value("--boundaries", file.path(script_dir, "data", "nc_county_boundaries_2024.csv"))
output_dir <- option_value("--output", file.path(script_dir, "critique-output"))

if (!file.exists(data_path) || !file.exists(boundary_path)) stop("The teaching table and boundary file are required.")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

data <- read.csv(data_path, stringsAsFactors = FALSE, colClasses = c(county_fips = "character"))
boundaries <- read.csv(boundary_path, stringsAsFactors = FALSE, colClasses = c(county_fips = "character"))
if (nrow(data) != 100 || nrow(boundaries) != 7121) stop("Released place data do not match the expected row counts.")
map_data <- cbind(boundaries, data[match(boundaries$county_fips, data$county_fips), setdiff(names(data), c("county_fips", "county_name")), drop = FALSE])

albers_equal_area <- function(longitude, latitude) {
  radians <- pi / 180
  phi1 <- 29.5 * radians
  phi2 <- 45.5 * radians
  phi0 <- 23 * radians
  lambda0 <- -96 * radians
  phi <- latitude * radians
  n <- 0.5 * (sin(phi1) + sin(phi2))
  theta <- n * (longitude * radians - lambda0)
  c_value <- cos(phi1)^2 + 2 * n * sin(phi1)
  rho <- sqrt(c_value - 2 * n * sin(phi)) / n
  rho0 <- sqrt(c_value - 2 * n * sin(phi0)) / n
  data.frame(projected_x = rho * sin(theta), projected_y = rho0 - rho * cos(theta))
}
map_data <- cbind(map_data, albers_equal_area(map_data$longitude, map_data$latitude))

raw_count_map <- ggplot2::ggplot(
  map_data,
  ggplot2::aes(x = projected_x, y = projected_y, group = polygon_group, fill = adult_population)
) +
  ggplot2::geom_polygon(color = "white", linewidth = 0.15) +
  ggplot2::coord_equal() +
  ggplot2::scale_fill_gradient(low = "#fee5d9", high = "#a50f15", name = "Adults") +
  ggplot2::labs(
    title = "Where health need is greatest",
    subtitle = "Adult population shown as if it were a health rate",
    caption = "Deliberately flawed: population size is mislabeled as need."
  ) +
  ggplot2::theme_void(base_size = 12) +
  ggplot2::theme(plot.title = ggplot2::element_text(face = "bold"))

ggplot2::ggsave(file.path(output_dir, "C1-raw-count-need-map.png"), raw_count_map, width = 10, height = 7, dpi = 180, bg = "white")

map_data$arbitrary_label <- cut(
  map_data$age_adjusted_fair_poor_health_pct,
  breaks = c(-Inf, 17, 20, 22, Inf),
  labels = c("Low", "Medium", "High", "Critical"),
  right = FALSE
)
arbitrary_map <- ggplot2::ggplot(
  map_data,
  ggplot2::aes(x = projected_x, y = projected_y, group = polygon_group, fill = arbitrary_label)
) +
  ggplot2::geom_polygon(color = "#f7f7f7", linewidth = 0.15) +
  ggplot2::coord_equal() +
  ggplot2::scale_fill_manual(values = c("Low" = "#ffffcc", "Medium" = "#fd8d3c", "High" = "#e31a1c", "Critical" = "#800026")) +
  ggplot2::labs(
    title = "County risk categories",
    subtitle = "Unexplained cut points turn a continuous estimate into official-sounding labels",
    fill = "Risk",
    caption = "Deliberately flawed: bins and category names have no declared decision basis."
  ) +
  ggplot2::theme_void(base_size = 12) +
  ggplot2::theme(plot.title = ggplot2::element_text(face = "bold"))

ggplot2::ggsave(file.path(output_dir, "C2-arbitrary-bin-map.png"), arbitrary_map, width = 10, height = 7, dpi = 180, bg = "white")

map_data$stigmatizing <- ifelse(map_data$reference_shortlist == "yes", "Problem county", "Other")
stigma_map <- ggplot2::ggplot(
  map_data,
  ggplot2::aes(x = projected_x, y = projected_y, group = polygon_group, fill = stigmatizing)
) +
  ggplot2::geom_polygon(color = "white", linewidth = 0.15) +
  ggplot2::coord_equal() +
  ggplot2::scale_fill_manual(values = c("Problem county" = "#d7301f", "Other" = "#f0f0f0")) +
  ggplot2::labs(
    title = "North Carolina's problem counties",
    subtitle = "A screening list is presented as a fixed identity",
    fill = NULL,
    caption = "Deliberately flawed: stigmatizing language replaces evidence, context, and local voice."
  ) +
  ggplot2::theme_void(base_size = 12) +
  ggplot2::theme(plot.title = ggplot2::element_text(face = "bold"))

ggplot2::ggsave(file.path(output_dir, "C3-stigmatizing-place-labels.png"), stigma_map, width = 10, height = 7, dpi = 180, bg = "white")

message("Created three deliberately flawed place figures in: ", normalizePath(output_dir))
