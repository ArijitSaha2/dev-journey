# Exercise 62 — Building a Calculator Module
# Task: Create a calculator using two Python files.

# File 1 — calculator.py

# Create four functions:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# Each function must:
# - Accept two numbers as arguments.
# - Return the calculated result.

# File 2 — 62_exercise.py
# 1. Import calculator.py.
# 2. Ask the user to enter two numbers.
# 3. Call all four functions from the imported module.
# 4. Display the results.
# Requirements:
# - Keep calculation logic inside calculator.py.
# - Keep user input and function calls inside main.py.
# - Use import or from ... import.
# - Handle division by zero.

import calculator

num1 = int(input("Enter a num: "))
num2 = int(input("Enter a num: "))

print(calculator.add(num1, num2))
print(calculator.sub(num1, num2))
print(calculator.Multiply(num1, num2))
print(calculator.Divide(num1, num2))