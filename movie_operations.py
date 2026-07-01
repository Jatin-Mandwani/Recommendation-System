# Movie Input and Vector Creation

from lookup import movie_lookup, genre_lookup, find_matching_movies
from data_manager import load_json_data, save_json_data, rebuild_genre_dict

def get_movie_name(data) -> str | None:
    while True:
        movie_name = input("Enter movie name (or type 'exit' to quit): ").strip()

        if not movie_name:
            print("Input cannot be empty!")
            continue

        elif movie_name.lower() == "exit":
            print("Exiting Movie Input...")
            return None

        existing_movie = movie_lookup(movie_name, data["movie_vectors"])
        if existing_movie is not None:
            print(f"'{existing_movie}' already exists!")
            continue

        print(f"You entered '{movie_name}'")
        return movie_name



def get_movie_vector(movie_name: str, data) -> list:
    genre_dict = rebuild_genre_dict(data["genre_list"])
    binary_vector = [0] * len(data["genre_list"])

    while True:
        genre_input = (input(f"Enter the genre of the movie '{movie_name}' (or type 'exit' to quit): ")
                       .strip())

        if not genre_input:
            print("Genre cannot be empty!")
            continue

        elif genre_input.lower() == "exit":
            print("Exiting Genre Input...")
            break

        validated_genre = genre_lookup(genre_input, data["genre_list"])
        if validated_genre is None:
            print("Genre not available! Kindly recheck")
            continue

        binary_vector[genre_dict[validated_genre]] = 1
        print(f"You entered '{validated_genre}' genre to the movie '{movie_name}'")

    return binary_vector



def search_movie() -> None:
    data = load_json_data()
    searched_movie = input("Enter movie name: ").strip()

    if not searched_movie:
        print("Input movie cannot be empty!")
        return


    validated_movie = find_matching_movies(searched_movie, data["movie_vectors"])
    if validated_movie is None:
        return

    result_genre_list = [
        data["genre_list"][i]
        for i, item in enumerate(data["movie_vectors"][validated_movie])
        if item == 1
    ]

    print("\nName: {}\n"
          "Genres:- \n{}".format(validated_movie,
                                 "\n".join("{}. {}".format(i + 1, genre)
                                           for i, genre in enumerate(result_genre_list))))



def filter_movies_by_genre() -> None:
    data = load_json_data()
    filtered_genre_list = []
    genre_dict = rebuild_genre_dict(data["genre_list"])

    while True:
        filter_genre = input("Enter the genre to get filtered suggestions (or type 'exit' to quit): ")

        if not filter_genre:
            print("Genre cannot be empty!")
            continue

        elif filter_genre.lower() == 'exit':
            break

        validated_genre = genre_lookup(filter_genre, data["genre_list"])

        if validated_genre is None:
            print(f"Genre '{filter_genre}' not found!")
            continue

        elif validated_genre in filtered_genre_list:
            print(f"Genre '{validated_genre}' already entered!")
            continue

        else:
            filtered_genre_list.append(validated_genre)

    if not filtered_genre_list:
        print("No genres entered!")
        return

    matching_movies = [
        movie
        for movie, vectors in data["movie_vectors"].items()
        if all(vectors[genre_dict[genre]] == 1 for genre in filtered_genre_list)
    ]

    if matching_movies:
        print("\n----------Movies/Shows based on the genres----------\n")

        for i, movie in enumerate(matching_movies, start=1):
            print(f"{i}) {movie}")
    else:
        print("No Movies/Shows Found!")



def add_movies() -> None:
    data = load_json_data()
    while True:
        movie_name = get_movie_name(data)

        if movie_name is None:
            break

        binary_vector = get_movie_vector(movie_name, data)

        if all(genre_values == 0 for genre_values in binary_vector):
            print(f"{movie_name} cannot be saved as no genre was associated with it!")
            continue

        data["movie_vectors"][movie_name] = binary_vector
        save_json_data(data)
