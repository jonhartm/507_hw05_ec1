import requests
import json

CACHE_FILE = 'boggle_twitter_cache.json'
API_cache = {}

# Try to open the cache file if you can find it and load the json data into API_cache
try:
    with open(CACHE_FILE, 'r') as f:
        API_cache = json.loads(f.read())
except:
    print("No cache file named {} exists or I can't read it properly. Creating one now...".format(CACHE_FILE))
    f = open(CACHE_FILE, 'w')
    f.close()

# Checks the cache file for a combination of url and keys to see if it exists in the cache already.
# params: a string for the url and a dictionary of paramaters
# returns: a dictionary of json, either pulled from the API or loaded from the cache
def Check(url, params, auth):
    param_keys = sorted(params.keys()) # sort the paramaters so we know they'll be in the same order even if they aren't in order in the dictionary attribute
    unique_ID = url # start creating the unique_ID with the URL
    for k in param_keys:
        if not("api" in k and "key" in k): # skip anything with the words "api" and "key"
            unique_ID += "_" + k + "_" + params[k].lower()

    # check to see if this unique ID is stored in the cache, and if not, make a request and add it
    if unique_ID in API_cache:
        print("Repeated request - retrieving from cache file.")
        return API_cache[unique_ID]
    else:
        print("New request - adding to cache file.")

    response = requests.get(url, params=params, auth=auth)
    API_cache[unique_ID] = json.loads(response.text)

    f = open(CACHE_FILE, 'w')
    f.write(json.dumps(API_cache)) # write the contents of the cache dictionary to the cache
    return json.loads(response.text)
