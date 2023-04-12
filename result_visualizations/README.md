# Training Data Directory

This directory contains all the produce the visualizations of the LSTM and BERT models applied on the scraped data.

## Scripts

### `viz.ipynb`

This notebook generates the visualizations of the LSTM and BERT models when applied on the scraped Twitter and NYT data.

#### Results
- `result_vizualizations/results/lstm_initial_twitter_summary_result.png` - High Level summary of the LSTM model applied on the scraped Twitter data
- `result_vizualizations/results/bert_initial_twitter_summary_result.png` - High Level summary of the BERT model applied on the scraped Twitter data
- `result_vizualizations/results/timeseries_distribution_grid.png` - Visualisation of results of both BERT/LSTM applied on scraped Twitter data over time
- `result_vizualizations/results/distribution_grid.png` - Visualisation of results of both BERT/LSTM applied on scraped Twitter data as a distribution
- `result_vizualizations/results/nyt_timeseries_distribution_grid.png` - Visualisation of results of both BERT/LSTM applied on scraped NYT data over time
- `result_vizualizations/results/nyt_distribution_grid.png` - Visualisation of results of both BERT/LSTM applied on scraped NYT data as a distribution
- `result_vizualizations/results/lstm_initial_nyt_summary_result.png` - High Level summary of the LSTM model applied on the scraped NYT data
- `result_vizualizations/results/bert_initial_nyt_summary_result.png` - High Level summary of the BERT model applied on the scraped NYT data
 
#### To Run
Execute `papermill viz.ipynb /dev/null` or open the notebook and run each cell individually.