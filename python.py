from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import random

# Load your movies data
movies = pd.read_csv('list.csv')  # Make sure this CSV file is in your project directory
# Replace any NaNs with empty strings to avoid errors
movies['Title'] = movies['Title'].fillna('')
movies['Genre'] = movies['Genre'].fillna('')
movies['Plot'] = movies['Plot'].fillna('')
movies['Actors'] = movies['Actors'].fillna('')

# Create combined features column
movies['combined_features'] = movies['Genre'] + " " + movies['Plot'] + " " + movies['Actors']

# Re-initialize the sample data for generating movie entries
titles = [
    "Inception", "The Matrix", "The Godfather", "Pulp Fiction", "Forrest Gump", 
    "The Dark Knight", "Titanic", "The Shawshank Redemption", "Avengers: Endgame", 
    "Gladiator", "Interstellar", "The Lion King", "Jurassic Park", "Star Wars", 
    "The Lord of the Rings", "Back to the Future", "Fight Club", "The Terminator", 
    "Die Hard", "Harry Potter", "The Silence of the Lambs", "Casablanca", "Schindler's List",
    "The Departed", "Braveheart", "Mad Max: Fury Road", "The Big Lebowski", "Jaws", 
    "Goodfellas", "The Godfather Part II", "Alien", "The Usual Suspects", "Saving Private Ryan",
    "The Green Mile", "The Prestige", "12 Angry Men", "Whiplash", "Django Unchained", 
    "La La Land", "Shutter Island", "Avatar", "The Social Network", "The Wolf of Wall Street",
    "Rocky", "Gone with the Wind", "The Wizard of Oz", "The Shining", "Psycho", "Scarface",
    "Blade Runner 2049", "Toy Story", "Finding Nemo", "Frozen", "The Incredibles", "Moana",
    "Coco", "Inside Out", "Aladdin", "Beauty and the Beast", "Mulan", "A Quiet Place",
    "It", "Get Out", "Her", "Moonlight", "The Revenant", "Black Panther", "Wonder Woman",
    "The Irishman", "Once Upon a Time in Hollywood", "Parasite", "Joker", "Knives Out",
    "Spider-Man: Into the Spider-Verse", "Deadpool", "Guardians of the Galaxy", "Doctor Strange",
    "Ant-Man", "Captain Marvel", "Thor: Ragnarok", "Logan", "X-Men", "Justice League",
    "Superman", "The Hunger Games", "Divergent", "Twilight", "The Fault in Our Stars",
    "A Star is Born", "Bohemian Rhapsody", "Rocketman", "The Greatest Showman", "Grease",
    "Footloose", "Singin' in the Rain", "Mary Poppins", "West Side Story", "Hamilton",
    "Les Misérables", "The Sound of Music", "Mamma Mia!", "La La Land", "Moulin Rouge!"
]

genres = [
    "Action", "Drama", "Comedy", "Sci-Fi", "Fantasy", "Romance", "Thriller", 
    "Adventure", "Crime", "Horror", "Mystery", "Animation", "Family", "Musical"
]

actors = [
    "Leonardo DiCaprio", "Tom Hanks", "Robert De Niro", "Al Pacino", "Meryl Streep",
    "Scarlett Johansson", "Chris Hemsworth", "Natalie Portman", "Christian Bale",
    "Brad Pitt", "Angelina Jolie", "Samuel L. Jackson", "Denzel Washington", 
    "Emma Stone", "Ryan Gosling", "Morgan Freeman", "Johnny Depp", "Kate Winslet",
    "Keanu Reeves", "Robert Downey Jr.", "Jennifer Lawrence", "Chris Evans", 
    "Anne Hathaway", "Will Smith", "Margot Robbie", "Matt Damon", "Sandra Bullock",
    "Hugh Jackman", "Joaquin Phoenix", "Gal Gadot"
]

# Function to create a random movie plot
def generate_plot():
    actions = ["saves", "discovers", "faces", "battles", "finds", "explores", "challenges"]
    themes = ["a secret world", "his destiny", "an ancient curse", "a hidden power", "a great love", 
              "a mysterious disappearance", "a time loop", "a galactic war", "a haunted house", "a parallel universe"]
    return f"A {random.choice(genres).lower()} story where the protagonist {random.choice(actions)} {random.choice(themes)}."

# Generate 10,000 movie entries
movies_data_large = []
for _ in range(10000):
    title = random.choice(titles)
    genre = "|".join(random.sample(genres, k=random.randint(1, 3)))
    plot = generate_plot()
    actor_list = "|".join(random.sample(actors, k=2))
    movies_data_large.append([title, genre, plot, actor_list])

# Create a DataFrame
df_large = pd.DataFrame(movies_data_large, columns=["Title", "Genre", "Plot", "Actors"])

# Save to a new CSV file
csv_path_large = (r'c:\Users\Dota2007\Documents\GitHub\Movies\list.csv')
df_large.to_csv(csv_path_large, index=False)

csv_path_large
print(movies.head())