# Duck Typing Exercise 1
# Create a class Flight with a fly() method
# Create a class Bird that inherits Flight
# Create a class Plane that inherits Flight
# Create one Bird object and one Plane object
# Store them in a list
# Loop through the list and call fly()

class Flight:

    is_alive = False

    def fly(self):
        print("Flying")
    
    def land(self):
        print("On the ground")

    

class Bird(Flight):
    is_alive = True

class Plane(Flight):
    pass

li = [Bird(), Plane()]

for items in li:
    items.fly()
    items.land()
    print(items.is_alive)