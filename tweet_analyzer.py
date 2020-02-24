import numpy as np
import pandas as pd

class TweetAnalyzer():
    """
    Functionality for analyzing and categorizing content from tweets.
    """

    """
    Extracts text from each of the tweets and converts it into a dataframe
    param: JSON format
    """
    def tweets_to_dataframe(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=["Tweets"])
        df["id"] = np.array([tweet.id for tweet in tweets])
        df["len"] = np.array([len(tweet.text) for tweet in tweets])
        df["date"] = np.array([tweet.created_at for tweet in tweets])
        df["source"] = np.array([tweet.source for tweet in tweets])
        df["likes"] = np.array([tweet.favorite_count for tweet in tweets])
        df["retweets"] = np.array([tweet.retweet_count for tweet in tweets])
        df["geo"] = np.array([tweet.geo for tweet in tweets])
        return df
