# Lookup Functions

def genre_lookup(genre: str, genre_list: list) -> str | None:
    for item in genre_list:
        if genre.lower() == item.lower():
            return item

    return None



def movie_lookup(movie_name: str, movie_dict: dict) -> str | None:
    for item in movie_dict:
        if movie_name.lower() == item.lower():
            return item

    return None



def find_matching_movies(movie_name: str, json_movie_data: dict) -> str | None:
    movie_dict = json_movie_data.keys()
    normalized_movie = movie_name.lower()

    matched_movies = [
        movie_item
        for movie_item in movie_dict
        if normalized_movie in (movie_item.split("(", 1)[0].strip().lower())
    ]

    if len(matched_movies) == 0:
        print(f"Movie '{movie_name}' not found")
        return None

    elif len(matched_movies) == 1:
        return matched_movies[0]

    print("These are the following results:-\n")
    for i, movie in enumerate(matched_movies):
        print(f"{i + 1}. {movie}")

    while True:
        try:
            choice = int(input("\nEnter the number corresponding to the movie of your choice: "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        if 1 <= choice <= len(matched_movies):
            return matched_movies[choice - 1]

        print(f"Please enter a number between 1 and {len(matched_movies)}.")