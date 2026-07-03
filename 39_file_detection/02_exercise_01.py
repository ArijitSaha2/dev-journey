# Exercise 1
# Use the relative path "stuff/test.txt".
# Check if the path exists.
# If it exists, print whether it is a file or a directory.
# If it does not exist, print "Path not found".

import os

file_path = "stuff/test.txt"

if os.path.exists(file_path):
    print("It exists")
    if os.path.isfile(file_path):
        print("Its a file")
    elif os.path.isdir(file_path):
        print("Its a directory")
else:
    print("Path not found")