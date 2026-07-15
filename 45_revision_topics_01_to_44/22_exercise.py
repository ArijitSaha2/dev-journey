# Ask the user for a file name.
# Check whether the file exists.
# If it exists, print "File found".
# Otherwise, print "File not found".

import os

file_name = input("Enter file name: ")

file_path = f"{file_name}.txt"

if os.path.exists(file_path):
    print("File Found")
else:
    print("File not found")