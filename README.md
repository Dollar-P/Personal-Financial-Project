# TradingUni

**A quantitative research journey through market microstructure, machine learning, and regime-aware trading.**

> **Central question:** *Can a useful description of current market conditions help explain when a predictive model or trading strategy works?*

TradingUni is my collection of exploratory quantitative research. It starts with **what the market data actually records**, builds features and representations of market behavior, tests hypotheses and predictive targets, and examines how trading-system design and walk-forward evaluation affect the interpretation of historical performance.

This repository is a **curated research archive and educational project—not a verified profitable strategy, investment product, or production trading system**. It preserves original notebook outputs, including inconclusive experiments and historical errors, so the research can be inspected rather than presented as a selection of favorable results.

## Explore the project

| Start here | What you'll find |
|---|---|
| **[Interactive Research Textbook V2.2](docs/index.html)** | Self-contained Thai-language textbook, 13 chapters, formulas, source-linked code walkthroughs, interactive examples, and notebook figures. |
| [13-chapter reading guide](docs/READING_PATH.md) | Recommended path through the research notebooks. |
| [Research process](docs/RESEARCH_PROCESS.md) | Questions, methods, and relationships visible in the source. |
| [Evidence and limitations](docs/EVIDENCE_AND_LIMITATIONS.md) | What the historical results and available validation can—and cannot—establish. |
| [คู่มือโครงการภาษาไทย](docs/PROJECT_GUIDE_TH.md) | Thai-language overview of the curated notebooks. |

**Viewing the textbook:** Download `docs/index.html` and open it in a browser, or enable **GitHub Pages** with `main` → `/docs` to serve it as a website. GitHub's normal repository file view may show the HTML source instead of running the website. See [Publishing & GitHub Pages](docs/PUBLISHING.md). Once published, add your actual Pages URL here; it depends on your repository owner/name.

## Research map

```text
                         MARKET DATA
                         /         \
       PAXG aggregated trades      ETH intraday bars / research tables
             (Phase 0)                       |
                |                             +-------------------+
     Trade events → market facts             |                   |
                |                      Market features      OHLC & timeframes
                |                             |                   |
                |                       Behavioral axes     Regime / indicator
                |                             |                   states
                |                       Hypothesis tests          |
                |                             |              Signals / filters
                |                      Adaptive features          |
                |                             |             Execution / costs
                |                     Discrete / continuous       |
                |                        market climate       Backtesting
                |                             |                   |
                +--- distinct research ------+           Walk-forward research
                             |
                     ML target experiments
               (hit / direction / magnitude)
```

*Conceptual research map, **not** a single verified, automatically executable data pipeline.* The PAXG aggregation example is separate from later ETH-based feature research. The ML and trading branches investigate related questions but are not shown to form one deployed model-to-order system.

## What I investigated

