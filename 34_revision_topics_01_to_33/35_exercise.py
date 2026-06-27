# Revision Exercise 35
# Create a class MathTools. Add a static method add(a, b) that returns their sum.
# Call the method using the class and print the result.

class MathTools:
    @staticmethod
    def add(a, b):
        merge = a, b
        return (f"Sum: {sum(merge)}")

print(MathTools.add(3, 4))