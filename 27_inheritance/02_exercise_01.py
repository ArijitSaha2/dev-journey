# Inheritance Exercise 1
# Create a parent class called Vehicle
# Attributes: make, model, year
# Method: describe() that prints all attributes
# Create two child classes: Car and Motorcycle
# Car adds a method: honk() that prints "Beep beep!"
# Motorcycle adds a method: wheelie() that prints "{model} does a wheelie!"
# Create one Car and one Motorcycle object, call describe() and their unique methods

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        print(f"Make in {self.make},\nModel = {self.model},\nYear = {self.year}")

class Car(Vehicle):
    def honk(self):
        print("Beep beep!")

class Motorcycle(Vehicle):
    def wheelie(self):
        print(f"{self.model} does a wheelie")

car = Car("Germany" , "Toyota", 2010)
bike = Motorcycle("Germany", "BMW", 2030)

car.describe()
car.honk()
print()

bike.describe()
bike.wheelie()