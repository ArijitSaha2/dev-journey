# Exercise 44 — String Formatting
# Write a program that:
# 1. Takes a name and age as input.
# 2. Displays a sentence containing both values using an f-string.
# 3. Displays the age in a formatted message using .format().
# Requirements:
# - Use a function.
# - Don't hardcode the name or age.
# - Practise both formatting methods.

def string_formatting(name, age):
    print(f"My name is {name} and I am {age}")
    print("My name is {} and I am {}.".format(name, age))

n1 = input("Enter name: ")
a1 = int(input("Enter age: "))
string_formatting(n1, a1)