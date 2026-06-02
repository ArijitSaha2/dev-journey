# Oral Question
x = 10

def my_func():
    x = 20
    print(x)  # prints local x

my_func()
print(x)  # prints global x

### ANSWER ###
"""Inside my_funct the x used is the local variable and that is printed first, it doesn't exist outside the function
   The global x is printed using the variable that exists outside the function but if the local value didn't exist the global x would've been used (Because LEGB)"""
