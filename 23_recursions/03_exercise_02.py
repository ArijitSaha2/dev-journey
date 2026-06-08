# Recursion Exercise 2
# Write a recursive function that calculates the sum of all numbers from 1 to n
# Example: rec_sum(5) → 15 (1+2+3+4+5)

def sum(n):
    if n == 0:
        return 0
    else:
        return sum(n - 1) + n
        

print(sum(5))