# Research evidence and limitations

This page records what the curated repository can substantiate **without claiming a complete reproduction of the historical research**. Read it together with the [research process](RESEARCH_PROCESS.md), [validation record](VALIDATION.md), and the notebook outputs themselves.

## Evidence categories

| Label | Meaning | How to use it |
|---|---|---|
| **Implemented** | The code expresses a computation, system component, or evaluation procedure. | Shows what was built, not whether it performs well. |
| **Historical output** | Tables, plots, messages or exceptions retained from an earlier notebook run. | Evidence of a saved run; inputs and execution state may not be reproducible from this release. |
| **Recorded interpretation** | A conclusion or concern written in the original research notes. | Attribute it to the original notes, and inspect the supporting experiment. |
| **Synthetic-check pass** | Existing tests of specific All for One behavior pass on constructed inputs. | Supports narrowly scoped logic only; no price data or investment outcomes. |
| **Exploratory / inconclusive** | An analysis or comparison that does not establish an out-of-sample effect. | Useful for generating and revising hypotheses; not a claim of predictive edge. |
| **Not reproduced** | A full data-driven run was not performed for this curated edition. | Do not advertise verified performance. |

## Study-level evidence ledger

| Area | What the repository contains | Important caveat |
|---|---|---|
| **Data facts** | Implementation of PAXG trade aggregation; saved shapes, examples and intermediate results. | Raw PAXG dataset excluded; gaps and time-unit handling rely on assumptions; saved cell state can differ across runs. |
| **Market axes & behavior** | Computations using activity, volatility, flow, persistence, concentration and impact, with saved exploratory outputs. | Later phases use ETH-derived files that are not generated end-to-end by the included PAXG example. |
| **Feature hypotheses** | Explicit hypotheses (including H1–H7) and original analyses of subsequent market behavior. | Multiple testing, overlap in future windows and data-dependency details require review before confirmatory inference. |
| **Adaptive microstructure** | Feature construction, rank/ECDF operations, temporal representations and original plots. | Intermediate fact/feature data excluded; output values are historical. |
| **Discrete climate** | Context grouping, predictive/proto-payoff experiments and written limitations. | Original notes identify small subgroup samples and a non-passing result under the chosen FDR method; no validated context-based edge is claimed. |
| **Continuous climate** | Robust scaling/PCA, neighborhood estimates and temporal exploration. | Certain local-neighborhood views include the query point among its neighbors: in-sample diagnostic, not future prediction validation. |
| **ML targets** | Barrier-hit, global-vs-context, magnitude/direction experiments, temporal evaluation code and outputs. | Intermediate tables/predictions missing; targets differ; do not infer a model's deployable performance from saved metrics alone. |
| **Regime baseline** | Multi-timeframe and Keltner/regime backtest implementation with some saved outputs. | The source has unfinished trailing analysis areas and a preserved historical error; performance is not independently reproduced. |
| **All for One** | Data/state alignment, signals, execution-cost logic, analytics, candidate experiments and walk-forward selection. | Six synthetic checks test specific logic; full experiments require ETH data and need a further performance/leakage audit. |

## Findings worth reading carefully

### Hypothesis design is explicit

`notebooks/data_facts/04_geometry_and_hypotheses.ipynb` records expected relationships between feature groups and future behavior. This is evidence of *test formulation*. It is not, by itself, proof that all proposed relationships hold.

### Discrete climate exposes a sample-size / multiple-testing problem

The original notes in `notebooks/microstructure/02_discrete_climate_and_models.ipynb` discuss small subgroup samples and failure under the selected false-discovery-rate procedure. This is a useful negative or inconclusive result and should not be hidden to make the portfolio look more successful.

### Continuous climate is an alternative under exploration

`notebooks/microstructure/03_continuous_climate.ipynb` explores geometry and neighborhoods instead of relying exclusively on discrete context bins. Some plots are in-sample, and the source does not establish a conclusive out-of-sample advantage over the discrete approach.

### Testing infrastructure has a deliberately narrow scope

The repository includes six synthetic checks of All for One: as-of alignment, state expiration, Keltner signals, regime filters, fold generation and candidate selection. They do not exercise a complete historical strategy run or confirm profitability.

## Reproducibility constraints

1. **Missing source and intermediate data.** Raw PAXG aggTrades, ETH yearly bars, feature tables, fold predictions and some result artifacts are excluded.
2. **Preserved kernel history.** Execution counts and saved outputs need not represent a clean sequential run. Several historical exceptions are kept, not concealed.
3. **Notebook composition.** Three source notebooks were split for reading while retaining shared variables; use `scripts/run_series.py` before attempting continuous execution.
4. **Dependency versions.** `requirements.txt` is inferred, not locked to a fully reproduced historical environment.
5. **Research-validity questions.** Cross-validation code, purging/embargo logic and point-in-time alignment are valuable but do not imply zero leakage across every exploratory experiment.
6. **Economic conclusions.** Profitability depends on execution timing, cost assumptions, strategy selection and fresh evaluation periods. Those claims remain unverified here.

## Before quoting a historical result publicly

- Identify the exact notebook, cell/output, dataset and prediction/strategy target.
- Check whether the metric is in-sample, validation or genuinely held-out.
- Inspect whether labels overlap, and whether any transformation was fit using future information.
- Specify transaction costs for strategy results.
- State the number of evaluated candidates and the selection procedure.
- Distinguish the number **visible in the saved output** from one **reproduced in a fresh run**.

## What should be tested next

These are proposed tests, **not completed results**:

- Regenerate source and intermediate datasets with explicit coverage checks and stable schemas.
- Re-run each major hypothesis with a clearly declared temporal split and multiple-testing protocol.
- Compare context representations on truly held-out periods, with no query-point/self-neighbor contamination.
- Review point-in-time availability and future-label construction end to end.
- Evaluate sensitivity to trading costs, market regimes, lookback windows and asset/timeframe changes.
- Record experiment configuration, seeds, data versions and outputs in a reproducible manifest.
