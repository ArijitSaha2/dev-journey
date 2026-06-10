# Recursion Exercise 6
# Write a recursive function that calculates the factorial of a number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))