# Create a list of 3 products with prices
# Print each product with its price formatted to 2 decimal places
# Add a + sign for positive prices
# Use comma separator for prices over 1000

products = ["Toys", "Clothes", "Smartphones"]
prices = [15 , 40, 1000]

for i in range(3):
    print(f"The {products[i]} Cost ${prices[i]:+,.2f}")