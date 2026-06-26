# Revision Exercise 18
# Create a function that uses *args
# It should accept any number of integers
# Return the largest number without using max()

def biggie(*args):
    largest = args[0]
    for x in args:
        if x > largest:
            largest = x
    return f"Largest Number: {largest}"

print(biggie(1,4,10,6,4))