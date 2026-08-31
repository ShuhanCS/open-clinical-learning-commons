# Sensitivity interpretation

- Conditions reviewed: `C01 through C05`
- Option-condition comparisons: `15`
- Null or failed comparisons retained: `6`
- Full-rule comparisons: `0 at the primary condition`

S01 becomes more favorable as load rises, but its point-demand median improvement remains below the predeclared 10-minute threshold. S02 improves left-before-seen and throughput while worsening median and P90 waits in every demand condition. Under C04, its median wait is 86.671644 minutes worse, so the failed stress result cannot be hidden. S03 provides partial benefits but does not clear the point-demand decision rule. C05 keeps the weaker 0.90 workflow effect visible.

The option ranking depends on what is valued and on the assumed service mechanism. The module therefore carries no option forward as if it were robust. Failed conditions remain part of the release.
