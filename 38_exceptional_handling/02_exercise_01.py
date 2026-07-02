# Exercise 1
# Ask the user to enter a number.
# Print 100 divided by that number.
# Handle ZeroDivisionError.
# Print "Done!" using finally.

try:
    number = int(input("Enter a number: "))
    print(100 / number)
except ZeroDivisionError:
    print("Do not enter 0 for division")
finally:
    print("Done!")