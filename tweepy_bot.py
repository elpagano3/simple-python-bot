#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
from twitter import TwitterHTTPError
from login import *

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Function that Search a tweet and else do a retweet for all of them
def search_tweet():
	query=raw_input("Palabra de busqueda: ")
	results=api.search(q=str(query), result_type='recent', count=5)
	for result in results:
		try:		
			api.retweet(result.id)
			print "RT @" + result.user.screen_name + " :"
			print result.text
		# when you have already favourited a tweet
    		# this error is thrown
    		except TwitterHTTPError as e:
        		print "Error: ", e
		
search_tweet()
    

