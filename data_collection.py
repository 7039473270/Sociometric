# data_collection.py
import os
from dotenv import load_dotenv
import tweepy
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Set up Twitter API credentials
consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
access_token = os.getenv('TWITTER_ACCESS_TOKEN')
access_secret = os.getenv('TWITTER_ACCESS_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Function to collect tweets
def collect_tweets(query, num_tweets=100):
    tweets = tweepy.Cursor(api.search, q=query, lang='en').items(num_tweets)
    data = {'text': [], 'likes': [], 'retweets': []}

    for tweet in tweets:
        data['text'].append(tweet.text)
        data['likes'].append(tweet.favorite_count)
        data['retweets'].append(tweet.retweet_count)

    df = pd.DataFrame(data)
    return df

# Example usage
# df = collect_tweets('your_search_query')
# df.to_csv('tweets.csv', index=False)
