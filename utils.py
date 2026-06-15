import json

with open("movies.json", "r") as mfile:
    data = json.load(mfile)

# Genre to Index Mapping in Dict

def rebuild_genre_dict(genre_list: list[str]) -> dict[str, int]:

    return {
        genre: i
        for i, genre in enumerate(genre_list)
    }

genre_dict = rebuild_genre_dict(data["genre_list"])

# Genre List and Dict Updation

def genre_updation():
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

                elif new_genre.lower() in [genre.lower() for genre in data["genre_list"]]:
                    print(f"The genre '{new_genre}' already exists")
                    continue

                else:
                    data["genre_list"].append(new_genre)
                    print(f"You entered '{new_genre}' as a new genre")
                    continue

            case 2:
                remove_genre = input("\nEnter the genre to be removed: ").strip()

                if not remove_genre:
                    print("Genre cannot be empty")
                    continue


                elif remove_genre.lower() not in [genre.lower() for genre in data["genre_list"]]:
                    print(f"'{remove_genre}' already does not exist")
                    continue

                elif remove_genre.lower() in [genre.lower() for genre in data["genre_list"]]:
                    data["genre_list"].remove(remove_genre)
                    print(f"You removed '{remove_genre}' from the list")
                    continue

            case 3:
                with open("movies.json", "w") as file:
                    json.dump(data, file, indent=4)
                break

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
            print(f"You entered '{movie_input}' movie")

        while True:
            genre_input = (input(f"Enter the genre of the movie '{movie_input}' (or type 'exit' to quit): ")
                           .strip())

            if genre_input.lower() == "exit":
                print("Exiting Genre Input...")
                break

            if not genre_input:
                print("Genre cannot be empty!")
                continue

            elif (genre_input.lower() != "exit") and genre_input.lower() not in [genre.lower() for genre in
                                                                                 data["genre_list"]]:
                print("Genre not available! Kindly recheck")
                continue

            elif genre_input.lower() in [genre.lower() for genre in data["genre_list"]]:
                data["movie_vectors"][movie_input][genre_dict[genre_input]] = 1
                print(f"You entered '{genre_input}' genre to the movie '{movie_input}'")

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

def cosine_similarity(movie_name: str) -> dict | None:
    cos_values_list = []
    ref_movie_dict = data["movie_vectors"]

    if movie_name not in ref_movie_dict:

        print("Movie not found.")

        choice = input("Would you like to add it? (y/n): ").lower()

        if choice == "y":
            input_movies_and_genres()

        return None

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
