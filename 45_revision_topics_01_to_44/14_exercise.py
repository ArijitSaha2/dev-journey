# Exercise 14
# Create a Student class.
# Create a class variable called school and set it to a school name.
# Use __init__() to give each student a name.
# Create three Student objects with different names.
# Create a display_info() method that prints the student's name and school.
# Call display_info() for all three students.

class Student:
    school = "ABC Schools"

    def __init__(self, name):
        self.name = name
    
    def display_info(self):
        print(f"Name of Student: {self.name}\nSchool Name: {self.school}")

stud1 = Student('Aria')
stud2 = Student('Ariana')
stud3 = Student('Cassie')

students = [stud1, stud2, stud3]

for student in students:
    print("-" * 30)
    student.display_info()

print("-" * 30)