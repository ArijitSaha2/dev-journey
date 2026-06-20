# OOP Exercise 9
# Create a class called Circle
# Attributes: radius
# Add area() that prints the area (pi = 3.14159)
# Add circumference() that prints the circumference
# Create two circle objects and test both methods

class Circle:

    def __init__(self, model, radius):
        self.model = model
        self.radius = radius


    def area(self):
        pi = 3.14159
        result = pi*self.radius**2        
        print(f"Area of Circle {self.model} is {result}")

    def circumference(self):
        pi = 3.14159
        result2 = 2*pi*self.radius
        print(f"Circumference of Circle {self.model} is {result2}")

circle1 = Circle(1, 7)
circle2 = Circle(2, 10)

circle1.area()
circle1.circumference()
print()
circle2.area()
circle2.circumference()