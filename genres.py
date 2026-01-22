import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('top_10000_1950-now.csv')
df2 = df[['Track Name', 'Artist Name(s)', 'Artist Genres']].dropna()

print(df.info())

# Look through genre lists and create new columns with a single genre
# New genres: Rock, Pop, Hip Hop, Jazz, Classical, Country, Electronic, Other
# Classify based on presence of keywords in the genre list
def classify_genre(genre_list):
    genre_list = genre_list.lower()
    if 'rock' in genre_list or 'british invasion' in genre_list:
        return 'Rock'
    elif 'pop' in genre_list or 'boy band' in genre_list:
        return 'Pop'
    elif 'indie' in genre_list or 'alternative' in genre_list:
        return 'Indie / Alt'
    elif 'hip hop' in genre_list or 'rap' in genre_list:
        return 'Hip Hop / Rap'
    elif 'soul' in genre_list or 'r&b' in genre_list:
        return 'R&B / Soul'
    elif 'jazz' in genre_list:
        return 'Jazz'
    elif 'classical' in genre_list or 'easy listening' in genre_list:
        return 'Classical'
    elif 'country' in genre_list:
        return 'Country'
    elif 'electronic' in genre_list or 'edm' in genre_list or 'dance' in genre_list or 'funk' in genre_list or 'house' in genre_list:
        return 'Electronic'
    else: 
        return 'Other'

# Create new column with simplified genre
df2['Genre'] = df2['Artist Genres'].apply(classify_genre)
print(df2['Genre'].value_counts())

# Look at the oringal genres that were classified as 'Other'
print(df2[df2['Genre'] == 'Other']['Artist Genres'].value_counts)

# Plot the genres
plt.figure(figsize=(12, 6))
sns.countplot(data=df2, y='Genre', order=df2['Genre'].value_counts().index)
plt.title('Genres in Top 10,000 Songs (1950 - now)')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.savefig('genre_distribution.png', bbox_inches='tight')