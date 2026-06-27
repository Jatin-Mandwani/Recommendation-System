# Data Persistence and Derived Data

import json

def save_json_data(json_data: dict):
    with open("movies.json", "w") as json_file:
        json.dump(json_data, json_file, indent=4)

# Loading content from JSON file

def load_json_data() -> dict:
    with open("movies.json", "r") as json_file:
        return json.load(json_file)


def rebuild_genre_dict(genre_list: list[str]) -> dict[str, int]:

    return {
        genre: i
        for i, genre in enumerate(genre_list)
    }
