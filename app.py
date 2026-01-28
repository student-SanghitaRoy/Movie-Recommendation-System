from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
import requests
import os
from dotenv import load_dotenv

load_dotenv()

OMDB_API_KEY = os.getenv("MOVIE_API_KEY")


app = Flask(__name__)


# Load Pickle Files


movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

def fetch_poster(movie_title):
    try:
        url = f"https://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
        response = requests.get(url, timeout=5)
        data = response.json()

        poster = data.get("Poster")

        if poster and poster != "N/A":
            return poster
        else:
            return "https://via.placeholder.com/300x450?text=No+Poster"

    except:
        return "https://via.placeholder.com/300x450?text=No+Poster"


# Convert to DataFrame


if not isinstance(movies, pd.DataFrame):
    movies = pd.DataFrame(movies)


# Auto Detect Movie Title Column


possible_cols = ["title", "movie_title", "name", "original_title"]

movie_col = None

for col in possible_cols:
    if col in movies.columns:
        movie_col = col
        break

# If still not found, pick first string column
if movie_col is None:
    for col in movies.columns:
        if movies[col].dtype == object:
            movie_col = col
            break

print("Movie title column detected as:", movie_col)


# Recommendation Function


def recommend(movie_name):

    try:
        index = movies[movies[movie_col] == movie_name].index[0]
    except:
        return []

    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movie_list:
        movie_title = movies.iloc[i[0]][movie_col]
        
        poster = fetch_poster(movie_title)

        recommendations.append({
            "title": movie_title,
            "poster": poster
        })

    return recommendations




# Routes


@app.route("/recommend", methods=["POST"])
def get_recommendation():

    selected_movie = request.form.get("movie")

    print("Selected movie:", selected_movie)

    if selected_movie is None or selected_movie == "":
        return render_template(
            "index.html",
            movie_list=movies[movie_col].values,
            error="No movie selected"
        )

    recommendations = recommend(selected_movie)

    print("Recommendations:", recommendations)

    return render_template(
        "index.html",
        movie_list=movies[movie_col].values,
        selected_movie=selected_movie,
        recommendations=recommendations
    )




# Run App



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)




