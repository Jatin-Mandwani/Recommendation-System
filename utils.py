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

# Movie name input

def get_movie_name() -> str | None:
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

# Vector creation from Genres

def get_movie_vector(movie_name: str) -> list:
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


# Searching and Displaying Movie Details

def search_movie() -> None:
    searched_movie = input("Enter movie name: ")

    if not searched_movie:
        print("Input movie cannot be empty!")

    else:
        validated_movie = movie_lookup(searched_movie, data["movie_vectors"])
        if validated_movie is None:
            print(f"Movie '{searched_movie}' not found!")

        else:

            result_genre_list = [
                data["genre_list"][i]
                for i, item in enumerate(data["movie_vectors"][validated_movie])
                if item == 1
            ]

            print("\nName: {}\n"
                  "Genres:- \n{}".format(validated_movie,
                                         "\n".join("{}. {}".format(i + 1, genre)
                                                   for i, genre in enumerate(result_genre_list))))

# Filtering Movies by Genres and display the results

def filter_movies_by_genre() -> None:
    filtered_genre_list = []
    genre_dict = rebuild_genre_dict(data["genre_list"])

    while True:
        filter_genre = input("Enter the genre to get filtered suggestions {or type 'exit' to quit): ")

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

# Adding Genre to the list

def add_genre() -> None:
    new_genre = input("\nEnter a new genre (or type 'exit' to quit): ").strip()

    if not new_genre:
        print("Genre cannot be empty")
        return

    existing_genre = genre_lookup(new_genre, data["genre_list"])
    if existing_genre is not None:
        print(f"The genre '{existing_genre}' already exists")
        return

    data["genre_list"].append(new_genre)
    save_json_data(data)
    print(f"You entered '{new_genre}' as a new genre")

# Removing Genre from the list

def remove_genre() -> None:
    genre_input = input("\nEnter the genre to be removed: ").strip()

    if not genre_input:
        print("Genre cannot be empty")
        return

    genre_to_remove = genre_lookup(genre_input, data["genre_list"])
    if genre_to_remove is None:
        print(f"'{genre_input}' does not exist")
        return

    data["genre_list"].remove(genre_to_remove)
    save_json_data(data)
    print(f"You removed '{genre_to_remove}' from the list")

# Genre List and Dict Updation

def genre_updation() -> None:

    while True:

        print("\nHow would you like to update the genre list: \n"
              "1) Add genre to the genre list (Press 1)\n"
              "2) Remove genre from the genre list (Press 2)\n"
              "3) Exit (Press 3)")

        task_input = int(input("Enter here: "))

        match task_input:

            case 1:
                add_genre()

            case 2:
                remove_genre()

            case 3:
                save_json_data(data)
                break

# Input handling for Movies and Genres

def add_movies() -> None:
    while True:
        movie_name = get_movie_name()

        if movie_name is None:
            break

        binary_vector = get_movie_vector(movie_name)

        if all(genre_values == 0 for genre_values in binary_vector):
            print(f"{movie_name} cannot be saved as no genre was associated with it!")
            continue

        data["movie_vectors"][movie_name] = binary_vector
        save_json_data(data)
