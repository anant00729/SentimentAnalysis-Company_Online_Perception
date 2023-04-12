import datetime
import pandas as pd
from pynytimes import NYTAPI

"""
In this script we scrape the short news article abstracts from the New York Times 
"""


def main():
    """
    This function contains base code for pulling news article abstracts/headlines from the New York Times API
    :return:
    """
    # SEARCH PARAMETERS

    # See here for search documentation: https://pynytimes.michadenheijer.com/search/article-search

    queries = ['Adani Group', 'Ftx', 'Microsoft', 'Google', 'Air Canada', 'Amazon', 'Apple ', 'Samsung', 'Meta', 'Intel', 'Bose', 'Fia']

    # Configuring NYT API
    nyt = NYTAPI("QIAH0a9rE0tg8mmAR322AY9EFc6TuelC", parse_dates=True)

    # Iterating through each company
    for c_query in queries:

        # Set the date range
        start_date = datetime.datetime(2021, 1, 1)
        end_date = datetime.datetime(2023, 3, 15)

        # Date setup
        delta_days = end_date - start_date
        delta_days = delta_days.days
        loop_min_date = start_date
        days_iter = delta_days // 15

        # Iteration
        for i in range(days_iter + 1):

            loop_date = loop_min_date + datetime.timedelta(days=15)

            if loop_date > end_date:
                loop_date = end_date

            # Just to show where the query is fetching results
            print(loop_min_date, loop_date)

            max_num_results = 30

            # Searching for articles
            articles = nyt.article_search(query=c_query, dates={"begin": loop_min_date, "end": loop_date}, results=max_num_results, options={"sort": "oldest"})

            # Iterating through articles
            for article in articles:
                each_record = {'Company': c_query.lower(), 'Source': 'NYT', 'Date': article['pub_date'].strftime("%m/%d/%Y"),
                               'Text': article['abstract'].lower()}
                df = pd.DataFrame([each_record])
                # df['Filter'] = df.apply(lambda x: x.Company in x.Text, axis=1)
                # fil_df = df.loc[df['Filter']==True]
                df.to_csv('data/nyt_api_data.csv', mode='a', header=False, index=False)
                # fil_df.to_csv('data/Api_data_cleaned.csv', mode='a', header=False, index=False)
            loop_min_date = loop_date

        print(c_query)


if __name__ == "__main__":
    main()
