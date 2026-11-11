# Exercise 64 — Classes and Objects
# Task: Create a Student class.
# Requirements:

# Create a constructor accepting a student's name, age and course.
# Store these as instance attributes.
# Create a method called display_info() that displays the student's details.
# Create two different student objects with different information.
# Call display_info() for both objects.

# Rules:
# Use a class and constructor.
# Use instance attributes and instance methods.
# No inheritance yet.

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"Student's Name: {self.name}\nAge: {self.age}\nCourse: {self.course}")

student1 = Student("Bella", 21, "C")
student2 = Student("Jess", 22, "Java")

student1.display_info()
print()
student2.display_info()