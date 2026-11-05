# TradingUni reading path — 13 chapters

This is a **learning and navigation guide** to the selected notebooks, not a claim that the files form one continuously executable project. The order below is a recommended conceptual progression. Original chronological decisions are not always recoverable from notebook metadata.

## How to read a chapter

For each notebook, look for six things:

1. **Question:** What behavior or prediction is being investigated?
2. **Inputs:** Which asset, timeframe, raw fields, and intermediate data are required?
3. **Method:** What exactly is calculated or trained?
4. **Evidence:** Which saved outputs or tests are actually present?
5. **Limitations:** What is unresolved (e.g., missing data, leakage, sample size, selection effects)?
6. **Connection:** Which research question should be examined next?

A notebook output is **historical evidence of a run**, not confirmation that its result was independently reproduced for this release.

## Part I — Market facts and research hypotheses

### Chapter 1 — Project map and research questions

**Start:** [README](../README.md) · [research process](RESEARCH_PROCESS.md)

- Central question: can market context explain when models or trading rules work?
- Separate market description, prediction and trading profitability.
- Understand the distinct PAXG trade-aggregation example and later ETH studies.
- Review notebook dependencies and scope before drawing cross-study conclusions.

### Chapter 2 — Trade events → market facts (Phase 0)

**Notebook:** [01_trade_to_facts.ipynb](../notebooks/data_facts/01_trade_to_facts.ipynb)

- Read PAXG aggregated trades and normalize timestamps/schema.
- Derive OHLC, VWAP, activity, buy/sell signed flow, trade timing, trade-size concentration, realized variation and trade-sign sequences.
- Understand thresholds for sparse bars, a complete one-minute time grid, and no-trade / missing heuristics.
- **Key caution:** aggregated records are not individual investors' orders; the timestamp/gap heuristics are dataset-specific.

### Chapter 3 — Market axes and behavioral features (Phases 1–2)

**Notebooks:** [02_market_axes](../notebooks/data_facts/02_market_axes.ipynb) · [03_behavior_features](../notebooks/data_facts/03_behavior_features.ipynb)

- Organize measurements into activity, volatility, flow, persistence, concentration and impact.
- Study relative ranks, temporal behavior, and fast/slow comparisons.
- Trace each feature to its actual input columns and lookback logic.
- **Key caution:** an interpretable feature name is not proof of the intended economic mechanism.

### Chapter 4 — Geometry and testable hypotheses (Phase 3)

**Notebook:** [04_geometry_and_hypotheses.ipynb](../notebooks/data_facts/04_geometry_and_hypotheses.ipynb)

- Explore feature distributions and their temporal structure.
- Read the recorded H1–H7 hypotheses, their conditions and potential falsification criteria.
- Distinguish observed effects from statistical claims requiring additional checks.
- **Key caution:** overlapping future windows and multiple testing can exaggerate apparent evidence.

## Part II — Market microstructure and context

> The following three parts were split from one original `Micro Structure.ipynb` notebook. They share variables and should be composed before a fresh full-series run.

### Chapter 5 — Adaptive windows and microstructure features

**Notebook:** [01_features_and_adaptive_windows.ipynb](../notebooks/microstructure/01_features_and_adaptive_windows.ipynb)

- Examine adaptive lookback constructions, empirical ranks, smoothing, slopes and event flags.
- Connect each measurement to the intended behavior rather than treating it as an automatic signal.

### Chapter 6 — Discrete market climate and predictive models

**Notebook:** [02_discrete_climate_and_models.ipynb](../notebooks/microstructure/02_discrete_climate_and_models.ipynb)

- Understand context bins, target construction, model evaluation, and subgroup comparisons.
- Pay particular attention to the recorded issues with small subgroup samples and the chosen FDR evaluation.
- **Key caution:** subgroup performance and attractive in-sample charts are not sufficient out-of-sample evidence.

### Chapter 7 — Continuous market climate

**Notebook:** [03_continuous_climate.ipynb](../notebooks/microstructure/03_continuous_climate.ipynb)

- Study robust scaling, PCA, neighborhood estimates and temporal stability.
- Compare this representation to discrete bins as a *research alternative*, not an established improvement.
- **Key caution:** some neighborhood plots include the query observation itself, so they are exploratory in-sample diagnostics.

## Part III — Prediction tasks

### Chapter 8 — Machine learning targets and comparisons

**Notebooks:** [01_barrier_hit_models](../notebooks/ml_targets/01_barrier_hit_models.ipynb) · [02_global_vs_context_models](../notebooks/ml_targets/02_global_vs_context_models.ipynb) · [03_magnitude_and_direction](../notebooks/ml_targets/03_magnitude_and_direction.ipynb)

- Separate barrier-hit, direction, magnitude and directional efficiency questions.
- Read CatBoost experiments, time-based folds, purging/embargo and global-vs-context comparisons where implemented.
- **Key caution:** movement probability, direction accuracy, and profitable trading are different claims; some intermediate model artifacts are missing.

> The first two ML target notebooks are consecutive parts of `Test_Hit.ipynb`; the third is a separate original notebook (`Energy.ipynb`).

## Part IV — Strategy engineering and evaluation

### Chapter 9 — Regime-based backtesting baseline

**Notebook:** [01_regime_baseline.ipynb](../notebooks/regime_backtesting/01_regime_baseline.ipynb)

- Study multi-timeframe inputs, regime labels, Keltner-based trading rules and execution assumptions.
- Review the original saved outputs and unfinished sections before interpreting performance.

> The next three chapters cover four consecutive parts split from `ALL_FOR_ONE.ipynb`.

### Chapter 10 — All for One: data, states and timing

**Notebook:** [01_data_state_alignment.ipynb](../notebooks/all_for_one/01_data_state_alignment.ipynb)

- Read input checks, multi-timeframe state construction, IMOM/IMACD and availability-time alignment.
- Understand what the as-of and state-expiration synthetic checks do and do not prove.

### Chapter 11 — All for One: signals, execution and analysis

**Notebooks:** [02_signals_filters_execution](../notebooks/all_for_one/02_signals_filters_execution.ipynb) · [03_analytics_and_visualization](../notebooks/all_for_one/03_analytics_and_visualization.ipynb)

- Trace signal → regime filter → execution → costs → trades → equity and risk metrics.
- Compare code assumptions with any preserved plotted results.

### Chapter 12 — All for One: experiments and walk-forward selection

**Notebook:** [04_experiments_and_walk_forward.ipynb](../notebooks/all_for_one/04_experiments_and_walk_forward.ipynb)

- Examine candidate definitions, parameter combinations, time-based selection and evaluation.
- Watch for selection bias and train/test instability; do not pick a 'winner' based solely on the largest historical return.

## Part V — Research retrospective

### Chapter 13 — What the project establishes and what remains open

**Sources:** [research process](RESEARCH_PROCESS.md) · [evidence and limitations](EVIDENCE_AND_LIMITATIONS.md) · [validation](VALIDATION.md)

- Summarize source-backed findings, negative/inconclusive observations and the limits of reproducibility.
- Separate completed engineering from validated economic conclusions.
- Identify next experiments: independent held-out tests, threshold/feature sensitivity, leakage audits and execution-cost robustness.

## Notebook execution note

Split notebook parts are **reading boundaries**, not standalone executables. See [data and running](DATA_AND_RUNNING.md) and `scripts/run_series.py` for composition and local input configuration. Do not execute the full collection against missing datasets and treat resulting errors as a completed reproducibility check.
