# Training Data Directory

This directory contains all the code to train and test the BERT model

## Scripts

### `my_dataset.py`

This script contains the custom pytorch dataset objects that are used to read in the data in a pytorch dataloader.

#### Results
This script has no results

#### To Run
This is not meant to be run as a standalone script, instead it is loaded in `train.ipynb` and `test.ipynb` and `real_data_testing.ipynb`.

### `train.ipynb`

This script trains the BERT model.

#### Results
- Model checkpoints in `bert/checkpoints`
- `bert/results/bert_training_params.png` - PNG table of training parameters used

#### To Run
Execute `papermill train.ipynb /dev/null` or open the notebook and run each cell individually.  Note, this will take about 1 hour to train the model on an Nvidia RTX 3090.

### `test.ipynb`

This script test the BERT model on split of the data (i.e. train/val/test) as well as each subsplit (i.e. news vs tweets)

#### Results
- `bert/results/bert_results_table.png` - PNG table of results
- `bert/results/bert_results_all_data.csv` - Results of the BERT model applied on all training data splits
- `bert/results/bert_results_news_data.csv` - Results of the BERT model applied on the [NewsMTSC](https://www.kaggle.com/datasets/fhamborg/news-articles-sentiment) portion of the data
- `bert/results/bert_results_twitter_data.csv` - Results of the BERT model applied on the [Sentiment140](https://www.kaggle.com/datasets/kazanova/sentiment140) portion of the data

#### To Run
Execute `papermill test.ipynb /dev/null` or open the notebook and run each cell individually.  Note, this will take about 30 minutes to test the model on an Nvidia RTX 3090.

### `real_data_testing.ipynb`

This script applies the BERT model on the data scraped from the New York Times and Twitter

#### Results
- `bert/results/twitter_bert_results.csv` - Results of the BERT model applied on the scraped Twitter data
- `bert/results/nyt_bert_results.csv` - Results of the BERT model applied on the scraped NYT data

#### To Run
Execute `papermill real_data_testing.ipynb /dev/null` or open the notebook and run each cell individually.  Note, this will take about 10 minutes to test the model on an Nvidia RTX 3090.


