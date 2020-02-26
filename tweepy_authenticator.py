from tweepy import OAuthHandler

import twitter_credentials

# <----------- TWITTER AUTHENTICATOR -------->
class TwitterAuthenticator():
    """
    Authenticates the consumer key and access token from the Twitter app
    """
    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth
