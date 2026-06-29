# Exercise 3
# Create a class called Laptop.
# Add __init__(brand, price).
# Add __gt__(other) to compare the prices of two laptops.
# Create two Laptop objects.
# Print the result of comparing them using >.

class Laptop:

    def __init__(self, brand, price):
        self.brand = brand 
        self.price = price

    def __gt__(self, other):
        return self.price > other.price
    
laptop1 = Laptop("Lenovo", 79999)
laptop2 = Laptop("Alienware", 99000)

print(laptop2 > laptop1)