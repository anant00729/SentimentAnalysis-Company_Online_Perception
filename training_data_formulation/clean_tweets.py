import pandas as pd
import re


def clean_tweet(tweet: str) -> str:
    """
    The function cleans a tweet
    :param tweet: The tweet in question
    :return: Cleaned tweet
    """
    # Remove links
    tweet = re.sub(r'http\S+', '', tweet)

    # Remove words that start with @
    tweet = re.sub(r'@\w+', '', tweet)

    # tweet = tweet.replace("@", "")

    # Remove words that start with #
    tweet = re.sub(r'#\w+', '', tweet)

    # Remove words that start with & and end with ;
    tweet = re.sub(r'&\w+;', '', tweet)

    # Remove brackets around ?
    tweet = re.sub(r'\(\?\)', '?', tweet)

    # Replace multiple spaces with a single space
    tweet = re.sub(r'\s{2,}', ' ', tweet)

    # Remove leading and trailing white space
    tweet = tweet.strip()

    # Remove substrings that start with a special character
    tweet = re.sub(r'^-', '', tweet)

    # Remove leading and trailing white space
    tweet = tweet.strip()

    # Removing quotations
    tweet = tweet.replace("\"", "")

    # Removing periods
    tweet = tweet.replace(".", "")

    # Remove leading and trailing white space
    tweet = tweet.strip()
    tweet = tweet.strip('"')

    # Removing quotations
    tweet = tweet.replace("\"", "")
    tweet = tweet.replace("“", "")
    tweet = tweet.replace("”", "")
    # Removing brackets
    tweet = tweet.replace("(", "")
    tweet = tweet.replace(")", "")
    tweet = tweet.replace("[", "")
    tweet = tweet.replace("]", "")

    # Removing commas
    tweet = tweet.replace(",", "")

    # Removing "-"
    tweet = tweet.replace("-", " ")

    # Removing double and triple spaces
    tweet = tweet.replace("  ", " ")
    tweet = tweet.replace("   ", " ")

    # Removing @ symbol
    tweet = tweet.replace("@", "")

    # Removing @ symbol
    tweet = tweet.replace("#", "")

    # Removing periods
    tweet = tweet.replace(".", "")

    # Removing —
    tweet = tweet.replace("—", "")

    # Removing some additional characters
    tweet = tweet.replace("?", "")
    tweet = tweet.replace("=", "")
    tweet = tweet.replace("!", "")
    tweet = tweet.replace(":", "")
    tweet = tweet.replace(";", "")
    tweet = tweet.replace("/", "")

    # Return tweets normalized to lowercase
    return tweet.lower()


def remove_unicode(text: str) -> str:
    """
    Removes unicode characters
    :param text: text to clean
    :return: cleaned text
    """

    # Convert the string to a bytes object
    bytes_text = text.encode('ascii', 'ignore')

    # Convert the bytes object back to a string
    clean_text = bytes_text.decode()

    return clean_text


def apply_polarity_values(polarity: int) -> int:
    """
    Converts polarity from (0,2,4) -> (-1,0,1) respectively
    :param polarity: The polarity value
    :return: New polarity value
    """
    if polarity == 0:
        return -1
    elif polarity == 2:
        return 0
    else:
        return 1


def main():
    """
    This scrip cleans the Sentiment140 dataset
    :return:
    """
    # Columns to use
    columns = ['target', 'ids', 'date', 'flag', 'user', 'tweet']

    # Reading in the dataset
    df = pd.read_csv('data/training.1600000.processed.noemoticon.csv', sep=',', encoding='latin-1', names=columns)

    # Updating the polarity values
    df['polarity'] = df['target'].apply(apply_polarity_values)

    # Cleaning the tweet
    df['tweet'] = df['tweet'].apply(clean_tweet)

    # Removing unicode characters
    df['tweet'] = df['tweet'].apply(remove_unicode)

    # Dropping NAs
    df.dropna(subset=['tweet'], inplace=True)

    # Subsetting to only the columns we want
    df = df[['polarity', 'tweet']]

    # Renaming the columns
    df.columns = ["label", "sequence"]

    # Writing to disk
    df.to_csv('results/tweets.csv', header=True, index=False)


if __name__ == "__main__":
    main()
