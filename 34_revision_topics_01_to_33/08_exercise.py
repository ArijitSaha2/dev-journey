# Revision Exercise 8
# Take a number as input
# Use a for loop
# Print the multiplication table from 1 to 10
# Example: 5 x 1 = 5

num = int(input("Enter a number: "))

for x in range(1, 11):
    print(f"{num} x {x} = {num * x}")