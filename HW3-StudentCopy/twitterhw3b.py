# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob
import sys

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):

    enc = file.encoding

    if enc == 'UTF-8':

        print(*objects, sep=sep, end=end, file=file)

    else:

        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)

        print(*map(f, objects), sep=sep, end=end, file=file)

# Unique code from Twitter
access_token = "783672422-f8n5mxjJdPinhDJNpoj4EPeMmyIbf5TQqVUjEtjz"
access_token_secret = "VQHV0tDXRRaaYkW2nq9ZXTbabnEHlXESKJn79P9itBwnd"
consumer_key = "cCxQmwhltBPqkV8njvc9xaZ94"
consumer_secret = "TAjrbPAm2ElfJzfpDWuXGHAzzGI1kpsbGUkn8vcjzke3dw89KP"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

search = input("Enter a search term of your choice: ")
public_tweets = api.search(search)

sub = 0
pol = 0
count = 0
for tweet in public_tweets:
    print('\n')
    uprint(tweet.text)
    count = count + 1
    analysis = TextBlob(tweet.text)
    sub = sub + (analysis.sentiment.subjectivity)
    pol = pol + (analysis.sentiment.polarity)
	
print("\nAverage subjectivity is " + str(sub/count))
print("Average polarity is " + str(pol/count))
