# popularity_prediction.py
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Function to predict popularity
def predict_popularity(df):
    X_train, X_test, y_train, y_test = train_test_split(df['clean_text'], df['likes'], test_size=0.2, random_state=42)
    vectorizer = CountVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = LinearRegression()
    model.fit(X_train_vec, y_train)

    predictions = model.predict(X_test_vec)
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')

# Example usage
# df = pd.read_csv('tweets.csv')
# predict_popularity(df)
