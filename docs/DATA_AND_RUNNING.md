# Data and running

## Local configuration

Absolute Colab and Windows path literals in active retained code are routed through `tradinguni_paths.py`. By default, `data_path(...)` uses `TradingUni/data/`, and `output_path(...)` uses `TradingUni/outputs/`. Both directories are ignored by Git. Original path strings in comments are retained as historical context.

You can point to an existing local data tree instead:

```bash
# Linux/macOS
export TRADINGUNI_DATA_DIR=/absolute/path/to/private/data
export TRADINGUNI_OUTPUT_DIR=/absolute/path/to/private/outputs
# Windows PowerShell
# $env:TRADINGUNI_DATA_DIR = "D:\TradingUniData"
# $env:TRADINGUNI_OUTPUT_DIR = "D:\TradingUniOutputs"
```

The internal subdirectories still mirror the original research layout. [path_map.json](path_map.json) records every redirected literal, including input and output references. It is a reference map, not a list saying every file must be provided in advance. The added setup cell sets the working directory to the repository root, so relative filenames in exploratory code resolve consistently there.

## Important inputs and gaps

| Workflow | Inputs | What is missing from this release |
|---|---|---|
| Trade-to-facts | PAXG aggTrades fields: `aggTradeId`, `timestamp`, `price`, `quantity`, `isBuyerMaker` | Raw PAXG trade files; example-specific timestamp normalization needs review for other exports |
| Market axes / behavior / hypotheses | ETH yearly one-minute aggBars, then phase feature tables | ETH aggBars and generated phase tables |
| Microstructure features | ETH aggBars with trade/activity/flow/sequence facts, not OHLCV alone | Underlying fact data |
| Discrete/continuous climate | Feature tables, `df_q_fixed_L_to_Tree.parquet`, fold prediction files and climate summaries | Several intermediate tables; a tree-table preparation cell is commented out, and fold prediction artifacts are read from prior experiments |
| Barrier-hit models | `df_q_fixed_L_to_Tree.parquet` | Prepared feature table |
| Magnitude/direction | `df_q_fixed_L.parquet` and intermediate prediction tables | Feature table; some predictions are read before a later section writes the same filename |
| Regime baseline | ETH one-minute files for 2020–2025 with `t`, OHLC and `vol_base` | Yearly data; trailing execution/metrics headings are unfinished placeholders |
| All for One | ETH one-minute files for 2020–2025; the initial selection uses `t`, `open`, `high`, `low`, `close` | Yearly data; full experiments may be expensive |

Source references to Binance Vision describe the original data provenance. This repository does not include a verified downloader or rebuild every historical intermediate automatically.

## Shared state after splitting

`notebook_series.json` defines three groups. `run_series.py` concatenates the parts in their original cell order, including the setup cell from part 1. It does not rerun a prerequisite in every part and does not serialize hidden kernel state.

```bash
python scripts/run_series.py all_for_one --export outputs/all_for_one_combined.ipynb
```

Open the exported notebook in Jupyter, review input paths, and execute only the sections whose prerequisites are available. For a fully prepared environment, automatic execution is explicit:

```bash
python scripts/run_series.py all_for_one --export outputs/all_for_one_executed.ipynb --execute
```

This can take a long time and can fail at a missing artifact or an unresolved original research issue. The local export retains execution context on failure. Keep generated notebooks in `outputs/` rather than committing them.

The four data-facts notebooks are separate file-based stages rather than one shared-state series. The PAXG aggregation example is separate from the ETH feature stages. The magnitude/direction notebook is also a separate experiment, not part 3 of the barrier-hit series despite its folder numbering.

## Validation boundaries

`check_repository.py` checks output structure, Python syntax, unique cell provenance and complete series ordering. `run_existing_checks.py` runs six original All for One checks against synthetic data. See [VALIDATION.md](VALIDATION.md) for observed outcomes and known limits.

Dependencies are inferred from imports and are not version-pinned. Restoring the original runtime or resolving library API differences may be necessary for full historical reproduction.
