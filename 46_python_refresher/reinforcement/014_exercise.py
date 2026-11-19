# Exercise 014 — Properties (Getter)
# Your task:
# - Create a class called Employee.
# - Store an employee's name in a private attribute _name.
# - Create a getter using @property to access the name.
# - Create an employee object and print its name using the property.
# Expected output:
# Employee name: Alex 

class Employee: 

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return f"Employee name: {self._name}"

Em1 = Employee("Alex")

print(Em1.name)