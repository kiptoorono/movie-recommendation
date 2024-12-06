from flask import Flask, render_template, request
import pandas as pd
import requests

app = Flask(__name__)

ratings=pd.read_csv(r'E:\Python\Movie Recomendation System\ml-25m\ml-25m\ratings.csv')
movies=pd.read_csv(r'E:\Python\Movie Recomendation System\ml-25m\ml-25m\movies.csv')

# Extract year and clean movie titles
movies['year'] = movies['title'].str.extract(r'\((\d{4})\)')
movies['title'] = movies['title'].str.replace(r'\(\d{4}\)', '', regex=True).str.strip()

# Define the collaborative filtering function
def collaborative_filtering_by_user(user_id, ratings, movies, threshold=0.10, top_n=10):
    target_user_rated_movies = ratings[(ratings["userId"] == user_id) & (ratings["rating"] > 4)]["movieId"]

    if target_user_rated_movies.empty:
        return pd.DataFrame(columns=["title", "genres"])
    
    similar_users = ratings[(ratings["movieId"].isin(target_user_rated_movies)) & (ratings["rating"] > 4)]["userId"].unique()
    similar_user_recs = ratings[(ratings["userId"].isin(similar_users)) & (ratings["rating"] > 4)]["movieId"]
    similar_user_recs = similar_user_recs.value_counts() / len(similar_users)
    similar_user_recs = similar_user_recs[~similar_user_recs.index.isin(target_user_rated_movies)]
    similar_user_recs = similar_user_recs[similar_user_recs > threshold]
    all_users = ratings[(ratings["movieId"].isin(similar_user_recs.index)) & (ratings["rating"] > 4)]
    all_user_recs = all_users["movieId"].value_counts() / len(all_users["userId"].unique())
    rec_percentages = pd.concat([similar_user_recs, all_user_recs], axis=1)
    rec_percentages.columns = ["similar", "all"]
    rec_percentages["score"] = rec_percentages["similar"] / rec_percentages["all"]
    rec_percentages = rec_percentages.sort_values("score", ascending=False)
    recommendations = rec_percentages.head(top_n).merge(movies, left_index=True, right_on="movieId")[["title", "genres", "year"]]
    return recommendations

# Fetch movie posters from OMDB API
def fetch_movie_poster(title, year=None):
    api_key = "af106882"
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}&y={year}" if year else f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            return data.get("Poster", "/static/no_poster.png")
    return "/static/no_poster.png"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = int(request.form['user_id'])
    recommendations = collaborative_filtering_by_user(user_id, ratings, movies)

    if recommendations.empty:
        return render_template('no_recommendations.html', user_id=user_id)

    # Fetch posters for the recommended movies
    movie_data = []
    for _, row in recommendations.iterrows():
        poster = fetch_movie_poster(row['title'], row['year'])
        movie_data.append({
            'title': row['title'],
            'genres': ', '.join(row['genres']),
            'poster': poster
        })

    return render_template('recommendations.html', user_id=user_id, recommendations=movie_data)

if __name__ == '__main__':
    app.run(debug=True)
