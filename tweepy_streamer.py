# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tweepy_streamer.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vinguyen <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/22 23:04:48 by vinguyen          #+#    #+#              #
#    Updated: 2020/02/23 03:13:18 by vinguyen         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
StreamListener is a class from the tweepy module that allows us to listen to tweets. OAuthHandler is a class that will authenticate our Twitter API usage associated with the Twitter App. 
"""
from tweepy.streaming import StreamListener 
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import Cursor

import twitter_credentials

# <----------- TWITTER AUTHENTICATOR -------->
class TwitterAuthenticator():
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth

# <------------ TWITTER STREAMER ------------>
"""
TwitterStreamer is a class that will streams the tweets and store the information in a file.

stream_tweets()
This function will pass in a filename to store the tweets into a JSON formatted file instead of printing it out in the terminal and passing in the search terms that will filter the tweets. It will handle Twitter authentication and the connection to the Twitter Streaming API.

Stream()
This function authenticates the credentials and checks the listener for any potential errors prior to filtering the stream.

filter()
This functions captures the Twitter streams in a JSON format based on inputted hashtags.
"""
class TwitterStreamer():
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator()

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        #Handles Twitter authentication and connection to Twitter Streaming API
        listener = TwitterListener(fetched_tweets_filename) 
        auth = self.twitter_authenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)
        
        #Filters and captures Twitter streams in a JSON dictionary format
        stream.filter(track=hash_tag_list)

# <-------------- TWITTER STREAM LISTENER -------->
"""
StdOutListener is our own Listener class that will inherit from the StreamListener. We will modify this class to contain functions that will override some functions in the StreamListener class. The two functions that we will override are on_data and on_error.

on_data()
This function will take in the data from the StreamListener.

on_error()
This function will print the error if there is an error from streaming. Twitter Twitter API has rate limits, meaning that you have a limited amount of twitter scraping. If you keep on ignoring the 420 message, Twitter will eventually block you from accessing this information.
"""

class TwitterListener(StreamListener):
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on data: %s" % str(e))
        return True

    def on_error(self, status):
        if status == 420:
            #Returning False on data method in case rate limit occurs.
            return False
        print(status)

if __name__ == "__main__":
    hash_tag_list = ["coronavirus", "nCoV2019", "COVID-19", "wuhan virus"]
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
