# Exercise 23 — Find the Largest Number

# Given a list of numbers, write a function that returns the largest number.

# Rules:
# - Use a function.
# - Use a for loop.
# - Do not use max().
# - Do not sort the list.
# numbers = [12, 45, 7, 89, 23]

# Topic focus: Lists and loops.

def largest(numbers):
    number = numbers[0]
    for num in numbers:
        if num > number:
            number = num

    return f"Maximum number using manual code: {number}"

print(largest(numbers = [12, 45, 7, 89, 23]))



def maxx(num):
    number = max(num)

    return f"Maximum number using Max() function: {number}"

print(maxx([12, 45, 7, 89, 23]))