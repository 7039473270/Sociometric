import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

# Function to perform sentiment analysis
def perform_sentiment_analysis(df):
    nltk.download('vader_lexicon')
    sia = SentimentIntensityAnalyzer()
    df['clean_text'] = df['Tweet'].apply(lambda x: ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", x).split()))
    df['compound'] = df['clean_text'].apply(lambda x: sia.polarity_scores(x)['compound'])
    df['sentiment'] = df['compound'].apply(lambda score: 'positive' if score >= 0 else 'negative')
    return df

#Example usage
df = pd.read_csv('tweets_data_world_Cup.csv')
df = perform_sentiment_analysis(df)
print(df.head())
