# Admin Tasks

from movie_operations import add_movies
from genre_operations import genre_updation
from importers import import_imdb_dataset

def admin_menu():
    print("\n<-------------------- ADMIN MODE OF RECOMMENDATION SYSTEM -------------------->\n")

    while True:
        print("\nWhat would you like to do?\n")
        print("1) Import Dataset (Press 1) \n"
              "2) Feed new movies and its genres to the database (Press 2) \n"
              "3) Update genre list (Press 3) \n"
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
                import_imdb_dataset("title.basics.tsv")
                continue
            case 2:
                add_movies()
                continue

            case 3:
                genre_updation()
                continue

            case 4:
                print("\nThank you for using me!\n")
                break

            case _:
                print("Enter valid input!")
                continue


if __name__ == "__main__":
    admin_menu()