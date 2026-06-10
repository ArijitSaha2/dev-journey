# Recursion Exercise 8
# Write a recursive function that counts down from n and prints "Go!" at the end

def count_down(n):
    if n == 0:
        return "Go"
    else:
        print(n)
        return count_down(n-1)
    
print(count_down(5))