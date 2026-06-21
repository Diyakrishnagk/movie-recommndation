import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\aiml\Movie recommendation\movie.csv")

print(movies.columns.tolist())

movies['genres'] = movies['genres'].fillna('')

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

cosine_sim = cosine_similarity(tfidf_matrix)

def recommend_movies(movie_name):
    movie_name = movie_name.lower()

    matches = movies[
        movies['title'].str.lower().str.contains(movie_name, na=False)
    ]

    if matches.empty:
        return ["Movie not found"]

    idx = matches.index[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    recommendations = []

    for i in sim_scores[1:6]:
        recommendations.append(movies.iloc[i[0]]['title'])

    return recommendations

movie = input("Enter movie name: ")

for rec in recommend_movies(movie):
    print(rec)
