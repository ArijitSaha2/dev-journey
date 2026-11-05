# Exercise 39 — For Loops
# Write a program that:
# 1. Takes a number as input.
# 2. Uses a for loop to iterate from 1 up to that number.
# 3. Prints each number.
# 4. Calculates and displays the total sum of all numbers.
# Use a for loop and range().

def for_loop(number):
    total = 0
    for i in range (1, number + 1):
        print(i)
        total += i
    print(f"Sum of all Numbers = {total}")

num = int(input("Enter number: "))
for_loop(num)