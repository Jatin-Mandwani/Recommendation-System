import numpy as np

genre_list = np.array([
    "Action",
    "Adventure",
    "Animation",
    "Comedy",
    "Crime",
    "Documentary",
    "Drama",
    "Family",
    "Horror",
    "Musical",
    "Mystery",
    "Romance",
    "Sci-Fi",
    "Superhero",
    "Thriller"
])

for i in range(len(genre_list)):
    print(f"{i}: {genre_list[i]}")