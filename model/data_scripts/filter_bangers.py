import pandas as pd

# Load the tweets data
tweets_df = pd.read_csv('data/raw/last_100_tweets_from_bangerers.csv')

# Load the accounts data
accounts_df = pd.read_csv('data/raw/banger_accounts_w_followers.csv')

# Merge the two dataframes on the username or account column (change as appropriate)
merged_df = pd.merge(tweets_df, accounts_df, on='username', how='left')

# Filter out tweets with links, replies, and RTs
merged_df = merged_df[~merged_df['tweet_text'].str.contains('http://|https://|@|RT ', na=False)]

# Define a followers/likes ratio
RATIO = 0.0084 # Getting aproximately 1/7 of the data -> TODO: test on smaller data pool w 0.0168
merged_df = merged_df[(merged_df['like_count'] / merged_df['followers']) > RATIO]

# Save the filtered data back to a new CSV
merged_df.to_csv('data/processed/filtered_banger_tweets.csv', index=False)

print("Filtered tweets saved to 'data/processed/filtered_tweets.csv'")
