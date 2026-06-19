# Create a class called Phone
# Attributes: brand, model, battery
# Add a method called show_battery()
# Print the battery percentage
# Create two phones and test the method

class Phone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def show_battery(self):
        print(f"Current Battery Percentage = {self.battery}")

phone1 = Phone("Redmi", "X10", "60%")
phone2 = Phone("Apple", "17 Pro MAX", "81%")

phone1.show_battery()
phone2.show_battery()