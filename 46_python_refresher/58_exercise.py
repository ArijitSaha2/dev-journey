# Write a recursive function that:
# 1. Accepts a positive integer.
# 2. Counts down to 1.
# 3. Prints each number.
# 4. Stops when it reaches 1.
# Requirements:
# - Use recursion.
# - Include a base case.
# - Do not use loops.

def recursive(num):
    if num > 1:
        print(num)
        recursive(num - 1)
    else:
        print(1)


user_input = int(input("Enter a positive number: "))
recursive(user_input)