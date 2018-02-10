from requests_oauthlib import OAuth1
import json
import caching
import secret_data

consumer_key = secret_data.CONSUMER_KEY
consumer_secret = secret_data.CONSUMER_SECRET
access_token = secret_data.ACCESS_KEY
access_secret = secret_data.ACCESS_SECRET

# placeholder
twitter_accounts = ['BarackObama', 'realDonaldTrump']
num_tweets = "25"

auth = OAuth1(consumer_key, consumer_secret, access_token, access_secret)

for account in twitter_accounts:
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    params = {'screen_name':account, 'count':num_tweets}
    response = caching.Check(url, params, auth)
