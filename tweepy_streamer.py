# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tweepy_streamer.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vinguyen <vinguyen@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/22 23:04:48 by vinguyen          #+#    #+#              #
#    Updated: 2020/02/23 23:21:57 by vinguyen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from tweepy.streaming import StreamListener 
from tweepy import Stream

import twitter_credentials

from tweepy_authenticator import TwitterAuthenticator
from tweepy_client import TwitterClient
from tweet_analyzer import TweetAnalyzer

from wordcloud import WordCloud

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# <------------ TWITTER STREAMER ------------>
"""
This class is for streaming and processing live tweets. When a Twitter Steamer
object is created and is used to stream_tweets, then a listener object will be
craeted to store listen for incoming streams and store the tweets in a file
"""
class TwitterStreamer():
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    """
    This function will create a listner object an authenticate the keys and tokens

    :param the file to store the tweets
    :param the searchy query hash tags in a list format
    """
    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        #Handles Twitter authentication and connection to Twitter Streaming API
        listener = TwitterListener(fetched_tweets_filename) 
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
        
        #Filters and captures Twitter streams in a JSON dictionary format based on inputted hashtags
        stream.filter(track=hash_tag_list)


# <-------------- TWITTER LISTENER -------->
"""
This is a basic listener class that puts received tweets into a file. 
The functions on_data and on_error override the StreamListener's functions.
When a TwitterListener object is created by steam_tweets(), these two functions will be called.
"""
class TwitterListener(StreamListener):
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
    
    #Prints out the tweet data that was received
    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data) 
            return True
        except BaseException as e:
            print("Error on data: %s" % str(e))
        return True

    #Prints out an error message if an error occurs
    def on_error(self, status):
        if status == 420:
            #Returning False on data method in case rate limit occurs.
            return False
        print(status)
        
from tweepy import Cursor
from tweepy import API
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
    
    def plot_word_cloud(self, query, limit=1000, remove = []):
        text = ""
        for tweet in Cursor(self.twitter_client.search, q=query, lang="en").items(limit):
            text += tweet.text.lower()
        removeWords = ["https","co", "com", ".", "mama", "may", "follow"]
        removeWords += remove
        for word in removeWords:
            text = text.replace(word, "")
        wordcloud = WordCloud().generate(text)
        plt.figure(figsize=(12,6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

if __name__ == "__main__":

    # Example Code #1: Using Streamer, Listener, Authenticator. Unlimited # of Tweets 
    # This is the basics of streaming tweets based on query names
    """
    hash_tag_list = ["coronavirus", "nCoV2019", "COVID-19"]
    filename =  "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(filename, hash_tag_list)
    """
    
    #Example Code #2: Using TwitterClient, TwitterAuthenticator, API, Customized Functions
    #This class will allow us to call a *certain number of tweets* based on the Cursor & API function
    """
    twitter_client = TwitterClient()
    print(twitter_client.get_user_timeline_tweets(1))

    print(twitter_client.get_friend_list(1))
    """
    
    # Example Code #3: Using TwitterClient to directly access the Twitter API functions
    # This class will allow us to obtain the API object, which can then be used to call API functions rather
    # than the customized functions.
    """
    twitter_client = TwitterClient()
    api = twitter_client.get_twitter_client_api()
    tweets = api.user_timeline(screen_name="42SiliconValley", count=1)
    print(tweets)
    """

    # Example Code #3: Using TwitterClient and Tweet Analyzer to categorize 
    # content from the tweets
    # Tweet Analyzer will convert the file from list of JSON into a dataframe
    """
    twitter_client = TwitterClient()
    api = twitter_client.get_twitter_client_api()
    tweets = api.search(q="coronavirus", count=10)

    tweet_analyzer = TweetAnalyzer()
    df = tweet_analyzer.tweets_to_dataframe(tweets)
    print(df.head(10))
    """

    # Example Code #4: Sorting a Dataframe by Retweets
    # This code will sort the values by retweet amoutn in descending order
    """
    twitter_client = TwitterClient()
    api = twitter_client.get_twitter_client_api()
    tweets = api.search(q="coronavirus", count=10)
    
    tweet_analyzer = TweetAnalyzer()
    df = tweet_analyzer.tweets_to_dataframe(tweets) 
    df = df.sort_values(by="retweets", ascending=False)
    print(df.head(10))
    #print(dir(tweets[0])) # This will print a list of things that you can sort it by
    """

    # Example Code #5: Obtaining Mathematical Information
    # This code provide examples of how to use the NumPy library for data manipulation
    """
    twitter_client = TwitterClient()
    api = twitter_client.get_twitter_client_api()
    tweets = api.search(q="coronavirus", count=100)
    
    tweet_analyzer = TweetAnalyzer()
    df = tweet_analyzer.tweets_to_dataframe(tweets) 

    tweet_visualizer = TweetVisualizer()
    
    #Get average length over all tweets
    print(tweet_visualizer.get_average_tweet_length(df))
    
    #Get the number of retweets for the most retweeted post
    print(tweet_visualizer.get_max_retweets(df))
    """

    # Example Code #6: Time series plot
    # This code provide examples of graphical manipulation of data
    """
    twitter_client = TwitterClient("USUhealthsci")
    tweets = twitter_client.get_user_timeline_tweets(100)
    
    tweet_analyzer = TweetAnalyzer()
    df = tweet_analyzer.tweets_to_dataframe(tweets) 
    
    # time_likes = pd.Series(data=df["likes"].values, index=df["date"])
    # time_likes.plot(figsize=(16,4), label="likes", legend=True)

    # time_retweets = pd.Series(data=df["retweets"].values, index=df["date"])
    # time_retweets.plot(figsize=(16,4), label="retweets", legend=True, title="@USUhealthsci: Likes vs. Retweets Over Time")
    
    # df = df.sort_values(by="retweets", ascending=False))

    plt.show()
    """
    
    # Example Code #7: Time series plot using function
    # This code will use TweetVisualizer function to graph the plot
    """
    twitter_client = TwitterClient("USUhealthsci")
    tweets = twitter_client.get_user_timeline_tweets(100)
    
    tweet_analyzer = TweetAnalyzer()
    df = tweet_analyzer.tweets_to_dataframe(tweets) 

    tweet_visualizer = TweetVisualizer()
    y_values="likes"
    tweet_visualizer.plot_time_series(df, y_values)
    """

    # Example Code #8: Word Cloud plot using function
    # This code will use TweetVisualizer function to graph the plot

    tweet_visualizer = TweetVisualizer()
    tweet_visualizer.plot_word_cloud("42SiliconValley")