# Research process visible in the notebooks

This guide reconstructs the work from source code and original notes. It does not reconstruct personal intentions that were never recorded, and it does not treat old notes as independently verified results.

## 1. Begin with observable market facts

`data_facts/01_trade_to_facts.ipynb` starts from trade-event fields and constructs bar-level price, participation, trade timing, size, signed flow and sequence statistics. Its current example uses PAXG trades. Later ETH notebooks consume a separate set of yearly one-minute bars; this is not a single automatic pipeline from that PAXG example.

The next notebooks organize facts into activity, volatility, flow, persistence, concentration and impact axes. Rolling ranks and fast/slow comparisons explore how to describe conditions relative to recent history rather than relying entirely on absolute thresholds.

## 2. Make an interpretation testable

`data_facts/04_geometry_and_hypotheses.ipynb` connects feature groups to hypotheses about subsequent activity, volatility, flow and other behavior. For example, the activity hypothesis asks whether high-activity conditions are followed by a higher participation distribution. It explicitly records what it would mean if the expected effect is absent.

This offers a concrete portfolio narrative: define the feature, state the expected behavior, specify a comparison, then assess the evidence. Future-window calculations and overlapping observations still need review before inferential claims.

## 3. Ask separate prediction questions

Microstructure and ML notebooks distinguish whether a price barrier is hit, which direction is reached, how large a movement may be, and whether a move has directional efficiency. CatBoost experiments and time-based folds explore these targets. Drift-based partitions and clustering are additional alternatives, not interchangeable definitions of market regimes.

The useful implementation detail is the target design: movement opportunity and direction need not be the same prediction task. No relative predictive benefit is claimed here without rerunning the evaluation.

## 4. Reconsider the context representation

The discrete-climate work explores bins, context groupings and model behavior within those groups. Original notes near the end of `microstructure/02_discrete_climate_and_models.ipynb` identify small subgroup sample sizes and failure under the chosen FDR procedure.

The following part explores robust scaling, PCA and neighborhood-based estimates in a continuous space. That transition is evidence of a change in experimental approach. It does not prove that the continuous alternative solved the statistical problem. In particular, the final R1 neighborhood visualizations include each query point among its own neighbors; they are exploratory in-sample views, not out-of-sample prediction evidence.

## 5. Connect research components into a trading simulation

All for One combines OHLC validation, multiple timeframes, persistent IMOM/IMACD states, availability-time alignment, Keltner signals, regime gates, fills, fees, slippage and performance attribution. Its final part includes candidate matrices and walk-forward selection.

Existing synthetic checks cover basic alignment, state expiration, signal logic, regime gates, fold generation and candidate selection. These checks can be run without the historical dataset. The broader strategy still needs a data-backed audit and rerun before making performance claims.

## Questions left open

- Do context effects persist in genuinely held-out periods after accounting for multiple comparisons?
- Are subgroup estimates supported by enough independent observations?
- Do model improvements survive fees, slippage and execution timing?
- Are all future targets constructed correctly, and are transformations fit on training data only?
- How sensitive are the findings to lookback windows, asset, timeframe and market period?

These are next research questions, not claims that the source has already answered them.
