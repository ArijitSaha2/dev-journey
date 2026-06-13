# Lambda Exercise 7
# Create a list of numbers = [5, 12, 3, 8, 21, 7, 15]
# Use filter and lambda to keep only numbers greater than 10
# Use map and lambda to square those numbers
# Print both results

numbers = [5, 12, 3, 8, 21, 7, 15]

greater = list(filter(lambda g: g > 10, numbers))

square = list(map(lambda sq: sq*sq, greater))

print(greater)

print(square)