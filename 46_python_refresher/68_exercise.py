# Exercise 68 — Class Methods and Static Methods

# Task: Create a simple Employee class.
# Requirements
# 1. Create a class attribute called employee_count, initially set to 0.
# 2. Create a constructor that accepts an employee's name.
# 3. Increment employee_count whenever a new employee is created, using a class method.
# 4. Create a @classmethod called get_employee_count() that returns the total number of employees.
# 5. Create a @staticmethod called is_adult(age) that returns True if the age is 18 or above, otherwise False.
# 6. Create two employee objects.
# 7. Display the employee count and test is_adult() with an age of your choice.
# Rules:
# - Use cls in class methods.
# - Don't use self or cls in the static method.
# - No inheritance.

class Employee:

    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.increment_count()

    @classmethod
    def increment_count(cls):
        cls.employee_count += 1

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

    @staticmethod
    def is_adult(age):
        return age >= 18
            
employee1 = Employee("Emily")
employee2 = Employee("Rose")

print(f"Employee count: {Employee.get_employee_count()}")
print(f"Adult?\nAnswer: {employee2.is_adult(23)}")