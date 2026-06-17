# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) uses to design the structure and layout of an object

from car import Car

car1 = Car("LaFerrari", 2021, "Red", False)
car2 = Car("Pagani", 2026, "White", True)

car1.describe()