# Main File

from recommendation import recommend_movies
from movie_operations import search_movie, filter_movies_by_genre

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
                recommend_movies()
                continue

            case 2:
                search_movie()
                continue

            case 3:
                filter_movies_by_genre()
                continue

            case 4:
                print("\nThank you for using me!\n")
                break

            case _:
                print("Enter valid input!")
                continue


if __name__ == "__main__":
    main_menu()
