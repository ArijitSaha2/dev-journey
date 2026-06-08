# Recursion Exercise 1
# Write a recursive function that counts down from n to 0
# Print each number during the countdown
# Example: countdown(5) → 5, 4, 3, 2, 1, 0

def count_down(n):
    print(n)
    if n == 0:
        return
    else:
        return count_down(n - 1)
    
    
count_down(5)