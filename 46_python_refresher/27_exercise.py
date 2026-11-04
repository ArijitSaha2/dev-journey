# Exercise 27 — Variable Mutability
# Create two variables:
# 1. A string containing "Python".
# 2. A list containing three programming languages.
# Then:
# - Change the string variable to "Java".
# - Add "Python" to the list.
# - Print both variables before and after the changes.

def variable_mutability(**kwargs):
    print(f"Before change {kwargs}")
    print("AFTER")
    kwargs['language'] = "Java"
    kwargs["list_of_languages"].append("Python")
    print(kwargs)

variable_mutability(language = "Python", list_of_languages = ["C#", "C++", "Assembly"])