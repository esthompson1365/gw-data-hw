#!/usr/bin/env python
# coding: utf-8

# ## Import Packages and Authenticate

# Dependencies
import tweepy
import pandas as pd
import numpy as np
import datetime
import json
import requests
import matplotlib.pyplot as plt
import time
import os
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()


consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

def SentimentTweet(): 
    # Pull Mentions
    # Search for all tweets with "@JohnZalk Analyze:"
    search_term = "@JohnZalk Analyze:"
    
    # List of mentions
    mention_list = []
    
    mentions = api.search(search_term, count=100)
    
    for mention in mentions["statuses"]:
        
        # add tweets to the list
        mention_list.append({'User' : '@' + mention["user"]["screen_name"],
                             'Account' : mention["text"].split(": ",1)[1],
                             # convert date
                             'Date' : time.strftime('%Y-%m-%d %H:%M:%S',
                                                    time.strptime(mention['created_at'],
                                                                  '%a %b %d %H:%M:%S +0000 %Y'))})
    
    # turn tweets to df
    mention_df = pd.DataFrame(mention_list)
    
    five_min_ago = datetime.datetime.now() - datetime.timedelta(minutes=5)
    
    #filter out mentions outside of last 5 mins 
    mention_df = mention_df[(mention_df['Date'] > str(five_min_ago))]
    
    if not mention_df.empty:
        
        #remove Account that have been mentioned twice
        counts = mention_df['Account'].value_counts()
        
        counts = counts.to_dict() #converts to dictionary
        
        #add counts to mentions df
        mention_df['Count'] = mention_df['Account'].map(counts) 
        
        #remove counts > 1
        mention_df = mention_df[mention_df.Count < 2]
    
        #take most recent mention
        recent_date = mention_df['Date'].max()
        mention_df=mention_df[mention_df['Date'] == recent_date]
        
        #turn account value to string
        target_account = mention_df.iloc[0]['Account']
        
        #turn user value to string
        user = mention_df.iloc[0]['User']
    
        # Pull Last 500 Tweets and Store in DF
        tweet_list =[]
        
        # Loop through 21 pages of tweets (total 500 tweets)
        for x in range(1, 21):
        
            # Get all tweets from home feed
            tweets = api.user_timeline(target_account, page=x)
        
            # Loop through all tweets and print the tweet text
            for tweet in tweets:
                tweet_list.append(tweet['text'])
                
    
        tweet_df = pd.DataFrame(tweet_list)
        
        #rename column
        tweet_df.rename(columns = {0:'Tweet'}, inplace = True)
        ##create column Tweets Ago for x axis of sentiment plot
        # count nuber of tweets becuase not all accounts have 500 and make number negative
        number_tweets = -len(tweet_df)
        #create an array 0 through number_tweets
        tweets_ago = np.arange(0,number_tweets,-1)
        #add array as column in df
        tweet_df['Tweets Ago'] = tweets_ago
        # create polarity column that's 0 for now
        tweet_df['Tweet Polarity'] = 0
    
        # Compute Polarity Score
    
        # loop through tweets and compute polarity score. Append score to list.
        polarity=[]
        for row in tweet_df['Tweet']:
            results = analyzer.polarity_scores(row)
            polarity.append(results['compound'])
        
        # turn list into df column
        tweet_df['Tweet Polarity'] = polarity
        
        # Plot
    
        plt.stem(tweet_df['Tweets Ago'], tweet_df['Tweet Polarity'], basefmt=' ', use_line_collection = True)
        plt.title("Sentiment Analysis of Tweets by " + target_account)
        plt.ylabel('Tweet Polarity')
        plt.xlabel("Tweets Ago")
        plt.grid(linestyle='-', linewidth='0.5', color='grey')
        plt.ylim(-1,1)
        
        # ***Cannot create tmp directory - need S3***
        
        plt.savefig('./tmp/sentiment_plot.png')
        
        # Tweet Plot
      
        #Create message for status update
        message ='New Tweet Analysis: ' + target_account + ' (Thx ' + user + '!!)'
        
        # Tweet the plot
        api.update_with_media('./tmp/sentiment_plot.png', status=message)
    
# Infinite loop
while(True):

    SentimentTweet()

    # Once tweeted, wait 5 mins before doing anything else
    time.sleep(300)





