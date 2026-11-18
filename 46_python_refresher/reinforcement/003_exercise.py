# Exercise 003 — Factorial (Recursion)
# Write a recursive function that:
# - Accepts an integer n.
# - Calculates its factorial.
# - Returns the result.
# - Uses a base case to stop recursion.
# Example:
# Enter number: 5
# Factorial: 120

def factorial(num):
    result = 0
    if num > 0:
        result = num * factorial(num - 1)
        return result
    else:
        return 1

n = int(input("Enter num: "))
print(factorial(n))