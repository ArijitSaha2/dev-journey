# Exercise 004 — Fibonacci Sequence (Recursion)
# Write a recursive function that:
# - Accepts an integer n.
# - Returns the Fibonacci number at position n.
# - Uses recursion and a base case.
# The sequence starts:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def fib(num):
    result = 0
    if num == 0:
        return 0
    
    elif num == 1:
        return 1
    
    else:
        result = fib(num - 1) + fib(num - 2)
        return result
    
n = int(input("Enter num: "))
print(fib(n))