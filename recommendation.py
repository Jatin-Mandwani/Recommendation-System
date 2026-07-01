# Recommendation Engine

from data_manager import load_json_data
from lookup import find_matching_movies

def dot(v1: list, v2: list) -> int:

    return sum(
        a * b
        for a, b in zip(v1, v2)
    )



def magnitude(v1: list) -> float:
    mod_value = (sum(component * component for component in v1)) ** 0.5
    return mod_value



def cosine_similarity(movie_name: str) -> list[tuple[str, float]] | None:
    data = load_json_data()
    cos_values_list = []

    input_vector = data["movie_vectors"][movie_name]
    input_movie_magnitude = magnitude(input_vector)
    for other_movie_name in data["movie_vectors"]:
        if other_movie_name == movie_name:
            continue

        dot_product = dot(input_vector, data["movie_vectors"][other_movie_name])
        other_movie_magnitude = magnitude(data["movie_vectors"][other_movie_name])
        cos_theta = (dot_product / (input_movie_magnitude * other_movie_magnitude))
        cos_values_list.append((other_movie_name, cos_theta))

    cos_values_list.sort(key=lambda movie_tuple: movie_tuple[1], reverse=True)

    return cos_values_list



def recommend_movies() -> None:
    data = load_json_data()

    while True:
        movie_name = input("Enter the movie name to get similar recommendations: ").strip()
        if not movie_name:
            print("Input movie cannot be empty!")
            continue

        movie_result = find_matching_movies(movie_name, data["movie_vectors"])

        if movie_result is None:
            continue

        break


    recommended_movies = cosine_similarity(movie_result)
    print()
    print("-" * 60)
    print(f"{'Movie Name':^30}|{'Score':^30}")
    print("-" * 60)
    for name, score in recommended_movies[0:5]:
        print(f"{name:^30}|{score:^30.4f}")
    print("-" * 60)
    print()
