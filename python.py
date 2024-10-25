import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load the Movie Data
movies = pd.read_csv('list.csv')

# Step 2: Preprocess Data - Combine Important Features
def combine_features(row):
    return row['Genre'] + " " + row['Plot'] + " " + row['Actors']

# Fill any missing values to avoid errors
movies['Genre'] = movies['Genre'].fillna('')
movies['Plot'] = movies['Plot'].fillna('')
movies['Actors'] = movies['Actors'].fillna('')

# Create a new column with all combined features
movies['combined_features'] = movies.apply(combine_features, axis=1)

# Step 3: Convert Text to Numerical Data Using TF-IDF with Improved Parameters
tfidf = TfidfVectorizer(
    stop_words='english',
    min_df=2,  # Ignore very rare words (appear in less than 2 documents)
    max_df=0.7,  # Ignore overly common words (appear in more than 70% of the documents)
    ngram_range=(1, 2)  # Use single words and bigrams (two-word phrases)
)

# Fit and transform the data
tfidf_matrix = tfidf.fit_transform(movies['combined_features'])

# Step 4: Calculate Similarity Scores Using Cosine Similarity
similarity_matrix = cosine_similarity(tfidf_matrix)

# Step 5: Define a Function to Get Recommendations
def get_recommendations(title, movies, similarity_matrix):
    # Convert the title to lower case for matching
    title = title.lower()
    
    # Try to find the index of the movie in the dataframe
    try:
        idx = movies[movies['Title'].str.lower() == title].index[0]
    except IndexError:
        return ["Movie not found! Please check the title or try another."]
    
    # Get the similarity scores for this movie
    sim_scores = list(enumerate(similarity_matrix[idx]))
    
    # Sort movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the indices of the top 5 similar movies (excluding the input movie)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    
    # Return the titles of the top 5 similar movies
    return movies['Title'].iloc[movie_indices].tolist()

# Step 6: Test the Function
recommendations = get_recommendations("Frozen", movies, similarity_matrix)
print("Recommended Movies:", recommendations)
