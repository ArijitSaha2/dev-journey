# Exercise 007 — Lambda with Conditional Expression
# Write a lambda expression that:
# - Accepts one number.
# - Returns "Even" if the number is even.
# - Returns "Odd" otherwise.
# - Store it in a variable called check_number.
# - Test it with 7 and 12.
# Expected output:
# Odd
# Even

num = int(input("Enter num: "))

check_number = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_number(num))