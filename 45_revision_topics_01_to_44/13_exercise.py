# Create a Car class.
# Give it the attributes: brand, model, year.
# Create a method called display_info() that prints all three attributes.
# Create two Car objects and call display_info() for each.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model 
        self.year = year 

    def display_info(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}")

car1 = Car("Ferrari", "Laferrari", 2017)
car2 = Car("BMW", "BM21", 2020)

print("-" * 25)
car1.display_info()
print("-" * 25)
car2.display_info()
print("-" * 25)