# Create a Temperature class.
# Create a static method that accepts a Celsius value and returns Fahrenheit.
# Create a class method that prints the class name.
# Call both methods without creating an object.

class Temperature:
    @staticmethod
    def temp_converter_c_to_f(celsius):
        print(f"Fahrenheit: {(celsius * 1.8) + 32}")

    @classmethod
    def class_name(cls):
        print(cls.__name__)

Temperature.temp_converter_c_to_f(30)
Temperature.class_name()