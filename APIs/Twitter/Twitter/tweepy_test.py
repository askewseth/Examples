from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'enELT2C8mGVljX71QWjEYB6Dw'
consumer_secret = 'va7KvCA2HIXmqkzPElOv6RfVvxVZjbmsESM5xXNECUECRkkgSi'
access_token = '237951803-6iXB0O6WTqalh2LjlIN4n4qKg2wwkfHfYq1R6UVd'
access_token_secret = 'dYGI6E3h2rX70m9cSM2DpyWr4d5ihCH1HSqcWGv2fYPPG'


class StdOutListener(StreamListener):
    """A basic listner that just prints recieved tweets to stdout."""

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == "__main__":

    # Handles twitter authentication and the connection to the streaming API
    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)

    # Filter twitter streams to capture data by keywords
    stream.filter(track=['trump', 'clintom'])
