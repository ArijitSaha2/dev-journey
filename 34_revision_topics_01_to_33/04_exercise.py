# Revision Exercise 4
# Take two numbers as input
# Convert both to integers
# Print their sum
# Print whether the first number is greater than the second using an if-else statement

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

merge = num1, num2

print(f"Sum of given numbers = {sum(merge)}")

if num1 > num2:
    print(f"{num1} is greater then {num2}")
else:
    print(f"{num2} is greater then {num1}")