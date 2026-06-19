# OOP Exercise 6
# Create a class called Rectangle
# Attributes: width, height
# Add a method called area() that prints the area
# Add a method called perimeter() that prints the perimeter
# Create two rectangle objects and test both methods

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area = self.width * self.height
        print(f"Area of Rectangle = {area}")
    
    def perimeter(self):
        peri = 2 * (self.width + self.height)
        print(f"Perimeter of Rectangle = {peri}")

rectangle1 = Rectangle(4, 2)
rectangle1.area()
rectangle1.perimeter()

rectangle2 = Rectangle(8, 5)
rectangle2.area()
rectangle2.perimeter()