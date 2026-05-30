# Create a shopping cart function using **kwargs
# Each kwarg is item_name=price
# Print each item and its price
# Calculate and print the total

def shop(**kwargs):
    total = 0
    for name, price in kwargs.items():
        print(f"{name} = {price}")
        total += price
    print(f"Total Cost = {total}")

shop(Smart_Phone = 40000, PC = 150000)