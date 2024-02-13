import pandas as pd
# Function to read tweets from CSV file
def read_tweets_from_csv(file_path='tweets_data_world_Cup.csv'):
    try:
        # Read CSV file into a DataFrame
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# Example usage
# Replace 'your_file_path.csv' with the actual file path if it's different
df_read = read_tweets_from_csv('tweets.csv')

# Display the DataFrame (optional)
if df_read is not None:
    print(df_read.head())  # Display the first few rows of the DataFrame
