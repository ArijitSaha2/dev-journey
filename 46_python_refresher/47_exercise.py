# Exercise 47 — List Methods
# Write a program that:
# 1. Takes five names from the user and stores them in a list.
# 2. Adds another name using append()(the user enters the name to add).
# 3. Removes a name using remove()(the user enters the name to remove).
# 4. Sorts the list alphabetically.
# 5. Displays the final list.
# Requirements:
# - Use a function.
# - Don't hardcode the names.
# - Use list methods.

def list_methods(names):

    y = input("Enter 1 more name: ")
    names.append(y)
    print(f"List of names: {names}")

    z = input("Enter 1 name you want removed: ")
    names.remove(z)
    print(f"Updated list after removal: {names}")

    names.sort()
    print(f"List in alphabetical order: {names}")


print("Enter 5 names of your choice!")
lis = []
for name in range (1, 6):
    x = input("Enter name: ")
    lis.append(x)

list_methods(lis)