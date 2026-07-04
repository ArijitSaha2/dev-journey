# Exercise 4
# Create a dictionary containing a game's title, genre, and release year.
# Create a file called game.json using write mode.
# Write the dictionary into the JSON file using json.dump() with indent=4.
# Print "game.json was created" after writing is complete.

import json

game_info = {
    "title": "Cyberpunk 2077",
    "genre": "Sci-fi",
    "year": 2021
}

file_path = "game.json"

with open(file_path, "w") as file:
    json.dump(game_info, file, indent=4)
    print(f"{file_path} was created")