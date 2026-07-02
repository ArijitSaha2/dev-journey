# Exercise 1
# Create a decorator called greet.
# Before the function runs, print "Welcome!".
# Create a function say_name(name) that prints the name.
# Decorate the function with @greet.
# Call it with your name.

def greet(func):
    def wrapper(*args, **kwargs):
        print("Welcome!")
        func(*args, **kwargs)
    return wrapper

@greet
def say_name(name):
    print(name)

say_name("Lisa")