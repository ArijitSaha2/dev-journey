# Exercise 25 — Sum of List Elements
# Write a function that calculates the total sum of all numbers in a list.

# Rules:
# - Use a function.
# - Use a for loop.
# - Use an accumulator variable.
# - Do not use sum().
# numbers = [10, 20, 5, 15, 30]

# Topic focus: Lists and loops.

def sum_of_elements(numbers):
    total = 0
    for num in numbers:
        total += num

    return total

print(sum_of_elements(numbers = [10, 20, 5, 15, 30]))


numbers = [10, 20, 5, 15, 30]
total = sum(numbers)
print(total)