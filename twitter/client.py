import sys
from tweepy import OAuthHandler
 
def get_twitter_auth():

    try:
        consumer_key    = ''
        consumer_secret = ''
        access_token    = ''
        access_secret   = ''
    except KeyError:
        sys.stderr.write("TWITTER_* enveroment variables not set\n")
        sys.exit(1)

    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    return auth

def get_twitter_client():
    pass
    # auth    = get_twitter_auth()
    # client  = API(auth)
    # return client
