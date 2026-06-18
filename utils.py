import json

# Saving content to JSON file

def save_json_data(json_data: dict):
    with open("movies.json", "w") as json_file:
        json.dump(json_data, json_file, indent=4)

# Loading content from JSON file

def load_json_data() -> dict:
    with open("movies.json", "r") as json_file:
        return json.load(json_file)


data = load_json_data()

# Genre to Index Mapping in Dict

def rebuild_genre_dict(genre_list: list[str]) -> dict[str, int]:

    return {
        genre: i
        for i, genre in enumerate(genre_list)
    }

genre_dict = rebuild_genre_dict(data["genre_list"])

# Genre Case Sensitivity Handling

def genre_lookup(genre: str, genre_list: list) -> str | None:
    for item in genre_list:
        if genre.lower() == item.lower():
            return item

    return None

# Movie/Show Name Case Sensitivity Handling

def movie_lookup(movie_name: str, movie_dict: dict) -> str | None:
    for item in movie_dict:
        if movie_name.lower() == item.lower():
            return item

    return None

# Genre List and Dict Updation

def genre_updation():
    global genre_dict

    while True:

        print("\nHow would you like to update the genre list: \n"
              "1) Add genre to the genre list (Press 1)\n"
              "2) Remove genre from the genre list (Press 2)\n"
              "3) Exit (Press 3)")

        task_input = int(input("Enter here: "))

        match task_input:

            case 1:
                new_genre = input("\nEnter a new genre (or type 'exit' to quit): ").strip()

                if not new_genre:
                    print("Genre cannot be empty")
                    continue

                existing_genre = genre_lookup(new_genre, data["genre_list"])
                if existing_genre is not None:
                    print(f"The genre '{existing_genre}' already exists")
                    continue

                data["genre_list"].append(new_genre)
                print(f"You entered '{new_genre}' as a new genre")
                genre_dict = rebuild_genre_dict(data["genre_list"])
                continue

            case 2:
                remove_genre = input("\nEnter the genre to be removed: ").strip()

                if not remove_genre:
                    print("Genre cannot be empty")
                    continue

                genre_to_remove = genre_lookup(remove_genre, data["genre_list"])
                if genre_to_remove is None:
                    print(f"'{remove_genre}' does not exist")
                    continue

                data["genre_list"].remove(genre_to_remove)
                print(f"You removed '{genre_to_remove}' from the list")
                genre_dict = rebuild_genre_dict(data["genre_list"])
                continue

            case 3:
                save_json_data(data)
                break

# Input handling for Movies and Genres

def input_movies_and_genres():
    while True:
        movie_input = input("Enter movie name (or type 'exit' to quit): ").strip()

        if not movie_input:
            print("Input cannot be empty!")
            continue

        elif movie_input.lower() == "exit":
            print("Exiting Movie Input...")
            break

        existing_movie = movie_lookup(movie_input, data["movie_vectors"])
        if existing_movie is not None:
            print(f"'{existing_movie}' already exists!")
            continue

        zero_list = [0] * len(data["genre_list"])
        print(f"You entered '{movie_input}' movie")

        while True:
            genre_input = (input(f"Enter the genre of the movie '{movie_input}' (or type 'exit' to quit): ")
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

            zero_list[genre_dict[validated_genre]] = 1
            print(f"You entered '{validated_genre}' genre to the movie '{movie_input}'")

        if all(genre_values == 0 for genre_values in zero_list):
            print(f"{movie_input} cannot be saved as no genre was associated with it!")
            continue

        data["movie_vectors"][movie_input] = zero_list
        save_json_data(data)


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

def cosine_similarity(movie_name: str) -> list[tuple[str, float]] | None:
    cos_values_list = []

    validated_movie = movie_lookup(movie_name, data["movie_vectors"])

    if validated_movie is None:
        return None

    input_movie_magnitude = magnitude(data["movie_vectors"][validated_movie])
    for other_movie_name in data["movie_vectors"]:
        if other_movie_name == validated_movie:
            continue

        dot_product = dot(data["movie_vectors"][validated_movie], data["movie_vectors"][other_movie_name])
        other_movie_magnitude = magnitude(data["movie_vectors"][other_movie_name])
        cos_theta = (dot_product / (input_movie_magnitude * other_movie_magnitude))
        cos_values_list.append((other_movie_name, cos_theta))

    cos_values_list.sort(key=lambda movie_tuple: movie_tuple[1], reverse=True)

    return cos_values_list
