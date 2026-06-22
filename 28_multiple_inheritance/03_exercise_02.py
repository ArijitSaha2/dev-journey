# Multiple Inheritance Exercise 2
# Create a class called Flyable with method fly()
# Create a class called Swimmable with method swim()
# Create a class called Diveable with method dive()
# Create a class called Seagull that inherits from Flyable and Swimmable
# Create a class called Penguin that inherits from Swimmable and Diveable
# Create one object from each and test all their methods


class Name:
    def __init__(self, name):
        self.name = name

class Flyable(Name):
    def fly(self):
        print(f"{self.name} can fly")

class Swimmable(Name):
    def swim(self):
        print(f"{self.name} can swim")

class Diveable(Name):
    def dive(self):
        print(f"{self.name} can dive")

class Seagull(Flyable, Swimmable):
    pass

class Penguin(Swimmable, Diveable):
    pass

bird = Seagull("Sea Gang")
pengu = Penguin("Ice Gang")

pengu.swim()
pengu.dive()

bird.fly()
bird.swim()