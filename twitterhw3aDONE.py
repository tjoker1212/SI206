# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy

# Unique code from Twitter
access_token = "1001992866-Z7Rx0dRzqsnOy7gfGc3ac1A8auGDVCyW1MWpurm"
access_token_secret = "nkvDTNtH5qLuuAemICUjcx2oK03cxVdQpP1bfFEA1x4H8"
consumer_key = "iBpaRhWYa4mDwmPYScWMV6OuG"
consumer_secret = "YURJCV4aU5QwM5QkmWFDeiHjundxiBkH9Jhwps3g5kotDPo0bL"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

#public_tweets = api.update_status('UMSI')
more = api.update_with_media(filename = 'Twitter.jpg', status = '#UMSI-206 #Proj3')

print ("Success!")
#for tweet in public_tweets:
#	print(tweet.text)

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")