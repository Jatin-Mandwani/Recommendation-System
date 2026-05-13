import numpy as np
from movies import genre_dict, movie_vectors, genre_list

# Dot Product Function

def dot(v1: np.ndarray, v2: np.ndarray) -> int:

    dot_product = 0

    for j in range(len(v1)):
        dot_product += v1[j] * v2[j]

    return dot_product

# Magnitude Function

def magnitude(v1: np.ndarray) -> float:

    mod_value = (sum(component * component for component in v1)) ** 0.5
    return mod_value

# Cosine Similarity Function

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
