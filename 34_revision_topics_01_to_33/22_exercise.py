# Revision Exercise 22
# Create a global variable:
# language = "Python"
# Create a function that prints the global variable
# Create a local variable inside the function called language = "English"
# Print both values to demonstrate scope

language = "Python"

def scope():
    language = "English"
    print(f"Local Variable = {language}")

scope()
print(f"Global Variable = {language}")