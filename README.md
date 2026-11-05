# TradingUni

**Exploring market behavior, predictive modeling, and regime-aware trading through quantitative research.**

TradingUni is a collection of my research notebooks on a central question:

> **Can a useful description of current market conditions help explain when a model or trading strategy works?**

Instead of starting and ending with a trading signal, this project investigates what can be observed from market data, how those observations can be represented as features or market contexts, whether they help predict future behavior, and whether any predictive relationship survives a realistic trading simulation.

**Project status:** Curated research archive / ongoing investigation — **not** a verified profitable trading system. This repository preserves selected code, notes, charts, and historical notebook outputs, including inconclusive results and errors. The original market datasets and large intermediate artifacts are not included.

## The research at a glance

```text
                     Observed market data
                              |
               Trade events / time-series bars
                              |
                  Market facts & features
                              |
                 +------------+-------------+
                 |            |             |
         Behavior &      Predictive      Trading systems
         market context  modeling        & backtesting
                 |            |             |
         Hypotheses,     Targets,        Signals, states,
         state geometry  temporal tests  fills, costs
                 |            |             |
                 +------------+-------------+
                              |
                   Evidence & limitations
```

This is a **conceptual map**, not a claim that every notebook is an automatically runnable pipeline. For example, the trade-to-facts example uses PAXG aggregated trades, while several later investigations use separately prepared ETH one-minute data and intermediate research tables.

### Research directions

| Area | Question | Start here |
|---|---|---|
| **Trade data & market facts** | What happened *inside* a price bar beyond OHLCV? | [Trade events → facts](notebooks/data_facts/01_trade_to_facts.ipynb) |
| **Behavioral features** | How can activity, volatility, flow, persistence, concentration, and impact be measured? | [Market axes](notebooks/data_facts/02_market_axes.ipynb) |
| **Hypothesis testing** | Do interpretations of these features correspond to subsequent market behavior? | [Geometry & hypotheses](notebooks/data_facts/04_geometry_and_hypotheses.ipynb) |
| **Market context** | Should market conditions be represented as discrete states or a continuous space? | [Discrete](notebooks/microstructure/02_discrete_climate_and_models.ipynb) / [continuous](notebooks/microstructure/03_continuous_climate.ipynb) climate |
| **Machine learning** | Are barrier hits, direction, magnitude, and directional efficiency distinct prediction problems? | [ML targets](notebooks/ml_targets/01_barrier_hit_models.ipynb) |
| **Trading research** | How do regimes, timing, costs, and walk-forward selection affect strategy evaluation? | [Regime baseline](notebooks/regime_backtesting/01_regime_baseline.ipynb) / [All for One](notebooks/all_for_one/01_data_state_alignment.ipynb) |

## What this repository demonstrates

The focus is the *research process*, including its uncertainties, rather than a single headline return:

- **From events to measurable facts.** Build time-bar price, trade-timing, signed-flow, trade-size, and trade-sequence statistics from aggregated trade records, with explicit data-quality rules.
- **From intuition to testable hypotheses.** Define what a feature group is expected to explain, and what observations would challenge that interpretation.
- **From fixed labels to context representations.** Explore adaptive windows, discrete market climates, and continuous feature-space neighborhoods; document statistical and sample-size limitations.
- **Separate prediction tasks.** Investigate barrier-hit, direction, and magnitude targets rather than conflating price movement with trading profit.
- **Evaluate strategies as systems.** Combine multi-timeframe indicators, availability-time alignment, Keltner-based signals, fees, slippage, performance analytics, and walk-forward candidate selection.

**A few particularly useful reading points:**

1. [Feature hypotheses](notebooks/data_facts/04_geometry_and_hypotheses.ipynb): turn a behavioral interpretation into a condition, expected observation, and potential falsification.
2. [Discrete climate](notebooks/microstructure/02_discrete_climate_and_models.ipynb): original notes describe small subgroup samples and an unsuccessful result under the chosen false-discovery-rate procedure. This is not evidence that the proposed contexts are predictive.
3. [Continuous climate](notebooks/microstructure/03_continuous_climate.ipynb): explores another representation, including in-sample neighborhood views; it does not establish that continuous climates solve the earlier statistical problem.
4. [All for One](notebooks/all_for_one/01_data_state_alignment.ipynb): a more integrated research system with basic synthetic checks for timing, signals, filters, and selection logic. Passing these checks does not validate historical trading returns.

