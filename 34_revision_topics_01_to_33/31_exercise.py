# Revision Exercise 31
# Create a class called Animal
# Add a method called speak()
# Create a class Dog that inherits from Animal
# Create one Dog object
# Call speak()

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} Can Speak")

class Dog(Animal):
    pass

dog1 = Dog("Doggy")

dog1.speak()