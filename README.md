# Output README

If you are opening output.zip, this zip file contains all outputs of all scripts in the project.
If you would like to regenerate the output, please download the source code of this project (i.e. source.zip)
and refer to the `Project README` section below.

# Project README

This repository contains the code for the project for CMPT 713 at Simon Fraser University.  To read the project report, please 
see `report.pdf`.  For code documentation, please see `project.ipynb` that contains details on the prerequisites for
running this repository and the structure of this repository.  To reproduce the figures and results in `report.pdf`
please first read `project.ipynb` so that you understand the structure of this repository, then see
`output.ipynb` that contains detailed instructions and code for reproducing the results.

This repository contains several surface level scripts that are:
- `download_models.py` - This script is used in both `project.ipynb` and `output.ipynb` and downloads the trained models for this project from Google Drive.
- `download_output.py` - This script is used in both `project.ipynb` and `output.ipynb` and downloads the data and results for this project from Google Drive.
- `zip_output.py` - This script zips the data and results for this project so that users can download it at a later date.
- `project.ipynb` - Documentation on the prerequisites and structure of this repository.
- `output.ipynb` - Documentation and code to reproduce the results shown in `report.pdf`.
- `chrome-extension` - The documentation and code demonstrate the usage of a BERT model to perform real-time sentiment analysis through a Chrome extension.

# Contributions

Aidan Vickars

    - Cleaned and standardized Sentiment 140 and NewsMTSC datasets
    - Trained and Evaluated BERT model
    - Wrote abstract
    - Wrote proposal
    - Wrote milestone
    - Wrote report (and made all visualizations and tables)
    - Scraped Twitter data from Twitter API
    - Formulated submission readiness of repository (i.e. wrote output.ipynb and project.ipynb)


Karthik Srinatha

    - Scraped data from New york Times
    - Lstm training and Evaluation Scripts
    - Prepared presentation material
    - Prepared Video
    - Contribution in proposal
    - Contribution in milestone report


Anant Sunilam Awasthy

    - Utilized Selenium and APIs to extract data and subsequently cleaned the Sentiment 140 and NewsMTSC datasets
    - Trained and Evaluated LSTM model
    - Contributed in proposal
    - Contributed in milestone report
    - Wrote the LSTM documentation that includes README file
    - Improved the LSTM model performance and scores
    - Contributed in report
    - Developed a Chrome extension which utilizes a Flask API to determine whether a sentiment is positive or negative using BERT