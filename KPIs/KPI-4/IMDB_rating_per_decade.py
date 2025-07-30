df['Decade'] = (df['Year'] // 10) * 10

avg_rating_decade = df.groupby('Decade')['Imdb_rating'].mean()


plt.figure(figsize=(10, 6))
avg_rating_decade.plot(kind='bar', color='teal')
plt.xlabel('Decade')
plt.ylabel('Average IMDb Rating')
plt.title('Average IMDb Rating by Decade (Top 250 Movies)')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

