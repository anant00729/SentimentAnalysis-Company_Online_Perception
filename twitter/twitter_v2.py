import tweepy
import pandas as pd
import time

auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAAMqwlwEAAAAAHGZsESgKC3OnlR54qwFB1q%2FfRPg%3Dc6RPhaCJGJuIWEPgnSmGkA8C3kYGSUwl4U324JP48UxtWFhfI0")
api = tweepy.API(auth)

def get_tweets():
    """
    This function scrapes tweets from a screen name
    :param screen_name: Screen name to scrape tweets from
    :return:
    """
    # screen_names  = ['YouTube', 'Microsoft', 'Google', 'AirCanada', 'amazon', 'Apple ', 'Samsung', 'Meta', 'intel', 'Bose', 'fia']

    screen_names = ['NBA']

    result_tweets = []

    for each_user in screen_names:
        print(each_user)
        # Gets online tweets (no replies)
        tweets = tweepy.Cursor(api.user_timeline,
                               screen_name=each_user,
                               count=None,
                               since_id=None,
                               max_id=None,
                               trim_user=True,
                               exclude_replies=True,
                               # contributor_details=False,
                               # include_entities=False
                               ).items(20000)

        for tweet in tweets:
            tweet_dict = {'Source': 'twitter', 'Company': each_user, 'Tweet Date': tweet._json['created_at'], 'Id': tweet._json['id_str'], 'Tweet': tweet._json["text"]}
            result_tweets.append(tweet_dict)

    return result_tweets

def get_replies(twitter_msg_ids):
    """
    This function gets replies to tweets made by <screen_name> on tweet <tweet_id>
    :param screen_name: Twitter username
    :param tweet_id: Id of a particular tweet
    :return:
    """
    attached_replies = []
    main_df = pd.DataFrame()

    print(len(twitter_msg_ids))
    i = 1
    for j in range(len(twitter_msg_ids)):
        print(i)
        i = i + 1
        each_user_msg = twitter_msg_ids.iloc[i].to_dict()
        tweet_id = each_user_msg['Id']
        screen_name = each_user_msg['Company']
        del each_user_msg['Tweet']
        tweet = api.get_status(tweet_id, tweet_mode='extended')

        replies = []

        for tweet in tweepy.Cursor(api.search_tweets, q='to:' + screen_name, since_id=int(tweet_id),
                                   result_type='recent').items(50):
            if hasattr(tweet, 'in_reply_to_status_id_str'):
                    replies.append(tweet._json['text'])

        replies = clean_tweets(replies)
        each_user_msg['replies'] = replies
        attached_replies.append(each_user_msg)
        # time.sleep(10)
        tweet_df = pd.DataFrame([each_user_msg])
        tweet_df = tweet_df.explode('replies')
        # main_df = tweet_df.append(each_user_msg, ignore_index=True)


        tweet_df.to_csv('data/tweet_with_replies_all.csv', mode='a', header=False, index=False)

    return attached_replies


def clean_tweets(tweets):
    seen = set()
    new_arr = []
    for s in tweets:
        words = s.split()
        key = tuple(words[:20])  # Change this line to use any 5 words instead of the first 5
        if key not in seen:
            seen.add(key)
            new_arr.append(s)
        else:
            print(key)
    print(new_arr)
    return new_arr

def main():
    # print("Fetching Ids")
    twitter_msg_ids = get_tweets()
    tweet_df = pd.DataFrame(twitter_msg_ids)
    tweet_df.to_csv('data/tweet.csv', mode='a', header=False)
    # print("Ids Fetched")
    # print("Fetching Replies")
    # twitter_msg_with_replies = get_replies(twitter_msg_ids)
    # print("Replies Fetched")
    #
    # tweet_df = pd.DataFrame(twitter_msg_with_replies)
    # tweet_df.to_csv('data/tweet_with_replies.csv')

if __name__ == "__main__":
    main()
