# Python Reading Files = Opening existing files and getting their stored data.
# Common file types: .txt, .json, .csv

# "r" = Read mode. Opens an existing file for reading.
# Raises FileNotFoundError if the file does not exist.

# TXT  → file.read()
# JSON → json.load(file)
# CSV  → csv.reader(file)
#        loop through rows

file_path = "input.txt"

try:
    # Opens the file in read mode and closes it automatically afterward.
    with open(file_path, "r") as file:

        # file.read() reads the entire file and returns its content as a string.
        content = file.read()

        print(".txt file")
        print(content)

except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have Permission to read that file")

print()


# -------------------- JSON FILE --------------------

import json

file_path = "input.json"

try:
    with open(file_path, "r") as file:

        # json.load() reads JSON data from the file
        # and converts it into a Python object, such as a dictionary.
        content = json.load(file)

        print(".json File")
        print(content)

except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have Permission to read that file")

print()


# -------------------- CSV FILE --------------------

import csv

file_path = "input.csv"

try:
    with open(file_path, "r") as file:

        # csv.reader() creates a CSV reader object connected to the file.
        content = csv.reader(file)

        print(".csv file")

        # Each loop gives one CSV row as a list.
        for line in content:
            print(line)

except FileNotFoundError:
    print("That file was not found")

except PermissionError:
    print("You do not have Permission to read that file")