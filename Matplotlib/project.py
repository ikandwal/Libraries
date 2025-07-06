import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r'Matplotlib/netflix_titles.csv')
df = df.dropna(subset=['type', 'country', 'release_year','duration', 'rating'])
# Bar Chart
# type_counts = df['type'].value_counts()
# plt.figure(figsize=(6,4))
# plt.bar(type_counts.index, type_counts.values, color=['blue', 'orange'])
# plt.xlabel('Type')
# plt.ylabel('Count')
# plt.title('Distribution of Content Types on Netflix')
# plt.tight_layout()
# plt.savefig('content_types_distribution.png', dpi=300, bbox_inches='tight')
# plt.show()

rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,6))
#plt.pie(type_count.index, type_count.values, color=['skyblue', 'orange'])
plt.pie(rating_counts.values, labels=rating_counts.index, autopct='%1.1f%%', startangle=90, colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Distribution of Ratings on Netflix')
plt.tight_layout()
plt.savefig('ratings_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# Histogram
movie_df= df[df['type'] == 'Movie'].copy()
movie_df['duration'] = movie_df['duration'].str.replace(' min', '').astype(int)
plt.figure(figsize=(10,6))
plt.hist(movie_df['duration'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Duration (minutes)')    
plt.ylabel('Frequency')
plt.title('Distribution of Movie Durations on Netflix') 
plt.tight_layout()
plt.savefig('movie_durations_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# Scatter Plot
plt.figure(figsize=(10,6))
release_year_counts = df['release_year'].value_counts().sort_index()
plt.scatter(release_year_counts.index, release_year_counts.values, color='blue', marker='o')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.title('Number of Titles Released Each Year on Netflix')
plt.grid(True, linestyle='--', alpha=0.5)   
plt.tight_layout()
plt.savefig('titles_per_year.png', dpi=300, bbox_inches='tight')
plt.show()


# Pie Chart
country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(10,8))
plt.barh(country_counts.index, country_counts.values, color='skyblue', edgecolor='black')
plt.title('Top 10 Countries with Most Titles on Netflix')
plt.tight_layout()
plt.savefig('top_countries_titles.png', dpi=300, bbox_inches='tight')

plt.show()

content_by_year = df.groupby('release_year')['type'].value_counts().unstack().fillna(0)
fig,ax = plt.subplots(1,2,figsize=(12, 8))

ax[0].plot(content_by_year.index, content_by_year['Movie'], label='Movies', color='blue')
ax[0].plot(content_by_year.index, content_by_year['TV Show'], label='TV Shows', color='orange')
ax[0].set_xlabel('Release Year')
ax[0].set_ylabel('Number of Titles')
ax[0].set_title('Number of Movies and TV Shows Released Each Year on Netflix')
ax[0].legend()
ax[0].grid(True, linestyle='--', alpha=0.5)
ax[1].bar(content_by_year.index, content_by_year['Movie'], label='Movies', color='blue', alpha=0.6)
ax[1].bar(content_by_year.index, content_by_year['TV Show'], label='TV Shows', color='orange', alpha=0.6, bottom=content_by_year['Movie'])
ax[1].set_xlabel('Release Year')    
ax[1].set_ylabel('Number of Titles')
ax[1].set_title('Stacked Bar Chart of Movies and TV Shows Released Each Year on Netflix')
ax[1].legend()
ax[1].grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
fig.suptitle('Comparison of Movies and TV Shows Released Each Year on Netflix', fontsize=16)
plt.savefig('movies_vs_tvshows_per_year.png', dpi=300, bbox_inches='tight')
plt.show()


