from tweepy import Cursor
from tweepy import API

from wordcloud import WordCloud
from textblob import TextBlob

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import re

from tweepy_authenticator import TwitterAuthenticator

class TweetVisualizer():
    """
    For visualizing the tweet data after the dataframe was created
    """
    def __init__(self, twitter_user = None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)
    """
    Factors over several days (eg. Likes over several days)
    """
    def get_average_tweet_length(self, df):
        return np.mean(df["len"])
    
    def get_max_retweets(self, df):
        return np.max(df["retweets"])
    
    def plot_time_series(self, df, y_values):  
        time_y = pd.Series(data=df[y_values].values, index=df["date"])
        time_y.plot(figsize=(16,4), label=y_values, legend=True, title="Time Series: " + y_values + " vs. time")  
    
    def plot_word_cloud(self, query, limit=500, remove = []):
        text = ""
        for i in range(len(remove)):
            remove[i] = remove[i].lower()
        for tweet in Cursor(self.twitter_client.search, q=query, lang="en").items(limit):
            text += tweet.text.lower()
        removeWords=["https", "co", "rt"]
        removeWords += remove
       
        list_words = re.sub(r"[^A-Za-z]", " ", text).split(" ")
        for word in list_words:
            if word in removeWords:
                list_words.remove(word)
        text = " ".join(list_words)
        wordcloud = WordCloud().generate(text)
        plt.figure(figsize=(12,6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()