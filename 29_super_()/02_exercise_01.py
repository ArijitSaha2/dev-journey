# Create a class Animal with a name attribute
# Create a class Dog that inherits from Animal
# Dog should also have a breed attribute
# Use super().__init__() to initialize name
# Create one Dog object
# Print its name
# Print its breed

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed
        super().__init__(name)

dog = Dog("Hell Hound", "Helios")

print(dog.name)
print(dog.breed)