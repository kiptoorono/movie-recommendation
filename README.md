# 🎬 Movie Recommendation System

A python collaborative movie recommendation system with a simple web interface. This project uses Flask for the backend, integrates with the OMDb API for movie data, and leverages Bootstrap for responsive design. Users can enjoy browsing trending movies and personalized recommendations with an intuitive interface.
## Data Set
Get the data set  here [MovieLens 25M Dataset](https://files.grouplens.org/datasets/movielens/ml-25m.zip)
## 🚀 Features

- **Personalized Recommendations**:  
  - Generate movie recommendations based on user profiles using cosine similarity between user preferences and movie genres.
  - Supports collaborative filtering to recommend movies based on similar users' preferences.

- **Data Cleaning and Preprocessing**:  
  - Automatically drops unnecessary columns (e.g., timestamps) from the dataset.
  - Cleans movie titles by removing special characters and noise.
  - Splits genres into one-hot encoded columns for efficient processing and comparison.

- **User Profile Generation**:  
  - Builds a user profile based on their movie ratings, weighting genres by the rating provided.
  - Aggregates a user's genre preferences into a weighted profile for better accuracy in recommendations.

- **Genre-Based Recommendations**:  
  - Uses cosine similarity to match a user's profile to movies based on genre attributes.
  - Outputs a ranked list of recommended movies along with their similarity scores.

- **Collaborative Filtering**:  
  - Identifies similar users based on shared high ratings for movies.
  - Recommends movies highly rated by these similar users, ensuring they aren't movies the target user has already rated.
  - Incorporates popularity scoring for recommendations based on the number of similar users who liked the movies.

- **Interactive Interface**:  
  - Browse trending movies and recommendations through a dynamic web UI built with Flask and Bootstrap.
  - Includes features such as searching for movies by title and viewing trailers.

- **Extensibility**:  
  - Ready for integrating more advanced algorithms, such as deep learning-based recommendation systems.
  - Flexible data pipeline that can handle large datasets like the MovieLens 25M dataset.


## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/movie-recommendation.git
   cd movie-recommendation
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up the OMDb API key:**

- Obtain an API key from OMDb API.
- Replace YOUR_API_KEY in app.py with your actual key.

4. **Run the flask app**

   ```bash
    flask run

   ```

5. **Run and interact with the recommendation Engine**

- The actual recommendation engine is in the recommender.ipynb Jupyter notebook

## 📜 Usage

### Homepage

- Displays a search bar and trending movies fetched from the OMDb API.

### Recommendations Page

- Displays a personalized list of movie recommendations for a given user ID.
- Movies are displayed with posters, titles, and genres.

### Movie Trailer Feature

- Watch trailers for featured movies by interacting with video controls.

---

## 📸 Screenshots

### Homepage

![Home](./flask/static/home.png)

### Recommendations Page

![Home](./flask/static/recommend.png)

---

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **API**: OMDb API for movie data
- **Styling Enhancements**: Backdrop blur, dynamic thumbnails, card layouts

---

## 🎯 Future Enhancements

- improve page layouts
- Implement a deep learning recommendation engine

## 🙌 Acknowledgments

- [OMDb API](http://www.omdbapi.com/) for providing movie data.
- [Bootstrap](https://getbootstrap.com/) for responsive design.

