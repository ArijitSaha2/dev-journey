# Exercise 72 — File Handling
# What this tests: Opening, writing, reading and closing files using Python.

# Task: Create a simple notes file manager.

# Requirements:
# 1. Open a file called notes.txt in write mode ("w").
# 2. Write three lines of text into it.
# 3. Use with open() to manage the file.
# 4. Open the same file in read mode ("r").
# 5. Read and display its contents.
# 6. Handle FileNotFoundError.
# Rules:
# - Use with open() for both operations.
# - No functions or classes.
# - Don't use os or pathlib.

try: 
    file_path = "notes.txt"

    with open(file_path, "w") as file:
        file.write("This is notes.txt\nCreated to test.\nAnd it should work?")
        print(f"{file_path} file was created")

    with open(file_path, "r") as file:
        f = file.read()
        print(f)

except FileNotFoundError:
    print("File not Found. Enter Directory or file location properly!")