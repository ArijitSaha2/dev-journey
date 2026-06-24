# Polymorphism Exercise 2
# Create a class Circle with an area() method
# Create a class Square with an area() method
# Create one Circle object and one Square object
# Store them in a list
# Loop through the list and print the result of area()

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Square:
    def __init__(self, sides):
        self.sides = sides

    def area(self):
        return self.sides * self.sides
    
shapes = [Circle(7), Square(5)]

for shape in shapes:
    print(shape.area())