| Research area | Question and implementation | Source |
|---|---|---|
| **Trade events & market facts** | Transform Binance PAXG aggTrades into one-minute bars, including VWAP, activity, directional flow, timing, concentration, sign sequences, sparse-bar gates, and a complete time grid. | [Phase 0](notebooks/data_facts/01_trade_to_facts.ipynb) |
| **Behavioral features** | Express activity, volatility, flow, persistence, concentration, and impact proxies on raw and relative scales; construct rolling flags and temporal behaviors. | [Market axes](notebooks/data_facts/02_market_axes.ipynb) · [Behavior features](notebooks/data_facts/03_behavior_features.ipynb) |
| **Hypothesis testing** | Study feature geometry and H1–H7 while auditing what proposed "forward" outcomes actually measure. | [Geometry & hypotheses](notebooks/data_facts/04_geometry_and_hypotheses.ipynb) |
| **Microstructure & climate** | Explore adaptive windows, discrete market climates, and continuous feature-space methods, including tests affected by sample sparsity. | [Adaptive](notebooks/microstructure/01_features_and_adaptive_windows.ipynb) · [Discrete](notebooks/microstructure/02_discrete_climate_and_models.ipynb) · [Continuous](notebooks/microstructure/03_continuous_climate.ipynb) |
| **Machine learning targets** | Investigate barrier-hit, global versus context-specific, direction, magnitude, and directional-efficiency tasks. | [Barrier hit](notebooks/ml_targets/01_barrier_hit_models.ipynb) · [Context models](notebooks/ml_targets/02_global_vs_context_models.ipynb) · [Magnitude & direction](notebooks/ml_targets/03_magnitude_and_direction.ipynb) |
| **Regime-aware backtesting** | Evaluate rule-based Keltner breakout/mean-reversion ideas under regime and transaction-cost assumptions. | [Regime baseline](notebooks/regime_backtesting/01_regime_baseline.ipynb) |
| **All for One** | Research multi-timeframe states, point-in-time alignment, signals, filters, execution, analytics, and walk-forward candidate selection. | [Data & state](notebooks/all_for_one/01_data_state_alignment.ipynb) · [Execution](notebooks/all_for_one/02_signals_filters_execution.ipynb) · [Analytics](notebooks/all_for_one/03_analytics_and_visualization.ipynb) · [Experiments](notebooks/all_for_one/04_experiments_and_walk_forward.ipynb) |

### Research observations—and why they need qualification

- **Trade-to-facts:** A saved PAXG example shows **39,996 observed one-minute bars** and a **40,320-row complete grid** for January 2026. These are **historical notebook outputs**, not data reprocessed for this release.
- **Discrete climates:** The recorded experiment considered **125 climate combinations**, and none passed all its selection criteria in the historical analysis. Subgroup sample sizes and multiple testing are central concerns; this is **not** a general proof that market context is useless.
- **Predictive labels:** Some Phase 3 helpers use a pattern equivalent to `shift(-1).rolling_mean(window_size=w)`. A trailing rolling window after shifting does **not** cover the intended full future horizon. Consequently, affected H1–H6 results should **not** be presented as validated forward predictive evidence without reimplementation and rerunning.
- **Walk-forward:** All for One includes historical candidate-selection and walk-forward results, but saved performance is not a new independent reproduction, and the selection procedure still requires careful bias and execution review.
- **Code checks:** Six original synthetic tests cover selected alignment, state, signal, filter, fold-generation, and candidate-selection logic. They do **not** validate trading profitability.

For context, source locations, methodological caveats, and detailed explanations, read the [textbook](docs/index.html), particularly its **Research Integrity**, **Chapter 4**, **Chapter 6**, **Chapter 12**, and **Chapter 13** sections.

## Research Textbook — 13 chapters

The textbook is primarily in **Thai** with English technical terms, Python identifiers, equations, interactive demonstrations, and links to individual source cells.

