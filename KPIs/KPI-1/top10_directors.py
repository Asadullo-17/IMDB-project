top_directors=(
    df.groupby('Director')['Imdb_rating'].mean().sort_values(ascending=False).head(10)
    
)

plt.figure(figsize=(10, 6))
top_directors.plot(kind='barh', color='skyblue')
plt.xlabel('Average IMDb Rating')
plt.title('Top 10 Directors by Average IMDb Rating (IMDb Top 250)')
plt.gca().invert_yaxis()  # highest on top
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
