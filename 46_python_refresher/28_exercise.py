# Exercise 28 — Type Casting
# Given the following values:
# age = "21"price = 499.99 quantity = "3"

# Perform these operations:
# 1. Convert age into an integer.
# 2. Convert price into an integer.
# 3. Convert quantity into an integer.
# 4. Convert age into a string again.
# 5. Print each converted value and its data type using type().
# Rules:
# - Use Python's built-in casting functions.
# - No loops required.
# - You may use a function if you find it useful.
# Topic focus: int(), float(), str().

def type_casting(**kwargs):

    kwargs['age'] = int(kwargs['age'])
    print(f"Age - {kwargs['age']}")
    print(type(kwargs['age']))
    print()

    kwargs['price'] = int(kwargs['price'])
    print(f"Price - {kwargs['price']}")
    print(type(kwargs['price']))
    print()

    kwargs['quantity'] = int(kwargs['quantity'])
    print(f"Quantity - {kwargs['quantity']}")
    print(type(kwargs['quantity']))
    print()

    kwargs['age'] = str(kwargs['age'])
    print(f"Age - {kwargs['age']}")
    print(type(kwargs['age']))

type_casting(age = "21", price = 499.99, quantity = "3")