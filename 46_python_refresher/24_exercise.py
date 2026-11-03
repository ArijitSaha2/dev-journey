# Exercise 24 — Count Even Numbers
# Given a list of numbers, write a function that counts how many even numbers are present.

# Rules:
# - Use a function.
# - Use a for loop.
# - Use a counter variable.
# - Do not use count().
# numbers = [2, 5, 8, 11, 14, 17, 20]

# Topic focus: Lists, loops and conditionals.

def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1

    return f"Total even numbers: {count}"
print(count_even(numbers = [2, 5, 8, 11, 14, 17, 20]))