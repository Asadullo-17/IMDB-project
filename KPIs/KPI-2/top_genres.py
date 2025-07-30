df_genres=df.explode('Genres')
top_genres=(
    df_genres.groupby('Genres')['Box_office'].mean().sort_values(ascending=False).head(10)
)

plt.figure(figsize=(10, 6))
top_genres.plot(kind='barh', color='lightgreen')
plt.xlabel('Average Box Office (in Billions $)')
plt.title('Top 10 Genres by Average Box Office (IMDb Top 250)')
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.xticks(rotation=0)
plt.show()
