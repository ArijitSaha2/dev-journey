# Variables

# Variables are containers for storing data values.

"""Creating Variables

Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.
Example
x = 5
y = "John"
print(x)
print(y)

Variables do not need to be declared with any particular type, and can even change type after they have been set.
Example
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

Casting
If you want to specify the data type of a variable, this can be done with casting.
Example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0 

Get the Type
You can get the data type of a variable with the type() function.
Example
x = 5
y = "John"
print(type(x))
print(type(y)) """

# Mutable - can be changed after creation (list, dict, set)
"""list = [1, 2, 3]
print(l)
list[0] = 3
print(l)

dic = {"food":"Pizza", "num":"23","drink":"Milk"}
print(dic)
dic.pop("food") # Deletes the Key "food". 
print(dic)
dic["area"] = "circle" # Adding a Key-Value pair. New Key-Value pairs are added at the end.

s = {1, 2, 3}
s.remove(1) # self researched. Removes a value from the set.
s.add(99)   # self researched. Adds a new value to the set.
print(s)"""

# Immutable - cannot be changed after creation (tuple, string, int, float)
"""t = (1, 2, 3)
# t[0] = 22   # Will Give error
t = (2, 3, 4) # Entirely New Values doesn't try to replace the original.
print(t)

s = "string" # Original string object created in memory
print(s)
s += "s"     # New string "strings" created, variable s now points to it. Original is gone.
print(s)

i = 10    # Integer - immutable, reassigning creates a new object in memory

f = 1.0   # Float - immutable, same as integer
"""
