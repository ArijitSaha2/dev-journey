# Exercise 46 — List Basics

# Write a program that:
# 1. Takes five numbers from the user and stores them in a list.
# 2. Displays the list.
# 3. Displays the first and last elements.
# 4. Displays the length of the list.
# 5. Calculates the sum of all elements.
# Requirements:
# - Use a function.
# - Use a loop to collect the numbers.
# - Use list indexing and built-in functions.

def list_basics(number):

    print(f"The list = {number}")
    print(f"The first element = {number[0]}\nThe last element = {number[-1]}\nThe length of list = {len(number)}")
    total = 0
    for x in number:
        total += x
    print(f"Sum of all elements = {total}")

print(f"You need to add Different numbers each time!")
lis = []
for num in range(1, 6):
    num = int(input("Enter number: "))
    lis.append(num)

list_basics(lis)