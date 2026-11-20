# Exercise 021 — File Handling (Appending to a File)
# Your task:
# - Create a file called journal.txt.
# - Write an initial message into it.
# - Reopen the file using append mode ("a").
# - Add a second message without overwriting the first.
# - Read the file and print its contents.
# Expected output:
# Today I learned Python.
# Tomorrow I will practise more.

file_path = "journal.txt"

with open(file_path, "w") as file:
    file.write("Today I learned Python.")

with open(file_path, "a") as file:
    file.write("\nTomorrow I will practise more.")

with open(file_path, "r") as file:
    red = file.read()
    print(red)