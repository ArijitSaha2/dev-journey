# Exercise 49 — Sets
# Write a program that:
# 1. Takes five values from the user and stores them in a set.
# 2. Displays the set.
# 3. Adds another value using add().
# 4. Removes a value using remove().
# 5. Displays the final set.
# Requirements:
# - Use a function.
# - Use a loop to collect values.
# - Don't hardcode the values.
# Remember: sets automatically remove duplicates, and they are unordered.

def sets(values_5):
    print(values_5)

    for_add = input("Enter a value to add: ")
    values_5.add(for_add)

    for_remove = input("Enter a value to remove: ")
    values_5.remove(for_remove)

    print(f"Final Set = {values_5}")


s = set()
for x in range(1, 6):
    y = input("Enter Values: ")
    s.add(y)

sets(s)