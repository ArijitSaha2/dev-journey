# Exercise 42 — String Methods & Searching
# Write a program that:
# 1. Takes a sentence as input.
# 2. Takes a separate word to search for as input.
# 3. Displays how many times that word appears using .count().
# 4. Displays the index of its first occurrence using .find().
# 5. Takes a prefix and suffix as input, then checks whether the sentence starts and ends with them using .startswith() and .endswith().
# Requirements:
# - Use a function.
# - Don't hardcode the sentence, search word, prefix or suffix.
# - Handle cases where the search word isn't found.

def str_analysis(sentence, word, start, end):

    print(sentence.count(word))
    print(sentence.find(word))

    if sentence.lower().startswith(start.lower()):
        print(True)
    else:
        print(False)

    if sentence.lower().endswith(end.lower()):
        print(True)
    else:
        print(False)
    

sentence_ = input("Enter a sentence: ")
word_ = input("Enter a word to search: ")
starts_with = input("Enter starting word (will print true or false): ")
ends_with = input("Enter ending word (will print true or false): ")

str_analysis(sentence_ , word_, starts_with, ends_with)