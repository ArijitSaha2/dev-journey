# Revision Exercise 16
# Create a function called greet()
# It should have a default parameter: name = "Guest"
# Print "Hello, <name>"
# Call the function once without an argument
# Call it again with your own name

def greet(name = "Guest"):
    print(f"Hello, {name}")

greet()
greet("Kaylee")