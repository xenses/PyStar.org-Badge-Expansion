Twitter Client 2.0
==================
Expanded by: Laura C.
---------------------

PyStar.org has an excellent idea and some fun programming tutorials (or 'badges') for beginners.
When learning a new language, most tutorials will have the user either printing values, doing calculations, or possibly doing calculations, printing values, and reading and/or writing to a file. The datasets usually used for such exercises are so small that the user must then venture out on their own to find other, larger sets of data in order to understand the full capacity of a language.
Using Twitter, PyStar.org has an excellent start to showing the more interesting/creative side of programming. I took this start and went a bit further on my own and created a sort of expansion to the original badge.

NB: I feel the use of a 'wrapper library' at this point in learning how a language works, to be counter-productive, if not counter-inuitive for the new or fairly new programmer. Therefore, I elected to keep my original code and so as to avoid having any ambiguous code. I strongly suggest that the step in the original badge for the wrapper library be avoided by those who are new or fairly new to programming and/or Python. Learn your code first, then take your shortcuts.

The instructions are as follows:
--------------------------------

1) Complete the original badge at the pystar.org website, minus the 'Using a wrapper library' portion. That should give you a foundation that looks like this:

```
import urllib
import json
import sys

def search_twitter(query='python'):
    url = 'http://search.twitter.com/search.json?q=' + query
    response = urllib.urlopen(url).read()
    data = json.loads(response)
    return data['results']

def print_tweets(tweets):
    for tweet in tweets:
    	print tweet['from_user'] + ':' + tweet['text'] + '\n'

if __name__ == "__main__":
   query = sys.argv[1]
   results = search_twitter(query)
   print_tweets(results)
```

2) Next, read the documentation on [twitter's search API][1] and find the boolean value you can set in the search query URL which will allow you to remove the following piece of code from your client:
```
tweet['from_user'] + ':' +
```

3) 

[1]: https://dev.twitter.com/docs/api/1/get/search "twitter's search API"