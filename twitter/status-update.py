from twitter import Twitter,OAuth
from os import environ 
from pprint import pprint

consumer_key    = environ['TWITTER_CONSUMER_KEY']
consumer_secret = environ['TWITTER_CONSUMER_SECRET']
access_token    = environ['TWITTER_ACCESS_TOKEN']
access_secret   = environ['TWITTER_ACCESS_SECRET']

t = Twitter(auth=OAuth(access_token,access_secret,consumer_key,consumer_secret))
statusUpdate = t.statuses.update(status='Hallo, word!')
pprint(statusUpdate)