# Exercise 008 — Using map()
# Given this list:
# numbers = [2, 4, 6, 8, 10]

# Your task:
# - Use map() to multiply every number by 3.
# - Convert the result into a list.
# - Print the result.
# Expected output:
# [6, 12, 18, 24, 30]

numbers = [2, 4, 6, 8, 10]

def triple(n):
    return n * 3

task = map(triple, numbers)
print(list(task))