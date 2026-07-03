# python file detection = Checking if a file or folder exists at a specified location.
#                         The os module can also check whether the location is a file or a folder.

# Relative file path = Location of a file/folder relative to the current working directory.
# Example: "stuff/test.txt"

# Absolute file path = Complete location of a file/folder starting from the drive/root directory.
# Example: "C:\\Users\\ariji\\OneDrive\\Desktop\\test" or "C:/Users/ariji/OneDrive/Desktop/test"

import os

file_path = "stuff/test.txt" # Relative Path

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")

else:
    print("That location doesn't exist")