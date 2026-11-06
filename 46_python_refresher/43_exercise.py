# Exercise 43 — String Slicing
# Write a program that:
# 1. Takes a string as input.
# 2. Displays the first 3 characters.
# 3. Displays the last 3 characters.
# 4. Displays the string in reverse.
# Requirements:
# - Use a function.
# - Use string slicing.
# - No hardcoded input.

def slice_ing(word_):
    print(word_[0:3])
    print(word_[-3:])
    print(word_[::-1])

word = input("Enter word: ")
slice_ing(word)