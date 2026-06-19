# OOP Exercise 5
# Create a class called Student
# Attributes: name, grade, passing_grade, passed (boolean)
# Add a method called check_pass() that checks if grade >= passing_grade and prints pass/fail result
# Create two students with different grades and test the method

class Student:
    def __init__(self, name, grade, passing_grade, passed):
        self.name = name
        self.grade = grade
        self.passing_grade = passing_grade
        self.passed = passed

    def check_pass(self):
        self.passing_grade = 30
        if self.grade >= self.passing_grade:
            print(f"Congratulations {self.name}! {self.grade} out of 100, YOU PASSED\nPassing_GRADE = {self.passing_grade}")
        else:
            print(f"{self.name}! {self.grade} out of 100, YOU Fail\nPassing_GRADE = {self.passing_grade}")

student1 = Student("Rosaria", 85, 30, True)
student2 = Student("John", 29, 30, False)

student1.check_pass()
student2.check_pass()