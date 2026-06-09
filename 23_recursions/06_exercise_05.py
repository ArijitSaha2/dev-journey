# Recursion Exercise 5
# Write a recursive function that calculates the sum of numbers from n down to 1
# Example: sum_down(5) → 15 (5+4+3+2+1)

def sum_reverse(x):
    if x == 0:
        return 0
    else:
        return x + sum_reverse(x - 1)
    
print(sum_reverse(5))