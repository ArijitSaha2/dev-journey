# Exercise 6
# Create a nested list containing a header row: Name, Genre, Year.
# Add three games as data rows.
# Create a file called games.csv using write mode.
# Create a CSV writer object.
# Use a loop and writerow() to write each row into the file.
# Print "games.csv was created" after writing is complete.

import csv 

games = [
    ["Name", "Genre", "Year"],
    ["Grand Theft Auto V", "Open World", 2013],
    ["Cyberpunk 2077", "Open World", 2021],
    ["Forza Horizon 6", "Racing", 2026],
]

file_path = "games.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for row in games:
        writer.writerow(row)
    print(f"{file_path} was created")