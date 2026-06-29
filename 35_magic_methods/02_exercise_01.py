# Exercise 1
# Create a class called Student.
# Add __init__(name, marks).
# Add __str__() to return "<name> scored <marks> marks".
# Create one Student object and print it.

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Name: {self.name}, Scored: {self.marks} marks"
    
student1 = Student("Aria", 77)

print(student1)