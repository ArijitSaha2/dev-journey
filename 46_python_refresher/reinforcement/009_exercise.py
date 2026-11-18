# Exercise 009 — Convert Strings to Integers Using map()
# Given:
# numbers = ["10", "20", "30", "40", "50"]

# Your task:
# - Use map() to convert every string into an integer.
# - Convert the result into a list.
# - Print the result.
# Expected output:
# [10, 20, 30, 40, 50]

numbers = ["10", "20", "30", "40", "50"]

def make_int(n):
    return int(n)

result = map(make_int, numbers)

print(list(result))