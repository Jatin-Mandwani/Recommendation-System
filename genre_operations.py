# Genre Operations

from lookup import genre_lookup
from data_manager import data, save_json_data

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
