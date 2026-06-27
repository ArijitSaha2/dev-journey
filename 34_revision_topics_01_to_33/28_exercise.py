# Revision Exercise 28
# Create a class called Dog
# Add a constructor with name and breed
# Create a method called bark()
# Print "<name> says Woof!"
# Create one Dog object
# Call bark()

class Dog:
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed

    def bark(self):
        print(f"{self.name} Says Woof!")

dog1 = Dog("Cupcake Destroyer", "Bull-Stallion")
dog1.bark()