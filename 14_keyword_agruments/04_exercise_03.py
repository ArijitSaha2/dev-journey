# Create a function that calculates the area of a rectangle
# Parameters: length and breadth
# Call it using keyword arguments
# Call it again with arguments in reverse order to prove order doesn't matter
# Print both results

def area_of_rectangle(length, breadth):
    print(f"Area of Rectangle = {length*breadth}")

area_of_rectangle(10, 20)
area_of_rectangle(breadth=20, length=10)