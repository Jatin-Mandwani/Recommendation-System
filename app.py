from traceback import print_tb

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

genre_dict = {}

for i in range(len(genre_list)):
    genre_dict.update({genre_list[i]: i})
