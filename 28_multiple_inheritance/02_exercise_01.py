# Multiple Inheritance Exercise 1
# Create a parent class called Animal with attribute name and method breathe()
# Create two child classes: Swimmer and Runner
# Swimmer adds: swim() method
# Runner adds: run() method
# Create a class called Duck that inherits from both Swimmer and Runner
# Create a Duck object and test all methods including breathe()

class Animal:
    def __init__(self, name):
        self.name = name

    def breath(self):
        print(f"{self.name} is breathing and alive")

class Swimmer(Animal):
    def swim(self):
        print(f"{self.name} can swim")

class Runner(Animal):
    def run(self):
        print(f"{self.name} can run")

class Duck(Swimmer, Runner):
    pass

duck = Duck("Quaccky")

duck.breath()
duck.swim()
duck.run()