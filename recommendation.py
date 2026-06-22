# Recommendation Engine

def dot(v1: list, v2: list) -> int:

    return sum(
        a * b
        for a, b in zip(v1, v2)
    )



def magnitude(v1: list) -> float:
    mod_value = (sum(component * component for component in v1)) ** 0.5
    return mod_value



def cosine_similarity(movie_name: str) -> list[tuple[str, float]] | None:
    cos_values_list = []

    validated_movie = movie_lookup(movie_name, data["movie_vectors"])

    if validated_movie is None:
        return None

    input_vector = data["movie_vectors"][validated_movie]
    input_movie_magnitude = magnitude(input_vector)
    for other_movie_name in data["movie_vectors"]:
        if other_movie_name == validated_movie:
            continue

        dot_product = dot(input_vector, data["movie_vectors"][other_movie_name])
        other_movie_magnitude = magnitude(data["movie_vectors"][other_movie_name])
        cos_theta = (dot_product / (input_movie_magnitude * other_movie_magnitude))
        cos_values_list.append((other_movie_name, cos_theta))

    cos_values_list.sort(key=lambda movie_tuple: movie_tuple[1], reverse=True)

    return cos_values_list



def recommend_movies() -> None:
    movie_name = input("Enter the movie name to get similar recommendations: ").strip()
    recommended_movies = cosine_similarity(movie_name)
    if recommended_movies is None:
        print("Movie not found.")
        return

    print()
    print("-" * 60)
    print(f"{'Movie Name':^30}|{'Score':^30}")
    print("-" * 60)
    for name, score in recommended_movies[0:5]:
        print(f"{name:^30}|{score:^30.4f}")
    print("-" * 60)
    print()
