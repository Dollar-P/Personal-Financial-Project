# Curation decisions

## Selection

The original nested archives contain 53 notebooks: 18 automatic checkpoints, 5 non-checkpoint files under `old_version`, and 30 others (including drafts and alternative variants). Nine source notebooks were selected. Splitting three of them produces 15 notebooks in this repository.

The retained paths cover facts/features/hypotheses, microstructure context research, hit/magnitude targets, a readable regime baseline, and All for One. Selection does not imply that omitted asset variants or experiments were byte-for-byte duplicates. The [full inventory](NOTEBOOK_INVENTORY.md) states the reason for every omission.

Standalone `backtest.py`, six supplementary PDF/DOCX design documents, nested ZIPs, the Parquet dataset, result CSV and temporary lock file are omitted from this focused notebook collection. Their originals remain in the source ZIP.

## Split boundaries

Ranges below use zero-based original cell indices, inclusive.

| Original | Curated sections | Cell ranges |
|---|---|---|
| `Micro Structure.ipynb` | Features/adaptive windows; discrete climate/models; continuous climate | 0–196; 197–430; 431–556 |
| `Test_Hit.ipynb` | Hit models/diagnostics; global-versus-context models | 0–197; 198–249 |
| `ALL_FOR_ONE.ipynb` | Data/state/alignment; signals/filter/execution; analytics/visualization; combined experiments | 0–49; 50–131; 132–198; 199–343 |

No original cell is dropped from a selected notebook. Cells remain in their original order. Original empty/comment-only cells remain to preserve references; new introductions explain what each file contains. These are reading boundaries, not independent program modules. The composition script restores one-kernel execution order.

## Source edits

1. Retain original cell outputs and execution counts in this edition. Notebook/runtime metadata stays curated.
2. Add introductory scope, status and prerequisite notes; add a repository-path setup cell to each independent notebook or first series part.
3. Replace absolute path string literals with `data_path` / `output_path` calls. Keep relative paths and commented historical paths intact.
4. Replace inline `!pip install polars/catboost` cells with comments pointing to `requirements.txt`.
5. Fix one concrete configuration typo in All for One original cell 251: add the missing comma between `"15min"` and `"1h"`. Python previously concatenated them into `"15min1h"`.

No model target, strategy formula, parameter sweep or statistical conclusion is intentionally changed. Other original issues may remain; this is a curated research source release, not a general rewrite or validation of the research.

[source_map.json](source_map.json) records each retained original cell's source hash, curated hash, destination and all source edit locations. It allows later comparison with the original ZIP without publishing duplicate notebooks.

## Preparing GitHub

Extract the ZIP and upload the contents of its `TradingUni/` folder as the repository root. Keep the original source ZIP separately. The README is the entry point; the Thai guide is a reminder for the author. Data/results are ignored, but `.gitignore` does not remove files already tracked in a different existing repository.

No license was selected on the author's behalf, and no GitHub repository was created or published as part of this packaging task.
