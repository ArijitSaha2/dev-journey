# Exercise 4
# Create a module named calculator.py containing:
# - add(a, b)
# - subtract(a, b)
#
# In another file:
# - Import the calculator module.
# - Ask the user for two numbers.
# - Ask the user to choose '+' or '-'.
# - Call the appropriate function.
# - Display the result using an f-string.
# - If the operator is invalid, print "Invalid operator".

import calculator

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

operation = input("Choose + or -: ")

if operation == "+":
    print(f"Add: {calculator.add(num1, num2)}")
elif operation == "-":
    print(f"Subtract: {calculator.subtract(num1, num2)}")
else:
    print(f"{operation} is an invalid operator")