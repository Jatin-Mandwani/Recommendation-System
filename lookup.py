# Lookup Functions

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
