# Polymorphism Exercise 3
# Create a class Dog with a move() method
# Create a class Fish with a move() method
# Create one Dog object and one Fish object
# Store them in a list
# Loop through the list and call move()

class Dog:
    def __init__(self, type_animal):
        self.type_animal = type_animal

    def move(self):
        return f"{self.type_animal} Runs away"
    
class Fish:
    def __init__(self, type_animalia):
        self.type_animalia = type_animalia

    def move(self):
        return f"{self.type_animalia} is hunting"
    
ani_box = [Dog("DOGGO"), Fish("Shark")]

for animal in ani_box:
    print(animal.move())