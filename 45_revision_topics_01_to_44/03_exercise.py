# Exercise 3
# Create a dictionary containing five words and their meanings.
# Ask the user to enter a word.
# Create a function that accepts the dictionary and the entered word.
# If the word exists, return:
# - The word in uppercase.
# - Its meaning.
# Otherwise, return "Word not found".
# Print the returned value using an f-string.

words = {"apple": "Fruit", 
         "toy-plane": "Toy", 
         "sunday": "Weekend", 
         "cat": "Animal", 
         "sun": "Star"}

user = input("Enter your word: ").lower()

def func(dictionary, entered_word):
    if entered_word in dictionary:
        return f"{entered_word.upper()}: {dictionary[entered_word]}"
    else:
        return f"{entered_word} not found"
    
print(func(words, user))