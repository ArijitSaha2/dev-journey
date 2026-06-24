# Polymorphism Exercise 1
# Create a class Animal with a speak() method
# Create a class Dog that inherits Animal and overrides speak()
# Create a class Cat that inherits Animal and overrides speak()
# Store a Dog and Cat object in a list
# Loop through the list and call speak() on each object

class Animal:
    def speak(self):
        print(f"{self.name} Says hes a Donkey")

class Dog(Animal):
    def speak(self):
        print(f"Says Woof Woof!")

class Cat(Animal):
    def speak(self):
        print(f"Says MEOW!")

class Donkey(Animal):
    def __init__(self, name):
        self.name = name

animals = [Dog(), Cat(), Donkey("John")]

for animal in animals:
    animal.speak()