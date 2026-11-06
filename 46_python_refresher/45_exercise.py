# Exercise 45 — String Operations

# Write a program that:
# 1. Takes a sentence as input.
# 2. Takes a word to search for.
# 3. Displays the sentence in uppercase.
# 4. Displays the number of occurrences of the word.
# 5. Displays the index of its first occurrence.
# 6. Displays the sentence in reverse.
# Requirements:
# - Use a function.
# - Use string methods and slicing.
# - Handle the case where the word isn't found.

def string_operation(sentence, word):

    print(f"Sentence in uppercase = {sentence.upper()}")
    print(f"number of occurrences of the word = {sentence.count(word)}")
    print(f"index of its first occerence(the word) = {sentence.find(word)}")
    print(f"Reverse: {sentence[::-1]}")


s1 = input("Enter sentence: ")
w1 = input("Enter word: ")
string_operation(s1, w1)