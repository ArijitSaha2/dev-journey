# class variables = Shared among all instances of a class 
#                    Defined outside the constructor
#                    Allow you to share data among all objects created from that class

class Student:
    class_year = 2026       # CLASS VARIABLE - shared by all Student objects
    num_students = 0        # CLASS VARIABLE - tracks total count across all objects

    def __init__(self, name, age):
        self.name = name    # INSTANCE VARIABLE - unique to each object
        self.age = age      # INSTANCE VARIABLE - unique to each object
        Student.num_students += 1  # modifying CLASS VARIABLE via class name, not self

student1 = Student("Spongebob", 30)  # INSTANCE of Student class
student2 = Student("Patrick", 35)    # INSTANCE of Student class
student3 = Student("Squidwart", 55)  # INSTANCE of Student class
student4 = Student("Sandy", 27)      # INSTANCE of Student class

print(f"My Graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)