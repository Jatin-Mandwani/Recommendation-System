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
movie_vectors = {}

for i in range(len(genre_list)):
    genre_dict.update({genre_list[i]: i})

while True:
    movie_input = input("Enter movie name (or type 'exit' to quit): ").strip()

    if movie_input.lower() == "exit":
        print("Exiting Movie Input...")
        break

    elif not movie_input:
        print("Input cannot be empty!")
        continue

    else:
        movie_vectors.update({movie_input: np.zeros(len(genre_dict), dtype=int)})


    while True:
        genre_input = input(f"Enter the genre that needs for the movie '{movie_input}': ")

        if genre_input.lower() == "exit":
            print("Exiting Genre Input...")
            break

        elif genre_input.lower() in [genre.lower() for genre in genre_list]:
            movie_vectors[movie_input][genre_dict[genre_input]] = 1


for movie in movie_vectors:
    print(f"{movie}: {movie_vectors[movie]}")