from tweepy import API
from tweepy import Cursor

from tweepy_authenticator import TwitterAuthenticator

"""
A Twitter Client class will hold the blueprints for creating client objects. The TwitterAuthenticator() is used to authenticate
who is accessing the twitter application and then assign the authorization to a client via API(). This API object can then be used
with multiple Twitter API functions to obtain specific information from Twitter. The information is extracted via a Cursor() and
appended to an appropriate list.

To add more functions, checkout the Twitter API:
http://docs.tweepy.org/en/latest/api.html#API.search
"""
# <----------- TWITTER CLIENT --------------->
class TwitterClient():
    def __init__(self, twitter_user = None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        self.twitter_user = twitter_user
        
    """
    This function makes the twitter_client member variable accesible outside the class

    :return API object
    """
    def get_twitter_client_api(self):
        return self.twitter_client

    """
    This function will get an N number of tweets from the specified user's timeline

    :param number of tweets
    :return [Status]
    """    
    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    """
    This function will obtain an N number of friends from the twitter user's friendlist

    :param number of friends
    :return [User]
    """
    def get_friend_list(self, num_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list

    """
    This function will stream an N number of tweets from the authenticator's home timeline.
    
    :param number of tweets
    :return [Status]
    """
    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets
    
    """
    This function will stream an N number of tweets based on the query and the input location.
    
    :param query item
    :param latitude, longitude, radius (km)
    :param number of tweets to scrape
    :return [SearchResults] in JSON format

    Example
    get_query_tweets_in_location("coronavirus", "30.5928,114.3055,50km", 1)
    """
    def get_query_tweets_in_location(self, query: str, geocode_input: str, num_tweets: int):
        tweets = []
        for tweet in Cursor(self.twitter_client.search, q=query, geocode=geocode_input).items(num_tweets):
            tweets.append(tweet)
        return tweets

    """
    This function will stream an N number of tweets based on the query.
    
    :param query item
    :param number of tweets to scrape
    :return [SearchResults] in JSON format 
    """
    def get_query_tweets(self, query: str, num_tweets: int):
        tweets = []
        for tweet in Cursor(self.twitter_client.search, q=query).items(num_tweets):
            tweets.append(tweet)
        return tweets