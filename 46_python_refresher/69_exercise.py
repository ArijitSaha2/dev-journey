# Exercise 69 — Properties and Decorators
# What this tests: Using @property, a setter and a deleter to control access to an object's attribute.

# Task: Create a Product class.

# Requirements:
# 1. Constructor accepts a product name and price.
# 2. Store the price using _price.
# 3. Create a getter using @property called price.
# 4. Create a setter that prevents prices below 0.
# 5. Create a deleter that deletes the price attribute.
# 6. Create a product object with price 500.
# 7. Display its price, change it to 750, and display it again.
# Rules:
# - Use @property for the getter.
# - Use @price.setter for the setter.
# - Use @price.deleter for the deleter.
# - Don't use inheritance.

class Product: 

    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def price(self):
        return f"Price: {self._price}"

    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            print("Price cannot be 0")

    @price.deleter
    def price(self):
        del self._price
        print(f"Price attribute has been deleted")

toy = Product("Superman", 500)
print(toy.price)

toy.price = 750  # Calls @price.setter

print(f"Updated {toy.price}")