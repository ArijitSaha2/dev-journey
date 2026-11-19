# Exercise 019 — super() and Parent Constructor Initialisation
# Your task:
# - Create a parent class called Person.
# - Give it an __init__ method that accepts name and stores it.
# - Create a child class called Employee that inherits from Person.
# - Give Employee its own __init__ method accepting name and salary.
# - Use super() to initialise the parent's name attribute.
# - Create an employee object and print both attributes.
# Expected output:
# Name: Alex
# Salary: 50000

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        self.salary = salary
        super().__init__(name)

em1 = Employee("Alex", 50000)

print(f"Name: {em1.name}")
print(f"Salary: {em1.salary}")