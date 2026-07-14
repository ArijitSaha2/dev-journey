# Create Dog, Cat, and Bird classes.
# Give each a speak() method.
# Create one function that accepts any object and calls speak().
# Pass all three objects to the function.

class Dog:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} is Barking!")

class Cat:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} is MEOWING!!!!")

class Bird:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} is SCREAMING!!")

dog1 = Dog("John Marston")
cat1 = Cat("Tom")
bird1 = Bird("Sparrow")

animals = [dog1, cat1, bird1]

def make_sound(animal):
    animal.speak()

print("-" * 30)
for animal in animals:
    make_sound(animal)
    print("-" * 30)