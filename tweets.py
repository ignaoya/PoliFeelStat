
import os
import sys
import plotly
import socket
import html

from analyzer import Analyzer
from twython import Twython
from twython import TwythonAuthError, TwythonError, TwythonRateLimitError
from termcolor import colored
import sys
import plotly
import socket
import html

from analyzer import Analyzer
from twython import Twython
from twython import TwythonAuthError, TwythonError, TwythonRateLimitError
from termcolor import colored

def main():
    
    if len(sys.argv) != 2:
        sys.exit("USage: ./tweet twitterhandle")
        
    tweets = get_user_timeline(sys.argv[1])
    
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    analyzer = Analyzer(positives, negatives)
    
    try:
        for tweet in tweets:
            score = analyzer.analyze(tweet)
            if score > 0.0:
                print(colored(tweet+" "+format(score), "green"))
            elif score < 0.0:
                print(colored(tweet+" "+format(score), "red"))
            else:
                print(colored(tweet+" "+format(score), "yellow"))
    except Exception as e:
        print(e)

def get_user_timeline(screen_name, count=50):
    """Return list of most recent tweets posted by screen_name."""

    # ensure count is valid
    if count < 1 or count > 50:
        raise RuntimeError("invalid count")

    # ensure environment variables are set
    if not os.environ.get("API_KEY"):
        raise RuntimeError("API_KEY not set")
    if not os.environ.get("API_SECRET"):
        raise RuntimeError("API_SECRET not set")

    # get screen_name's most recent tweets
    # https://dev.twitter.com/rest/reference/get/users/lookup
    # https://dev.twitter.com/rest/reference/get/statuses/user_timeline
    # https://github.com/ryanmcgrath/twython/blob/master/twython/endpoints.py
    try:
        #twitter = Twython(os.environ.get("API_KEY"), os.environ.get("API_SECRET"))
        twitter = Twython("", "")
        user = twitter.lookup_user(screen_name=screen_name)
        if user[0]["protected"]:
            return None
        tweets = twitter.get_user_timeline(screen_name=screen_name, count=count)
        return [html.unescape(tweet["text"].replace("\n", " ")) for tweet in tweets]
    except TwythonAuthError:
        raise RuntimeError("invalid API_KEY and/or API_SECRET") from None
    except TwythonRateLimitError:
        raise RuntimeError("you've hit a rate limit") from None
    except TwythonError:
        return None
        
if __name__ == "__main__":
    main()
