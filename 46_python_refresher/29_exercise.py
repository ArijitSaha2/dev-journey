# Exercise 29 — Arithmetic Operations
# Write a Python program that:
# 1. Takes two numbers and stores them in variables.
# 2. Calculates their:
#    - Addition
#    - Subtraction
#    - Multiplication
#    - Division
#    - Floor division
#    - Modulus
#    - Exponentiation
# 3. Prints each operation and its result.
# Rules:
# - Use variables and arithmetic operators.
# - No loops required.
# - No functions required.
# - Use your own numbers.
# Topic focus: Arithmetic operators (+, -, *, /, //, %, **).

def arithmetic_operations(a, b):
    print(f"Addition - {a + b}")
    print(f"Subtraction - {a - b}")
    print(f"Multiplication - {a * b}")
    print(f"Division - {a / b}")
    print(f"Floor division - {a // b}")
    print(f"Modulus - {a % b}")
    print(f"Exponentiation - {a ** b}")

arithmetic_operations(5, 4)