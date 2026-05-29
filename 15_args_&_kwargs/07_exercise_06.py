# Create a function using **kwargs
# Accept details about a product (name, price, category, stock)
# Print each detail formatted cleanly
# Add a discount of 10% to the price and print the final price

def product(**kwargs):
    price = kwargs["Unit_Price"]
    discount = price * 0.90
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print(f"Discount 10% off: {discount}")

product(Name = "Dishwasher",
        Unit_Price = 25000,
        Category = "Electronics & Kitchen",
        Stock = "10 Units")