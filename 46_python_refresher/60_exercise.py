# Exercise 60 — Mixed Revision (Revised)
# Write a program that:
# 1. Accepts five numbers from the user and stores them in a list.
# 2. Uses a regular function to find the largest number.
# 3. Uses a lambda function with filter() to extract even numbers.
# 4. Uses a recursive function to count up from 1 to 5.
# 5. Displays the results.
# Requirements:
# - Use def for both regular functions.
# - Use lambda with filter().
# - Include a recursion base case.
# - No loops inside the recursive function.

def rev(numbers):
    print(f"Largest: {max(numbers)}")
    print(list(filter(lambda n: n % 2 == 0, numbers)))

x = []

for num in range(5):
    y = int(input("Enter num: "))
    x.append(y)

rev(x)

print("Recursive Function Starts here")
def recursive(num):
    
    if num > 1:
        recursive(num - 1)
        print(num)
    else:
        print(1)

recursive(5)