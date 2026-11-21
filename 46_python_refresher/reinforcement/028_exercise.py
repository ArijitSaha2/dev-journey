# Exercise 028 — os.remove()

# os.remove() deletes a file—and raises FileNotFoundError if it doesn't exist, or PermissionError / IsADirectoryError if it isn't a removable file.

# Your task:
# Write a small helper function remove_temp_file(file_path) that attempts to delete the target file using os.remove().
# Make it handle a missing file cleanly without crashing, and return a clear status message (e.g., deleted, or not found).
# Test it on "temp_notes.txt" (covering both when the file is missing and when it exists).

# Expected behavior:
# temp_notes.txt not found.

import os

file_path = "temp_notes.txt"

def remove_temp_file(file):
    try: 
        os.remove(file)
        return (f"{file} is deleted!")

    except FileNotFoundError:
        return (f"{file} not found.\nFile is either deleted or doesn't exist")

print(remove_temp_file(file_path))