# Exercise 012 — Static Methods
# Your task:
# - Create a class called Employee.
# - Add a static method called is_valid_salary(salary).
# - Return True if the salary is greater than 0, otherwise return False.
# - Test it with salaries 50000 and -1000.
# Expected output:
# True
# False

class Employee:

    @staticmethod
    def is_valid_salary(salary):
        result = True if salary > 0 else False
        return result

print(Employee.is_valid_salary(50000))
print(Employee.is_valid_salary(-1000))