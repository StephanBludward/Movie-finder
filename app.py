from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, render_template

app = Flask(__name__)

# Load data and compute similarity
movies = pd.read_csv('list.csv')
movies['combined_features'] = movies['Genre'] + " " + movies['Plot'] + " " + movies['Actors']
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['combined_features'])
similarity_matrix = cosine_similarity(tfidf_matrix)

# Helper function to get recommendations
def get_recommendations(title):
    # Convert input title and movie titles to lowercase for case-insensitive search
    title_lower = title.lower()
    movies['Title_lower'] = movies['Title'].str.lower()
    
    if title_lower not in movies['Title_lower'].values:
        return ["Movie not found! Try a different one."]
    
    idx = movies.index[movies['Title_lower'] == title_lower].tolist()
    if not idx:
        return ["Movie not found! Try a different one."]
    idx = idx[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Get top 5 similar movies
    movie_indices = [i[0] for i in sim_scores]
    return movies['Title'].iloc[movie_indices].tolist()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['GET'])
def recommend():
    title = request.args.get('title')
    if not title:
        return render_template('recommendations.html', movies=["No title provided. Please try again."])
    recommendations = get_recommendations(title)
    return render_template('recommendations.html', movies=recommendations, title=title)


if __name__ == '__main__':
    app.run(debug=True)
