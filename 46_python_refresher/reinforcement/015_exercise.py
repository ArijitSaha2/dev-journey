# Exercise 015 — Properties (Setter)
# Your task:
# - Create a class called Employee.
# - Store the employee's name in _name.
# - Create a getter using @property.
# - Create a setter using @name.setter to update the employee's name.
# - Create an employee object, print the original name, change it, and print the updated name.
# Expected output:
# Alex
# John

class Employee:

    def __init__(self, name):
        self._name = name

    @property 
    def name(self):
        return f"Employee name: {self._name}"

    @name.setter
    def name(self, new_name):
        self._name = new_name


em1 = Employee("Alex")
print(em1.name)

em1.name = "John"
print(em1.name)