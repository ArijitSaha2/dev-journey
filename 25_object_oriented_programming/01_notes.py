# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) uses to design the structure and layout of an object

from car import Car

car1 = Car("LaFerrari", 2021, "Red", False)
car2 = Car("Pagani", 2026, "White", True)

car1.describe()

# Class — the blueprint that defines what attributes and methods objects of this type will have.

# Object — one actual instance created from a class, with its own real data.

# Constructor (__init__) — runs automatically when an object is created, and assigns initial values to that object using self.

# self — refers to whichever specific object is currently being worked with. It's what lets each object keep its own separate data.

# Attribute — a variable that belongs to an object (like self.name).

# Method — a function that belongs to a class and can act on an object's data via self.