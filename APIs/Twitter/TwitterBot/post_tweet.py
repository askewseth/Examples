"""Module for tweeting remotely."""
import tweepy

class Tweeter(object):

    def __init__(self):
        self.ckey, self.csecret, self.akey, self.asecret = self._get_keys()

    def _get_keys(self):
        # Get API information
        with open("api_info.txt", "rb") as f:
            lines = f.readlines()
            # Take out header information
            lines.pop(0)
            return map(lambda x: x.strip(), lines)

    def tweet(self, text):
        auth = tweepy.OAuthHandler(self.ckey, self.csecret)
        auth.set_access_token(self.akey, self.asecret)

        api = tweepy.API(auth)
        api.update_status(text)



def test():
    t = Tweeter()
    t.tweet("Testing Object Orientation")

    print "Done"


if __name__ == "__main__":
    test()
