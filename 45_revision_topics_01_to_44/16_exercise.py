# Exercise 16
# Create a Person class with a name.
# Create an Employee class that inherits from Person.
# Use super() to initialize the name.
# Give Employee a job attribute.
# Create one Employee object.
# Print the employee's name and job.

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, job):
        super().__init__(name)
        self.job = job

employee1 = Employee("Aria", "Hair Stylist")

print(employee1.name)
print(employee1.job)