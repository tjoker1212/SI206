# Name: Francisco Gallardo
# Class: SI 206, Section 006 on Fridays from 1 PM - 2 PM

# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "1001992866-Z7Rx0dRzqsnOy7gfGc3ac1A8auGDVCyW1MWpurm"
access_token_secret = "nkvDTNtH5qLuuAemICUjcx2oK03cxVdQpP1bfFEA1x4H8"
consumer_key = "oIKUQxPg4eW6EwpzA1h5ocmeZ"
consumer_secret = "MlsYZn1jY1AmkMtvtPdjxAZAofpFgp6xQi8rch8Kmn6RbHGRa3"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('World Series')

polarityscore = 0.0
subjectivityscore = 0.0

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	#print (type(analysis.sentiment))
	#print (len(analysis.sentiment))
	#print ("")
	#print (analysis.sentiment)
	#print (analysis.sentiment[0])
	#print (analysis.sentiment[1])
	polarityscore += analysis.sentiment[0]
	subjectivityscore += analysis.sentiment[1]

#print (polarityscore, subjectivityscore)
avgpolarity = polarityscore / len(public_tweets)
avgsubjectivity = subjectivityscore / len(public_tweets)
print (avgsubjectivity, avgpolarity)

print("Average subjectivity is " + str(avgsubjectivity))
print("Average polarity is " + str(avgpolarity))

# LETS GO CUBS! #
# FlyTheW #
