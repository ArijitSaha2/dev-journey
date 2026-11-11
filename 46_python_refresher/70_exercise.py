# Exercise 70 — Shape Calculator
# What this tests: Inheritance, super() and method overriding.

# Task: Create a parent class Shape and a child class Rectangle.

# Requirements:
# 1. Shape constructor accepts a name.
# 2. Add a method describe() that prints the shape's name.
# 3. Rectangle inherits from Shape.
# 4. Its constructor accepts name, width and height.
# 5. Use super() to initialize the name.
# 6. Override describe() to display the name, width and height.
# Rules:
# - No additional classes.
# - No static methods or class methods.
# - No properties or decorators.
# - No notes.

class Shape:

    def __init__(self, name):
        self.name = name

    def describe(self):
        print(f"It is a {self.name}")

class Rectangle(Shape):

    def __init__(self, name, width, height):
        self.width = width
        self.height = height
        super().__init__(name)

    def describe(self):
        print(f"It is a {self.name}\nWidth: {self.width}\nHeight: {self.height}")

sha = Shape("Circle")
rec = Rectangle("Rectangle", 4, 10)

sha.describe()
print()
rec.describe()