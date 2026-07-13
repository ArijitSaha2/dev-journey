# Exercise 2
# Ask the user to enter a word.
# Create a function that accepts the word.
# Return the word in uppercase if its length is even.
# Otherwise, return the word in lowercase.
# Print the returned value.

word = input("Enter a word: ")

def func(w = word):
    if len(word) % 2 == 0:
        return f"Capital: {w.capitalize()}"
    else:
        return f"Lowercase: {w.lower()}"
    
print(func())