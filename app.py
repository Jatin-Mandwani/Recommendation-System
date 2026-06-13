from utils import genre_updation, input_movies_and_genres, cosine_similarity
import json

with open("movies.json", "r") as mfile:
    data = json.load(mfile)


def main_menu():
    print("\n<-------------------- WELCOME TO THE RECOMMENDATION SYSTEM -------------------->\n")

    while True:
        print("\nWhat would you like to do?\n")
        print("1) Recommend Movies (Press 1) \n"
              "2) Search Movie (Press 2) \n"
              "3) Browse by Genre (Press 3) \n"
              "4) Exit (Press 4)")

        option = int(input("\nEnter here: "))

        match option:
            case 1:
                movie_name = input("Enter the movie name to get similar recommendations: ")
                recommended_movies = cosine_similarity(movie_name)
                if recommended_movies is None:
                    continue

                print("")
                print("-" * 45)
                print(f"{'Movie Name':^25}|{'Score':^20}")
                print("-" * 45)
                for name, score in list(recommended_movies.items())[0:5]:
                    print(f"{name:^25}|{score:^20.4f}")
                print("-" * 45)
                print("")
                continue

            case 2:
                searched_movie = input("Enter movie name: ")

                if searched_movie.lower() not in (keys.lower() for keys in data["movie_vectors"].keys()):
                    print(f"Movie '{searched_movie}' not found!")

                elif not searched_movie:
                    print("Input movie cannot be empty!")

                else:
                    temp_dict = {}
                    for i, genre_item in enumerate(data["genre_list"]):
                        temp_dict.update({i: genre_item})

                    temp_genre_list = [
                        temp_dict[i]
                        for i, item in enumerate(data["movie_vectors"][searched_movie])
                        if item == 1
                    ]

                    print("\nName: {}\n"
                          "Genres:- \n{}".format(searched_movie,
                                                 "\n".join("{}. {}".format(i + 1, temp_genre_list[i])
                                                           for i, item in enumerate(temp_genre_list))))

                continue

            case 3:
                filtered_genre_list = []
                filtered_genre_index = []

                temp_dict = {
                    genre.lower(): i
                    for i, genre in enumerate(data["genre_list"])
                }

                while True:
                    filter_genre = input("Enter the genre to get filtered suggestions {or type 'exit' to quit): ")

                    if not filter_genre:
                        print("Genre cannot be empty!")
                        continue

                    elif filter_genre.lower() == 'exit':
                        break

                    elif filter_genre.lower() in (items.lower() for items in filtered_genre_list):
                        print(f"Genre '{filter_genre}' already entered!")
                        continue

                    elif filter_genre.lower() not in temp_dict:
                        print(f"Genre '{filter_genre}' not found!")
                        continue

                    else:
                        filtered_genre_list.append(filter_genre)

                if not filtered_genre_list:
                    print("No genres entered!")
                    continue

                filtered_genre_index = [
                    temp_dict[genre_item.lower()]
                    for genre_item in filtered_genre_list
                ]

                matching_movies = [
                    movie
                    for movie, vectors in data["movie_vectors"].items()
                    if all(vectors[index] == 1 for index in filtered_genre_index)
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

            case default:
                print("Enter valid input!")
                continue


if __name__ == "__main__":
    main_menu()
