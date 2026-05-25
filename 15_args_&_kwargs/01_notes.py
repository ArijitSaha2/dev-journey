# *args    = allows you to pass multiple non-key arguments 
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#            1. positional 2. default 3. keyword 4. ARBITRARY

"""
*args: 
# *args packs multiple positional arguments into a TUPLE
# you can pass as many arguments as you want, no fixed number needed
# Example: add(1,2,3) or add(1,2,3,4,5) both work
# When to use *args: when you don't know how many values will be passed

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3 ,4))

def display_name(*args):
    for arg in args:
        print(arg, end =" ")

display_name("Dr", "Spongebob", "Harold","Squarepants", "III")
"""

"""
**kwargs:
# **kwargs packs multiple keyword arguments into a DICTIONARY
# each argument must be passed as key=value
# you access them using .items() to get key-value pairs
# When to use **kwargs: when you don't know how many key=value pairs will be passed

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.",
              apt="100",
              city="Detroit",
              state="MI",
              zip="54321")
"""