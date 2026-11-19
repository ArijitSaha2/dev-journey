# Exercise 016 — Properties (Deleter)
# Your task:
# - Create a class called Employee.
# - Store the employee's name in _name.
# - Create a getter using @property.
# - Create a deleter using @name.deleter.
# - The deleter should delete the _name attribute.
# - Create an employee object, print the name, delete the property, and confirm the attribute no longer exists.
# Expected output:
# Alex
# False


class Employee:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return f"Employee Name: {self._name}"

    @name.deleter
    def name(self):
        del self._name

emp1 = Employee("Alex")
print(emp1.name)

del emp1.name
print(hasattr(emp1, "_name"))