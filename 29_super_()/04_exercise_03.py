# Create a class Shape with a color attribute
# Create a class Circle that inherits Shape
# Circle should also have a radius attribute
# Use super().__init__() to initialize color
# Create one Circle object
# Print its color
# Print its radius

class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

circle = Circle("Red", 5)

print(f"Color of circle: {circle.color}")
print(f"Radius of circle: {circle.radius}")