# Exercise 027 — os.path.exists()

# Your task:
#     Check whether a file named config.txt currently exists using os.path.exists().
#     Print a clear message telling whether config.txt exists or does not exist.

# Expected output (when config.txt does not exist):
# config.txt does not exist.


import os

file_path = "config.txt"

if os.path.exists(file_path):
    print(f"{file_path} exists")
else:
    print(f"{file_path} does not exist")