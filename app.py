from flask import Flask, render_template, request
import pickle
import pandas as pd
import requests
import os
from urllib.parse import quote
from dotenv import load_dotenv


# Load Environment Variables


load_dotenv()
OMDB_API_KEY = os.getenv("MOVIE_API_KEY")

app = Flask(__name__)


# Load Data


movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# Ensure movies is DataFrame
if not isinstance(movies, pd.DataFrame):
    movies = pd.DataFrame(movies)


# Auto Detect Movie Title Column


possible_cols = ["title", "movie_title", "name", "original_title"]
movie_col = None

for col in possible_cols:
    if col in movies.columns:
        movie_col = col
        break

if movie_col is None:
    for col in movies.columns:
        if movies[col].dtype == object:
            movie_col = col
            break

print("Movie title column detected as:", movie_col)


# Fetch Poster Function

def fetch_poster(movie_title):
    try:
        safe_title = quote(movie_title)
        url = f"https://www.omdbapi.com/?s={safe_title}&apikey={OMDB_API_KEY}"
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("Search"):
            poster = data["Search"][0].get("Poster")
            if poster and poster != "N/A":
                return poster

        return "https://via.placeholder.com/300x450?text=No+Poster"

    except:
        return "https://via.placeholder.com/300x450?text=No+Poster"


# Recommendation Function


def recommend(movie_name):

    movie_name = movie_name.strip()

    # Case-insensitive matching
    matched = movies[movies[movie_col].str.lower() == movie_name.lower()]

    if matched.empty:
        return None   # Movie not found

    index = matched.index[0]
    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]   # Skip itself

    recommendations = []

    for i in movie_list:
        movie_title = movies.iloc[i[0]][movie_col]
        poster = fetch_poster(movie_title)
        similarity_score = round(i[1], 3)

        recommendations.append({
            "title": movie_title,
            "poster": poster,
            "score": similarity_score
        })

    return recommendations


# Routes

@app.route("/")
def home():
    movie_names = movies[movie_col].values
    return render_template(
        "index.html",
        movie_list=movie_names
    )

@app.route("/recommend", methods=["POST"])
def get_recommendation():

    selected_movie = request.form.get("movie")

    # Empty input check
    if not selected_movie:
        return render_template(
            "index.html",
            movie_list=movies[movie_col].values,
            error="Please select or enter a movie."
        )

    recommendations = recommend(selected_movie)

    # Movie not found check
    if recommendations is None:
        return render_template(
            "index.html",
            movie_list=movies[movie_col].values,
            error=f'"{selected_movie}" not found in our dataset.'
        )

    return render_template(
        "index.html",
        movie_list=movies[movie_col].values,
        selected_movie=selected_movie,
        recommendations=recommendations
    )


# Run App


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)