# Exercise 2
# Create a class called Product.
# Add __init__(name, price).
# Create a property price that returns "$<price>".
# Add a setter that only allows price > 0.
# Create one Product object.
# Change the price and print it.

class Product:

    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def rprice(self):
        return f"{self._name} is ${self._price}"
    
    @rprice.setter
    def rprice(self, price):
        if price > 0:
            self._price = price
        
        else:
            print(f"${price} can not be zero")
        
product1 = Product("Toy set", 1000)

product1.rprice = 0

print(product1.rprice)