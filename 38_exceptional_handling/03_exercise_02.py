# Exercise 2
# Ask the user to enter two numbers.
# Print the result of dividing the first number by the second.
# Handle ValueError if the user enters text.
# Handle ZeroDivisionError if the second number is 0.
# Print "Program Ended" using finally.

try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    print(num1 / num2)
except ValueError:
    print("Only Enter Numbers please.")

except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("Program Ended")