import tweepy
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import TwitterConf


class Twitter:
    def __init__(self):      
        client = tweepy.Client(
            consumer_key=TwitterConf.API_KEY,
            consumer_secret=TwitterConf.API_SECRET_KEY,
            access_token=TwitterConf.ACCESS_TOKEN,
            access_token_secret=TwitterConf.ACCESS_TOKEN_SECRET,
            bearer_token=TwitterConf.BEARER_TOKEN,
        )
        self.client = client

    def tweet(self, message):
        self.client.create_tweet(text=message)

if __name__ == "__main__":
    twitter_client = Twitter()
    twitter_client.tweet('This is a test tweet from the Twitter API.')
