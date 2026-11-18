# Exercise 005 — Reverse a String (Recursion)
# Write a recursive function called reverse_string() that:
# - Accepts a string.
# - Returns the string in reverse order.
# - Uses recursion, not loops.
# Example:
# reverse_string("hello")
# "olleh"
# reverse_string("python")
# "nohtyp"

def reverse_string(word):

    if len(word) == 0:
        return ""
    else:
        result = word[-1] + reverse_string(word[:-1])
        return result

w = input("Enter a word: ")
print(reverse_string(w))