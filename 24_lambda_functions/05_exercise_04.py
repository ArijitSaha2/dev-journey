# Lambda Extra Exercise
# Create a list of temperatures in Celsius = [0, 20, 37, 100]
# Use map and lambda to convert all to Fahrenheit (multiply by 1.8 and add 32)
# Use filter and lambda to keep only temperatures above 50 Fahrenheit
# Print both results

celsius = [0, 20, 37, 100]

fahrenheit = list(map(lambda temperature: temperature * 1.8 + 32, celsius))

result_50above = list(filter(lambda values: values > 50, fahrenheit))

print("Fahrenheit = ",fahrenheit)
print("Above 50 =   ",result_50above)