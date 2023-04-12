import tweepy
import pandas as pd
import sys

auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAAMqwlwEAAAAAHGZsESgKC3OnlR54qwFB1q%2FfRPg%3Dc6RPhaCJGJuIWEPgnSmGkA8C3kYGSUwl4U324JP48UxtWFhfI0")
api = tweepy.API(auth)


def get_tweets(screen_name: str):
    """
    This function gets replies to tweets made by <screen_name> on tweet <tweet_id>
    :param screen_name: Twitter username
    :param tweet_id: Id of a particular tweet
    :return:
    """

    tweets = []
    for tweet in tweepy.Cursor(api.search_tweets, q='to:' + screen_name, result_type='recent').items():
        tweets.append(tweet)

    tweets_data = []
    for tweet in tweets:
        tweet_data = {"date": tweet._json['created_at'], "id": tweet._json['id_str'], "text": tweet._json["text"]}

        tweets_data.append(tweet_data)

    tweets_data_df = pd.DataFrame(tweets_data)

    tweets_data_df.to_csv(f"data/{screen_name}_tweets.csv")


def main():
    try:
        screen_name = sys.argv[1]
    except IndexError:
        print("[ERROR] Twitter handle not passed.  Needs to be: \"\python twitter.py <twitter handle>\"")
        exit(1)

    get_tweets(screen_name=screen_name)


if __name__ == "__main__":
    main()
