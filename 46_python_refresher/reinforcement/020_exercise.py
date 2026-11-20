# Exercise 020 — File Handling (Writing to a File)
# Your task:
# - Create a file called notes.txt.
# - Open it using open() in write mode ("w").
# - Write "Learning Python file handling!" into it.
# - Close the file.
# - Reopen the file in read mode ("r").
# - Read and print its contents.
# - Close the file.
# Expected output:
# Learning Python file handling!

file_path = "notes.txt"

with open(file_path, "w") as file:
    file.write("Learning Python file handling!\nRemember to Delete the file that was created when you executed this!!!")

with open(file_path, "r") as file:
    red = file.read()
    print(red)