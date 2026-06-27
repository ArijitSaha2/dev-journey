# Revision Exercise 30
# Create a class called Student
# Add a class variable called school = "ABC High School"
# Create a constructor with name
# Create one Student object
# Print the student's name
# Print the school name

class Student:

    school = "ABC High School"

    def __init__(self, name):
        self.name = name

student1 = Student("Aria")

print(student1.name)
print(Student.school)