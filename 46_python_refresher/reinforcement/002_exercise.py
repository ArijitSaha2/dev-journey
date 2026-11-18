# Exercise 002 — Sum of Natural Numbers
# Write a recursive function that:
# - Accepts an integer n.
# - Calculates the sum of all numbers from 1 to n.
# - Returns the result.
# - Uses a base case to stop recursion.
# Example:
# Enter number: 5
# Sum: 15

# Because (5 + 4 + 3 + 2 + 1 = 15).

def sum_of_all(num):
    result = 0
    if num > 0:
        result =  num + sum_of_all(num - 1)
        return result
    else: 
        return(0)

n = int(input("Enter num: "))
print(sum_of_all(n))