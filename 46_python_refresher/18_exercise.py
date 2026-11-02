# Exercise 18 — Product Price Filter
# Given:
# products = {"Laptop": 55000, "Mouse": 500, "Keyboard": 1500, "Monitor": 12000, "USB": 300}

# Write a function that returns a new dictionary containing products priced below ₹2000.
# Expected output:
# {"Mouse": 500, "Keyboard": 1500, "USB": 300}

# Rules:
# - Use a function, loop and conditional.
# - No dictionary comprehension.

def product_price_filter(products):
    new_dict = {}
    for stuff in products:
        if products[stuff] < 2000:
            new_dict[stuff] = products[stuff]
    
    return new_dict
print(product_price_filter({"Laptop": 55000, "Mouse": 500, "Keyboard": 1500, "Monitor": 12000, "USB": 300}))