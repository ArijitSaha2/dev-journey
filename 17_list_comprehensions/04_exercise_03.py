# temperatures = [32, 45, 78, 23, 89, 56, 12, 67, 90, 34]
# Use list comprehension to get only temperatures above 50
# Multiply each of those by 1.8 and add 32 (convert Celsius to Fahrenheit)
# Print the result

temperatures = [32, 45, 78, 23, 89, 56, 12, 67, 90, 34]

above_50 = [temperatures * 1.8 + 32 for temperatures in temperatures if temperatures > 50]

print(above_50)