# Module 01: Encoding and the grammar of graphics

- Course: DA-730, Clinical Data Visualization and Decision Storytelling
- Module ID: `oclc-da730-01`
- Learner time: 7 hours
- Release status: runnable release candidate
- Module version: 0.1.0

## The decision

A Massachusetts hospital patient-experience director needs a readable comparison of published HCAHPS recommendation results. The display should help the director choose where to begin a deeper qualitative review. It must not present one survey result as a complete hospital ranking.

Your first job is not to choose a chart name. It is to decide what each variable means and which visible property will carry it.

## Competency

Given a healthcare question and tabular data, map variables to suitable visual channels and explain why the resulting display has its form.

By the end of the module, you can:

1. classify a variable as nominal, ordered, quantitative, or temporal for the question at hand;
2. identify the marks, channels, scales, coordinate system, labels, and layers in a chart;
3. map a quantitative comparison to aligned position or length;
4. distinguish data encodings from annotations and source notes;
5. document a chart as a reproducible variable-to-channel map; and
6. state what decision the chart can support and what it cannot establish.

## Before you begin

You need the week-zero R bridge or equivalent skills:

- open an R script;
- set a working directory or use a project;
- run a complete script;
- find a CSV and a PNG; and
- read a simple error message.

You do not need to write a chart from a blank file for Tier 1.

## Twenty-minute concept core

### 1. Start with the variables

A variable's role depends on the question.

| Type | Meaning | Examples in this case |
|---|---|---|
| Nominal | Names or groups with no inherent order | Hospital, city, state |
| Ordered | Categories with a defensible order | Low, medium, high; one to five stars |
| Quantitative | Amounts on a numeric scale | Recommendation percent, completed surveys |
| Temporal | Dates, times, or durations | Measurement-period start and end |

The same stored field can play different roles. A facility ID is stored as characters, but its role is nominal. Converting it to a number would not make arithmetic meaningful.

### 2. Choose a mark

A mark is the visible object that represents data.

- A point represents one hospital result.
- A line can connect values or represent a path through time.
- An area can represent an interval, region, or magnitude when area is the intended comparison.

In the worked chart, each hospital is one point. A faint segment connects the statewide reference value to that hospital's point. Text repeats the exact percentage.

### 3. Map variables to channels

A channel is a property of a mark that can vary.

| Channel | Good use | Common problem |
|---|---|---|
| Position | Precise quantitative comparison on a shared scale | A broken or unexplained scale changes the apparent gap |
| Length | Quantitative comparison from a common baseline | Unequal baselines make lengths hard to compare |
| Angle or area | Broad magnitude or part-to-whole patterns | People estimate these less precisely than aligned position |
| Color lightness | Ordered magnitude with a clear sequential scale | Small differences may be inaccessible or hard to judge |
| Color hue | Distinct groups | Hue has no natural numerical order |
| Shape | A small number of distinct groups | Too many shapes become difficult to distinguish |
| Text | Exact values, direct labels, or annotations | Dense text can overwhelm the pattern |

For a precise hospital comparison, `recommend_percent` belongs on an aligned position scale. An unordered palette should not carry the percentage by itself. Circle area should not carry the only evidence for a close comparison.

### 4. Assemble the grammar

Read a chart as a sentence with six parts:

1. **Data:** Which rows and variables are in view?
2. **Mapping:** Which variable controls each visible channel?
3. **Mark or geometry:** What object represents a row or summary?
4. **Scale and coordinates:** How do data values become visible positions, lengths, sizes, or colors?
5. **Labels and annotations:** What helps the reader interpret the display?
6. **Layers:** Which parts are data marks, references, labels, and context?

Chart labels such as dot plot, bar chart, and heatmap are useful shorthand. The grammar explains why the display works and makes repair easier when it does not.

## Worked encoding map

The lab builds a comparison of the 15 Massachusetts hospitals with the most completed surveys in the pinned CMS release. This is a readable teaching peer set, not a quality class.

| Variable | Role | Mark or layer | Channel | Reason |
|---|---|---|---|---|
| `facility_name` | Nominal | Point | Y position | One aligned row supports facility lookup. |
| `recommend_percent` | Quantitative | Point | X position | A common scale supports precise comparison. |
| `recommend_percent` | Quantitative | Text | Direct label | The exact published value is available without estimating position. |
| `completed_surveys` | Quantitative context | Selection rule | Not encoded | It defines the 15-row teaching view and remains visible in the table. |
| Statewide median | Reference statistic | Dashed line | X position | It gives orientation without declaring a target. |
| CMS release and period | Provenance | Caption | Not encoded | They describe the evidence rather than a hospital result. |

## Run the package

From this module directory:

```powershell
Rscript validate_hcahps.R
Rscript lab.R
Rscript critique_charts.R
```

If `Rscript` is not on your terminal path, run the scripts from RStudio or use the full path to your R installation.

The lab creates:

- `outputs/lab/peer-set-table.csv`
- `outputs/lab/encoding-map.csv`
- `outputs/lab/layered-comparison.png`

The critique script creates two intentionally flawed displays:

- `outputs/critique/01-unordered-color.png`
- `outputs/critique/02-area-for-precision.png`

Generated output folders are working files. Your assessed submission uses the filenames in `assessment.md`.

## Three scaffold tiers

### Tier 1: Run and observe

Run `lab.R` without editing it. Match each row in `encoding-map.csv` to the rendered chart. Identify the data, mapping, marks, scale, coordinates, labels, and layers.

### Tier 2: Modify and explain

Make one change at a time in a copy of `lab.R`:

1. replace the point with a bar and explain what length adds or removes;
2. remove direct labels and record what becomes harder to read; and
3. map completed survey count to size, then decide whether that added channel helps the director's question.

Your explanation matters more than matching one preferred chart style.

### Tier 3: Author and justify

Build a comparison for the named director. Submit the exact six-file package in `assessment.md`. Your chart may differ from the reference if its mappings are accurate, readable, accessible, and justified.

## Interpretation boundaries

- The data are hospital-level published survey results, not patient records.
- A recommendation percentage is not a complete measure of hospital quality.
- The 15-hospital view is selected by completed survey count for readability. It is not a clinical peer-group definition.
- Response, case mix, survey mode, sampling, adjustment, and uncertainty require deeper analysis than this first module provides.
- The chart may identify results for follow-up. It does not establish why results differ or which intervention will change them.

Modules 05 and 06 own denominators, adjustment, uncertainty, and small-number judgment. Module 02 next asks how accurately readers can perceive the encodings chosen here.

## Accessibility requirements

Your figure must include a descriptive title, named measure, units, readable text, visible source and period, and a written text alternative. Do not make color the only way to recover a required value or group. Test the PNG at ordinary document size.

## AI use

You may use an AI assistant to explain syntax, help debug, or propose alternatives. You remain responsible for the source, mappings, code, chart, and claims. Record the tool, prompt purpose, adopted change, and verification in the disclosure section of `decision-note.md`. If you did not use AI, write `No AI assistance used.`

## Source

Centers for Medicare & Medicaid Services, Patient survey (HCAHPS) - Hospital:

https://data.cms.gov/provider-data/dataset/dgck-syfz

The committed extract is from the CMS release dated 2026-08-13 and covers 2024-10-01 through 2025-09-30. See `source-record.yml` and `data-spec.md` for the exact query, transformations, public-domain notice, checksum, and limits.
