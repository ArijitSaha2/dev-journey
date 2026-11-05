# Exercise 36 — Conditional Expressions

# Write a program that takes a temperature as input and determines whether the weather is:
# - "Hot" if temperature is 30 or above.
# - "Warm" if temperature is between 20 and 29.
# - "Cold" if temperature is below 20.
# Use a conditional expression (ternary operator) to determine the result.

def temperatures(temp):

    result = "Hot" if temp >= 30 else "Warm" if temp >= 20 else "Cold"

    return result

temp = int(input("Enter temperature: "))
print(temperatures(temp))