# Exercise 010 — Using filter()
# Given:
# numbers = [12, -5, 8, -2, 0, 15, -9, 20]

# Your task:
# - Use filter() to keep only positive numbers and keep numbers greater than 0.
# - Convert the result into a list.
# - Print the result.
# Expected output:
# [12, 8, 15, 20]

numbers = [12, -5, 8, -2, 0, 15, -9, 20]

def positive(n):
    return n > 0

result = filter(positive, numbers)

print(list(result))