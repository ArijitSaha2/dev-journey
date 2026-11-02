# Exercise 17 — Inventory Checker
# You are given a dictionary representing product stock:
# inventory = {"Laptop": 8, "Mouse": 25, "Keyboard": 4, "Monitor": 12, "Headphones": 3}

# Write a function that returns a list containing the names of products with fewer than 10 units in stock.
# Expected output:
# ["Laptop", "Keyboard", "Headphones"]

# Rules:
# - Use a function and dictionary iteration.
# - Use a regular loop and conditional.
# - No dictionary or list comprehension.

def inventory_checker(inventory):
    list_of_names = []
    for product in inventory:
        if inventory[product] < 10:
            list_of_names.append(product)

    return list_of_names
print(inventory_checker({"Laptop": 8, "Mouse": 25, "Keyboard": 4, "Monitor": 12, "Headphones": 3}))