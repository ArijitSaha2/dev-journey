# Exercise 5
# Ask the user to enter their name, favorite programming language, and experience level.
# Store the answers in a dictionary.
# Create a file called developer.json using write mode.
# Write the dictionary into the JSON file using json.dump() with indent=4.
# Print "developer.json was created" after writing is complete.

import json

name = input("Enter your name: ")
fav = input("Enter your favourite programming language: ")
exp = input("Enter your experience level: ")

dictionary = {
    "Name": name, 
    "Fav_Programming_language": fav, 
    "Experience": exp}

file_path = "developer.json"

with open(file_path, "w") as file:
    json.dump(dictionary, file, indent=4)
    print(f"{file_path} was created")