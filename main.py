import pandas as pd
from matplotlib import pyplot as plt
from matplotlib_venn import venn2
import seaborn as sns
from wordcloud import WordCloud 
from wordcloud import STOPWORDS
from collections import Counter

# Load & View Data
# df_colors = pd.read_csv('MTA_Colors.cvs')
# df_riders = pd.read_csv('MTA_DailyRidershipData.csv')
df = pd.read_csv('top_10000_1950-now.csv')

# print(df.info())

# Histogram
# hours = [17, 20, 22, 25, 26, 27, 30, 31, 32, 38, 40, 40, 45, 55]

# Initialize layout
# fig, ax = plt.subplots(figsize = (9, 9))

# plot
# ax.hist(hours, bins=5, edgecolor="black");

# WorldCloud
color = sns.cubehelix_palette(as_cmap=True)

# Create a list of word
word_list = df['Track Name'].dropna()

# print(word_list)
track_list = word_list.values
print(track_list)

tracks = Counter(track_list)

# track_str = ' '.join(track for track in track_list.split())

# Create the wordcloud object
wordcloud = WordCloud(width=1600, height=1200, margin=0, background_color="white", colormap=color).generate_from_frequencies(tracks)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
# plt.title("Frequency of Song Titles", fontsize=26, color='#bf7c99')

plt.savefig('wordcloud.png')
plt.close()

# Check if the frequency shown in the graph is accurate
# counts = df['Track Name'].value_counts()
# print(counts)

''' 
# Venn diagram 
artists_2000 = df['Artist Name(s)']
artists_2010 = df['Artist Name(s)']

# TODO: Convert series to set for my data
series1 = 
series2 = 

# Convert to SETS to identify items in common, unique, etc. 
set1 = set(series1)
set2 = set(series2)

# Calculate interesection and differences for labels
only_1 = set1 - set2
only_2 = set2 - set1
both = set1 & set2

# Create the plot
plt.figure(figsize=(8,6))
v = venn2([set1, set2], set_labels=('Set 1', 'Set 2'))

# Use the venn2 function
v.get_label_by_id('10').set_text('\n'.join(only_1))
v.get_label_by_id('01').set_text('\n'.join(only_2))
v.get_label_by_id('11').set_text('\n'.join(both))


plt.savefig('venn.png', bbox_inches='tight')
plt.close()
'''

