# Lambda Exercise 3
# Create a list of prices = [100, 250, 450, 80, 320, 175]
# Use map and lambda to apply a 10% discount to all prices
# Use filter and lambda to keep only prices above 200 after discount
# Print both results

prices = [100, 250, 450, 80, 320, 175]

discount_10 = list(map(lambda num: num * 0.9, prices))

above_200 = list(filter(lambda nums: nums > 200, discount_10))

print(discount_10)
print(above_200)