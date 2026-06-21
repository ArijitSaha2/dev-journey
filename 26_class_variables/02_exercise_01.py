# Class Variables Exercise 1
# Create a class called Dog
# Class variables: species = "Canis familiaris", total_dogs = 0
# Instance variables: name, breed
# Increment total_dogs every time a new dog is created
# Create 3 dogs and print total_dogs and the species using the class name

class Dog:
    species = "Canis Familiaris"
    total_dogs = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Dog.total_dogs += 1

dog1 = Dog("Popo", "Kansa")
dog2 = Dog("Po", "Kronko")
dog3 = Dog("Lont", "Prek")

print(f"There are {Dog.total_dogs} dogs in the nursery and they belong to {Dog.species} Species.")