# Exercise 59 — Lambda Functions
# Write a lambda function that:
# 1. Accepts two numbers.
# 2. Returns their product.
# 3. Store the lambda in a variable.
# 4. Call it using two user-input values.
# 5. Display the result.
# No regular def function for this exercise.

x = int(input("Enter number: "))
y = int(input("Enter number: "))

add = lambda a, b: (a * b)

print(f"Multiply: {add(x, y)}")