# Ask the user to enter two numbers.
# Divide the first number by the second.
# Handle:
# - ValueError
# - ZeroDivisionError
# Print the result if no exception occurs.

try: 
    n1 = int(input("Enter Number1: "))
    n2 = int(input("Enter Number2: "))
    print(n1 / n2)
except ValueError:
    print("Enter numbers only")
except ZeroDivisionError:
    print("A number can not be divided by zero")
except Exception:
    print("Something went wrong")