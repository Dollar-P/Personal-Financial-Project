# Validation for this curated release

Checked on 5 November 2026.

Inspected runtime: Python 3.12.14, NumPy 2.3.5, pandas 2.2.3 and matplotlib 3.10.8. This records the validation environment, not a historical dependency lockfile.

| Check | Observed result |
|---|---|
| Notebook JSON / structure | 15 notebooks parsed successfully |
| Code syntax | 1,453 code cells parsed, including added setup cells |
| Source provenance | All 1,703 original cells from the nine selected notebooks accounted for exactly once |
| Split ordering | Three series preserve complete original cell ordering |
| Historical outputs | 992 original output objects restored to 553 cells with saved outputs, together with original execution counts |
| Composition | All three series exported successfully without executing research |
| Existing All for One synthetic checks | 6 passed |
| Full historical experiments | Not run; datasets and intermediate artifacts excluded |

The six existing checks cover basic as-of alignment, state expiration, Keltner signal logic, regime filter logic, walk-forward fold generation and candidate selection. They run definitions and synthetic inputs from the original notebook; they do not invoke the market-data loader or candidate sweeps.

The check run emitted pandas FutureWarnings about timezone-aware datetime assignment and assigning missing values into boolean columns in original alignment code. The checks passed in the inspected environment. Future pandas releases may require dtype changes; this release does not claim compatibility across untested library versions.

Notebook syntax and cell preservation are source checks. They cannot establish correct future-window construction, absence of leakage throughout exploratory code, reliable execution of every research section, or profitable trading results.
