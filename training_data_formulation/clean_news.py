import pandas as pd


def clean_sentence(sentence: str) -> str:
    """
    Cleans a news article sentence
    :param sentence:  to clean
    :return: cleaned sentence (lower case)
    """
    # Remove leading and trailing white space
    sentence = sentence.strip()
    sentence = sentence.strip('"')

    # Removing quotations
    sentence = sentence.replace("\"", "")
    sentence = sentence.replace("“", "")
    sentence = sentence.replace("”", "")
    # Removing brackets
    sentence = sentence.replace("(", "")
    sentence = sentence.replace(")", "")
    sentence = sentence.replace("[", "")
    sentence = sentence.replace("]", "")

    # Removing commas
    sentence = sentence.replace(",", "")

    # Removing "-"
    sentence = sentence.replace("-", " ")

    # Removing double and triple spaces
    sentence = sentence.replace("  ", " ")
    sentence = sentence.replace("   ", " ")

    # Removing @ symbol
    sentence = sentence.replace("@", "")

    # Removing @ symbol
    sentence = sentence.replace("#", "")

    # Removing periods
    sentence = sentence.replace(".", "")

    # Removing —
    sentence = sentence.replace("—", "")
    
    # Removing some additional characters
    sentence = sentence.replace("?", "")
    sentence = sentence.replace("=", "")
    sentence = sentence.replace("!", "")
    sentence = sentence.replace(":", "")
    sentence = sentence.replace(";", "")
    sentence = sentence.replace("/", "")

    # Returning the sentence normalized to lower case
    return sentence.lower()


def contains_invalid_sequence(sentence: str) -> bool:
    """
    # Checks if the sentence is invalid in some capacity
    :param sentence: Sequence to check
    :return: flag if the sequence contains an invalid sentence
    """

    # Checking if the sequence contains a hyperlink.
    # We noticed sequences containing these were just weird
    if "http" in sentence:
        return True

    # Checking if the sequence contains a new line.
    # We noticed sequences containing these were just were
    if "\n" in sentence:
        return True

    return False


def main():
    """
    This script cleans the NewsMTSC Dataset, this dataset can be downloaded here: https://www.kaggle.com/datasets/fhamborg/news-articles-sentiment
    :return:
    """

    # Reading in the data set splits
    df_news_dev = pd.read_json('data/dev.jsonl', lines=True)
    df_news_test = pd.read_json('data/test.jsonl', lines=True)
    df_news_train = pd.read_json('data/train.jsonl', lines=True)

    # Merging the datasets together
    df_news = pd.concat([df_news_dev, df_news_test, df_news_train])

    # Cleaning the sequence
    df_news['sentence'] = df_news['sentence'].apply(clean_sentence)

    # Checking for bad sequences
    df_news['is_bad'] = df_news['sentence'].apply(contains_invalid_sequence)

    # Dropping NAs
    df_news.dropna(subset=['sentence'], inplace=True)

    # Dropping bad sequences
    df_news = df_news[df_news['is_bad'] == False]

    # Submitting to only the columns we want
    df_news = df_news[['polarity', 'sentence']]

    # Renaming the columns
    df_news.columns = ["label", "sequence"]

    # Dropping any duplicates
    df_news = df_news.drop_duplicates()

    # Writing to disk
    df_news.to_csv('results/news.csv', header=True, index=False)


if __name__ == "__main__":
    main()
