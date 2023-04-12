# Training Data Directory

This directory contains all the code to clean and formulate the training data used in this project.

## Scripts

### `clean_tweets.py`

This script reads in the [Sentiment140](https://www.kaggle.com/datasets/kazanova/sentiment140) dataset and performs all cleaning.  To clean the data we
perform the following operations on the tweet sequences:

- Remove links
- Remove words that start with @
- Remove words that start with #
- Remove words that start with & and end with ;, such as &
- Remove brackets around ?
- Replace multiple spaces with a single space
- Remove leading and trailing white space
- Remove substrings that start with a special character. 

The script also adds a new column called "polarity", where -1 represents a negative sentiment, 0 represents a neutral sentiment, and 1 represents a positive sentiment.

#### Results
This script outputs `training_data_formulation/results/tweets.csv` that contains the cleaned version of the data.

#### To Run
Execute `python clean_tweets.py`

### `clean_news.py`

This script reads the [NewsMTSC](https://www.kaggle.com/datasets/fhamborg/news-articles-sentiment) dataset and performs all cleaning.   
perform the following operations on the sequences:

- Remove leading and trailing white space

#### Results
This script outputs `training_data_formulation/results/news.csv` that contains the cleaned version of the data.

#### To Run
Execute `python clean_news.py`


### `data_formulation.ipynb`

This script reads the output of `clean_news.py` and `clean_tweets.py` and randomly samples 4000 sequences from each dataset and merges them together.  The merged
set is then broken into training, testing and validation splits.

#### Results
- `training_data_formulation/results/test_4000.csv` - The test data
- `training_data_formulation/results/train_4000.csv` - The training data
- `training_data_formulation/results/val_4000.csv` - The validation data
- `training_data_formulation/results/val_4000_news.csv` - The portion of data in the validation data that is from the [NewsMTSC](https://www.kaggle.com/datasets/fhamborg/news-articles-sentiment) dataset
- `training_data_formulation/results/train_4000_news.csv` - The portion of data in the training data that is from the [NewsMTSC](https://www.kaggle.com/datasets/fhamborg/news-articles-sentiment) dataset
- `training_data_formulation/results/test_4000_news.csv` - The portion of data in the test data that is from the [NewsMTSC](https://www.kaggle.com/datasets/fhamborg/news-articles-sentiment) dataset
- `training_data_formulation/results/val_4000_tweets.csv` - The portion of data in the validation data that is from the [Sentiment140](https://www.kaggle.com/datasets/kazanova/sentiment140) dataset
- `training_data_formulation/results/train_4000_tweets.csv` - The portion of data in the training data that is from the [Sentiment140](https://www.kaggle.com/datasets/kazanova/sentiment140) dataset
- `training_data_formulation/results/test_4000_tweets.csv` - The portion of data in the test data that is from the [Sentiment140](https://www.kaggle.com/datasets/kazanova/sentiment140) dataset
- `news_stats.png` - PNG table of summary stats of data sampled from the [NewsMTSC](https://www.kaggle.com/datasets/fhamborg/news-articles-sentiment) dataset
- `tweets_stats.png` - PNG table of summary stats of data sampled from the [Sentiment140](https://www.kaggle.com/datasets/kazanova/sentiment140)  dataset
- `split_stats.png` - PNG table of summary stats on the merged training data

#### To Run
Execute `papermill data_formulation.ipynb /dev/null` or open the notebook and run each cell individually.
