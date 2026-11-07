# Exercise 48 — Tuples
# Write a program that:
# 1. Takes five values from the user and stores them in a tuple.
# 2. Displays the tuple.
# 3. Displays the first and last elements.
# 4. Displays the number of occurrences of a value using count().
# 5. Finds the index of a value using index().
# Requirements:
# - Use a function.
# - Use a loop to collect the values.
# - Don't hardcode the values.

def tuples(values):
    print(f"{values}\nFirst element = {values[0]}\nLast element = {values[-1]}")

    a = input("Enter a value to search for its total occurrences: ")
    print(f"Total occurrences: {values.count(a)}")

    find_index = input("Enter a value to find its index: ")
    print(f"{values.index(find_index)}")


l = []
for x in range(1, 6):
    y = input("Enter values: ")
    l.append(y)

t = tuple(l)

tuples(t)