# pip install tweepy if you don't have tweepy installed
import tweepy
import pandas as pd
import time

#user credentials to authenticate API
#you will get these credentilas when creating a developer account on Twitter
consumer_key = "QsWUqQEugbdFV7iHQyUNGxhZL"
consumer_secret = "xrKOEzf19gVj1OlYSxVF1FRDXRli5qFf2sIajaeBByMaHqCwkR"
access_token = "1127916883360010241-beYUbnEGTUlP9sofgJOozbrm3tJoZq"
access_token_secret = "WGjbW2gbHwdBM5g1CbicHfSmAxnpSscUg3mU1OKheADjF"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#creating a list of tweets
tweets = []

#specify whose tweets you're scraping
username = 'Trump'
#number of tweets you need
tweets_num = 100

#defining a converting function which takes username and count as parameters
def tweets_to_csv(username,tweets_num):

        #getting the individual tweets
        for tweet in api.user_timeline(id=username, count=tweets_num):

            #adding tweets to the list
            tweets.append((tweet.created_at,tweet.id,tweet.text))

            #creating a dataframe in pandas and defining column names
            df = pd.DataFrame(tweets,columns=['Date', 'Tweet_ID', 'Message'])

            #converting dataframe to CSV file
            df.to_csv('scraped_tweets.csv')


#calling the function to create the CSV file
tweets_to_csv(username, tweets_num)
