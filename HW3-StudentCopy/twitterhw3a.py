# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy
import nltk

# Unique code from Twitter
access_token = "783672422-f8n5mxjJdPinhDJNpoj4EPeMmyIbf5TQqVUjEtjz"
access_token_secret = "VQHV0tDXRRaaYkW2nq9ZXTbabnEHlXESKJn79P9itBwnd"
consumer_key = "cCxQmwhltBPqkV8njvc9xaZ94"
consumer_secret = "TAjrbPAm2ElfJzfpDWuXGHAzzGI1kpsbGUkn8vcjzke3dw89KP"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

image = input('Enter location of image: ')
message = input('Enter tweet: ')
api.update_with_media(image, status = message)


