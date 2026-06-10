# Recursion Exercise 7
# Write a recursive function that reverses a string
# Example input: "hello"

def reverse_string(word):
    if len(word) == 0:
        return ""
    else:
        return word[-1] + reverse_string(word[:-1])
print(reverse_string("Hello"))