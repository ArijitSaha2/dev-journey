# Create a function using *args
# It should take any number of numbers
# Print the highest number without using max()

def highest(*args):
    largest = args[0]
    for arg in args:
        if arg > largest:
            largest = arg
    print(f"Highest number in {args} is {largest}")

highest(1, 2, 23, 3, 10)