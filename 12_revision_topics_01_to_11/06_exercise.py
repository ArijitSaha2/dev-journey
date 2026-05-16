# Create a function that takes a name and age
# If age is under 18 print "Hello [name], you are a minor"
# If age is 18 or above print "Hello [name], you are an adult"
# Use f-string and .capitalize() on the name

def task():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age < 18:
        print(f"Hello {name.capitalize()}, You are a minor")
    elif age >= 18:
        print(f"Hello {name.capitalize()}, You are an adult")


task()