from twitter import Twitter,OAuth
from os import environ 
from pprint import pprint

consumer_key    = environ['TWITTER_CONSUMER_KEY']
consumer_secret = environ['TWITTER_CONSUMER_SECRET']
access_token    = environ['TWITTER_ACCESS_TOKEN']
access_secret   = environ['TWITTER_ACCESS_SECRET']

t = Twitter(auth=OAuth(access_token,access_secret,consumer_key,consumer_secret))

# pythonStatuses = t.statuses.user_timeline(screen_name='montypython',count=5)
pythonStatuses = t.statuses.user_timeline(screen_name='googledevs',count=5)
print(pythonStatuses)