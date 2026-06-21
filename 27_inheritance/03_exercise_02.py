# Inheritance Exercise 2
# Create a parent class called Shape
# Attributes: name
# Method: describe() that prints "This is a {name}"
# Create two child classes: Circle and Rectangle
# Circle adds: radius attribute in constructor, area() method
# Rectangle adds: width, height attributes in constructor, area() method
# Create one object from each and test all methods

class shape:
    def __init__(self, name):
        self.name = name
    
    def describe(self):
        print(f"This shape is {self.name}")

class Circle(shape):
    def area(self, radius):
        pi = 3.142
        self.radius = radius
        print(f"Area of Circle = {pi*self.radius**2}")

class Rectangle(shape):
    def area(self, width, height):
        self.width = width
        self.height = height
        print(f"Area of rectangle = {self.width * self.height}")

circle = Circle("Circle")
circle.describe()
circle.area(7)

rectangle = Rectangle("Rectangle")
rectangle.describe()
rectangle.area(5, 10)