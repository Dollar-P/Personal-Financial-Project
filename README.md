# TradingUni

Research notebooks exploring how market context relates to future price behavior, model performance and trading strategies.

The central question is: **Can a useful description of current market conditions help explain when a model or strategy works?** The work spans trade aggregation, feature construction, hypothesis testing, context-aware machine learning and regime-filtered backtesting.

This is a curated research repository. It contains source code and original research notes. Saved notebook outputs and execution counts are preserved from the original notebooks. Standalone market datasets, result files, checkpoints and alternate implementations are excluded. The saved outputs reflect historical runs, including any errors from those runs.

## Start reading

| Start here | What it shows |
|---|---|
| [Research process](docs/RESEARCH_PROCESS.md) | The questions, experiments and decisions visible in the source |
| [Project guide in Thai](docs/PROJECT_GUIDE_TH.md) | A short reminder of what each area does |
| [Feature hypotheses](notebooks/data_facts/04_geometry_and_hypotheses.ipynb) | Turning feature interpretations into testable statements |
| [Discrete climate research](notebooks/microstructure/02_discrete_climate_and_models.ipynb) | Context bins, target design and original notes on statistical limitations |
| [Continuous climate research](notebooks/microstructure/03_continuous_climate.ipynb) | PCA, neighborhood estimates and temporal stability exploration |
| [All for One](notebooks/all_for_one/01_data_state_alignment.ipynb) | A system combining data validation, states, time alignment, signals, execution and evaluation |

## Repository map

| Folder | Contents |
|---|---|
| `notebooks/data_facts/` | 4 notebooks: trade events → facts → market axes → behavior features → hypotheses |
| `notebooks/microstructure/` | 3 consecutive parts: features/adaptive windows, discrete climate/models, continuous climate |
| `notebooks/ml_targets/` | 2 consecutive barrier-hit parts and 1 separate magnitude/direction notebook |
| `notebooks/regime_backtesting/` | 1 readable baseline implementation |
| `notebooks/all_for_one/` | 4 consecutive parts of the integrated research system |
| `docs/` | Research guide, data requirements, selection decisions and source provenance |
| `scripts/` | Source validation, notebook composition and existing synthetic checks |

Nine source notebooks were selected from 53 originals and organized into 15 smaller notebooks. [The inventory](docs/NOTEBOOK_INVENTORY.md) records a decision for every original file. [Curation notes](docs/CURATION.md) explain the edits and split boundaries.

## Setup and checks

Python 3.10 or newer is required by the included utility scripts. No historical dependency lockfile was available; `requirements.txt` lists imports inferred from the retained source.

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python scripts/check_repository.py
python scripts/run_existing_checks.py
```

The first check needs only Python's standard library. The synthetic checks load definitions from All for One and do not load market data. Neither establishes trading performance.

## Reading and running split notebooks

Parts within a series share variables and definitions. Separate notebook tabs normally use separate kernels. For interactive work, compose the series into one local notebook in the original cell order:

```bash
python scripts/run_series.py all_for_one --export outputs/all_for_one_combined.ipynb
python scripts/run_series.py microstructure --export outputs/microstructure_combined.ipynb
python scripts/run_series.py barrier_hit --export outputs/barrier_hit_combined.ipynb
jupyter lab
```

Open the exported notebook, then inspect/configure its inputs before running cells. Composition does not run code. Optional `--execute` runs the composed notebook in one fresh kernel after its inputs are available.

**Full historical runs require local datasets and several intermediate research artifacts that are not included.** Some upstream steps are commented out in the original work. See [data and running](docs/DATA_AND_RUNNING.md) for the gaps and path configuration.

## Scope of conclusions

The code contains time-based splits, purge/embargo logic in ML experiments, point-in-time alignment checks, baseline comparisons, fees/slippage and walk-forward candidate selection. Their presence shows the intended evaluation approach; it does not establish that every exploratory section is free of leakage or that a strategy is profitable. The continuous-climate sections include in-sample exploratory visualizations as well as separate stability experiments.

Saved outputs document historical runs. They were not regenerated or independently validated for this edition.
