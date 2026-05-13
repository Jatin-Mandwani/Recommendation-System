import numpy as np

def dot(v1: np.ndarray, v2: np.ndarray) -> int:

    dot_product = 0

    for j in range(len(v1)):
        dot_product += v1[j] * v2[j]

    return dot_product

def magnitude(v1: np.ndarray) -> float:

    mod_value = (sum(component * component for component in v1)) ** 0.5
    return mod_value

def cosine_similarity(movie_name: str) -> dict:

    cos_values_list = []

    if movie_name not in movie_vectors:
        pass

    input_movie_magnitude = magnitude(movie_vectors[movie_name])
    for other_movie_name in movie_vectors:
        if other_movie_name == movie_name:
            continue

        else:
            dot_product = dot(movie_vectors[movie_name], movie_vectors[other_movie_name])
            other_movie_magnitude = magnitude(movie_vectors[other_movie_name])
            cos_theta = (dot_product / (input_movie_magnitude * other_movie_magnitude))
            cos_values_list.append((other_movie_name, cos_theta))

    cos_values_list.sort(key=lambda movie_tuple: movie_tuple[1], reverse=True)
    cos_values = dict(cos_values_list)
    return cos_values


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

        if not genre_input:
            print("Genre cannot be empty!")
            continue

        elif genre_input.lower() not in [genre.lower() for genre in genre_list]:
            print("Genre not available! Kindly recheck")
            continue

        elif genre_input.lower() in [genre.lower() for genre in genre_list]:
            movie_vectors[movie_input][genre_dict[genre_input]] = 1


for movie in movie_vectors:
    print(f"{movie}: {movie_vectors[movie]}")