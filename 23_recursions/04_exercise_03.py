# Recursion Exercise 3
# Write a recursive function that prints numbers from 1 to n
# Example: count_up(5) → 1, 2, 3, 4, 5

def count_up(n):
    if n == 0:
        return
    else:
        count_up(n - 1)
    print(n)
    
    
count_up(5)