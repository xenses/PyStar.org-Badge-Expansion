import urllib
import json
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user', dest='username')
parser.add_argument('-s', '--search', dest='query')
args = parser.parse_args()
                    
def search_twitter(query):
    url = 'http://search.twitter.com/search.json?show_user=true&q=' + args.query
    response = urllib.urlopen(url).read()
    data = json.loads(response)
    return data['results']
                    
def search_user(query):
    url = 'http://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&screen_name=' + args.username
    response = urllib.urlopen(url).read()
    data = json.loads(response)
    return data

def print_tweets(tweets):
    for tweet in tweets:
        print tweet['text'] + '\n'

if __name__ == "__main__":
    if args.username:
        try:
            results = search_user(args.username)
            print_tweets(results)
        except IOError:
            print "That user's account is either private or does not exist. Please enter a valid account."
    elif args.query:
        results = search_twitter(args.query)
        if results:
            print_tweets(results)
        else:
            print "Your query matched no terms, please try a different query."
