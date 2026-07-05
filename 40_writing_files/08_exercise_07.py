# Exercise 7
# Create a nested list containing a header row: Language, Creator, Year.
# Add three programming languages as data rows.
# Create a file called programming_history.csv using write mode.
# Create a CSV writer object.
# Use a loop and writerow() to write each row into the file.
# Print "programming_history.csv was created" after writing is complete.

import csv 

languages = [
    ["Language", "Creator", "Year"],
    ["Python", "XYZ", 2000],
    ["Typescript", "Microsoft", 2010],
    ["C++", "ABC", 1999]
]

file_path = "programming_history.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for language in languages:
        writer.writerow(language)
    print(f"{file_path} was created")