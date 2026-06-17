# OOP Exercise 1
# Create a class called Dog
# It should have attributes: name, breed, age
# Add a method called bark() that prints "{name} says Woof!"
# Create two dog objects with different details
# Call the bark method on both

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    

    def bark(self):
        print(f"{self.name}, says Woof!")

dog1 = Dog("Jonky", "Hell Hound", 10000)
dog2 = Dog("Chungus", "Hell chompers", 50000)


dog1.bark()
dog2.bark()