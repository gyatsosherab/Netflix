# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!

# Load the CSV file and store as netflix_df.
netflix_df = pd.read_csv("netflix_data.csv")
#print(netflix_df)

# To get unique movie type
# movie_types = netflix_df['type'].unique()
# print("Unique types of movies:")
# for movie_type in movie_types:
#     print(movie_type)

# Filter the data to remove TV shows and store as netflix_subset.
netflix_subset = netflix_df[netflix_df['type'] == 'Movie']
#print(netflix_subset)

# Investigate the Netflix movie data
netflix_movies = netflix_subset.loc[:, ["title", "country", "genre", "release_year", "duration"]]
# Displaying the first few rows of the new DataFrame
#print(netflix_movies.head())

# Filter netflix_movies shoter than 60 minutes
short_movies = netflix_movies[netflix_movies['duration'] < 60]

# List to store assigned colors for each movie based on genre groups
colors = []

# Assigning colors based on genre groups for each movie
for index, row in netflix_movies.iterrows():
    genre = row['genre']
    if genre == "Children":
        colors.append('green')  # Assigning green for Children genre
    elif genre == "Documentaries":
        colors.append('red')    # Assigning red for Documentaries genre 
    elif genre == "Stand-Up":
        colors.append('blue')   # Assigning blue for Stand-Up genre
    else:
        colors.append('gray')   # Assigning gray for Other genres
        
# Creating a Scatter plot
fig, ax = plt.subplots()
ax.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)

# Adding labels and title to the plot
ax.set_xlabel('Release year')
ax.set_ylabel('Duration (min)')
ax.set_title('Movie Duration by Year of Release')



answer = 'maybe'
