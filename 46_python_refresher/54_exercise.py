# Exercise 54 — Comprehensions
# Quick refresher first:
# A comprehension lets you create a collection in a compact way using an expression and a loop.

# General syntax:
# [expression for item in iterable]

# For example, converting numbers into their squares:
# squares = [x ** 2 for x in range(1, 6)]

# Create a function that accepts a list of numbers and:
# 1. Creates a new list containing only even numbers using list comprehension.
# 2. Creates a dictionary containing each number and its square using dictionary comprehension.
# 3. Creates a set containing the unique numbers using set comprehension.
# 4. Displays all three collections.

# Requirements:
# - Take 8 numbers through user input.
# - Use a function.
# - Use comprehensions for all three conversions.

def func(numbers):

    even = [even for even in numbers if even % 2 == 0 ]
    print(f"Even: {even}")

    dictionary = {num: num ** 2 for num in numbers}
    print("Number and its squares: ",dictionary) 

    s = {num for num in numbers}
    print(f"Set: {s}")
    print()

l = []

for y in range(8):
    number = int(input("Enter number: "))
    l.append(number)

func(l)