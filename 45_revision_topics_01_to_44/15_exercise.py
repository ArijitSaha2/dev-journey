# Create a Vehicle class with a drive() method.
# Create a Car class that inherits from Vehicle.
# Create a Bike class that inherits from Vehicle.
# Call drive() using both objects.

class Vehicle:
    def __init__(self, name):
        self.name = name

    def drive(self):
        print(f"A {self.name} Starts Driving")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

car1 = Car("Car")
car1.drive()

bike1 = Bike("Bike")
bike1.drive()