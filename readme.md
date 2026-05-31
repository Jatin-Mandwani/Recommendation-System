# Movie Recommendation System 🎬

A Python-based Movie/TV Show Recommendation System that recommends similar content based on genre similarity. The system also allows users to expand and maintain the movie database by adding new titles and updating their genres.

## Features

* Get recommendations for movies and TV shows
* Add new movies and their genres to the database
* Update genre lists by adding or removing genres
* Store movie information using JSON
* Handle movies that are not yet present in the database

## Technologies Used

* Python
* JSON
* File Handling
* Vector Similarity (Cosine Similarity)

## How It Works

Each movie is represented as a genre vector. When a user requests recommendations, the system calculates the cosine similarity between the selected movie and all other movies in the database. Movies with the highest similarity scores are returned as recommendations.

If a movie is not found in the database, the user can:

* Add the movie along with its genres
* Return to the main menu

## Project Structure

```text
Recommendation-System/
│
├── app.py          # Main application and menu
├── utils.py        # Helper functions and recommendation logic
├── movies.json     # Movie database
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/Jatin-Mandwani/Recommendation-System.git
```

2. Navigate to the project directory

```bash
cd Recommendation-System
```

3. Run the application

```bash
python app.py
```

## Example Usage

### Get Recommendations

```text
Enter the movie name to get similar recommendations:
Breaking Bad
```

Output:

```text
---------------------------------------------
       Movie Name       |       Score
---------------------------------------------
Better Call Saul        |      0.9432
Ozark                   |      0.9124
Narcos                  |      0.8871
---------------------------------------------
```

### Update Genres

```text
1. Add Genre
2. Remove Genre
```

Modify a movie's genre list without manually editing the JSON database.

## Motivation

I built this project to explore recommendation system fundamentals, cosine similarity, JSON-based data storage, and modular Python application design.

## Learning Outcomes

This project helped me strengthen my understanding of:

* Python programming
* Functions and modular code design
* File handling
* JSON data storage
* Similarity algorithms
* Recommendation system fundamentals

## Future Improvements

* FastAPI integration
* User accounts and watch history
* Web interface
* Content-based recommendation enhancements

## Author

**Jatin Mandwani**