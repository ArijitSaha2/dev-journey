# Exercise 1
# Read and print the contents of story.txt using file.read().
# Read and print the contents of player.json using json.load().
# Read scores.csv using csv.reader() and print each row using a loop.
# Handle FileNotFoundError for each file.

# for .txt
file_path = "story.txt"
print("For Txt file")
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not Found!")

# for .json
import json 

file_path = "player.json"
print("For Json file")
try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("File not Found!!")

# for .csv
import csv

file_path = "scores.csv"
print("For Csv file")
try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("File not Found!!!")