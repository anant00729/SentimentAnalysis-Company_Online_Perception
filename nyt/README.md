# New York Times Directory

This directory contains all code used to scrape and visualize scraped data from the new york times.

## Scripts

### `nyt.py`

In this script we scrape the news article abstracts from the New York Times.  Note, the required API key
is left in the script for ease of use.  It will be disabled in May 2023.  Users will then need
to replace the API key with their own.

#### Output

This script outputs `nyt/data/Api_data.csv` that contains the abstracts for the scraped news articles.

#### To run
Execute `python nyt.py`

### `scraped_data_results_table.ipynb`

In this jupyter notebook, we produce a png of high level summary table of scraped data from the New York Times in `nyt.py`

#### Output

This notebook outputs `nyt/results/nyt_data.png`.



#### To run
Execute `papermill scraped_data_results_table.ipynb /dev/null` or open the notebook and run each cell individually.
`