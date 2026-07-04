# Python Writing Files = Saving data from a Python program into a file.
# Common file types: .txt, .json, .csv

# File modes:
# "w" = Write mode. Creates a new file or overwrites an existing file.
# "a" = Append mode. Adds new content to the end of an existing file.
# "x" = Create mode. Creates a new file but raises FileExistsError if it already exists.


# -------------------- TXT FILE --------------------

# .txt = A plain text file used to store simple readable text.

employees = ["Eugene", "Squidwart", "Spongbob", "Patrick"]


file_path = "output.txt"

try:
    with  open(file_path, "w") as file:
        for employee in employees:
            file.write(employee + " ")
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")


# -------------------- JSON FILE --------------------

# JSON = A file format used to store structured data using key-value pairs.
# Python's json module is used to work with JSON files.

import json

employee = {
    "name": "Spongbob",
    "age": 30,
    "job": "cook"
}

file_path = "output.json"

try:
    with  open(file_path, "w") as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")


# -------------------- CSV FILE --------------------

# CSV = Comma-Separated Values.
# Used to store table-like data in rows and columns.
import csv

employees = [["Name", "Age", "Job"],
            ["Sponebob", 30, "Cook"],
            ["Patrick", 37, "Umemployed"],
            ["Sandy", 27, "Scientist"]]

file_path = "output.csv"

try:
    with  open(file_path, "w", newline='') as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")