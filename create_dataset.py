import pandas as pd

data = {
    "title": [
        "Avatar",
        "Titanic",
        "Inception",
        "The Dark Knight",
        "Interstellar",
        "Gladiator",
        "The Matrix",
        "Parasite",
        "Avengers Endgame",
        "Toy Story"
    ],
    "genres": [
        "Action",
        "Romance",
        "Sci-Fi",
        "Action",
        "Sci-Fi",
        "Action",
        "Sci-Fi",
        "Drama",
        "Action",
        "Animation"
    ],
    "year": [
        2009,
        1997,
        2010,
        2008,
        2014,
        2000,
        1999,
        2019,
        2019,
        1995
    ],
    "rating": [
        7.8,
        7.9,
        8.8,
        9.0,
        8.6,
        8.5,
        8.7,
        8.6,
        8.4,
        8.3
    ]
}

df = pd.DataFrame(data)

df.to_csv("movies_cleaned.csv", index=False)

print("movies_cleaned.csv created successfully!")
print(df)