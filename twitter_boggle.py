from requests_oauthlib import OAuth1
import json
import nltk
from nltk.corpus import stopwords

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

# generic list of stop words
stop_words = stopwords.words('english') # from https://pythonspot.com/nltk-stop-words/
stop_words.extend(['http', 'https', 'RT'])

freq_list_by_account = {}
for account in twitter_accounts:
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    params = {'screen_name':account, 'count':num_tweets}
    responses = caching.Check(url, params, auth)
    tokens = []
    for response in responses:
        for word in nltk.word_tokenize(response['text']):
            word = word.lower()
            if word.isalpha() and word not in stop_words:
                tokens.append(word)
    freq_list_by_account[account] = nltk.FreqDist(tokens)
