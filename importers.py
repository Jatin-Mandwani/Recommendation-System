# Dataset Import Functions

from data_manager import save_json_data, load_json_data, rebuild_genre_dict
from genre_operations import verify_genres, create_binary_vector
from lookup import movie_lookup
import csv

def import_imdb_dataset(filename: str):

    data = load_json_data()
    genre_dict = rebuild_genre_dict(data["genre_list"])

    with open(filename, "r", newline="", encoding="utf-8") as importfile:
        movies_and_genres = csv.DictReader(importfile, delimiter="\t")
        total_entries = 0
        movies_shows_added = 0
        duplicates_skipped = 0
        no_genre_items = 0
        invalid_genre = 0

        for entry in movies_and_genres:
            total_entries += 1
            title = entry["primaryTitle"]

            validated_title = movie_lookup(title, data["movie_vectors"])
            if validated_title is not None:
                print(f"Movie '{validated_title}' already exists!")
                duplicates_skipped += 1
                continue

            if entry["genres"] == "\\N":
                no_genre_items += 1
                continue

            dataset_genre = entry["genres"].split(",")
            if not verify_genres(dataset_genre, data["genre_list"]):
                invalid_genre += 1
                continue

            binary_movie_vector = create_binary_vector(dataset_genre, genre_dict, data)

            data["movie_vectors"][title] = binary_movie_vector
            movies_shows_added += 1

            print(f"{title}: {binary_movie_vector}")

        save_json_data(data)

        print("==========IMPORT SUMMARY==========")

        print(f"Entries Processed: {total_entries}\n"
              f"Total Movies/Shows Added: {movies_shows_added}\n"
              f"Duplicates Skipped: {duplicates_skipped}\n"
              f"No Genres: {no_genre_items}\n"
              f"Invalid Genres: {invalid_genre}\n")