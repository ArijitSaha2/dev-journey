# Create 3 variables: name, price, quantity
# Print them in a formatted receipt style
# Price should show 2 decimal places with comma separator
# Right align the prices with 10 spaces

name = "OnePunchManFigurine"

price = 10

quantity = "1"

print(f"Name of the toy is: {name:^21}")
print(f"Price of the toy is: {price:>10,.2f}")
print(f"How much toys are required: {quantity:^2}")