# Exercise 025 — readline() and readlines()

# Your task:
# Assume a text file named notes.txt already exists with multiple lines of text.
# Open notes.txt using a context manager and read the first line using readline().
# Read all remaining lines into a list using readlines().
# Print the first line and the total count of remaining lines.

# Expected output:
# First line: Python refresher notes
# Remaining lines count: 3

file_path = "notes.text"

count = 0
try: 
    with open(file_path, "r") as file:
        fil = file.readline()
        print(f"First line: {fil.strip()}")

        for line in file.readlines():
            count += 1
        print(f"Remaining lines count: {count}")

except FileNotFoundError:
    print("File not found check if file_path is correct in code")