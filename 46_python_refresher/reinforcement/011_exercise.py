# Exercise 011 — Instance Methods
# Your task:
# - Create a class called Employee.
# - Add an __init__ method that accepts name and salary.
# - Store both values as instance attributes.
# - Create an instance method called display_details() that prints the employee's name and salary.
# - Create two employee objects with different details.
# - Call display_details() on both objects.

# Expected output:

# Name: Alex
# Salary: 40000

# Name: John
# Salary: 55000

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}\nSalary: {self.salary}")

worker1 = Employee("Ariana", 80000)
worker2 = Employee("Rosita", 78000)

print("Employee Names and Salary Below: \n")
worker1.display_details()
print()
worker2.display_details()