# Recursion Exercise 4
# Write a recursive function that prints a string n times
# Example: repeat("hello", 3) → hello, hello, hello

def repeat(x, y = 3):
    if y == 0:
        return 
    else:
        print(x)
        return repeat(x, y - 1)
    
repeat("hello", 3)