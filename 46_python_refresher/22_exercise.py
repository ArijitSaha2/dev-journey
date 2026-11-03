# Exercise 22 — Remove Duplicate Items

# Given a list of numbers, write a function that:

# 1. Removes duplicate values.
# 2. Preserves the original order of first occurrences.
# 3. Returns a new list without modifying the original.

# Rules:

# - Use a function and a loop.
# - Use a conditional.
# - Do not use `set()` to convert the entire list.
# - No list comprehension.

# Topic focus: Lists, sets, loops and conditionals.

# numbers = [4, 2, 4, 7, 2, 9, 7, 1]

def remove_doubles(numbers):
    stored_num = []
    for num in numbers:
        if num not in stored_num:
            stored_num.append(num)

    return stored_num

print(remove_doubles([4, 2, 4, 7, 2, 9, 7, 1]))