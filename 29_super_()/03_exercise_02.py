# Create a class Person with a name attribute
# Create a class Employee that inherits Person
# Employee should also have a salary attribute
# Use super().__init__() to initialize name
# Create one Employee object
# Print its name
# Print its salary

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

employee = Employee("Anna", 90000)

print(f"Name: {employee.name:>6}")
print(f"Salary: {employee.salary}")