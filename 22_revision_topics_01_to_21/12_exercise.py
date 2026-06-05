# Revision - Functions
# Create a function that takes a name and age as parameters
# If age is 18 or over print "Welcome [name], you are an adult"
# Otherwise print "Sorry [name], you are too young"
# Call the function twice with different values

def func(name , age):
    if age >= 18:
        print(f"Welcome {name}, you are an adult")
    else:
        print (f"Sorry {name}, you are too young")

func("Annie", 17)
func("Angie", 24)