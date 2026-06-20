# OOP Exercise 10
# Create a class called Person
# Attributes: name, age
# Add a method called greet() that prints "Hi, I'm {name} and I'm {age} years old"
# Add a method called is_adult() that prints whether the person is an adult or not (18+)
# Create two person objects and test both methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")

    def is_adult(self):
        if self.age >= 18:
            print("The person is Adult")
        else:
            print("The Person is a child")

person1 = Person("Alicia", 22)
person2 = Person("Diana", 17)

print()
person1.greet()
person1.is_adult()
print()

person2.greet()
person2.is_adult()
print()