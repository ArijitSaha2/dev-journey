# Exercise 30 — Comparison Operators
# Given two numbers, write a program that compares them using all six comparison operators.

# Your program should check:
# 1. Whether the numbers are equal (==).
# 2. Whether they are different (!=).
# 3. Whether the first is greater (>).
# 4. Whether the first is smaller (<).
# 5. Whether the first is greater than or equal to the second (>=).
# 6. Whether the first is less than or equal to the second (<=).
# Rules:
# - Use two variables.
# - Print the result of each comparison.
# - You may use a function if useful.
# - No loops required.

# Topic focus: Comparison operators.

def compare(x, y):
    print(f"x == y - {x == y}")
    print(f"x != y - {x != y}")
    print(f"x > y - {x > y}")
    print(f"x < y - {x < y}")
    print(f"x >= y - {x >= y}")
    print(f"x <= y - {x <= y}")

compare(2, 3)