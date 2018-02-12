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
stop_words.extend(['http', 'https', 'rt'])

# Gets the most common words that appear between two dictionaries
# params: a dict formatted {'twitterUser1':{'token':X, ...}, 'twitterUser2':{'token':X, ...}} and a count of the number of words to return
# returns: a list of strings
def most_common_shared_words(dicts, count=5):
    common_words = {}
    # order the dicts by the number of k:v pairs
    ordered_dicts = sorted(dicts, key=lambda x: len(dicts[x]), reverse=True)
    # iterate through the words in the first dictionary, since that will be the longest
    for word in dicts[ordered_dicts[0]]:
        if word in dicts[ordered_dicts[1]]:
            common_words[word] = dicts[ordered_dicts[0]][word] + dicts[ordered_dicts[1]][word] #TODO: oh god this is ugly
    return sorted(common_words, key=lambda x: common_words[x], reverse=True)[:count] # sort the words by total count between accounts and slice to the count

# finds the most common words that do not appear in the other dictionary
# params: a dict formatted {'twitterUser1':{'token':X, ...}, 'twitterUser2':{'token':X, ...}} and a count of the number of words to return
# returns: a dictionary formatted {'twitterUser1':['token'], 'twitterUser1':['token']}
def most_common_different_words(dicts, count=5):
    # get every word that's common between the two accounts
    common_words = most_common_shared_words(dicts, -1)
    different_words = {}
    for d in dicts:
        # find the most common words in this dictionary that don't appear in the common_words list
        different_words[d] = most_common_words_not_in(dicts[d], common_words, count)
    return different_words

def most_common_words_not_in(d, ignore_list, count):
    unique_words = {}
    for word in d:
        if word not in ignore_list:
            unique_words[word] = d[word] # if the word doesn't appear in the ignore_list, add it to this dictionary
    return sorted(unique_words, key=lambda x: unique_words[x], reverse=True)[:count] # sort the words by total count between accounts and slice to the count

if __name__ == '__main__':
    twitter_accounts[0] = input("Enter in a twitter account name to compare: ")
    twitter_accounts[1] = input("Enter in another twitter account name to compare: ")
    num_tweets = input("How many tweets should I look at? ")
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
    print("Most common words between {} and {}:".format(twitter_accounts[0], twitter_accounts[1]))
    for word in most_common_shared_words(freq_list_by_account):
        print("  " + word)
    different_words = most_common_different_words(freq_list_by_account)
    for x in different_words:
        print("Most common words unique to {}:".format(x))
        for word in different_words[x]:
            print("  " + word)
