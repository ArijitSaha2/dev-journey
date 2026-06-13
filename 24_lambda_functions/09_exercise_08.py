# Lambda Exercise 8
# numbers = [1, 2, 3, 4, 5]
# Use map and lambda to double each number
# Print the result as a tuple

numbers = [1, 2, 3, 4, 5]

double = tuple(map(lambda d: d+d, numbers))

print(double)