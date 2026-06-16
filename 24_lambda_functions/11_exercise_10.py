# Lambda Exercise 10
# Create a list of distances in km = [5, 12, 8, 20, 3]
# Use filter and lambda to keep distances over 6 km
# Use map and lambda to convert those to miles (multiply by 0.621)
# Print the result as a tuple

km = [5, 12, 8, 20, 3]

over_6 = list(filter(lambda o: o > 6, km))

convert_miles = tuple(map(lambda m: m * 0.621, over_6))

print(convert_miles)