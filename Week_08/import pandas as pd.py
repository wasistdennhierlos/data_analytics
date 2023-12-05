import pandas as pd
import ast

# Load the CSV file
df = pd.read_csv('goodreads_data.csv')

# Function to extract the first genre
def get_first_genre(genres):
    genres_list = ast.literal_eval(genres)
    if genres_list:
        return genres_list[0]
    else:
        return None

# Apply the function to the 'genres' column
df['First Genre'] = df['Genres'].apply(get_first_genre)

# Save the DataFrame to a new CSV file
df.to_csv('goodreads_data_prepared.csv', index=False)