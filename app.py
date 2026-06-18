from utils import data, genre_dict, genre_lookup, save_json_data, load_json_data, movie_lookup, cosine_similarity

def main_menu():
    print("\n<-------------------- WELCOME TO THE RECOMMENDATION SYSTEM -------------------->\n")

    while True:
        print("\nWhat would you like to do?\n")
        print("1) Recommend Movies (Press 1) \n"
              "2) Search Movie (Press 2) \n"
              "3) Browse by Genre (Press 3) \n"
              "4) Exit (Press 4)")

        try:
            option = int(input("\nEnter here: "))

        except ValueError:
            print("Invalid Input! Please enter one of the given numbers")
            continue

        except KeyboardInterrupt:
            print("Operation Cancelled!")
            break

        match option:
            case 1:
                movie_name = input("Enter the movie name to get similar recommendations: ")
                recommended_movies = cosine_similarity(movie_name)
                if recommended_movies is None:
                    print("Movie not found.")
                    continue

                print("")
                print("-" * 60)
                print(f"{'Movie Name':^30}|{'Score':^30}")
                print("-" * 60)
                for name, score in recommended_movies[0:5]:
                    print(f"{name:^30}|{score:^30.4f}")
                print("-" * 60)
                print("")
                continue

            case 2:
                searched_movie = input("Enter movie name: ")
                validated_movie = movie_lookup(searched_movie, data["movie_vectors"])

                if not searched_movie:
                    print("Input movie cannot be empty!")

                elif validated_movie is None:
                    print(f"Movie '{searched_movie}' not found!")

                else:

                    result_genre_list = [
                        data["genre_list"][i]
                        for i, item in enumerate(data["movie_vectors"][validated_movie])
                        if item == 1
                    ]

                    print("\nName: {}\n"
                          "Genres:- \n{}".format(validated_movie,
                                                 "\n".join("{}. {}".format(i + 1, result_genre_list[i])
                                                           for i, item in enumerate(result_genre_list))))

                continue

            case 3:
                filtered_genre_list = []

                while True:
                    filter_genre = input("Enter the genre to get filtered suggestions {or type 'exit' to quit): ")
                    validated_genre = genre_lookup(filter_genre, data["genre_list"])

                    if not filter_genre:
                        print("Genre cannot be empty!")
                        continue

                    elif filter_genre.lower() == 'exit':
                        break

                    elif validated_genre is None:
                        print(f"Genre '{filter_genre}' not found!")
                        continue

                    elif validated_genre in filtered_genre_list:
                        print(f"Genre '{validated_genre}' already entered!")
                        continue

                    else:
                        filtered_genre_list.append(validated_genre)

                if not filtered_genre_list:
                    print("No genres entered!")
                    continue

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

                continue

            case 4:
                print("\nThank you for using me!\n")
                break

            case _:
                print("Enter valid input!")
                continue


if __name__ == "__main__":
    main_menu()
