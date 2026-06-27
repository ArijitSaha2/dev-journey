# Revision Exercise 33
# Create a class called Bird
# Create a method called move()
# Print "Bird is moving"
# Create a class Eagle that inherits from Bird
# Override move()
# Print "Eagle is flying"
# Create one Bird object and one Eagle object
# Call move() on both

class Bird:
    def move(self):
        print("Bird is moving")

class Eagle(Bird):
    def move(self):
        print("Eagle is Flying")

bird1 = Bird()
eagle1 = Eagle()

bird1.move()
eagle1.move()