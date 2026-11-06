# Exercise 41 — String Basics
# Write a program that:
# 1. Takes a full name as input.
# 2. Displays the number of characters in the name.
# 3. Displays the first and last character.
# 4. Displays the name in uppercase and lowercase.
# Use len(), indexing and string methods.

def string_basics(full_name):
    if full_name:
        print(f"Number of characters in name: {len(full_name)}")
        print(f"Start alphabet:{full_name[0]}, End alphabet: {full_name[-1]}")
        print(f"Uppercase: {full_name.upper()}, Lowercase: {full_name.lower()}")

name = input("Enter name: ")
string_basics(name)