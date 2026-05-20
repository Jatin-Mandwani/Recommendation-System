import numpy as np
import json
from movies import genre_dict, movie_vectors, genre_list

with open("movies.json", "r") as mfile:
    data = json.load(mfile)
# Genre List and Dict Updation

def genre_updation():

    while True:
        new_genre = input("\nEnter a new genre (or type 'exit' to quit): ").strip()

        if not new_genre:
            print("Genre cannot be empty")
            continue

        elif new_genre == "exit":
            break

        elif new_genre.lower() in [genre.lower() for genre in data["genre_list"]]:
            print(f"The genre '{new_genre}' already exists")
            continue

        else:
            data["genre_list"].append(new_genre)


    for i in range(len(data["genre_list"])):
        data["genre_dict"].update({data["genre_list"][i]: i})

    with open("movies.json", "w") as file:
        json.dump(data, file, indent=4)

# Input handling for Movies and Genres

def input_movies_and_genres():
    while True:
        movie_input = input("Enter movie name (or type 'exit' to quit): ").strip()

        if movie_input.lower() == "exit":
            print("Exiting Movie Input...")
            break

        elif not movie_input:
            print("Input cannot be empty!")
            continue

        else:
            zero_list = [0] * len(data["genre_list"])
            data["movie_vectors"].update({movie_input: zero_list})

        while True:
            genre_input = (input(f"Enter the genre that needs for the movie '{movie_input}' (or type 'exit' to quit): ")
                           .strip())

            if genre_input.lower() == "exit":
                print("Exiting Genre Input...")
                break

            if not genre_input:
                print("Genre cannot be empty!")
                continue

            elif genre_input.lower() not in [genre.lower() for genre in data["genre_list"]]:
                print("Genre not available! Kindly recheck")
                continue

            elif genre_input.lower() in [genre.lower() for genre in data["genre_list"]]:
                for i in range(len(data["genre_list"])):
                    data["genre_dict"].update({data["genre_list"][i]: i})

                data["movie_vectors"][movie_input][data["genre_dict"][genre_input]] = 1

    with open("movies.json", "w") as file:
        json.dump(data, file, indent=4)

# Dot Product Function

def dot(v1: list, v2: list) -> int:

    dot_product = 0

    for j in range(len(v1)):
        dot_product += v1[j] * v2[j]

    return dot_product

# Magnitude Function

def magnitude(v1: list) -> float:

    mod_value = (sum(component * component for component in v1)) ** 0.5
    return mod_value

# Cosine Similarity Function

def cosine_similarity(movie_name: str) -> dict:

    cos_values_list = []
    ref_movie_dict = data["movie_vectors"]

    if movie_name not in ref_movie_dict:
        input_movies_and_genres()

    input_movie_magnitude = magnitude(ref_movie_dict[movie_name])
    for other_movie_name in ref_movie_dict:
        if other_movie_name == movie_name:
            continue

        else:
            dot_product = dot(ref_movie_dict[movie_name], ref_movie_dict[other_movie_name])
            other_movie_magnitude = magnitude(ref_movie_dict[other_movie_name])
            cos_theta = (dot_product / (input_movie_magnitude * other_movie_magnitude))
            cos_values_list.append((other_movie_name, cos_theta))

    cos_values_list.sort(key=lambda movie_tuple: movie_tuple[1], reverse=True)
    cos_values = dict(cos_values_list)
    return cos_values