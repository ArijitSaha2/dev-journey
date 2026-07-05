# Exercise 8
# Create a nested list containing a header row: City, Country, Population.
# Add three cities as data rows.
# Create a file called city_data.csv using write mode.
# Create a CSV writer object.
# Use a loop and writerow() to write each row into the file.
# Print "city_data.csv was created" after writing is complete.

import csv

geography = [
    ["City", "Country", "Population"],
    ["New York", "America", 100],
    ["Sydney", "Australia", 55],
    ["Shanghai", "China", 1000],
]

file_path = "city_data.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for cities in geography:
        writer.writerow(cities)
    print(f"{file_path} was created")