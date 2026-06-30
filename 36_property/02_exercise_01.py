# Exercise 1
# Create a class called Person.
# Add __init__(name, age).
# Create a property age that returns "<age> years old".
# Add a setter that only allows age >= 0.
# Create one Person object.
# Change the age and print it.

class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return f"{self._age} years old"
    
    @age.setter
    def age(self, ages):
        if ages >= 0:
            self._age = ages
        else:
            print(f"{self._name} must not be negavtive")

person1 = Person("Julie", 21)

person1.age = 22

print(person1.age)