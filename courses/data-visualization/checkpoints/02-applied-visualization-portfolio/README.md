# Checkpoint 2: applied visualization portfolio

This package assembles and checks the DA-730 Week 6 submission. It uses released work from Modules 07 through 12 to create six figures, six exact tables, six accessible alternatives, and six matching source records. Learners complete the portfolio argument, view-purpose audit, critique repair, accessibility report, decision brief, capstone proposal, and AI-use record.

The full contract is in [the checkpoint specification](../../../../docs/curriculum/courses/DA-730/checkpoints/02-applied-visualization-portfolio-spec.md).

## Assemble a starter portfolio

Run from the repository root:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File courses/data-visualization/checkpoints/02-applied-visualization-portfolio/assemble_checkpoint.ps1 -Target checkpoint-2
```

If `Rscript` is not on the command path, pass its full path with `-RscriptPath`.

The target must be absent or empty. The script does not overwrite existing work.

## Six evidence chains

| Artifact | Analysis | Exact table | Source record | Accessible alternative |
|---|---|---|---|---|
| `figures/accessible-display.png` | `analysis/accessible-display.R` | `evidence-tables/accessible-display.csv` | `source-records/accessible-display-source.yml` | `alt-text/accessible-display.md` |
| `figures/time-display.png` | `analysis/time-display.R` | `evidence-tables/time-display.csv` | `source-records/time-display-source.yml` | `alt-text/time-display.md` |
| `figures/comparison-display.png` | `analysis/comparison-display.R` | `evidence-tables/comparison-display.csv` | `source-records/comparison-display-source.yml` | `alt-text/comparison-display.md` |
| `figures/place-display.png` | `analysis/place-display.R` | `evidence-tables/place-display.csv` | `source-records/place-display-source.yml` | `alt-text/place-display.md` |
| `figures/structure-display.png` | `analysis/structure-display.R` | `evidence-tables/structure-display.csv` | `source-records/structure-display-source.yml` | `alt-text/structure-display.md` |
| `figures/dashboard.png` | `analysis/dashboard.R` | `evidence-tables/dashboard.csv` | `source-records/dashboard-source.yml` | `alt-text/dashboard.md` |

The default analysis wrappers call the released module labs. A learner who changes a figure may replace the matching wrapper with another approved editable source while keeping the base name and evidence chain.

## Complete the submission

Replace every bracketed instruction in the eight Markdown templates. Update a source record, table, and accessible alternative whenever a figure changes.

The review panel decides whether to approve, approve with conditions, revise, or refer the proposed Module 13 capstone.

## Validate the completed portfolio

```powershell
python courses/data-visualization/checkpoints/02-applied-visualization-portfolio/validate_checkpoint.py checkpoint-2
```

Test the validator itself with:

```powershell
python courses/data-visualization/checkpoints/02-applied-visualization-portfolio/validate_checkpoint.py --self-check
```

The structural check does not grade clinical reasoning. An instructor still reviews the interpretation, decision boundaries, source fit, accessibility, AI verification, and capstone feasibility.
