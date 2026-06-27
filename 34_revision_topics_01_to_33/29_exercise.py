# Revision Exercise 29
# Create a class called Car
# Add a constructor with brand and year
# Create a method called display_info()
# Return the brand and year
# Create one Car object
# Print the returned information

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
            return f"Brand: {self.brand}, Year: {self.year}"
    
car1 = Car("LaFerrari", 2016)

print(car1.display_info())