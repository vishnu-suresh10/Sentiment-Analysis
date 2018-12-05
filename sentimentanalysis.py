import tweepy
from textblob import TextBlob

searchVal = 'WHAT YOU WANT TO SEARCH FOR'

consumer_key = 'Qge2Aq6I6vTTL6dbgtd9lCAoK'
consumer_secret = 'l9f9VzZnBSym0Pzfy3mRLs7pJ0M1YM6FeDzTCOgo15qMgdrG2y'

access_token = '961780142522683392-Yy9alvvvoXPQjJSIVhaUPGfWoWlPwg3'
access_token_secret = '28EsZcWmNaV9fFVYGDqHBnepWYb76eEiErY7Z95N7rWCD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search(searchVal)

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
