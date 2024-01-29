# main.py
from data_collection import collect_tweets
from sentiment_analysis import perform_sentiment_analysis
from popularity_prediction import predict_popularity

# Example usage
query = 'your_search_query'
num_tweets = 100

# Collect tweets
df = collect_tweets(query, num_tweets)
df.to_csv('tweets.csv', index=False)

# Perform sentiment analysis
df = perform_sentiment_analysis(df)
print(df.head())

# Predict popularity
predict_popularity(df)