## Reading guide

If you are new to the repository, read in this order:

1. **[Research learning path — 13 chapters](docs/READING_PATH.md)** for the full narrative, from trade events to walk-forward experiments.
2. **[Research process](docs/RESEARCH_PROCESS.md)** for the methodology and decisions visible in the source.
3. **[Research evidence & limitations](docs/EVIDENCE_AND_LIMITATIONS.md)** to distinguish implementation, historical output, and supported conclusions.
4. **[คู่มือภาษาไทย](docs/PROJECT_GUIDE_TH.md)** for a shorter Thai-language map of the project.

Additional technical references: [data & running](docs/DATA_AND_RUNNING.md), [notebook inventory](docs/NOTEBOOK_INVENTORY.md), [curation decisions](docs/CURATION.md), and [validation notes](docs/VALIDATION.md).

## Repository structure

```text
TradingUni/
├── README.md
├── docs/
│   ├── READING_PATH.md
│   ├── RESEARCH_PROCESS.md
│   ├── EVIDENCE_AND_LIMITATIONS.md
│   ├── PROJECT_GUIDE_TH.md
│   ├── DATA_AND_RUNNING.md
│   ├── CURATION.md
│   ├── NOTEBOOK_INVENTORY.md
│   ├── VALIDATION.md
│   ├── path_map.json
│   └── source_map.json
├── notebooks/
│   ├── data_facts/          # 4 notebooks
│   ├── microstructure/      # 3 consecutive notebook parts
│   ├── ml_targets/          # 2 consecutive parts + 1 separate notebook
│   ├── regime_backtesting/  # 1 baseline notebook
│   └── all_for_one/         # 4 consecutive notebook parts
├── scripts/                 # structural checks, synthetic checks, series composer
├── notebook_series.json
├── tradinguni_paths.py
└── requirements.txt
```

The release selects **9 source notebooks from 53 originals**, organized into **15 curated notebooks**. Saved outputs are kept intentionally because they help readers follow the original experiments. Some outputs reflect stale kernel state or historical errors. See [curation](docs/CURATION.md) and [validation](docs/VALIDATION.md).

## Running the code

Python **3.10+** is expected by the included utility scripts. Dependencies are inferred from retained imports; this is **not** a historical lockfile.

```bash
python -m venv .venv
# Linux / macOS:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt
python scripts/check_repository.py
python scripts/run_existing_checks.py
```

`check_repository.py` checks notebook structure, source provenance, syntax, and split ordering. `run_existing_checks.py` exercises **six existing synthetic tests** of All for One's core logic; it does not load market data or reproduce investment results.

Some notebook series were split for readability but retain their shared variables. To reconstruct a series in its original order:

```bash
python scripts/run_series.py microstructure --export outputs/microstructure_combined.ipynb
python scripts/run_series.py barrier_hit --export outputs/barrier_hit_combined.ipynb
python scripts/run_series.py all_for_one --export outputs/all_for_one_combined.ipynb
```

Exporting **does not execute** the notebooks. Open the resulting file in Jupyter after configuring its data dependencies. A full historical run requires datasets and intermediate files excluded from this public repository; see [Data & Running](docs/DATA_AND_RUNNING.md).

## Research integrity & reproducibility

- **Preserved historical outputs are not independently reproduced results.** Some execution counts and cell states reflect exploratory work.
- **Implementation is not evidence of predictive power.** Temporal splits, purging/embargo, regime labels, and backtesting code must still be assessed in the context of their actual experiments.
- **Exploratory and out-of-sample results are not interchangeable.** In particular, some neighborhood visualizations use the query points themselves as neighbors.
- **Synthetic checks do not establish profitability.** Performance also depends on data quality, execution assumptions, selection bias, and unseen market periods.

See the [evidence ledger](docs/EVIDENCE_AND_LIMITATIONS.md) and [validation record](docs/VALIDATION.md) for more detail.

## Documentation in progress

A longer **interactive research textbook** is planned to explain the notebooks, features, models, formulas, experiments, and decisions in depth. It will be linked here when the HTML artifact is ready and reviewed. This repository already contains the original research notebooks and a source-grounded reading path.

---

*Personal research and education. Nothing here is investment advice or a claim of a live, deployable trading strategy.*
