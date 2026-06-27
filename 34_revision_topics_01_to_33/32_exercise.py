# Revision Exercise 32
# Create a class called Employee
# Add a constructor with name
# Create a method called work()
# Create a class Manager that inherits from Employee
# Override the work() method
# Create one Manager object
# Call work()

class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print("Work In Progress")

class Manager(Employee):
    def work(self): # Overide
        print("Work not in Progress")

manager1 = Manager("Ariana")

manager1.work()