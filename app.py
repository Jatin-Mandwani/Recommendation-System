from utils import genre_updation, input_movies_and_genres, cosine_similarity

def main_menu():
    print("\n<-------------------- WELCOME TO THE RECOMMENDATION SYSTEM -------------------->\n")

    print("\nWhat would you like to do?\n")
    while True:
        print("1) Recommend movies (Press 1) \n"
              "2) Feed new movies and its genres to the database (Press 2) \n"
              "3) Update genre list (Press 3) \n"
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
                input_movies_and_genres()
                continue

            case 3:
                genre_updation()
                continue

            case 4:
                print("\nThank you for using me!\n")
                break

            case default:
                print("Enter valid input!")
                continue


if __name__ == "__main__":
    main_menu()