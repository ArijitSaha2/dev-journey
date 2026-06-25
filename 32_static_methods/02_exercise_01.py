# Static Methods Exercise 1
# Create a class Temperature
# Add a static method called celsius_to_fahrenheit()
# The method should accept a Celsius temperature
# Return the Fahrenheit value
# Call the static method using the class name
# Print the result

class Temperature:
    
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 1.8) + 32
        return f"{fahrenheit} fahrenheits"
    
print(Temperature.celsius_to_fahrenheit(35))