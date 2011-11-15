Twitter Client 2.0
==================
Expanded by: Laura C.
---------------------

PyStar.org has an excellent idea and some fun programming tutorials (or 'badges') for beginners.
When learning a new language, most tutorials will have the user either printing values, doing calculations, or possibly doing calculations, printing values, and reading and/or writing to a file. The datasets usually used for such exercises are so small that the user must then venture out on their own to find other, larger sets of data in order to understand the full capacity of a language.
Using Twitter, PyStar.org has an excellent start to showing the more interesting/creative side of programming. I took this start and went a bit further on my own and created a sort of expansion to the original badge.

NB: I feel the use of a 'wrapper library' at this point in learning how a language works, to be counter-productive, if not counter-inuitive for the new or fairly new programmer. Therefore, I elected to keep my original code and so as to avoid having any ambiguous code. I strongly suggest that the step in the original badge for the wrapper library be avoided by those who are new or fairly new to programming and/or Python. Learn your code first, then take your shortcuts.

For this exercise, we'll be committing our code after each step, this will get the user in the habit of committing their code, and doing it often. Should you need help with version control, please see the help section at github.com

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
***COMMIT YOUR CODE ONCE THIS IS COMPLETE***

2) Next, read the documentation on [twitter's search API][1] and find the boolean value you can set in the search query URL which will allow you to remove the following piece of code from your client:

```
tweet['from_user'] + ':' +
```

You will simply add the correct variable assignment followed by an '&' after the '?' but before the 'q'.

***COMMIT YOUR CODE ONCE THIS IS COMPLETE***

3) Giving users options in how they query information is an important option to be provided by our application. To this end, we will add a function, named 'search_user', which will search twitter for a username and return tweets by a specific user. This [API][2] will get you started. This function will not work, just yet. We want to simply get the function defined and the URL that we'll need. HINT: You can copy a lot of the previous function for searching tweets for this function, and changing a few identifying variables.
HINT: To see if this function is working, simply call this function from your if statement, just replace 'search_twitter' with 'search_user' and it should work the same, only it will be calling the proper URL for the username search. 

At this point, you may start seeing errors and you can't get your data to display. That's what we want to happen. Mistakes mean you're learning something new, so let's go with that. To star figuring out what is happening, look at the JSON for the search_twitter function (including your search term), and then look at the JSON for the search_user function. Understanding your data is the best way to figure out where things may be going wrong. See if you can see the difference between the two objects, and then adjust your code accordingly. 

***COMMIT YOUR CODE ONCE THIS IS COMPLETE***

4)Next, we're going to use [argparse][3] to allow the user to enter a flag whether they are going to search for a username or for a search term. Depending on the flag, argparse is going to save the value in one of two variables. We will then take those variables and use them in our code. Let's call the variables for argparse 'username', and 'query'. The flags for each are simply '-u' or '-s'.
Once you have the argparse variables set (don't forget that when you're using a library you must import the lib into your code) replace query = sys.argv[1] with your argparse variables. This means 'query' is no longer needed, so the first line of your if statement can be taken out completely and instead of passing 'query' to your functions, you'll pass the corresponding argparse variables.

***COMMIT YOUR CODE ONCE THIS IS COMPLETE***


[1]: https://dev.twitter.com/docs/api/1/get/search "twitter's search API"
[2]: https://dev.twitter.com/docs/api/1/get/statuses/user_timeline "API"
[3]: http://docs.python.org/dev/library/argparse.html "argparse"