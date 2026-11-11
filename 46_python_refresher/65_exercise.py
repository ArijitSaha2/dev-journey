# Exercise 65 — Inheritance and super()
# Task: Create a basic employee management system using inheritance.

# Requirements:
# 1. Create a parent class called Employee.
# - Constructor accepts name and salary.
# - Create a method display_info() to display both attributes.
# 2. Create a child class called Manager.
# - Inherit from Employee.
# - Add an additional attribute called department.
# - Use super() to initialise the parent attributes.
# 3. Override display_info() in Manager.
# - Display the employee's name, salary and department.
# 4. Create one Employee object and one Manager object.
# 5. Call display_info() on both objects.
# Rules:
# - Use inheritance and super().
# - Demonstrate method overriding.
# - Don't duplicate the parent's constructor logic in the child class.

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee Name = {self.name}\nEmployee Salary = {self.salary}")


class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        print(f"Employee Name = {self.name}\nEmployee Salary = {self.salary}\nEmployee Department = {self.department}")

employe1 = Employee("Andre", 80000)
manager1 = Manager("Holly", 90000, "Marketing")

employe1.display_info()
print()
manager1.display_info()