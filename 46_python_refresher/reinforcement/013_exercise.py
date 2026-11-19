# Exercise 013 — Class Methods

# Your task:
# - Create a class called Employee.
# - Add a class attribute company = "TechCorp".
# - Create a class method called change_company(cls, new_company).
# - Update the company name using the class method.
# - Print the company name before and after the change.
# Expected output:
# TechCorp
# Google

class Employee:

    company = "TechCorp"

    @classmethod
    def change_company(cls, new_company):
        print(f"Old Company name: {cls.company}")

        cls.company = new_company
        print(f"New Company name: {cls.company}")

Employee.change_company("Google")