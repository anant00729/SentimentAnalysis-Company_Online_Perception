# Twitter Directory

This directory contains all code used to scrape and visualize scraped data from Twitter.

## Scripts

### `twitter.py`

In this script we scrape tweets relating to target companies from Twitter from the previous seven days.  Note, the API
key has been left for ease of use.  This will be removed in May 2023

#### Output

This script outputs `twitter/data/<twitter handle>_tweets.csv` that contains scraped tweets for the target company.

#### To run
Execute `python twitter.py <twitter handle>`.  The script requires the twitter handle of the target company to be passed as a
command line arguement.  For instance, `python twitter.py FTX` will scrape the tweets relating to the twitter handle `FTX`.  Note, running this script
often requires a 10 to 15 minutes cool down period between runs so as not to exceed the Twitter API rate limit.

### `scraped_data_cleaning.ipynb`

In this jupyter notebook, we read in the scraped data from both the Twitter API (`twitter.py`) and Selenium (`scraper.py`), clean it, and merge them together
into a single dataset.  Several summaries are produced as well.

#### Output

- `twitter/results/<twitter handle>_tweets_cleaned.csv` - The cleaned version of the data from the Twitter API for each target company.
- `twitter/results/tweet_with_replies_all_cleaned.csv` - The cleaned version of the data scraped from Twitter using Selenium.
- `twitter/results/results/twitter_scraped_cleaned.csv` - The merged version of `twitter/results/<twitter handle>_tweets_cleaned.csv` and `twitter/results/tweet_with_replies_all_cleaned.csv` where all duplicate tweets has been removed.
- `twitter/results/twitter_data_merged.png` - PNG of a table that contains the counts of the Tweets scraped from both sources.  This is used in the final report.
- `twitter/results/twitter_cleaned.csv` - PNG of a table that contains the counts of the tweets for each target company in `twitter/results/results/twitter_scraped_cleaned.csv`.  This is used in the final report.

#### To run
Execute `papermill scraped_data_cleaning.ipynb /dev/null` or open the notebook and run each cell individually.  Note, this notebook can take around 10 minutes to run.