# Create 3 variables - one string, one integer, one float
# Print the type of each variable using type()
# Reassign the string variable to an integer value
# Print the type again to show it changed
# Create a list and change one of its values
# Create a tuple and try to change a value (comment out the error line and explain why)

a = "apple"
x = 1
b = 1.0 # or 1. same thing

print("Variable a is",type(a))
print("Variable x is",type(x))
print("Variable b is",type(b))

a = 23
print("Changed/Updated variable a =",type(a))

l = [1, 2, 3]
print(l)
l[0] = 'Rose'
print("Changed Value =",l)

t = (1, 2, 3)
# t[0] = 7 # They are immutable meaning cannot be changed once created. Other option is give it entirely new values.
print(t)