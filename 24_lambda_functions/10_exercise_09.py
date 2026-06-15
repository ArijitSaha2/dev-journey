# Lambda Exercise 9
# Create a list of numbers = [10, 25, 30, 45, 50]
# Use map and lambda to find 15% of each number
# Print the result as a tuple

numbers = [10, 25, 30, 45, 50]

find_15 = tuple(map(lambda f: f * .15, numbers))

print(find_15)