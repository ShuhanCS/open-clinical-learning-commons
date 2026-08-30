# Reference figure accessibility record

## Calibration display

`outputs/calibration.svg` is labeled as a teaching display and includes a title and description in the SVG. It compares five equal-size test groups using predicted probability on the horizontal axis and observed outcome proportion on the vertical axis.

The display does not stand alone. `outputs/calibration-table.csv` contains every group, row count, outcome count, mean prediction, observed proportion, minimum prediction, maximum prediction, and interpretation limit.

## Threshold display

`outputs/threshold.svg` includes a title, description, named axes, line labels, and the exact locked threshold. It shows validation sensitivity and specificity over observed candidate thresholds and marks 0.08513264.

`outputs/threshold-table.csv` is the required structured alternative. It contains all 71 thresholds and exact TN, FP, FN, TP, sensitivity, specificity, PPV, NPV, and rule status values.

## Visual boundaries

- Color is not the only source of exact meaning; tables and line labels are present.
- No point must be read from pixel position to complete the assessment.
- The figures do not imply smooth performance between observed thresholds.
- The calibration figure does not claim a stable curve from four outcomes.
- The SVG files contain no local path, secret, or patient-identifying information.
