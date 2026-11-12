# Exercise 71 — Safe Calculator
# What this tests: try, except, else and finally.

# Create a simple division calculator.

# Requirements:
# 1. Ask the user for two numbers.
# 2. Handle ValueError if the user enters non-numeric input.
# 3. Handle ZeroDivisionError if the second number is zero.
# 4. Use else to display the result when no exception occurs.
# 5. Use finally to display "Calculator finished." regardless of the outcome.
# Rules:
# - Use separate except blocks.
# - Don't use if to check for division by zero.
# - No unnecessary functions or classes.

try: 
    user1 = int(input("Enter number: "))
    user2 = int(input("Enter number: "))
    division = user1 / user2

except ValueError:
    print("You have to enter number in number!")

except ZeroDivisionError:
    print("Do not enter 0!")

else:
    print("Great No errors and heres the answer Below")
    print(f"Division = {division}")

finally:   
    print(f"Calculator finished")