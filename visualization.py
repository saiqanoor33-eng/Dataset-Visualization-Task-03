import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv(r"C:\Users\DELL\Desktop\task\DA\movies_cleaned.csv")
genre_counts = df["genres"].value_counts()

plt.figure(figsize=(8, 5))
genre_counts.plot(kind="bar")
plt.title("Number of Movies by Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("01_movies_by_genre.png")
plt.show()
year_counts = df["year"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
plt.plot(year_counts.index, year_counts.values, marker="o")
plt.title("Number of Movies by Year")
plt.xlabel("Year")
plt.ylabel("Number of Movies")
plt.grid(True)
plt.tight_layout()
plt.savefig("02_movies_by_year.png")
plt.show()
def rating_category(rating):
    if rating >= 8:
        return "Excellent (8+)"
    elif rating >= 7:
        return "Good (7-7.9)"
    else:
        return "Average (<7)"


df["rating_category"] = df["rating"].apply(rating_category)

rating_counts = df["rating_category"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(
    rating_counts.values,
    labels=rating_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Movie Rating Categories")
plt.tight_layout()
plt.savefig("03_rating_categories.png")
plt.show()


plt.figure(figsize=(8, 5))
plt.hist(df["rating"], bins=5, edgecolor="black")
plt.title("Distribution of Movie Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig("04_rating_distribution.png")
plt.show()
plt.figure(figsize=(8, 5))
plt.scatter(df["year"], df["rating"])
plt.title("Movie Year vs Rating")
plt.xlabel("Year")
plt.ylabel("Rating")
plt.grid(True)
plt.tight_layout()
plt.savefig("05_year_vs_rating.png")
plt.show()

print("All 5 visualizations created successfully!")