# OOP Exercise 8
# Create a class called Car with attributes: make, model, year, speed (default 0)
# Add accelerate() that increases speed by 10 and prints current speed
# Add brake() that decreases speed by 10 (minimum 0) and prints current speed
# Create one car and call both methods a few times

class Car:
    def __init__(self, make, model, year, speed = 0):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print(f"Speed Increased by 10\nCurrent Speed = {self.speed} Model - {self.model}")

    def brake(self):
        if self.speed > 0:
            self.speed -= 10
            print(f"Speed will be Decreased by 10\nCurrent Speed = {self.speed} miles for {self.model}")
            print()
        else:
            print(f"Car Stopped, Speed = {self.speed} miles for {self.model}")

car1 = Car("Made in Germany", "Horizon", 2026, 50)
car2 = Car("Made in America", "LaFerrai", 2002, 0)

car1.brake()
car2.accelerate()