| Part | Chapter | Topic |
|---|---|---|
| Foundations | [01](docs/index.html#ch1) | Understanding TradingUni |
| Foundations | [02](docs/index.html#ch2) | Trade Events → Market Facts |
| Foundations | [03](docs/index.html#ch3) | Market Axes & Behavioral Features |
| Foundations | [04](docs/index.html#ch4) | Geometry & Hypothesis Testing |
| Microstructure | [05](docs/index.html#ch5) | Adaptive Windows |
| Microstructure | [06](docs/index.html#ch6) | Discrete Market Climate |
| Microstructure | [07](docs/index.html#ch7) | Continuous Market Climate |
| ML | [08](docs/index.html#ch8) | Targets, Models & Experiments |
| Trading | [09](docs/index.html#ch9) | Regime-Based Trading Baseline |
| Trading | [10](docs/index.html#ch10) | All for One: Data & State Engines |
| Trading | [11](docs/index.html#ch11) | All for One: Signals, Execution & Analytics |
| Trading | [12](docs/index.html#ch12) | All for One: Experiments & Walk-Forward |
| Synthesis | [13](docs/index.html#ch13) | What Did TradingUni Actually Teach Us? |

The website also contains a searchable **Feature Encyclopedia**, **Models & Algorithms**, **Architecture Explorer**, **Evidence Explorer**, **Mathematical Reference**, and **Source Browser**.

## Repository structure

```text
.
├── README.md
├── docs/
│   ├── index.html               # Self-contained interactive textbook (V2.2)
│   ├── .nojekyll                # Publish the HTML unchanged with GitHub Pages
│   ├── PUBLISHING.md           # Instructions for publishing and updating
│   ├── READING_PATH.md
│   ├── RESEARCH_PROCESS.md
│   ├── EVIDENCE_AND_LIMITATIONS.md
│   ├── DATA_AND_RUNNING.md
│   ├── CURATION.md
│   ├── VALIDATION.md
│   └── ...
├── notebooks/
│   ├── data_facts/             # 4 notebooks
│   ├── microstructure/         # 3 notebook parts
│   ├── ml_targets/             # 3 notebooks
│   ├── regime_backtesting/     # 1 notebook
│   └── all_for_one/            # 4 notebook parts
├── scripts/
│   ├── check_repository.py
│   ├── run_existing_checks.py
│   └── run_series.py
├── notebook_series.json
├── tradinguni_paths.py
└── requirements.txt
```

The curated edition retains **15 notebooks** from **9 selected source notebooks** out of an original collection of 53. Notebook cell outputs are intentionally kept for interpretation, not as evidence of a clean, repeatable run. See [curation](docs/CURATION.md) and [validation](docs/VALIDATION.md).

## Running the repository checks

This repository is primarily a **research archive**, and the original market data and many intermediate Parquet files are **not included**. You can run the structural checks without those datasets.

```bash
python -m pip install -r requirements.txt
python scripts/check_repository.py
python scripts/run_existing_checks.py
```

- `check_repository.py` validates notebook structure, code syntax, original-cell provenance, and split-cell ordering.
- `run_existing_checks.py` runs six original **synthetic logic tests** from All for One. Passing them is **not** a reproduction of historical ML or backtest results.
- The scripts explicitly read UTF-8 files so they work with notebook text containing Thai or other Unicode characters on Windows.

Some notebooks were split for reading but rely on a shared kernel. To combine them in original order **without executing**:

```bash
python scripts/run_series.py microstructure --export outputs/microstructure_combined.ipynb
python scripts/run_series.py barrier_hit --export outputs/barrier_hit_combined.ipynb
python scripts/run_series.py all_for_one --export outputs/all_for_one_combined.ipynb
```

Running the actual research requires the appropriate source data, intermediate artifacts, and environment. See [Data & Running](docs/DATA_AND_RUNNING.md). The dependencies in `requirements.txt` are inferred from imports and are **not a historical lockfile**.

## Research integrity

The project intentionally distinguishes:

| Evidence type | Interpretation |
|---|---|
| **Code-verified** | What the current retained implementation calculates. |
| **Historical output** | What is visible in old notebook output cells; not automatically reproducible. |
| **Documented research note** | A conclusion or concern explicitly recorded in the original notes. |
| **Technical interpretation** | A reasoned explanation, which may need a dedicated empirical test. |
| **Unverified hypothesis / future work** | A question, proposed fix, or result that has not yet been established. |
| **Newly reproduced** | A result rerun and actually verified in the current environment. |

Known challenges include forward-target alignment, temporal state confirmation, shared-kernel dependencies, missing data, overlapping observations, multiple testing, backtest execution assumptions, and selection bias. The website documents these concerns near the corresponding experiments.

This repository is **not financial advice**. No strategy's future profitability is asserted or guaranteed.

---

**TradingUni** · Independent quantitative research · Historical notebooks, transparent evidence, and ongoing methodological improvement.
