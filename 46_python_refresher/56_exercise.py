# Exercise 56 — Function Arguments
# Write a function that accepts product details and calculates the final bill.
# 1. Accept the product name and price as positional arguments.
# 2. Accept a quantity with a default value of 1.
# 3. Accept a discount using a keyword argument.
# 4. Use *args to accept additional charges.
# 5. Use **kwargs to accept additional product details.
# 6. Display the final bill.
# Requirements:
# - Take user input for the product name, price and quantity.
# - Use all five argument types.
# - Keep the calculation inside the function.

def func_argument(*args, **kwargs):

    print(f"Summary")
    print(f"Product Name: {args[0]}")

    pr_ice = args[1] * kwargs['Quantity']
    print(f"Price: {pr_ice}$")

    print(f"Additional Charges(Taxes): {args[2]} $")

    print(f"Quantity: {kwargs['Quantity']}")

    print(f"Age rating: {kwargs['Age_rating']}")

    tax = args[2]
    with_tax = pr_ice + tax
    discount_amount = with_tax * kwargs['Discount'] / 100
    final_price = with_tax - discount_amount

    print(f"Lucky offer {kwargs['Discount']}% off for 7 days!!!!")
    print(f"Discounted price: {final_price}$")
    print()

print(f"Enter Product Specs As Specified....!")

product_name = input("Enter Product Name: ")

Price = int(input("Enter Product Price: "))

additional_charges = 200

Quantity = int(input("Enter Quantity: "))
print()

print(f"Checking Quantity.....")
if Quantity >= 1:
    print(f"You added {Quantity} of {product_name}'s in bag")
else:
    print("Quantity must be atleast 1 to progress with order! Thank you.")
    exit() 

print()

func_argument(product_name, Price, additional_charges, Quantity = Quantity, Discount = 50, Age_rating = "18 and above!")
