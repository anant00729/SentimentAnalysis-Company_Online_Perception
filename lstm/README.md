# Training Data Directory

This directory contains all the code to train and test the LSTM model

## Scripts

### `train.ipynb`

This script trains the LSTM model.

#### Results
- Model checkpoints in `lstm/checkpoints`

#### To Run
Execute `papermill train.ipynb /dev/null` or open the notebook and run each cell individually.  

### `test.ipynb`

This script test the LSTM model on split of the data (i.e. train/val/test) as well as each subsplit (i.e. news vs tweets)

#### Results
- `lstm/results/lstm_results_table.png` - PNG table of results
- `lstm/results/lstm_results_all_data.csv` - Results of the LSTM model applied on all training data splits
- `lstm/results/lstm_results_news_data.csv` - Results of the LSTM model applied on the [NewsMTSC](https://www.kaggle.com/datasets/fhamborg/news-articles-sentiment) portion of the data
- `lstm/results/lstm_results_twitter_data.csv` - Results of the LSTM model applied on the [Sentiment140](https://www.kaggle.com/datasets/kazanova/sentiment140) portion of the data

#### To Run
Execute `papermill test.ipynb /dev/null` or open the notebook and run each cell individually.

### `real_data_lstm_testing.ipynb`

This script applies the LSTM model on the data scraped from the New York Times and Twitter

#### Results
- `lstm/results/twitter_lstm_results.csv` - Results of the LSTM model applied on the scraped Twitter data
- `lstm/results/nyt_lstm_results.csv` - Results of the LSTM model applied on the scraped NYT data

#### To Run
Execute `papermill real_data_testing.ipynb /dev/null` or open the notebook and run each cell individually.  


