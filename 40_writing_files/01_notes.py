# Python Writing Files = Saving data from a Python program into a file.
# Common file types: .txt, .json, .csv

# File modes:
# "w" = Write mode. Creates a new file or overwrites an existing file.
# "a" = Append mode. Adds new content to the end of an existing file.
# "x" = Create mode. Creates a new file but raises FileExistsError if it already exists.


# -------------------- TXT FILE --------------------

employees = ["Eugene", "Squidwart", "Spongbob", "Patrick"]
# List containing the text we want to write.

file_path = "output.txt"
# Name/path of the file to create.

try:
    # Opens output.txt in write mode and closes it automatically when finished.
    with open(file_path, "w") as file:

        # Goes through each employee in the list.
        for employee in employees:

            # Writes each employee name followed by a space.
            file.write(employee + " ")

        print(f"txt file '{file_path}' was created")

except FileExistsError:
    print("That file already exists!")


# -------------------- JSON FILE --------------------

import json
# Imports the module needed to work with JSON.

employee = {
    "name": "Spongbob",
    "age": 30,
    "job": "cook"
}
# Python dictionary containing structured employee data.

file_path = "output.json"

try:
    with open(file_path, "w") as file:

        # Converts the Python dictionary into JSON and writes it to the file.
        # indent=4 formats the JSON neatly instead of writing everything on one line.
        json.dump(employee, file, indent=4)

        print(f"json file '{file_path}' was created")

except FileExistsError:
    print("That file already exists!")


# -------------------- CSV FILE --------------------

import csv
# Imports the module needed to work with CSV files.

employees = [
    ["Name", "Age", "Job"],       # Header row
    ["Sponebob", 30, "Cook"],     # Data row
    ["Patrick", 37, "Unemployed"],
    ["Sandy", 27, "Scientist"]
]
# Nested list: every inner list represents one row.

file_path = "output.csv"

try:
    # newline='' prevents unwanted blank lines between CSV rows.
    with open(file_path, "w", newline='') as file:

        # Creates a CSV writer connected to the opened file.
        writer = csv.writer(file)

        # Goes through each inner list (row).
        for row in employees:

            # Writes one inner list as one CSV row.
            writer.writerow(row)

        print(f"csv file '{file_path}' was created")

except FileExistsError:
    print("That file already exists!")