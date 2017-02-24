#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv

#http://www.tweepy.org/
import tweepy

#Get your Twitter API credentials and enter them here
consumer_key = "0tlhmsuJDr0aqbCqAS53FtCIn"
consumer_secret = "JcMFyPq58N8YICifvSoEXfVCEbWSV0LKdqAv8Za3xduClEqnv2"
access_key = "2574486728-EYAGYEPZWvvyPvJH1iJ2LezrsZELde55MUIdvBu"
access_secret = "GYkYjjJ95zh2xbzwjEx4TAoAoWRYgllyUg5Gz7jZgc6cu"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

# Lisbon's place ID
places = api.geo_search(query="Lisbon", granularity="city")
place_id = places[0].id#

tweets = []
# search for 1000 tweets geo-located to Lisbon, which have the key-word 'comida'
public_tweets = api.search(
	# geocode = "-9.137657, 38.713967, 10km",
	q="vegan,place:%s" % place_id,
	# rpp = 100,
	# page = 100,
	count=100
	)
for tweet in public_tweets:
    print(tweet.coordinates, tweet.text)
    tweets.append(tweet.text)

with open('../../data/tweets.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(tweets)


